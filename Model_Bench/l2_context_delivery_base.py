#!/usr/bin/env python3
"""Harness-owned deterministic context assembly for Chitragupta L2.

This module owns no ticket lifecycle state and performs no model reasoning.
It converts requester-grounded ticket data plus governed retrieval results into
a bounded, stage-specific L2ContextEnvelope, renders exactly what the worker
receives, and persists an auditable receipt.

GBrain is a derived ranking/index layer. Delivered content comes from validated
source files. Historical cases are analogies/counterexamples only; live XStudio
evidence remains current-ticket truth.
"""
from __future__ import annotations

import copy
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping

import kb_retrieval as kb
from l2_context_envelope import (
    SCHEMA_VERSION,
    build_context_envelope,
    make_context_item,
    validate_context_envelope,
)

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_POLICY = ROOT / "deploy" / "l2_context_policy.json"
DEPLOYED_POLICY = Path(__file__).resolve().parent / "l2_context_policy.json"
DEFAULT_VAULT = Path.home() / ".hermes" / "l2-learning"
REQUESTER_FIELDS = (
    "BriefDetails",
    "Description",
    "ProblemCategory",
    "HermesAreaName",
    "ExtractedEntitiesJson",
)
STAGES = ("investigation", "review", "rework")

SECTION_TITLES = {
    "canonical_documents": "CANONICAL PROCEDURE / REFERENCE",
    "promoted_facts": "REVIEWED REUSABLE FACTS",
    "governed_solutions": "GOVERNED REUSABLE SOLUTIONS",
    "approved_cases": "APPROVED HISTORICAL ANALOGIES — NOT CURRENT PROOF",
    "rejected_cases": "REVIEWER-REJECTED HISTORICAL PATTERNS — NEGATIVE EXAMPLES",
    "reopened_cases": "REOPENED / REGRESSION HISTORY — WARNING SIGNALS",
    "prior_ticket_evidence": "CURRENT-RUN / PRIOR VERIFIED TICKET EVIDENCE",
}

