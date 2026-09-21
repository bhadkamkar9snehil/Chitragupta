"""Reusable System-One support-action selection for a future Hermes L1 surface.

Chitragupta currently has no L1 runtime in this repository, so this module is a
ready integration primitive rather than a lifecycle mutation.
"""
from __future__ import annotations
from typing import Any

from .client import system_one


DEFAULT_ACTIONS = {
    "ANSWER_FROM_VERIFIED_KNOWLEDGE": "A supported answer can be given from verified reference knowledge without live investigation.",
    "ASK_CLARIFYING_QUESTION": "One specific requester fact is required before useful progress can be made.",
    "HANDOFF_L2": "Live state, specialist investigation, or L2 evidence is needed.",
    "NEEDS_HUMAN_ACTION": "The action is understood but requires authorized human execution.",
}


def assess_l1_action(
    state: dict[str, Any],
    *,
    actions: dict[str, Any] | None = None,
    api_key: str | None = None,
    sender=None,
) -> dict[str, Any]:
    criteria = actions or DEFAULT_ACTIONS
    return system_one(
        state,
        {
            "support_action": {
                "type": "choice",
                "instructions": "Choose the next supported L1 action. Do not invent an action outside the supplied choices.",
                "criteria": criteria,
            },
            "can_resolve_without_live_investigation": {
                "type": "noul",
                "instructions": "Can this request be correctly resolved without current private/live operational evidence?",
            },
            "requires_l2_evidence": {
                "type": "noul",
                "instructions": "Does this request require L2 investigation or live evidence rather than a knowledge-only answer?",
            },
            "handoff_risk": {
                "type": "score",
                "instructions": "Rate the risk of trying to resolve this entirely at L1.",
                "criteria": [
                    "Low risk; routine supported answer.",
                    "Some uncertainty; verify scope or one fact.",
                    "Material risk of wrong answer without L2 evidence.",
                    "High risk; must not be resolved at L1.",
                ],
            },
        },
        api_key=api_key,
        sender=sender,
    )
