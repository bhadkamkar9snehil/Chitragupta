"""Semantic reranking of deterministic candidates."""
from __future__ import annotations
from typing import Any

from .client import system_one


def rerank_candidates(
    query: str,
    candidates: list[dict[str, Any]],
    *,
    top: int = 5,
    candidate_kind: str = "candidate",
    api_key: str | None = None,
    sender=None,
) -> dict[str, Any]:
    if not candidates:
        return {"ok": True, "ranked": [], "answers": {}}

    labels = {f"c{i}": c for i, c in enumerate(candidates[:32])}
    questions: dict[str, Any] = {}
    for label in labels:
        questions[f"rel_{label}"] = {
            "type": "noul",
            "instructions": {
                "task": f"Is this {candidate_kind} semantically relevant to the investigation query?",
                "query_path": "query",
                "candidate_path": f"candidates.{label}",
            },
        }
        questions[f"fit_{label}"] = {
            "type": "score",
            "instructions": {
                "task": f"Rate how useful this {candidate_kind} is as the next evidence lead for the query.",
                "query_path": "query",
                "candidate_path": f"candidates.{label}",
            },
            "criteria": [
                "Irrelevant or distracting.",
                "Weak lead; only generic overlap.",
                "Plausible lead worth considering.",
                "Strong, specific next evidence lead.",
            ],
        }

    result = system_one({"query": query, "candidates": labels}, questions, api_key=api_key, sender=sender)
    if not result.get("ok"):
        return {**result, "ranked": candidates[:top]}

    ranked = []
    answers = result.get("answers") or {}
    for label, candidate in labels.items():
        rel = answers.get(f"rel_{label}") or {}
        fit = answers.get(f"fit_{label}") or {}
        rel_p = float(rel.get("noul") or 0.0) if rel.get("type") == "noul" else 0.0
        fit_score = float(fit.get("score") or 0.0) if fit.get("type") == "score" else 0.0
        fit_conf = float(fit.get("confidence") or 0.0) if fit.get("type") == "score" else 0.0
        composite = rel_p * 4.0 + fit_score
        enriched = dict(candidate)
        enriched["jev_relevance"] = round(rel_p, 6)
        enriched["jev_fit_score"] = round(fit_score, 6)
        enriched["jev_fit_confidence"] = round(fit_conf, 6)
        enriched["jev_rank_score"] = round(composite, 6)
        ranked.append(enriched)
    ranked.sort(key=lambda x: (-x["jev_rank_score"], -x["jev_relevance"]))
    return {**result, "ranked": ranked[:max(1, top)]}
