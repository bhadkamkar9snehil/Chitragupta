"""Bounded Jev selection of which real schema relationships are worth
following from a row a prior probe already returned.

This is the "grow the evidence tree one real edge at a time" step: probing
a table returns a row; that row may contain foreign-key-style values the
semantic atlas already knows connect to other real tables (xstudio_semantic_
atlas.json's `relationships`, human/config-derived, never invented). Rather
than have Qwen notice a connection and freehand a new SELECT (the exact
hallucination risk this whole design avoids), Jev picks which of the small,
already-real set of available hops are worth also fetching for this ticket.
Deterministic code executes the chosen hops via probe_related_table(),
using the value already in hand -- no new filter is derived or guessed.
"""
from __future__ import annotations
from typing import Any

from .client import system_one


def select_relationship_hops(
    ticket: dict[str, Any],
    primary_table: str,
    primary_row: dict[str, Any],
    available_hops: list[dict[str, Any]],
    *,
    api_key: str | None = None,
    sender=None,
) -> dict[str, Any]:
    """available_hops: [{"source_column", "source_value", "target_database",
    "target_table", "target_column", "cardinality"}, ...] -- all real,
    already-resolved edges from the atlas whose source_column is present
    with a non-null value on primary_row. Never invented, never guessed.
    """
    limited = {f"h{i}": hop for i, hop in enumerate(available_hops[:10])}
    if not limited:
        return {"ok": True, "answers": {}, "selected": []}

    questions: dict[str, Any] = {}
    for label in limited:
        questions[f"worth_fetching_{label}"] = {
            "type": "noul",
            "instructions": {
                "task": (
                    "Given the ticket and the row already fetched from the primary table, "
                    "would following this real known relationship to fetch the related row "
                    "plausibly add evidence value for this specific ticket? Do not select a "
                    "hop just because it exists -- most real relationships are irrelevant to "
                    "any one ticket."
                ),
                "ticket_path": "ticket",
                "primary_row_path": "primary_row",
                "hop_path": f"available_hops.{label}",
            },
        }

    result = system_one(
        {
            "ticket": ticket,
            "primary_table": primary_table,
            "primary_row": primary_row,
            "available_hops": limited,
        },
        questions,
        api_key=api_key,
        sender=sender,
    )
    if not result.get("ok"):
        return {**result, "selected": []}

    answers = result.get("answers") or {}
    selected = []
    for label, hop in limited.items():
        answer = answers.get(f"worth_fetching_{label}") or {}
        worth = float(answer.get("noul") or 0.0) if answer.get("type") == "noul" else 0.0
        if worth >= 0.60:
            selected.append({**hop, "jev_worth_fetching": round(worth, 6)})
    selected.sort(key=lambda h: -h["jev_worth_fetching"])
    return {**result, "selected": selected}
