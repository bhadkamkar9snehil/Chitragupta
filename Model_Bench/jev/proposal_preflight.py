"""Semantic proposal checks before independent review."""
from __future__ import annotations
from typing import Any

from .client import system_one


RESPONSE_TYPES = {
    "UPDATE": "Verified progress exists but no final outcome is established.",
    "QUESTION": "A specific requester fact is genuinely required and cannot be established from current evidence.",
    "RESOLUTION": "A final outcome or fix is supported strongly enough to close after independent review.",
    "L3_ESCALATION": "Root cause remains unresolved, evidence is contradictory beyond L2, or specialist investigation is required.",
    "NEEDS_HUMAN_ACTION": "Cause and corrective action are known, but execution is outside the approved L2 worker authority.",
}


def assess_proposal(state: dict[str, Any], *, api_key: str | None = None, sender=None) -> dict[str, Any]:
    questions = {
        "evidence_supports_core_claim": {
            "type": "noul",
            "instructions": "Does the supplied evidence materially support the core factual claim made by the proposal?",
        },
        "reply_overstates_evidence": {
            "type": "noul",
            "instructions": "Does the proposed reply state certainty, causation, completion, or success more strongly than the supplied evidence supports?",
        },
        "reply_claims_action_was_performed": {
            "type": "noul",
            "instructions": "Does the proposed reply claim or clearly imply that a corrective, configuration, or production action was actually performed?",
        },
        "audit_shows_claimed_action": {
            "type": "noul",
            "instructions": "If the proposal claims an action was performed, does the run action audit contain evidence of that performed action? If no action is claimed, answer yes.",
        },
        "root_cause_is_established_not_speculative": {
            "type": "noul",
            "instructions": "Is the proposed root cause established by evidence rather than merely plausible or speculative?",
        },
        "requester_information_is_still_required": {
            "type": "noul",
            "instructions": "Is specific requester information still genuinely required before the issue can be advanced accurately?",
        },
        "proposed_response_type": {
            "type": "choice",
            "instructions": "Which response type best matches the evidence and current worker authority?",
            "criteria": RESPONSE_TYPES,
        },
        "review_risk": {
            "type": "score",
            "instructions": "Rate semantic risk if this proposal were published without deeper verification.",
            "criteria": [
                "Routine; claims are narrow and directly supported.",
                "Needs focused verification of one or two claims.",
                "Materially risky; important claims or workflow outcome are uncertain.",
                "Unsafe without deeper review; likely overclaim, contradiction, or authority mismatch.",
            ],
        },
    }
    return system_one(state, questions, api_key=api_key, sender=sender)
