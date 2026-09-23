#!/usr/bin/env python3
"""Compatibility entrypoint for the deterministic L2 pipeline scout.

scout() executes the central lifecycle sequence: full synchronous reconciliation
followed by workflow-binding verification and bounded ticket claiming.
"""
import subprocess
import sys
from pathlib import Path
from l2_pipeline_runtime import cli


def is_dry_run(argv: list[str]) -> bool:
    return "--dry-run" in argv


def flush_observability() -> bool:
    """Drain hook events and write deterministic Helpdesk activity notes.

    The two-minute scout is the durable lifecycle backstop, so it is also the
    durable audit backstop.  Use the existing coalescing runner shared with
    the event hook: an agent crash can therefore still have its captured
    trace and terminal/recovery note persisted on the next scout tick without
    introducing an independent competing cron job.
    """
    runner = Path(__file__).with_name("run_coalesced.py")
    try:
        completed = subprocess.run(
            [sys.executable, str(runner), "drain_and_summarize.py", "--python", sys.executable],
            capture_output=True,
            text=True,
            timeout=120,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        print(f"WARNING: observability flush unavailable: {type(exc).__name__}: {exc}", file=sys.stderr)
        return False
    if completed.returncode:
        detail = (completed.stderr or completed.stdout or "unknown failure").strip()[:300]
        print(f"WARNING: observability flush failed: {detail}", file=sys.stderr)
        return False
    return True

if __name__ == "__main__":
    try:  # local call trace (Model_Bench/l2_calltrace.py); L2_CALLTRACE=0 disables
        import l2_calltrace
        l2_calltrace.install()
    except ImportError:
        pass
    rc = cli(["scout", *sys.argv[1:]])

    # A dry-run must be read-only end-to-end, including its audit sink.
    if not is_dry_run(sys.argv[1:]):
        flush_observability()

    raise SystemExit(rc)
