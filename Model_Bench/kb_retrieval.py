#!/usr/bin/env python3
"""Deterministic retrieval for Chitragupta's reusable solution knowledge.

This is intentionally NOT mem0 retrieval and NOT schema discovery.

Responsibilities:
- infer deterministic canonical route candidates from Knowledge/manifest.json;
- optionally use TypeSafe Jev as a confidence-gated semantic route chooser;
- search active Hermes_Solution_Article_Mst_Tbl articles by the ticket's actual
  words, not merely by a broad route;
- return IDs + provenance so an investigator/reviewer can name the source;
- abstain when no article is relevant enough instead of always returning five;
- expose the canonical Knowledge documents associated with likely routes.

Schema/table retrieval remains in Hermes_Orchestrator.py and ticket-specific
episodic state remains in InvestigationJson; neither belongs here.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
from pathlib import Path
from typing import Any

from jev import policy as jev_policy
from jev.audit import persist_rows, rows_for_result
from jev.kb_applicability import assess_kb_candidates
from jev.ticket_triage import assess_ticket

try:
    import pyodbc
except ImportError:  # pure routing/scoring tests do not need the live driver
    pyodbc = None

ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = ROOT / "Knowledge" / "manifest.json"
MIN_MATCHED_TERMS = 2

STOPWORDS = {
    "the", "a", "an", "is", "was", "were", "are", "be", "been", "and", "or",
    "but", "for", "with", "this", "that", "these", "those", "on", "in", "at",
    "to", "of", "it", "its", "as", "by", "from", "has", "have", "had", "not",
    "no", "does", "did", "do", "why", "what", "when", "where", "how", "which",
    "there", "here", "any", "some", "all", "than", "then", "so", "if", "into",
    "issue", "problem", "ticket", "please", "check", "getting", "showing",
}
TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9_\-]*")


def _iter_gbrain_rows(payload: Any) -> list[dict[str, Any]]:
    """Best-effort normalization of GBrain search output without trusting its synthesis.

    Shared by l2_context_delivery_assembly so the context envelope's GBrain
    hit-count is derived the same way regardless of which GBrain response
    shape (list, or dict wrapping results/hits/items/documents/data) came back.
    """
    if isinstance(payload, list):
        return [row for row in payload if isinstance(row, dict)]
    if not isinstance(payload, dict):
        return []
    for key in ("results", "hits", "items", "documents", "data"):
        value = payload.get(key)
        if isinstance(value, list):
            return [row for row in value if isinstance(row, dict)]
        if isinstance(value, dict):
            nested = _iter_gbrain_rows(value)
            if nested:
                return nested
    return []


def tokenize(text: str) -> set[str]:
    return {
        t.lower()
        for t in TOKEN_RE.findall(text or "")
        if len(t) > 2 and t.lower() not in STOPWORDS
    }


def load_manifest() -> dict[str, Any]:
    if not MANIFEST_PATH.exists():
        raise FileNotFoundError(f"Knowledge manifest not found: {MANIFEST_PATH}")
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def _identifier_routes(manifest: dict[str, Any]) -> list[tuple[re.Pattern[str], tuple[str, ...], str]]:
    """Compile strong identifier routing from the manifest.

    Arrays are the canonical representation. String values remain accepted for
    backward compatibility with older manifests that used "route_a or route_b".
    """
    compiled: list[tuple[re.Pattern[str], tuple[str, ...], str]] = []
    for identifier, configured in (manifest.get("identifier_routing") or {}).items():
        if isinstance(configured, list):
            routes = tuple(str(r) for r in configured if r)
        elif isinstance(configured, str):
            routes = tuple(part.strip() for part in configured.split(" or ") if part.strip())
        else:
            continue
        if not routes:
            continue
        compiled.append(
            (
                re.compile(rf"\b{re.escape(str(identifier))}\b", re.I),
                routes,
                f"{identifier} identifier",
            )
        )
    return compiled


def route_candidates(query: str, manifest: dict[str, Any], top: int = 3) -> list[dict[str, Any]]:
    q_tokens = tokenize(query)
    scores: dict[str, float] = {}
    reasons: dict[str, list[str]] = {}

    # Explicit identifiers are strong structural evidence and should outrank
    # vague natural-language overlap.
    for pattern, routes, reason in _identifier_routes(manifest):
        if pattern.search(query):
            for route in routes:
                scores[route] = scores.get(route, 0.0) + 30.0
                reasons.setdefault(route, []).append(reason)

    for route_def in manifest.get("routes", []):
        route = route_def.get("route")
        if not route or route == "discover":
            continue
        route_tokens = tokenize(
            " ".join(
                [
                    route.replace("_", " "),
                    str(route_def.get("description") or ""),
                    " ".join(route_def.get("keywords") or []),
                ]
            )
        )
        overlap = sorted(q_tokens & route_tokens)
        if overlap:
            scores[route] = scores.get(route, 0.0) + (3.0 * len(overlap))
            reasons.setdefault(route, []).append("keywords: " + ", ".join(overlap[:8]))

        q_lower = query.lower()
        phrase_hits = [
            kw for kw in (route_def.get("keywords") or [])
            if " " in kw and kw.lower() in q_lower
        ]
        if phrase_hits:
            scores[route] = scores.get(route, 0.0) + 5.0 * len(phrase_hits)
            reasons.setdefault(route, []).append("phrases: " + ", ".join(phrase_hits[:4]))

    ranked = sorted(scores.items(), key=lambda item: (-item[1], item[0]))[:top]
    if not ranked:
        return [{"route": "discover", "score": 0.0, "reasons": ["no deterministic route signal"]}]

    return [
        {"route": route, "score": round(score, 2), "reasons": reasons.get(route, [])}
        for route, score in ranked
    ]



def _strong_identifier_routes(query: str, manifest: dict[str, Any]) -> list[str]:
    """Return canonical routes supported by explicit identifier names in the ticket."""
    seen: set[str] = set()
    ordered: list[str] = []
    for pattern, routes, _reason in _identifier_routes(manifest):
        if not pattern.search(query):
            continue
        for route in routes:
            if route not in seen:
                seen.add(route)
                ordered.append(route)
    return ordered


def resolve_route_candidates(
    query: str,
    manifest: dict[str, Any],
    top: int = 3,
    *,
    jev_decider=None,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Fuse deterministic routing with an optional Jev semantic Choice.

    Explicit identifiers remain structural authority. A single unambiguous
    identifier route skips Jev entirely. When an identifier maps to multiple
    routes (for example TransactionID -> API transaction or SAP posting), Jev
    may disambiguate only inside that allowed set. Without an identifier, Jev
    may choose from the full canonical manifest, including discover.

    Any unavailable/error/low-confidence Jev result falls back to the exact
    deterministic ordering returned by route_candidates().
    """
    deterministic = route_candidates(query, manifest, top=top)
    identifier_routes = _strong_identifier_routes(query, manifest)

    routing: dict[str, Any] = {
        "mode": "deterministic",
        "deterministic_candidates": deterministic,
        "identifier_routes": identifier_routes,
        "jev": None,
    }

    if len(identifier_routes) == 1:
        routing["jev"] = {
            "enabled": False,
            "accepted": False,
            "reason": "single explicit identifier route is authoritative",
        }
        return deterministic, routing

    if jev_decider is None:
        routing["jev"] = {
            "enabled": False,
            "accepted": False,
            "reason": "no semantic route decision supplied",
        }
        return deterministic, routing

    try:
        jev = jev_decider(
            query,
            manifest,
            allowed_routes=identifier_routes if len(identifier_routes) > 1 else None,
        )
    except Exception as exc:  # injected semantic decision must never break retrieval
        jev = {
            "enabled": True,
            "accepted": False,
            "reason": "Jev decider raised unexpectedly",
            "error_type": type(exc).__name__,
        }

    routing["jev"] = jev
    if not jev.get("accepted"):
        return deterministic, routing

    choice = str(jev.get("choice") or "")
    canonical = {str(r.get("route") or "") for r in manifest.get("routes", [])}
    if choice not in canonical:
        routing["jev"] = {
            **jev,
            "accepted": False,
            "reason": "Jev choice was not a canonical manifest route",
        }
        return deterministic, routing
    if identifier_routes and choice not in identifier_routes:
        routing["jev"] = {
            **jev,
            "accepted": False,
            "reason": "Jev choice escaped explicit identifier constraints",
        }
        return deterministic, routing

    existing = {r["route"]: r for r in deterministic}
    base = dict(existing.get(choice) or {"route": choice, "score": 0.0, "reasons": []})
    reasons = list(base.get("reasons") or [])
    reasons.insert(0, f"Jev semantic choice; confidence={float(jev.get('confidence') or 0.0):.3f}")
    base["reasons"] = reasons
    base["semantic_source"] = "typesafe_jev"
    base["semantic_confidence"] = float(jev.get("confidence") or 0.0)

    fused = [base]
    for candidate in deterministic:
        if candidate["route"] == choice:
            continue
        fused.append(candidate)
        if len(fused) >= top:
            break

    routing["selected_route"] = choice
    routing["mode"] = "jev"
    return fused[:top], routing


