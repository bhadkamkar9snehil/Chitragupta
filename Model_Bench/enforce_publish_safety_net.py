#!/usr/bin/env python3
"""Deterministic, no-LLM safety net: guarantees no L2 ticket is ever left
silently claimed-but-unpublished.

Why this exists: a real, repeated 2026-09-03 failure had the investigating
agent write a complete-sounding final response ("Investigation halted...
escalating to L3...") and the cron wrapper mark the run "completed" --
while `Hermes_L2_Response_Trn_Tbl` never actually got a ReplyText/
ResponseType written, because the agent's own turn ended without ever
emitting the --publish-response tool call. This is a documented, general
agent failure class ("execution hallucination" / narrating an action
without the tool call that performs it) -- prompting alone does not
reliably fix it. The fix is an independent, deterministic verifier that
NEVER trusts the agent's own narration, per standard agent-harness design:
"the system must never issue a retry without first consulting a
postcondition verifier... judged by tool-observed state, not narration."

What this does: finds any run claimed by this worker that is still
non-terminal (CLAIMED/INVESTIGATING) and old enough that a genuine
investigation would have finished by now (the longest observed real
investigation this session was ~15 minutes), and force-publishes a plain,
honest L3_ESCALATION for it -- "the investigating process did not publish
a response in time" -- rather than leaving the ticket silently stuck. This
does NOT replace Hermes' own much-longer stale-claim recovery (~1hr, for
genuinely crashed/abandoned processes) -- it's a much tighter net for the
"agent turn completed but forgot to publish" case specifically, which the
scheduler's own recovery does not catch (from Hermes' point of view the
cron execution genuinely completed).

Usage (deterministic, --no-agent cron job):
    python enforce_publish_safety_net.py --server 10.2.6.204 [--dry-run]
"""
import os
import argparse
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
import pyodbc

STALE_AFTER_MINUTES = 45
# History: 20 -> 30 -> 15 -> 5, all tuned around the OLD single-turn
# draft/nudge pipeline. On 2026-09-03 the whole pipeline was migrated to
# Kanban (ticket_scout.py claims + creates a task; --publish-response now
# happens ONLY when the l2-nemo reviewer approves via
# kanban_request_review/kanban_complete) -- nothing touches
# Hermes_L2_Response_Trn_Tbl for the entire investigate-then-review
# duration, which can legitimately run 15-30+ minutes on these small local
# models. At 5 minutes this net was firing on EVERY real investigation --
# confirmed live: 10 of 13 in-flight kanban tasks got force-escalated with
# the blind canned message while genuinely still working, including one
# that was actively converging on the right table when it got clobbered.
# Kanban's own dispatcher already handles genuine crash/hang recovery
# (stale-claim reclaim, protocol-violation retry-then-block) -- this net's
# only remaining real job is the case Kanban can't see at all: a ticket
# claimed via --poll in ticket_scout.py that crashed before the kanban
# task itself got created. 45 is a true last-resort number for that
# narrow case, not a responsiveness knob for normal investigation time.
ORCHESTRATOR_PATH = Path(__file__).parent.parent / "Hermes_Orchestrator.py"


def find_stale_claims(server, database, username, password, stale_after_minutes=STALE_AFTER_MINUTES):
    conn = pyodbc.connect(
        f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};"
        f"UID={username};PWD={password};TrustServerCertificate=yes"
    )
    try:
        cur = conn.cursor()
        # ClaimedOn is written in the SQL Server's own local time (server
        # GETDATE(), not UTC -- confirmed live 2026-09-03: comparing it
        # against Python's UTC "now" made every real stale claim look like
        # it was in the future, since local time here runs ~5.5h ahead of
        # UTC). Do the cutoff entirely in SQL against GETDATE() instead of
        # computing it client-side, so this can't drift out of sync with
        # whatever timezone the server actually uses.
        cur.execute(
            "SELECT ID, TicketID, ClaimedOn FROM Hermes_L2_Response_Trn_Tbl "
            "WHERE ProcessStatus IN ('CLAIMED', 'INVESTIGATING') AND IsActive = 1 "
            "AND ClaimedOn < DATEADD(MINUTE, -?, GETDATE())",
            stale_after_minutes,
        )
        return [{"run_id": str(r[0]), "ticket_id": str(r[1]), "claimed_on": str(r[2])} for r in cur.fetchall()]
    finally:
        conn.close()


_NON_TERMINAL_KANBAN_STATUSES = {"ready", "blocked", "triage", "running", "review", "scheduled"}


