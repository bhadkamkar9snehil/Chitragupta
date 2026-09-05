"""xstudio-l2-orchestrator -- event-driven trigger for the L2 kanban bridge
scripts, replacing wall-clock cron polling with immediate action on the
actual event that matters.

Why this exists (2026-09-04): every hand-off in the L2 pipeline (investigator
done -> reviewer board, reviewer reject -> rework card, reviewer approve ->
publish, review board dispatch, trace-log drain) was previously driven by a
cron job polling on a fixed interval (2-3 min each) regardless of whether
anything had actually happened. The user's explicit direction: prefer event-
driven over "dumb wall-clock cron" wherever a real event exists to trigger
on, and only keep cron as a backstop for cases genuinely unreachable by an
event (a crashed process, a gateway restart mid-flight) -- not as the
primary mechanism.

The event that matters already exists and is directly observable: every
kanban hand-off in this design is gated behind exactly one of two tool
calls, `kanban_complete` or `kanban_block`, both callable only by the model
itself and both already captured by Hermes's own `post_tool_call` observer
hook. This plugin hooks that same event and, the moment either call
succeeds, immediately fires every one of the (idempotent, no-op-when-
nothing-to-do) bridge/publisher/dispatch scripts instead of waiting for
their next cron tick. It deliberately does NOT try to resolve which board
or profile the call came from and fire only the "correct" one script --
that would require an extra kanban lookup per event and duplicate logic
that already lives correctly in each script; firing all of them and letting
each script's own existing "nothing to do" early-exit decide is simpler,
harder to get subtly wrong, and just as fast in practice given board sizes
here (tens of tasks, not thousands).

Debounced via a PID lock file per script: if several kanban_complete/
kanban_block calls fire in quick succession (confirmed live this session:
7 tasks completing near-simultaneously), a script already in flight is not
re-spawned -- the in-flight run will pick up whatever accumulated by the
time it actually gets there. A dead PID is treated as a stale lock and the
script is respawned normally, so a crashed run never permanently blocks
future triggers.
"""
from __future__ import annotations

import os
import subprocess
import sys
import time
from pathlib import Path

_SCRIPTS_DIR = Path.home() / ".hermes" / "profiles" / "l2-investigator" / "scripts"
_LOCK_DIR = Path.home() / ".hermes" / "plugin-data" / "xstudio-l2-orchestrator" / "locks"

_dbg_dir = Path.home() / ".hermes" / "plugin-data" / "xstudio-l2-orchestrator"
try:
    _dbg_dir.mkdir(parents=True, exist_ok=True)
    with open(_dbg_dir / "_imported_marker.txt", "a", encoding="utf-8") as _f:
        _f.write(f"imported at {time.time()} pid={os.getpid()}\n")
except Exception:
    pass

# Plain scripts, invoked with the current interpreter (all stdlib-only, no
# extra deps -- confirmed against kanban_reject_bridge.py,
# kanban_approval_publisher.py, drain_and_summarize.py,
# repair_incomplete_completions.py).
#
# kanban_forward_bridge.py retired 2026-09-04 (later): ticket_scout.py now
# creates the reviewer card immediately, gated on the investigator's card
# via native --parent dependency promotion -- no cron/hook-triggered
# cross-board bridge needed for that hop anymore.
#
# repair_incomplete_completions.py runs FIRST, deliberately, and on every
# kanban_complete/kanban_block (not just the investigator's) -- confirmed
# live 2026-09-05: 73% of recent investigator completions called
# kanban_complete with a real finding in `summary` but no response_type/
# reply_text in metadata, which the reviewer/publisher both require. This
# salvages what's salvageable before the reviewer card even promotes to
# ready, so a genuinely good investigation doesn't get rejected purely for
# a metadata-packaging failure.
_PY_SCRIPTS = [
    "repair_incomplete_completions.py",
    "kanban_reject_bridge.py",
    "kanban_approval_publisher.py",
    "drain_and_summarize.py",
]

_TRIGGER_TOOL_NAMES = {"kanban_complete", "kanban_block"}


def _is_pid_alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
        return True
    except (OSError, ProcessLookupError):
        return False
    except Exception:
        return True  # unknown platform quirk -- assume alive, err toward not double-spawning


def _try_lock(name: str) -> bool:
    """Returns True if the caller now owns the lock (should spawn), False if
    a live run already holds it.

    2026-09-05: when a live run holds the lock we now set a `.dirty` flag
    before returning False, instead of dropping the trigger. The old comment
    here claimed the in-flight run "will see the new state anyway" -- it does
    not. A run that started BEFORE this event has already queried the board
    and built its work list, so the event is invisible to it and nothing
    re-runs. Confirmed live: Ticket_343's approved response sat unpublished
    because the publisher happened to be mid-run when the approval landed,
    and only a manual invocation rescued it.

    `run_coalesced.py` owns the other half: it clears `.dirty` before each
    run and, if the flag reappears during that run, runs exactly once more.
    """
    _LOCK_DIR.mkdir(parents=True, exist_ok=True)
    lock_path = _LOCK_DIR / f"{name}.pid"
    try:
        if lock_path.exists():
            old_pid = int(lock_path.read_text(encoding="utf-8").strip() or "0")
            if old_pid and _is_pid_alive(old_pid):
                # Re-arm the in-flight supervisor rather than losing the event.
                try:
                    (_LOCK_DIR / f"{name}.dirty").touch()
                except Exception:
                    pass
                return False
    except Exception:
        pass  # unreadable/corrupt lock -- treat as stale, proceed to overwrite
    return True


def _spawn(name: str, args: list) -> None:
    if not _try_lock(name):
        return
    lock_path = _LOCK_DIR / f"{name}.pid"
    try:
        proc = subprocess.Popen(
            args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            start_new_session=True,
        )
        lock_path.write_text(str(proc.pid), encoding="utf-8")
    except Exception:
        pass  # a failed trigger must never break the agent loop; cron backstop still runs


def _fire_all() -> None:
    """Fire every bridge script through the coalescing supervisor.

    Each script is launched as `run_coalesced.py <script>` rather than
    directly, so a trigger that lands while that script is already running
    re-arms it (see `_try_lock`) instead of being silently dropped. If the
    supervisor is missing for any reason, fall back to launching the script
    directly -- degraded (events can be lost mid-run) but never worse than
    the pre-2026-09-05 behaviour, and the cron backstop still covers it.
    """
    python = sys.executable
    supervisor = _SCRIPTS_DIR / "run_coalesced.py"
    for script in _PY_SCRIPTS:
        path = _SCRIPTS_DIR / script
        if not path.exists():
            continue
        if supervisor.exists():
            _spawn(script, [python, str(supervisor), script, "--python", python])
        else:
            _spawn(script, [python, str(path)])
    # Single board now (default) -- already driven by the main gateway's
    # own kanban dispatcher, no separate l2-review board dispatch needed.


def on_post_tool_call(**kwargs) -> None:
    try:
        with open(_dbg_dir / "_hook_calls.log", "a", encoding="utf-8") as f:
            f.write(f"{time.time()} tool={kwargs.get('tool_name')} status={kwargs.get('status')}\n")
    except Exception:
        pass
    if kwargs.get("status") != "ok":
        return
    if kwargs.get("tool_name") not in _TRIGGER_TOOL_NAMES:
        return
    try:
        _fire_all()
    except Exception:
        pass  # fail-open -- cron backstop covers a broken trigger path


def register(ctx) -> None:
    ctx.register_hook("post_tool_call", on_post_tool_call)