def knowledge_docs_for_routes(manifest: dict[str, Any], routes: list[dict[str, Any]]) -> list[dict[str, Any]]:
    defs = {r.get("route"): r for r in manifest.get("routes", [])}
    seen: set[str] = set()
    docs: list[dict[str, Any]] = []

    for path in manifest.get("always_load", []):
        if path not in seen:
            seen.add(path)
            docs.append({"path": f"Knowledge/{path}", "reason": "always_load", "route": None})

    for candidate in routes:
        route = candidate["route"]
        route_def = defs.get(route) or {}
        for path in route_def.get("load", []):
            if path in seen:
                continue
            seen.add(path)
            docs.append({"path": f"Knowledge/{path}", "reason": "route", "route": route})

    return docs


def connect(server: str, database: str, username: str, password: str | None):
    if pyodbc is None:
        raise RuntimeError("pyodbc is required for live KB retrieval; use the Windows Python deployment interpreter")
    if not password:
        raise RuntimeError("MSSQL_MCP_PASSWORD is required for KB retrieval")
    conn_str = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={server};DATABASE={database};UID={username};PWD={password};"
        "TrustServerCertificate=yes;Encrypt=no;"
    )
    return pyodbc.connect(conn_str, timeout=10)


def fetch_articles(conn) -> list[dict[str, Any]]:
    cur = conn.cursor()
    cur.execute(
        "SELECT CASE WHEN COL_LENGTH('dbo.Hermes_Solution_Article_Mst_Tbl', 'ArticleStatus') "
        "IS NULL THEN 0 ELSE 1 END"
    )
    governed = bool(cur.fetchone()[0])
    if governed:
        cur.execute(
            """
            SELECT ID, Title, ProblemSummary, RootCause, ResolutionSteps,
                   Route, Tags, UsageCount, CreatedOn, ModifiedOn,
                   KnowledgeType, ArticleStatus, CanonicalKey, RevisionNo,
                   ContentHash, SourceTicketID, SourceRunID, LastVerifiedOn,
                   ApplicabilityJson, NegativeIndicatorsJson, VerificationJson,
                   EvidenceJson, DiagnosticSteps, VerificationSteps, ExpectedResult
            FROM dbo.Hermes_Solution_Article_Mst_Tbl
            WHERE IsActive = 1 AND IsDeleted = 0 AND ArticleStatus = 'Approved';
            """
        )
    else:
        cur.execute(
            """
            SELECT ID, Title, ProblemSummary, RootCause, ResolutionSteps,
                   Route, Tags, UsageCount, CreatedOn, ModifiedOn
            FROM dbo.Hermes_Solution_Article_Mst_Tbl
            WHERE IsActive = 1 AND IsDeleted = 0;
            """
        )
    cols = [d[0] for d in cur.description]
    return [dict(zip(cols, row)) for row in cur.fetchall()]


