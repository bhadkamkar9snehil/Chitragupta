#!/usr/bin/env python3
"""Deterministic context-envelope contract for Chitragupta L2 workers.

The envelope is the durable interface between harness-owned retrieval and model
reasoning.  It records the exact governed material delivered to a worker,
including trust classification, provenance, retrieval metadata and a canonical
SHA-256 identity.

This module is intentionally pure: it performs no SQL, Hermes, GBrain, file or
network I/O.  Retrieval and lifecycle code build envelopes; this module only
normalizes, validates and hashes them.
"""
from __future__ import annotations

import copy
import hashlib
import json
from typing import Any, Mapping

SCHEMA_VERSION = 1

CONTEXT_COLLECTIONS = (
    "canonical_documents",
    "promoted_facts",
    "governed_solutions",
    "approved_cases",
    "rejected_cases",
    "reopened_cases",
    "prior_ticket_evidence",
)

REQUIRED_ITEM_FIELDS = (
    "source_type",
    "source_ref",
    "trust_class",
    "title",
    "content",
    "content_sha256",
    "retrieval_rank",
    "retrieval_score",
    "verification_required",
)

# Trust classification is structural, not prompt advice.  A record whose trust
# class does not belong in a collection is rejected before it can be delivered.
ALLOWED_TRUST_BY_COLLECTION: dict[str, frozenset[str]] = {
    "canonical_documents": frozenset({"canonical_reference", "canonical_procedure"}),
    "promoted_facts": frozenset({"reviewed_operational", "reviewed_operational_heuristic"}),
    "governed_solutions": frozenset({"governed_reusable_solution"}),
    "approved_cases": frozenset({"reviewed_published_historical_case"}),
    "rejected_cases": frozenset({"reviewed_negative_example"}),
    "reopened_cases": frozenset({"observed_resolution_regression"}),
    "prior_ticket_evidence": frozenset({
        "current_ticket_evidence",
        "current_run_evidence",
        "prior_verified_ticket_evidence",
        "prior_rejected_reasoning",
        "original_governed_context_snapshot",
    }),
}

# These arrays are sets semantically. Ranked retrieval/result arrays remain
# order-sensitive and are deliberately not sorted by the hash normalizer.
UNORDERED_TOP_LEVEL_LISTS = frozenset({"route_reasons"})
UNORDERED_RETRIEVAL_LISTS = frozenset({"gbrain_sources"})


def canonical_json(value: Any) -> str:
    """Canonical JSON representation used for every deterministic digest."""
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        default=str,
    )


def sha256_text(value: str) -> str:
    return hashlib.sha256((value or "").encode("utf-8")).hexdigest()


def content_sha256(content: str) -> str:
    return sha256_text(content)


def make_context_item(
    *,
    source_type: str,
    source_ref: str,
    trust_class: str,
    title: str,
    content: str,
    retrieval_rank: int | None = None,
    retrieval_score: float | int | None = None,
    verification_required: bool = True,
    **extra: Any,
) -> dict[str, Any]:
    """Create a context item whose digest covers the exact delivered content."""
    item: dict[str, Any] = {
        "source_type": str(source_type),
        "source_ref": str(source_ref),
        "trust_class": str(trust_class),
        "title": str(title),
        "content": str(content),
        "content_sha256": content_sha256(str(content)),
        "retrieval_rank": retrieval_rank,
        "retrieval_score": retrieval_score,
        "verification_required": bool(verification_required),
    }
    item.update(extra)
    return item


def _normalized_unordered_strings(value: Any) -> list[str]:
    if not isinstance(value, list):
        return value
    return sorted({str(item) for item in value})


def normalized_for_hash(envelope: Mapping[str, Any]) -> dict[str, Any]:
    """Return the canonical hash view without destroying ranked-list order.

    Only fields explicitly declared semantically unordered are normalized.
    Context result collections remain in delivered/ranked order, so reordering
    two retrieved items changes the context identity.
    """
    out = copy.deepcopy(dict(envelope))
    out.pop("context_sha256", None)
    for key in UNORDERED_TOP_LEVEL_LISTS:
        if key in out:
            out[key] = _normalized_unordered_strings(out[key])
    retrieval = out.get("retrieval")
    if isinstance(retrieval, dict):
        for key in UNORDERED_RETRIEVAL_LISTS:
            if key in retrieval:
                retrieval[key] = _normalized_unordered_strings(retrieval[key])
    return out


