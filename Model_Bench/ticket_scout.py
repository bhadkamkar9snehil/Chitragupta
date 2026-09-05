#!/usr/bin/env python3
"""Deterministic bridge from the live SQL ticket queue to Hermes Kanban.

Current architecture:
- `Hermes_Orchestrator.py --poll` atomically claims one Helpdesk ticket.
- this script creates an investigator task on the default board;
- it creates a reviewer task on the same board with `--parent` pointing to
  the investigator task, so Hermes native parent gating promotes review only
  after investigation completes;
- no forward bridge and no separate review board are involved.

The investigator card carries ONE deterministic investigation bundle. Older
versions independently embedded the ticket, called --suggest-tables, called
--get-ledger, and then taught the worker to call --investigate-bundle again.
That duplicated context, tool turns, and retrieval paths. The bundle is now the
single dispatch-time context assembly path; its own sections degrade
independently inside Hermes_Orchestrator.py.
"""
from __future__ import annotations

import json
import os
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

# The gateway intentionally runs one worker at a time because LM Studio's
# unified KV cache cannot safely sustain two long 65K-context workers on the
# current hardware. Priority is therefore the fairness mechanism.
INVESTIGATOR_PRIORITY = 10
REVIEWER_PRIORITY = 5

# Safe to archive only work that is not actively executing and is not useful
# completed history. `todo` includes a reviewer still gated on an old parent.
_ARCHIVABLE_STATUSES = {"todo", "ready", "blocked", "triage", "scheduled"}


def _orchestrator_cmd(*extra: str) -> list[str]:
    """Build the standard orchestrator command without forcing a null password.

    Hermes_Orchestrator.py already reads MSSQL_MCP_PASSWORD from the environment,
    so omitting --password when the variable is absent is both safer and avoids
    passing None into subprocess.
    """
    cmd = [PYTHON, ORCHESTRATOR, "--server", SERVER, "--username", USER]
    if PASSWORD:
        cmd += ["--password", PASSWORD]
    cmd += list(extra)
    return cmd


