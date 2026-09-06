"""xstudio-l2-learning — thin supplemental GBrain recall for Hermes L2 workers.

Hermes owns sessions, skills, tool execution and memory-provider plumbing. This
plugin adds only Chitragupta's trust-scoped organizational recall tool.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

for _helper_dir in (
    Path(__file__).resolve().parent.parent,
    Path.home() / ".hermes" / "profiles" / "l2-investigator" / "scripts",
):
    if str(_helper_dir) not in sys.path:
        sys.path.insert(0, str(_helper_dir))

from l2_gbrain import SCOPE_SOURCES, available as gbrain_available, search as gbrain_search  # noqa: E402

TOOLSET = "l2_learning"
RECALL_TOOL = "l2_recall"

_SCOPE_POLICY = {
    "trusted": "Governed reference only; verify current-ticket claims live.",
    "knowledge": "Canonical reference only; verify current-ticket state live.",
    "facts": "Reviewed reusable facts; verify applicability live.",
    "solutions": "Governed reusable solutions; verify applicability live.",
    "cases": "Historical outcomes are analogies/counterexamples, not proof.",
    "approved_cases": "Prior success is not proof for this ticket.",
    "rejected_cases": "Reviewer-rejected history is a negative example.",
    "reopened_cases": "Reopened history is a regression warning.",
    "sessions": "Raw history may contain mistakes; use only as a lead.",
    "candidates": "Unreviewed candidates are not facts.",
    "all": "Mixed trust search; classify and verify every result.",
}


def _recall(params: dict[str, Any]) -> str:
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
    return json.dumps({
        "ok": True,
        "backend": "gbrain",
        "scope": scope,
        "source_ids": result.get("source_ids") or [],
        "warning": _SCOPE_POLICY[scope],
        "results": result.get("results") or [],
        "live_verification_required": True,
    }, ensure_ascii=False, default=str)


_RECALL_SCHEMA = {
    "name": RECALL_TOOL,
    "description": "Search Chitragupta's GBrain knowledge/history sources. Read-only; current-ticket claims still require live xstudio_l2 evidence.",
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
        name=RECALL_TOOL,
        toolset=TOOLSET,
        schema=_RECALL_SCHEMA,
        handler=lambda params, **_: _recall(params),
        description="Read-only trust-scoped GBrain recall.",
    )
