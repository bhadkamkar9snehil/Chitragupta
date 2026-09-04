"""xstudio-l2-trace -- Hermes observer-hook plugin for the AI Helpdesk /
Hermes L2 project.

Why this exists (2026-09-04): the user wants full agent traces "properly
written in Helpdesk" -- not a third-party SaaS dashboard, the actual
XStudio Helpdesk product. Confirmed live that `Hermes_L2_SQL_Action_Trn_Tbl`
(the one existing audit table) only ever captures SQL reads/writes the
model explicitly chose to route through `--query`/`Hermes_L2_Execute_SQL_Usp`
-- it has no idea what OTHER tools the model called, what arguments it used,
whether a call errored, or how long anything took. Hermes's own observer-hook
contract (docs/observability/README.md) already exposes exactly this at the
platform layer, unconditionally, regardless of what the model remembers to
log itself -- the same category of fix already applied to the kanban
staleness logic this session (stop trusting the model's own narration,
consult ground truth instead).

Design: hook callbacks must stay cheap (Hermes gates expensive payload
construction behind `has_hook(...)`, and a slow hook blocks the agent loop).
This plugin does the minimum possible work per call -- serialize a small
dict, append one line to a local JSONL file under a lock -- and never
touches the network or a database directly. `pyodbc` is not usable in this
venv at all (confirmed live: `ImportError: libodbc.so.2` -- no ODBC driver
manager installed in this WSL environment), which independently rules out
writing to SQL Server from inside the hook. A separate, existing-pattern
cron job (Model_Bench/drain_l2_trace_log.py, invoked via the Windows Python
interpreter that already has a working ODBC driver) drains this file into
XStudio_Helpdesk.dbo.Hermes_Agent_Trace_Trn_Tbl on its own schedule,
decoupled from the hot path.

Captured events: pre_tool_call / post_tool_call (every tool the model
calls, args, result, status, duration, error), post_api_request and
api_request_error (model/provider, token usage, duration, finish reason),
plus (2026-09-04 addition) lmstudio_sample / gpu_sample on session
start/end -- see _sample_hardware_async. Content is bounded per field (see
_MAX_CHARS) -- this is an operational audit trail, not a full-fidelity
conversation replay; use the bundled Langfuse plugin
(observability/langfuse) alongside this one if you also want that.

Ticket correlation (2026-09-04 addition): every event also carries run_id/
ticket_id, resolved once per kanban task_id via `hermes kanban show` and
cached -- so Hermes_L2_Compute_Per_Ticket_Vw (Knowledge/60_metrics_and_
reporting.sql) can compute tokens-used/tool-calls/wall-clock per ticket
with a plain GROUP BY, no join back into kanban's own sqlite state. The
resolution lookup itself runs in a background thread on first sight of a
new task_id (never blocks the hook that triggered it) -- the first one or
two events for a brand-new task may show a null run_id/ticket_id until
that resolution completes, which self-heals within about a second, well
inside the many-minute lifetime of a real investigation.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import threading
import time
from pathlib import Path
from typing import Any, Dict, Optional

_LOCK = threading.Lock()
_MAX_CHARS = 4000  # per string field; keeps one JSONL line small and the drain cheap

# Secret redaction -- 2026-09-04: confirmed live that this profile's
# MSSQL_MCP_USER/PASSWORD env vars have, on at least two real past
# investigations (cron output logs 2026-09-02/03), NOT been visible to the
# model's own execution context, forcing it toward typing --username/
# --password directly on the Hermes_Orchestrator.py command line -- which
# `pre_tool_call`/`post_tool_call` would otherwise capture verbatim into
# `args`/`result` and this plugin would durably write into a live SQL
# Server table with no further scrubbing downstream. Redact before the
# event ever leaves this process, not just at the eventual DB-insert step,
# since the local JSONL file is itself a durable artifact. Patterns match
# the shape used by the bundled Langfuse plugin's own secret scrubber
# (broadened here for this project's own known credential shapes).
_SECRET_PATTERNS = [
    re.compile(r"(--password\s+)(\S+|'[^']*'|\"[^\"]*\")", re.IGNORECASE),
    re.compile(r"(--pwd\s+)(\S+|'[^']*'|\"[^\"]*\")", re.IGNORECASE),
    re.compile(r"(PWD\s*=\s*)([^;'\"\s]+)", re.IGNORECASE),
    re.compile(r"(password\s*[:=]\s*)('[^']*'|\"[^\"]*\"|\S+)", re.IGNORECASE),
    re.compile(r"(MSSQL_MCP_PASSWORD\s*[:=]\s*)(\S+)", re.IGNORECASE),
    re.compile(r"(API_SERVER_KEY\s*[:=]\s*)(\S+)", re.IGNORECASE),
    re.compile(r"\b(sk-[A-Za-z0-9]{10,}|pk-lf-[A-Za-z0-9_-]{10,}|sk-lf-[A-Za-z0-9_-]{10,})\b"),
    re.compile(r"\b(eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,})\b"),  # JWT-shaped
]


def _redact(value: str) -> str:
    for pattern in _SECRET_PATTERNS:
        if pattern.groups >= 2:
            value = pattern.sub(lambda m: m.group(1) + "[REDACTED]", value)
        else:
            value = pattern.sub("[REDACTED]", value)
    return value

_DATA_DIR = Path.home() / ".hermes" / "plugin-data" / "xstudio-l2-trace"
_EVENTS_PATH = _DATA_DIR / "events.jsonl"

# Import-time marker -- proves the module was actually imported by whatever
# process loaded it, independent of whether any hook has fired yet. Debug
# aid only; safe to leave in permanently (negligible cost, fires once).
try:
    _DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(_DATA_DIR / "_imported_marker.txt", "a", encoding="utf-8") as _f:
        _f.write(f"imported at {time.time()} pid={os.getpid()}\n")
except Exception:
    pass


def _truncate(value: Any) -> Any:
    if isinstance(value, str):
        value = _redact(value)
        if len(value) > _MAX_CHARS:
            return value[:_MAX_CHARS] + f"...[truncated, {len(value)} chars total]"
        return value
    if isinstance(value, dict):
        return {k: _truncate(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_truncate(v) for v in value[:50]]  # bound list length too
    return value


def _write_event(event: Dict[str, Any]) -> None:
    """Append one JSON line. Fail-open: a broken trace write must never
    break the agent loop or lose the tool result it's observing."""
    try:
        event["written_at"] = time.time()
        line = json.dumps(_truncate(event), default=str) + "\n"
        with _LOCK:
            _DATA_DIR.mkdir(parents=True, exist_ok=True)
            with open(_EVENTS_PATH, "a", encoding="utf-8") as f:
                f.write(line)
    except Exception:
        pass  # observer hooks must be inert on failure, per the Hermes contract


