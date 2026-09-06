#!/usr/bin/env python3
"""Temporary dispatch-time adapter for the shared XStudio GBrain.

Hermes workers use GBrain natively through MCP. This module exists only for the
legacy dispatch-time prefetch path in l2_pipeline_runtime.py and should disappear
when that prefetch is moved in-process.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path
from typing import Any

DEFAULT_GBRAIN_HOME = Path.home() / ".hermes" / "xstudio-gbrain"
DEFAULT_TIMEOUT = max(10, int(os.environ.get("XSTUDIO_GBRAIN_TIMEOUT_SECONDS", "60")))

SOURCE_IDS: tuple[str, ...] = (
    "xstudio-knowledge",
    "xstudio-reference",
    "xstudio-solutions",
    "xstudio-approved-cases",
    "xstudio-rejected-cases",
    "xstudio-reopened-cases",
)

SCOPE_SOURCES: dict[str, tuple[str, ...]] = {
    "trusted": ("xstudio-knowledge", "xstudio-reference", "xstudio-solutions"),
    "knowledge": ("xstudio-knowledge", "xstudio-reference"),
    "reference": ("xstudio-reference",),
    "solutions": ("xstudio-solutions",),
    "cases": ("xstudio-approved-cases", "xstudio-rejected-cases", "xstudio-reopened-cases"),
    "approved_cases": ("xstudio-approved-cases",),
    "rejected_cases": ("xstudio-rejected-cases",),
    "reopened_cases": ("xstudio-reopened-cases",),
}


def gbrain_home(value: str | None = None) -> Path:
    raw = value or os.environ.get("XSTUDIO_GBRAIN_HOME", "").strip()
    return Path(raw).expanduser() if raw else DEFAULT_GBRAIN_HOME


def binary() -> str:
    return os.environ.get("XSTUDIO_GBRAIN_BIN", "gbrain").strip() or "gbrain"


def available() -> bool:
    return shutil.which(binary()) is not None


def run(args: list[str], *, timeout: int = DEFAULT_TIMEOUT) -> tuple[int, str, str]:
    env = os.environ.copy()
    env["GBRAIN_HOME"] = str(gbrain_home())
    try:
        proc = subprocess.run(
            [binary(), *args],
            capture_output=True,
            text=True,
            timeout=timeout,
            env=env,
        )
    except FileNotFoundError:
        return 127, "", "gbrain not found"
    except subprocess.TimeoutExpired:
        return 124, "", "gbrain command timed out"
    return proc.returncode, proc.stdout or "", proc.stderr or ""


def sources_for_scope(scope: str) -> tuple[str, ...]:
    try:
        return SCOPE_SOURCES[scope]
    except KeyError as exc:
        raise ValueError(f"unknown scope: {scope}") from exc


def search(query: str, *, scope: str = "trusted", limit: int = 5) -> dict[str, Any]:
    """Source-scoped lexical prefetch for the legacy dispatcher path."""
    if scope not in SCOPE_SOURCES:
        return {
            "ok": False,
            "error": f"unknown scope: {scope}",
            "retry_same_call": False,
            "backend": "gbrain",
        }
    sources = sources_for_scope(scope)
    rc, out, err = run([
        "search",
        query,
        "--source", ",".join(sources),
        "--limit", str(max(1, min(10, int(limit)))),
        "--json",
    ])
    if rc != 0:
        return {
            "ok": False,
            "error": (err or out).strip()[-1000:] or f"gbrain search exited {rc}",
            "retry_same_call": False,
            "backend": "gbrain",
            "scope": scope,
            "source_ids": list(sources),
        }
    try:
        payload = json.loads(out or "null")
    except json.JSONDecodeError:
        return {
            "ok": False,
            "error": "gbrain returned non-JSON output",
            "retry_same_call": False,
            "backend": "gbrain",
            "scope": scope,
            "source_ids": list(sources),
        }
    return {
        "ok": True,
        "backend": "gbrain",
        "scope": scope,
        "source_ids": list(sources),
        "results": payload,
    }