DEFAULT_DROP_ORDER = {
    "investigation": [
        "reopened_cases",
        "rejected_cases",
        "approved_cases",
        "governed_solutions",
        "promoted_facts",
        "route_canonical",
    ],
    "review": [
        "approved_cases",
        "governed_solutions",
        "promoted_facts",
        "route_canonical",
        "rejected_cases",
        "reopened_cases",
    ],
    "rework": [
        "approved_cases",
        "governed_solutions",
        "promoted_facts",
        "route_canonical",
        "rejected_cases",
        "reopened_cases",
    ],
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def vault_path(value: str | Path | None = None) -> Path:
    if value:
        return Path(value).expanduser()
    raw = os.environ.get("CHITRAGUPTA_L2_LEARNING_VAULT", "").strip()
    return Path(raw).expanduser() if raw else DEFAULT_VAULT


def normalize_whitespace(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def _stable_field_text(value: Any) -> str:
    if value in (None, ""):
        return ""
    if isinstance(value, str):
        return value
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, default=str)


def build_requester_retrieval_query(ticket: Mapping[str, Any]) -> str:
    """Build initial retrieval query only from requester/system-grounded fields."""
    parts = [_stable_field_text(ticket.get(field)) for field in REQUESTER_FIELDS]
    return normalize_whitespace(" ".join(part for part in parts if part))


def _policy_candidates(path: Path | None = None) -> list[Path]:
    if path is not None:
        return [path]
    configured = os.environ.get("CHITRAGUPTA_L2_CONTEXT_POLICY", "").strip()
    out = [Path(configured).expanduser()] if configured else []
    out.extend([DEFAULT_POLICY, DEPLOYED_POLICY])
    return out


def load_context_policy(path: Path | None = None) -> dict[str, Any]:
    candidates = _policy_candidates(path)
    selected = next((candidate for candidate in candidates if candidate.is_file()), None)
    if selected is None:
        raise FileNotFoundError(
            "L2 context policy not found; checked: "
            + ", ".join(str(candidate) for candidate in candidates)
        )
    data = json.loads(selected.read_text(encoding="utf-8"))
    errors = validate_context_policy(data)
    if errors:
        raise ValueError("invalid L2 context policy: " + "; ".join(errors))
    return data


def validate_context_policy(policy: Any) -> list[str]:
    if not isinstance(policy, dict):
        return ["context policy must be an object"]
    errors: list[str] = []
    if policy.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    maximum = policy.get("maximum_total_rendered_context_characters")
    if not isinstance(maximum, int) or isinstance(maximum, bool) or maximum < 4000 or maximum > 120000:
        errors.append("maximum_total_rendered_context_characters must be an integer between 4000 and 120000")
    route_docs = policy.get("route_canonical_documents")
    if not isinstance(route_docs, int) or isinstance(route_docs, bool) or route_docs < 0 or route_docs > 10:
        errors.append("route_canonical_documents must be an integer between 0 and 10")
    for stage in STAGES:
        cfg = policy.get(stage)
        if not isinstance(cfg, dict):
            errors.append(f"{stage} must be an object")
            continue
        for key in ("facts", "solutions", "approved_cases", "rejected_cases", "reopened_cases"):
            value = cfg.get(key)
            if not isinstance(value, int) or isinstance(value, bool) or value < 0 or value > 10:
                errors.append(f"{stage}.{key} must be an integer between 0 and 10")
        drop = cfg.get("drop_order")
        if drop is not None and (
            not isinstance(drop, list) or not all(isinstance(v, str) and v for v in drop)
        ):
            errors.append(f"{stage}.drop_order must be an array of strings")
    return errors


def _stage_limits(policy: dict[str, Any], stage: str) -> dict[str, int]:
    if stage not in STAGES:
        raise ValueError(f"unsupported pipeline stage: {stage}")
    cfg = policy[stage]
    return {
        "facts": cfg["facts"],
        "solutions": cfg["solutions"],
        "approved_cases": cfg["approved_cases"],
        "rejected_cases": cfg["rejected_cases"],
        "reopened_cases": cfg["reopened_cases"],
    }


def _route_reason_strings(routes: list[dict[str, Any]]) -> list[str]:
    out: list[str] = []
    for candidate in routes:
        route = str(candidate.get("route") or "")
        for reason in candidate.get("reasons") or []:
            out.append(f"{route}: {reason}")
    return out or ["discover: no deterministic route signal"]


def _successful_canonical(values: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [dict(v) for v in values if v.get("source_ref") and not v.get("error")]


def _split_canonical(values: list[dict[str, Any]], route_limit: int) -> list[dict[str, Any]]:
    always = [v for v in values if v.get("reason") == "always_load"]
    route = [v for v in values if v.get("reason") != "always_load"][:route_limit]
    return always + route


def _copy_limited(values: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    return [copy.deepcopy(v) for v in values[:max(0, limit)]]


def _make_evidence_item(
    *,
    source_type: str,
    source_ref: str,
    title: str,
    content: Any,
    trust_class: str = "current_run_evidence",
) -> dict[str, Any]:
    return make_context_item(
        source_type=source_type,
        source_ref=source_ref,
        trust_class=trust_class,
        title=title,
        content=_stable_field_text(content),
        verification_required=False,
    )


def _render_item(item: Mapping[str, Any]) -> str:
    verification = "YES" if item.get("verification_required") else "NO"
    rank = item.get("retrieval_rank")
    score = item.get("retrieval_score")
    meta = [
        f"source={item.get('source_ref')}",
        f"trust={item.get('trust_class')}",
        f"live_verification_required={verification}",
    ]
    if rank is not None:
        meta.append(f"rank={rank}")
    if score is not None:
        meta.append(f"score={score}")
    return (
        f"### {item.get('title') or item.get('source_ref')}\n"
        f"[{' | '.join(meta)}]\n\n"
        f"{item.get('content') or ''}\n"
    )


def render_context_envelope(envelope: Mapping[str, Any]) -> str:
    errors = validate_context_envelope(envelope)
    if errors:
        raise ValueError("cannot render invalid context envelope: " + "; ".join(errors))
    retrieval = envelope["retrieval"]
    lines = [
        "=== HARNESS-PROVIDED GOVERNED CONTEXT ===",
        "This context was selected by deterministic harness policy; the worker did not author or retrieve it.",
        "Authority order: current live XStudio/SQL evidence > lifecycle state > canonical reference > reviewed facts/Solutions > historical cases.",
        "Historical similarity is never proof of this ticket. Verify current-ticket claims live.",
        f"context_schema_version: {envelope['schema_version']}",
        f"context_sha256: {envelope['context_sha256']}",
        f"query_sha256: {envelope['query_sha256']}",
        f"pipeline_stage: {envelope['pipeline_stage']}",
        f"route: {envelope['route']}",
        f"retrieval_degraded: {str(retrieval['retrieval_degraded']).lower()}",
    ]
    if retrieval["retrieval_degraded"]:
        lines += [
            f"degradation_reason: {retrieval.get('degradation_reason') or 'historical retrieval degraded'}",
            "",
            "IMPORTANT: Historical retrieval is degraded/unavailable. Do not infer historical precedent. "
            "Use current live evidence and canonical procedure.",
        ]
    lines += ["", "REQUESTER-GROUNDED RETRIEVAL QUERY", envelope["requester_query"] or "(empty)", ""]
    for collection in (
        "canonical_documents",
        "promoted_facts",
        "governed_solutions",
        "approved_cases",
        "rejected_cases",
        "reopened_cases",
        "prior_ticket_evidence",
    ):
        values = envelope.get(collection) or []
        if not values:
            continue
        lines += [SECTION_TITLES[collection], "-" * len(SECTION_TITLES[collection])]
        for item in values:
            lines.append(_render_item(item))
        lines.append("")
    lines += [
        "LIVE-VERIFICATION RULE",
        "Use xstudio_l2/current harness evidence before asserting current state, root cause, or resolution applicability.",
        "=== END HARNESS-PROVIDED GOVERNED CONTEXT ===",
    ]
    return "\n".join(lines).strip() + "\n"


def _drop_one(selected: dict[str, list[dict[str, Any]]], target: str) -> bool:
    if target == "route_canonical":
        for index in range(len(selected["canonical_documents"]) - 1, -1, -1):
            if selected["canonical_documents"][index].get("reason") != "always_load":
                selected["canonical_documents"].pop(index)
                return True
        return False
    values = selected.get(target)
    if values:
        values.pop()
        return True
    return False


def _collection_counts(selected: Mapping[str, list[dict[str, Any]]]) -> dict[str, int]:
    return {key: len(value) for key, value in selected.items()}


def _build_envelope(
    *,
    run_id: str,
    ticket_id: str,
    ticket_no: str,
    stage: str,
    review_cycle: int,
    query: str,
    routes: list[dict[str, Any]],
    selected: dict[str, list[dict[str, Any]]],
    gbrain_sources: list[str],
    degraded: bool,
    degradation_reason: str | None,
    retrieval_extra: dict[str, Any],
) -> dict[str, Any]:
    primary_route = str((routes[0] if routes else {}).get("route") or "discover")
    return build_context_envelope(
        generated_at=utc_now(),
        run_id=run_id,
        ticket_id=ticket_id,
        ticket_no=ticket_no,
        pipeline_stage=stage,
        review_cycle=review_cycle,
        route=primary_route,
        route_reasons=_route_reason_strings(routes),
        requester_query=query,
        canonical_documents=selected["canonical_documents"],
        promoted_facts=selected["promoted_facts"],
        governed_solutions=selected["governed_solutions"],
        approved_cases=selected["approved_cases"],
        rejected_cases=selected["rejected_cases"],
        reopened_cases=selected["reopened_cases"],
        prior_ticket_evidence=selected["prior_ticket_evidence"],
        retrieval_backend="manifest+authoritative-files+gbrain-ranking",
        gbrain_sources=gbrain_sources,
        gbrain_query=query,
        retrieval_degraded=degraded,
        degradation_reason=degradation_reason,
        **retrieval_extra,
    )



__all__ = [name for name in globals() if not name.startswith("__")]
