"""Advisory routing between configured reasoning profiles/models."""
from __future__ import annotations
from typing import Any

from .client import system_one


def assess_model_route(
    state: dict[str, Any],
    profiles: dict[str, Any],
    *,
    api_key: str | None = None,
    sender=None,
) -> dict[str, Any]:
    if not profiles:
        return {"ok": False, "reason": "No model/profile candidates supplied", "answers": {}}
    if len(profiles) == 1:
        name = next(iter(profiles))
        return {
            "ok": True,
            "model": "deterministic-single-option",
            "answers": {
                "profile": {
                    "type": "choice",
                    "choice": name,
                    "confidence": 1.0,
                    "probabilities": {name: 1.0},
                }
            },
        }
    return system_one(
        {"task": state, "profiles": profiles},
        {
            "profile": {
                "type": "choice",
                "instructions": "Which configured reasoning profile is the best fit for this task, considering complexity, required capabilities, and risk? Choose only among supplied profiles.",
                "criteria": profiles,
            },
            "system2_need": {
                "type": "score",
                "instructions": "How much deep System-2 reasoning does this task likely require?",
                "criteria": [
                    "Minimal; bounded semantic or deterministic handling is enough.",
                    "Some reasoning, but narrow and routine.",
                    "Substantial multi-step reasoning or evidence correlation.",
                    "Deep specialist reasoning is important for correctness or safety.",
                ],
            },
        },
        api_key=api_key,
        sender=sender,
    )
