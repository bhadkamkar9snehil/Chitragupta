#!/usr/bin/env python3
"""Deterministic forward handoff: investigator (default board) -> reviewer
(l2-review board). No LLM ever performs this hop -- the investigator's only
terminal action is a plain kanban_complete on its OWN board; this script
does the actual cross-board choreography.

Why this exists: real evidence 2026-09-04 traced the single largest
failure category this project has found (48% of all session logs showing
"[could not complete/block ... unknown id]") to the SAME task object
changing owner mid-flow on a shared board -- a later retry/nudge then
collides with an ownership it no longer holds. Splitting investigator and
reviewer onto separate boards removes that collision surface entirely: an
investigator retry can, at worst, hit its own already-terminal card.

Design pattern: this is the Transactional Outbox pattern (the investigator's
committed "done" task IS the outbox record -- durable, already committed by
Hermes itself) plus the Idempotent Consumer pattern for the receiving side
(Hermes's own --idempotency-key on `kanban create`, keyed on the source
task's id, so a re-run of this script can never create a duplicate review
card even if it crashes mid-run and gets retried).

What this does, every tick:
1. List every 'done' task on the default board assigned to an investigator
   profile (l2-gemma, l2-investigator) whose kanban_complete metadata has a
   run_id/ticket_id/response_type/reply_text (a real investigation result,
   not some other kind of done task).
2. For each not yet bridged (tracked in a local state file, belt-and-
   suspenders alongside the idempotency key), create a task on l2-review
   assigned to the reviewer, body carrying the same run_id/ticket_id/
   metadata the old kanban_request_review handoff used to carry, plus an
   explicit back-reference (investigation_task_id) since native cross-board
   kanban_link isn't supported.

Usage (intended as a --no-agent cron job, every ~2-3 min):
    python kanban_forward_bridge.py [--dry-run]
"""
import argparse
import json
import shlex
import shutil
import subprocess
import sys
from pathlib import Path

STATE_PATH = Path(__file__).parent / "kanban_bridged_forward.json"
# This script is deployed both ways: run manually from Windows (where
# 'wsl' exists and must wrap the call into the Ubuntu environment) and as
# a native WSL cron job under l2-investigator (where 'wsl' does not exist
# on PATH at all -- confirmed live 2026-09-04, FileNotFoundError -- and
# 'hermes' is directly callable). Detect once at import time instead of
# hardcoding one path.
_HAS_WSL = shutil.which("wsl") is not None
REVIEW_BOARD = "l2-review"
DEFAULT_BOARD = "default"
INVESTIGATOR_PROFILES = {"l2-gemma", "l2-investigator"}
REVIEWER_BY_INVESTIGATOR = {
    "l2-gemma": "l2-gemma-verifier",
    "l2-investigator": "l2-qwen-verifier",
}


def run_hermes(args, timeout=30):
    """args is a plain list of real argv tokens (NO manual shell quoting --
    that was a real bug: quoting for the wsl+bash -lc path corrupted
    arguments on the native-WSL path, where subprocess.run(list) already
    handles argument boundaries without a shell)."""
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


def list_done_investigator_tasks():
    r = run_hermes(["kanban", "--board", DEFAULT_BOARD, "list", "--status", "done", "--json"])
    if r.returncode != 0:
        print(f"WARNING: could not list default board done tasks: {r.stderr.strip()[:300]}")
        return []
    tasks = json.loads(r.stdout)
    return [t for t in tasks if (t.get("assignee") or "") in INVESTIGATOR_PROFILES]


def get_runs(task_id, board):
    r = run_hermes(["kanban", "--board", board, "runs", task_id, "--json"])
    if r.returncode != 0:
        return []
    return json.loads(r.stdout)


def extract_investigation_metadata(runs, investigator_profile):
    """The investigator's own terminal kanban_complete run carries the real
    finding -- take the LAST one under its own profile (in case of any
    internal retries within the same task)."""
    candidates = [
        r for r in runs
        if r.get("status") == "done"
        and r.get("profile") == investigator_profile
        and r.get("metadata")
    ]
    if not candidates:
        return None
    return candidates[-1]["metadata"]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    tasks = list_done_investigator_tasks()
    if not tasks:
        print("No done investigator tasks found.")
        return

    state = load_state()
    bridged = 0

    for t in tasks:
        task_id = t["id"]
        investigator_profile = t.get("assignee") or ""
        if task_id in state:
            continue

        runs = get_runs(task_id, DEFAULT_BOARD)
        metadata = extract_investigation_metadata(runs, investigator_profile)
        if not metadata or not metadata.get("run_id") or not metadata.get("response_type") or not metadata.get("reply_text"):
            # Not every 'done' investigator task is a real investigation
            # result (e.g. it could be a housekeeping task) -- skip quietly,
            # don't mark bridged so a later real completion on retry is
            # still caught, but don't spam a warning every tick either.
            continue

        reviewer_profile = REVIEWER_BY_INVESTIGATOR.get(investigator_profile, "l2-gemma-verifier")
        ticket_id = metadata.get("ticket_id") or ""
        title = f"REVIEW: {t.get('title', task_id)}"
        body = (
            f"investigation_task_id: {task_id}\n"
            f"run_id: {metadata['run_id']}\n"
            f"ticket_id: {ticket_id}\n\n"
            f"Investigator's proposed response (from {investigator_profile}, board={DEFAULT_BOARD}):\n"
            f"{json.dumps(metadata, indent=2, default=str)}\n"
        )

        print(f"{'[DRY RUN] ' if args.dry_run else ''}Bridging {task_id} -> {REVIEW_BOARD} (reviewer={reviewer_profile})")
        if args.dry_run:
            continue

        r = run_hermes([
            "kanban", "--board", REVIEW_BOARD, "create",
            title,
            "--body", body,
            "--assignee", reviewer_profile,
            "--skill", "xstudio-l2-draft-verifier",
            "--skill", "xstudio-sql-write-discipline",
            "--idempotency-key", f"fwd-{task_id}",
            "--max-runtime", "15m",
        ], timeout=30)
        if r.returncode != 0:
            print(f"    FAILED to create review card: {r.stderr.strip()[:300]}")
        else:
            print(f"    Created review card.")
            state.add(task_id)
            bridged += 1

    if not args.dry_run:
        save_state(state)
    print(f"\n{len(tasks)} done investigator task(s) checked, {bridged} newly bridged to {REVIEW_BOARD}.")


if __name__ == "__main__":
    main()
