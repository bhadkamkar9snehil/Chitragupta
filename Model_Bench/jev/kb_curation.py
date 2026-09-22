"""Post-resolution semantic KB deduplication and curation."""
from __future__ import annotations

from typing import Any

from .client import system_one


def rerank_articles(
    query: str,
    candidates: list[dict[str, Any]],
    *,
    top: int = 8,
    api_key: str | None = None,
    sender=None,
) -> dict[str, Any]:
    """Rank only supplied governed articles; never invent a KB candidate."""
    if not candidates:
        return {"ok": True, "ranked": [], "answers": {}}

    labels = {f"c{i}": candidate for i, candidate in enumerate(candidates[:24])}
    questions: dict[str, Any] = {}
    for label in labels:
        questions[f"relevant_{label}"] = {
            "type": "noul",
            "instructions": {
                "task": "Is this existing governed Solution article semantically relevant to the verified incident?",
                "query_path": "query",
                "candidate_path": f"candidates.{label}",
            },
        }
        questions[f"same_pattern_{label}"] = {
            "type": "noul",
            "instructions": {
                "task": "Does this article describe substantially the same root-cause/resolution pattern as the verified incident?",
                "query_path": "query",
                "candidate_path": f"candidates.{label}",
            },
        }

    result = system_one(
        {"query": query, "candidates": labels},
        questions,
        api_key=api_key,
        sender=sender,
    )
    if not result.get("ok"):
        return {**result, "ranked": candidates[:top]}

    answers = result.get("answers") or {}
    ranked = []
    for label, candidate in labels.items():
        relevant = answers.get(f"relevant_{label}") or {}
        same_pattern = answers.get(f"same_pattern_{label}") or {}
        relevance = float(relevant.get("noul") or 0.0) if relevant.get("type") == "noul" else 0.0
        pattern = float(same_pattern.get("noul") or 0.0) if same_pattern.get("type") == "noul" else 0.0
        enriched = dict(candidate)
        enriched["jev_relevance"] = round(relevance, 6)
        enriched["jev_same_pattern"] = round(pattern, 6)
        enriched["jev_rank_score"] = round((2.0 * pattern) + relevance, 6)
        ranked.append(enriched)

    ranked.sort(key=lambda row: (-row["jev_rank_score"], -row["jev_relevance"]))
    return {**result, "ranked": ranked[:max(1, top)]}


def assess_curation(state: dict[str, Any], *, api_key: str | None = None, sender=None) -> dict[str, Any]:
    questions = {
        "curation_disposition": {
            "type": "choice",
            "instructions": "Given the verified resolution and existing candidate knowledge, choose the best curation disposition. This is a suggestion only; deterministic and human governance decides.",
            "criteria": {
                "REUSE_EXISTING": "An existing article already represents the reusable pattern adequately.",
                "UPDATE_EXISTING": "An existing article is the same reusable pattern but materially needs an update.",
                "CREATE_CANDIDATE": "The incident is generalizable and no existing article adequately represents it.",
                "NONE": "No reusable knowledge-base action should be taken.",
            },
        },
        "same_root_cause": {"type": "noul", "instructions": "Does at least one existing candidate represent the same verified root cause?"},
        "same_resolution_pattern": {"type": "noul", "instructions": "Does at least one existing candidate represent the same reusable resolution or diagnostic pattern?"},
        "existing_article_stale": {"type": "noul", "instructions": "Does the best matching existing article appear materially stale or incomplete relative to the verified incident?"},
        "generalizable_incident": {"type": "noul", "instructions": "Is the verified incident reusable beyond this one ticket rather than instance-specific?"},
    }
    return system_one(state, questions, api_key=api_key, sender=sender)
