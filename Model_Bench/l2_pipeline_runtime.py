#!/usr/bin/env python3
"""Context-aware facade over Chitragupta's deterministic L2 lifecycle core.

Phase 2 keeps the proven lifecycle state machine byte-for-byte in
``l2_pipeline_runtime_core`` and layers deterministic context delivery around
investigation, review and rework card creation.
"""
import l2_pipeline_runtime_core as _core
import l2_pipeline_context_helpers as _helpers
import l2_pipeline_context_cards as _cards
import l2_pipeline_context_scout as _scout
from l2_pipeline_context_helpers import *

# Re-export the complete existing lifecycle API first.
for _name in dir(_core):
    if not _name.startswith("__") and _name not in globals():
        globals()[_name] = getattr(_core, _name)


def _sync(module, names):
    """Propagate facade-level overrides/patches into a split implementation module."""
    for name in names:
        if name in globals():
            setattr(module, name, globals()[name])


def task_context_receipt(*args, **kwargs):
    return _helpers.task_context_receipt(*args, **kwargs)


def task_source_context_receipt(*args, **kwargs):
    return _helpers.task_source_context_receipt(*args, **kwargs)


def _load_receipt_envelope(*args, **kwargs):
    _sync(_helpers, ["load_context_receipt"])
    return _helpers._load_receipt_envelope(*args, **kwargs)


def _ticket_snapshot(*args, **kwargs):
    _sync(_helpers, ["run_orchestrator"])
    return _helpers._ticket_snapshot(*args, **kwargs)


def _run_evidence_snapshot(*args, **kwargs):
    _sync(_helpers, ["run_orchestrator"])
    return _helpers._run_evidence_snapshot(*args, **kwargs)


def _query_for_retrieval(*args, **kwargs):
    return _helpers._query_for_retrieval(*args, **kwargs)


def _run_kb_retrieval(*args, **kwargs):
    _sync(_helpers, ["_orch_python", "subprocess", "KB_RETRIEVER_WIN"])
    return _helpers._run_kb_retrieval(*args, **kwargs)


def _investigation_bundle(*args, **kwargs):
    _sync(_helpers, ["run_orchestrator"])
    return _helpers._investigation_bundle(*args, **kwargs)


def _original_context_for_task(*args, **kwargs):
    _sync(_helpers, ["task_context_receipt", "task_source_context_receipt", "load_context_receipt"])
    return _helpers._original_context_for_task(*args, **kwargs)


def _context_ticket_or_original(*args, **kwargs):
    return _helpers._context_ticket_or_original(*args, **kwargs)


def _build_and_persist_stage_context(*args, **kwargs):
    _sync(_helpers, ["assemble_stage_context", "assemble_degraded_context", "persist_context_receipt"])
    return _helpers._build_and_persist_stage_context(*args, **kwargs)


def create_reviewer_card(*args, **kwargs):
    _sync(_cards, [
        "_original_context_for_task", "_ticket_snapshot", "_run_evidence_snapshot",
        "_build_and_persist_stage_context", "provenance_header", "run_hermes",
        "body_field", "task_review_cycle", "REVIEWER_PROFILE", "REVIEW_PRIORITY",
    ])
    return _cards.create_reviewer_card(*args, **kwargs)


def ensure_missing_reviewers(*args, **kwargs):
    _sync(_cards, [
        "list_tasks", "task_run_id", "safe_query_active_run", "_source_has_reviewer",
        "_source_has_rework", "_completion_metadata", "_proposal_complete", "create_reviewer_card",
        "INVESTIGATOR_PROFILES",
    ])
    return _cards.ensure_missing_reviewers(*args, **kwargs)


def create_rework_card(*args, **kwargs):
    _sync(_cards, [
        "task_run_id", "task_ticket_id", "task_review_cycle", "MAX_REVIEW_CYCLES",
        "_escalate_run", "list_tasks", "_source_has_rework", "_persist_rejected_ledger",
        "body_field", "_original_context_for_task", "_ticket_snapshot", "_run_evidence_snapshot",
        "_build_and_persist_stage_context", "provenance_header", "run_hermes",
        "INVESTIGATOR_PROFILE", "REWORK_PRIORITY",
    ])
    return _cards.create_rework_card(*args, **kwargs)


def scout(*args, **kwargs):
    _sync(_scout, [
        "reconcile", "load_workflow_binding", "_binding_ready_for_claims", "query_active_runs",
        "run_orchestrator", "_archive_stale_cards_for_ticket", "_build_and_persist_stage_context",
        "provenance_header", "_investigation_bundle", "_query_instructions", "run_hermes",
        "INVESTIGATOR_PROFILE", "NEW_INVESTIGATION_PRIORITY", "REWORK_PRIORITY", "REVIEW_PRIORITY",
        "DEFAULT_ELIGIBLE_STATUS",
    ])
    return _scout.scout(*args, **kwargs)


# Install only Phase-2 overrides into the unchanged lifecycle core. Existing
# reconciler functions resolve these globals at call time.
for _name, _value in {
    "task_context_receipt": task_context_receipt,
    "task_source_context_receipt": task_source_context_receipt,
    "_run_kb_retrieval": _run_kb_retrieval,
    "_investigation_bundle": _investigation_bundle,
    "create_reviewer_card": create_reviewer_card,
    "ensure_missing_reviewers": ensure_missing_reviewers,
    "create_rework_card": create_rework_card,
    "scout": scout,
}.items():
    globals()[_name] = _value
    setattr(_core, _name, _value)


if __name__ == "__main__":
    raise SystemExit(cli())
