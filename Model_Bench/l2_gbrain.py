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
# The real, already-populated Chitragupta brain on this deployment (415 pages
# synced from the repo's own Knowledge/deploy/skills tree: SP catalog, runtime
# DB design, XBatch relationship atlas, vendor per-heat docs). Still a
# dedicated project brain, not the operator's generic personal one -- just not
# the not-yet-existing donor-proposed "l2-gbrain" name. CHITRAGUPTA_GBRAIN_HOME
# overrides this for local testing.
DEFAULT_GBRAIN_HOME = Path.home() / ".hermes" / "xstudio-gbrain"
DEFAULT_TIMEOUT = max(10, int(os.environ.get("L2_GBRAIN_TIMEOUT_SECONDS", "60")))

# bun-installed CLIs (gbrain among them) are not reliably on PATH for a
# systemd --user gateway service, whose Environment=PATH is a snapshot taken
# at profile-install time. Mirrors l2_pipeline_runtime._hermes_executable()'s
# fallback-path search rather than requiring a service-unit edit per machine.
_BINARY_FALLBACKS = (
    Path.home() / ".bun" / "bin" / "gbrain",
    Path.home() / ".local" / "bin" / "gbrain",
)

# Real, already-populated source on this deployment: a full-repo Knowledge/
# deploy/skills sync (SP catalog, runtime DB design, XBatch relationship
# atlas, vendor per-heat docs) registered directly against the repo, not a
# vault subdirectory -- so it is referenced in SCOPE_SOURCES but deliberately
# left out of SOURCE_DIRS, which sync_l2_gbrain.py uses only to provision and
# validate vault-relative learning lanes.
XSTUDIO_KNOWLEDGE_SOURCE = "xstudio-knowledge"

