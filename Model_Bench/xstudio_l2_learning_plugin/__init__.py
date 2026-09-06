"""xstudio-l2-learning — trust-scoped experience plane backed by GBrain.

Sessions are recorded. Generic automatic retrieval injection is not used.
GBrain is the derivative search/graph/synthesis substrate; Chitragupta keeps the
model-facing trust contract and live XStudio remains current-ticket truth.
"""
from __future__ import annotations

import hashlib
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
LESSON_TOOL = "l2_lesson"
DEFAULT_VAULT = Path.home() / ".hermes" / "l2-learning"
MAX_QUERY_CHARS = max(100, int(os.environ.get("L2_LEARNING_MAX_QUERY_CHARS", "600")))
MAX_RESULT_CHARS = max(1000, int(os.environ.get("L2_LEARNING_MAX_RESULT_CHARS", "7000")))
MAX_TURN_CHARS = max(4000, int(os.environ.get("L2_LEARNING_MAX_TURN_CHARS", "65536")))
MAX_LESSON_CHARS = max(500, int(os.environ.get("L2_LEARNING_MAX_LESSON_CHARS", "6000")))

# The helper is beside this plugin in the repo and in the shared investigator
# scripts directory after deployment. Keep source/scope routing in one module.
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
    "knowledge": ("canonical_reference_lead", "Git/skill reference documents behavior, not this ticket's current state."),
    "facts": ("reviewed_operational_heuristic", "Promoted operational facts are durable lessons, not ticket-specific proof."),
    "solutions": ("governed_reusable_solution", "Approved solutions are reusable guidance; verify applicability and current live evidence."),
    "cases": ("historical_outcome_evidence", "Historical cases contain positive, rejected and reopened outcomes. Use as analogies/counterexamples only."),
    "approved_cases": ("reviewed_published_historical_case", "Proposal passed independent review and publisher postconditions at that time; it is not a universal fix."),
    "rejected_cases": ("reviewed_negative_example", "Proposal was reviewer-rejected. This is a counterexample signal, not proof every statement was false."),
    "reopened_cases": ("observed_resolution_regression", "A prior resolution later left its recorded terminal status. Treat as a regression signal, not a diagnosis."),
    "sessions": ("unverified_episodic", "Sessions can contain mistakes, rejected hypotheses, stale state or hallucinations. Use only as a lead."),
    "candidates": ("unverified_candidate", "Candidates are explicitly unreviewed. Never treat them as facts."),
    "all": ("mixed_untrusted", "Mixed search includes historical cases, unverified sessions and candidates. Classify every result and verify live."),
}


def _now() -> datetime:
    return datetime.now(timezone.utc)


def _stamp() -> str:
    return _now().strftime("%Y%m%d-%H%M%S-%f")


def _vault() -> Path:
    raw = os.environ.get("CHITRAGUPTA_L2_LEARNING_VAULT", "").strip()
    return Path(raw).expanduser() if raw else DEFAULT_VAULT


def _ensure_layout() -> Path:
    vault = _vault()
    for rel in (
        "sessions", "cases/approved", "cases/rejected", "cases/reopened",
        "facts", "candidates", "knowledge", "solutions/approved",
        "actions/plans", "actions/candidates", "eval",
        "archive/candidates/promoted", "archive/candidates/rejected",
    ):
        (vault / rel).mkdir(parents=True, exist_ok=True)
    return vault


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
        result = subprocess.run(
            ["hermes", "kanban", "show", _MY_TASK_ID, "--json"],
            capture_output=True, text=True, timeout=8,
        )
        if result.returncode != 0:
            return
        data = json.loads(result.stdout or "{}")
        task = data.get("task") if isinstance(data.get("task"), dict) else data
        found = {"kanban_task_id": _MY_TASK_ID}
        for line in str(task.get("body") or "").splitlines():
            if ":" not in line:
                continue
            key, value = line.split(":", 1)
            key = key.strip().lower()
            if key in {"run_id", "ticket_id", "ticket_no", "pipeline_stage", "review_cycle"}:
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
        vault = _ensure_layout()
        profile = _slug(_profile(kwargs), "unknown-profile")
        session = _slug(str(kwargs.get("session_id") or "unknown-session"), "unknown-session")
        turn = _slug(str(kwargs.get("turn_id") or _stamp()), _stamp())
        path = vault / "sessions" / _now().strftime("%Y-%m-%d") / profile / session / f"{turn}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        correlated = _context()
        meta = {
            "kind": "l2_session_turn", "trust": "unverified_episodic", "recorded_at": _now().isoformat(),
            "profile": _profile(kwargs), "session_id": str(kwargs.get("session_id") or ""),
            "turn_id": str(kwargs.get("turn_id") or ""),
            "task_id": correlated.get("kanban_task_id") or _MY_TASK_ID or str(kwargs.get("task_id") or ""),
            "run_id": correlated.get("run_id", ""), "ticket_id": correlated.get("ticket_id", ""),
            "ticket_no": correlated.get("ticket_no", ""), "pipeline_stage": correlated.get("pipeline_stage", ""),
            "review_cycle": correlated.get("review_cycle", ""), "model": str(kwargs.get("model") or ""),
            "platform": str(kwargs.get("platform") or ""), "user_truncated": user_cut, "assistant_truncated": assistant_cut,
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
        "ok": True,
        "backend": "gbrain",
        "scope": scope,
        "source_ids": result.get("source_ids"),
        "requested_mode": result.get("requested_mode"),
        "effective_mode": result.get("effective_mode"),
        "trust": trust,
        "warning": warning,
        "results": serialized,
        "automatic_prefetch": False,
        "live_verification_required": True,
    }, ensure_ascii=False)


