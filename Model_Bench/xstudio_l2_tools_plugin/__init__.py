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
from pathlib import Path
from typing import Any, Optional

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
    "xstudio_heat_context": _tool_schema(
        "Read canonical EAF/LRF/CCM, work-order, SAP and billet evidence for one heat.",
        {"heat": _STRING, "database": _DATABASE}, ("heat",),
    ),
    "xstudio_sap_api_context": _tool_schema(
        "Read the live reviewed SAP API transaction summary for one API type.",
        {"api_type": _STRING, "identifier": _STRING, "database": _DATABASE}, ("api_type",),
    ),
    "xstudio_work_order_context": _tool_schema(
        "Read canonical work-order and campaign evidence using fixed reviewed recipes.",
        {"work_order": _STRING, "campaign": _STRING, "database": _DATABASE}, ("work_order",),
    ),
    "xstudio_submit_proposal": _tool_schema(
        "Complete the L2 investigation with a flat proposal. Preferred over kanban_complete "
        "for submitting investigation results. The harness assembles full structured metadata.",
        {
            "response_type": {"type": "string", "enum": [
                "UPDATE", "QUESTION", "RESOLUTION", "L3_ESCALATION", "NEEDS_HUMAN_ACTION",
            ]},
            "summary": _STRING,
            "reply_text": _STRING,
            "requester_question": {"type": "string", "description": "Specific question for the requester when a necessary identifier or fact is missing. Sets response_type=QUESTION and waits for their answer instead of retrying."},
            "next_investigation_step": {"type": "string", "description": "For an incomplete UPDATE, the concrete new evidence check the next attempt can perform without waiting for requester information. Required for publication."},
            "evidence_status": {"type": "string", "enum": ["COMPLETE", "INCOMPLETE"]},
            "claim_status": {"type": "string", "enum": [
                "VERIFIED", "INFERRED", "UNVERIFIED", "CONTRADICTED",
            ]},
            "action_id": _STRING,
            "problem_summary": _STRING,
            "root_cause": _STRING,
            "resolution": _STRING,
        },
        ("response_type", "summary"),
    ),
}

_VALID_RESPONSE_TYPES = {"UPDATE", "QUESTION", "RESOLUTION", "L3_ESCALATION", "NEEDS_HUMAN_ACTION"}

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
    "xstudio_heat_context": "heat_context",
    "xstudio_sap_api_context": "sap_api_context",
    "xstudio_work_order_context": "work_order_context",
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
    "xstudio_heat_context": ("database", "run_id", "heat"),
    "xstudio_sap_api_context": ("database", "run_id", "api_type"),
    "xstudio_work_order_context": ("database", "run_id", "work_order"),
}
_CONTEXT_FIELD_RE = {
    "run_id": re.compile(r"(?:current\s+)?run_id\s*[:=]\s*[`\"']?([A-Za-z0-9-]+)", re.IGNORECASE),
    "ticket_id": re.compile(r"(?:current\s+)?ticket_id\s*[:=]\s*[`\"']?([A-Za-z0-9-]+)", re.IGNORECASE),
    "pipeline_stage": re.compile(r"pipeline_stage\s*[:=]\s*[`\"']?(investigation|rework|review)\b", re.IGNORECASE),
    "contract_repaired_from_unstructured": re.compile(
        r"contract_repaired_from_unstructured[`\"']?\s*:\s*(true)\b", re.IGNORECASE
    ),
    "valid_tables": re.compile(r"(?:current\s+)?valid_tables\s*[:=]\s*(.+)", re.IGNORECASE),
}

# Bounded so a single session cannot spend the 65.6K context on transport
# flailing. These are deliberately small: a competent investigation needs a
# handful of typed reads, not dozens of shell experiments.
MAX_TOOL_CALLS = max(1, int(os.environ.get("L2_MAX_XSTUDIO_TOOL_CALLS", "14")))
MAX_IDENTICAL_FAILURES = max(1, int(os.environ.get("L2_MAX_IDENTICAL_FAILURES", "2")))
BRIDGE_TIMEOUT_SECONDS = max(10, int(os.environ.get("L2_BRIDGE_TIMEOUT_SECONDS", "90")))
MIN_SUBSTANTIVE_COMPLETION_CHARS = 160

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
    "heat_context": ("database", "run_id", "heat"),
    "sap_api_context": ("database", "run_id", "api_type"),
    "work_order_context": ("database", "run_id", "work_order"),
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