def _run_orchestrator(extra_args: list[str], timeout: int = 60) -> dict | list | None:
    """Run Hermes_Orchestrator.py and parse JSON stdout.

    This is enrichment/dispatch support. Failure must never fabricate context;
    callers either fall back to already-claimed ticket data or fail explicitly.
    """
    try:
        r = subprocess.run(
            _orchestrator_cmd(*extra_args),
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        if r.returncode != 0:
            return None
        return json.loads(r.stdout)
    except (subprocess.TimeoutExpired, json.JSONDecodeError, OSError, TypeError):
        return None


def _archive_stale_cards_for_ticket(ticket_id: str, new_run_id: str) -> None:
    """Archive stale queued/gated cards when the SQL ticket is reclaimed.

    Run IDs are unique per attempt, but a ticket can be reclaimed after an old
    run expires while its Kanban card is still queued. Without ticket-level
    cleanup that produces duplicate live work for the same ticket.
    """
    result = subprocess.run(
        ["hermes", "kanban", "list", "--json"],
        capture_output=True,
        text=True,
        timeout=30,
    )
    if result.returncode != 0:
        print(f"WARNING: could not list board for stale-card cleanup: {result.stderr.strip()[:300]}")
        return

    try:
        tasks = json.loads(result.stdout)
    except json.JSONDecodeError:
        print("WARNING: could not parse kanban list; skipping stale-card cleanup this tick.")
        return

    ticket_pattern = re.compile(rf"ticket_id:\s*{re.escape(ticket_id)}\b", re.IGNORECASE)
    stale_ids = [
        t["id"]
        for t in tasks
        if t.get("status") in _ARCHIVABLE_STATUSES
        and ticket_pattern.search(t.get("body") or "")
    ]
    if not stale_ids:
        return

    print(
        f"Ticket {ticket_id} reclaimed as run {new_run_id}; "
        f"archiving {len(stale_ids)} stale card(s): {stale_ids}"
    )
    archive = subprocess.run(
        ["hermes", "kanban", "archive", *stale_ids],
        capture_output=True,
        text=True,
        timeout=30,
    )
    if archive.returncode != 0:
        print(f"WARNING: stale-card archive failed: {archive.stderr.strip()[:300]}")


def _investigation_bundle_section(ticket_id: str, fallback_ticket: dict) -> str:
    """Return the single dispatch-time context package for an investigator.

    `--investigate-bundle` already assembles:
      - current ticket context;
      - mechanically narrowed real schema candidates;
      - prior ledger;
      - recent prior attempts;
      - known-solution candidates.

    Do not reproduce those as independent dispatcher calls. If the bundle command
    itself fails, retain only the already-claimed ticket snapshot and state the
    failure honestly; the worker still has deterministic discovery tools.
    """
    result = _run_orchestrator(
        ["--database", "XStudio_Helpdesk", "--investigate-bundle", ticket_id],
        timeout=90,
    )

    if not isinstance(result, dict):
        result = {
            "ticket_id": ticket_id,
            "ticket": fallback_ticket,
            "bundle_warning": (
                "Dispatcher could not assemble --investigate-bundle. "
                "Use the exact query commands below for live discovery; do not invent missing context."
            ),
        }

    # Bound card growth. The bundle is context, not a database export. Individual
    # bundle sections are already compact; this outer cap protects Kanban/task
    # context if an SP unexpectedly returns oversized text in the future.
    rendered = json.dumps(result, indent=2, default=str)
    if len(rendered) > 12000:
        rendered = rendered[:12000] + "\n... [bundle truncated by dispatcher at 12,000 chars]"

    return (
        "\n--- Investigation bundle (single dispatch-time context package) ---\n"
        "Treat retrieved solutions, prior findings, and table suggestions as leads, not proof.\n"
        "Current live SQL/data or verified Knowledge/ sources must support final claims.\n"
        f"{rendered}\n"
    )


def _how_to_query_section(run_id: str, ticket_id: str) -> str:
    """Exact worker commands so the model never spends turns rediscovering paths."""
    py = PYTHON
    orch = "/mnt/c/" + ORCHESTRATOR.replace("\\", "/").removeprefix("C:/")
    return (
        "\n--- Exact investigation commands for this run ---\n"
        f"Interpreter: {py}\n"
        f"Script: {orch}\n\n"
        "The starting investigation bundle is ALREADY above. Do not fetch the same context again.\n\n"
        "1) Preferred read: mechanically validate table + columns before SELECT:\n"
        f'   {py} "{orch}" --server {SERVER} --database XStudio_Xbatch \\\n'
        '     --build-query dbo.SomeTable --columns "ColA,ColB" \\\n'
        '     --where "HeatNo = \'123\'" --top 20 --execute\n\n'
        "2) If the bundle's schema candidates are insufficient, narrow the real schema again:\n"
        f'   {py} "{orch}" --server {SERVER} --database XStudio_Xbatch \\\n'
        '     --suggest-tables "<specific unresolved symptom or identifier>" --top 8\n\n'
        "3) Raw read-only SQL when needed (database is mandatory):\n"
        f'   {py} "{orch}" --server {SERVER} --database XStudio_Xbatch \\\n'
        '     --query "SELECT TOP 20 ... FROM dbo.SomeView WHERE ..."\n\n'
        "4) Preserve useful ticket-specific findings before completion/rework:\n"
        f'   {py} "{orch}" --server {SERVER} --database XStudio_Helpdesk \\\n'
        f"     --save-ledger {run_id} --ledger '{{\"tables_queried\":[...],\n"
        '     "key_values_found":{...},"ruled_out":[...],"conclusion":"..."}\'\n\n'
        f"If current ticket data must be refreshed later: --get-ticket-context {ticket_id} "
        "--database XStudio_Helpdesk\n"
        "Writes to the live ticket are owned by reviewer + deterministic publisher, never --query.\n"
    )


def main() -> None:
    result = subprocess.run(
        _orchestrator_cmd(
            "--poll",
            "--eligible-status",
            ELIGIBLE_STATUS,
            "--bot-label",
            INVESTIGATOR_PROFILE,
        ),
        capture_output=True,
        text=True,
        timeout=60,
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
    ticket = poll_result.get("ticket") or {}
    ticket_no = ticket.get("TicketNo") or ticket_id

    _archive_stale_cards_for_ticket(ticket_id, run_id)

    body = (
        f"run_id: {run_id}\n"
        f"ticket_id: {ticket_id}\n"
        + _investigation_bundle_section(ticket_id, ticket)
        + _how_to_query_section(run_id, ticket_id)
    )

    create = subprocess.run(
        [
            "hermes",
            "kanban",
            "create",
            f"L2 {ticket_no}",
            "--assignee",
            INVESTIGATOR_PROFILE,
            "--body",
            body,
            "--skill",
            "xstudio-l2-ticket-workflow",
            "--skill",
            "xstudio-sql-write-discipline",
            "--priority",
            str(INVESTIGATOR_PRIORITY),
            "--idempotency-key",
            f"l2-ticket-{run_id}",
            "--max-runtime",
            "20m",
            "--json",
        ],
        capture_output=True,
        text=True,
        timeout=30,
    )
    if create.returncode != 0:
        print(f"kanban create FAILED for run {run_id}: {create.stderr.strip()[:500]}")
        sys.exit(1)

    try:
        investigator_task_id = json.loads(create.stdout).get("id")
    except json.JSONDecodeError:
        investigator_task_id = None

    print(
        f"Created investigator task for run {run_id} (ticket {ticket_id}): "
        f"{create.stdout.strip()}"
    )

    if not investigator_task_id:
        print(
            "WARNING: could not read investigator task id from create output; "
            "reviewer card was not created."
        )
        return

    review_body = (
        f"run_id: {run_id}\n"
        f"ticket_id: {ticket_id}\n"
        f"investigation_task_id: {investigator_task_id}\n\n"
        "This reviewer task is gated on the investigator through Hermes native --parent handoff. "
        "When promoted, use kanban_show() and the structured parent completion metadata as the "
        "proposal to verify. Do not reconstruct the investigator's answer from prose."
    )

    review = subprocess.run(
        [
            "hermes",
            "kanban",
            "create",
            f"REVIEW: L2 {ticket_no}",
            "--assignee",
            REVIEWER_PROFILE,
            "--body",
            review_body,
            "--priority",
            str(REVIEWER_PRIORITY),
            "--parent",
            investigator_task_id,
            "--skill",
            "xstudio-l2-draft-verifier",
            "--skill",
            "xstudio-sql-write-discipline",
            "--idempotency-key",
            f"rev-{run_id}",
            "--max-runtime",
            "15m",
            "--json",
        ],
        capture_output=True,
        text=True,
        timeout=30,
    )
    if review.returncode != 0:
        print(f"kanban create (reviewer) FAILED for run {run_id}: {review.stderr.strip()[:500]}")
        sys.exit(1)

    print(f"Created reviewer task (gated on {investigator_task_id}): {review.stdout.strip()}")


if __name__ == "__main__":
    main()