def _propose_lesson(params: dict[str, Any], **kwargs: Any) -> str:
    summary = _redact(str(params.get("summary") or "").strip())
    evidence = _redact(str(params.get("evidence") or "").strip())
    if not summary:
        return json.dumps({"ok": False, "error": "summary is required", "retry_same_call": False})
    if not evidence:
        return json.dumps({"ok": False, "error": "evidence is required; lessons without provenance are not accepted", "retry_same_call": False})
    kind = str(params.get("kind") or "operational_heuristic")
    allowed = {"operational_heuristic", "failure_pattern", "schema_fact", "workflow_lesson", "tool_lesson"}
    if kind not in allowed:
        return json.dumps({"ok": False, "error": f"unknown lesson kind: {kind}", "retry_same_call": False})
    summary, _ = _bounded(summary, MAX_LESSON_CHARS)
    evidence, _ = _bounded(evidence, MAX_LESSON_CHARS)
    vault = _ensure_layout()
    digest = hashlib.sha256((kind + "\0" + summary).encode()).hexdigest()[:12]
    path = vault / "candidates" / f"{_stamp()}-{_slug(kind, 'lesson')}-{digest}.md"
    correlated = _context()
    meta = {
        "kind": "l2_learning_candidate", "candidate_type": kind, "trust": "unverified_candidate",
        "created_at": _now().isoformat(), "profile": _profile(kwargs),
        "session_id": str(kwargs.get("session_id") or ""),
        "task_id": correlated.get("kanban_task_id") or _MY_TASK_ID or str(kwargs.get("task_id") or ""),
        "run_id": correlated.get("run_id", ""), "ticket_id": correlated.get("ticket_id", ""),
        "pipeline_stage": correlated.get("pipeline_stage", ""), "review_cycle": correlated.get("review_cycle", ""),
        "route": _redact(str(params.get("route") or "").strip()),
        "tags": _redact(str(params.get("tags") or "").strip()), "content_hash": digest,
    }
    fm = "\n".join(f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in meta.items())
    body = f"---\n{fm}\n---\n\n# Candidate lesson\n\n{summary}\n\n# Evidence / provenance\n\n{evidence}\n\n> This file is intentionally untrusted until promoted by the learning curator.\n"
    with _write_lock:
        path.write_text(body, encoding="utf-8")
    return json.dumps({
        "ok": True, "status": "candidate_recorded", "path": str(path),
        "trust": "unverified_candidate",
        "note": "Candidate only; promotion is a separate reviewed/outcome-gated operation.",
    }, ensure_ascii=False)


_RECALL_SCHEMA = {
    "name": RECALL_TOOL,
    "description": "Explicit trust-scoped GBrain recall. No automatic prefetch; current-ticket claims still require live verification.",
    "parameters": {"type": "object", "properties": {
        "query": {"type": "string"},
        "scope": {"type": "string", "enum": list(SCOPE_SOURCES)},
        "mode": {"type": "string", "enum": ["hybrid", "deep", "fts", "vector"]},
        "limit": {"type": "integer", "minimum": 1, "maximum": 10}},
        "required": ["query"], "additionalProperties": False},
}
_LESSON_SCHEMA = {
    "name": LESSON_TOOL,
    "description": "Record a reusable lesson only as an unverified candidate with explicit provenance.",
    "parameters": {"type": "object", "properties": {
        "operation": {"type": "string", "enum": ["propose"]},
        "kind": {"type": "string", "enum": ["operational_heuristic", "failure_pattern", "schema_fact", "workflow_lesson", "tool_lesson"]},
        "summary": {"type": "string"}, "evidence": {"type": "string"},
        "route": {"type": "string"}, "tags": {"type": "string"}},
        "required": ["summary", "evidence"], "additionalProperties": False},
}


def register(ctx: Any) -> None:
    ctx.register_tool(
        name=RECALL_TOOL, toolset=TOOLSET, schema=_RECALL_SCHEMA,
        handler=lambda params, **kwargs: _recall(params),
        description="Trust-scoped GBrain retrieval behind the Chitragupta safety contract.",
    )
    ctx.register_tool(
        name=LESSON_TOOL, toolset=TOOLSET, schema=_LESSON_SCHEMA,
        handler=lambda params, **kwargs: _propose_lesson(params, **kwargs)
        if str(params.get("operation") or "propose") == "propose"
        else json.dumps({"ok": False, "error": "only operation='propose' is model-accessible"}),
        description="Record an unverified reusable lesson candidate with provenance.",
    )
    ctx.register_hook("post_llm_call", _write_session_turn)
    if _MY_TASK_ID:
        threading.Thread(target=_resolve_task_context, daemon=True, name="l2-learning-task-context").start()
