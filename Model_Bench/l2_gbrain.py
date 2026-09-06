#!/usr/bin/env python3
"""Small harness-owned GBrain adapter for Chitragupta's learning plane.

GBrain is a derivative retrieval/index substrate. This module never writes to
XStudio/Helpdesk and never exposes raw GBrain writes to an L2 worker.

Every Chitragupta trust lane is a separate non-federated GBrain source. Reads
must name their source(s) explicitly so an unqualified brain search cannot
silently cross trust boundaries.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path
from typing import Any

DEFAULT_VAULT = Path.home() / ".hermes" / "l2-learning"
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


def vault_path(value: str | None = None) -> Path:
    if value:
        return Path(value).expanduser()
    raw = os.environ.get("CHITRAGUPTA_L2_LEARNING_VAULT", "").strip()
    return Path(raw).expanduser() if raw else DEFAULT_VAULT


def binary() -> str:
    return os.environ.get("CHITRAGUPTA_GBRAIN_BIN", "gbrain").strip() or "gbrain"


def available() -> bool:
    return shutil.which(binary()) is not None


def run(args: list[str], *, timeout: int = DEFAULT_TIMEOUT,
        cwd: Path | None = None) -> tuple[int, str, str]:
    try:
        proc = subprocess.run(
            [binary(), *args],
            cwd=str(cwd) if cwd else None,
            capture_output=True,
            text=True,
            timeout=timeout,
            env=os.environ.copy(),
        )
    except FileNotFoundError:
        return 127, "", "gbrain not found; run Model_Bench/install_l2_learning_prereqs.sh"
    except subprocess.TimeoutExpired:
        return 124, "", "gbrain command timed out"
    return proc.returncode, proc.stdout or "", proc.stderr or ""


def parse_json(text: str) -> Any:
    value = json.loads(text or "null")
    return value


def sources_for_scope(scope: str) -> tuple[str, ...]:
    if scope not in SCOPE_SOURCES:
        raise ValueError(f"unknown scope: {scope}")
    return SCOPE_SOURCES[scope]


def search(query: str, *, scope: str = "trusted", mode: str = "hybrid",
           limit: int = 5) -> dict[str, Any]:
    """Run one explicitly source-scoped GBrain retrieval.

    `gbrain search` is already cheap hybrid retrieval (keyword + vector + RRF)
    without LLM query expansion. `deep` opts into `gbrain query`. Legacy
    `fts` maps to the cheap search lane; legacy `vector` maps to deep retrieval
    because GBrain does not expose a vector-only public query contract here.
    """
    sources = sources_for_scope(scope)
    requested = mode
    effective = "deep" if mode in {"deep", "vector"} else "hybrid"
    command = "query" if effective == "deep" else "search"
    source_arg = ",".join(sources)
    rc, out, err = run([
        command,
        query,
        "--source", source_arg,
        "--limit", str(max(1, min(10, int(limit)))),
        "--json",
    ])
    if rc != 0:
        return {
            "ok": False,
            "error": (err or out).strip()[-1000:] or f"gbrain {command} exited {rc}",
            "retry_same_call": False,
            "backend": "gbrain",
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
        }
    return {
        "ok": True,
        "backend": "gbrain",
        "scope": scope,
        "source_ids": list(sources),
        "requested_mode": requested,
        "effective_mode": effective,
        "results": payload,
    }
