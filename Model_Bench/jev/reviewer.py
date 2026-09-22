"""Primary semantic reviewer for a frozen Chitragupta proposal.

Jev makes the bounded semantic decision. Deterministic code still owns lifecycle,
publication, SQL safety, and the thresholds that decide whether a local deep
review is required.
"""
from __future__ import annotations
from typing import Any

from .client import system_one


DECISIONS = {
    "APPROVE": "Evidence supports the proposal, the response type fits, no material overclaim/action-authority mismatch is present, and publication can proceed.",
    "REWORK": "The proposal has a specific correctable semantic/evidence problem that should go back to investigation.",
    "LOCAL_REVIEW": "The case is ambiguous, conflicting, high-risk, or requires deeper System-2 reasoning before publication.",
    "L3_ESCALATION": "The evidence indicates the issue is outside bounded L2/Jev handling or cannot be safely resolved within current authority.",
}

REWORK_REASONS = {
    "EVIDENCE_GAP": "Core claim is not adequately supported by current live evidence.",
    "OVERCLAIM": "Reply states certainty, causation, completion, or success beyond the evidence.",
    "ACTION_AUTHORITY": "Reply claims/implies a performed action that is not supported by the action audit or worker authority.",
    "RESPONSE_TYPE": "Chosen response type does not fit the evidence/current authority.",
    "ROOT_CAUSE": "Root cause is speculative or contradicted.",
    "REQUESTER_INFO": "A specific requester fact is still required.",
    "OTHER": "A bounded semantic issue exists that does not fit the other categories.",
}


QUESTIONS = {
    "decision": {
        "type": "choice",
        "instructions": (
            "Act as the primary bounded semantic reviewer. Choose APPROVE only when the "
            "frozen proposal is supported by the supplied live evidence and action audit, "
            "does not overclaim, and matches worker authority. Use LOCAL_REVIEW when deeper "
            "reasoning is genuinely required rather than guessing."
        ),
        "criteria": DECISIONS,
    },
    "rework_reason": {
        "type": "choice",
        "instructions": "If the decision is REWORK, choose the main correctable reason. Otherwise choose OTHER.",
        "criteria": REWORK_REASONS,
    },
    "evidence_supports_core_claim": {
        "type": "noul",
        "instructions": "Does the supplied evidence materially support the proposal's core factual claim?",
    },
    "reply_overstates_evidence": {
        "type": "noul",
        "instructions": "Does the reply overstate certainty, causation, completion, or success relative to the evidence?",
    },
    "reply_claims_action_was_performed": {
        "type": "noul",
        "instructions": "Does the reply claim or clearly imply that a corrective/configuration/production action was performed?",
    },
    "audit_shows_claimed_action": {
        "type": "noul",
        "instructions": "If the reply claims an action was performed, is that action supported by the action audit? If no action is claimed, answer yes.",
    },
    "root_cause_established": {
        "type": "noul",
        "instructions": "If a root cause is asserted, is it established by current evidence rather than merely plausible?",
    },
    "response_type_fit": {
        "type": "noul",
        "instructions": "Does the proposed response type fit the evidence, unresolved uncertainty, requester-information needs, and worker authority?",
    },
    "needs_deep_local_reasoning": {
        "type": "noul",
        "instructions": "Would a stronger local/System-2 reviewer materially improve correctness because evidence is conflicting, nuanced, or underdetermined?",
    },
    "publication_risk": {
        "type": "score",
        "instructions": "Rate semantic/publication risk of publishing the frozen proposal now.",
        "criteria": [
            "Low: narrow claims directly supported; no authority mismatch.",
            "Moderate: one focused uncertainty remains.",
            "High: material evidence/claim ambiguity or response-type risk.",
            "Very high: likely false success, unsupported action, major overclaim, or unsafe outcome.",
        ],
    },
}


def review_proposal(
    state: dict[str, Any],
    *,
    api_key: str | None = None,
    sender=None,
) -> dict[str, Any]:
    return system_one(state, QUESTIONS, api_key=api_key, sender=sender)