def _field_overlap(q_tokens: set[str], text: str | None) -> set[str]:
    return q_tokens & tokenize(text or "")


def score_article(
    article: dict[str, Any],
    query: str,
    routes: list[dict[str, Any]],
) -> tuple[float, list[str], list[str]]:
    q_tokens = tokenize(query)
    route_rank = {c["route"]: i for i, c in enumerate(routes)}

    weights = {
        "Title": 5.0,
        "ProblemSummary": 4.0,
        "RootCause": 3.5,
        "Tags": 3.0,
        "ResolutionSteps": 1.0,
    }

    score = 0.0
    matched: set[str] = set()
    reasons: list[str] = []

    for field, weight in weights.items():
        overlap = _field_overlap(q_tokens, article.get(field))
        if overlap:
            matched |= overlap
            score += weight * len(overlap)
            reasons.append(f"{field}: {', '.join(sorted(overlap)[:8])}")

    # Route can improve a textually relevant article but route alone cannot
    # retrieve it. This is the key correction over the old Route=? TOP 5 path.
    article_route = (article.get("Route") or "").strip()
    if matched and article_route in route_rank:
        route_bonus = max(2.0, 8.0 - (2.0 * route_rank[article_route]))
        score += route_bonus
        reasons.append(f"route: {article_route}")

    # Usage is a tie-breaker only after textual relevance exists.
    usage = int(article.get("UsageCount") or 0)
    if matched and usage > 0:
        score += min(3.0, math.log2(usage + 1))
        reasons.append(f"usage_count: {usage}")

    return score, sorted(matched), reasons