def find_live_kanban_run_ids():
    """run_ids that still have a LIVE (genuinely non-terminal) kanban task
    tracking them -- ready/running/review/blocked/triage/scheduled all
    count as "kanban is still the authority for this ticket, leave it
    alone." Only a run_id with NO matching non-terminal task at all is the
    true bridge-failure case this net exists for. Added 2026-09-03 after
    confirming live that the blind wall-clock version clobbered a genuine,
    well-reasoned investigation (Ticket_214) that took 114 minutes across
    real Kanban retries -- the net was racing Kanban's own retry cycle
    instead of respecting it.

    2026-09-04 correction: the original version scanned EVERY task
    regardless of status, so a task that reached 'done' -- the exact
    "agent narrated completion but never called --publish-response" case
    this net exists to catch -- still counted as "kanban has this," and
    the net deferred to it forever. Confirmed live: Ticket_264 ran 6
    consecutive attempts over 6.5 hours, every one reaching kanban 'done'
    with a real investigative summary and zero DB write, and the net
    never force-escalated a single one -- each was only ever cleaned up by
    the unrelated 60-minute Hermes_L2_Recover_Stale_Runs_Usp sweep marking
    it FAILED with nothing recorded, then ticket_scout.py reclaiming it
    for an identical next attempt. Restricting this to genuinely
    non-terminal statuses is what makes the net actually fire for that
    case instead of only for the narrower "kanban task never got created
    at all" case its docstring originally described.

    Best-effort: any failure here (hermes CLI unavailable, bad JSON) fails
    OPEN to the old blind behavior for that sweep rather than silently
    never escalating anything."""
    try:
        result = subprocess.run(
            ["wsl", "-d", "Ubuntu", "--", "bash", "-lc", "hermes kanban list --json"],
            capture_output=True, text=True, timeout=30,
        )
        if result.returncode != 0:
            print(f"WARNING: kanban list failed ({result.stderr.strip()[:200]}), "
                  f"falling back to blind wall-clock behavior this sweep.")
            return None
        tasks = json.loads(result.stdout)
    except Exception as e:
        print(f"WARNING: could not check kanban liveness ({e}), "
              f"falling back to blind wall-clock behavior this sweep.")
        return None

    live_run_ids = set()
    for t in tasks:
        if t.get("status") not in _NON_TERMINAL_KANBAN_STATUSES:
            continue
        body = t.get("body") or ""
        for line in body.splitlines():
            line = line.strip()
            if line.startswith("run_id:"):
                live_run_ids.add(line.split(":", 1)[1].strip())
                break
    return live_run_ids


def force_escalate(run_id, server, database, username, password, dry_run):
    reply = (
        "This ticket was claimed for automated investigation, but the investigating "
        "process did not publish a response within the expected time window. "
        "Escalating for manual review -- no automated finding was recorded for this run."
    )
    if dry_run:
        print(f"[DRY RUN] Would force-publish L3_ESCALATION for run {run_id}")
        return
    import subprocess
    result = subprocess.run(
        [sys.executable, str(ORCHESTRATOR_PATH),
         "--server", server, "--database", database,
         "--username", username, "--password", password,
         "--publish-response", "--run-id", run_id, "--force-run-id",
         "--response-type", "L3_ESCALATION", "--reply-text", reply],
        capture_output=True, text=True, timeout=60,
    )
    if result.returncode != 0:
        print(f"FAILED to force-publish for run {run_id}: {result.stderr.strip()}")
    else:
        print(f"Force-published L3_ESCALATION for run {run_id}: {result.stdout.strip()}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--server", default="10.2.6.204")
    ap.add_argument("--database", default="XStudio_Helpdesk")
    ap.add_argument("--username", default="sa")
    ap.add_argument("--password", default=os.environ.get("MSSQL_MCP_PASSWORD"))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--stale-after-minutes", type=int, default=STALE_AFTER_MINUTES)
    args = ap.parse_args()

    stale = find_stale_claims(args.server, args.database, args.username, args.password,
                               args.stale_after_minutes)
    if not stale:
        print("No stale unpublished claims found.")
        return

    live_run_ids = find_live_kanban_run_ids()

    print(f"Found {len(stale)} stale unpublished claim(s):")
    for s in stale:
        if live_run_ids is not None and s["run_id"] in live_run_ids:
            print(f"  run {s['run_id']} (ticket {s['ticket_id']}, claimed {s['claimed_on']}) "
                  f"-- SKIPPED, Kanban still has a live task for this run")
            continue
        print(f"  run {s['run_id']} (ticket {s['ticket_id']}, claimed {s['claimed_on']})")
        force_escalate(s["run_id"], args.server, args.database, args.username, args.password, args.dry_run)


if __name__ == "__main__":
    main()
