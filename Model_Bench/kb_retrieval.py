#!/usr/bin/env python3
"""Deterministic retrieval for Chitragupta's reusable solution knowledge.

This is intentionally NOT mem0 retrieval and NOT schema discovery.

Responsibilities:
- infer canonical route candidates from Knowledge/manifest.json;
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
import json
import math
import os
import re
from pathlib import Path
from typing import Any

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
                "retrieval_score": round(score, 2),
                "matched_terms": matched_terms,
                "retrieval_reasons": reasons,
                "verification_required": True,
            }
        )

    ranked.sort(key=lambda row: (-row["retrieval_score"], -row["usage_count"], str(row["solution_id"])))
    return ranked[:top]


def retrieve(
    conn,
    query: str,
    manifest: dict[str, Any],
    top: int = 5,
    min_score: float = 7.0,
    min_matched_terms: int = MIN_MATCHED_TERMS,
) -> dict[str, Any]:
    routes = route_candidates(query, manifest)
    ranked = rank_articles(
        fetch_articles(conn),
        query,
        routes,
        top=top,
        min_score=min_score,
        min_matched_terms=min_matched_terms,
    )

    return {
        "query": query,
        "route_candidates": routes,
        "knowledge_documents": knowledge_docs_for_routes(manifest, routes),
        "solutions": ranked,
        "abstained": not bool(ranked),
        "abstention_reason": None if ranked else "No active solution article met the relevance threshold.",
        "retrieval_policy": {
            "route_only_match_allowed": False,
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
        )
    finally:
        conn.close()

    print(json.dumps(result, indent=2, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
