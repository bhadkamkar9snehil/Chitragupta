#!/usr/bin/env python3
"""Deterministic bridge between the real SQL ticket queue and the Kanban
board -- replaces the old per-bot polling cron jobs entirely (2026-09-03
Kanban migration). Runs as a --no-agent cron job on l2-investigator (the
one profile whose gateway hosts the kanban dispatcher).

What it does, every tick:
1. Calls Hermes_Orchestrator.py --poll (the real atomic claim, unchanged)
   via the Windows Python interpreter (has pyodbc).
2. If a ticket was genuinely claimed, archives any stale kanban card
   already sitting on the board for the SAME ticket (see below), then
   creates TWO kanban tasks: the investigator's card (assignee
   INVESTIGATOR_PROFILE, currently l2-investigator-primary -- see that
   constant below for the live value, not this comment, if they ever
   drift again), and a reviewer card gated on it via --parent (assignee
   REVIEWER_PROFILE, currently l2-reviewer-primary) -- both on the single
   default board. The reviewer
   card auto-promotes from 'todo' to 'ready' the moment the investigator's
   card completes; no separate bridge script needed for that hop.
3. If nothing was claimable, does nothing -- NO_TICKETS/NO_CLAIMABLE_TICKET
   are not errors.

2026-09-04 (later): rewritten to use native Kanban dependency gating
(`kanban create --parent`) instead of a separate forward-bridge cron
script. Verified against Hermes's own source
(hermes_cli/kanban_swarm.py, kanban_db.py build_worker_context): a task
created with --parent <investigator_task_id> starts 'todo' and is
auto-promoted to 'ready' the moment that parent completes, and the
reviewer's own context automatically includes the investigator's
kanban_complete summary/metadata (build_worker_context's "structured
handoff of every done parent task") -- no manual body-JSON copying or
cron polling needed for the forward hop. `kanban_forward_bridge.py` is
retired. The `hermes kanban swarm` command itself was evaluated and
rejected for this role: its verifier/synthesizer skills are hardcoded in
source (requesting-code-review / humanizer) with no override, which
would silently replace the real xstudio-l2-draft-verifier SQL/schema
verification with a generic skill -- --parent gating is the actual
native primitive we want, swarm is just an unsuitable convenience
wrapper around it for this use case. Both cards now live on ONE board
(default) -- the old two-board split existed to avoid a *same-task*
reassignment bug (kanban_request_changes reassigning one shared card
between roles); that bug doesn't apply here since investigator and
reviewer are always separate task objects that never change owner.

Why archive the old card before creating a new one (2026-09-04 incident):
this script's idempotency key is keyed on run_id, not ticket_id, because
run_id is meant to be unique per attempt -- that part is correct. But
Hermes_L2_Recover_Stale_Runs_Usp (called inside --poll, stale_minutes=60)
starts its staleness clock at CLAIM time, not at dispatch time. With
max_in_progress=1 on this gateway, a ticket can sit ready/blocked in the
kanban queue for well over an hour before a worker ever touches it, time
out server-side, get marked FAILED, and immediately become reclaimable
again on the next --poll -- producing a brand-new run_id (and, since the
idempotency key is run_id-based, a brand-new kanban card) for a ticket
that already has an old, now-orphaned card still sitting in ready/blocked.
Nothing ever cleaned those up. Confirmed live: 472 total tasks on the
default board, 413 of them exactly this kind of duplicate, up to 22
duplicate cards for one ticket (Ticket_244) spanning 21 hours of hourly
stale-timeout-and-reclaim cycles the dispatcher could never keep up with.
This step is the fix: whenever a ticket is reclaimed, any of its own
older cards still sitting in a not-yet-dispatched state get archived
first, so the board can never accumulate more than one live card per
ticket again, regardless of how backed up the dispatch queue gets.
"""
import os
import json
import re
import subprocess
import sys

PYTHON = "/mnt/c/Python314/python.exe"
ORCHESTRATOR = r"C:\Users\Admin\Documents\Office\AIHelpdesk\Hermes_Orchestrator.py"
SERVER = "10.2.6.204"
USER = "sa"
PASSWORD = os.environ.get("MSSQL_MCP_PASSWORD")
ELIGIBLE_STATUS = "Enter"
INVESTIGATOR_PROFILE = "l2-investigator-primary"
REVIEWER_PROFILE = "l2-reviewer-primary"

# Cards in one of these statuses have not yet been (or are no longer being)
# actively worked -- safe to archive once we know their ticket has been
# reclaimed under a new run_id. 'running' and 'done' are deliberately
# excluded: never archive a card that's actively executing, and 'done'
# cards are a legitimate historical record, not backlog noise. 'todo' is
# included as of the native --parent-gating rewrite: a reviewer card sits
# 'todo' (not 'ready') until its investigator parent completes, so a stale
# gated-but-not-yet-promoted reviewer card needs the same cleanup as a
# stale 'ready' investigator card, or it would dangle forever pointing at
# a parent that's about to be orphaned.
_ARCHIVABLE_STATUSES = {"todo", "ready", "blocked", "triage", "scheduled"}


