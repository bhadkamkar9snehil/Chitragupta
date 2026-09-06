#!/usr/bin/env python3
"""Review/rework card constructors for Phase-2 L2 context delivery."""
from __future__ import annotations
from l2_pipeline_context_helpers import *

def create_reviewer_card(
    *,
    args: Any,
    source_task: dict[str, Any],
    proposal: dict[str, Any],
    dry_run: bool = False,
) -> Optional[str]:
    run_id = str(proposal["run_id"])
    ticket_id = str(proposal["ticket_id"])
    ticket_no = body_field(source_task.get("body"), "ticket_no") or ticket_id
    cycle = task_review_cycle(source_task)
    proposal_json = json.dumps(proposal, separators=(",", ":"), default=str)
    original_context, original_receipt = _original_context_for_task(source_task)
    ticket = _ticket_snapshot(args, ticket_id)
    current_run_evidence = _run_evidence_snapshot(args, run_id)
    envelope, rendered_context, receipt = _build_and_persist_stage_context(
        args=args,
        ticket=ticket,
        run_id=run_id,
        ticket_id=ticket_id,
        ticket_no=ticket_no,
        stage="review",
        review_cycle=cycle,
        dry_run=dry_run,
        proposal=proposal,
        current_run_evidence=current_run_evidence,
        original_context=original_context,
    )
    source_context_sha = (original_context or {}).get("context_sha256") or body_field(source_task.get("body"), "context_sha256") or "unknown"
    source_receipt_value = original_receipt or task_context_receipt(source_task) or "unknown"

    body = (
        f"run_id: {run_id}\n"
        f"ticket_id: {ticket_id}\n"
        f"ticket_no: {ticket_no}\n"
        f"investigation_task_id: {source_task['id']}\n"
        f"review_cycle: {cycle}\n"
        "pipeline_stage: review\n"
        + provenance_header(envelope, receipt)
        + f"source_context_sha256: {source_context_sha}\n"
        + f"source_context_receipt: {source_receipt_value}\n"
        + f"proposal_json: {proposal_json}\n\n"
        + rendered_context
        + "\n--- Reviewer contract ---\n"
        "Verify the frozen proposal against current live evidence. Specifically challenge unsupported root cause, "
        "response type, invented identifiers, analogy-as-proof, claimed writes without receipts, and relevant reopen/regression warnings. "
        "Approve with kanban_complete; reject with kanban_block. The deterministic reconciler owns publication/rework.\n"
    )
    argv = [
        "kanban", "create", f"REVIEW[{cycle}]: L2 {ticket_no}",
        "--assignee", REVIEWER_PROFILE,
        "--body", body,
        "--priority", str(REVIEW_PRIORITY),
        "--skill", "xstudio-l2-draft-verifier",
        "--skill", "xstudio-sql-write-discipline",
        "--idempotency-key", f"review-{run_id}-{cycle}-{source_task['id']}",
        "--max-runtime", "15m",
        "--json",
    ]
    if dry_run:
        print(f"[DRY RUN] create reviewer for {source_task['id']} cycle={cycle} context={envelope['context_sha256'][:12]}")
        return "dry-run"
    result = run_hermes(argv)
    if result.returncode != 0:
        print(f"WARNING: reviewer create failed for {source_task['id']}: {result.stderr.strip()[:300]}")
        return None
    try:
        return (json.loads(result.stdout) or {}).get("id")
    except json.JSONDecodeError:
        return None


def ensure_missing_reviewers(args: Any, *, dry_run: bool = False) -> int:
    tasks = list_tasks()
    created = 0
    for task in tasks:
        if task.get("status") != "done" or (task.get("assignee") or "") not in INVESTIGATOR_PROFILES:
            continue
        run_id = task_run_id(task)
        if not run_id or not safe_query_active_run(run_id, args):
            continue
        if _source_has_reviewer(tasks, task["id"]) or _source_has_rework(tasks, task["id"]):
            continue
        proposal = _completion_metadata(task)
        if not _proposal_complete(proposal):
            continue
        if create_reviewer_card(args=args, source_task=task, proposal=proposal or {}, dry_run=dry_run):
            created += 1
    return created


