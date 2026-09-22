"""Jev assessment and meta-attention over deterministic ticket evidence."""
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
    "execution_mode": {
        "type": "choice",
        "instructions": (
            "Recommend the cheapest sufficient next reasoning mode. This is advisory only: "
            "the deterministic runtime will independently gate whether Qwen may actually be skipped."
        ),
        "criteria": {
            "QWEN_FREE": (
                "No local-model reasoning or prose generation is needed. Use only when the evidence "
                "supports a bounded deterministic handoff/outcome that can be rendered without inventing facts."
            ),
            "COMPOSE_ONLY": (
                "Evidence and semantic decisions are already strong; a local model is useful only to compose "
                "concise user-facing wording from supplied context, with at most a tiny focused recovery read."
            ),
            "FOCUSED_REASONING": (
                "Contradiction, causality, missing evidence, or domain interpretation still requires System-2 reasoning."
            ),
        },
    },
    "needs_route_skill": {
        "type": "noul",
        "instructions": (
            "Does the next local System-2 step materially need the route-specific domain skill, rather than "
            "only the base L2 workflow and already-compiled evidence?"
        ),
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

_CONTEXT_LEVELS = [
    "Omit from the next local-model context: this chunk is irrelevant, redundant, stale, or lower-value than other supplied evidence.",
    "Show only a terse provenance/identity summary so the local model knows this source exists without spending context on its details.",
    "Show a compact structured representation containing the fields needed for the next synthesis/reasoning step.",
    "Show the full bounded chunk because its details materially matter to the next synthesis/reasoning step.",
]


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


def _context_attention_questions(state: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """Score how much of each explicit state chunk the next System-2 step needs.

    The chunk metadata points at state already present in this same request, so
    we do not duplicate evidence just to ask the relevance question.
    """
    questions: dict[str, dict[str, Any]] = {}
    chunks = state.get("context_chunks") or []
    if not isinstance(chunks, list):
        return questions

    for chunk in chunks[:20]:
        if not isinstance(chunk, dict):
            continue
        question_id = str(chunk.get("attention_question") or "")
        state_path = str(chunk.get("state_path") or "")
        if not question_id.startswith("context_c") or not state_path:
            continue
        questions[question_id] = {
            "type": "score",
            "instructions": {
                "task": (
                    "For the next local System-2 investigation/synthesis step, how much of "
                    "this explicit context chunk should be shown? Judge relevance and needed "
                    "detail only; do not change its authority or treat historical/KB material "
                    "as proof of the current incident."
                ),
                "chunk_path": state_path,
                "chunk_kind": chunk.get("kind"),
                "authority": chunk.get("authority"),
                "source": chunk.get("source"),
            },
            "criteria": _CONTEXT_LEVELS,
        }
    return questions


def assess_investigation(
    state: dict[str, Any],
    *,
    api_key: str | None = None,
    sender=None,
) -> dict[str, Any]:
    questions = dict(_STATIC_QUESTIONS)
    questions["known_solution"] = _known_solution_question(state)
    questions.update(_context_attention_questions(state))
    return system_one(state, questions, api_key=api_key, sender=sender)
