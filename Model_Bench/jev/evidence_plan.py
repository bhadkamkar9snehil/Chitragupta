"""Bounded Jev evidence planning over deterministic real candidates."""
from __future__ import annotations
from typing import Any

from .client import system_one


def plan_evidence(
    ticket: dict[str, Any],
    candidates: list[dict[str, Any]],
    *,
    known_solutions: list[dict[str, Any]] | None = None,
    api_key: str | None = None,
    sender=None,
) -> dict[str, Any]:
    limited = {f"c{i}": c for i, c in enumerate(candidates[:12])}
    questions: dict[str, Any] = {
        "needs_local_reasoning_before_probe": {
            "type": "noul",
            "instructions": "Is the ticket so ambiguous that a deep local reasoner is needed before selecting any bounded evidence probe?",
        },
        "plan_complexity": {
            "type": "score",
            "instructions": "Rate how many bounded evidence surfaces are likely needed.",
            "criteria": [
                "One focused probe should usually be enough.",
                "Two related probes are likely needed.",
                "Several correlated probes are likely needed.",
                "The case is cross-domain or too open-ended for bounded automatic probing.",
            ],
        },
    }
    for label in limited:
        questions[f"inspect_{label}"] = {
            "type": "noul",
            "instructions": {
                "task": "Should this real deterministic SQL candidate be probed for current-ticket evidence?",
                "ticket_path": "ticket",
                "candidate_path": f"candidates.{label}",
            },
        }
        questions[f"value_{label}"] = {
            "type": "score",
            "instructions": {
                "task": "Rate expected evidence value of probing this candidate next.",
                "ticket_path": "ticket",
                "candidate_path": f"candidates.{label}",
            },
            "criteria": [
                "Very low value.",
                "Possible supporting context.",
                "Useful direct evidence.",
                "Likely decisive evidence.",
            ],
        }
    return system_one(
        {"ticket": ticket, "candidates": limited, "known_solutions": known_solutions or []},
        questions,
        api_key=api_key,
        sender=sender,
    )
