"""Parallel ticket characterization."""
from __future__ import annotations
from typing import Any

from .client import system_one


def _criteria(manifest: dict[str, Any], allowed_routes: list[str] | None = None) -> dict[str, Any]:
    allowed = set(allowed_routes or [])
    out: dict[str, Any] = {}
    for row in manifest.get("routes", []):
        route = str(row.get("route") or "").strip()
        if not route or (allowed and route not in allowed):
            continue
        out[route] = {
            "description": row.get("description") or route.replace("_", " "),
            "typical_indicators": row.get("keywords") or [],
        }
    return out


def assess_ticket(
    ticket_state: dict[str, Any],
    manifest: dict[str, Any],
    *,
    allowed_routes: list[str] | None = None,
    api_key: str | None = None,
    sender=None,
) -> dict[str, Any]:
    routes = _criteria(manifest, allowed_routes)
    if not routes:
        return {"ok": False, "reason": "No canonical routes available", "answers": {}}
    questions = {
        "route": {
            "type": "choice",
            "instructions": "Choose the canonical Chitragupta investigation route that best matches the supplied ticket.",
            "criteria": routes,
        },
        "cross_domain": {
            "type": "noul",
            "instructions": "Does the ticket materially span more than one investigation domain rather than having one primary domain?",
        },
        "ticket_ambiguity": {
            "type": "score",
            "instructions": "Rate how ambiguous the ticket is for investigation planning.",
            "criteria": [
                "Direct and explicit; identifiers and requested behavior are clear.",
                "Some interpretation is required but the likely investigation target is clear.",
                "Materially ambiguous; multiple plausible interpretations or missing important scope.",
                "Insufficiently scoped; useful investigation cannot be selected without substantial discovery or requester clarification.",
            ],
        },
        "investigation_complexity": {
            "type": "score",
            "instructions": "Rate expected investigation complexity from the ticket as written.",
            "criteria": [
                "One obvious bounded live check.",
                "Small investigation across a few known evidence points.",
                "Multiple evidence surfaces or dependencies must be correlated.",
                "Cross-domain, unusually broad, or likely to require extensive discovery.",
            ],
        },
        "likely_requires_live_state": {
            "type": "noul",
            "instructions": "Will resolving or accurately answering the ticket likely require current live operational or database state?",
        },
        "likely_requires_schema_discovery": {
            "type": "noul",
            "instructions": "Is schema or object discovery likely necessary because the relevant database objects are not obvious from the ticket?",
        },
        "likely_existing_known_issue": {
            "type": "noul",
            "instructions": "Does the ticket look like a recurring or known support pattern that could plausibly match reusable knowledge?",
        },
    }
    return system_one({"ticket": ticket_state}, questions, api_key=api_key, sender=sender)
