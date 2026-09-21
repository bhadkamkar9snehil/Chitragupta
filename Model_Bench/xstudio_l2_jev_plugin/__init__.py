"""Hermes plugin exposing bounded Chitragupta Jev workflows.

This is intentionally not a generic "ask Jev anything" tool. Each operation
maps to a reviewed System-One workflow owned by Model_Bench/jev.
"""
from __future__ import annotations

import json
import subprocess
import threading
from collections import defaultdict
from pathlib import Path
from typing import Any

TOOL_NAME = "xstudio_jev"
TOOLSET = "xstudio_jev"
WINDOWS_PYTHON = "/mnt/c/Python314/python.exe"
BRIDGE_WIN = r"C:\Users\Admin\Documents\Office\AIHelpdesk\Model_Bench\jev_workflow_bridge.py"
MAX_CALLS = 10

_lock = threading.Lock()
_session_calls: dict[str, int] = defaultdict(int)


def _session_key(task_id: str = "", **kwargs: Any) -> str:
    return str(task_id or kwargs.get("session_id") or kwargs.get("conversation_id") or "default")


def _invoke(params: dict[str, Any]) -> str:
    try:
        proc = subprocess.run(
            [WINDOWS_PYTHON, BRIDGE_WIN],
            input=json.dumps(params, separators=(",", ":"), default=str),
            capture_output=True,
            text=True,
            timeout=45,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return json.dumps({
            "ok": False,
            "error": f"Jev bridge transport failed: {type(exc).__name__}: {exc}",
            "retry_same_call": False,
        })
    text = (proc.stdout or "").strip()
    if not text:
        return json.dumps({
            "ok": False,
            "error": (proc.stderr or f"bridge exited {proc.returncode}").strip()[:1200],
            "retry_same_call": False,
        })
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        parsed = {"ok": False, "error": "Jev bridge returned non-JSON output", "retry_same_call": False}
    return json.dumps(parsed, separators=(",", ":"), default=str)


def _handler(params: dict[str, Any], **kwargs: Any) -> str:
    del kwargs
    return _invoke(params)


def _pre_tool_call(tool_name: str, args: dict[str, Any] | None = None,
                   task_id: str = "", **kwargs: Any) -> dict[str, str] | None:
    del args
    if tool_name != TOOL_NAME:
        return None
    session = _session_key(task_id, **kwargs)
    with _lock:
        count = _session_calls[session]
        if count >= MAX_CALLS:
            return {
                "action": "block",
                "message": (
                    "Jev workflow budget exhausted. Stop re-asking semantic questions. "
                    "Use the judgments already returned, gather one missing live fact if needed, "
                    "then complete the task."
                ),
            }
        _session_calls[session] = count + 1
    return None


def _cleanup(task_id: str = "", **kwargs: Any) -> None:
    session = _session_key(task_id, **kwargs)
    with _lock:
        _session_calls.pop(session, None)


def _pre_llm_call(**kwargs: Any) -> dict[str, str]:
    del kwargs
    return {
        "context": (
            "JEV COORDINATOR CONTRACT: use xstudio_jev for bounded semantic judgments; "
            "do not reproduce those classifications with free-form reasoning. Use xstudio_l2 "
            "only for the small set of live reads Jev/evidence planning identifies. Jev output "
            "is typed evidence, not permission to mutate or publish. Deterministic lifecycle "
            "code owns ticket state and publication."
        )
    }


_SCHEMA = {
    "name": TOOL_NAME,
    "description": (
        "Bounded TypeSafe Jev/System-One workflows for Chitragupta. "
        "No arbitrary prompts; choose a reviewed workflow operation."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "workflow": {"type": "string", "enum": [
                "ticket_triage", "evidence_plan", "investigation_assessment",
                "primary_review", "proposal_preflight", "review_risk",
                "candidate_rerank", "kb_applicability", "kb_curation",
                "trace_assessment", "security", "security_batch",
                "model_routing", "l1_action"
            ]},
            "state": {"type": "object"},
            "ticket": {"type": "object"},
            "manifest": {"type": "object"},
            "allowed_routes": {"type": "array", "items": {"type": "string"}},
            "query": {"type": "string"},
            "candidates": {"type": "array", "items": {"type": "object"}},
            "known_solutions": {"type": "array", "items": {"type": "object"}},
            "candidate_kind": {"type": "string"},
            "top": {"type": "integer", "minimum": 1, "maximum": 100},
            "source": {"type": "string"},
            "items": {"type": "array", "items": {"type": "object"}},
            "profiles": {"type": "object"},
            "actions": {"type": "object"},
            "ticket_id": {"type": "string"},
            "run_id": {"type": "string"},
            "audit_stage": {"type": "string"},
            "question_version": {"type": "string"},
            "accepted": {"type": "boolean"}
        },
        "required": ["workflow"],
        "additionalProperties": False
    }
}


def register(ctx: Any) -> None:
    ctx.register_tool(
        name=TOOL_NAME,
        toolset=TOOLSET,
        schema=_SCHEMA,
        handler=_handler,
        description="Bounded Chitragupta TypeSafe Jev workflows.",
    )
    ctx.register_hook("pre_tool_call", _pre_tool_call)
    ctx.register_hook("pre_llm_call", _pre_llm_call)
    ctx.register_hook("on_session_end", _cleanup)
    ctx.register_hook("on_session_finalize", _cleanup)
    ctx.register_hook("on_session_reset", _cleanup)