def create_rework_card(
    args: Any,
    *,
    source_task: dict[str, Any],
    reason: str,
    investigation_task_id: Optional[str],
    dry_run: bool = False,
) -> Optional[str]:
    run_id, ticket_id = task_run_id(source_task), task_ticket_id(source_task)
    if not run_id or not ticket_id:
        return None
    current_cycle = task_review_cycle(source_task)
    next_cycle = current_cycle + 1
    if next_cycle >= MAX_REVIEW_CYCLES:
        return "escalated" if _escalate_run(
            args,
            run_id=run_id,
            ticket_id=ticket_id,
            reason=reason,
            cycle=current_cycle,
            dry_run=dry_run,
        ) else None

    tasks = list_tasks()
    if _source_has_rework(tasks, source_task["id"]):
        return None

    prior = "" if dry_run else _persist_rejected_ledger(args, investigation_task_id, run_id)
    ticket_no = body_field(source_task.get("body"), "ticket_no") or ticket_id
    original_context, original_receipt = _original_context_for_task(source_task)
    ticket = _ticket_snapshot(args, ticket_id)
    current_run_evidence = _run_evidence_snapshot(args, run_id)
    original_proposal = task_proposal(source_task)
    envelope, rendered_context, receipt = _build_and_persist_stage_context(
        args=args,
        ticket=ticket,
        run_id=run_id,
        ticket_id=ticket_id,
        ticket_no=ticket_no,
        stage="rework",
        review_cycle=next_cycle,
        dry_run=dry_run,
        proposal=original_proposal,
        current_run_evidence=current_run_evidence,
        rejection_reason=reason,
        original_context=original_context,
    )
    source_context_sha = (original_context or {}).get("context_sha256") or body_field(source_task.get("body"), "source_context_sha256") or "unknown"
    source_receipt_value = original_receipt or task_source_context_receipt(source_task) or task_context_receipt(source_task) or "unknown"

    body = (
        f"run_id: {run_id}\n"
        f"ticket_id: {ticket_id}\n"
        f"ticket_no: {ticket_no}\n"
        f"review_cycle: {next_cycle}\n"
        f"rework_source_id: {source_task['id']}\n"
        f"prior_investigation_task_id: {investigation_task_id or 'unknown'}\n"
        "pipeline_stage: rework\n"
        + provenance_header(envelope, receipt)
        + f"source_context_sha256: {source_context_sha}\n"
        + f"source_context_receipt: {source_receipt_value}\n\n"
        + rendered_context
        + f"\nREWORK REASON:\n{reason}\n\n"
        "Address this exact rejected/invalid point using current live evidence. Reuse prior verified findings; "
        "do not restart the entire investigation unless the objection invalidates them. The prior rejected hypothesis "
        "is negative evidence, not trusted truth. Complete with the full structured metadata contract.\n"
    )
    if prior:
        body += f"\nPRIOR FINDINGS / REJECTED ATTEMPT (verbatim provenance):\n{prior}\n"

    argv = [
        "kanban", "create", f"REWORK[{next_cycle}]: L2 {ticket_no}",
        "--body", body,
        "--assignee", INVESTIGATOR_PROFILE,
        "--priority", str(REWORK_PRIORITY),
        "--skill", "xstudio-l2-ticket-workflow",
        "--skill", "xstudio-sql-write-discipline",
        "--idempotency-key", f"rework-{source_task['id']}",
        "--max-runtime", "20m",
        "--json",
    ]
    if dry_run:
        print(f"[DRY RUN] create rework from {source_task['id']} cycle={next_cycle} context={envelope['context_sha256'][:12]}")
        return "dry-run"
    result = run_hermes(argv)
    if result.returncode != 0:
        print(f"WARNING: rework create failed for {source_task['id']}: {result.stderr.strip()[:300]}")
        return None
    try:
        return (json.loads(result.stdout) or {}).get("id") or "created"
    except json.JSONDecodeError:
        return "created"



__all__=[name for name in globals() if not name.startswith("__")]
