"""Small reusable TypeSafe System One adapter.

Uses the public HTTP contract directly so Chitragupta remains dependency-free.
All workflow modules call this one adapter; no feature reimplements transport.
"""
from __future__ import annotations

import json
import os
import socket
import time
import urllib.error
import urllib.request
from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any

from . import policy

DEFAULT_BASE_URL = "https://api.typesafe.ai"
DEFAULT_MODEL = "jev-latest"
SYSTEM_ONE_PATH = "/v1/systemone"
DEFAULT_TIMEOUT = 10.0
REPO_ROOT = Path(__file__).resolve().parents[2]
DEV_ENV_FILE = REPO_ROOT / "deploy" / "dev" / "typesafe.env"

JsonSender = Callable[[str, dict[str, Any], dict[str, str], float], dict[str, Any]]


def _float_env(name: str, default: float) -> float:
    try:
        value = float(os.environ.get(name, default))
    except (TypeError, ValueError):
        return default
    return value if value > 0 else default


def _dev_api_key() -> str:
    """Load the explicitly-approved dev key without exposing it to model context."""
    try:
        for raw in DEV_ENV_FILE.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            if line.startswith("TYPESAFE_API_KEY="):
                return line.split("=", 1)[1].strip()
    except OSError:
        pass
    return ""


def resolved_api_key(api_key: str | None = None) -> str:
    return (api_key or os.environ.get("TYPESAFE_API_KEY", "") or _dev_api_key()).strip()


def typesafe_available(api_key: str | None = None) -> bool:
    return bool(policy.JEV_ENABLED and resolved_api_key(api_key))


def _http_sender(url: str, payload: dict[str, Any], headers: dict[str, str], timeout: float) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        data=json.dumps(payload, separators=(",", ":"), default=str).encode("utf-8"),
        headers=headers,
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        decoded = json.loads(response.read().decode("utf-8"))
    if not isinstance(decoded, dict):
        raise ValueError("TypeSafe response is not a JSON object")
    return decoded


def system_one(
    state: Any,
    questions: Mapping[str, dict[str, Any]],
    *,
    api_key: str | None = None,
    model: str | None = None,
    timeout: float | None = None,
    sender: JsonSender | None = None,
) -> dict[str, Any]:
    """Execute one multi-question System One request and return a safe envelope."""
    if not policy.JEV_ENABLED:
        return {"ok": False, "enabled": False, "reason": "CHITRAGUPTA_JEV_ENABLED is disabled", "answers": {}}

    key = resolved_api_key(api_key)
    if not key:
        return {"ok": False, "enabled": False, "reason": "TYPESAFE_API_KEY is not configured", "answers": {}}
    if not questions:
        return {"ok": False, "enabled": True, "reason": "No questions supplied", "answers": {}}

    resolved_model = (model or os.environ.get("TYPESAFE_DEFAULT_MODEL") or DEFAULT_MODEL).strip()
    base = (os.environ.get("TYPESAFE_BASE_URL") or DEFAULT_BASE_URL).rstrip("/")
    resolved_timeout = timeout or _float_env("CHITRAGUPTA_JEV_TIMEOUT_SECONDS", DEFAULT_TIMEOUT)

    payload = {"model": resolved_model, "state": state, "questions": dict(questions)}
    headers = {
        "Authorization": f"Bearer {key}",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "chitragupta-jev-fabric/1",
    }
    started = time.monotonic()
    send = sender or _http_sender
    try:
        raw = send(base + SYSTEM_ONE_PATH, payload, headers, resolved_timeout)
        answers = raw.get("answers")
        if not isinstance(answers, dict):
            raise ValueError("TypeSafe response has no answers object")
        return {
            "ok": True,
            "enabled": True,
            "model": str(raw.get("model") or resolved_model),
            "answers": answers,
            "usage": raw.get("usage") or {},
            "latency_ms": round((time.monotonic() - started) * 1000, 2),
        }
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
            "ok": False,
            "enabled": True,
            "reason": "TypeSafe request/response failed",
            "error_type": type(exc).__name__,
            "answers": {},
            "latency_ms": round((time.monotonic() - started) * 1000, 2),
        }
