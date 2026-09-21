"""Semantic KB relevance, applicability, and negative-indicator judgments."""
from __future__ import annotations
from typing import Any

from .client import system_one


def assess_kb_candidates(
    ticket: dict[str, Any],
    candidates: list[dict[str, Any]],
    *,
    api_key: str | None = None,
    sender=None,
) -> dict[str, Any]:
    if not candidates:
        return {"ok": True, "answers": {}, "candidates": []}
    limited = {f"k{i}": c for i, c in enumerate(candidates[:12])}
    questions: dict[str, Any] = {}
    for label in limited:
        questions.update({
            f"relevant_{label}": {
                "type": "noul",
                "instructions": {"task": "Is this knowledge item semantically relevant to the ticket symptom?", "ticket_path": "ticket", "candidate_path": f"candidates.{label}"},
            },
            f"applicable_{label}": {
                "type": "noul",
                "instructions": {"task": "Is this knowledge item compatible with the current ticket's context and applicability?", "ticket_path": "ticket", "candidate_path": f"candidates.{label}"},
            },
            f"negative_{label}": {
                "type": "noul",
                "instructions": {"task": "Is there a material negative indicator showing this knowledge item should not be applied?", "ticket_path": "ticket", "candidate_path": f"candidates.{label}"},
            },
            f"same_pattern_{label}": {
                "type": "noul",
                "instructions": {"task": "Does this describe the same failure or diagnostic pattern as the ticket?", "ticket_path": "ticket", "candidate_path": f"candidates.{label}"},
            },
            f"same_root_family_{label}": {
                "type": "noul",
                "instructions": {"task": "Is this plausibly the same root-cause family without assuming the historical fix is true for this ticket?", "ticket_path": "ticket", "candidate_path": f"candidates.{label}"},
            },
        })
    result = system_one({"ticket": ticket, "candidates": limited}, questions, api_key=api_key, sender=sender)
    if not result.get("ok"):
        return {**result, "candidates": candidates}
    answers = result["answers"]
    enriched = []
    for label, candidate in limited.items():
        row = dict(candidate)
        for name, key in (
            ("relevance", f"relevant_{label}"),
            ("applicability", f"applicable_{label}"),
            ("negative_indicator", f"negative_{label}"),
            ("same_failure_pattern", f"same_pattern_{label}"),
            ("same_root_cause_family", f"same_root_family_{label}"),
        ):
            answer = answers.get(key) or {}
            row[f"jev_{name}"] = float(answer.get("noul") or 0.0) if answer.get("type") == "noul" else None
        enriched.append(row)
    return {**result, "candidates": enriched}