# ---------------------------------------------------------------------------
# Ticket correlation: task_id -> (run_id, ticket_id), resolved once per task
# via `hermes kanban show`, in a background thread so no hook ever blocks on
# it. See module docstring.
# ---------------------------------------------------------------------------
_TASK_CACHE_LOCK = threading.Lock()
_TASK_CACHE: Dict[str, Dict[str, Optional[str]]] = {}
_RESOLVING: set = set()
_TASK_CACHE_MAX = 500

# 2026-09-04 correction: the observer hooks' own `task_id` kwarg turned out
# (confirmed live) to just equal `session_id` for a top-level kanban worker
# (no subagent involved) -- NOT the kanban board's own t_xxxxxxxx task id,
# despite the docs describing task_id as "especially useful for ... isolated
# execution". `hermes kanban show <session_id>` against that value silently
# resolves nothing (wrong ID shape) and gets cached as a permanent miss.
# The real kanban task id IS available, just not through any hook kwarg --
# it's a literal argument on this process's own command line (confirmed
# live: `hermes -p l2-gemma --cli ... chat -q "work kanban task
# t_e3decd2a"`). Read it once from this process's own argv instead of
# trusting the hook payload.
_KANBAN_TASK_ID_RE = re.compile(r"\bt_[0-9a-f]{6,}\b")
_MY_KANBAN_TASK_ID: Optional[str] = None
try:
    for _arg in sys.argv:
        _m = _KANBAN_TASK_ID_RE.search(_arg)
        if _m:
            _MY_KANBAN_TASK_ID = _m.group(0)
            break
except Exception:
    pass


