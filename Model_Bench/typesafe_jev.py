#!/usr/bin/env python3
"""Compatibility facade for Chitragupta's TypeSafe Jev fabric.

New integrations should import Model_Bench/jev workflow modules. This module
retains choose_route() for the original PR #9 routing integration and exports
system_one() as the reusable primitive.
"""
from __future__ import annotations

import os
from collections.abc import Iterable
from typing import Any

from jev.client import system_one
from jev.policy import MIN_CHOICE_CONFIDENCE


def _route_definitions(
    manifest: dict[str, Any],
    allowed_routes: Iterable[str] | None = None,
) -> dict[str, Any]:
    allowed = set(allowed_routes or [])
    restrict = bool(allowed)
    criteria: dict[str, Any] = {}
    for route_def in manifest.get("routes", []):
        route = str(route_def.get("route") or "").strip()
        if not route or (restrict and route not in allowed):
            continue
        criteria[route] = {
            "description": str(route_def.get("description") or route.replace("_", " ")),
            "typical_indicators": [str(k) for k in (route_def.get("keywords") or [])],
            "fallback": route == "discover",
        }
    return criteria


def choose_route(
    query: str,
    manifest: dict[str, Any],
    *,
    allowed_routes: Iterable[str] | None = None,
    min_confidence: float | None = None,
    api_key: str | None = None,
    sender=None,
) -> dict[str, Any]:
    """Choose one canonical route while preserving deterministic fallback semantics."""
    criteria = _route_definitions(manifest, allowed_routes)
    if not criteria:
        return {"enabled": True, "accepted": False, "reason": "No canonical route criteria were available"}
    if len(criteria) == 1:
        only = next(iter(criteria))
        return {
            "enabled": True,
            "accepted": True,
            "choice": only,
            "confidence": 1.0,
            "probabilities": {only: 1.0},
            "model": "deterministic-single-option",
            "reason": "Only one canonical route was eligible",
        }

    threshold = MIN_CHOICE_CONFIDENCE if min_confidence is None else max(0.0, min(1.0, min_confidence))
    result = system_one(
        {"ticket_text": query},
        {
            "route": {
                "type": "choice",
                "instructions": (
                    "Choose the single canonical Chitragupta investigation route that best matches "
                    "the support ticket. Select only from supplied criteria. Prefer a specific route "
                    "when clearly applicable; use discover only when no specific route clearly fits."
                ),
                "criteria": criteria,
            }
        },
        api_key=api_key,
        sender=sender,
    )
    if not result.get("ok"):
        return {
            "enabled": bool(result.get("enabled")),
            "accepted": False,
            "reason": result.get("reason") or "TypeSafe request failed",
            "error_type": result.get("error_type"),
        }

    answer = (result.get("answers") or {}).get("route") or {}
    if answer.get("type") != "choice":
        return {"enabled": True, "accepted": False, "reason": "TypeSafe route answer is not a choice"}
    choice = str(answer.get("choice") or "")
    if choice not in criteria:
        return {
            "enabled": True,
            "accepted": False,
            "reason": "TypeSafe returned a route outside the supplied criteria",
            "error_type": "ValueError",
        }
    try:
        confidence = float(answer.get("confidence"))
    except (TypeError, ValueError):
        return {
            "enabled": True,
            "accepted": False,
            "reason": "TypeSafe route confidence is invalid",
            "error_type": "ValueError",
        }
    probabilities = answer.get("probabilities") if isinstance(answer.get("probabilities"), dict) else {}
    return {
        "enabled": True,
        "accepted": confidence >= threshold,
        "choice": choice,
        "confidence": round(confidence, 6),
        "probabilities": probabilities,
        "model": result.get("model") or os.environ.get("TYPESAFE_DEFAULT_MODEL", "jev-latest"),
        "min_confidence": threshold,
        "reason": None if confidence >= threshold else "Jev confidence below configured threshold",
        "latency_ms": result.get("latency_ms"),
    }


__all__ = ["system_one", "choose_route"]
