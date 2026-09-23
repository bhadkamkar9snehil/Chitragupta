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
TOOLSET = "xstudio_l2"
# Investigator-only completion tool; reviewer profiles leave this toolset off.
SUBMIT_TOOLSET = "l2_submit"

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
# These are deliberately small model-facing schemas. The bridge still receives
# the old operation vocabulary internally, but the model never has to choose an
# operation or fill an unrelated union of arguments.
TOOL_SCHEMAS: dict[str, dict[str, Any]] = {
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
    "xstudio_read_table": _tool_schema(
        "Read one XStudio table or view for THIS ticket. Give only the table name: the harness "
        "filters by the ticket's own heat/work order/billet/document and picks the relevant "
        "columns. Each result carries an action_id for VERIFIED claims.",
        {"table": _STRING, "database": _DATABASE}, ("table",),
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
            "root_cause": {"type": "string", "description": "The established cause, when one was found. Feeds the governed knowledge base."},
            "resolution": {"type": "string", "description": "Required for RESOLUTION: the observed, verified outcome that answers or fixes the request. A diagnosis or proposed fix is not a resolution."},
        },
        ("response_type", "summary"),
    ),
}

_VALID_RESPONSE_TYPES = {"UPDATE", "QUESTION", "RESOLUTION", "L3_ESCALATION", "NEEDS_HUMAN_ACTION"}

TOOL_OPERATIONS: dict[str, str] = {
    "xstudio_get_ticket_context": "get_ticket_context",
    "xstudio_get_run_actions": "get_run_actions",
    "xstudio_save_ledger": "save_ledger",
    "xstudio_read_table": "probe_table",
    "xstudio_heat_context": "heat_context",
    "xstudio_sap_api_context": "sap_api_context",
    "xstudio_work_order_context": "work_order_context",
}
_REQUIRED_FIELDS_BY_TOOL = {
    name: tuple(schema["parameters"]["required"])
    for name, schema in TOOL_SCHEMAS.items()
}
_EFFECTIVE_REQUIRED_FIELDS_BY_TOOL: dict[str, tuple[str, ...]] = {
    "xstudio_get_ticket_context": ("ticket_id",),
    "xstudio_get_run_actions": ("run_id",),
    "xstudio_save_ledger": ("run_id", "ledger"),
    "xstudio_read_table": ("database", "run_id", "ticket_id", "table"),
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
    "review_cycle": re.compile(r"review_cycle\s*[:=]\s*(\d+)", re.IGNORECASE),
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
    "Use the named xstudio_* tools in the xstudio_l2 toolset instead. "
    "Do not retry this command with wrappers, timeouts, or a different shell."
)

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
    if operation in {"resolve_heat", "heat_context", "sap_api_context", "work_order_context", "probe_table"} and not effective.get("database"):
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
    if tool_name == "xstudio_save_ledger" and not isinstance(args.get("ledger"), dict):
        return "xstudio_save_ledger requires ledger as an object"
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