def rank_articles(
    articles: list[dict[str, Any]],
    query: str,
    routes: list[dict[str, Any]],
    top: int = 5,
    min_score: float = 7.0,
    min_matched_terms: int = MIN_MATCHED_TERMS,
) -> list[dict[str, Any]]:
    """Rank reusable solutions and reject weak one-word/domain-only matches."""
    ranked: list[dict[str, Any]] = []
    for article in articles:
        score, matched_terms, reasons = score_article(article, query, routes)
        if score < min_score or len(matched_terms) < min_matched_terms:
            continue
        ranked.append(
            {
                "kb_id": f"solution:{article['ID']}",
                "solution_id": article["ID"],
                "source_type": "solution_article",
                "source_ref": f"Hermes_Solution_Article_Mst_Tbl:{article['ID']}",
                "title": article.get("Title"),
                "problem_summary": article.get("ProblemSummary"),
                "root_cause": article.get("RootCause"),
                "resolution_steps": article.get("ResolutionSteps"),
                "route": article.get("Route"),
                "tags": article.get("Tags"),
                "usage_count": int(article.get("UsageCount") or 0),
                "created_on": article.get("CreatedOn"),
                "modified_on": article.get("ModifiedOn"),
                "knowledge_type": article.get("KnowledgeType"),
                "article_status": article.get("ArticleStatus") or ("Approved" if article.get("IsActive", 1) else None),
                "canonical_key": article.get("CanonicalKey"),
                "revision_no": article.get("RevisionNo"),
                "content_hash": article.get("ContentHash"),
                "source_ticket_id": article.get("SourceTicketID"),
                "source_run_id": article.get("SourceRunID"),
                "last_verified_on": article.get("LastVerifiedOn"),
                "applicability": article.get("ApplicabilityJson"),
                "negative_indicators": article.get("NegativeIndicatorsJson"),
                "verification": article.get("VerificationJson"),
                "evidence": article.get("EvidenceJson"),
                "diagnostic_steps": article.get("DiagnosticSteps"),
                "verification_steps": article.get("VerificationSteps"),
                "expected_result": article.get("ExpectedResult"),
                "retrieval_score": round(score, 2),
                "matched_terms": matched_terms,
                "retrieval_reasons": reasons,
                "verification_required": True,
            }
        )

    ranked.sort(key=lambda row: (-row["retrieval_score"], -row["usage_count"], str(row["solution_id"])))
    return ranked[:top]


