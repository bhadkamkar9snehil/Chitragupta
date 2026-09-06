#!/usr/bin/env python3
"""Stage assembly for deterministic L2 context delivery."""
from __future__ import annotations
from l2_context_delivery_base import *

def assemble_stage_context(
    *,
    ticket: Mapping[str, Any],
    run_id: str,
    ticket_id: str,
    ticket_no: str,
    stage: str,
    review_cycle: int,
    policy: dict[str, Any] | None = None,
    policy_path: Path | None = None,
    manifest: dict[str, Any] | None = None,
    vault: Path | None = None,
    root: Path | None = None,
    proposal: Mapping[str, Any] | None = None,
    current_run_evidence: Any = None,
    rejection_reason: str | None = None,
    original_context: Mapping[str, Any] | None = None,
    include_gbrain: bool = True,
) -> tuple[dict[str, Any], str]:
    """Build, budget, hash and render one stage context."""
    policy = policy or load_context_policy(policy_path)
    if stage not in STAGES:
        raise ValueError(f"unsupported pipeline stage: {stage}")
    vault = vault or vault_path()
    query = build_requester_retrieval_query(ticket)

    limits = _stage_limits(policy, stage)
    retrieval = kb.retrieve(
        query,
        manifest if manifest is not None else kb.load_manifest(),
        vault=vault,
        root=root,
        top=max([1, *limits.values()]),
        include_gbrain=include_gbrain,
        limits=limits,
    )
    routes = retrieval.get("route_candidates") or [{"route": "discover", "reasons": ["no deterministic route signal"]}]
    canonical = _split_canonical(
        _successful_canonical(retrieval.get("canonical_documents") or []),
        int(policy["route_canonical_documents"]),
    )

    selected = {
        "canonical_documents": canonical,
        "promoted_facts": _copy_limited(retrieval.get("promoted_facts") or [], limits["facts"]),
        "governed_solutions": _copy_limited(retrieval.get("governed_solutions") or [], limits["solutions"]),
        "approved_cases": _copy_limited(retrieval.get("approved_cases") or [], limits["approved_cases"]),
        "rejected_cases": _copy_limited(retrieval.get("rejected_cases") or [], limits["rejected_cases"]),
        "reopened_cases": _copy_limited(retrieval.get("reopened_cases") or [], limits["reopened_cases"]),
        "prior_ticket_evidence": [],
    }

    # Reviewer/rework get explicit current-run evidence rather than relying on historical similarity.
    if proposal:
        selected["prior_ticket_evidence"].append(_make_evidence_item(
            source_type="frozen_proposal",
            source_ref=f"run:{run_id}/proposal/review-cycle:{review_cycle}",
            title="Frozen investigator proposal",
            content=proposal,
        ))
    if current_run_evidence not in (None, "", [], {}):
        selected["prior_ticket_evidence"].append(_make_evidence_item(
            source_type="current_run_evidence",
            source_ref=f"run:{run_id}/actions",
            title="Current run action/evidence receipt",
            content=current_run_evidence,
        ))
    if rejection_reason:
        selected["prior_ticket_evidence"].append(_make_evidence_item(
            source_type="reviewer_rejection",
            source_ref=f"run:{run_id}/review-cycle:{review_cycle}/rejection",
            title="Reviewer rejection reason",
            content=rejection_reason,
            trust_class="prior_rejected_reasoning",
        ))
    if original_context:
        selected["prior_ticket_evidence"].append(_make_evidence_item(
            source_type="original_context_identity",
            source_ref=f"context:{original_context.get('context_sha256') or 'unknown'}",
            title="Original governed context identity",
            content={
                "context_sha256": original_context.get("context_sha256"),
                "query_sha256": original_context.get("query_sha256"),
                "route": original_context.get("route"),
                "retrieval_degraded": (original_context.get("retrieval") or {}).get("retrieval_degraded"),
            },
        ))

    initial_counts = _collection_counts(selected)
    gbrain_results = retrieval.get("gbrain") or {}
    gbrain_sources = sorted({
        str(source)
        for result in gbrain_results.values()
        if isinstance(result, dict)
        for source in (result.get("source_ids") or [])
        if source
    })
    degradation_reasons = [str(v) for v in retrieval.get("degradation_reasons") or [] if str(v).strip()]
    degraded = bool(retrieval.get("retrieval_degraded"))
    degradation_reason = "; ".join(degradation_reasons)[:2000] if degraded else None

    dropped = {key: 0 for key in selected}
    max_chars = int(policy["maximum_total_rendered_context_characters"])
    drop_order = policy[stage].get("drop_order") or DEFAULT_DROP_ORDER[stage]

    # Build/render iteratively so the hash always describes exactly what was delivered.
    while True:
        delivered_counts = _collection_counts(selected)
        retrieval_extra = {
            "stage_policy": stage,
            "delivered_counts": delivered_counts,
            "dropped_counts": dropped,
            "source_hit_counts": {
                key: len(kb._iter_gbrain_rows(value.get("results")))
                for key, value in gbrain_results.items()
                if isinstance(value, dict)
            },
            "live_sql_leads": retrieval.get("live_sql_leads") or [],
        }
        envelope = _build_envelope(
            run_id=run_id,
            ticket_id=ticket_id,
            ticket_no=ticket_no,
            stage=stage,
            review_cycle=review_cycle,
            query=query,
            routes=routes,
            selected=selected,
            gbrain_sources=gbrain_sources,
            degraded=degraded,
            degradation_reason=degradation_reason,
            retrieval_extra=retrieval_extra,
        )
        rendered = render_context_envelope(envelope)
        if len(rendered) <= max_chars:
            break
        removed = False
        for target in drop_order:
            before = _collection_counts(selected)
            if _drop_one(selected, target):
                after = _collection_counts(selected)
                if target == "route_canonical":
                    dropped["canonical_documents"] += before["canonical_documents"] - after["canonical_documents"]
                elif target in dropped:
                    dropped[target] += before[target] - after[target]
                removed = True
                break
        if not removed:
            raise ValueError(
                f"mandatory L2 context exceeds policy budget ({len(rendered)} > {max_chars}); "
                "refusing partial-item truncation"
            )

    # Final integrity check.
    errors = validate_context_envelope(envelope)
    if errors:
        raise ValueError("assembled invalid L2 context envelope: " + "; ".join(errors))
    return envelope, rendered



