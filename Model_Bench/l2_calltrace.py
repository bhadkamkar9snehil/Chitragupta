"""Local file call trace: every call into our own code, one JSON line per call/return.

Each line: IST time, pid, thread, event (call|return|exception), function, file:line,
depth, arguments (on call) or return value / exception type and message, and elapsed ms.
Only frames from this project's files are traced; stdlib and third-party code are not.

Enabled by default; set L2_CALLTRACE=0 to disable. Files go to
~/.hermes/logs/l2_calltrace/YYYY-MM-DD.jsonl (override: L2_CALLTRACE_DIR); only today's and
yesterday's files are kept.
"""
from __future__ import annotations

import dis
import json
import os
import sys
import threading
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

IST = timezone(timedelta(hours=5, minutes=30))
VALUE_CHARS = int(os.environ.get("L2_CALLTRACE_VALUE_CHARS", "400"))
# Substrings of the file paths that belong to this project (repo and deployed copies).
_OWN = ("l2_pipeline_runtime", "Hermes_Orchestrator", "xstudio_l2_tool_bridge", "ticket_scout",
        "/jev/", "\\jev\\", "xstudio-l2-tools", "xstudio_l2_tools_plugin", "l2_gbrain",
        "jev_post_resolution_curation")

# A frame that stops anywhere but a return instruction is unwinding an exception.
_RETURN_OPS = {dis.opmap[name] for name in ("RETURN_VALUE", "RETURN_CONST", "YIELD_VALUE")
               if name in dis.opmap}

# Hot tiny helpers (_norm ran ~90K times per table read) would drown the file: after
# FULL_CALLS calls of one function in a process, only every SAMPLE_EVERY-th is logged.
FULL_CALLS = int(os.environ.get("L2_CALLTRACE_FULL_CALLS", "200"))
SAMPLE_EVERY = int(os.environ.get("L2_CALLTRACE_SAMPLE_EVERY", "1000"))
_counts: dict[object, int] = {}

_lock = threading.Lock()
_local = threading.local()
_installed = False


def _own(filename: str) -> bool:
    return Path(filename).name != "l2_calltrace.py" and any(part in filename for part in _OWN)


def _short(value: object) -> str:
    try:
        text = repr(value)
    except Exception as exc:  # a broken __repr__ must not break the traced code
        text = f"<unreprable {type(value).__name__}: {exc}>"
    return text if len(text) <= VALUE_CHARS else text[:VALUE_CHARS] + f"...(+{len(text) - VALUE_CHARS})"


_current: Path | None = None


def _path() -> Path:
    """Today's file; on the first write of a new day, files older than yesterday are deleted."""
    global _current
    base = Path(os.environ.get("L2_CALLTRACE_DIR") or Path.home() / ".hermes" / "logs" / "l2_calltrace")
    today = base / f"{datetime.now(IST):%Y-%m-%d}.jsonl"
    if today != _current:
        base.mkdir(parents=True, exist_ok=True)
        keep = {today.name, f"{datetime.now(IST) - timedelta(days=1):%Y-%m-%d}.jsonl"}
        for old in base.glob("*.jsonl"):
            if old.name not in keep:
                old.unlink(missing_ok=True)
        _current = today
    return today


def _write(record: dict) -> None:
    line = json.dumps(record, default=str, ensure_ascii=False) + "\n"
    with _lock:
        with _path().open("a", encoding="utf-8") as handle:
            handle.write(line)


def _args(frame) -> dict[str, str]:
    code = frame.f_code
    names = code.co_varnames[:code.co_argcount + code.co_kwonlyargcount
                             + bool(code.co_flags & 0x04) + bool(code.co_flags & 0x08)]
    return {name: _short(frame.f_locals.get(name)) for name in names if name in frame.f_locals}


def _base(code, seen: int) -> dict:
    base = {
        "ts": datetime.now(IST).isoformat(timespec="milliseconds"),
        "pid": os.getpid(), "thread": threading.current_thread().name,
        "fn": code.co_qualname if hasattr(code, "co_qualname") else code.co_name,
        "at": f"{Path(code.co_filename).name}:{code.co_firstlineno}",
    }
    if seen > FULL_CALLS:
        base["sampled"] = f"call {seen} (1 in {SAMPLE_EVERY} logged after {FULL_CALLS})"
    return base


def _trace(frame, event, arg):
    """Global trace hook: sees each new frame ("call") and decides whether to follow it."""
    code = frame.f_code
    # <listcomp>/<genexpr>/<lambda> are expressions, not functions worth a line each.
    if event != "call" or code.co_name.startswith("<") or not _own(code.co_filename):
        return None
    _counts[code] = seen = _counts.get(code, 0) + 1
    if seen > FULL_CALLS and seen % SAMPLE_EVERY:
        return None
    depth = getattr(_local, "depth", 0) + 1
    _local.depth = depth
    _write({**_base(code, seen), "event": "call", "depth": depth, "args": _args(frame)})
    frame.f_trace_lines = False  # only call/return/exception events, never per line
    started = time.perf_counter()
    # Only the type name and message are kept: holding the exception object keeps its
    # traceback (and every local in it, e.g. a failed pyodbc cursor) alive, which left the
    # connection "busy with results" and stalled claims for ~50 minutes on 2026-09-23.
    raised: list[tuple[str, str]] = []

    def _local_trace(frame, event, arg):
        if event == "exception":
            raised[:] = [(arg[0].__name__, _short(str(arg[1])))]  # latest wins; no object refs
            return _local_trace
        if event != "return":
            return _local_trace
        _local.depth = depth - 1
        record = {**_base(code, seen), "depth": depth,
                  "ms": round((time.perf_counter() - started) * 1000, 2)}
        # An unwinding frame reports "return" with None after its "exception" event.
        unwinding = arg is None and raised and code.co_code[frame.f_lasti] not in _RETURN_OPS
        if unwinding:
            error_type, error = raised[0]
            record.update(event="exception", error_type=error_type, error=error)
        else:
            record.update(event="return", value=_short(arg))
        _write(record)
        return _local_trace

    return _local_trace


def install() -> None:
    """Start tracing this process (idempotent). No-op when L2_CALLTRACE=0."""
    global _installed
    if _installed or os.environ.get("L2_CALLTRACE", "1") == "0":
        return
    _installed = True
    sys.settrace(_trace)
    threading.settrace(_trace)
