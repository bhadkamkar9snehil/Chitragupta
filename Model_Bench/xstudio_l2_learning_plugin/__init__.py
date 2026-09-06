"""xstudio-l2-learning — supplemental read-only recall + unverified session capture.

Automatic governed context is assembled by the deterministic L2 harness before a
worker starts. This plugin therefore owns no automatic prefetch and no durable
knowledge writes. The only model-facing operation is supplemental ``l2_recall``
for new identifiers/signals discovered during investigation. Completed turns are
redacted and archived as ``unverified_episodic`` experience.
"""
from __future__ import annotations

import json
import os
import re
import sys
import threading
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

PLUGIN_NAME = "xstudio-l2-learning"
TOOLSET = "l2_learning"
RECALL_TOOL = "l2_recall"
DEFAULT_VAULT = Path.home() / ".hermes" / "l2-learning"
MAX_QUERY_CHARS = max(100, int(os.environ.get("L2_LEARNING_MAX_QUERY_CHARS", "600")))
MAX_RESULT_CHARS = max(1000, int(os.environ.get("L2_LEARNING_MAX_RESULT_CHARS", "7000")))
MAX_TURN_CHARS = max(4000, int(os.environ.get("L2_LEARNING_MAX_TURN_CHARS", "65536")))

for _helper_dir in (
    Path(__file__).resolve().parent.parent,
    Path.home() / ".hermes" / "profiles" / "l2-investigator" / "scripts",
):
    if str(_helper_dir) not in sys.path:
        sys.path.insert(0, str(_helper_dir))
from l2_gbrain import SCOPE_SOURCES, available as _gbrain_available, search as _gbrain_search  # noqa: E402

_SECRET_PATTERNS = (
    re.compile(r"(--password\s+)(\S+|'[^']*'|\"[^\"]*\")", re.I),
    re.compile(r"(--pwd\s+)(\S+|'[^']*'|\"[^\"]*\")", re.I),
    re.compile(r"(PWD\s*=\s*)([^;'\"\s]+)", re.I),
    re.compile(r"(password\s*[:=]\s*)('[^']*'|\"[^\"]*\"|\S+)", re.I),
    re.compile(r"(MSSQL_MCP_PASSWORD\s*[:=]\s*)(\S+)", re.I),
    re.compile(r"(API_SERVER_KEY\s*[:=]\s*)(\S+)", re.I),
    re.compile(r"\b(sk-[A-Za-z0-9]{10,}|pk-lf-[A-Za-z0-9_-]{10,}|sk-lf-[A-Za-z0-9_-]{10,})\b"),
    re.compile(r"\b(eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,})\b"),
)
_TASK_RE = re.compile(r"\bt_[0-9a-f]{6,}\b")
_MY_TASK_ID = next((m.group(0) for arg in sys.argv if (m := _TASK_RE.search(str(arg)))), "")
_write_lock = threading.Lock()
_context_lock = threading.Lock()
_task_context: dict[str, str] = {}

_SCOPE_POLICY = {
    "trusted": ("mixed_trusted_reference", "Governed reference can guide diagnosis; current-ticket claims still require live verification."),
    "knowledge": ("canonical_reference_lead", "Canonical reference documents behavior, not this ticket's current state."),
    "facts": ("reviewed_operational_heuristic", "Promoted facts are reusable guidance, not ticket-specific proof."),
    "solutions": ("governed_reusable_solution", "Approved solutions require live applicability verification."),
    "cases": ("historical_outcome_evidence", "Historical outcomes are analogies/counterexamples only."),
    "approved_cases": ("reviewed_published_historical_case", "Prior success is not proof for this ticket."),
    "rejected_cases": ("reviewed_negative_example", "Reviewer-rejected history is a counterexample signal."),
    "reopened_cases": ("observed_resolution_regression", "Reopened history is a regression warning signal."),
    "sessions": ("unverified_episodic", "Raw sessions may contain mistakes or hallucinations; use only as a lead."),
    "candidates": ("unverified_candidate", "Candidates are explicitly unreviewed and never facts."),
    "all": ("mixed_untrusted", "Mixed search contains untrusted material; classify and verify every result."),
}


def _now() -> datetime:
    return datetime.now(timezone.utc)


def _stamp() -> str:
    return _now().strftime("%Y%m%d-%H%M%S-%f")


def _vault() -> Path:
    raw = os.environ.get("CHITRAGUPTA_L2_LEARNING_VAULT", "").strip()
    return Path(raw).expanduser() if raw else DEFAULT_VAULT


def _redact(text: str) -> str:
    out = text
    for pattern in _SECRET_PATTERNS:
        repl = (lambda m: m.group(1) + "[REDACTED]") if pattern.groups >= 2 else "[REDACTED]"
        out = pattern.sub(repl, out)
    return out


def _text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    try:
        return json.dumps(value, ensure_ascii=False, default=str)
    except Exception:
        return str(value)


def _bounded(text: str, limit: int) -> tuple[str, bool]:
    if len(text) <= limit:
        return text, False
    return text[:limit] + f"\n\n[TRUNCATED: original {len(text)} chars]\n", True


def _slug(value: str, fallback: str) -> str:
    out = re.sub(r"[^A-Za-z0-9._-]+", "-", value.strip()).strip("-").lower()
    return out[:80] or fallback


def _profile(kwargs: dict[str, Any]) -> str:
    return str(kwargs.get("profile") or os.environ.get("HERMES_PROFILE") or os.environ.get("HERMES_PROFILE_NAME") or "unknown-profile")


