#!/usr/bin/env python3
"""Adapter giving l2_context_delivery_assembly.assemble_stage_context() the
retrieve(query, manifest, ...) call shape it expects (`kb.retrieve(...)`),
sourced from what this branch actually has -- without replacing kb_retrieval.py.

Why this exists: l2_context_delivery_base.py does `import kb_retrieval as kb`
and calls `kb.retrieve(query, manifest, vault=..., root=..., top=..., include_gbrain=...,
limits=...)`. That call shape was written against the donor branch's
kb_retrieval_corpus.py (a file/vault-only retriever). This branch's
kb_retrieval.py is the live SQL Solution Article + Jev retriever that Jev's
own pre-investigation KB step already owns (retrieve(conn, query, manifest, ...)
-- a different signature, needing a live pyodbc connection). Overwriting it
would break that existing, working path.

This module is imported as `l2_context_delivery_base.kb` instead (see the
import rebinding in l2_pipeline_runtime.py's _build_and_persist_stage_context),
and sources:
  - canonical_documents: read directly from Knowledge/ via the same
    route_candidates()/knowledge_docs_for_routes() manifest routing
    kb_retrieval.py already uses -- pure file reads, no SQL, no duplication.
  - promoted_facts/governed_solutions/approved_cases/rejected_cases/
    reopened_cases: l2_gbrain.py scopes, already wired to the real, populated
    xstudio-knowledge source. A scope with nothing populated degrades
    gracefully (l2_gbrain.search returns ok=False), never raises.

Live Solution Article SQL search is deliberately not added here: it needs a
credentialed connection assemble_stage_context() does not carry, and Jev's
existing pre-investigation KB step already covers it for fresh investigation.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

import l2_gbrain as gbrain
from jev.kb_applicability import assess_kb_candidates
from jev.policy import KB_JUDGMENTS_ENABLED, HIGH_RISK_NOUL
from kb_retrieval import (
    _compose_kb_score, _iter_gbrain_rows, knowledge_docs_for_routes,
    load_manifest, retrieve_gbrain, route_candidates,
)
from l2_context_envelope import make_context_item

REPO_ROOT = Path(__file__).resolve().parent.parent

# (gbrain scope, envelope key, source_type, trust_class)
#
# "promoted_facts" deliberately uses the "knowledge" scope (which includes the
# real, populated xstudio-knowledge source: 415 pages of SP catalog, runtime
# DB design, XBatch relationship atlas, vendor per-heat docs) rather than the
# not-yet-populated "facts" lane -- this is broader semantic-search coverage
# than the curated canonical_documents routing above, and is real signal
# today instead of a guaranteed degrade. "solutions"/"approved_cases"/
# "rejected_cases"/"reopened_cases" stay on their dedicated, currently-empty
# learning-cycle lanes: there is no real analog for ticket-outcome history in
# xstudio-knowledge, so degrading honestly is correct, not a bug.
#
# Tuple shape: (policy limit key, gbrain scope to actually query, envelope key,
# source_type, trust_class). The policy limit key always matches
# _stage_limits()'s keys (facts/solutions/approved_cases/rejected_cases/
# reopened_cases); the gbrain scope is what's passed to l2_gbrain.search().
_GBRAIN_LANES = (
    ("facts", "knowledge", "promoted_facts", "promoted_fact", "reviewed_operational"),
    ("solutions", "solutions", "governed_solutions", "governed_solution", "governed_reusable_solution"),
    ("approved_cases", "approved_cases", "approved_cases", "historical_approved_case", "reviewed_published_historical_case"),
    ("rejected_cases", "rejected_cases", "rejected_cases", "historical_rejected_case", "reviewed_negative_example"),
    ("reopened_cases", "reopened_cases", "reopened_cases", "historical_reopened_case", "observed_resolution_regression"),
)


def _canonical_documents(manifest: dict[str, Any], routes: list[dict[str, Any]], root: Path | None) -> list[dict[str, Any]]:
    base = root or REPO_ROOT
    items: list[dict[str, Any]] = []
    for doc in knowledge_docs_for_routes(manifest, routes):
        rel = str(doc.get("path") or "")
        if not rel:
            continue
        try:
            text = (base / rel).read_text(encoding="utf-8")
        except OSError as exc:
            items.append({"source_ref": rel, "error": f"unreadable: {exc}"})
            continue
        items.append(make_context_item(
            source_type="canonical_document",
            source_ref=rel,
            trust_class="canonical_reference",
            title=rel,
            content=text,
            reason=doc.get("reason") or "route",
        ))
    return items


def _investigator_equivalent_knowledge_search(query: str, manifest: dict[str, Any], limit: int) -> dict[str, Any]:
    """The exact same xstudio-knowledge lookup fresh investigation gets:
    retrieve_gbrain()'s score/overlap filter, then the same Jev applicability
    judgment (assess_kb_candidates()), same negative-indicator drop, same
    composite-score sort. Review/rework previously got this same source via
    l2_gbrain.search(scope="knowledge") instead -- no threshold, no Jev
    judgment at all -- so a stage's process could see meaningfully different,
    less-vetted GBrain content than the investigation it's reviewing.
    """
    gbrain_config = dict(manifest.get("gbrain") or {})
    gbrain_config["return_limit"] = limit
    result = retrieve_gbrain(query, gbrain_config)
    hits = result.get("hits") or []
    if hits and KB_JUDGMENTS_ENABLED:
        judged = assess_kb_candidates({"query": query}, hits)
        if judged.get("ok"):
            hits = list(judged.get("candidates") or hits)
            for row in hits:
                row["jev_kb_composite"] = _compose_kb_score(row)
            hits = [row for row in hits if float(row.get("jev_negative_indicator") or 0.0) < HIGH_RISK_NOUL]
            hits.sort(key=lambda row: (-float(row.get("jev_kb_composite") or 0.0), -float(row.get("retrieval_score") or 0.0)))
    results = [
        {"slug": h.get("slug"), "title": h.get("title"), "chunk_text": h.get("excerpt"), "score": h.get("retrieval_score")}
        for h in hits
    ]
    return {"ok": True, "results": results} if results else {"ok": True, "results": [], "_skipped": not bool(hits)}


def _scope_items(raw: dict[str, Any], *, source_type: str,
                  trust_class: str) -> tuple[list[dict[str, Any]], str | None]:
    if not raw.get("ok"):
        return [], None if raw.get("_skipped") else str(raw.get("error") or "GBrain retrieval unavailable")
    items = []
    for rank, row in enumerate(raw.get("results") or [], start=1):
        if not isinstance(row, dict):
            continue
        ref = str(row.get("slug") or row.get("id") or f"rank-{rank}")
        items.append(make_context_item(
            source_type=source_type,
            source_ref=ref,
            trust_class=trust_class,
            title=str(row.get("title") or ref),
            content=str(row.get("chunk_text") or row.get("content") or ""),
            retrieval_rank=rank,
            retrieval_score=row.get("score"),
        ))
    return items, None


def retrieve(query: str, manifest: dict[str, Any], *, vault: Path | None = None,
             root: Path | None = None, top: int = 5, include_gbrain: bool = True,
             limits: dict[str, int] | None = None, **_ignored: Any) -> dict[str, Any]:
    """Same call shape assemble_stage_context() expects from `kb.retrieve()`."""
    limits = limits or {}
    routes = route_candidates(query, manifest, top=3) or [
        {"route": "discover", "reasons": ["no deterministic route signal"]}
    ]
    out: dict[str, Any] = {
        "route_candidates": routes,
        "canonical_documents": _canonical_documents(manifest, routes, root),
    }
    errors: list[str] = []
    gbrain_raw: dict[str, Any] = {}
    for limit_key, scope, envelope_key, source_type, trust_class in _GBRAIN_LANES:
        limit = int(limits.get(limit_key, top))
        if not include_gbrain or limit <= 0 or not query.strip():
            raw: dict[str, Any] = {"ok": False, "_skipped": True}
        elif scope == "knowledge":
            # Same xstudio-knowledge source, same retrieval+Jev judgment as
            # fresh investigation -- not the threshold-less l2_gbrain.search().
            raw = _investigator_equivalent_knowledge_search(query, manifest, limit)
        else:
            raw = gbrain.search(query, scope=scope, limit=limit, automatic=True)
        gbrain_raw[scope] = raw
        items, error = _scope_items(raw, source_type=source_type, trust_class=trust_class)
        out[envelope_key] = items
        if error:
            errors.append(f"{scope}: {error}")
    out["gbrain"] = gbrain_raw
    out["retrieval_degraded"] = bool(errors)
    out["degradation_reasons"] = errors
    return out
