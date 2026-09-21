"""Semantic assessment for already-structurally-safe typed tool calls."""
from __future__ import annotations
from typing import Any

from .client import system_one


def assess_tool_call(state: dict[str, Any], *, api_key: str | None = None, sender=None) -> dict[str, Any]:
    return system_one(
        state,
        {
            "relevant_to_investigation": {
                "type": "noul",
                "instructions": "Is the proposed typed-tool call relevant to the supplied investigation context and current evidence goal?",
            },
            "excessively_broad": {
                "type": "noul",
                "instructions": "Is the proposed read substantially broader than necessary for the stated investigation context?",
            },
            "likely_duplicate_of_previous_read": {
                "type": "noul",
                "instructions": "Is the proposed read materially duplicating a previous read without a meaningful narrowing or new evidence purpose?",
            },
            "semantic_risk": {
                "type": "score",
                "instructions": "Rate how likely this call is to waste investigation budget while adding little useful evidence. Structural SQL safety is checked elsewhere.",
                "criteria": [
                    "Focused and useful.",
                    "Minor semantic inefficiency.",
                    "Likely wasteful or weakly relevant.",
                    "Strong sign of looping, broad fishing, or unrelated investigation.",
                ],
            },
        },
        api_key=api_key,
        sender=sender,
    )
