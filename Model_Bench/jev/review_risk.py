"""Review-depth judgment. Adaptive behavior remains disabled until calibrated."""
from __future__ import annotations
from typing import Any

from .client import system_one


def assess_review_risk(state: dict[str, Any], *, api_key: str | None = None, sender=None) -> dict[str, Any]:
    return system_one(
        state,
        {
            "requires_full_reasoning_review": {
                "type": "noul",
                "instructions": "Does this proposal materially benefit from full independent reasoning review rather than a lightweight structural and semantic check?",
            },
            "risk_level": {
                "type": "score",
                "instructions": "Rate consequence and uncertainty risk of publishing this proposal.",
                "criteria": [
                    "Low-risk informational or update response with directly supported claims.",
                    "Moderate; focused verification is appropriate.",
                    "High; substantial reasoning and evidence verification is required.",
                    "Very high; publication without deep review would be unsafe.",
                ],
            },
        },
        api_key=api_key,
        sender=sender,
    )
