#!/usr/bin/env python3
"""Deterministic reject handoff: reviewer (l2-review board) -> investigator
(default board) rework. No LLM performs this hop -- the reviewer's only two
terminal actions are kanban_complete (approve) or kanban_block (reject with
a reason); this script does the actual cross-board choreography for the
reject path, mirroring kanban_forward_bridge.py's outbox/idempotent-consumer
design.

Why kanban_block, not kanban_request_changes: kanban_request_changes is a
same-board reassignment primitive (Hermes's own docs: "Review feedback
never creates, unblocks, requeues, or otherwise mutates a task" outside
that mechanism) -- it doesn't fit a cross-board design and was the
mechanism most tied to the original ownership-collision bug this whole
split is meant to eliminate. kanban_block already means "I can't finish
this as-is, needs input" -- reusing it for "reject, send back for rework"
is a natural fit and keeps the reviewer's tool surface to exactly two
well-understood verbs.

What this does, every tick:
1. List every 'blocked' task on the l2-review board assigned to a reviewer
   profile.
2. For each not yet bridged, create a rework task on the default board
   assigned back to the original investigator, body carrying the
   reviewer's objection plus the original run_id/ticket_id.

Usage (intended as a --no-agent cron job, every ~2-3 min):
    python kanban_reject_bridge.py [--dry-run]
"""
import argparse
import json
import re
import shlex
import shutil
import subprocess
from pathlib import Path

STATE_PATH = Path(__file__).parent / "kanban_bridged_reject.json"
# Deployed both from Windows (needs the wsl wrapper) and as a native WSL
# cron job (no 'wsl' binary on PATH there, confirmed live 2026-09-04).
_HAS_WSL = shutil.which("wsl") is not None
# 2026-09-04 (later): single board now -- see ticket_scout.py's header for
# why the two-board split (REVIEW_BOARD/DEFAULT_BOARD) was retired in
# favor of native --parent gating on one board.
REVIEWER_PROFILES = {"l2-gemma-verifier", "l2-qwen-verifier"}
INVESTIGATOR_BY_REVIEWER = {
    "l2-gemma-verifier": "l2-gemma",
    "l2-qwen-verifier": "l2-investigator",
}


def run_hermes(args, timeout=30):
    """args is a plain list of real argv tokens, no manual shell quoting."""
    if _HAS_WSL:
        cmd = ["wsl", "-d", "Ubuntu", "--", "bash", "-lc", "hermes " + shlex.join(args)]
    else:
        cmd = ["hermes"] + args
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)


def load_state():
    if STATE_PATH.exists():
        return set(json.loads(STATE_PATH.read_text(encoding="utf-8")))
    return set()


def save_state(state):
    STATE_PATH.write_text(json.dumps(sorted(state)), encoding="utf-8")


def list_blocked_reviewer_tasks():
    r = run_hermes(["kanban", "list", "--status", "blocked", "--json"])
    if r.returncode != 0:
        print(f"WARNING: could not list blocked tasks: {r.stderr.strip()[:300]}")
        return []
    tasks = json.loads(r.stdout)
    return [t for t in tasks if (t.get("assignee") or "") in REVIEWER_PROFILES]


def get_block_reason(task_id, reviewer_profile):
    r = run_hermes(["kanban", "runs", task_id, "--json"])
    if r.returncode != 0:
        return None
    runs = json.loads(r.stdout)
    blocks = [
        x for x in runs
        if x.get("outcome") == "blocked" and x.get("profile") == reviewer_profile
    ]
    if not blocks:
        return None
    return blocks[-1].get("summary") or "(no reason recorded)"


def extract_source_ids(body):
    run_id = re.search(r"run_id:\s*([A-F0-9-]+)", body or "", re.IGNORECASE)
    ticket_id = re.search(r"ticket_id:\s*([A-F0-9-]+)", body or "", re.IGNORECASE)
    investigation_task_id = re.search(r"investigation_task_id:\s*(\S+)", body or "")
    return (
        run_id.group(1) if run_id else None,
        ticket_id.group(1) if ticket_id else None,
        investigation_task_id.group(1) if investigation_task_id else None,
    )


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    tasks = list_blocked_reviewer_tasks()
    if not tasks:
        print("No blocked reviewer tasks found.")
        return

    state = load_state()
    bridged = 0

    for t in tasks:
        task_id = t["id"]
        reviewer_profile = t.get("assignee") or ""
        if task_id in state:
            continue

        reason = get_block_reason(task_id, reviewer_profile)
        if not reason:
            continue

        run_id, ticket_id, investigation_task_id = extract_source_ids(t.get("body"))
        investigator_profile = INVESTIGATOR_BY_REVIEWER.get(reviewer_profile, "l2-gemma")
        title = f"REWORK: {t.get('title', task_id)}"
        body = (
            f"run_id: {run_id or 'unknown'}\n"
            f"ticket_id: {ticket_id or 'unknown'}\n"
            f"prior_investigation_task_id: {investigation_task_id or 'unknown'}\n"
            f"review_task_id: {task_id}\n\n"
            f"REVIEWER OBJECTION (from {reviewer_profile}):\n{reason}\n\n"
            f"Fix exactly this problem -- re-fetch the ticket via --get-ticket-context "
            f"(do not trust old context, it may be stale), address the specific objection "
            f"above, then follow the normal investigation procedure to a fresh kanban_complete."
        )

        print(f"{'[DRY RUN] ' if args.dry_run else ''}Bridging reject {task_id} (investigator={investigator_profile})")
        if args.dry_run:
            continue

        r = run_hermes([
            "kanban", "create",
            title,
            "--body", body,
            "--assignee", investigator_profile,
            "--skill", "xstudio-l2-ticket-workflow",
            "--skill", "xstudio-sql-write-discipline",
            "--idempotency-key", f"rej-{task_id}",
            "--max-runtime", "20m",
        ], timeout=30)
        if r.returncode != 0:
            print(f"    FAILED to create rework card: {r.stderr.strip()[:300]}")
        else:
            print(f"    Created rework card.")
            state.add(task_id)
            bridged += 1

    if not args.dry_run:
        save_state(state)
    print(f"\n{len(tasks)} blocked reviewer task(s) checked, {bridged} newly bridged (rework card created).")


if __name__ == "__main__":
    main()
