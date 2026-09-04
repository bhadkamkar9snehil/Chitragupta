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
import shutil
import subprocess
import sys
from pathlib import Path

# 2026-09-05: this script used to connect via pyodbc directly. Broke live
# after a `hermes update` changed which Python interpreter/environment
# cron scripts run under -- the new one has the pyodbc *package* installed
# in some paths but not the system ODBC driver manager
# (ImportError: libodbc.so.2), exactly the gap every other script in this
# project already routes around by shelling out to
# Hermes_Orchestrator.py --query via the Windows Python interpreter
# instead of importing pyodbc in-process. Matching that pattern here too
# so this script doesn't depend on which environment happens to be running
# it.
_HAS_WSL = shutil.which("wsl") is not None
ORCHESTRATOR_PYTHON = sys.executable if _HAS_WSL else r"/mnt/c/Python314/python.exe"
# 2026-09-05: was Path(__file__).parent.parent -- correct only when this
# script runs from its Model_Bench source location (one level below the
# project root), silently wrong once deployed to
# ~/.hermes/profiles/<profile>/scripts/ (two levels below a completely
# different root). Confirmed live: this made the deployed copy unable to
# reach Hermes_Orchestrator.py at all, and since ORCHESTRATOR_PYTHON is
# always a Windows interpreter (native or via /mnt/c/... from WSL), the
# path it needs is always the Windows one regardless of where this script
# itself was copied to.
ORCHESTRATOR_PATH = r"C:\Users\Admin\Documents\Office\AIHelpdesk\Hermes_Orchestrator.py"

SAFETY_NET_MARKER = "did not publish a response within the expected time window"


def run_hermes(args_list, timeout=30):
    if _HAS_WSL:
        import shlex
        cmd = ["wsl", "-d", "Ubuntu", "--", "bash", "-lc", "hermes " + shlex.join(args_list)]
    else:
        cmd = ["hermes"] + args_list
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)


def find_done_tasks():
    result = run_hermes(["kanban", "list", "--status", "done", "--json"])
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


def check_real_state(args, run_id):
    cmd = [
        ORCHESTRATOR_PYTHON, str(ORCHESTRATOR_PATH),
        "--server", args.server, "--database", args.database,
        "--username", args.username, "--password", args.password,
        "--query",
        "SELECT ProcessStatus, ResponseType, ReplyText, CompletedOn "
        f"FROM Hermes_L2_Response_Trn_Tbl WHERE ID = '{run_id}'",
    ]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    if r.returncode != 0:
        return False, f"query failed: {r.stderr.strip()[:200]}"
    try:
        rows = json.loads(r.stdout)
    except json.JSONDecodeError:
        return False, f"could not parse query output: {r.stdout[:200]}"
    if not rows:
        return False, "no matching Hermes_L2_Response_Trn_Tbl row exists for this run_id at all"
    row = rows[0]
    process_status = row.get("ProcessStatus")
    response_type = row.get("ResponseType")
    reply_text = row.get("ReplyText")
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

    false_positives = 0
    for t in done_tasks:
        run_id = extract_run_id(t.get("body"))
        if not run_id:
            print(f"  {t['id']}: no run_id found in body, skipping")
            continue
        ok, reason = check_real_state(args, run_id)
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
        comment = run_hermes([
            "kanban", "comment", t["id"],
            f"AUDIT: this task was marked done, but the live ticket "
            f"was never actually published ({reason}) -- confirmed via Hermes_L2_Response_Trn_Tbl, not "
            f"narration. Kanban's own kanban_complete has no tool-evidence gate (NousResearch/hermes-agent "
            f"issue #32746) so this false completion was accepted without a protocol_violation. Needs "
            f"human review; run_id {run_id} is already SQL-terminal and cannot be re-published normally.",
        ])
        if comment.returncode != 0:
            print(f"    FAILED to comment: {comment.stderr.strip()[:300]}")
        else:
            print(f"    Commented on the task with the discrepancy for human review.")

    print(f"\n{len(done_tasks)} 'done' task(s) checked, {false_positives} false positive(s).")


if __name__ == "__main__":
    main()
