#!/usr/bin/env python3
"""Coalescing supervisor for the event-driven L2 bridge scripts.

Guarantees, across independent OS processes (kanban workers, the gateway,
cron, and manual runs all trigger these):

  1. At most ONE run of a given script at a time.
  2. A trigger arriving mid-run is never silently dropped by a RACE: it is
     always either serviced by the current owner or serviced by the trigger
     becoming the owner itself.
  3. A crashed/killed supervisor never wedges the script permanently.

Deliberate limit on (2): this is race-freedom, not an unconditional
delivery guarantee. Two bounds intentionally hand work back to the cron
backstop rather than let one script monopolise its lock -- MAX_CONSECUTIVE_
RUNS (a script that re-dirties itself every pass) and RUN_TIMEOUT_SECONDS
(a hung run). When either fires, outstanding triggers are left for cron.
That is a considered trade: unbounded re-running would starve every other
bridge script and could spin indefinitely. So cron remains a genuine
backstop here, not decoration.

Why the previous design was wrong
---------------------------------
v1 used a PID file: "if the recorded PID is alive, skip". That is advisory
only and has two real races:

  * TOCTOU on acquire -- two triggers can both read "no live PID" and both
    spawn, so property (1) was never actually guaranteed.
  * Dirty-check -> release race -- the supervisor checked the `.dirty` flag
    and then released the lock as two separate steps. A trigger landing in
    that window sees the lock still held (so it only sets `.dirty` and
    returns), while the supervisor has already decided to exit. The flag is
    set, nothing owns it, and nothing re-runs: the event is lost until a
    cron tick -- the exact wall-clock fallback this layer exists to remove.

How this version is actually atomic
-----------------------------------
Two POSIX `flock`s (kernel-enforced, and released automatically when the
holding process dies -- which is what makes crash recovery free):

  run.lock    held for the WHOLE duration of a supervisor's run loop.
              Holding it *is* the definition of "a run is in flight".
  state.lock  held only for microseconds, guarding reads/writes of the
              `pending` flag.

The invariant that closes the race: **run.lock is only ever released while
state.lock is held.** So a trigger that holds state.lock cannot observe
"run.lock is free" at the same moment the supervisor is deciding to exit --
the two are serialised.

  trigger:    lock(state) -> pending = True
                          -> try lock(run) non-blocking
                             acquired? -> pending = False, unlock(state), run loop
                             busy?     -> unlock(state), exit  (owner will see pending)

  owner end:  lock(state) -> pending set? -> pending = False, unlock(state), loop again
                          -> otherwise    -> unlock(run) THEN unlock(state), exit

Because the owner consumes `pending` under state.lock, and the trigger sets
it under state.lock before ever testing run.lock, every trigger either
becomes the owner or is guaranteed to be observed by the current owner.

Usage (invoked by the orchestrator plugin, not by hand):
    run_coalesced.py <script-name> [--python <interpreter>]
"""
from __future__ import annotations

import fcntl
import subprocess
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
LOCK_DIR = Path.home() / ".hermes" / "plugin-data" / "xstudio-l2-orchestrator" / "locks"
# Ceiling on consecutive re-runs so a script that somehow re-dirties itself
# every pass cannot hold run.lock forever. Cron still backstops the remainder.
MAX_CONSECUTIVE_RUNS = 5
# A single run exceeding this is treated as hung; the supervisor stops rather
# than holding run.lock (and therefore blocking every future trigger) forever.
RUN_TIMEOUT_SECONDS = 900


def _paths(script: str):
    LOCK_DIR.mkdir(parents=True, exist_ok=True)
    return (LOCK_DIR / f"{script}.run.lock",
            LOCK_DIR / f"{script}.state.lock",
            LOCK_DIR / f"{script}.pending")


def _acquire(fh, *, blocking: bool) -> bool:
    """flock a file handle. Returns False only for a non-blocking miss."""
    flags = fcntl.LOCK_EX if blocking else (fcntl.LOCK_EX | fcntl.LOCK_NB)
    try:
        fcntl.flock(fh.fileno(), flags)
        return True
    except (BlockingIOError, OSError):
        return False


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

    run_lock_path, state_lock_path, pending_path = _paths(script)

    # Open both lock files for the whole process lifetime; the kernel drops
    # the flocks if we die, so a crash can never wedge this script.
    with open(run_lock_path, "a+") as run_fh, open(state_lock_path, "a+") as state_fh:
        # --- acquire phase, under state.lock -------------------------------
        _acquire(state_fh, blocking=True)
        pending_path.touch()  # announce this trigger before testing run.lock
        owner = _acquire(run_fh, blocking=False)
        if owner:
            pending_path.unlink(missing_ok=True)  # we are servicing it now
        fcntl.flock(state_fh.fileno(), fcntl.LOCK_UN)
        if not owner:
            # Someone else is running it. They consume `pending` under
            # state.lock before releasing run.lock, so they cannot miss us.
            return 0

        # --- run loop, holding run.lock ------------------------------------
        runs = 0
        while runs < MAX_CONSECUTIVE_RUNS:
            runs += 1
            try:
                subprocess.run(
                    [python, str(target)],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    timeout=RUN_TIMEOUT_SECONDS,
                )
            except (subprocess.TimeoutExpired, Exception):
                break  # hung or unlaunchable: stop supervising, release below

            # Decide whether to loop again, atomically w.r.t. new triggers.
            _acquire(state_fh, blocking=True)
            if pending_path.exists():
                pending_path.unlink(missing_ok=True)
                fcntl.flock(state_fh.fileno(), fcntl.LOCK_UN)
                continue  # a trigger landed during the run -- service it
            # No pending work: release run.lock while STILL holding
            # state.lock. This is the step that makes the handoff race-free.
            fcntl.flock(run_fh.fileno(), fcntl.LOCK_UN)
            fcntl.flock(state_fh.fileno(), fcntl.LOCK_UN)
            return 0

        # Hit the ceiling (or a hung run): release explicitly and let cron
        # cover whatever is still outstanding.
        _acquire(state_fh, blocking=True)
        fcntl.flock(run_fh.fileno(), fcntl.LOCK_UN)
        fcntl.flock(state_fh.fileno(), fcntl.LOCK_UN)
    return 0


if __name__ == "__main__":
    sys.exit(main())