_VALID_TABLE_ENTRY_RE = re.compile(r"([^,\[\]]+?)(?:\[([^\]]*)\])?\s*(?:,|$)")


def _parse_valid_tables(raw: str) -> dict[str, set[str] | None]:
    """'db1.tbl1[colA,colB], db2.tbl2' -> {'tbl1': {'cola','colb'}, 'db1.tbl1': {...},
    'tbl2': None, 'db2.tbl2': None} (lowercase keys; None means no column list
    was recorded for that table, so columns are not restricted for it).

    Both the bare table name and the fully-qualified form are accepted as keys
    since the model may supply either in its own `table` argument.
    """
    allowed: dict[str, set[str] | None] = {}
    for match in _VALID_TABLE_ENTRY_RE.finditer(raw):
        name = match.group(1).strip().strip(".")
        if not name:
            continue
        cols_raw = match.group(2)
        columns = {c.strip().lower() for c in cols_raw.split(",") if c.strip()} if cols_raw else None
        for key in ({name.lower(), name.rsplit(".", 1)[-1].lower()} if "." in name else {name.lower()}):
            allowed[key] = columns
    return allowed


def _table_not_in_valid_tables(session: str, effective_args: dict[str, Any]) -> str | None:
    """None if the call's table (and, when recorded, its requested columns)
    are allowed, or no evidence-plan restriction applies to this ticket;
    otherwise a message naming the real options.
    """
    with _lock:
        raw = _session_context.get(session, {}).get("valid_tables")
    if not raw:
        return None
    allowed = _parse_valid_tables(raw)
    if not allowed:
        return None
    table = str(effective_args.get("table") or "").strip()
    if not table:
        return None
    bare = table.rsplit(".", 1)[-1].lower()
    if table.lower() not in allowed and bare not in allowed:
        return (
            f"'{table}' is not one of the tables Jev's evidence plan selected for this ticket "
            f"(valid_tables: {raw})."
        )

    allowed_columns = allowed.get(table.lower())
    if allowed_columns is None:
        allowed_columns = allowed.get(bare)
    requested = effective_args.get("columns")
    if allowed_columns and isinstance(requested, list):
        bad = [c for c in requested if str(c).strip().lower() not in allowed_columns]
        if bad:
            return (
                f"{bad} are not among the real columns Jev's evidence plan already probed on "
                f"'{table}' (valid_tables: {raw})."
            )
    return None


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
    if operation in {"resolve_heat", "heat_context", "sap_api_context", "work_order_context"} and not effective.get("database"):
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


def _validate_submit_proposal_inputs(
    params: dict[str, Any], context: dict[str, Any],
) -> tuple[Optional[str], Optional[dict[str, Any]]]:
    """Reject bad/incomplete xstudio_submit_proposal input before any assembly.
    Returns (error_json, None) to reject the call, or (None, validated_fields)
    to proceed. Pure validation -- no side effects, no derived metadata."""
    response_type = str(params.get("response_type") or "").upper().strip()
    summary = str(params.get("summary") or "").strip()
    if response_type not in _VALID_RESPONSE_TYPES:
        return json.dumps({
            "ok": False,
            "error": f"response_type must be one of {sorted(_VALID_RESPONSE_TYPES)}, got {response_type!r}",
            "retry_same_call": False,
        }), None
    if len(summary) < MIN_SUBSTANTIVE_COMPLETION_CHARS:
        return json.dumps({
            "ok": False,
            "error": (
                f"summary must be at least {MIN_SUBSTANTIVE_COMPLETION_CHARS} characters of "
                f"substantive investigation findings (got {len(summary)})"
            ),
            "retry_same_call": False,
        }), None

    run_id = context.get("run_id", "")
    ticket_id = context.get("ticket_id", "")
    if not run_id or not ticket_id:
        return json.dumps({
            "ok": False,
            "error": "run_id and ticket_id could not be resolved from session context; "
                     "ensure the task body was parsed before calling xstudio_submit_proposal",
            "retry_same_call": False,
        }), None

    requester_question = str(params.get("requester_question") or "").strip()
    if requester_question:
        response_type = "QUESTION"
    if response_type == "QUESTION" and not requester_question:
        return json.dumps({
            "ok": False,
            "error": "QUESTION requires requester_question: ask for the specific missing fact in customer-facing language.",
            "retry_same_call": False,
        }), None

    claim_status = str(params.get("claim_status") or "UNVERIFIED").upper().strip()
    if claim_status not in {"VERIFIED", "INFERRED", "UNVERIFIED", "CONTRADICTED"}:
        claim_status = "UNVERIFIED"

    action_id = str(params.get("action_id") or "").strip()
    if claim_status == "VERIFIED" and not action_id:
        return json.dumps({
            "ok": False,
            "error": "VERIFIED claims require action_id — a current-run Hermes action ID. "
                     "Use xstudio_get_run_actions to find one, or set claim_status to INFERRED/UNVERIFIED.",
            "retry_same_call": False,
        }), None

    return None, {
        "response_type": response_type,
        "summary": summary,
        "run_id": run_id,
        "ticket_id": ticket_id,
        "requester_question": requester_question,
        "claim_status": claim_status,
        "action_id": action_id,
    }