def compute_context_sha256(envelope: Mapping[str, Any]) -> str:
    payload = canonical_json(normalized_for_hash(envelope))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _require_nonempty_string(value: Any, label: str, errors: list[str]) -> None:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{label} must be a non-empty string")


def _validate_item(item: Any, collection: str, index: int, errors: list[str]) -> None:
    label = f"{collection}[{index}]"
    if not isinstance(item, dict):
        errors.append(f"{label} must be an object")
        return
    missing = [field for field in REQUIRED_ITEM_FIELDS if field not in item]
    if missing:
        errors.append(f"{label} missing required fields: {', '.join(missing)}")
        return

    for field in ("source_type", "source_ref", "trust_class", "title"):
        _require_nonempty_string(item.get(field), f"{label}.{field}", errors)
    if not isinstance(item.get("content"), str):
        errors.append(f"{label}.content must be a string")
    else:
        expected = content_sha256(item["content"])
        if item.get("content_sha256") != expected:
            errors.append(f"{label}.content_sha256 does not match delivered content")

    rank = item.get("retrieval_rank")
    if rank is not None and (not isinstance(rank, int) or isinstance(rank, bool) or rank < 1):
        errors.append(f"{label}.retrieval_rank must be null or an integer >= 1")
    score = item.get("retrieval_score")
    if score is not None and (not isinstance(score, (int, float)) or isinstance(score, bool)):
        errors.append(f"{label}.retrieval_score must be null or numeric")
    if not isinstance(item.get("verification_required"), bool):
        errors.append(f"{label}.verification_required must be boolean")

    trust = str(item.get("trust_class") or "")
    allowed = ALLOWED_TRUST_BY_COLLECTION[collection]
    if trust not in allowed:
        errors.append(
            f"{label}.trust_class {trust!r} is not allowed in {collection}; "
            f"allowed={sorted(allowed)}"
        )


def validate_context_envelope(envelope: Mapping[str, Any], *, require_hash: bool = True) -> list[str]:
    """Return validation errors; an empty list means the envelope is valid."""
    errors: list[str] = []
    if not isinstance(envelope, Mapping):
        return ["context envelope must be an object"]

    if envelope.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"schema_version must be {SCHEMA_VERSION}")

    for field in ("generated_at", "run_id", "ticket_id", "ticket_no", "pipeline_stage", "route"):
        _require_nonempty_string(envelope.get(field), field, errors)

    review_cycle = envelope.get("review_cycle")
    if not isinstance(review_cycle, int) or isinstance(review_cycle, bool) or review_cycle < 0:
        errors.append("review_cycle must be an integer >= 0")

    reasons = envelope.get("route_reasons")
    if not isinstance(reasons, list) or not all(isinstance(v, str) for v in reasons):
        errors.append("route_reasons must be an array of strings")

    requester_query = envelope.get("requester_query")
    if not isinstance(requester_query, str):
        errors.append("requester_query must be a string")
    elif envelope.get("query_sha256") != sha256_text(requester_query):
        errors.append("query_sha256 does not match requester_query")

    for collection in CONTEXT_COLLECTIONS:
        values = envelope.get(collection)
        if not isinstance(values, list):
            errors.append(f"{collection} must be an array")
            continue
        for index, item in enumerate(values):
            _validate_item(item, collection, index, errors)

    retrieval = envelope.get("retrieval")
    if not isinstance(retrieval, dict):
        errors.append("retrieval must be an object")
    else:
        _require_nonempty_string(retrieval.get("backend"), "retrieval.backend", errors)
        sources = retrieval.get("gbrain_sources")
        if not isinstance(sources, list) or not all(isinstance(v, str) and v for v in sources):
            errors.append("retrieval.gbrain_sources must be an array of non-empty strings")
        gbrain_query = retrieval.get("gbrain_query")
        if not isinstance(gbrain_query, str):
            errors.append("retrieval.gbrain_query must be a string")
        elif retrieval.get("gbrain_query_sha256") != sha256_text(gbrain_query):
            errors.append("retrieval.gbrain_query_sha256 does not match retrieval.gbrain_query")
        if not isinstance(retrieval.get("retrieval_degraded"), bool):
            errors.append("retrieval.retrieval_degraded must be boolean")
        reason = retrieval.get("degradation_reason")
        if reason is not None and not isinstance(reason, str):
            errors.append("retrieval.degradation_reason must be null or a string")
        if retrieval.get("retrieval_degraded") and not str(reason or "").strip():
            errors.append("retrieval.degradation_reason is required when retrieval is degraded")

    if require_hash:
        digest = envelope.get("context_sha256")
        if not isinstance(digest, str) or len(digest) != 64:
            errors.append("context_sha256 must be a 64-character SHA-256 hex digest")
        elif digest != compute_context_sha256(envelope):
            errors.append("context_sha256 does not match the canonical envelope")
    return errors