def _archive_stale_cards_for_ticket(ticket_id: str, new_run_id: str) -> None:
    result = subprocess.run(
        ["hermes", "kanban", "list", "--json"],
        capture_output=True, text=True, timeout=30,
    )
    if result.returncode != 0:
        print(f"WARNING: could not list board to check for stale cards: {result.stderr.strip()[:300]}")
        return

    try:
        tasks = json.loads(result.stdout)
    except json.JSONDecodeError:
        print("WARNING: could not parse kanban list output; skipping stale-card cleanup this tick.")
        return

    ticket_pattern = re.compile(rf"ticket_id:\s*{re.escape(ticket_id)}\b", re.IGNORECASE)
    stale_ids = [
        t["id"] for t in tasks
        if t.get("status") in _ARCHIVABLE_STATUSES
        and ticket_pattern.search(t.get("body") or "")
    ]
    if not stale_ids:
        return

    print(f"Ticket {ticket_id} reclaimed as run {new_run_id}; archiving {len(stale_ids)} stale card(s): {stale_ids}")
    archive = subprocess.run(
        ["hermes", "kanban", "archive"] + stale_ids,
        capture_output=True, text=True, timeout=30,
    )
    if archive.returncode != 0:
        print(f"WARNING: archive of stale cards failed: {archive.stderr.strip()[:300]}")


def main():
    result = subprocess.run(
        [PYTHON, ORCHESTRATOR, "--poll", "--eligible-status", ELIGIBLE_STATUS,
         "--server", SERVER, "--username", USER, "--password", PASSWORD,
         "--bot-label", INVESTIGATOR_PROFILE],
        capture_output=True, text=True, timeout=60,
    )
    if result.returncode != 0:
        print(f"Poll failed: {result.stderr.strip()[:500]}")
        sys.exit(1)

    try:
        poll_result = json.loads(result.stdout)
    except json.JSONDecodeError:
        print(f"Could not parse poll output: {result.stdout[:500]}")
        sys.exit(1)

    status = poll_result.get("status")
    if status in ("NO_TICKETS", "NO_CLAIMABLE_TICKET"):
        print(f"{status}: nothing to do this tick.")
        return

    if status != "CLAIMED":
        print(f"Unexpected poll status: {status}")
        sys.exit(1)

    run_id = poll_result["run_id"]
    ticket_id = poll_result["ticket_id"]
    ticket = poll_result.get("ticket", {})
    # The board should show the human-readable ticket number (e.g.
    # "Ticket_176"), not the raw TicketID GUID -- the GUID is still in the
    # body for the worker to use, this is purely a display fix for anyone
    # looking at the board.
    ticket_no = ticket.get("TicketNo") or ticket_id

    _archive_stale_cards_for_ticket(ticket_id, run_id)

    body = (
        f"run_id: {run_id}\n"
        f"ticket_id: {ticket_id}\n\n"
        f"Full ticket context (already claimed via --poll, do not re-poll):\n"
        f"{json.dumps(ticket, indent=2, default=str)[:4000]}\n"
    )

    create = subprocess.run(
        ["hermes", "kanban", "create", f"L2 {ticket_no}",
         "--assignee", INVESTIGATOR_PROFILE,
         "--body", body,
         "--skill", "xstudio-l2-ticket-workflow",
         "--skill", "xstudio-sql-write-discipline",
         "--idempotency-key", f"l2-ticket-{run_id}",
         # A single hung/slow investigation blocking the whole queue behind
         # it was a real incident 2026-09-03 (max_in_progress:1, one task
         # ran 36+ min while 12 others piled up in `ready`). 20m is well
         # above the ~3-15min genuine range observed across models so far,
         # short enough that a truly stuck task doesn't block the queue
         # for the better part of an hour.
         "--max-runtime", "20m",
         "--json"],
        capture_output=True, text=True, timeout=30,
    )
    if create.returncode != 0:
        print(f"kanban create FAILED for run {run_id}: {create.stderr.strip()[:500]}")
        sys.exit(1)

    try:
        investigator_task_id = json.loads(create.stdout).get("id")
    except json.JSONDecodeError:
        investigator_task_id = None
    print(f"Created kanban task for run {run_id} (ticket {ticket_id}): {create.stdout.strip()}")

    if not investigator_task_id:
        print("WARNING: could not read investigator task id from create output; "
              "no reviewer card created for this run (nothing will bridge it).")
        return

    review_body = (
        f"run_id: {run_id}\n"
        f"ticket_id: {ticket_id}\n"
        f"investigation_task_id: {investigator_task_id}\n\n"
        f"Gated on the investigator's card ({investigator_task_id}) -- this "
        f"card auto-promotes to ready the moment that one completes, and "
        f"the investigator's kanban_complete summary/metadata surfaces "
        f"automatically in your own context (native parent handoff). "
        f"Call kanban_show() to read it."
    )
    review = subprocess.run(
        ["hermes", "kanban", "create", f"REVIEW: L2 {ticket_no}",
         "--assignee", REVIEWER_PROFILE,
         "--body", review_body,
         "--parent", investigator_task_id,
         "--skill", "xstudio-l2-draft-verifier",
         "--skill", "xstudio-sql-write-discipline",
         "--idempotency-key", f"rev-{run_id}",
         "--max-runtime", "15m",
         "--json"],
        capture_output=True, text=True, timeout=30,
    )
    if review.returncode != 0:
        print(f"kanban create (reviewer) FAILED for run {run_id}: {review.stderr.strip()[:500]}")
        sys.exit(1)
    print(f"Created reviewer task (gated on {investigator_task_id}): {review.stdout.strip()}")


if __name__ == "__main__":
    main()