def _resolve_task_ids_blocking(kanban_task_id: str) -> None:
    run_id = ticket_id = None
    for board_args in (["kanban", "show", kanban_task_id, "--json"],
                        ["kanban", "--board", "l2-review", "show", kanban_task_id, "--json"]):
        try:
            result = subprocess.run(["hermes"] + board_args, capture_output=True, text=True, timeout=8)
            if result.returncode != 0:
                continue
            data = json.loads(result.stdout)
            body = data.get("body") or (data.get("task") or {}).get("body") or ""
            for line in body.splitlines():
                line = line.strip()
                if line.lower().startswith("run_id:"):
                    run_id = line.split(":", 1)[1].strip()
                elif line.lower().startswith("ticket_id:"):
                    ticket_id = line.split(":", 1)[1].strip()
                elif line.lower().startswith("investigation_task_id:") and not run_id:
                    # A review-board card doesn't carry run_id/ticket_id directly in
                    # its own top-level lines the same way -- but its body embeds
                    # them further down (kanban_forward_bridge.py's own format), so
                    # the generic scan above already catches them there too. This
                    # branch is just documentation of that fact, not extra logic.
                    pass
            if run_id or ticket_id:
                break
        except Exception:
            continue
    with _TASK_CACHE_LOCK:
        _TASK_CACHE[kanban_task_id] = {"run_id": run_id, "ticket_id": ticket_id}
        _RESOLVING.discard(kanban_task_id)


def _get_or_start_resolve() -> Dict[str, Optional[str]]:
    """Resolves THIS process's own kanban task (see _MY_KANBAN_TASK_ID) --
    every hook call in this process is for the same one task, so there is
    exactly one cache entry per process, not one per (wrong) hook kwarg."""
    if not _MY_KANBAN_TASK_ID:
        return {"run_id": None, "ticket_id": None}
    with _TASK_CACHE_LOCK:
        cached = _TASK_CACHE.get(_MY_KANBAN_TASK_ID)
        if cached is not None:
            return cached
        already_resolving = _MY_KANBAN_TASK_ID in _RESOLVING
        _RESOLVING.add(_MY_KANBAN_TASK_ID)
    if not already_resolving:
        threading.Thread(target=_resolve_task_ids_blocking, args=(_MY_KANBAN_TASK_ID,), daemon=True).start()
    return {"run_id": None, "ticket_id": None}


def _identity_fields(kwargs: Dict[str, Any]) -> Dict[str, Any]:
    ids = _get_or_start_resolve()
    return {
        "session_id": kwargs.get("session_id"),
        "task_id": _MY_KANBAN_TASK_ID or kwargs.get("task_id"),
        "turn_id": kwargs.get("turn_id"),
        "tool_call_id": kwargs.get("tool_call_id"),
        "api_request_id": kwargs.get("api_request_id"),
        "run_id": ids.get("run_id"),
        "ticket_id": ids.get("ticket_id"),
    }


def on_pre_tool_call(**kwargs) -> None:
    _write_event({
        "event_type": "pre_tool_call",
        **_identity_fields(kwargs),
        "tool_name": kwargs.get("tool_name"),
        "args": kwargs.get("args"),
    })


def on_post_tool_call(**kwargs) -> None:
    _write_event({
        "event_type": "post_tool_call",
        **_identity_fields(kwargs),
        "tool_name": kwargs.get("tool_name"),
        "result": kwargs.get("result"),
        "status": kwargs.get("status"),
        "duration_ms": kwargs.get("duration_ms"),
        "error_type": kwargs.get("error_type"),
        "error_message": kwargs.get("error_message"),
    })


def on_post_api_request(**kwargs) -> None:
    _write_event({
        "event_type": "post_api_request",
        **_identity_fields(kwargs),
        "model": kwargs.get("model"),
        "provider": kwargs.get("provider"),
        "api_duration": kwargs.get("api_duration"),
        "finish_reason": kwargs.get("finish_reason"),
        "usage": kwargs.get("usage"),
        "assistant_content_chars": kwargs.get("assistant_content_chars"),
        "assistant_tool_call_count": kwargs.get("assistant_tool_call_count"),
    })


def on_api_request_error(**kwargs) -> None:
    _write_event({
        "event_type": "api_request_error",
        **_identity_fields(kwargs),
        "model": kwargs.get("model"),
        "provider": kwargs.get("provider"),
        "status_code": kwargs.get("status_code"),
        "retry_count": kwargs.get("retry_count"),
        "retryable": kwargs.get("retryable"),
        "error": kwargs.get("error"),
    })