def _derive_proposal_metadata(fields: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
    """Pure derivation of the kanban_complete metadata dict: claim assembly,
    evidence_status, reply_text. Assumes fields already passed validation."""
    response_type = fields["response_type"]
    summary = fields["summary"]
    claim_status = fields["claim_status"]
    action_id = fields["action_id"]
    requester_question = fields["requester_question"]

    evidence: list[dict[str, str]] = []
    if action_id:
        evidence = [{"action_id": action_id}]
    claim = {
        "id": "C1",
        "claim": summary,
        "material": True,
        "status": claim_status,
        "evidence": evidence,
    }

    evidence_status = str(params.get("evidence_status") or "").upper().strip()
    if evidence_status not in {"COMPLETE", "INCOMPLETE"}:
        # Default: COMPLETE only for RESOLUTION with VERIFIED claim
        evidence_status = "COMPLETE" if (
            response_type == "RESOLUTION" and claim_status == "VERIFIED"
        ) else "INCOMPLETE"
    if claim_status != "VERIFIED" or not action_id:
        evidence_status = "INCOMPLETE"

    reply_text = str(params.get("reply_text") or "").strip()
    if not reply_text:
        if evidence_status == "INCOMPLETE":
            reply_text = (
                "Evidence status: INCOMPLETE. The investigation produced findings "
                "that require independent review before any cause or resolution is "
                "treated as verified.\n\n" + summary
            )
        else:
            reply_text = summary
    elif evidence_status == "INCOMPLETE" and not reply_text.lower().startswith("evidence status: incomplete"):
        reply_text = (
            "Evidence status: INCOMPLETE. No material claim below should be treated as "
            "verified until current-run evidence is cited.\n\n" + reply_text
        )

    metadata: dict[str, Any] = {
        "run_id": fields["run_id"],
        "ticket_id": fields["ticket_id"],
        "response_type": response_type,
        "reply_text": reply_text,
        "claims_contract_version": 1,
        "claims": [claim],
        "evidence_status": evidence_status,
        "submitted_via": "xstudio_submit_proposal",
    }
    if requester_question:
        metadata["reply_text"] = requester_question
        metadata["requester_question"] = requester_question
        metadata["investigator_notes"] = summary
    for optional_field in ("problem_summary", "root_cause", "resolution", "next_investigation_step"):
        value = str(params.get(optional_field) or "").strip()
        if value:
            metadata[optional_field] = value
    return metadata


def _submit_proposal_handler(params: dict[str, Any], **kwargs: Any) -> str:
    """Assemble flat proposal args into full kanban_complete metadata, then complete the task.

    This is trusted harness code. The model fills in simple top-level string
    fields; this handler builds the nested claims array and metadata dict that
    the completion contract requires, then calls ``hermes kanban complete``
    directly.  It does NOT consume the XStudio tool-call budget and does NOT
    go through the SQL bridge.
    """
    session = _session_key(kwargs.get("task_id", ""))
    context = _context_for(session, kwargs)
    params = _recover_leaked_parameters(dict(params or {}))
    if context.get("pipeline_stage", "").lower() == "review":
        return json.dumps({"ok": False, "error": "Reviewers judge the frozen proposal: use kanban_complete to approve or kanban_block to reject. Do not submit a replacement proposal.", "retry_same_call": False})

    error, fields = _validate_submit_proposal_inputs(params, context)
    if error:
        return error

    metadata = _derive_proposal_metadata(fields, params)
    response_type = fields["response_type"]
    claim_status = fields["claim_status"]
    evidence_status = metadata["evidence_status"]

    # Hermes scopes a dispatcher worker to HERMES_KANBAN_TASK and refuses any
    # other target; a remembered kanban_show id can be a prior task the worker
    # only inspected (live 2026-09-22: "refusing to mutate t_0f7bffa4").
    task_id = str(os.environ.get("HERMES_KANBAN_TASK") or context.get("kanban_task_id") or kwargs.get("task_id") or "")
    if not task_id:
        return json.dumps({
            "ok": False,
            "error": "task_id is not available in the handler context",
            "retry_same_call": False,
        })

    cmd = [
        "hermes", "kanban", "complete", task_id,
        "--summary", fields["summary"][:500],
        "--result", response_type,
        "--metadata", json.dumps(metadata, separators=(",", ":"), default=str),
    ]
    try:
        # Explicit cwd: an inherited, since-deleted worker cwd made `hermes`
        # fail with "getcwd() failed" and lost a VERIFIED RESOLUTION (2026-09-22).
        proc = subprocess.run(
            cmd, capture_output=True, text=True, timeout=30, cwd=str(Path.home()),
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return json.dumps({
            "ok": False,
            "error": f"kanban complete failed: {type(exc).__name__}: {exc}",
            "retry_same_call": False,
        })
    if proc.returncode != 0:
        stderr = (proc.stderr or "").strip()[:500]
        return json.dumps({
            "ok": False,
            "error": f"kanban complete exited {proc.returncode}: {stderr}",
            "retry_same_call": False,
        })

    return json.dumps({
        "ok": True,
        "submitted": True,
        "response_type": response_type,
        "evidence_status": evidence_status,
        "claim_status": claim_status,
        "message": (
            f"Proposal submitted as {response_type} with {claim_status} claim. "
            "The deterministic reconciler will create a reviewer and handle publication."
        ),
    })


# Build handlers for bridge-routed tools; xstudio_submit_proposal has its own handler.
_BRIDGE_TOOLS = {name for name in TOOL_SCHEMAS if name != "xstudio_submit_proposal"}

TOOL_HANDLERS: dict[str, Any] = {
    name: (lambda params, _name=name, **kwargs: _named_tool_handler(_name, params, **kwargs))
    for name in _BRIDGE_TOOLS
}
TOOL_HANDLERS["xstudio_submit_proposal"] = _submit_proposal_handler


def _kanban_review_contract_guard(context: dict[str, Any]) -> dict[str, str] | None:
    if (context.get("pipeline_stage", "").lower() == "review"
            and context.get("contract_repaired_from_unstructured", "").lower() == "true"):
        return {
            "action": "block",
            "message": (
                "L2 review contract: this frozen proposal was repaired from an unstructured "
                "investigator completion and is not eligible for approval. Call kanban_block "
                "with the specific missing claim/evidence objection so deterministic rework can "
                "produce a fresh structured proposal."
            ),
        }
    return None


def _kanban_completion_metadata_guard(args: dict[str, Any], context: dict[str, Any]) -> dict[str, str] | None:
    if context.get("pipeline_stage", "").lower() not in {"investigation", "rework"}:
        return None
    metadata = dict(args.get("metadata") or {}) if isinstance(args.get("metadata"), dict) else {}
    for field in ("run_id", "ticket_id"):
        if not metadata.get(field) and context.get(field):
            metadata[field] = context[field]
    metadata.setdefault("claims_contract_version", 1)
    missing = [field for field in ("run_id", "ticket_id", "response_type", "reply_text", "claims")
               if metadata.get(field) in (None, "", [])]
    summary = str(args.get("summary") or "").strip()
    if (len(summary) >= MIN_SUBSTANTIVE_COMPLETION_CHARS
            and metadata.get("run_id") and metadata.get("ticket_id")
            and all(metadata.get(field) in (None, "", [])
                    for field in ("response_type", "reply_text", "claims"))):
        # Small local models reliably produce a useful flat summary but can loop
        # forever when asked to serialize the nested proposal contract. Package
        # that summary as an explicitly incomplete UPDATE. The independent
        # reviewer still owns truth, and no statement is promoted to VERIFIED.
        metadata.update({
            "response_type": "UPDATE",
            "reply_text": (
                "Evidence status: INCOMPLETE. The investigation produced findings "
                "that require independent review before any cause or resolution is "
                "treated as verified."
            ),
            "claims": [{
                "id": "summary-1",
                "claim": summary,
                "material": True,
                "status": "UNVERIFIED",
                "evidence": [],
            }],
            "contract_packaged_from_summary": True,
            "evidence_status": "INCOMPLETE",
            "investigator_notes": summary,
        })
        return {"action": "modify", "args": {"metadata": metadata}}
    if missing:
        return {
            "action": "block",
            "message": (
                "L2 completion contract: metadata is missing " + ", ".join(missing) + ". "
                "Stay in this turn and retry kanban_complete with metadata containing run_id, ticket_id, "
                "response_type, reply_text, claims_contract_version=1, and a non-empty claims array. "
                "Each claim needs id, claim, material, status, and evidence; VERIFIED material claims "
                "must cite current-run action_id values."
            ),
        }
    return None


_LEAKED_TOOL_MARKUP = re.compile(r"</?(?:parameter|function|result|summary|tool_call)\b[^>]*>", re.I)
_LEAKED_PARAMETER = re.compile(r"<parameter=(\w+)>\s*(.*?)\s*(?=</parameter>|<parameter=|</?function|$)", re.I | re.S)


def _recover_leaked_parameters(args: dict[str, Any]) -> dict[str, Any]:
    """Split Qwen tool-call markup that leaked into a string argument.

    Qwen's native format is <parameter=name>value</parameter>. It sometimes
    serializes later arguments inside the first string, so the markup reached
    customer ReplyText (6 live rows) and an argument it did choose, such as
    claim_status=VERIFIED, was silently lost. Each string is cut at the first
    markup tag; a leaked name=value pair fills that argument only if it is empty.
    """
    repaired = dict(args)
    recovered: dict[str, str] = {}
    for key, value in args.items():
        if not isinstance(value, str):
            continue
        match = _LEAKED_TOOL_MARKUP.search(value) or re.search(r"<parameter=", value, re.I)
        if not match:
            continue
        tail = value[match.start():]
        repaired[key] = value[:match.start()].rstrip()
        for name, leaked in _LEAKED_PARAMETER.findall(tail):
            leaked = _LEAKED_TOOL_MARKUP.sub("", leaked).strip()
            if leaked and name not in recovered:
                recovered[name] = leaked
    for name, value in recovered.items():
        if repaired.get(name) in (None, ""):
            repaired[name] = value
    return repaired


def _kanban_contract_guard(tool_name: str, args: dict[str, Any], context: dict[str, Any]) -> dict[str, str] | None:
    """Every kanban_complete/kanban_block/terminal special case, self-contained."""
    if tool_name == "kanban_complete":
        result = _kanban_review_contract_guard(context)
        if result is not None:
            return result
        result = _kanban_completion_metadata_guard(args, context)
        if result is not None:
            return result
        # A small model can select the right terminal Kanban action yet serialize
        # an empty object. Preserve that decision without paying for another model
        # turn; structured metadata and the SQL evidence trail remain authoritative.
        if not (args.get("summary") or args.get("result")):
            return {"action": "modify", "args": {
                "summary": "Task completed; use the structured task metadata and persisted evidence trail for details."
            }}
        return None

    if tool_name == "kanban_block" and not (args.get("reason") or args.get("summary")):
        return {"action": "modify", "args": {
            "reason": "Task rejected or blocked; no structured reason was supplied by the worker."
        }}

    if tool_name == "terminal":
        command = _terminal_command(args)
        if any(marker in command for marker in _BLOCKED_TERMINAL_MARKERS):
            return {"action": "block", "message": _BLOCK_MESSAGE}
        return None

    return None


def _resolve_typed_tool_args(
    tool_name: str, args: dict[str, Any], session: str, kwargs: dict[str, Any],
) -> tuple[Optional[str], dict[str, Any], dict[str, Any]]:
    """Shape/compatibility resolution: one owner for "is this call well-formed,
    and what are its effective (possibly repaired) arguments"."""
    if tool_name == TOOL_NAME:
        # Keep the old guard for compatibility with pre-migration callers, but
        # never expose/register this polymorphic surface to the model.
        return _shape_error(args), args, {}
    effective_args, repairs = _repair_args(tool_name, args, session, kwargs)
    return _shape_error_for_tool(tool_name, effective_args), effective_args, repairs


def _budget_guard(session: str, tool_name: str, effective_args: dict[str, Any]) -> dict[str, str] | None:
    """Repeated-failure and per-session call-budget rate limiting. Self-contained
    owner of _session_calls/_session_failures; the only place that mutates them."""
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
    return None


def _completion_guard(tool_name: str, args: dict[str, Any], context: dict[str, Any]) -> dict[str, Any] | None:
    """Repair leaked tool-call markup, then apply the completion contract to the repaired args."""
    repaired = args if tool_name == "terminal" else _recover_leaked_parameters(args)
    result = _kanban_contract_guard(tool_name, repaired, context)
    if repaired == args or (result and result.get("action") == "block"):
        return result
    return {"action": "modify", "args": {**repaired, **((result or {}).get("args") or {})}}


def _pre_tool_call(tool_name: str, args: dict[str, Any] | None = None,
                   task_id: str = "", **kwargs: Any) -> dict[str, str] | None:
    args = args or {}
    session = _session_key(task_id, **kwargs)
    context = _context_for(session, kwargs)

    if tool_name in ("kanban_complete", "kanban_block", "terminal"):
        return _completion_guard(tool_name, args, context)

    # xstudio_submit_proposal does its own validation in _submit_proposal_handler
    # and is not a bridge/SQL tool, so it must not consume the investigation budget.
    if tool_name == "xstudio_submit_proposal":
        return None

    if tool_name not in TOOL_OPERATIONS and tool_name != TOOL_NAME:
        return None

    shape_error, effective_args, repairs = _resolve_typed_tool_args(tool_name, args, session, kwargs)
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

    if tool_name in ("xstudio_select", "xstudio_validate_identifiers"):
        table_error = _table_not_in_valid_tables(session, effective_args)
        if table_error:
            return {
                "action": "block",
                "message": (
                    f"{table_error} This call was not sent to SQL and did not consume the "
                    "investigation budget. Use one of the listed valid_tables, or call "
                    "find_objects/suggest_tables first if genuinely none of them fit."
                ),
            }

    budget_error = _budget_guard(session, tool_name, effective_args)
    if budget_error:
        return budget_error
    if repairs:
        return {"action": "modify", "args": repairs}
    return None


def _post_tool_call(tool_name: str, args: dict[str, Any] | None = None,
                    result: Any = None, task_id: str = "", **kwargs: Any) -> None:
    # Hermes does not consistently include the full task body in pre_llm_call.
    # Every Kanban worker does, however, begin with kanban_show. Learn the two
    # harness-owned identifiers from that deterministic response so model-hidden
    # run_id/ticket_id defaults remain reliable in real sessions.
    if tool_name == "kanban_show":
        parsed = _parse_result(result)
        task = parsed.get("task") if isinstance(parsed, dict) else None
        own_task = os.environ.get("HERMES_KANBAN_TASK")
        # Only the worker's own card defines its identity; inspecting a prior
        # attempt's card must not retarget run/ticket/task for this session.
        if isinstance(task, dict) and (not own_task or str(task.get("id") or "") == own_task):
            session = _session_key(task_id, **kwargs)
            _remember_context(session, task.get("body"))
            kanban_task_id = str(task.get("id") or "").strip()
            if kanban_task_id:
                with _lock:
                    _session_context[session]["kanban_task_id"] = kanban_task_id
        return
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
    completion_contract = (
        "You are the REVIEWER. Judge the frozen proposal; never submit a replacement. "
        "Approve with kanban_complete or reject with kanban_block. First check response type: "
        "reject UPDATE if only missing requester information can unblock the case, requiring QUESTION. "
        "Reject RESOLUTION if it only diagnoses a problem or proposes an unexecuted fix. "
        "Reject unsupported causal assertions without broad schema exploration. "
        if context.get("pipeline_stage", "").lower() == "review" else
        "When completing the investigation, use xstudio_submit_proposal(response_type,summary) "
        "instead of kanban_complete. If only the requester can supply a missing incident identifier "
        "or reproduction detail, submit QUESTION with requester_question containing the exact question "
        "now; do not submit UPDATE or query unrelated sample rows. "
    )
    return {
        "context": (
            "L2 EXECUTION CONTRACT: use only the named xstudio_* tools in the xstudio_l2 toolset for XStudio/Helpdesk SQL, "
            "schema discovery, run evidence, ticket refresh, and ledger work. "
            "Each tool has a small required schema; never invent an operation field. "
            f"{completion_contract}"
            "UPDATE retries automatically and cannot obtain a user's answer. "
            "Incomplete UPDATE requires next_investigation_step naming a concrete new evidence check. "
            "RESOLUTION closes the ticket: require COMPLETE evidence, VERIFIED claims with action_id, "
            "and resolution describing an observed successful outcome. A diagnosis or proposed fix is not resolution. "
            f"Compact investigation state:{{known_context:{ids or ' none'}, live_calls_used:{used}, "
            f"live_calls_remaining:{max(0, MAX_TOOL_CALLS - used)}}}. "
            "Any raw Python/sqlcmd/pyodbc/pip command shown in older task text is legacy and "
            "is blocked by the harness. Do not install dependencies. After two identical tool "
            "failures, change the evidence path instead of retrying. Jev planning/review is "
            "harness-owned; xstudio_l2 returns deterministic live evidence only. Do not attempt "
            "to call TypeSafe/Jev directly or recreate semantic routing inside this tool.\n"
            "DATABASE ROUTING & OPERATION CONTRACTS:\n"
            "- Target 'XStudio_Xbatch' for ALL production/plant process evidence (heats, EAF, CCM, billets, work orders, SAP postings). Plant/EAF evidence lives in XStudio_Xbatch, NOT XStudio_Helpdesk.\n"
            "- Target 'XStudio_Helpdesk' for Helpdesk tickets, Hermes runs, workflow status, and activity timeline.\n"
            "- Target 'XStudio_Configuration_Xbatch' for configuration metadata.\n"
            "- Every SQL/schema operation REQUIRES 'database' and its operation-specific parameters (e.g. select: database+table+columns; query: database+sql; suggest_tables/find_objects: database+search; get_definition: database+object_name; validate_identifiers: database+table+identifiers)."
        )
    }


_SCHEMA = {
    "name": TOOL_NAME,
    "description": (
        "Typed XStudio L2 investigation interface for database, schema, ticket, run, and ledger operations. "
        "Use this instead of terminal/Python/sqlcmd. "
        "DATABASE ROUTING: "
        "- 'XStudio_Xbatch': All production and plant process evidence (heats, EAF, CCM, billets, work orders, SAP process data). "
        "- 'XStudio_Helpdesk': Helpdesk tickets, Hermes runs, workflow status, activity timeline. "
        "- 'XStudio_Configuration_Xbatch': XStudio configuration metadata. "
        "Every SQL/schema operation REQUIRES 'database' and its operation-specific parameters."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "operation": {
                "type": "string",
                "enum": [
                    "select", "query", "probe_table", "suggest_tables", "find_objects",
                    "get_definition", "validate_identifiers", "read_procedure",
                    "get_ticket_context", "get_run_actions", "save_ledger"
                ],
                "description": (
                    "Operation to execute. Required fields per operation:\n"
                    "- 'select': requires [database, table, columns, run_id]\n"
                    "- 'query': requires [database, sql, run_id]\n"
                    "- 'probe_table': requires [database, table, ticket, run_id]\n"
                    "- 'suggest_tables': requires [database, search]\n"
                    "- 'find_objects': requires [database, search]\n"
                    "- 'get_definition': requires [database, object_name]\n"
                    "- 'validate_identifiers': requires [database, table, identifiers]\n"
                    "- 'read_procedure': requires [database, run_id, procedure, parameters]\n"
                    "- 'get_ticket_context': requires [ticket_id]\n"
                    "- 'get_run_actions': requires [run_id]\n"
                    "- 'save_ledger': requires [run_id, ledger]"
                )
            },
            "database": {
                "type": "string",
                "enum": [
                    "XStudio_Helpdesk", "XStudio_Xbatch", "XStudio_Configuration_Xbatch"
                ],
                "description": (
                    "Target database. REQUIRED for select, query, probe_table, suggest_tables, "
                    "find_objects, get_definition, validate_identifiers, read_procedure.\n"
                    "ROUTING:\n"
                    "* 'XStudio_Xbatch': Production/plant process evidence, heats, EAF, CCM, billets, work orders, SAP process data.\n"
                    "* 'XStudio_Helpdesk': Helpdesk tickets, Hermes runs, Helpdesk workflow status, activity timeline.\n"
                    "* 'XStudio_Configuration_Xbatch': XStudio configuration metadata.\n"
                    "Do NOT query XStudio_Helpdesk for plant/EAF/heat data."
                )
            },
            "table": {
                "type": "string",
                "description": "Target table or view name (e.g. 'dbo.EAF_PER_HEAT'). REQUIRED for: select, probe_table, validate_identifiers."
            },
            "columns": {
                "type": "array",
                "items": {"type": "string"},
                "description": "List of real column names to project. REQUIRED for: select. (Must be real columns; use find_objects or validate_identifiers first; do NOT pass wildcards or subqueries)."
            },
            "sql": {
                "type": "string",
                "description": "Read-only SELECT query string. REQUIRED for: query. (Write/DDL/EXEC statements are strictly blocked)."
            },
            "search": {
                "type": "string",
                "description": "Search keyword for table or object discovery. REQUIRED for: suggest_tables, find_objects."
            },
            "object_name": {
                "type": "string",
                "description": "Name of the SQL object to inspect. REQUIRED for: get_definition."
            },
            "schema": {
                "type": "string",
                "description": "Schema name for get_definition (defaults to 'dbo')."
            },
            "object_type": {
                "type": "string",
                "enum": ["TABLE", "VIEW", "PROCEDURE", "TRIGGER"],
                "description": "Optional filter for find_objects."
            },
            "identifiers": {
                "type": "array",
                "items": {"type": "string"},
                "description": "List of column names to validate against allowlist. REQUIRED for: validate_identifiers."
            },
            "procedure": {
                "type": "string",
                "description": "Allowlisted diagnostic procedure name ('XMES_Get_API_Transaction_Summary'). REQUIRED for: read_procedure."
            },
            "parameters": {
                "type": "object",
                "description": "Parameter object matching procedure allowlist contract (e.g. {'APIType': '...'}). REQUIRED for: read_procedure."
            },
            "run_id": {
                "type": "string",
                "description": "Active Hermes run UUID (given at the top of this task's body). REQUIRED for: select, query, probe_table, get_run_actions, save_ledger, read_procedure -- every read that returns evidence must be attributable in the run's own action audit trail."
            },
            "ticket_id": {
                "type": "string",
                "description": "Helpdesk ticket UUID. REQUIRED for: get_ticket_context."
            },
            "ticket": {
                "type": "object",
                "description": "Ticket context object containing fields like HeatNo/Description. REQUIRED for: probe_table."
            },
            "matched_columns": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Optional column names for probe_table."
            },
            "ledger": {
                "type": "object",
                "description": "Structured investigation ledger object to persist. REQUIRED for: save_ledger."
            },
            "where": {
                "type": "string",
                "description": "Optional WHERE clause condition for select (e.g. \"[HeatNo] = N'1604015'\")."
            },
            "order_by": {
                "type": "string",
                "description": "Optional ORDER BY clause for select."
            },
            "top": {
                "type": "integer",
                "minimum": 1,
                "maximum": 100,
                "description": "Optional maximum rows to return (default 20, max 100)."
            }
        },
        "required": ["operation"],
        "additionalProperties": False
    }
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
