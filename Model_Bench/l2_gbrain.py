#!/usr/bin/env python3
"""Harness-owned GBrain adapter for Chitragupta's L2 retrieval plane.

GBrain is disposable derivative retrieval state. It never owns Helpdesk
lifecycle state, never writes XStudio, and is never exposed to L2 workers as a
raw memory API.

Every trust lane is a separate non-federated source. Every read names its
source(s) explicitly. Chitragupta also gives this adapter a dedicated GBrain
home so unrelated/default user brains cannot leak into L2 retrieval.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path
from typing import Any

DEFAULT_VAULT = Path.home() / ".hermes" / "l2-learning"
DEFAULT_GBRAIN_HOME = Path.home() / ".hermes" / "l2-gbrain"
DEFAULT_TIMEOUT = max(10, int(os.environ.get("L2_GBRAIN_TIMEOUT_SECONDS", "60")))

SOURCE_DIRS: dict[str, str] = {
    "l2-knowledge": "knowledge",
    "l2-facts": "facts",
    "l2-solutions": "solutions/approved",
    "l2-approved-cases": "cases/approved",
    "l2-rejected-cases": "cases/rejected",
    "l2-reopened-cases": "cases/reopened",
    "l2-sessions": "sessions",
    "l2-candidates": "candidates",
}

SCOPE_SOURCES: dict[str, tuple[str, ...]] = {
    "trusted": ("l2-knowledge", "l2-facts", "l2-solutions"),
    "knowledge": ("l2-knowledge",),
    "facts": ("l2-facts",),
    "solutions": ("l2-solutions",),
    "cases": ("l2-approved-cases", "l2-rejected-cases", "l2-reopened-cases"),
    "approved_cases": ("l2-approved-cases",),
    "rejected_cases": ("l2-rejected-cases",),
    "reopened_cases": ("l2-reopened-cases",),
    "sessions": ("l2-sessions",),
    "candidates": ("l2-candidates",),
    "all": tuple(SOURCE_DIRS),
}

SUPPORTED_SEARCH_MODES = frozenset({"hybrid", "deep", "fts", "vector"})
# Automatic harness retrieval may use trusted guidance or explicitly-labelled
# historical cases, but must never silently widen into raw sessions/candidates
# or the mixed all-source scope.
AUTOMATIC_FORBIDDEN_SCOPES = frozenset({"all", "sessions", "candidates"})


def vault_path(value: str | None = None) -> Path:
    if value:
        return Path(value).expanduser()
    raw = os.environ.get("CHITRAGUPTA_L2_LEARNING_VAULT", "").strip()
    return Path(raw).expanduser() if raw else DEFAULT_VAULT


def gbrain_home(value: str | None = None) -> Path:
    if value:
        return Path(value).expanduser()
    raw = os.environ.get("CHITRAGUPTA_GBRAIN_HOME", "").strip()
    return Path(raw).expanduser() if raw else DEFAULT_GBRAIN_HOME


def binary() -> str:
    return os.environ.get("CHITRAGUPTA_GBRAIN_BIN", "gbrain").strip() or "gbrain"


def available() -> bool:
    return shutil.which(binary()) is not None


def run(args: list[str], *, timeout: int = DEFAULT_TIMEOUT,
        cwd: Path | None = None) -> tuple[int, str, str]:
    """Run one GBrain command inside the dedicated Chitragupta brain home."""
    env = os.environ.copy()
    env["GBRAIN_HOME"] = str(gbrain_home())
    try:
        proc = subprocess.run(
            [binary(), *args],
            cwd=str(cwd) if cwd else None,
            capture_output=True,
            text=True,
            timeout=timeout,
            env=env,
        )
    except FileNotFoundError:
        return 127, "", "gbrain not found; run Model_Bench/install_l2_learning_prereqs.sh"
    except subprocess.TimeoutExpired:
        return 124, "", "gbrain command timed out"
    return proc.returncode, proc.stdout or "", proc.stderr or ""


def parse_json(text: str) -> Any:
    return json.loads(text or "null")


def sources_for_scope(scope: str) -> tuple[str, ...]:
    if scope not in SCOPE_SOURCES:
        raise ValueError(f"unknown scope: {scope}")
    return SCOPE_SOURCES[scope]


def automatic_scope_allowed(scope: str) -> bool:
    return scope in SCOPE_SOURCES and scope not in AUTOMATIC_FORBIDDEN_SCOPES


def search(query: str, *, scope: str = "trusted", mode: str = "hybrid",
           limit: int = 5, automatic: bool = False) -> dict[str, Any]:
    """Run one explicit, source-scoped GBrain retrieval-only search.

    ``gbrain query`` is intentionally never invoked. Legacy callers may request
    ``deep``, ``fts`` or ``vector`` during migration, but all are normalized to
    the same retrieval-only hybrid ``search`` path.

    When ``automatic=True`` the adapter additionally forbids mixed/raw scopes
    (`all`, `sessions`, `candidates`). Explicit supplemental recall may still
    request those scopes with ``automatic=False`` and must preserve their trust
    labels upstream.
    """
    if mode not in SUPPORTED_SEARCH_MODES:
        return {
            "ok": False,
            "error": f"unknown search mode: {mode}",
            "retry_same_call": False,
            "backend": "gbrain",
        }
    if scope not in SCOPE_SOURCES:
        return {
            "ok": False,
            "error": f"unknown scope: {scope}",
            "retry_same_call": False,
            "backend": "gbrain",
        }
    if automatic and not automatic_scope_allowed(scope):
        return {
            "ok": False,
            "error": f"scope {scope!r} is forbidden for automatic harness retrieval",
            "retry_same_call": False,
            "backend": "gbrain",
            "scope": scope,
        }

    sources = sources_for_scope(scope)
    requested = mode
    effective = "hybrid"
    source_arg = ",".join(sources)
    rc, out, err = run([
        "search",
        query,
        "--source", source_arg,
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
        payload = parse_json(out)
    except Exception:
        return {
            "ok": False,
            "error": "gbrain returned non-JSON output",
            "detail": out.strip()[:1000],
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
        "requested_mode": requested,
        "effective_mode": effective,
        "automatic": automatic,
        "results": payload,
        "deterministic_retrieval": True,
    }
