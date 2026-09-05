#!/usr/bin/env python3
"""Coalescing supervisor for the event-driven L2 bridge scripts.

Why this exists (2026-09-05): the orchestrator plugin's original debounce
was "if a run of this script is already in flight, skip -- it will see the
new state anyway." That assumption is wrong and silently drops the exact
event that matters.

Concrete failure it causes: reviewer approves ticket X at T. The approval
publisher happens to already be in flight since T-5s (triggered by some
earlier completion). It has ALREADY queried the board and built its task
list, so it never sees X. The plugin skips re-spawning because the lock is
held. Nothing re-runs. X's approved response is never published, and the
only thing that eventually rescues it is a wall-clock cron tick -- which is
precisely the "dumb scheduled polling" this event layer exists to replace.
Confirmed live: Ticket_343's approval sat unpublished until the publisher
was invoked by hand.

The fix is the standard coalescing / run-again-if-signalled pattern:

    trigger arrives, no run in flight  -> spawn supervisor, run script
    trigger arrives, run IS in flight  -> set a `.dirty` flag, return
    supervisor finishes a run          -> if `.dirty` was set during it,
                                          clear it and run exactly once more

This guarantees the property the debounce was reaching for (never more than
one concurrent run of a script) WITHOUT the property that broke it (an
event arriving mid-run being lost). At most one extra run is queued no
matter how many triggers land during a run, so a burst of N completions
still costs at most 2 runs, not N.

Usage (invoked by the plugin, not by hand):
    run_coalesced.py <script-name> [--python <interpreter>]

`<script-name>` is resolved inside this script's own directory, so the
supervisor and the bridge scripts stay co-located and there is no path
configuration to drift.
"""
from __future__ import annotations

import os
import subprocess
import sys
import time
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
LOCK_DIR = Path.home() / ".hermes" / "plugin-data" / "xstudio-l2-orchestrator" / "locks"
# Hard ceiling on consecutive re-runs. A script that is somehow re-dirtied
# every single time it runs must not spin forever holding the lock; the cron
# backstop still exists for whatever the ceiling drops.
MAX_CONSECUTIVE_RUNS = 5
# A single bridge run that exceeds this is treated as hung: the supervisor
# gives up waiting rather than holding the lock (and therefore blocking every
# future trigger for this script) indefinitely.
RUN_TIMEOUT_SECONDS = 900


def _dirty_path(script: str) -> Path:
    return LOCK_DIR / f"{script}.dirty"


def _lock_path(script: str) -> Path:
    return LOCK_DIR / f"{script}.pid"


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: run_coalesced.py <script-name> [--python <interpreter>]", file=sys.stderr)
        return 2
    script = sys.argv[1]
    python = sys.executable
    if "--python" in sys.argv:
        python = sys.argv[sys.argv.index("--python") + 1]

    target = SCRIPTS_DIR / script
    if not target.exists():
        print(f"run_coalesced: {target} does not exist", file=sys.stderr)
        return 2

    LOCK_DIR.mkdir(parents=True, exist_ok=True)
    dirty = _dirty_path(script)
    lock = _lock_path(script)

    runs = 0
    try:
        while runs < MAX_CONSECUTIVE_RUNS:
            # Clear BEFORE running: any trigger that lands from here on is a
            # genuinely new event this run may not observe, and must re-arm.
            dirty.unlink(missing_ok=True)
            runs += 1
            try:
                subprocess.run(
                    [python, str(target)],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    timeout=RUN_TIMEOUT_SECONDS,
                )
            except subprocess.TimeoutExpired:
                # Hung run: stop supervising rather than hold the lock forever.
                break
            except Exception:
                break
            if not dirty.exists():
                break
    finally:
        # Release the lock last, so a trigger arriving during the final run
        # either sets dirty (and is picked up by the loop above) or, if it
        # lands after the loop exits, finds no live lock and spawns cleanly.
        try:
            if lock.exists() and lock.read_text(encoding="utf-8").strip() == str(os.getpid()):
                lock.unlink(missing_ok=True)
        except Exception:
            pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
