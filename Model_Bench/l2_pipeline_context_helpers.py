#!/usr/bin/env python3
"""Context-aware facade over Chitragupta's deterministic L2 lifecycle core.

The lifecycle state machine is preserved in ``l2_pipeline_runtime_core``. This
facade owns only the Phase-2 context-delivery boundary around investigation,
review and rework card creation:

- requester-grounded deterministic retrieval;
- bounded stage-specific L2ContextEnvelope assembly;
- fail-closed degradation semantics;
- durable context receipts and hashes;
- current-run evidence packaging for review/rework.

The core remains the sole lifecycle/publish/recovery authority. Retrieval never
changes SQL ticket state and GBrain remains derived ranking/index state.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Optional

import l2_pipeline_runtime_core as _core
from l2_context_delivery import (
    assemble_degraded_context,
    assemble_stage_context,
    build_requester_retrieval_query,
    load_context_receipt,
    persist_context_receipt,
    provenance_header,
)

# Re-export the complete existing lifecycle API, including private helpers used
# by sibling learning/runtime modules. Overrides below are installed into both
# this facade and the core module so the existing core reconciler/CLI resolves
# the Phase-2 card constructors at runtime without duplicating the state machine.
for _name in dir(_core):
    if not _name.startswith("__"):
        globals()[_name] = getattr(_core, _name)


def task_context_receipt(task: dict[str, Any]) -> Optional[str]:
    return body_field(task.get("body"), "context_receipt")


def task_source_context_receipt(task: dict[str, Any]) -> Optional[str]:
    return body_field(task.get("body"), "source_context_receipt")


def _load_receipt_envelope(value: str | None) -> dict[str, Any] | None:
    if not value or value.startswith("dry-run:"):
        return None
    try:
        receipt = load_context_receipt(value)
    except Exception:
        return None
    envelope = receipt.get("envelope")
    return envelope if isinstance(envelope, dict) else None


def _ticket_snapshot(args: Any, ticket_id: str, fallback: dict[str, Any] | None = None) -> dict[str, Any]:
    """Get the current Helpdesk ticket row from the existing investigation bundle.

    This reuses the already-supported orchestrator surface instead of creating a
    second SQL transport/query implementation in the context layer.
    """
    try:
        bundle = run_orchestrator(args, ["--investigate-bundle", ticket_id], timeout=90)
    except RuntimeError:
        return dict(fallback or {})
    if isinstance(bundle, dict) and isinstance(bundle.get("ticket"), dict):
        return dict(bundle["ticket"])
    return dict(fallback or {})


def _run_evidence_snapshot(args: Any, run_id: str) -> dict[str, Any]:
    """Read a bounded current-run action receipt for reviewer/rework context."""
    safe = str(run_id).replace("'", "''")
    sql = (
        "SELECT TOP 20 ID, RunID, TicketID, ActionNo, ActionType, DatabaseName, "
        "SchemaName, ObjectName, OperationName, Purpose, Status, RowsAffected, "
        "StartedOn, CompletedOn, ErrorNumber, ErrorMessage "
        "FROM dbo.Hermes_L2_SQL_Action_Trn_Tbl "
        f"WHERE RunID = '{safe}' AND IsDeleted = 0 ORDER BY ActionNo;"
    )
    try:
        rows = run_orchestrator(args, ["--query", sql], timeout=60)
    except RuntimeError as exc:
        return {
            "available": False,
            "error": f"current-run action receipt unavailable: {exc}"[:800],
            "rows": [],
        }
    return {
        "available": True,
        "rows": rows if isinstance(rows, list) else [],
    }


def _query_for_retrieval(ticket: dict[str, Any]) -> str:
    return build_requester_retrieval_query(ticket)


def _run_kb_retrieval(args: Any, ticket: dict[str, Any]) -> dict[str, Any]:
    """Compatibility helper: governed retrieval only, never raw Solution SQL."""
    query = _query_for_retrieval(ticket)
    if not query:
        return {
            "schema_version": 2,
            "query": "",
            "route_candidates": [{"route": "discover", "score": 0.0, "reasons": ["no requester-grounded retrieval text"]}],
            "canonical_documents": [],
            "promoted_facts": [],
            "governed_solutions": [],
            "approved_cases": [],
            "rejected_cases": [],
            "reopened_cases": [],
            "gbrain": {},
            "retrieval_degraded": False,
            "degradation_reasons": [],
        }
    try:
        import kb_retrieval as kb
        return kb.retrieve(query, top=5)
    except Exception as exc:
        return {
            "schema_version": 2,
            "query": query,
            "route_candidates": [{"route": "discover", "score": 0.0, "reasons": ["governed retriever unavailable"]}],
            "canonical_documents": [],
            "promoted_facts": [],
            "governed_solutions": [],
            "approved_cases": [],
            "rejected_cases": [],
            "reopened_cases": [],
            "gbrain": {},
            "retrieval_degraded": True,
            "degradation_reasons": [f"governed retriever failed: {type(exc).__name__}: {exc}"[:1000]],
        }


def _investigation_bundle(args: Any, ticket_id: str, fallback_ticket: dict[str, Any]) -> str:
    """Render operational/live bundle only; governed reusable context is separate."""
    try:
        bundle = run_orchestrator(args, ["--investigate-bundle", ticket_id], timeout=90)
    except RuntimeError as exc:
        bundle = {
            "ticket_id": ticket_id,
            "ticket": fallback_ticket,
            "bundle_warning": f"Dispatcher could not assemble investigation bundle: {exc}",
        }
    if not isinstance(bundle, dict):
        bundle = {
            "ticket_id": ticket_id,
            "ticket": fallback_ticket,
            "bundle_warning": "Unexpected bundle shape.",
        }
    # Old orchestrator KB material is not a second worker-facing retrieval plane.
    bundle.pop("known_solutions", None)
    bundle.pop("kb_retrieval", None)
    rendered = json.dumps(bundle, indent=2, default=str)
    if len(rendered) > 14000:
        rendered = rendered[:14000] + "\n... [operational bundle truncated at 14,000 chars]"
    return (
        "\n--- Current-ticket operational bundle ---\n"
        "This package is current-ticket/run context, not reusable-memory authority. "
        "Final claims still require live xstudio_l2 verification.\n"
        f"{rendered}\n"
    )


def _original_context_for_task(task: dict[str, Any]) -> tuple[dict[str, Any] | None, str | None]:
    """Resolve the original investigation context carried through review/rework."""
    direct = task_source_context_receipt(task) or task_context_receipt(task)
    envelope = _load_receipt_envelope(direct)
    if envelope is not None:
        return envelope, direct

    # Compatibility/recovery path for older cards: follow investigation_task_id.
    investigation_task_id = body_field(task.get("body"), "investigation_task_id")
    if investigation_task_id:
        try:
            for candidate in list_tasks():
                if str(candidate.get("id")) == str(investigation_task_id):
                    value = task_context_receipt(candidate)
                    loaded = _load_receipt_envelope(value)
                    if loaded is not None:
                        return loaded, value
                    break
        except RuntimeError:
            pass
    return None, direct


def _context_ticket_or_original(
    ticket: dict[str, Any], original_context: dict[str, Any] | None
) -> dict[str, Any]:
    if build_requester_retrieval_query(ticket):
        return ticket
    if original_context and str(original_context.get("requester_query") or "").strip():
        # The original query was already deterministically derived only from safe
        # requester/system fields; using it as a degraded refresh seed cannot add a
        # model hypothesis to retrieval.
        return {"BriefDetails": str(original_context["requester_query"])}
    return ticket


def _build_and_persist_stage_context(
    *,
    args: Any,
    ticket: dict[str, Any],
    run_id: str,
    ticket_id: str,
    ticket_no: str,
    stage: str,
    review_cycle: int,
    dry_run: bool,
    proposal: dict[str, Any] | None = None,
    current_run_evidence: Any = None,
    rejection_reason: str | None = None,
    original_context: dict[str, Any] | None = None,
) -> tuple[dict[str, Any], str, str]:
    safe_ticket = _context_ticket_or_original(ticket, original_context)
    try:
        envelope, rendered = assemble_stage_context(
            ticket=safe_ticket,
            run_id=run_id,
            ticket_id=ticket_id,
            ticket_no=ticket_no,
            stage=stage,
            review_cycle=review_cycle,
            proposal=proposal,
            current_run_evidence=current_run_evidence,
            rejection_reason=rejection_reason,
            original_context=original_context,
        )
    except Exception as exc:
        envelope, rendered = assemble_degraded_context(
            ticket=safe_ticket,
            run_id=run_id,
            ticket_id=ticket_id,
            ticket_no=ticket_no,
            stage=stage,
            review_cycle=review_cycle,
            reason=f"governed context assembly failed: {type(exc).__name__}: {exc}",
            proposal=proposal,
            current_run_evidence=current_run_evidence,
            rejection_reason=rejection_reason,
            original_context=original_context,
        )

    if dry_run:
        receipt = f"dry-run:{run_id}:{stage}:{review_cycle}:{envelope['context_sha256']}"
    else:
        # Receipt persistence is part of the provenance correctness contract. If
        # this fails, do not create a worker card whose delivered context cannot
        # later be reconstructed.
        receipt = str(persist_context_receipt(envelope, rendered))
    return envelope, rendered, receipt



__all__=[name for name in globals() if not name.startswith("__")]
