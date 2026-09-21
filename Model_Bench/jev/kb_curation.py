"""Post-resolution semantic KB curation."""
from __future__ import annotations
from typing import Any

from .client import system_one


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
