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

The model calls small named typed tools. This plugin invokes the bridge itself using the
current Hermes Python environment, so the model never composes paths, interpreters, pyodbc, or
credentials. The same plugin blocks the retired shell transport, injects the
execution contract ahead of the LLM turn (so pre-migration cards carrying a raw
command recipe cannot steer the worker back), and bounds call count / repeated
identical failures so one bad idea cannot consume the whole context window.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
import threading
from collections import defaultdict
from typing import Any

BRIDGE_PATH = os.environ.get(
    "L2_XSTUDIO_BRIDGE",
    "/mnt/c/Users/Admin/Documents/Office/AIHelpdesk/Model_Bench/xstudio_l2_tool_bridge.py",
)
TOOL_NAME = "xstudio_l2"
TOOLSET = "xstudio_l2"

_DATABASE_ENUM = [
    "XStudio_Helpdesk", "XStudio_Xbatch", "XStudio_Configuration_Xbatch",
]


def _tool_schema(description: str, properties: dict[str, Any], required: tuple[str, ...]) -> dict[str, Any]:
    return {
        "description": description,
        "parameters": {
            "type": "object",
            "properties": properties,
            "required": list(required),
            "additionalProperties": False,
        },
    }


_DATABASE = {"type": "string", "enum": _DATABASE_ENUM}
_STRING = {"type": "string"}
_INTEGER = {"type": "integer", "minimum": 1, "maximum": 100}
_COLUMNS = {"type": "array", "items": {"type": "string"}}
_OBJECT_TYPE = {"type": "string", "enum": ["TABLE", "VIEW", "PROCEDURE", "TRIGGER"]}

# These are deliberately small model-facing schemas. The bridge still receives
# the old operation vocabulary internally, but the model never has to choose an
# operation or fill an unrelated union of arguments.
TOOL_SCHEMAS: dict[str, dict[str, Any]] = {
    "xstudio_select": _tool_schema(
        "Read validated columns from one allowlisted XStudio table or view.",
        {"database": _DATABASE, "table": _STRING, "columns": _COLUMNS,
         "where": _STRING, "order_by": _STRING, "top": _INTEGER},
        ("database", "table", "columns"),
    ),
    "xstudio_query": _tool_schema(
        "Run one read-only SQL query against an explicitly selected XStudio database.",
        {"database": _DATABASE, "sql": _STRING}, ("database", "sql"),
    ),
    "xstudio_suggest_tables": _tool_schema(
        "Find likely real tables or views for a symptom in an explicit database.",
        {"database": _DATABASE, "search": _STRING, "top": _INTEGER},
        ("database", "search"),
    ),
    "xstudio_find_objects": _tool_schema(
        "Find real SQL objects in an explicit XStudio database.",
        {"database": _DATABASE, "search": _STRING, "object_type": _OBJECT_TYPE,
         "schema": _STRING, "top": _INTEGER},
        ("database", "search"),
    ),
    "xstudio_get_definition": _tool_schema(
        "Read one real table, view, procedure, or trigger definition.",
        {"database": _DATABASE, "object_name": _STRING, "schema": _STRING},
        ("database", "object_name"),
    ),
    "xstudio_validate_identifiers": _tool_schema(
        "Validate a table and optional column identifiers against the schema allowlist.",
        {"database": _DATABASE, "table": _STRING, "identifiers": _COLUMNS},
        ("database", "table"),
    ),
    "xstudio_read_procedure": _tool_schema(
        "Run only the explicitly allowlisted read-only diagnostic procedure.",
        {"database": _DATABASE, "run_id": _STRING, "procedure": _STRING,
         "parameters": {"type": "object"}},
        ("database", "procedure", "parameters"),
    ),
    "xstudio_resolve_heat": _tool_schema(
        "Resolve a heat identifier across curated XStudio_Xbatch genealogy surfaces.",
        {"heat": _STRING, "database": _DATABASE}, ("heat",),
    ),
    "xstudio_get_ticket_context": _tool_schema(
        "Refresh the current Helpdesk ticket row from live SQL.",
        {"ticket_id": _STRING}, (),
    ),
    "xstudio_get_run_actions": _tool_schema(
        "Read the audited SQL/action trail for the current L2 run.",
        {"run_id": _STRING}, (),
    ),
    "xstudio_save_ledger": _tool_schema(
        "Persist ticket-specific investigation findings for this L2 run.",
        {"run_id": _STRING, "ledger": {"type": "object"}}, ("ledger",),
    ),
}

