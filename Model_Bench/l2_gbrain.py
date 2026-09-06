#!/usr/bin/env python3
"""Small harness-owned adapter around Chitragupta's isolated GBrain.

GBrain is derivative retrieval state, never Helpdesk lifecycle authority. Only
reviewed/canonical material is indexed automatically; historical cases remain
explicitly labelled analogies. Raw sessions and unreviewed candidates are kept
out of the model-facing retrieval plane entirely.
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
DEFAULT_KNOWLEDGE = Path("/mnt/c/Users/Admin/Documents/Office/AIHelpdesk/Knowledge")
DEFAULT_REFERENCE = Path("/mnt/c/Users/Admin/Documents/Office/AIHelpdesk/Reference Documents")
DEFAULT_TIMEOUT = max(10, int(os.environ.get("L2_GBRAIN_TIMEOUT_SECONDS", "60")))

VAULT_SOURCE_DIRS: dict[str, str] = {
    "l2-facts": "facts",
    "l2-solutions": "solutions/approved",
    "l2-approved-cases": "cases/approved",
    "l2-rejected-cases": "cases/rejected",
    "l2-reopened-cases": "cases/reopened",
}
SOURCE_IDS: tuple[str, ...] = ("l2-knowledge", "l2-reference", *VAULT_SOURCE_DIRS)

SCOPE_SOURCES: dict[str, tuple[str, ...]] = {
    "trusted": ("l2-knowledge", "l2-reference", "l2-facts", "l2-solutions"),
    "knowledge": ("l2-knowledge", "l2-reference"),
    "reference": ("l2-reference",),
    "facts": ("l2-facts",),
    "solutions": ("l2-solutions",),
    "cases": ("l2-approved-cases", "l2-rejected-cases", "l2-reopened-cases"),
    "approved_cases": ("l2-approved-cases",),
    "rejected_cases": ("l2-rejected-cases",),
    "reopened_cases": ("l2-reopened-cases",),
}


def vault_path(value: str | None = None) -> Path:
    raw = value or os.environ.get("CHITRAGUPTA_L2_LEARNING_VAULT", "").strip()
    return Path(raw).expanduser() if raw else DEFAULT_VAULT


def gbrain_home(value: str | None = None) -> Path:
    raw = value or os.environ.get("CHITRAGUPTA_GBRAIN_HOME", "").strip()
    return Path(raw).expanduser() if raw else DEFAULT_GBRAIN_HOME


def _repo_subdir(value: str | None, env_name: str, folder: str, fallback: Path) -> Path | None:
    raw = value or os.environ.get(env_name, "").strip()
    if raw:
        return Path(raw).expanduser()
    for candidate in (
        Path.cwd() / folder,
        Path(__file__).resolve().parent.parent / folder,
        fallback,
    ):
        if candidate.is_dir():
            return candidate
    return None


def knowledge_path(value: str | None = None) -> Path | None:
    return _repo_subdir(value, "CHITRAGUPTA_KNOWLEDGE_PATH", "Knowledge", DEFAULT_KNOWLEDGE)


def reference_path(value: str | None = None) -> Path | None:
    return _repo_subdir(value, "CHITRAGUPTA_REFERENCE_PATH", "Reference Documents", DEFAULT_REFERENCE)


def binary() -> str:
    return os.environ.get("CHITRAGUPTA_GBRAIN_BIN", "gbrain").strip() or "gbrain"


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
        return 127, "", "gbrain not found; install the pinned Chitragupta GBrain prerequisite"
    except subprocess.TimeoutExpired:
        return 124, "", "gbrain command timed out"
    return proc.returncode, proc.stdout or "", proc.stderr or ""


def sources_for_scope(scope: str) -> tuple[str, ...]:
    try:
        return SCOPE_SOURCES[scope]
    except KeyError as exc:
        raise ValueError(f"unknown scope: {scope}") from exc


def search(query: str, *, scope: str = "trusted", limit: int = 5) -> dict[str, Any]:
    """Run source-scoped retrieval only. This adapter never calls `gbrain query`."""
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
        "deterministic_retrieval": True,
    }