def _outcome_field_error(response_type: str, params: dict[str, Any]) -> Optional[str]:
    """Fields the deterministic publisher will require, checked while the worker can still add them."""
    if response_type == "RESOLUTION" and not str(params.get("resolution") or "").strip():
        return ("RESOLUTION requires resolution: state the observed, verified outcome. "
                "If you only diagnosed the problem, submit UPDATE or NEEDS_HUMAN_ACTION instead.")
    incomplete = str(params.get("evidence_status") or "").upper() != "COMPLETE"
    if response_type == "UPDATE" and incomplete and not str(params.get("next_investigation_step") or "").strip():
        return ("An incomplete UPDATE requires next_investigation_step naming a concrete new evidence check. "
                "If only the requester can unblock progress, use requester_question instead.")
    return None


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

    field_error = _outcome_field_error(response_type, params)
    if field_error:
        return json.dumps({"ok": False, "error": field_error, "retry_same_call": False}), None

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

    # evidence_status carries the gap for review; the reply stays requester-facing.
    reply_text = str(params.get("reply_text") or "").strip() or summary

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

    with _lock:
        _submitted_tasks.add(task_id)
    return json.dumps({
        "ok": True,
        "submitted": True,
        "response_type": response_type,
        "evidence_status": evidence_status,
        "claim_status": claim_status,
        "message": (
            f"Proposal submitted as {response_type} with {claim_status} claim. "
            "This task is now complete: stop here and do not call kanban_complete "
            "(the card is already closed). The reconciler handles review and publication."
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


_SUBMIT_REDIRECT = (
    "Do not complete with kanban_complete. Call xstudio_submit_proposal now with flat fields: "
    "response_type (RESOLUTION / UPDATE / QUESTION / L3_ESCALATION / NEEDS_HUMAN_ACTION), summary, "
    "claim_status plus action_id for verified facts (xstudio_get_run_actions lists them), "
    "resolution for RESOLUTION, next_investigation_step for an incomplete UPDATE, "
    "requester_question for QUESTION. The harness builds the structured proposal."
)
# Cards already closed by a successful xstudio_submit_proposal (worker task ids).
_submitted_tasks: set[str] = set()
# Empty investigator completions already redirected once, keyed by worker task/run.
_redirected_empty_completions: set[str] = set()


def _packaged_summary_metadata(metadata: dict[str, Any], summary: str) -> dict[str, Any]:
    """Last-resort packaging of a flat summary as an explicitly incomplete UPDATE."""
    return {**metadata,
            "response_type": "UPDATE",
            "reply_text": (
                "We are still investigating this ticket. Our findings so far are not yet "
                "confirmed against live data; we will update you once they are."
            ),
            "claims": [{"id": "summary-1", "claim": summary, "material": True,
                        "status": "UNVERIFIED", "evidence": []}],
            "contract_packaged_from_summary": True,
            "evidence_status": "INCOMPLETE",
            "investigator_notes": summary}


def _metadata_with_identity(args: dict[str, Any], context: dict[str, Any]) -> dict[str, Any]:
    """Model-supplied metadata with harness-known run/ticket identity filled in."""
    raw = args.get("metadata")
    metadata = dict(raw) if isinstance(raw, dict) else {}
    for field in ("run_id", "ticket_id"):
        if not metadata.get(field) and context.get(field):
            metadata[field] = context[field]
    return metadata


def _kanban_completion_metadata_guard(args: dict[str, Any], context: dict[str, Any]) -> dict[str, Any] | None:
    if context.get("pipeline_stage", "").lower() not in {"investigation", "rework"}:
        return None
    metadata = _metadata_with_identity(args, context)
    metadata.setdefault("claims_contract_version", 1)
    missing = [field for field in ("run_id", "ticket_id", "response_type", "reply_text", "claims")
               if metadata.get(field) in (None, "", [])]
    if not missing:
        return None
    # Qwen reliably fills the flat submit tool but not this nested contract. An empty
    # completion first gets one exact redirect: packaging it straight away turned real
    # verified findings into canned "INCOMPLETE" UPDATEs (55 of 132 live UPDATE rows).
    key = os.environ.get("HERMES_KANBAN_TASK") or str(metadata.get("run_id") or "")
    with _lock:
        first_attempt = key not in _redirected_empty_completions
        _redirected_empty_completions.add(key)
    if first_attempt:
        return {"action": "block", "message": "L2 completion contract: metadata is missing "
                + ", ".join(missing) + ". " + _SUBMIT_REDIRECT}
    summary = str(args.get("summary") or "").strip()
    if len(summary) >= MIN_SUBSTANTIVE_COMPLETION_CHARS and metadata.get("run_id") and metadata.get("ticket_id"):
        # Second empty attempt: preserve the finding rather than let a small model loop.
        return {"action": "modify", "args": {"metadata": _packaged_summary_metadata(metadata, summary)}}
    return {"action": "block", "message": "L2 completion contract: " + _SUBMIT_REDIRECT}


def _review_completion_metadata(args: dict[str, Any], context: dict[str, Any]) -> dict[str, Any] | None:
    """Deterministic audit record for a reviewer approval; the model supplies only its notes."""
    if context.get("pipeline_stage", "").lower() != "review":
        return None
    metadata = dict(args["metadata"]) if isinstance(args.get("metadata"), dict) else {}
    notes = str(args.get("summary") or args.get("result") or "").strip()
    lowered = notes.lower()
    # Same rule as l2_pipeline_runtime.is_reviewer_rejection.
    rejected = lowered.startswith("reject") or "rejected frozen proposal" in lowered
    record = {
        "review_decision": "REJECTED" if rejected else "APPROVED",
        "run_id": context.get("run_id"),
        "ticket_id": context.get("ticket_id"),
        "review_cycle": context.get("review_cycle"),
        "reviewed_by": "local_reviewer",
        "review_notes": notes[:2000],
        "recorded_by": "xstudio-l2-tools",
    }
    merged = {**{k: v for k, v in record.items() if v not in (None, "")}, **metadata}
    return None if merged == metadata else {"action": "modify", "args": {"metadata": merged}}


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
        with _lock:
            already_submitted = os.environ.get("HERMES_KANBAN_TASK", "") in _submitted_tasks
        if already_submitted:
            # Live: after a successful submit the model called kanban_complete and was
            # told to submit again, looping on an already-closed card.
            return {"action": "block", "message": (
                "Already done: xstudio_submit_proposal completed this card. Do not call any more tools; "
                "end the session now.")}
        result = _kanban_completion_metadata_guard(args, context) or _review_completion_metadata(args, context)
        if result is not None and result.get("action") == "block":
            return result
        repaired = {**args, **((result or {}).get("args") or {})}
        # A small model can select the right terminal Kanban action yet serialize an
        # empty object; Hermes then rejects it ("provide at least one of: summary").
        if not (repaired.get("summary") or repaired.get("result")):
            repaired["summary"] = "Task completed; use the structured task metadata and persisted evidence trail for details."
        return None if repaired == args else {"action": "modify", "args": repaired}

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


_SCRIPT_SUFFIXES = (".py", ".sh", ".ps1", ".bash")


def _script_authoring_guard(args: dict[str, Any], context: dict[str, Any]) -> dict[str, str] | None:
    """L2 workers cannot execute interpreters, so authoring a script is pure waste.

    Live 2026-09-23: 321 write_file calls in one morning, mostly parse_task.py /
    parse_proposal.py written to decode a spilled card, never runnable.
    """
    path = str(args.get("path") or args.get("file_path") or "").lower()
    if not context.get("pipeline_stage") or not path.endswith(_SCRIPT_SUFFIXES):
        return None
    return {
        "action": "block",
        "message": (
            "Scripts cannot run in an L2 session. The card already states the facts you need: "
            "run_id/ticket_id/pipeline_stage lines and, for reviews, the PROPOSAL DIGEST. "
            "Use the xstudio_* tools for evidence, then complete."
        ),
    }


def _pre_tool_call(tool_name: str, args: dict[str, Any] | None = None,
                   task_id: str = "", **kwargs: Any) -> dict[str, str] | None:
    args = args or {}
    session = _session_key(task_id, **kwargs)
    context = _context_for(session, kwargs)

    if tool_name in ("kanban_complete", "kanban_block", "terminal"):
        return _completion_guard(tool_name, args, context)
    if tool_name in ("write_file", "patch"):
        return _script_authoring_guard(args, context)

    # xstudio_submit_proposal does its own validation in _submit_proposal_handler
    # and is not a bridge/SQL tool, so it must not consume the investigation budget.
    if tool_name == "xstudio_submit_proposal":
        return None

    if tool_name not in TOOL_OPERATIONS:
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
    if tool_name not in TOOL_OPERATIONS:
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
        "You are the WRITER: the evidence is on the card. Finish with one "
        "xstudio_submit_proposal call; if the evidence does not answer the ticket, choose "
        "L3_ESCALATION, or QUESTION when only the requester can supply the missing identifier. "
    )
    return {
        "context": (
            "L2 EXECUTION CONTRACT: the harness owns every database read. Never write SQL, "
            "scripts or files. "
            f"{completion_contract}"
            "UPDATE needs next_investigation_step; RESOLUTION needs resolution and VERIFIED claims "
            "with action_id. "
            f"State: known_context={ids or 'none'}, live_calls_used={used}, "
            f"live_calls_remaining={max(0, MAX_TOOL_CALLS - used)}. "
            "After two identical tool failures, change the evidence path."
        )
    }


def register(ctx: Any) -> None:
    sys.path.insert(0, str(Path(BRIDGE_PATH).parent))  # l2_calltrace lives beside the bridge
    try:  # local call trace (Model_Bench/l2_calltrace.py); L2_CALLTRACE=0 disables
        import l2_calltrace
        l2_calltrace.install()
    except ImportError:
        pass
    for name, schema in TOOL_SCHEMAS.items():
        # Registry injects the actual name into the OpenAI schema. Keeping the
        # same toolset preserves the existing profile enablement boundary.
        ctx.register_tool(
            name=name,
            toolset=SUBMIT_TOOLSET if name == "xstudio_submit_proposal" else TOOLSET,
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
