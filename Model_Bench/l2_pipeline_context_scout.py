#!/usr/bin/env python3
"""Investigation claim/card constructor for Phase-2 L2 context delivery."""
from __future__ import annotations
from l2_pipeline_context_helpers import *

def scout(args: Any, *, dry_run: bool = False) -> dict[str, Any]:
    reconciliation = reconcile(args, dry_run=dry_run)
    if dry_run:
        return {"status": "DRY_RUN", "reconcile": reconciliation}

    binding = load_workflow_binding()
    ready, reason = _binding_ready_for_claims(binding)
    if not ready:
        return {
            "status": "WORKFLOW_BINDING_NOT_READY",
            "reason": reason,
            "binding_path": binding.get("_path"),
            "reconcile": reconciliation,
        }

    active = query_active_runs(args)
    if active:
        return {"status": "WIP_LIMIT", "active_runs": active, "reconcile": reconciliation}

    eligible = str(binding.get("eligible_ticket_status") or args.eligible_status or DEFAULT_ELIGIBLE_STATUS)
    poll = run_orchestrator(
        args,
        ["--poll", "--eligible-status", eligible, "--bot-label", INVESTIGATOR_PROFILE],
        timeout=90,
    )
    if not isinstance(poll, dict):
        raise RuntimeError(f"unexpected poll response: {poll!r}")
    if poll.get("status") in ("NO_TICKETS", "NO_CLAIMABLE_TICKET"):
        return {"status": poll.get("status"), "reconcile": reconciliation}
    if poll.get("status") != "CLAIMED":
        raise RuntimeError(f"unexpected poll status: {poll.get('status')}")

    run_id = str(poll["run_id"])
    ticket_id = str(poll["ticket_id"])
    ticket = poll.get("ticket") or {}
    ticket_no = str(ticket.get("TicketNo") or ticket_id)
    _archive_stale_cards_for_ticket(ticket_id, run_id)

    try:
        envelope, rendered_context, receipt = _build_and_persist_stage_context(
            args=args,
            ticket=ticket,
            run_id=run_id,
            ticket_id=ticket_id,
            ticket_no=ticket_no,
            stage="investigation",
            review_cycle=0,
            dry_run=False,
        )
    except Exception as exc:
        # A claimed run without durable context provenance must not be handed to
        # a worker. Fail it cleanly so the normal retry mechanism can reclaim it.
        try:
            run_orchestrator(args, [
                "--fail-run", "--run-id", run_id,
                "--error-message", f"Dispatcher could not persist governed L2 context: {type(exc).__name__}: {exc}"[:500],
                "--retry-after-minutes", "5",
            ])
        except RuntimeError:
            pass
        raise RuntimeError(f"investigation context persistence failed: {exc}") from exc

    body = (
        f"run_id: {run_id}\n"
        f"ticket_id: {ticket_id}\n"
        f"ticket_no: {ticket_no}\n"
        "review_cycle: 0\n"
        "pipeline_stage: investigation\n"
        + provenance_header(envelope, receipt)
        + "\n"
        + rendered_context
        + _investigation_bundle(args, ticket_id, ticket)
        + _query_instructions(run_id, ticket_id)
    )
    create = run_hermes([
        "kanban", "create", f"L2 {ticket_no}",
        "--assignee", INVESTIGATOR_PROFILE,
        "--body", body,
        "--skill", "xstudio-l2-ticket-workflow",
        "--skill", "xstudio-sql-write-discipline",
        "--priority", str(NEW_INVESTIGATION_PRIORITY),
        "--idempotency-key", f"l2-ticket-{run_id}",
        "--max-runtime", "20m",
        "--json",
    ])
    if create.returncode != 0:
        try:
            run_orchestrator(args, [
                "--fail-run", "--run-id", run_id,
                "--error-message", f"Dispatcher could not create investigator Kanban task: {create.stderr.strip()[:400]}",
                "--retry-after-minutes", "5",
            ])
        except RuntimeError:
            pass
        raise RuntimeError(f"investigator create failed: {create.stderr.strip()[:500]}")
    try:
        investigator_id = (json.loads(create.stdout) or {}).get("id")
    except json.JSONDecodeError:
        investigator_id = None
    if not investigator_id:
        raise RuntimeError("investigator task was created but its id could not be parsed")

    return {
        "status": "CLAIMED",
        "run_id": run_id,
        "ticket_id": ticket_id,
        "investigator_task_id": investigator_id,
        "reviewer_task_id": None,
        "reviewer_creation": "deferred_until_normalized_completion",
        "context_sha256": envelope["context_sha256"],
        "context_receipt": receipt,
        "retrieval_degraded": envelope["retrieval"]["retrieval_degraded"],
        "priorities": {
            "investigation": NEW_INVESTIGATION_PRIORITY,
            "rework": REWORK_PRIORITY,
            "review": REVIEW_PRIORITY,
        },
        "reconcile": reconciliation,
    }



__all__=[name for name in globals() if not name.startswith("__")]