def _triage_route_decider(triage: dict[str, Any]):
    def decide(query: str, manifest: dict[str, Any], *, allowed_routes=None) -> dict[str, Any]:
        del query, manifest, allowed_routes
        answer = (triage.get("answers") or {}).get("route") or {}
        if not triage.get("ok") or answer.get("type") != "choice":
            return {
                "enabled": bool(triage.get("enabled")),
                "accepted": False,
                "reason": triage.get("reason") or "Jev triage route unavailable",
            }
        confidence = float(answer.get("confidence") or 0.0)
        return {
            "enabled": True,
            "accepted": confidence >= jev_policy.MIN_CHOICE_CONFIDENCE,
            "choice": answer.get("choice"),
            "confidence": confidence,
            "probabilities": answer.get("probabilities") or {},
            "model": triage.get("model"),
            "reason": None if confidence >= jev_policy.MIN_CHOICE_CONFIDENCE
                else "Jev confidence below configured threshold",
        }
    return decide


def _compose_kb_score(row: dict[str, Any]) -> float:
    relevance = float(row.get("jev_relevance") or 0.0)
    applicability = float(row.get("jev_applicability") or 0.0)
    same_pattern = float(row.get("jev_same_failure_pattern") or 0.0)
    same_root = float(row.get("jev_same_root_cause_family") or 0.0)
    negative = float(row.get("jev_negative_indicator") or 0.0)
    return round(
        (2.0 * relevance) + (2.0 * applicability) + same_pattern + (0.5 * same_root) - (2.5 * negative),
        6,
    )


