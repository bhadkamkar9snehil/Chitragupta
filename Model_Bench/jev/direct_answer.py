"""Jev decides whether audited facts answer the ticket, and which outcome they support.

Jev writes nothing. It picks one outcome; the harness renders the reply from the
recorded values (Model_Bench/direct_answer.py).
"""
from __future__ import annotations

from typing import Any

from .client import system_one

OUTCOMES = {
    "CONFIRMED": "The requester quoted values and the recorded values match them: the reported concern does not hold.",
    "CORRECTED": "The requester quoted values and at least one recorded value differs: the answer is the official recorded values.",
    "ANSWERED": "The requester asked for current values/status and the listed recorded fields directly answer it.",
    "NOT_FOUND": "No record exists for the ticket's identifier in the searched tables, so the requester must confirm it.",
    "NEEDS_REASONING": "The facts do not directly answer the question (cause analysis, calculation, missing fields, or a different table is needed).",
}

QUESTIONS = {
    "outcome": {
        "type": "choice",
        "instructions": (
            "The harness read live records for this ticket and extracted the fields the ticket "
            "names (facts: recorded value, the value the requester reported if any, and whether "
            "they match). Choose the outcome these facts support for the requester's actual "
            "question. Choose NEEDS_REASONING whenever the question asks why, asks for a "
            "calculation, or the listed fields are not the ones the question is about."
        ),
        "criteria": OUTCOMES,
    },
    "facts_answer_question": {
        "type": "noul",
        "instructions": "Do the listed recorded fields directly answer what the requester asked, with nothing essential missing?",
    },
}


def choose_outcome(state: dict[str, Any], *, api_key: str | None = None, sender=None) -> dict[str, Any]:
    """state: {"ticket": requester text fields, "fact_table": compact facts}."""
    return system_one(state, QUESTIONS, api_key=api_key, sender=sender)
