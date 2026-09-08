#!/usr/bin/env python3
"""Compatibility entrypoint for the deterministic L2 pipeline scout.

Every scout tick first reconciles work already in flight. New Helpdesk claims are
then allowed only when the deterministic Helpdesk resolution-status binding is
configured; this prevents spending an investigation only to discover at publish
time that the harness cannot move the real ticket to its verified terminal state.
"""
import json
import subprocess
import sys
from pathlib import Path
from l2_pipeline_runtime import cli, load_workflow_binding


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
    # The scout is the durable 2-minute reconciliation backstop even while new
    # claiming is administratively disabled by an incomplete workflow binding.
    rc = cli(["reconcile", *sys.argv[1:]])
    if rc != 0:
        raise SystemExit(rc)

    # A dry-run must be read-only end-to-end, including its audit sink.
    if not is_dry_run(sys.argv[1:]):
        flush_observability()

    binding = load_workflow_binding()
    if binding.get("strict_resolution_status_binding", True) and not binding.get("resolved_ticket_status"):
        print(json.dumps({
            "ok": True,
            "mode": "scout",
            "result": {
                "status": "WORKFLOW_BINDING_NOT_READY",
                "reason": "resolved_ticket_status is not configured; run Model_Bench/configure_helpdesk_workflow.py against the live Helpdesk before enabling new claims.",
                "binding_path": binding.get("_path")
            }
        }, indent=2))
        raise SystemExit(0)

    # scout() performs its own idempotent reconciliation too; the second pass is
    # intentional so work that landed between the backstop pass and claim check
    # cannot be overtaken by a fresh ticket.
    raise SystemExit(cli(["scout", *sys.argv[1:]]))
