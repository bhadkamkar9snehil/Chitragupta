"""Typed, guarded XStudio investigation tool for Hermes L2 workers.

Why this exists (Ticket_424 / Ticket_441, 2026-09-05): the deterministic
lifecycle was already working, but the investigator burned 1,026,911 tokens /
27 tool calls / 2 sessions trying to build the SQL *transport* itself. It
malformed the interpreter call as `python3 /mnt/c/Python314/python.exe ...`,
retried the same broken shape with `timeout` wrappers, fell back to
`pip install pyodbc`, hit Tirith's fail-closed dependency scan, and finally
overflowed context. That is an agent-computer-interface defect, not a
lifecycle defect, so it is fixed at the harness boundary rather than taught
through mem0.

The model calls ONE typed tool. This plugin invokes the Windows bridge itself,
so the model never composes Windows/WSL paths, interpreters, pyodbc, or
credentials. The same plugin blocks the retired shell transport, injects the
execution contract ahead of the LLM turn (so pre-migration cards carrying a raw
command recipe cannot steer the worker back), and bounds call count / repeated
identical failures so one bad idea cannot consume the whole context window.
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import threading
from collections import defaultdict
from typing import Any

WINDOWS_PYTHON = "/mnt/c/Python314/python.exe"
BRIDGE_WIN = r"C:\Users\Admin\Documents\Office\AIHelpdesk\Model_Bench\xstudio_l2_tool_bridge.py"
TOOL_NAME = "xstudio_l2"
TOOLSET = "xstudio_l2"

# Bounded so a single session cannot spend the 65.6K context on transport
# flailing. These are deliberately small: a competent investigation needs a
# handful of typed reads, not dozens of shell experiments.
MAX_TOOL_CALLS = max(1, int(os.environ.get("L2_MAX_XSTUDIO_TOOL_CALLS", "14")))
MAX_IDENTICAL_FAILURES = max(1, int(os.environ.get("L2_MAX_IDENTICAL_FAILURES", "2")))
BRIDGE_TIMEOUT_SECONDS = max(10, int(os.environ.get("L2_BRIDGE_TIMEOUT_SECONDS", "90")))

# Matched case-insensitively as substrings of the model's terminal command.
# Every entry here is a *transport* path the harness owns. Benign inspection
# (ls/cat/grep/git/reading docs) is deliberately NOT matched -- including
# `grep -i pyodbc`, which is why pyodbc is matched only as real Python usage.
_BLOCKED_TERMINAL_MARKERS = (
    # the retired orchestrator-as-transport path
    "hermes_orchestrator.py",
    # Windows interpreter reached from WSL (the exact Ticket_424 shape)
    "/mnt/c/python314/python.exe",
    "\\python314\\python.exe",
    "python.exe",
    # alternate SQL transports
    "sqlcmd",
    "bcp ",
    # driver use the harness owns
    "import pyodbc",
    "from pyodbc",
    # dependency / environment mutation
    "pip install",
    "pip3 install",
    "pipx install",
    "uv pip",
    "python -m pip",
    "python3 -m pip",
    "conda install",
    "poetry add",
    "easy_install",
    "apt install",
    "apt-get install",
)

_BLOCK_MESSAGE = (
    "L2 execution guard: database/runtime transport is harness-owned. "
    "Do not invoke Hermes_Orchestrator.py, Windows Python, sqlcmd, pyodbc, pip, "
    "or install packages from terminal -- that path is retired and blocked. "
    "Use the xstudio_l2 typed tool instead (operations: select, query, "
    "suggest_tables, find_objects, get_definition, validate_identifiers, "
    "read_procedure, get_ticket_context, get_run_actions, save_ledger). "
    "Do not retry this command with wrappers, timeouts, or a different shell."
)

_lock = threading.Lock()
_session_calls: dict[str, int] = defaultdict(int)
_session_failures: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))


def _session_key(task_id: str | None = None, **kwargs: Any) -> str:
    return str(kwargs.get("session_id") or kwargs.get("task_id") or task_id or "unknown-session")


def _fingerprint(args: dict[str, Any]) -> str:
    """Identity of a call, so a genuinely different call is never penalised."""
    raw = json.dumps(args or {}, sort_keys=True, separators=(",", ":"), default=str)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _terminal_command(args: dict[str, Any]) -> str:
    parts = [args.get("command"), args.get("cmd"), args.get("input"), args.get("script")]
    if isinstance(args.get("args"), (list, tuple)):
        parts.extend(str(x) for x in args["args"])
    return " ".join(str(p) for p in parts if p).lower()


def _parse_result(result: Any) -> dict[str, Any]:
    if isinstance(result, dict):
        return result
    try:
        value = json.loads(result or "{}")
        return value if isinstance(value, dict) else {"ok": True, "result": value}
    except (json.JSONDecodeError, TypeError):
        return {"ok": False, "error": str(result)[:500]}


def _invoke_bridge(params: dict[str, Any]) -> str:
    """Run the Windows bridge directly.

    This is trusted harness code, not a model-driven terminal call, so it is the
    one place the Windows interpreter is named. Note the argv shape: the Windows
    interpreter is argv[0] and the bridge script argv[1] -- never prefixed with
    `python3`, which is precisely the mistake Ticket_424 kept retrying.
    """
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
            "retry_same_call": False,
        })
    text = (proc.stdout or "").strip()
    if not text:
        return json.dumps({
            "ok": False,
            "operation": params.get("operation"),
            "error": (proc.stderr or f"bridge exited {proc.returncode}").strip()[:1000],
            "retry_same_call": False,
        })
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        parsed = {
            "ok": False,
            "operation": params.get("operation"),
            "error": "bridge returned non-JSON output",
            "detail": text[:1000],
            "retry_same_call": False,
        }
    if proc.returncode != 0 and parsed.get("ok", True):
        parsed = {
            "ok": False,
            "operation": params.get("operation"),
            "error": f"bridge exited {proc.returncode}",
            "detail": parsed,
            "retry_same_call": False,
        }
    return json.dumps(parsed, default=str)


def _tool_handler(params: dict[str, Any], **kwargs: Any) -> str:
    del kwargs
    return _invoke_bridge(params)


def _pre_tool_call(tool_name: str, args: dict[str, Any] | None = None,
                   task_id: str = "", **kwargs: Any) -> dict[str, str] | None:
    args = args or {}
    session = _session_key(task_id, **kwargs)

    if tool_name == "terminal":
        command = _terminal_command(args)
        if any(marker in command for marker in _BLOCKED_TERMINAL_MARKERS):
            return {"action": "block", "message": _BLOCK_MESSAGE}
        return None

    if tool_name != TOOL_NAME:
        return None

    fp = _fingerprint(args)
    with _lock:
        calls = _session_calls[session]
        failures = _session_failures[session].get(fp, 0)
        if failures >= MAX_IDENTICAL_FAILURES:
            return {
                "action": "block",
                "message": (
                    f"Repeated-failure guard: this exact xstudio_l2 call already failed "
                    f"{failures} times. Do not retry it or wrap it differently. Change the "
                    "evidence path/arguments, use another typed operation, or complete with "
                    "an honest non-resolution outcome."
                ),
            }
        if calls >= MAX_TOOL_CALLS:
            return {
                "action": "block",
                "message": (
                    f"L2 investigation budget exhausted ({MAX_TOOL_CALLS} xstudio_l2 calls "
                    "this session). Stop querying. Save the current ledger if possible and "
                    "complete with UPDATE/QUESTION/L3_ESCALATION/NEEDS_HUMAN_ACTION based "
                    "only on verified evidence; do not open another shell path."
                ),
            }
        _session_calls[session] = calls + 1
    return None


def _post_tool_call(tool_name: str, args: dict[str, Any] | None = None,
                    result: Any = None, task_id: str = "", **kwargs: Any) -> None:
    if tool_name != TOOL_NAME:
        return
    parsed = _parse_result(result)
    if parsed.get("ok") is not False and "error" not in parsed:
        return
    session = _session_key(task_id, **kwargs)
    fp = _fingerprint(args or {})
    with _lock:
        _session_failures[session][fp] += 1


def _cleanup_session(task_id: str = "", **kwargs: Any) -> None:
    session = _session_key(task_id, **kwargs)
    with _lock:
        _session_calls.pop(session, None)
        _session_failures.pop(session, None)


def _pre_llm_call(**kwargs: Any) -> dict[str, str]:
    """Re-assert the execution contract every turn.

    Pre-migration Kanban cards still contain the old raw interpreter recipe in
    their body. Without this, an old card's text can out-argue the skill and
    send the worker back down the retired path.
    """
    del kwargs
    return {
        "context": (
            "L2 EXECUTION CONTRACT: use the xstudio_l2 tool for ALL XStudio/Helpdesk SQL, "
            "schema discovery, run evidence, ticket refresh, and investigation-ledger work. "
            "Any raw Python/sqlcmd/pyodbc/pip command shown in older task text is legacy and "
            "is blocked by the harness. Do not install dependencies. After two identical tool "
            "failures, change the evidence path instead of retrying."
        )
    }


_SCHEMA = {
    "name": TOOL_NAME,
    "description": (
        "Typed XStudio L2 investigation interface. Use this instead of terminal/Python/sqlcmd "
        "for database/schema/ticket/run/ledger work. The harness owns credentials, pyodbc, "
        "Windows/WSL transport, read-only enforcement, auditing, retry limits, and safe "
        "procedure allowlisting."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "operation": {"type": "string", "enum": [
                "select", "query", "suggest_tables", "find_objects",
                "get_definition", "validate_identifiers", "read_procedure",
                "get_ticket_context", "get_run_actions", "save_ledger"
            ]},
            "database": {"type": "string", "enum": [
                "XStudio_Helpdesk", "XStudio_Xbatch", "XStudio_Configuration_Xbatch"
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
            "ledger": {"type": "object"}
        },
        "required": ["operation"],
        "additionalProperties": False
    }
}


def register(ctx: Any) -> None:
    ctx.register_tool(
        name=TOOL_NAME,
        toolset=TOOLSET,
        schema=_SCHEMA,
        handler=_tool_handler,
        description="Guarded typed XStudio L2 investigation interface.",
    )
    ctx.register_hook("pre_tool_call", _pre_tool_call)
    ctx.register_hook("post_tool_call", _post_tool_call)
    ctx.register_hook("pre_llm_call", _pre_llm_call)
    ctx.register_hook("on_session_end", _cleanup_session)
    ctx.register_hook("on_session_finalize", _cleanup_session)
    ctx.register_hook("on_session_reset", _cleanup_session)
