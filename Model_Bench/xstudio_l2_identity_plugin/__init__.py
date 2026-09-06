"""Cross-cutting identity guard for Chitragupta L2 tools.

The model may reason about *what* to read or plan, but it must not choose *which
L2 run/ticket* receives evidence, ledger writes, or action-plan provenance.

Hermes pre_tool_call hooks support {"action":"modify","args":{...}}; this
plugin resolves the real Kanban card from harness argv, reads its run_id and
ticket_id once, and shallow-merges those identifiers into identity-sensitive
tool calls. Conflicting model-supplied identifiers are blocked.

This is deliberately a separate cross-cutting plugin rather than duplicate
identity code in xstudio_l2, l2_learning, and l2_actions.
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

PLUGIN_NAME = "xstudio-l2-identity"
_TASK_ID_RE = re.compile(r"\bt_[0-9a-f]{6,}\b", re.IGNORECASE)
_PLAN_ID_RE = re.compile(r"^[a-f0-9]{32}$")
_CONTEXT_KEYS = {"run_id", "ticket_id", "ticket_no", "pipeline_stage", "review_cycle"}

_XSTUDIO_RUN_OPS = {"select", "query", "read_procedure", "get_run_actions", "save_ledger"}
_XSTUDIO_TICKET_OPS = {"get_ticket_context"}
_ACTION_BOUND_OPS = {"plan", "plans"}

_lock = threading.Lock()
_context_cache: dict[str, dict[str, str]] = {}


def _actual_task_id(task_id: str | None = None) -> str:
    for candidate in (task_id or "", *[str(x) for x in sys.argv]):
        match = _TASK_ID_RE.search(candidate)
        if match:
            return match.group(0)
    return ""


def _parse_task_payload(payload: Any, task_id: str) -> dict[str, str]:
    if not isinstance(payload, dict):
        return {}
    task = payload.get("task") if isinstance(payload.get("task"), dict) else payload
    body = str(task.get("body") or "")
    found: dict[str, str] = {"kanban_task_id": task_id}
    for raw in body.splitlines():
        if ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        key = key.strip().lower()
        value = value.strip()
        if key in _CONTEXT_KEYS and value:
            found[key] = value
    return found


def _resolve_context(task_id: str | None = None) -> dict[str, str]:
    actual = _actual_task_id(task_id)
    if not actual:
        return {}
    with _lock:
        cached = _context_cache.get(actual)
        if cached:
            return dict(cached)
    try:
        proc = subprocess.run(
            ["hermes", "kanban", "show", actual, "--json"],
            capture_output=True,
            text=True,
            timeout=8,
        )
        if proc.returncode != 0:
            return {}
        context = _parse_task_payload(json.loads(proc.stdout or "{}"), actual)
    except Exception:
        return {}
    if context.get("run_id") and context.get("ticket_id"):
        with _lock:
            _context_cache[actual] = dict(context)
    return context


def _conflict(args: dict[str, Any], context: dict[str, str], key: str) -> str | None:
    supplied = str(args.get(key) or "").strip()
    bound = str(context.get(key) or "").strip()
    if supplied and bound and supplied != bound:
        return f"model supplied {key}={supplied!r}, but current Kanban task is bound to {bound!r}"
    return None


def _identity_modification(args: dict[str, Any], task_id: str, *, need_run: bool, need_ticket: bool) -> dict[str, Any]:
    context = _resolve_context(task_id)
    if need_run and not context.get("run_id"):
        raise RuntimeError("current Kanban task run_id could not be resolved by the identity guard")
    if need_ticket and not context.get("ticket_id"):
        raise RuntimeError("current Kanban task ticket_id could not be resolved by the identity guard")
    for key in ("run_id", "ticket_id"):
        problem = _conflict(args, context, key)
        if problem:
            raise ValueError(problem)
    modified: dict[str, Any] = {}
    if need_run:
        modified["run_id"] = context["run_id"]
    if need_ticket:
        modified["ticket_id"] = context["ticket_id"]
    return modified


def _plan_matches_current_identity(args: dict[str, Any], task_id: str) -> str | None:
    plan_id = str(args.get("plan_id") or "").strip()
    if not _PLAN_ID_RE.match(plan_id):
        return None  # l2_actions will report the normal plan-id validation error.
    context = _resolve_context(task_id)
    if not context.get("run_id") or not context.get("ticket_id"):
        return "current Kanban task identity could not be resolved"
    vault = Path(os.environ.get("CHITRAGUPTA_L2_LEARNING_VAULT") or (Path.home() / ".hermes" / "l2-learning"))
    path = vault / "actions" / "plans" / f"{plan_id}.json"
    if not path.exists():
        return None  # planner owns not-found reporting.
    try:
        plan = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None
    plan_context = plan.get("context") if isinstance(plan.get("context"), dict) else {}
    if str(plan_context.get("run_id") or "") != context["run_id"]:
        return "requested action plan belongs to a different L2 run"
    if str(plan_context.get("ticket_id") or "") != context["ticket_id"]:
        return "requested action plan belongs to a different Helpdesk ticket"
    return None


def _pre_tool_call(tool_name: str, args: dict[str, Any] | None = None,
                   task_id: str = "", **kwargs: Any) -> dict[str, Any] | None:
    del kwargs
    args = args or {}
    operation = str(args.get("operation") or "")
    try:
        if tool_name == "xstudio_l2":
            need_run = operation in _XSTUDIO_RUN_OPS
            need_ticket = operation in _XSTUDIO_TICKET_OPS
            if not need_run and not need_ticket:
                return None
            modified = _identity_modification(args, task_id, need_run=need_run, need_ticket=need_ticket)
            return {"action": "modify", "args": modified}

        if tool_name == "l2_action":
            if operation in _ACTION_BOUND_OPS:
                modified = _identity_modification(args, task_id, need_run=True, need_ticket=True)
                return {"action": "modify", "args": modified}
            if operation == "validate_plan":
                problem = _plan_matches_current_identity(args, task_id)
                if problem:
                    return {"action": "block", "message": f"L2 identity guard: {problem}."}
        return None
    except (RuntimeError, ValueError) as exc:
        return {
            "action": "block",
            "message": (
                f"L2 identity guard: {exc}. Run/ticket identity is harness-owned; "
                "do not retry with another identifier or use a shell workaround."
            ),
        }


def register(ctx: Any) -> None:
    ctx.register_hook("pre_tool_call", _pre_tool_call)