def log_retrieval_telemetry(
    conn,
    *,
    query: str,
    routes: list[dict[str, Any]],
    ranked: list[dict[str, Any]],
    ticket_id: str | None,
    run_id: str | None,
) -> dict[str, Any]:
    """Reuse Agent Trace for retrieval telemetry; do not create a Jev/KB side table."""
    if not ranked:
        return {"ok": True, "inserted": 0}
    try:
        query_hash = hashlib.sha256(query.encode("utf-8")).hexdigest()
        route_names = {r.get("route") for r in routes}
        compact = []
        for rank_no, row in enumerate(ranked, start=1):
            compact.append({
                "rank": rank_no,
                "kb_id": row.get("kb_id"),
                "source_type": row.get("source_type"),
                "deterministic_score": row.get("retrieval_score"),
                "jev_relevance": row.get("jev_relevance"),
                "jev_applicability": row.get("jev_applicability"),
                "jev_negative_indicator": row.get("jev_negative_indicator"),
                "route_match": bool(row.get("route") in route_names),
            })
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO dbo.Hermes_Agent_Trace_Trn_Tbl
            (EventType, EventOn, ToolName, Status, ArgsJson, ResultJson,
             Provider, RunID, TicketID, Source)
            VALUES
            ('kb_retrieval', GETDATE(), 'kb_retrieval', 'ok', ?, ?, 'chitragupta', ?, ?, 'KB');
            """,
            json.dumps({"query_hash": query_hash, "phase": "PRE_INVESTIGATION"}, separators=(",", ":")),
            json.dumps({"candidates": compact}, separators=(",", ":"), default=str),
            run_id,
            ticket_id,
        )
        conn.commit()
        return {"ok": True, "inserted": 1}
    except Exception as exc:
        return {"ok": False, "inserted": 0, "reason": f"{type(exc).__name__}: {exc}"}


def retrieve(
    conn,
    query: str,
    manifest: dict[str, Any],
    top: int = 5,
    min_score: float = 7.0,
    min_matched_terms: int = MIN_MATCHED_TERMS,
    *,
    ticket_id: str | None = None,
    run_id: str | None = None,
) -> dict[str, Any]:
    identifier_routes = _strong_identifier_routes(query, manifest)
    triage = assess_ticket(
        {"query": query},
        manifest,
        allowed_routes=identifier_routes if identifier_routes else None,
    )
    routes, routing = resolve_route_candidates(
        query,
        manifest,
        jev_decider=_triage_route_decider(triage),
    )
    routing["triage"] = triage

    ranked = rank_articles(
        fetch_articles(conn),
        query,
        routes,
        top=top,
        min_score=min_score,
        min_matched_terms=min_matched_terms,
    )

    kb_semantics = {"ok": False, "reason": "KB Jev judgments disabled", "candidates": ranked}

    if ranked and jev_policy.KB_JUDGMENTS_ENABLED:
        kb_semantics = assess_kb_candidates({"query": query, "routes": routes}, ranked)
        if kb_semantics.get("ok"):
            ranked = list(kb_semantics.get("candidates") or ranked)
            for row in ranked:
                row["jev_kb_composite"] = _compose_kb_score(row)
            ranked.sort(
                key=lambda row: (
                    bool(float(row.get("jev_negative_indicator") or 0.0) >= jev_policy.HIGH_RISK_NOUL),
                    -float(row.get("jev_kb_composite") or 0.0),
                    -float(row.get("retrieval_score") or 0.0),
                )
            )

    retrieval_telemetry = log_retrieval_telemetry(
        conn,
        query=query,
        routes=routes,
        ranked=ranked,
        ticket_id=ticket_id,
        run_id=run_id,
    )

    # Best-effort audit. Retrieval must never fail because audit persistence is unavailable.
    audit_results = []
    for stage, state, result in (
        ("TICKET_TRIAGE", {"query": query}, triage),
        (
            "KB_APPLICABILITY",
            {"query": query, "candidate_ids": [str(row.get("kb_id") or "") for row in ranked]},
            kb_semantics,
        ),
    ):
        if result.get("ok"):
            try:
                audit_results.append(persist_rows(rows_for_result(
                    result=result,
                    stage=stage,
                    state=state,
                    ticket_id=ticket_id,
                    run_id=run_id,
                )))
            except Exception as exc:
                audit_results.append({"ok": False, "reason": f"{type(exc).__name__}: {exc}"})

    return {
        "query": query,
        "route_candidates": routes,
        "routing": routing,
        "ticket_characterization": triage.get("answers") if triage.get("ok") else {},
        "knowledge_documents": knowledge_docs_for_routes(manifest, routes),
        "solutions": ranked,
        "jev_kb_applicability": {
            "ok": bool(kb_semantics.get("ok")),
            "model": kb_semantics.get("model"),
            "latency_ms": kb_semantics.get("latency_ms"),
        },
        "jev_security": {
            "ok": bool(kb_semantics.get("ok")) and jev_policy.SECURITY_SCREEN_ENABLED,
            "model": kb_semantics.get("model"),
            "latency_ms": kb_semantics.get("latency_ms"),
            "coalesced_with": "KB_APPLICABILITY",
        },
        "jev_audit": audit_results,
        "retrieval_telemetry": retrieval_telemetry,
        "abstained": not bool(ranked),
        "abstention_reason": None if ranked else "No active solution article met the relevance threshold.",
        "retrieval_policy": {
            "route_only_match_allowed": False,
            "semantic_route_is_active": True,
            "semantic_kb_reranking_is_active": True,
            "jev_low_confidence_falls_back_to_deterministic": True,
            "min_score": min_score,
            "min_matched_terms": min_matched_terms,
            "top": top,
            "provenance_required": True,
            "live_verification_required": True,
        },
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--server", default=os.environ.get("MSSQL_MCP_SERVER", "10.2.6.204"))
    ap.add_argument("--database", default="XStudio_Helpdesk")
    ap.add_argument("--username", default=os.environ.get("MSSQL_MCP_USER", "sa"))
    ap.add_argument("--password", default=os.environ.get("MSSQL_MCP_PASSWORD"))
    ap.add_argument("--query", required=True, help="Ticket text/problem description to retrieve against")
    ap.add_argument("--ticket-id")
    ap.add_argument("--run-id")
    ap.add_argument("--top", type=int, default=5)
    ap.add_argument("--min-score", type=float, default=7.0)
    ap.add_argument("--min-matched-terms", type=int, default=MIN_MATCHED_TERMS)
    args = ap.parse_args()

    manifest = load_manifest()
    conn = connect(args.server, args.database, args.username, args.password)
    try:
        result = retrieve(
            conn,
            args.query,
            manifest,
            top=max(1, args.top),
            min_score=args.min_score,
            min_matched_terms=max(1, args.min_matched_terms),
            ticket_id=args.ticket_id,
            run_id=args.run_id,
        )
    finally:
        conn.close()

    print(json.dumps(result, indent=2, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
