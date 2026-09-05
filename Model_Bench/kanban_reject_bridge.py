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
import os
import re
import shlex
import shutil
import subprocess
import sys
from pathlib import Path

STATE_PATH = Path(__file__).parent / "kanban_bridged_reject.json"
# Deployed both from Windows (needs the wsl wrapper) and as a native WSL
# cron job (no 'wsl' binary on PATH there, confirmed live 2026-09-04).
_HAS_WSL = shutil.which("wsl") is not None
ORCHESTRATOR_PYTHON = sys.executable if _HAS_WSL else r"/mnt/c/Python314/python.exe"
ORCHESTRATOR_PATH = r"C:\Users\Admin\Documents\Office\AIHelpdesk\Hermes_Orchestrator.py"
SQL_SERVER = "10.2.6.204"
SQL_DATABASE = "XStudio_Helpdesk"
SQL_USERNAME = "sa"
SQL_PASSWORD = os.environ.get("MSSQL_MCP_PASSWORD")
# 2026-09-05: reject->rework was an unbounded loop -- a ticket that keeps
# hitting the SAME underlying mistake (wrong column name, unverified
# claim) just got a fresh rework card every time, forever, at real
# compute cost, with the native block-recurrence-breaker never applying
# because each rework is a NEW kanban task id, not the same one re-
# blocked. Reusing AttemptNo -- already tracked per-ticket by
# Hermes_L2_Get_Candidate_Tickets_Usp's own claim logic, no new counter
# needed -- to cap this: after this many attempts on the SAME ticket with
# no valid published response, escalate to the human L3 queue instead of
# creating another rework card. The existing L3-exclusion in
# Hermes_L2_Get_Candidate_Tickets_Usp then keeps it from ever being
# reclaimed while that escalation sits open.
MAX_ATTEMPTS_BEFORE_ESCALATION = 3
# 2026-09-04 (later): single board now -- see ticket_scout.py's header for
# why the two-board split (REVIEW_BOARD/DEFAULT_BOARD) was retired in
# favor of native --parent gating on one board.
REVIEWER_PROFILES = {"l2-gemma-verifier", "l2-qwen-verifier"}
INVESTIGATOR_BY_REVIEWER = {
    "l2-gemma-verifier": "l2-gemma",
    "l2-qwen-verifier": "l2-investigator",
}


def _base_orchestrator_args():
    """MSSQL_MCP_PASSWORD lives in the WINDOWS environment -- visible to
    ORCHESTRATOR_PYTHON (always a Windows interpreter, native or via
    /mnt/c/... from WSL) automatically, but NOT to this script's own
    process when it runs as WSL-native python3 (confirmed live: empty).
    Only pass --password when we can actually see it locally; otherwise
    omit it and let Hermes_Orchestrator.py's own argparse default (same
    env var, read on the Windows side where it genuinely exists) resolve
    it correctly."""
    args = ["--server", SQL_SERVER, "--database", SQL_DATABASE, "--username", SQL_USERNAME]
    if SQL_PASSWORD:
        args += ["--password", SQL_PASSWORD]
    return args


def run_orchestrator_query(sql):
    """Read-only SELECT via Hermes_Orchestrator.py --query (never a direct
    pyodbc import here -- see audit_kanban_completions.py's own 2026-09-05
    note for why that broke silently once deployed)."""
    cmd = [ORCHESTRATOR_PYTHON, ORCHESTRATOR_PATH, *_base_orchestrator_args(), "--query", sql]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    if r.returncode != 0:
        return None
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        return None


def get_attempt_count(ticket_id):
    rows = run_orchestrator_query(
        "SELECT COUNT(DISTINCT AttemptNo) AS Cnt FROM Hermes_L2_Response_Trn_Tbl "
        f"WHERE TicketID = '{ticket_id}' AND IsDeleted = 0"
    )
    if not rows:
        return 0
    return rows[0].get("Cnt", 0)


def escalate_repeated_failure(run_id, ticket_id, reason, attempt_count):
    root_cause = (
        f"{attempt_count} investigation attempts made on this ticket, all rejected by review "
        f"without ever reaching a publishable response. Most recent objection: {reason}"
    )
    # Fail the run first (so it stops looking "active" and eligible for
    # its own staleness retry), THEN escalate for human visibility --
    # Hermes_L2_Log_Blocked_Escalation_Usp is visibility-only (does not
    # touch Complaint_Mst_Tbl or require an active run) -- built 2026-09-05
    # for the genuine-capability-block case, reused here for the same
    # "needs a human, stop auto-retrying" signal via a different trigger.
    # A huge --retry-after-minutes is cosmetic: Hermes_L2_Get_Candidate_
    # Tickets_Usp's own L3-exclusion is what actually stops re-polling
    # while the escalation stays open, not this retry window.
    subprocess.run([
        ORCHESTRATOR_PYTHON, ORCHESTRATOR_PATH, *_base_orchestrator_args(),
        "--fail-run", "--run-id", run_id,
        "--error-message", f"Escalated to L3 after {attempt_count} failed attempts.",
        "--retry-after-minutes", "999999",
    ], capture_output=True, text=True, timeout=30)

    r = subprocess.run([
        ORCHESTRATOR_PYTHON, ORCHESTRATOR_PATH, *_base_orchestrator_args(),
        "--escalate-blocked", "--run-id", run_id, "--ticket-id", ticket_id,
        "--block-reason", root_cause,
    ], capture_output=True, text=True, timeout=30)
    if r.returncode != 0:
        print(f"    FAILED to escalate: {r.stderr.strip()[:300]}")
    return r.returncode == 0


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

        if ticket_id:
            attempt_count = get_attempt_count(ticket_id)
            if attempt_count >= MAX_ATTEMPTS_BEFORE_ESCALATION:
                print(f"{'[DRY RUN] ' if args.dry_run else ''}{task_id}: ticket {ticket_id} has "
                      f"{attempt_count} attempts, all rejected -- escalating to L3 instead of another rework")
                if not args.dry_run:
                    if escalate_repeated_failure(run_id or "unknown", ticket_id, reason, attempt_count):
                        state.add(task_id)
                        bridged += 1
                continue

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