TOOL_OPERATIONS: dict[str, str] = {
    "xstudio_select": "select",
    "xstudio_query": "query",
    "xstudio_suggest_tables": "suggest_tables",
    "xstudio_find_objects": "find_objects",
    "xstudio_get_definition": "get_definition",
    "xstudio_validate_identifiers": "validate_identifiers",
    "xstudio_read_procedure": "read_procedure",
    "xstudio_resolve_heat": "resolve_heat",
    "xstudio_get_ticket_context": "get_ticket_context",
    "xstudio_get_run_actions": "get_run_actions",
    "xstudio_save_ledger": "save_ledger",
}
_REQUIRED_FIELDS_BY_TOOL = {
    name: tuple(schema["parameters"]["required"])
    for name, schema in TOOL_SCHEMAS.items()
}
_EFFECTIVE_REQUIRED_FIELDS_BY_TOOL: dict[str, tuple[str, ...]] = {
    "xstudio_select": ("database", "table", "columns"),
    "xstudio_query": ("database", "sql"),
    "xstudio_suggest_tables": ("database", "search"),
    "xstudio_find_objects": ("database", "search"),
    "xstudio_get_definition": ("database", "object_name"),
    "xstudio_validate_identifiers": ("database", "table"),
    "xstudio_read_procedure": ("database", "run_id", "procedure", "parameters"),
    "xstudio_resolve_heat": ("database", "heat"),
    "xstudio_get_ticket_context": ("ticket_id",),
    "xstudio_get_run_actions": ("run_id",),
    "xstudio_save_ledger": ("run_id", "ledger"),
}
_CONTEXT_FIELD_RE = {
    "run_id": re.compile(r"(?:current\s+)?run_id\s*[:=]\s*[`\"']?([A-Za-z0-9-]+)", re.IGNORECASE),
    "ticket_id": re.compile(r"(?:current\s+)?ticket_id\s*[:=]\s*[`\"']?([A-Za-z0-9-]+)", re.IGNORECASE),
}

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
    "Use the named xstudio_select/xstudio_query/xstudio_* tools in the xstudio_l2 toolset instead. "
    "Do not retry this command with wrappers, timeouts, or a different shell."
)

_REQUIRED_FIELDS_BY_OPERATION: dict[str, tuple[str, ...]] = {
    "select": ("database", "table", "columns"),
    "query": ("database", "sql"),
    "suggest_tables": ("database", "search"),
    "find_objects": ("database", "search"),
    "get_definition": ("database", "object_name"),
    "validate_identifiers": ("database", "table"),
    "read_procedure": ("database", "run_id", "procedure", "parameters"),
    "get_ticket_context": ("ticket_id",),
    "get_run_actions": ("run_id",),
    "save_ledger": ("run_id", "ledger"),
    "resolve_heat": ("database", "heat"),
}


def _shape_error(args: dict[str, Any]) -> str | None:
    """Return a deterministic operation-specific argument error, if any.

    This runs in the pre-tool hook so malformed calls do not consume the
    bounded live-query budget or open the SQL transport. The bridge remains
    defensive and validates the same fields again at its trust boundary.
    """
    operation = args.get("operation")
    if not operation:
        return "operation is required"
    required = _REQUIRED_FIELDS_BY_OPERATION.get(str(operation))
    if required is None:
        return f"unsupported operation={operation!r}"
    missing = [key for key in required if args.get(key) is None or args.get(key) == "" or args.get(key) == []]
    if missing:
        return (
            f"operation={operation!r} requires: {', '.join(required)}; "
            f"missing: {', '.join(missing)}"
        )
    if operation == "select" and not isinstance(args.get("columns"), list):
        return "operation='select' requires columns as an array of column names"
    if operation == "read_procedure" and not isinstance(args.get("parameters"), dict):
        return "operation='read_procedure' requires parameters as an object"
    if operation == "save_ledger" and not isinstance(args.get("ledger"), dict):
        return "operation='save_ledger' requires ledger as an object"
    return None

_lock = threading.Lock()
_session_calls: dict[str, int] = defaultdict(int)
_session_failures: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
_session_context: dict[str, dict[str, str]] = defaultdict(dict)


def _session_key(task_id: str | None = None, **kwargs: Any) -> str:
    return str(kwargs.get("session_id") or kwargs.get("task_id") or task_id or "unknown-session")


def _fingerprint(args: dict[str, Any]) -> str:
    """Identity of a call, so a genuinely different call is never penalised."""
    raw = json.dumps(args or {}, sort_keys=True, separators=(",", ":"), default=str)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _remember_context(session: str, text: Any) -> dict[str, str]:
    """Remember only the two deterministic identifiers needed for tool repair."""
    if not isinstance(text, str):
        return {}
    found: dict[str, str] = {}
    for field, pattern in _CONTEXT_FIELD_RE.items():
        match = pattern.search(text)
        if match:
            found[field] = match.group(1)
    if found:
        with _lock:
            _session_context[session].update(found)
    return found