def _resolve_task_context() -> None:
    if not _MY_TASK_ID:
        return
    try:
        import subprocess
        result = subprocess.run(["hermes", "kanban", "show", _MY_TASK_ID, "--json"], capture_output=True, text=True, timeout=8)
        if result.returncode != 0:
            return
        data = json.loads(result.stdout or "{}")
        task = data.get("task") if isinstance(data.get("task"), dict) else data
        found = {"task_id": _MY_TASK_ID}
        for line in str(task.get("body") or "").splitlines():
            if ":" not in line:
                continue
            key, value = line.split(":", 1)
            key = key.strip().lower()
            if key in {"run_id", "ticket_id", "ticket_no", "pipeline_stage", "review_cycle", "context_sha256", "source_context_sha256"}:
                found[key] = value.strip()
        with _context_lock:
            _task_context.update(found)
    except Exception:
        return


def _context() -> dict[str, str]:
    with _context_lock:
        return dict(_task_context)


def _write_session_turn(**kwargs: Any) -> None:
    try:
        user = _redact(_text(kwargs.get("user_message")))
        assistant = _redact(_text(kwargs.get("assistant_response")))
        if not user and not assistant:
            return
        user, user_cut = _bounded(user, MAX_TURN_CHARS)
        assistant, assistant_cut = _bounded(assistant, MAX_TURN_CHARS)
        correlated = _context()
        vault = _vault()
        profile = _slug(_profile(kwargs), "unknown-profile")
        session = _slug(str(kwargs.get("session_id") or "unknown-session"), "unknown-session")
        turn = _slug(str(kwargs.get("turn_id") or _stamp()), _stamp())
        path = vault / "sessions" / _now().strftime("%Y-%m-%d") / profile / session / f"{turn}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        meta = {
            "kind": "l2_session_turn", "trust": "unverified_episodic", "recorded_at": _now().isoformat(),
            "profile": _profile(kwargs), "session_id": str(kwargs.get("session_id") or ""), "turn_id": str(kwargs.get("turn_id") or ""),
            "task_id": correlated.get("task_id") or _MY_TASK_ID or str(kwargs.get("task_id") or ""),
            "run_id": correlated.get("run_id", ""), "ticket_id": correlated.get("ticket_id", ""), "ticket_no": correlated.get("ticket_no", ""),
            "pipeline_stage": correlated.get("pipeline_stage", ""), "review_cycle": correlated.get("review_cycle", ""),
            "context_sha256": correlated.get("context_sha256", ""), "source_context_sha256": correlated.get("source_context_sha256", ""),
            "model": str(kwargs.get("model") or ""), "platform": str(kwargs.get("platform") or ""),
            "user_truncated": user_cut, "assistant_truncated": assistant_cut,
        }
        fm = "\n".join(f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in meta.items())
        body = f"---\n{fm}\n---\n\n# User\n\n{user}\n\n# Assistant\n\n{assistant}\n"
        with _write_lock:
            path.write_text(body, encoding="utf-8")
    except Exception:
        return


def _recall(params: dict[str, Any]) -> str:
    query = str(params.get("query") or "").strip()
    scope = str(params.get("scope") or "trusted")
    mode = str(params.get("mode") or "hybrid")
    if not query:
        return json.dumps({"ok": False, "error": "query is required", "retry_same_call": False})
    if scope not in SCOPE_SOURCES:
        return json.dumps({"ok": False, "error": f"unknown scope: {scope}", "retry_same_call": False})
    if mode not in {"hybrid", "deep", "fts", "vector"}:
        return json.dumps({"ok": False, "error": f"unknown mode: {mode}", "retry_same_call": False})
    try:
        limit = max(1, min(10, int(params.get("limit") or 5)))
    except (TypeError, ValueError):
        limit = 5
    if not _gbrain_available():
        return json.dumps({"ok": False, "error": "gbrain is not installed", "retry_same_call": False})
    result = _gbrain_search(query[:MAX_QUERY_CHARS], scope=scope, mode=mode, limit=limit)
    if not result.get("ok"):
        return json.dumps(result, ensure_ascii=False)
    serialized = json.dumps(result.get("results"), ensure_ascii=False, default=str)
    if len(serialized) > MAX_RESULT_CHARS:
        serialized = serialized[:MAX_RESULT_CHARS] + "...[results truncated]"
    trust, warning = _SCOPE_POLICY[scope]
    return json.dumps({
        "ok": True, "backend": "gbrain", "scope": scope, "source_ids": result.get("source_ids"),
        "requested_mode": result.get("requested_mode"), "effective_mode": result.get("effective_mode"),
        "trust": trust, "warning": warning, "results": serialized,
        "supplemental_recall": True, "automatic_context_already_provided": True,
        "live_verification_required": True,
    }, ensure_ascii=False)


_RECALL_SCHEMA = {
    "name": RECALL_TOOL,
    "description": "Supplemental trust-scoped GBrain recall for new signals discovered after harness context delivery. Read-only; current-ticket claims still require live verification.",
    "parameters": {"type": "object", "properties": {
        "query": {"type": "string"}, "scope": {"type": "string", "enum": list(SCOPE_SOURCES)},
        "mode": {"type": "string", "enum": ["hybrid", "deep", "fts", "vector"]},
        "limit": {"type": "integer", "minimum": 1, "maximum": 10}},
        "required": ["query"], "additionalProperties": False},
}


def register(ctx: Any) -> None:
    ctx.register_tool(name=RECALL_TOOL, toolset=TOOLSET, schema=_RECALL_SCHEMA, handler=lambda params, **kwargs: _recall(params), description="Supplemental read-only GBrain recall behind the Chitragupta trust contract.")
    ctx.register_hook("post_llm_call", _write_session_turn)
    if _MY_TASK_ID:
        threading.Thread(target=_resolve_task_context, daemon=True, name="l2-learning-task-context").start()
