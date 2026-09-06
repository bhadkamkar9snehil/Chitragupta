"""xstudio-l2-learning — shared experience/learning substrate for Chitragupta.

This is intentionally NOT a Hermes MemoryProvider. mem0 remains free to serve as
compact operational memory. This plugin does two different jobs:

1. Record every completed L2 turn as redacted, provenance-rich episodic Markdown.
2. Expose explicit, scoped hybrid recall through zvec-grep.

There is deliberately no automatic prefetch. Recording experience and granting it
epistemic authority are different acts. Session material is useful for failure
mining, replay, evaluation, and "have we seen this shape before?" searches, but it
must never be injected into every prompt as if an old assistant statement were a
fact.

The vault is shared across L2 profiles by default:
    ~/.hermes/l2-learning/
      sessions/              unverified episodic turn records
      facts/                 reviewed operational lessons
      candidates/            model-proposed, untrusted lessons
      knowledge/             mirrored canonical Git/skill reference corpus
      solutions/approved/    reserved for governed SQL Solution exports
      archive/               rejected/superseded learning artifacts
      .zvec-grep/            disposable local search index

zvec-grep is a disposable retrieval index. Source authority remains with live SQL,
Git knowledge, governed Solution articles, and explicit promotion records.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
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
DEFAULT_ZG = "zg"
QUERY_TIMEOUT_SECONDS = max(10, int(os.environ.get("L2_LEARNING_QUERY_TIMEOUT", "60")))
MAX_QUERY_CHARS = max(100, int(os.environ.get("L2_LEARNING_MAX_QUERY_CHARS", "600")))
MAX_RESULT_CHARS = max(1000, int(os.environ.get("L2_LEARNING_MAX_RESULT_CHARS", "7000")))
MAX_TURN_CHARS = max(4000, int(os.environ.get("L2_LEARNING_MAX_TURN_CHARS", "65536")))
MAX_LESSON_CHARS = max(500, int(os.environ.get("L2_LEARNING_MAX_LESSON_CHARS", "6000")))

_SECRET_PATTERNS = (
    re.compile(r"(--password\s+)(\S+|'[^']*'|\"[^\"]*\")", re.IGNORECASE),
    re.compile(r"(--pwd\s+)(\S+|'[^']*'|\"[^\"]*\")", re.IGNORECASE),
    re.compile(r"(PWD\s*=\s*)([^;'\"\s]+)", re.IGNORECASE),
    re.compile(r"(password\s*[:=]\s*)('[^']*'|\"[^\"]*\"|\S+)", re.IGNORECASE),
    re.compile(r"(MSSQL_MCP_PASSWORD\s*[:=]\s*)(\S+)", re.IGNORECASE),
    re.compile(r"(API_SERVER_KEY\s*[:=]\s*)(\S+)", re.IGNORECASE),
    re.compile(r"\b(sk-[A-Za-z0-9]{10,}|pk-lf-[A-Za-z0-9_-]{10,}|sk-lf-[A-Za-z0-9_-]{10,})\b"),
    re.compile(r"\b(eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,})\b"),
)

_KANBAN_TASK_ID_RE = re.compile(r"\bt_[0-9a-f]{6,}\b")
_MY_KANBAN_TASK_ID = ""
for _arg in sys.argv:
    _m = _KANBAN_TASK_ID_RE.search(str(_arg))
    if _m:
        _MY_KANBAN_TASK_ID = _m.group(0)
        break

_write_lock = threading.Lock()
_task_context_lock = threading.Lock()
_task_context: dict[str, str] = {}

_SCOPE_GLOBS: dict[str, list[str]] = {
    "trusted": ["knowledge/**", "facts/**", "solutions/approved/**"],
    "knowledge": ["knowledge/**"],
    "facts": ["facts/**"],
    "solutions": ["solutions/approved/**"],
    "sessions": ["sessions/**"],
    "candidates": ["candidates/**"],
    "all": [],
}

_SCOPE_POLICY = {
    "trusted": (
        "mixed_trusted_reference",
        "Reference/approved material can guide diagnosis, but current-ticket claims still require live verification.",
    ),
    "knowledge": (
        "canonical_reference_lead",
        "Git/skill reference is authoritative for documented behavior, not proof of this ticket's current state.",
    ),
    "facts": (
        "reviewed_operational_heuristic",
        "Operational facts are durable lessons, not ticket-specific proof.",
    ),
    "solutions": (
        "governed_reusable_solution",
        "Approved solutions are reusable guidance; verify applicability and current live evidence before reuse.",
    ),
    "sessions": (
        "unverified_episodic",
        "Session recall may contain mistakes, rejected hypotheses, stale state, or hallucinated assistant claims. Use only as a lead.",
    ),
    "candidates": (
        "unverified_candidate",
        "Candidates are explicitly unreviewed. Never treat them as facts.",
    ),
    "all": (
        "mixed_untrusted",
        "Mixed search includes unverified sessions/candidates. Every result must be classified by path and independently verified.",
    ),
}


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


def _stamp() -> str:
    return _utc_now().strftime("%Y%m%d-%H%M%S-%f")


def _vault() -> Path:
    raw = os.environ.get("CHITRAGUPTA_L2_LEARNING_VAULT", "").strip()
    return Path(raw).expanduser() if raw else DEFAULT_VAULT


def _zg() -> str:
    return os.environ.get("CHITRAGUPTA_ZG_BIN", DEFAULT_ZG).strip() or DEFAULT_ZG


def _redact(text: str) -> str:
    value = text
    for pattern in _SECRET_PATTERNS:
        if pattern.groups >= 2:
            value = pattern.sub(lambda m: m.group(1) + "[REDACTED]", value)
        else:
            value = pattern.sub("[REDACTED]", value)
    return value


def _as_text(value: Any) -> str:
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


def _safe_slug(value: str, fallback: str = "item") -> str:
    slug = re.sub(r"[^A-Za-z0-9._-]+", "-", value.strip()).strip("-").lower()
    return slug[:80] or fallback


def _ensure_layout() -> Path:
    vault = _vault()
    for rel in (
        "sessions",
        "facts",
        "candidates",
        "knowledge",
        "solutions/approved",
        "archive/candidates/promoted",
        "archive/candidates/rejected",
    ):
        (vault / rel).mkdir(parents=True, exist_ok=True)
    return vault


def _profile_name(kwargs: dict[str, Any]) -> str:
    return str(
        kwargs.get("profile")
        or os.environ.get("HERMES_PROFILE")
        or os.environ.get("HERMES_PROFILE_NAME")
        or "unknown-profile"
    )


def _resolve_task_context() -> None:
    """Best-effort correlation of this worker process to L2 run/ticket metadata.

    Hermes hook task_id is session-shaped for top-level Kanban workers in the
    deployed version, so—as in xstudio-l2-trace—we read the real t_xxx id from
    argv and resolve the card once in a background thread. Session capture never
    waits on this lookup.
    """
    if not _MY_KANBAN_TASK_ID:
        return
    try:
        result = subprocess.run(
            ["hermes", "kanban", "show", _MY_KANBAN_TASK_ID, "--json"],
            capture_output=True,
            text=True,
            timeout=8,
        )
        if result.returncode != 0:
            return
        data = json.loads(result.stdout or "{}")
        task = data.get("task") if isinstance(data.get("task"), dict) else data
        body = str(task.get("body") or "")
        found: dict[str, str] = {"kanban_task_id": _MY_KANBAN_TASK_ID}
        for line in body.splitlines():
            if ":" not in line:
                continue
            key, value = line.split(":", 1)
            key = key.strip().lower()
            if key in {"run_id", "ticket_id", "ticket_no", "pipeline_stage", "review_cycle"}:
                found[key] = value.strip()
        with _task_context_lock:
            _task_context.update(found)
    except Exception:
        return


def _task_context_snapshot() -> dict[str, str]:
    with _task_context_lock:
        return dict(_task_context)


def _write_session_turn(**kwargs: Any) -> None:
    """Record one completed LLM turn as unverified episodic experience.

    One file per turn avoids cross-process append races across the four active
    Hermes profile processes. Tool-by-tool execution evidence remains in the
    existing xstudio-l2-trace pipeline; this archive records conversational
    intent/outcome for later replay and learning.
    """
    try:
        user = _redact(_as_text(kwargs.get("user_message")))
        assistant = _redact(_as_text(kwargs.get("assistant_response")))
        if not user and not assistant:
            return
        user, user_truncated = _bounded(user, MAX_TURN_CHARS)
        assistant, assistant_truncated = _bounded(assistant, MAX_TURN_CHARS)

        vault = _ensure_layout()
        profile = _safe_slug(_profile_name(kwargs), "unknown-profile")
        session = _safe_slug(str(kwargs.get("session_id") or "unknown-session"), "unknown-session")
        turn = _safe_slug(str(kwargs.get("turn_id") or _stamp()), _stamp())
        day = _utc_now().strftime("%Y-%m-%d")
        out_dir = vault / "sessions" / day / profile / session
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"{turn}.md"

        correlated = _task_context_snapshot()
        task_id = correlated.get("kanban_task_id") or _MY_KANBAN_TASK_ID or str(kwargs.get("task_id") or "")
        meta = {
            "kind": "l2_session_turn",
            "trust": "unverified_episodic",
            "recorded_at": _utc_now().isoformat(),
            "profile": _profile_name(kwargs),
            "session_id": str(kwargs.get("session_id") or ""),
            "turn_id": str(kwargs.get("turn_id") or ""),
            "task_id": task_id,
            "run_id": correlated.get("run_id", ""),
            "ticket_id": correlated.get("ticket_id", ""),
            "ticket_no": correlated.get("ticket_no", ""),
            "pipeline_stage": correlated.get("pipeline_stage", ""),
            "review_cycle": correlated.get("review_cycle", ""),
            "model": str(kwargs.get("model") or ""),
            "platform": str(kwargs.get("platform") or ""),
            "user_truncated": user_truncated,
            "assistant_truncated": assistant_truncated,
        }
        frontmatter = "\n".join(f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in meta.items())
        body = (
            "---\n"
            f"{frontmatter}\n"
            "---\n\n"
            "# User\n\n"
            f"{user}\n\n"
            "# Assistant\n\n"
            f"{assistant}\n"
        )
        with _write_lock:
            path.write_text(body, encoding="utf-8")
    except Exception:
        return


def _post_llm_call(**kwargs: Any) -> None:
    _write_session_turn(**kwargs)


def _index_ready(vault: Path) -> bool:
    return (vault / ".zvec-grep" / "manifest.json").exists()


def _run_zg(args: list[str], timeout: int = QUERY_TIMEOUT_SECONDS) -> tuple[int, str, str]:
    try:
        proc = subprocess.run(
            [_zg(), *args],
            cwd=str(_ensure_layout()),
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        return proc.returncode, proc.stdout or "", proc.stderr or ""
    except FileNotFoundError:
        return 127, "", "zg not found; install @zvec/zvec-grep (Node.js 22+)"
    except subprocess.TimeoutExpired:
        return 124, "", "zg query timed out"


def _recall(params: dict[str, Any]) -> str:
    query = str(params.get("query") or "").strip()
    if not query:
        return json.dumps({"ok": False, "error": "query is required", "retry_same_call": False})
    scope = str(params.get("scope") or "trusted")
    if scope not in _SCOPE_GLOBS:
        return json.dumps({"ok": False, "error": f"unknown scope: {scope}", "retry_same_call": False})
    mode = str(params.get("mode") or "hybrid")
    if mode not in {"hybrid", "fts", "vector"}:
        return json.dumps({"ok": False, "error": f"unknown mode: {mode}", "retry_same_call": False})
    try:
        limit = max(1, min(10, int(params.get("limit") or 5)))
    except (TypeError, ValueError):
        limit = 5

    vault = _ensure_layout()
    if not shutil.which(_zg()):
        return json.dumps({
            "ok": False,
            "error": "zvec-grep is not installed; run the branch deployment prerequisites first",
            "retry_same_call": False,
        })
    if not _index_ready(vault):
        return json.dumps({
            "ok": False,
            "error": "learning index is not ready; run sync_l2_learning_corpus.py and build the zvec index",
            "retry_same_call": False,
        })

    q = query[:MAX_QUERY_CHARS]
    cmd = ["query", "--mode", "auto", "--refresh", "background", "--preview", "short", "--limit", str(limit)]
    if mode == "fts":
        cmd += ["--fts", q]
    elif mode == "vector":
        cmd += ["--vector", q]
    else:
        cmd += [q]
    for glob in _SCOPE_GLOBS[scope]:
        cmd += ["-g", glob]

    rc, out, err = _run_zg(cmd)
    if rc != 0:
        return json.dumps({
            "ok": False,
            "error": f"zg query failed: {(err or out).strip()[-800:]}",
            "retry_same_call": False,
        })
    result = out.strip()
    if len(result) > MAX_RESULT_CHARS:
        result = result[:MAX_RESULT_CHARS].rsplit("\n", 1)[0] + "\n...[results truncated]"
    trust, warning = _SCOPE_POLICY[scope]
    return json.dumps({
        "ok": True,
        "scope": scope,
        "trust": trust,
        "warning": warning,
        "results": result,
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

    route = _redact(str(params.get("route") or "").strip())
    tags = _redact(str(params.get("tags") or "").strip())
    summary, _ = _bounded(summary, MAX_LESSON_CHARS)
    evidence, _ = _bounded(evidence, MAX_LESSON_CHARS)

    vault = _ensure_layout()
    digest = hashlib.sha256((kind + "\0" + summary).encode("utf-8")).hexdigest()[:12]
    path = vault / "candidates" / f"{_stamp()}-{_safe_slug(kind)}-{digest}.md"
    correlated = _task_context_snapshot()
    meta = {
        "kind": "l2_learning_candidate",
        "candidate_type": kind,
        "trust": "unverified_candidate",
        "created_at": _utc_now().isoformat(),
        "profile": _profile_name(kwargs),
        "session_id": str(kwargs.get("session_id") or ""),
        "task_id": correlated.get("kanban_task_id") or _MY_KANBAN_TASK_ID or str(kwargs.get("task_id") or ""),
        "run_id": correlated.get("run_id", ""),
        "ticket_id": correlated.get("ticket_id", ""),
        "pipeline_stage": correlated.get("pipeline_stage", ""),
        "review_cycle": correlated.get("review_cycle", ""),
        "route": route,
        "tags": tags,
        "content_hash": digest,
    }
    frontmatter = "\n".join(f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in meta.items())
    body = (
        "---\n" + frontmatter + "\n---\n\n"
        "# Candidate lesson\n\n" + summary + "\n\n"
        "# Evidence / provenance\n\n" + evidence + "\n\n"
        "> This file is intentionally untrusted until promoted by the learning curator.\n"
    )
    with _write_lock:
        path.write_text(body, encoding="utf-8")
    return json.dumps({
        "ok": True,
        "status": "candidate_recorded",
        "path": str(path),
        "trust": "unverified_candidate",
        "note": "Recording a candidate does not make it memory or KB. Promotion is a separate reviewed/outcome-gated step.",
    }, ensure_ascii=False)


def _lesson_handler(params: dict[str, Any], **kwargs: Any) -> str:
    operation = str(params.get("operation") or "propose")
    if operation != "propose":
        return json.dumps({"ok": False, "error": "only operation='propose' is model-accessible"})
    return _propose_lesson(params, **kwargs)


_RECALL_SCHEMA = {
    "name": RECALL_TOOL,
    "description": (
        "Explicit hybrid recall over Chitragupta's shared learning vault. No results are injected automatically. "
        "Use scope='trusted' for normal prior knowledge; use scope='sessions' only to look for historical patterns/dead ends, "
        "never as proof. Every returned scope includes its trust policy and still requires live verification for ticket claims."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "query": {"type": "string"},
            "scope": {"type": "string", "enum": ["trusted", "knowledge", "facts", "solutions", "sessions", "candidates", "all"]},
            "mode": {"type": "string", "enum": ["hybrid", "fts", "vector"]},
            "limit": {"type": "integer", "minimum": 1, "maximum": 10},
        },
        "required": ["query"],
        "additionalProperties": False,
    },
}

_LESSON_SCHEMA = {
    "name": LESSON_TOOL,
    "description": (
        "Propose a durable lesson learned during this ticket. This writes only an UNVERIFIED candidate with provenance; "
        "it does not become trusted memory/KB until separately promoted. Use for genuinely reusable operational, failure, "
        "schema, workflow, or tool lessons — never for ticket IDs or one-off incident facts."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "operation": {"type": "string", "enum": ["propose"]},
            "kind": {"type": "string", "enum": ["operational_heuristic", "failure_pattern", "schema_fact", "workflow_lesson", "tool_lesson"]},
            "summary": {"type": "string"},
            "evidence": {"type": "string"},
            "route": {"type": "string"},
            "tags": {"type": "string"},
        },
        "required": ["summary", "evidence"],
        "additionalProperties": False,
    },
}


def register(ctx: Any) -> None:
    ctx.register_tool(
        name=RECALL_TOOL,
        toolset=TOOLSET,
        schema=_RECALL_SCHEMA,
        handler=lambda params, **kwargs: _recall(params),
        description="Scoped zvec hybrid recall with explicit trust semantics.",
    )
    ctx.register_tool(
        name=LESSON_TOOL,
        toolset=TOOLSET,
        schema=_LESSON_SCHEMA,
        handler=_lesson_handler,
        description="Record an unverified reusable lesson candidate with provenance.",
    )
    # Session recording is intentionally ON. Automatic recall/prefetch is
    # intentionally absent: storage != authority.
    ctx.register_hook("post_llm_call", _post_llm_call)

    # Resolve task/run/ticket correlation once, off the hook hot path. The worker
    # session typically lasts minutes, so metadata is available by final turn.
    if _MY_KANBAN_TASK_ID:
        threading.Thread(target=_resolve_task_context, daemon=True, name="l2-learning-task-context").start()