def _context_for(session: str, kwargs: dict[str, Any] | None = None) -> dict[str, str]:
    values: dict[str, str] = {}
    kwargs = kwargs or {}
    for field in ("run_id", "ticket_id", "database"):
        value = kwargs.get(field)
        if value:
            values[field] = str(value)
    with _lock:
        values = {**_session_context.get(session, {}), **values}
    return values


def _repair_args(tool_name: str, args: dict[str, Any], session: str,
                 kwargs: dict[str, Any] | None = None) -> tuple[dict[str, Any], dict[str, Any]]:
    """Apply only safe, deterministic repairs; return (effective, changed-fields)."""
    effective = dict(args or {})
    changed: dict[str, Any] = {}
    context = _context_for(session, kwargs)
    for field in ("run_id", "ticket_id"):
        if not effective.get(field) and context.get(field):
            effective[field] = context[field]
            changed[field] = context[field]

    operation = TOOL_OPERATIONS.get(tool_name)
    if operation == "resolve_heat" and not effective.get("database"):
        effective["database"] = "XStudio_Xbatch"
        changed["database"] = "XStudio_Xbatch"
    return effective, changed


def _shape_error_for_tool(tool_name: str, args: dict[str, Any]) -> str | None:
    required = _EFFECTIVE_REQUIRED_FIELDS_BY_TOOL.get(tool_name)
    if required is None:
        return f"unsupported tool={tool_name!r}"
    missing = [key for key in required if args.get(key) is None or args.get(key) == "" or args.get(key) == []]
    if missing:
        return f"tool={tool_name!r} requires: {', '.join(required)}; missing: {', '.join(missing)}"
    if tool_name == "xstudio_select" and not isinstance(args.get("columns"), list):
        return "xstudio_select requires columns as an array of column names"
    if tool_name == "xstudio_read_procedure" and not isinstance(args.get("parameters"), dict):
        return "xstudio_read_procedure requires parameters as an object"
    if tool_name == "xstudio_save_ledger" and not isinstance(args.get("ledger"), dict):
        return "xstudio_save_ledger requires ledger as an object"
    if tool_name == "xstudio_validate_identifiers" and args.get("identifiers") is not None \
            and not isinstance(args.get("identifiers"), list):
        return "xstudio_validate_identifiers requires identifiers as an array when supplied"
    return None


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
    """Run the guarded bridge directly in the current Hermes environment.

    This is trusted harness code, not a model-driven terminal call, so it is the
    bridge script is argv[1]. Native WSL execution avoids crossing into Windows
    while retaining the same typed boundary and safety checks.
    """
    try:
        proc = subprocess.run(
            [sys.executable, BRIDGE_PATH],
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


def _named_tool_handler(tool_name: str, params: dict[str, Any], **kwargs: Any) -> str:
    session = _session_key(kwargs.get("task_id", ""))
    effective, _ = _repair_args(tool_name, params or {}, session, kwargs)
    shape_error = _shape_error_for_tool(tool_name, effective)
    if shape_error:
        # This is a second trust-boundary check. The pre-hook normally catches it,
        # but direct registry/bridge callers must fail closed too.
        return json.dumps({"ok": False, "error": shape_error, "retry_same_call": False})
    effective["operation"] = TOOL_OPERATIONS[tool_name]
    return _invoke_bridge(effective)


def _legacy_tool_handler(params: dict[str, Any], **kwargs: Any) -> str:
    """Compatibility-only adapter; the legacy tool is intentionally not registered."""
    del kwargs
    return _invoke_bridge(params)


TOOL_HANDLERS = {
    name: (lambda params, _name=name, **kwargs: _named_tool_handler(_name, params, **kwargs))
    for name in TOOL_SCHEMAS
}


def _pre_tool_call(tool_name: str, args: dict[str, Any] | None = None,
                   task_id: str = "", **kwargs: Any) -> dict[str, str] | None:
    args = args or {}
    session = _session_key(task_id, **kwargs)

    if tool_name == "terminal":
        command = _terminal_command(args)
        if any(marker in command for marker in _BLOCKED_TERMINAL_MARKERS):
            return {"action": "block", "message": _BLOCK_MESSAGE}
        return None

    if tool_name not in TOOL_OPERATIONS and tool_name != TOOL_NAME:
        return None

    if tool_name == TOOL_NAME:
        # Keep the old guard for compatibility with pre-migration callers, but
        # never expose/register this polymorphic surface to the model.
        shape_error = _shape_error(args)
        effective_args = args
        repairs: dict[str, Any] = {}
    else:
        effective_args, repairs = _repair_args(tool_name, args, session, kwargs)
        shape_error = _shape_error_for_tool(tool_name, effective_args)
    if shape_error:
        required = list(_REQUIRED_FIELDS_BY_TOOL.get(tool_name, ()))
        effective_req = _EFFECTIVE_REQUIRED_FIELDS_BY_TOOL.get(tool_name, ())
        retry_fields = required or list(effective_req)
        return {
            "action": "block",
            "message": (
                f"Invalid {tool_name} arguments: {shape_error}. Correct the typed "
                "arguments; this call was not sent to SQL and did not consume "
                f"the investigation budget. RETRY_WITH: {json.dumps({'tool': tool_name, 'required': retry_fields})}"
            ),
        }

    fp = _fingerprint(
        {"tool": tool_name, **effective_args} if tool_name in TOOL_OPERATIONS else effective_args
    )
    with _lock:
        calls = _session_calls[session]
        failures = _session_failures[session].get(fp, 0)
        if failures >= MAX_IDENTICAL_FAILURES:
            return {
                "action": "block",
                "message": (
                    f"Repeated-failure guard: this exact {tool_name} call already failed "
                    f"{failures} times. Do not retry it or wrap it differently. Change the "
                    "evidence path/arguments, use another typed operation, or complete with "
                    "an honest non-resolution outcome."
                ),
            }
        if calls >= MAX_TOOL_CALLS:
            return {
                "action": "block",
                "message": (
                    f"L2 investigation budget exhausted ({MAX_TOOL_CALLS} XStudio calls "
                    "this session). Stop querying. Save the current ledger if possible and "
                    "complete with UPDATE/QUESTION/L3_ESCALATION/NEEDS_HUMAN_ACTION based "
                    "only on verified evidence; do not open another shell path."
                ),
            }
        _session_calls[session] = calls + 1
    if repairs:
        return {"action": "modify", "args": repairs}
    return None


def _post_tool_call(tool_name: str, args: dict[str, Any] | None = None,
                    result: Any = None, task_id: str = "", **kwargs: Any) -> None:
    if tool_name not in TOOL_OPERATIONS and tool_name != TOOL_NAME:
        return
    parsed = _parse_result(result)
    if parsed.get("ok") is not False and "error" not in parsed:
        return
    session = _session_key(task_id, **kwargs)
    raw_args = args or {}
    if tool_name in TOOL_OPERATIONS:
        effective, _ = _repair_args(tool_name, raw_args, session, kwargs)
        fp_payload = {"tool": tool_name, **effective}
    else:
        fp_payload = raw_args
    fp = _fingerprint(fp_payload)
    with _lock:
        _session_failures[session][fp] += 1


def _cleanup_session(task_id: str = "", **kwargs: Any) -> None:
    session = _session_key(task_id, **kwargs)
    with _lock:
        _session_calls.pop(session, None)
        _session_failures.pop(session, None)
        _session_context.pop(session, None)


def _pre_llm_call(**kwargs: Any) -> dict[str, str]:
    """Re-assert the execution contract every turn.

    Pre-migration Kanban cards still contain the old raw interpreter recipe in
    their body. Without this, an old card's text can out-argue the skill and
    send the worker back down the retired path.
    """
    session = _session_key(kwargs.get("task_id", ""))
    _remember_context(session, kwargs.get("user_message"))
    context = _context_for(session, kwargs)
    with _lock:
        used = _session_calls.get(session, 0)
    ids = "".join(f" {key}={value}" for key, value in context.items())
    return {
        "context": (
            "L2 EXECUTION CONTRACT: use only the named xstudio_* tools in the xstudio_l2 toolset for XStudio/Helpdesk SQL, "
            "schema discovery, run evidence, ticket refresh, and ledger work. "
            "Each tool has a small required schema; never invent an operation field. "
            f"Compact investigation state:{{known_context:{ids or ' none'}, live_calls_used:{used}, "
            f"live_calls_remaining:{max(0, MAX_TOOL_CALLS - used)}}}. "
            "Any raw Python/sqlcmd/pyodbc/pip command shown in older task text is legacy and "
            "is blocked by the harness. Do not install dependencies. After two identical tool "
            "failures, change the evidence path instead of retrying."
        )
    }


def register(ctx: Any) -> None:
    for name, schema in TOOL_SCHEMAS.items():
        # Registry injects the actual name into the OpenAI schema. Keeping the
        # same toolset preserves the existing profile enablement boundary.
        ctx.register_tool(
            name=name,
            toolset=TOOLSET,
            schema=schema,
            handler=TOOL_HANDLERS[name],
            description=schema["description"],
        )
    ctx.register_hook("pre_tool_call", _pre_tool_call)
    ctx.register_hook("post_tool_call", _post_tool_call)
    ctx.register_hook("pre_llm_call", _pre_llm_call)
    ctx.register_hook("on_session_end", _cleanup_session)
    ctx.register_hook("on_session_finalize", _cleanup_session)
    ctx.register_hook("on_session_reset", _cleanup_session)