SOURCE_DIRS: dict[str, str] = {
    # Vault-relative learning lanes that sync_l2_gbrain.py provisions and
    # registers as non-federated sources. Not yet populated on this brain --
    # the learning cycle that would mine real investigation/review outcomes
    # into them doesn't exist yet. search() skips any source gbrain reports
    # as unknown_source rather than failing, so referencing them in scope now
    # is forward-compatible, not a hard dependency.
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
    "trusted": (XSTUDIO_KNOWLEDGE_SOURCE, "l2-knowledge", "l2-facts", "l2-solutions"),
    "knowledge": (XSTUDIO_KNOWLEDGE_SOURCE, "l2-knowledge"),
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
    override = os.environ.get("CHITRAGUPTA_GBRAIN_BIN", "").strip()
    if override:
        return override
    on_path = shutil.which("gbrain")
    if on_path:
        return on_path
    for fallback in _BINARY_FALLBACKS:
        if fallback.exists() and os.access(fallback, os.X_OK):
            return str(fallback)
    return "gbrain"


def available() -> bool:
    return shutil.which(binary()) is not None


def _env() -> dict[str, str]:
    env = os.environ.copy()
    env["GBRAIN_HOME"] = str(gbrain_home())
    # gbrain's own shebang is `env bun`; a systemd --user gateway's PATH is a
    # snapshot from profile-install time and does not reliably carry bun's
    # install directory. Make it resolvable without requiring a service-unit
    # edit per machine, same rationale as the binary() fallback above.
    bun_bin = str(Path.home() / ".bun" / "bin")
    if bun_bin not in env.get("PATH", "").split(os.pathsep):
        env["PATH"] = bun_bin + os.pathsep + env.get("PATH", "")
    return env


class Brain:
    """One `gbrain serve` (MCP stdio) session for many fast calls: the world walk reads pages and
    links step by step, where a CLI process per call (~0.7 s each) would dominate."""

    def __init__(self) -> None:
        self.proc = subprocess.Popen([binary(), "serve"], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                     stderr=subprocess.DEVNULL, text=True, env=_env(), bufsize=1)
        self.next_id = 0
        self.request("initialize", {"protocolVersion": "2024-11-05", "capabilities": {},
                                    "clientInfo": {"name": "chitragupta", "version": "1"}})
        self.proc.stdin.write(json.dumps({"jsonrpc": "2.0", "method": "notifications/initialized"}) + "\n")

    def request(self, method: str, params: dict) -> dict:
        self.next_id += 1
        self.proc.stdin.write(json.dumps({"jsonrpc": "2.0", "id": self.next_id, "method": method, "params": params}) + "\n")
        while True:
            line = self.proc.stdout.readline()
            if not line:
                raise RuntimeError("gbrain serve closed the connection")
            msg = json.loads(line)
            if msg.get("id") == self.next_id:
                if "error" in msg:
                    raise RuntimeError(msg["error"])
                return msg["result"]

    def call(self, tool: str, **args) -> Any:
        result = self.request("tools/call", {"name": tool, "arguments": args})
        text = "".join(c.get("text", "") for c in result.get("content", []))
        if result.get("isError"):
            raise RuntimeError(text[:300])
        try:
            return json.loads(text)
        except ValueError:
            return {"text": text}

    def all_pages(self, page_size: int = 100) -> list[dict]:
        """list_pages caps each call, so page through with offset."""
        pages, offset = [], 0
        while True:
            listed = self.call("list_pages", limit=page_size, offset=offset)
            batch = listed if isinstance(listed, list) else listed.get("pages", [])
            pages += batch
            if len(batch) < page_size:
                return pages
            offset += page_size


def run(args: list[str], *, timeout: int = DEFAULT_TIMEOUT,
        cwd: Path | None = None) -> tuple[int, str, str]:
    """Run one GBrain command inside the dedicated Chitragupta brain home."""
    env = _env()
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
    bounded_limit = max(1, min(10, int(limit)))

    # The installed gbrain CLI scopes one `search` call to exactly one
    # --source-id; there is no combined multi-source query syntax. Query each
    # source in the scope separately and merge. A scope lane that has not
    # been populated yet (e.g. l2-facts before the learning cycle exists) is
    # reported by gbrain as unknown_source -- skip that lane rather than
    # failing the whole call, but only if at least one lane in the scope
    # actually exists and answered.
    queried: list[str] = []
    missing: list[str] = []
    merged_rows: list[dict[str, Any]] = []
    last_hard_error: str | None = None
    for source_id in sources:
        rc, out, err = run([
            "search", query,
            "--source-id", source_id,
            "--limit", str(bounded_limit),
            "--json",
        ])
        if rc != 0:
            message = (err or out).strip()
            if "unknown_source" in message or "does not exist" in message:
                missing.append(source_id)
                continue
            last_hard_error = message[-1000:] or f"gbrain search exited {rc}"
            continue
        try:
            payload = parse_json(out)
        except Exception:
            last_hard_error = "gbrain returned non-JSON output"
            continue
        queried.append(source_id)
        rows = payload if isinstance(payload, list) else payload.get("results") or []
        for row in rows:
            if isinstance(row, dict):
                merged_rows.append(row)

    if not queried and not automatic and not last_hard_error and scope != "knowledge":
        # Explicit recall into a lane nobody has populated yet (no curated cases/facts/solutions)
        # answered with an error, and the worker spent a turn retrying scope=knowledge (7x in 2h,
        # 2026-09-23). Answer from the populated reference lane in the same call and say so.
        fallback = search(query, scope="knowledge", mode=mode, limit=limit, automatic=False)
        if fallback.get("ok"):
            return {**fallback, "requested_scope": scope, "fallback_scope": "knowledge",
                    "note": f"No {scope} are recorded yet; these results come from the reference knowledge."}
    if not queried:
        return {
            "ok": False,
            "error": last_hard_error or "no requested source is populated yet",
            "retry_same_call": False,
            "backend": "gbrain",
            "scope": scope,
            "source_ids": list(sources),
            "missing_source_ids": missing,
        }

    merged_rows.sort(key=lambda row: row.get("score") or 0, reverse=True)
    return {
        "ok": True,
        "backend": "gbrain",
        "scope": scope,
        "source_ids": queried,
        "missing_source_ids": missing,
        "requested_mode": requested,
        "effective_mode": effective,
        "automatic": automatic,
        "results": merged_rows[:bounded_limit],
        "deterministic_retrieval": True,
    }
