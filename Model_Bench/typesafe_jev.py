#!/usr/bin/env python3
"""TypeSafe Jev semantic judgments for Chitragupta.

This module is deliberately small and dependency-free. It speaks the current
TypeSafe System One HTTP contract directly so the deterministic helpdesk harness
does not need to install another Python package on the production Windows/WSL
path.

Jev is advisory here. Chitragupta owns routing policy and every workflow/action
boundary; Jev only chooses among canonical routes already defined in
Knowledge/manifest.json. Callers must retain deterministic fallbacks.
"""
from __future__ import annotations

import json
import os
import socket
import urllib.error
import urllib.request
from collections.abc import Callable, Iterable
from typing import Any

DEFAULT_BASE_URL = "https://api.typesafe.ai"
DEFAULT_MODEL = "jev-latest"
DEFAULT_TIMEOUT_SECONDS = 10.0
DEFAULT_MIN_CONFIDENCE = 0.70
SYSTEM_ONE_PATH = "/v1/systemone"

JsonSender = Callable[[str, dict[str, Any], dict[str, str], float], dict[str, Any]]


def _env_enabled() -> bool:
    raw = os.environ.get("CHITRAGUPTA_JEV_ENABLED", "1").strip().lower()
    return raw not in {"0", "false", "no", "off", "disabled"}


def _float_env(name: str, default: float) -> float:
    raw = os.environ.get(name)
    if not raw:
        return default
    try:
        value = float(raw)
    except ValueError:
        return default
    return value if value > 0 else default


def _route_definitions(
    manifest: dict[str, Any],
    allowed_routes: Iterable[str] | None = None,
) -> dict[str, str]:
    allowed = set(allowed_routes or [])
    restrict = bool(allowed)
    criteria: dict[str, str] = {}

    for route_def in manifest.get("routes", []):
        route = str(route_def.get("route") or "").strip()
        if not route or (restrict and route not in allowed):
            continue
        description = str(route_def.get("description") or "").strip()
        keywords = [str(k).strip() for k in (route_def.get("keywords") or []) if str(k).strip()]
        detail = description or route.replace("_", " ")
        if keywords:
            detail += " Typical indicators: " + ", ".join(keywords[:16]) + "."
        if route == "discover":
            detail += " Use this when no specific canonical route clearly fits or the symptom is genuinely cross-domain."
        criteria[route] = detail

    return criteria


def _http_json_sender(
    url: str,
    payload: dict[str, Any],
    headers: dict[str, str],
    timeout: float,
) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        data=json.dumps(payload, separators=(",", ":")).encode("utf-8"),
        headers=headers,
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        body = response.read()
    decoded = json.loads(body.decode("utf-8"))
    if not isinstance(decoded, dict):
        raise ValueError("TypeSafe response is not a JSON object")
    return decoded


def choose_route(
    query: str,
    manifest: dict[str, Any],
    *,
    allowed_routes: Iterable[str] | None = None,
    min_confidence: float | None = None,
    api_key: str | None = None,
    sender: JsonSender | None = None,
) -> dict[str, Any]:
    """Ask Jev to choose one canonical Chitragupta route.

    The return value is always structured and never raises for normal service
    failures. accepted is true only when the response is valid and meets the
    configured confidence gate.
    """
    if not _env_enabled():
        return {
            "enabled": False,
            "accepted": False,
            "reason": "CHITRAGUPTA_JEV_ENABLED is disabled",
        }

    key = (api_key if api_key is not None else os.environ.get("TYPESAFE_API_KEY", "")).strip()
    if not key:
        return {
            "enabled": False,
            "accepted": False,
            "reason": "TYPESAFE_API_KEY is not configured",
        }

    criteria = _route_definitions(manifest, allowed_routes)
    if not criteria:
        return {
            "enabled": True,
            "accepted": False,
            "reason": "No canonical route criteria were available",
        }
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

    model = os.environ.get("TYPESAFE_DEFAULT_MODEL", DEFAULT_MODEL).strip() or DEFAULT_MODEL
    base_url = os.environ.get("TYPESAFE_BASE_URL", DEFAULT_BASE_URL).strip().rstrip("/") or DEFAULT_BASE_URL
    timeout = _float_env("CHITRAGUPTA_JEV_TIMEOUT_SECONDS", DEFAULT_TIMEOUT_SECONDS)
    threshold = min_confidence if min_confidence is not None else _float_env(
        "CHITRAGUPTA_JEV_MIN_CONFIDENCE", DEFAULT_MIN_CONFIDENCE
    )
    threshold = max(0.0, min(1.0, threshold))

    payload: dict[str, Any] = {
        "model": model,
        "state": {
            "ticket_text": query,
        },
        "questions": {
            "route": {
                "type": "choice",
                "instructions": (
                    "Choose the single canonical Chitragupta investigation route that best matches "
                    "the support ticket in ticket_text. Select only from the supplied criteria. "
                    "Prefer a specific route when the ticket clearly belongs there; choose discover "
                    "only when no specific route clearly fits or the symptom is genuinely cross-domain."
                ),
                "criteria": criteria,
            }
        },
    }
    headers = {
        "Authorization": f"Bearer {key}",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "chitragupta-typesafe-jev/1",
    }

    send = sender or _http_json_sender
    try:
        raw = send(base_url + SYSTEM_ONE_PATH, payload, headers, timeout)
        answer = ((raw.get("answers") or {}).get("route") or {})
        if answer.get("type") != "choice":
            raise ValueError("TypeSafe route answer is not a choice")
        choice = str(answer.get("choice") or "")
        confidence = float(answer.get("confidence"))
        probabilities = answer.get("probabilities") or {}
        if choice not in criteria:
            raise ValueError("TypeSafe returned a route outside the supplied criteria")
        if not isinstance(probabilities, dict):
            raise ValueError("TypeSafe probabilities are not an object")
    except (
        OSError,
        TimeoutError,
        socket.timeout,
        urllib.error.URLError,
        urllib.error.HTTPError,
        ValueError,
        TypeError,
        KeyError,
        json.JSONDecodeError,
    ) as exc:
        return {
            "enabled": True,
            "accepted": False,
            "reason": "TypeSafe request/response failed",
            "error_type": type(exc).__name__,
        }

    return {
        "enabled": True,
        "accepted": confidence >= threshold,
        "choice": choice,
        "confidence": round(confidence, 6),
        "probabilities": {
            str(k): round(float(v), 6)
            for k, v in probabilities.items()
            if isinstance(v, (int, float))
        },
        "model": str(raw.get("model") or model),
        "min_confidence": threshold,
        "reason": None if confidence >= threshold else "Jev confidence below configured threshold",
    }