def finalize_context_envelope(envelope: Mapping[str, Any]) -> dict[str, Any]:
    """Normalize semantically unordered fields, validate, and attach the hash."""
    out = copy.deepcopy(dict(envelope))
    out["schema_version"] = SCHEMA_VERSION
    for key in UNORDERED_TOP_LEVEL_LISTS:
        if key in out:
            out[key] = _normalized_unordered_strings(out[key])
    retrieval = out.get("retrieval")
    if isinstance(retrieval, dict):
        for key in UNORDERED_RETRIEVAL_LISTS:
            if key in retrieval:
                retrieval[key] = _normalized_unordered_strings(retrieval[key])

    errors = validate_context_envelope(out, require_hash=False)
    if errors:
        raise ValueError("invalid L2 context envelope: " + "; ".join(errors))
    out["context_sha256"] = compute_context_sha256(out)
    return out


def build_context_envelope(
    *,
    generated_at: str,
    run_id: str,
    ticket_id: str,
    ticket_no: str,
    pipeline_stage: str,
    review_cycle: int,
    route: str,
    route_reasons: list[str],
    requester_query: str,
    canonical_documents: list[dict[str, Any]] | None = None,
    promoted_facts: list[dict[str, Any]] | None = None,
    governed_solutions: list[dict[str, Any]] | None = None,
    approved_cases: list[dict[str, Any]] | None = None,
    rejected_cases: list[dict[str, Any]] | None = None,
    reopened_cases: list[dict[str, Any]] | None = None,
    prior_ticket_evidence: list[dict[str, Any]] | None = None,
    retrieval_backend: str = "gbrain",
    gbrain_sources: list[str] | None = None,
    gbrain_query: str = "",
    retrieval_degraded: bool = False,
    degradation_reason: str | None = None,
    **retrieval_extra: Any,
) -> dict[str, Any]:
    retrieval: dict[str, Any] = {
        "backend": retrieval_backend,
        "gbrain_sources": list(gbrain_sources or []),
        "gbrain_query": gbrain_query,
        "gbrain_query_sha256": sha256_text(gbrain_query),
        "retrieval_degraded": retrieval_degraded,
        "degradation_reason": degradation_reason,
    }
    retrieval.update(retrieval_extra)
    return finalize_context_envelope({
        "schema_version": SCHEMA_VERSION,
        "generated_at": generated_at,
        "run_id": run_id,
        "ticket_id": ticket_id,
        "ticket_no": ticket_no,
        "pipeline_stage": pipeline_stage,
        "review_cycle": review_cycle,
        "route": route,
        "route_reasons": list(route_reasons),
        "requester_query": requester_query,
        "query_sha256": sha256_text(requester_query),
        "canonical_documents": list(canonical_documents or []),
        "promoted_facts": list(promoted_facts or []),
        "governed_solutions": list(governed_solutions or []),
        "approved_cases": list(approved_cases or []),
        "rejected_cases": list(rejected_cases or []),
        "reopened_cases": list(reopened_cases or []),
        "prior_ticket_evidence": list(prior_ticket_evidence or []),
        "retrieval": retrieval,
    })