# ---------------------------------------------------------------------------
# Hardware sampling -- 2026-09-04 addition. LM Studio + GPU utilization on
# the desktop (100.111.69.102), reusing the exact mechanism already proven
# in ~/.hermes/profiles/infra-guardian/scripts/infra_watchdog.py
# (check_lmstudio_server/check_gpu) rather than inventing a new one. LM
# Studio's /v1/models is a cheap local-ish HTTP call; the GPU check is a
# real remote WinRM round-trip (nvidia-smi on the desktop) and can take
# several seconds -- always run in a background thread, and only a single
# sample (not infra_watchdog's 3-sample-6s-apart loop, which exists for
# stuck-vs-slow detection this plugin doesn't need) to keep the WinRM load
# this adds, on top of infra-guardian's own periodic checks, reasonable.
# ---------------------------------------------------------------------------
_LMSTUDIO_MODELS_URL = "http://100.111.69.102:1235/v1/models"
_POWERSHELL_EXE = "/mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe"
_GPU_SCRIPT_WIN_PATH = "C:/Users/Admin/AppData/Local/hermes/profiles/infra-guardian/scripts/gpu_check.ps1"


def _sample_lmstudio() -> Optional[Dict[str, Any]]:
    try:
        import urllib.request
        t0 = time.time()
        with urllib.request.urlopen(_LMSTUDIO_MODELS_URL, timeout=8) as resp:
            data = json.loads(resp.read())
        return {"latency_s": round(time.time() - t0, 3), "models": [m.get("id") for m in data.get("data", [])]}
    except Exception as e:
        return {"error": str(e)}


def _sample_gpu() -> Optional[Dict[str, Any]]:
    try:
        t0 = time.time()
        out = subprocess.run(
            [_POWERSHELL_EXE, "-File", _GPU_SCRIPT_WIN_PATH],
            capture_output=True, text=True, timeout=25,
        ).stdout
        line = None
        for l in out.splitlines():
            if "MiB /" in l and "%" in l:
                line = l.strip()
                break
        if not line:
            return {"error": "no parseable nvidia-smi line", "raw": out[:500]}
        util_m = re.search(r"(\d+)%\s*(?:Default|E\. Process)", line)
        mem_m = re.search(r"(\d+)MiB\s*/\s*(\d+)MiB", line)
        return {
            "latency_s": round(time.time() - t0, 3),
            "gpu_util_pct": int(util_m.group(1)) if util_m else None,
            "mem_used_mb": int(mem_m.group(1)) if mem_m else None,
            "mem_total_mb": int(mem_m.group(2)) if mem_m else None,
            "raw": line,
        }
    except Exception as e:
        return {"error": str(e)}


def _sample_hardware_async(boundary: str, kwargs: Dict[str, Any]) -> None:
    def _run():
        _get_or_start_resolve()  # kick off resolution if not already cached/in-flight
        # ids may still be unresolved at session_start (just spawned); the
        # GPU sample alone takes several seconds, which gives the background
        # resolver thread time to finish before we read the cache again below.
        lm = _sample_lmstudio()
        gpu = _sample_gpu()
        ids2 = _TASK_CACHE.get(_MY_KANBAN_TASK_ID, {}) if _MY_KANBAN_TASK_ID else {}
        base = {
            "session_id": kwargs.get("session_id"),
            "task_id": _MY_KANBAN_TASK_ID or kwargs.get("task_id"),
            "run_id": ids2.get("run_id"),
            "ticket_id": ids2.get("ticket_id"),
        }
        _write_event({"event_type": "lmstudio_sample", "boundary": boundary, **base, "result": lm})
        _write_event({"event_type": "gpu_sample", "boundary": boundary, **base, "result": gpu})

    threading.Thread(target=_run, daemon=True).start()


def on_session_start(**kwargs) -> None:
    _sample_hardware_async("session_start", kwargs)


def on_session_end(**kwargs) -> None:
    _sample_hardware_async("session_end", kwargs)


def register(ctx) -> None:
    ctx.register_hook("pre_tool_call", on_pre_tool_call)
    ctx.register_hook("post_tool_call", on_post_tool_call)
    ctx.register_hook("post_api_request", on_post_api_request)
    ctx.register_hook("api_request_error", on_api_request_error)
    ctx.register_hook("on_session_start", on_session_start)
    ctx.register_hook("on_session_end", on_session_end)
