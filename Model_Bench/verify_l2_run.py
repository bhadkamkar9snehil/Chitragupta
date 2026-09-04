#!/usr/bin/env python3
"""Postcondition verifier for a Hermes_L2 run -- checks real database state,
never the agent's own narration of what it did.

Why this exists: a real 2026-09-03 incident had the agent's final response
say "A question was published to the ticket" when the actual database row
was untouched (ProcessStatus still INVESTIGATING, ReplyText NULL). This is
a documented failure class ("execution hallucination" / "tool calling
hallucination" -- the model narrates an action without actually emitting
the tool call for it). No amount of prompt wording fixes this reliably;
the fix is external verification against ground truth, per standard agent-
harness design: "the system must never issue a retry without first
consulting a postcondition verifier... judged by tool-observed state and
downstream artifacts, not the agent's narration."

Usage:
    python verify_l2_run.py <run_id> [--server 10.2.6.204]

Exit 0 = genuinely published (ProcessStatus terminal, ReplyText present,
ResponseType set). Exit 1 = NOT actually done, regardless of what the
cron output transcript claims -- prints exactly what's missing.
"""
import os
import argparse
import sys

sys.path.insert(0, str(__file__.rsplit("\\", 2)[0] if "\\" in __file__ else __file__.rsplit("/", 2)[0]))

import pyodbc

# Real values observed live in Hermes_L2_Response_Trn_Tbl.ProcessStatus
# (checked against actual data 2026-09-03, not guessed): COMPLETED, FAILED,
# INVESTIGATING, WAITING_USER. Both COMPLETED and WAITING_USER represent a
# genuinely-published response (WAITING_USER = a QUESTION response awaiting
# the requester's reply, still a real publish, not a stall).
TERMINAL_STATUSES = {"COMPLETED", "WAITING_USER"}


def verify(run_id: str, server: str, database: str = "XStudio_Helpdesk",
           username: str = "sa", password: str = None) -> tuple[bool, list[str]]:
    conn = pyodbc.connect(
        f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};"
        f"UID={username};PWD={password};TrustServerCertificate=yes"
    )
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT ProcessStatus, ResponseType, ReplyText, IsResolved, "
            "RequiresUserInput, EscalateToL3, ErrorMessage, CompletedOn "
            "FROM Hermes_L2_Response_Trn_Tbl WHERE ID = ?",
            run_id,
        )
        row = cur.fetchone()
        if row is None:
            return False, [f"No Hermes_L2_Response_Trn_Tbl row exists for run_id {run_id!r} at all"]

        process_status, response_type, reply_text, is_resolved, requires_input, escalate, error_msg, completed_on = row
        problems = []
        if process_status not in TERMINAL_STATUSES:
            problems.append(f"ProcessStatus is {process_status!r}, not a terminal status "
                             f"({sorted(TERMINAL_STATUSES)}) -- run was never actually completed")
        if not response_type:
            problems.append("ResponseType is not set -- --publish-response was never actually called")
        if not reply_text or not reply_text.strip():
            problems.append("ReplyText is empty -- nothing was actually written for the user/ticket")
        if completed_on is None:
            problems.append("CompletedOn is NULL -- no completion timestamp recorded")
        if error_msg:
            problems.append(f"ErrorMessage is set: {error_msg!r}")

        return (len(problems) == 0), problems
    finally:
        conn.close()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("run_id")
    ap.add_argument("--server", default="10.2.6.204")
    ap.add_argument("--database", default="XStudio_Helpdesk")
    ap.add_argument("--username", default="sa")
    ap.add_argument("--password", default=os.environ.get("MSSQL_MCP_PASSWORD"))
    args = ap.parse_args()

    ok, problems = verify(args.run_id, args.server, args.database, args.username, args.password)
    if ok:
        print(f"VERIFIED: run {args.run_id} genuinely published (ProcessStatus terminal, "
              f"ReplyText present, CompletedOn set).")
        sys.exit(0)
    else:
        print(f"NOT VERIFIED: run {args.run_id} is NOT actually complete, "
              f"regardless of what any transcript claims:")
        for p in problems:
            print(f"  - {p}")
        sys.exit(1)


if __name__ == "__main__":
    main()
