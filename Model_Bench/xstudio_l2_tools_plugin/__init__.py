"""Chitragupta's single Hermes domain-tool plugin.

Hermes owns the agent harness. This plugin exposes:
- xstudio_l2: typed XStudio/Helpdesk evidence and ledger operations;
- l2_recall: read-only, trust-scoped GBrain retrieval.

Identity-sensitive XStudio calls are bound to the current Kanban task before
they cross the Windows/pyodbc bridge.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import threading
from pathlib import Path
from typing import Any

WINDOWS_PYTHON = "/mnt/c/Python314/python.exe"
BRIDGE_WIN = r"C:\Users\Admin\Documents\Office\AIHelpdesk\Model_Bench\xstudio_l2_tool_bridge.py"
BRIDGE_TIMEOUT_SECONDS = max(10, int(os.environ.get("L2_BRIDGE_TIMEOUT_SECONDS", "90")))

XSTUDIO_TOOL = "xstudio_l2"
XSTUDIO_TOOLSET = "xstudio_l2"
RECALL_TOOL = "l2_recall"
RECALL_TOOLSET = "l2_learning"

_TASK_ID_RE = re.compile(r"\bt_[0-9a-f]{6,}\b", re.IGNORECASE)
_RUN_OPS = {"select", "query", "read_procedure", "get_run_actions", "save_ledger"}
_TICKET_OPS = {"get_ticket_context"}
_CONTEXT_LOCK = threading.Lock()
_CONTEXT_CACHE: dict[str, dict[str, str]] = {}

for _helper_dir in (
    Path(__file__).resolve().parent.parent,
    Path.home() / ".hermes" / "profiles" / "l2-investigator" / "scripts",
):
    if str(_helper_dir) not in sys.path:
        sys.path.insert(0, str(_helper_dir))

from l2_gbrain import SCOPE_SOURCES, available as gbrain_available, search as gbrain_search  # noqa: E402


def _kanban_task_id(task_id: str | None = None) -> str:
    for candidate in (task_id or "", *map(str, sys.argv)):
        if match := _TASK_ID_RE.search(candidate):
            return match.group(0)
    return ""


def _task_context(task_id: str | None = None) -> dict[str, str]:
    actual = _kanban_task_id(task_id)
    if not actual:
        return {}
    with _CONTEXT_LOCK:
        if actual in _CONTEXT_CACHE:
            return dict(_CONTEXT_CACHE[actual])
    try:
        proc = subprocess.run(
            ["hermes", "kanban", "show", actual, "--json"],
            capture_output=True,
            text=True,
            timeout=8,
        )
        if proc.returncode:
            return {}
        payload = json.loads(proc.stdout or "{}")
        task = payload.get("task") if isinstance(payload.get("task"), dict) else payload
    except Exception:
        return {}

    context: dict[str, str] = {}
    for raw in str(task.get("body") or "").splitlines():
        if ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        key, value = key.strip().lower(), value.strip()
        if key in {"run_id", "ticket_id"} and value:
            context[key] = value
    if context.get("run_id") and context.get("ticket_id"):
        with _CONTEXT_LOCK:
            _CONTEXT_CACHE[actual] = dict(context)
    return context


def _bind_identity(params: dict[str, Any], task_id: str | None) -> dict[str, Any]:
    operation = str(params.get("operation") or "")
    required = {
        "run_id": operation in _RUN_OPS,
        "ticket_id": operation in _TICKET_OPS,
    }
    if not any(required.values()):
        return dict(params)

    context = _task_context(task_id)
    bound = dict(params)
    for key, needed in required.items():
        if not needed:
            continue
        actual = context.get(key)
        if not actual:
            raise RuntimeError(f"current Kanban task {key} could not be resolved")
        supplied = str(bound.get(key) or "").strip()
        if supplied and supplied != actual:
            raise ValueError(f"{key} belongs to a different L2 task")
        bound[key] = actual
    return bound


def _invoke_bridge(params: dict[str, Any]) -> str:
    try:
        proc = subprocess.run(
            [WINDOWS_PYTHON, BRIDGE_WIN],
            input=json.dumps(params, separators=(",", ":"), default=str),
            capture_output=True,
            text=True,
            timeout=BRIDGE_TIMEOUT_SECONDS,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return json.dumps({
            "ok": False,
            "operation": params.get("operation"),
            "error": f"bridge transport failed: {type(exc).__name__}: {exc}",
        })
    text = (proc.stdout or "").strip()
    if not text:
        return json.dumps({
            "ok": False,
            "operation": params.get("operation"),
            "error": (proc.stderr or f"bridge exited {proc.returncode}").strip()[:1000],
        })
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return json.dumps({
            "ok": False,
            "operation": params.get("operation"),
            "error": "bridge returned non-JSON output",
        })
    if proc.returncode and isinstance(data, dict) and data.get("ok", True):
        data = {
            "ok": False,
            "operation": params.get("operation"),
            "error": f"bridge exited {proc.returncode}",
            "detail": data,
        }
    return json.dumps(data, ensure_ascii=False, default=str)


def _xstudio(params: dict[str, Any], task_id: str = "", **_: Any) -> str:
    try:
        return _invoke_bridge(_bind_identity(params, task_id))
    except (RuntimeError, ValueError) as exc:
        return json.dumps({
            "ok": False,
            "operation": params.get("operation"),
            "error": f"L2 identity guard: {exc}",
        })


def _recall(params: dict[str, Any], **_: Any) -> str:
    query = " ".join(str(params.get("query") or "").split())
    scope = str(params.get("scope") or "trusted")
    if not query:
        return json.dumps({"ok": False, "error": "query is required"})
    if scope not in SCOPE_SOURCES:
        return json.dumps({"ok": False, "error": f"unknown scope: {scope}"})
    try:
        limit = max(1, min(10, int(params.get("limit") or 5)))
    except (TypeError, ValueError):
        limit = 5
    if not gbrain_available():
        return json.dumps({"ok": False, "error": "gbrain is unavailable"})
    result = gbrain_search(query[:600], scope=scope, limit=limit)
    if not result.get("ok"):
        return json.dumps(result, ensure_ascii=False, default=str)
    historical = scope == "cases" or scope.endswith("_cases")
    return json.dumps({
        "ok": True,
        "backend": "gbrain",
        "scope": scope,
        "source_ids": result.get("source_ids") or [],
        "warning": (
            "Historical outcomes are leads/counterexamples, not proof."
            if historical
            else "Reusable reference only; verify current-ticket claims live."
        ),
        "results": result.get("results") or [],
        "live_verification_required": True,
    }, ensure_ascii=False, default=str)


_XSTUDIO_SCHEMA = {
    "name": XSTUDIO_TOOL,
    "description": "Typed XStudio/Helpdesk L2 evidence interface. Use current live evidence for ticket claims.",
    "parameters": {
        "type": "object",
        "properties": {
            "operation": {"type": "string", "enum": [
                "select", "query", "suggest_tables", "find_objects",
                "get_definition", "validate_identifiers", "read_procedure",
                "get_ticket_context", "get_run_actions", "save_ledger",
            ]},
            "database": {"type": "string", "enum": [
                "XStudio_Helpdesk", "XStudio_Xbatch", "XStudio_Configuration_Xbatch",
            ]},
            "run_id": {"type": "string"},
            "ticket_id": {"type": "string"},
            "table": {"type": "string"},
            "columns": {"type": "array", "items": {"type": "string"}},
            "where": {"type": "string"},
            "order_by": {"type": "string"},
            "top": {"type": "integer", "minimum": 1, "maximum": 100},
            "sql": {"type": "string"},
            "search": {"type": "string"},
            "object_type": {"type": "string", "enum": ["TABLE", "VIEW", "PROCEDURE", "TRIGGER"]},
            "schema": {"type": "string"},
            "object_name": {"type": "string"},
            "identifiers": {"type": "array", "items": {"type": "string"}},
            "procedure": {"type": "string"},
            "parameters": {"type": "object"},
            "ledger": {"type": "object"},
        },
        "required": ["operation"],
        "additionalProperties": False,
    },
}

_RECALL_SCHEMA = {
    "name": RECALL_TOOL,
    "description": "Read-only trust-scoped GBrain recall. Live ticket claims still require xstudio_l2 evidence.",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {"type": "string"},
            "scope": {"type": "string", "enum": list(SCOPE_SOURCES)},
            "limit": {"type": "integer", "minimum": 1, "maximum": 10},
        },
        "required": ["query"],
        "additionalProperties": False,
    },
}


def register(ctx: Any) -> None:
    ctx.register_tool(
        name=XSTUDIO_TOOL,
        toolset=XSTUDIO_TOOLSET,
        schema=_XSTUDIO_SCHEMA,
        handler=_xstudio,
        description="Typed guarded XStudio L2 evidence interface.",
    )
    ctx.register_tool(
        name=RECALL_TOOL,
        toolset=RECALL_TOOLSET,
        schema=_RECALL_SCHEMA,
        handler=_recall,
        description="Read-only trust-scoped GBrain recall.",
    )
