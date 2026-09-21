"""Jev assessment of deterministic evidence gathered for one ticket."""
from __future__ import annotations

from typing import Any

from .client import system_one


_STATIC_QUESTIONS = {
    "evidence_sufficient": {
        "type": "noul",
        "instructions": "Is the gathered current-ticket evidence sufficient to choose a support outcome without broad additional discovery?",
    },
    "response_type": {
        "type": "choice",
        "instructions": "Choose the best current support outcome from the evidence.",
        "criteria": {
            "UPDATE": "Verified progress but no final outcome is established.",
            "QUESTION": "A specific requester fact is still required.",
            "RESOLUTION": "Current evidence establishes a final outcome or verified fix.",
            "L3_ESCALATION": "The issue remains unresolved/outside bounded L2 or evidence is contradictory.",
            "NEEDS_HUMAN_ACTION": "Cause/action are known but execution requires authorized human action.",
        },
    },
    "root_cause_family": {
        "type": "choice",
        "instructions": "Choose the best supported root-cause family; choose UNKNOWN if current evidence does not establish one.",
        "criteria": {
            "DATA_ENTRY_ERROR": "Incorrect manual/operator-entered value.",
            "SAP_INTEGRATION_FAILURE": "SAP/API/posting path failed or rejected.",
            "SENSOR_DATA_SYNC_DELAY": "Real event occurred but persisted/view state lagged or was out of sync.",
            "CONFIGURATION_GAP": "Required mapping, limit, route, or rule is absent/misconfigured.",
            "PROCESS_DEVIATION": "Underlying production/process deviation is real.",
            "SOFTWARE_DEFECT": "Application/view/SP logic is demonstrably defective.",
            "INFRASTRUCTURE": "Environment/tooling/service failure is causal.",
            "USER_TRAINING": "System behavior is correct; workflow was misunderstood.",
            "UNKNOWN": "Evidence does not establish a root-cause family.",
        },
    },
    "needs_additional_probe": {
        "type": "noul",
        "instructions": "Would one more bounded evidence probe materially improve the support outcome?",
    },
    "needs_local_model": {
        "type": "noul",
        "instructions": "Is deeper local/System-2 reasoning still needed after this structured evidence assessment, beyond composing concise user-facing wording?",
    },
    "human_action_required": {
        "type": "noul",
        "instructions": "Is the corrective action outside the ordinary read-only investigator authority and therefore requires an authorized human?",
    },
    "confidence_quality": {
        "type": "score",
        "instructions": "Rate how strong and internally consistent the current evidence package is.",
        "criteria": [
            "Weak/insufficient.",
            "Some useful evidence but important gaps remain.",
            "Strong enough for a bounded support outcome.",
            "Decisive and internally consistent.",
        ],
    },
}


def _known_solution_question(state: dict[str, Any]) -> dict[str, Any]:
    criteria: dict[str, Any] = {
        "NONE": "No known solution is sufficiently supported by current evidence."
    }
    for index, row in enumerate((state.get("known_solutions") or [])[:10]):
        criteria[f"s{index}"] = {
            "title": row.get("title"),
            "source_ref": row.get("source_ref"),
            "root_cause": row.get("root_cause"),
            "resolution_steps": row.get("resolution_steps"),
        }
    return {
        "type": "choice",
        "instructions": "Choose a known solution only if current evidence supports applying it to this ticket; otherwise choose NONE.",
        "criteria": criteria,
    }


def assess_investigation(
    state: dict[str, Any],
    *,
    api_key: str | None = None,
    sender=None,
) -> dict[str, Any]:
    questions = dict(_STATIC_QUESTIONS)
    questions["known_solution"] = _known_solution_question(state)
    return system_one(state, questions, api_key=api_key, sender=sender)
