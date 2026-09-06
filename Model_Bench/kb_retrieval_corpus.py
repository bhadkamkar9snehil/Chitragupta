#!/usr/bin/env python3
"""Governed file/case retrieval and aggregate query for Chitragupta L2."""
from __future__ import annotations
from kb_retrieval_base import *

def _rank_markdown(
    directory: Path,
    query: str,
    *,
    source_type: str,
    source_prefix: str,
    allowed_trust: frozenset[str],
    limit: int,
    gbrain_result: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    """Return full authoritative Markdown items, using GBrain only as a ranking hint."""
    q = tokenize(query)
    ranked: list[tuple[int, float, int, str, dict[str, Any]]] = []
    if not directory.exists() or not q:
        return []
    hints = _gbrain_rank_hints(gbrain_result or {})
    for path in sorted(directory.glob("*.md")):
        meta, body = _frontmatter(path.read_text(encoding="utf-8", errors="replace"))
        trust = str(meta.get("trust") or "")
        if trust not in allowed_trust:
            continue
        overlap = sorted(q & tokenize(body))
        hint = hints.get(path.name.lower())
        if len(overlap) < MIN_MATCHED_TERMS and hint is None:
            continue
        lexical_score = float(len(overlap))
        gbrain_rank = hint[0] if hint else 10_000
        gbrain_score = hint[1] if hint else 0.0
        content = body.strip()
        item = make_context_item(
            source_type=source_type,
            source_ref=f"{source_prefix}/{path.name}",
            trust_class=trust,
            title=str(meta.get("title") or _first_heading(content, path.stem)),
            content=content,
            retrieval_score=max(lexical_score, gbrain_score),
            verification_required=True,
            matched_terms=overlap,
            gbrain_rank=None if hint is None else gbrain_rank,
        )
        for key in (
            "solution_id", "content_sha256", "approved_by", "approved_at", "review_evidence",
            "reviewed_by", "promoted_at", "case_id", "outcome", "run_id", "ticket_id",
            "ticket_no", "review_cycle", "response_type", "proposal_hash",
        ):
            if meta.get(key) not in (None, ""):
                out_key = "governance_content_sha256" if key == "content_sha256" else key
                item[out_key] = meta[key]
        ranked.append((gbrain_rank, -gbrain_score, -len(overlap), path.name, item))
    ranked.sort(key=lambda row: row[:4])
    out: list[dict[str, Any]] = []
    for rank, (*_, item) in enumerate(ranked[:max(0, limit)], 1):
        item = dict(item)
        item["retrieval_rank"] = rank
        out.append(item)
    return out


def promoted_facts(
    query: str, *, vault: Path | None = None, limit: int = MAX_RESULTS,
    gbrain_result: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    return _rank_markdown(
        (vault or _vault()) / "facts", query,
        source_type="promoted_fact", source_prefix="facts",
        allowed_trust=frozenset({"reviewed_operational", "reviewed_operational_heuristic"}),
        limit=limit, gbrain_result=gbrain_result,
    )


def governed_solutions(
    query: str, *, vault: Path | None = None, limit: int = MAX_RESULTS,
    gbrain_result: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    return _rank_markdown(
        (vault or _vault()) / "solutions" / "approved", query,
        source_type="governed_solution", source_prefix="solutions/approved",
        allowed_trust=frozenset({"governed_reusable_solution"}),
        limit=limit, gbrain_result=gbrain_result,
    )


_CASE_CONFIG = {
    "approved_cases": ("cases/approved", "historical_approved_case", frozenset({"reviewed_published_historical_case"})),
    "rejected_cases": ("cases/rejected", "historical_rejected_case", frozenset({"reviewed_negative_example"})),
    "reopened_cases": ("cases/reopened", "historical_reopened_case", frozenset({"observed_resolution_regression"})),
}


def historical_cases(
    query: str, *, scope: str, vault: Path | None = None, limit: int = MAX_RESULTS,
    gbrain_result: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    if scope not in _CASE_CONFIG:
        raise ValueError(f"unsupported historical-case scope: {scope}")
    rel, source_type, trusts = _CASE_CONFIG[scope]
    return _rank_markdown(
        (vault or _vault()) / rel, query,
        source_type=source_type, source_prefix=rel,
        allowed_trust=trusts, limit=limit, gbrain_result=gbrain_result,
    )


def retrieve(
    query_or_conn: Any,
    query_or_manifest: str | dict[str, Any] | None = None,
    legacy_manifest: dict[str, Any] | None = None,
    *,
    vault: Path | None = None,
    root: Path | None = None,
    top: int = 3,
    include_gbrain: bool = True,
    limits: dict[str, int] | None = None,
) -> dict[str, Any]:
    """Retrieve governed source material.

    Old ``retrieve(conn, query, manifest)`` callers remain accepted; ``conn`` is ignored.
    GBrain supplies ranking hints only. Delivered content is read from authoritative source
    files after trust validation.
    """
    if isinstance(query_or_conn, str):
        query = query_or_conn
        manifest = query_or_manifest if isinstance(query_or_manifest, dict) else legacy_manifest
    else:
        query = str(query_or_manifest or "")
        manifest = legacy_manifest
    manifest = manifest or load_manifest()
    vault = vault or _vault()
    top = max(1, min(10, int(top)))
    configured = {
        "facts": top,
        "solutions": top,
        "approved_cases": min(2, top),
        "rejected_cases": min(1, top),
        "reopened_cases": min(1, top),
    }
    for key, value in (limits or {}).items():
        if key in configured:
            configured[key] = max(0, min(10, int(value)))

    routes = route_candidates(query, manifest, top=min(3, top))
    canonical = load_canonical_documents(manifest, routes, root=root, vault=vault)

    scopes = ("facts", "solutions", "approved_cases", "rejected_cases", "reopened_cases")
    gbrain: dict[str, dict[str, Any]] = {}
    if include_gbrain and query.strip():
        for scope in scopes:
            gbrain[scope] = gbrain_scope_search(
                query, scope=scope, limit=max(1, configured[scope])
            )
    else:
        gbrain = {
            scope: {"ok": True, "backend": "gbrain", "scope": scope, "source_ids": [], "results": []}
            for scope in scopes
        }

    facts = promoted_facts(
        query, vault=vault, limit=configured["facts"], gbrain_result=gbrain["facts"]
    )
    solutions = governed_solutions(
        query, vault=vault, limit=configured["solutions"], gbrain_result=gbrain["solutions"]
    )
    approved = historical_cases(
        query, scope="approved_cases", vault=vault,
        limit=configured["approved_cases"], gbrain_result=gbrain["approved_cases"],
    )
    rejected = historical_cases(
        query, scope="rejected_cases", vault=vault,
        limit=configured["rejected_cases"], gbrain_result=gbrain["rejected_cases"],
    )
    reopened = historical_cases(
        query, scope="reopened_cases", vault=vault,
        limit=configured["reopened_cases"], gbrain_result=gbrain["reopened_cases"],
    )

    errors = [str(item.get("error")) for item in canonical if item.get("error")]
    for scope in scopes:
        if not gbrain[scope].get("ok"):
            errors.append(f"{scope}: {gbrain[scope].get('error') or 'GBrain retrieval failed'}")

    return {
        "schema_version": 2,
        "query": query,
        "route_candidates": routes,
        "canonical_documents": canonical,
        "live_sql_leads": live_sql_leads_for_routes(manifest, routes),
        "promoted_facts": facts,
        "governed_solutions": solutions,
        "solutions": solutions,  # compatibility alias
        "approved_cases": approved,
        "rejected_cases": rejected,
        "reopened_cases": reopened,
        "gbrain": gbrain,
        "retrieval_degraded": bool(errors),
        "degradation_reasons": errors,
        "retrieval_policy": {
            "live_solution_sql_read_allowed": False,
            "governed_solution_export_required": True,
            "automatic_gbrain_scopes": list(scopes),
            "automatic_untrusted_scopes_forbidden": ["all", "sessions", "candidates"],
            "gbrain_is_ranking_index_not_content_authority": True,
            "live_verification_required": True,
        },
    }


__all__=[name for name in globals() if not name.startswith("__")]