def assemble_degraded_context(
    *,
    ticket: Mapping[str, Any],
    run_id: str,
    ticket_id: str,
    ticket_no: str,
    stage: str,
    review_cycle: int,
    reason: str,
    proposal: Mapping[str, Any] | None = None,
    current_run_evidence: Any = None,
    rejection_reason: str | None = None,
    original_context: Mapping[str, Any] | None = None,
) -> tuple[dict[str, Any], str]:
    """Build a valid fail-closed envelope when normal retrieval cannot run at all.

    This is intentionally not a broad-search fallback. It provides only requester-grounded
    identity plus current-run/prior provenance supplied by the harness, marks historical
    retrieval degraded, and tells the worker to rely on live typed evidence.
    """
    if stage not in STAGES:
        raise ValueError(f"unsupported pipeline stage: {stage}")
    query = build_requester_retrieval_query(ticket)
    prior: list[dict[str, Any]] = []
    if proposal:
        prior.append(_make_evidence_item(
            source_type="frozen_proposal",
            source_ref=f"run:{run_id}/proposal/review-cycle:{review_cycle}",
            title="Frozen investigator proposal",
            content=proposal,
        ))
    if current_run_evidence not in (None, "", [], {}):
        prior.append(_make_evidence_item(
            source_type="current_run_evidence",
            source_ref=f"run:{run_id}/actions",
            title="Current run action/evidence receipt",
            content=current_run_evidence,
        ))
    if rejection_reason:
        prior.append(_make_evidence_item(
            source_type="reviewer_rejection",
            source_ref=f"run:{run_id}/review-cycle:{review_cycle}/rejection",
            title="Reviewer rejection reason",
            content=rejection_reason,
            trust_class="prior_rejected_reasoning",
        ))
    if original_context:
        prior.append(_make_evidence_item(
            source_type="original_context_identity",
            source_ref=f"context:{original_context.get('context_sha256') or 'unknown'}",
            title="Original governed context identity",
            content={
                "context_sha256": original_context.get("context_sha256"),
                "query_sha256": original_context.get("query_sha256"),
                "route": original_context.get("route"),
                "retrieval_degraded": (original_context.get("retrieval") or {}).get("retrieval_degraded"),
            },
        ))
    envelope = build_context_envelope(
        generated_at=utc_now(),
        run_id=run_id,
        ticket_id=ticket_id,
        ticket_no=ticket_no,
        pipeline_stage=stage,
        review_cycle=review_cycle,
        route="discover",
        route_reasons=["context assembly failed before governed retrieval completed"],
        requester_query=query,
        prior_ticket_evidence=prior,
        retrieval_backend="degraded-harness-fallback",
        gbrain_sources=[],
        gbrain_query=query,
        retrieval_degraded=True,
        degradation_reason=normalize_whitespace(reason)[:2000] or "governed context assembly failed",
        stage_policy=stage,
        delivered_counts={
            "canonical_documents": 0,
            "promoted_facts": 0,
            "governed_solutions": 0,
            "approved_cases": 0,
            "rejected_cases": 0,
            "reopened_cases": 0,
            "prior_ticket_evidence": len(prior),
        },
        dropped_counts={},
        source_hit_counts={},
        live_sql_leads=[],
    )
    return envelope, render_context_envelope(envelope)


__all__ = [name for name in globals() if not name.startswith("__")]
