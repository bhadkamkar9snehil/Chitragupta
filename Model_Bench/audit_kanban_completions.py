#!/usr/bin/env python3
"""Deterministic, no-LLM audit: never trust a Kanban 'done' status on its
own -- verify the real SQL state actually matches before treating a review
as genuinely finished.

Why this exists: confirmed 2026-09-03 that Kanban's own protocol-violation
guard has a real, currently-open gap -- NousResearch/hermes-agent issue
#32746, "Kanban dispatcher accepts kanban_complete with zero tool calls (no
tool-evidence gate)". A worker can call kanban_complete with NO prior tool
calls at all, and the dispatcher accepts it as a clean completion. This is
not a prompt-wording problem on our side -- it's an upstream gap. Confirmed
live: l2-gemma-verifier called kanban_complete twice in a row with zero
--publish-response calls in either session log, and Kanban marked both
'done' with no violation recorded.

This script is the compensating control: for every task a *-verifier
profile marked 'done', check whether the real Hermes_L2_Response_Trn_Tbl row
for that run_id actually reflects a genuine publish matching what the
reviewer claimed (non-stale ReplyText, not the safety-net's canned rescue
text). If it doesn't, the "done" status is a false positive -- reopen the
task via kanban_block so a human (or a fixed pipeline later) can see it
needs real attention, rather than letting it sit silently marked complete.

Usage (intended as a --no-agent cron job, every ~5-10 min):
    python audit_kanban_completions.py --server 10.2.6.204 [--dry-run]
"""
import os
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
import pyodbc

SAFETY_NET_MARKER = "did not publish a response within the expected time window"


def find_done_tasks():
    result = subprocess.run(
        ["wsl", "-d", "Ubuntu", "--", "bash", "-lc", "hermes kanban list --status done --json"],
        capture_output=True, text=True, timeout=30,
    )
    if result.returncode != 0:
        print(f"WARNING: could not list done tasks: {result.stderr.strip()[:300]}")
        return []
    return json.loads(result.stdout)


def extract_run_id(body):
    for line in (body or "").splitlines():
        line = line.strip()
        if line.startswith("run_id:"):
            return line.split(":", 1)[1].strip()
    return None


def check_real_state(cur, run_id):
    cur.execute(
        "SELECT ProcessStatus, ResponseType, ReplyText, CompletedOn "
        "FROM Hermes_L2_Response_Trn_Tbl WHERE ID = ?",
        run_id,
    )
    row = cur.fetchone()
    if row is None:
        return False, "no matching Hermes_L2_Response_Trn_Tbl row exists for this run_id at all"
    process_status, response_type, reply_text, completed_on = row
    if process_status not in ("COMPLETED", "WAITING_USER"):
        return False, f"ProcessStatus is {process_status!r}, not terminal -- was never actually published"
    if not response_type or not reply_text or not reply_text.strip():
        return False, "ResponseType or ReplyText is empty -- nothing was actually written"
    if SAFETY_NET_MARKER in reply_text:
        return False, "ReplyText is the safety net's canned rescue text, not a real finding -- reviewer never actually published"
    return True, None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--server", default="10.2.6.204")
    ap.add_argument("--database", default="XStudio_Helpdesk")
    ap.add_argument("--username", default="sa")
    ap.add_argument("--password", default=os.environ.get("MSSQL_MCP_PASSWORD"))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    done_tasks = find_done_tasks()
    if not done_tasks:
        print("No 'done' tasks found.")
        return

    conn = pyodbc.connect(
        f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={args.server};DATABASE={args.database};"
        f"UID={args.username};PWD={args.password};TrustServerCertificate=yes"
    )
    try:
        cur = conn.cursor()
        false_positives = 0
        for t in done_tasks:
            run_id = extract_run_id(t.get("body"))
            if not run_id:
                print(f"  {t['id']}: no run_id found in body, skipping")
                continue
            ok, reason = check_real_state(cur, run_id)
            if ok:
                print(f"  {t['id']} (run {run_id}): OK, genuinely published")
                continue
            false_positives += 1
            print(f"  {t['id']} (run {run_id}): FALSE POSITIVE -- {reason}")
            if args.dry_run:
                print(f"    [DRY RUN] Would comment the discrepancy on the task")
                continue
            # kanban's own CLI has no "reopen a done task" verb -- block/
            # unblock only operate on the active lifecycle (ready/running/
            # review/blocked), confirmed live 2026-09-03 ("cannot block"
            # on an already-done task). A durable comment is the correct,
            # honest record here; whether to re-attempt the underlying
            # SQL ticket is a separate human decision, not something this
            # audit should silently force through a raw UPDATE.
            comment = subprocess.run(
                ["wsl", "-d", "Ubuntu", "--", "bash", "-lc",
                 f"hermes kanban comment {t['id']} \"AUDIT: this task was marked done, but the live ticket "
                 f"was never actually published ({reason}) -- confirmed via Hermes_L2_Response_Trn_Tbl, not "
                 f"narration. Kanban's own kanban_complete has no tool-evidence gate (NousResearch/hermes-agent "
                 f"issue #32746) so this false completion was accepted without a protocol_violation. Needs "
                 f"human review; run_id {run_id} is already SQL-terminal and cannot be re-published normally.\""],
                capture_output=True, text=True, timeout=30,
            )
            if comment.returncode != 0:
                print(f"    FAILED to comment: {comment.stderr.strip()[:300]}")
            else:
                print(f"    Commented on the task with the discrepancy for human review.")

        print(f"\n{len(done_tasks)} 'done' task(s) checked, {false_positives} false positive(s).")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
