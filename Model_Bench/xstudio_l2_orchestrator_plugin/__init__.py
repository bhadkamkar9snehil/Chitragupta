"""xstudio-l2-orchestrator: event trigger for deterministic pipeline reconciliation.

The hook intentionally does not implement lifecycle logic. It only turns a successful
kanban_complete/kanban_block event into an immediate reconciler run. The same
reconciler is also called by ticket_scout every two minutes, so event delivery is an
optimization, not a correctness dependency.
"""
from __future__ import annotations

import os
import subprocess
import sys
import time
from pathlib import Path

_TRIGGER_TOOLS = {"kanban_complete", "kanban_block"}
_PROFILE_SCRIPT_DIRS = [
    Path.home() / ".hermes" / "profiles" / "l2-investigator" / "scripts",
    Path.home() / ".hermes" / "profiles" / "l2-investigator-primary" / "scripts",
]
_DEBUG_DIR = Path.home() / ".hermes" / "plugin-data" / "xstudio-l2-orchestrator"


def _scripts_dir() -> Path | None:
    for path in _PROFILE_SCRIPT_DIRS:
        if (path / "reconcile_l2_pipeline.py").exists():
            return path
    for path in _PROFILE_SCRIPT_DIRS:
        if path.exists():
            return path
    return None


def _spawn_through_supervisor(scripts: Path, script: str) -> None:
    target = scripts / script
    if not target.exists():
        return
    supervisor = scripts / "run_coalesced.py"
    if supervisor.exists():
        argv = [sys.executable, str(supervisor), script, "--python", sys.executable]
    else:
        argv = [sys.executable, str(target)]
    try:
        subprocess.Popen(argv, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
    except Exception:
        pass


def _fire() -> None:
    scripts = _scripts_dir()
    if not scripts:
        return
    # Lifecycle reconciliation is ONE sequential deterministic program. This fixes
    # the old race where repair, reject and publisher were spawned concurrently.
    _spawn_through_supervisor(scripts, "reconcile_l2_pipeline.py")
    # Trace draining is independent of lifecycle state and may run separately.
    _spawn_through_supervisor(scripts, "drain_and_summarize.py")


def on_post_tool_call(**kwargs) -> None:
    try:
        _DEBUG_DIR.mkdir(parents=True, exist_ok=True)
        with (_DEBUG_DIR / "_hook_calls.log").open("a", encoding="utf-8") as f:
            f.write(f"{time.time()} tool={kwargs.get('tool_name')} status={kwargs.get('status')} pid={os.getpid()}\n")
    except Exception:
        pass
    if kwargs.get("status") != "ok" or kwargs.get("tool_name") not in _TRIGGER_TOOLS:
        return
    try:
        _fire()
    except Exception:
        # Never break the agent loop. ticket_scout runs reconcile before every new
        # claim, so the 2-minute scout job is the durable backstop.
        pass


def register(ctx) -> None:
    ctx.register_hook("post_tool_call", on_post_tool_call)
