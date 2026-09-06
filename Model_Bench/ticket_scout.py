#!/usr/bin/env python3
"""Compatibility entrypoint for the deterministic L2 pipeline scout.

Every scout tick first reconciles work already in flight. One best-effort
learning sidecar cycle then materializes reviewer/publisher outcomes and mines
conservative learning candidates. New Helpdesk claims remain gated only by
deterministic workflow binding and WIP state: learning must never become
lifecycle authority or block ticket processing.
"""
import json
import sys
from l2_pipeline_runtime import cli, load_workflow_binding


def _run_learning_cycle_best_effort() -> None:
    try:
        from l2_learning_cycle import run_learning_cycle
        result = run_learning_cycle()
        print(json.dumps({"learning_cycle": result}, separators=(",", ":"), default=str))
    except Exception as exc:
        print(json.dumps({
            "warning": "learning cycle failed; lifecycle continues",
            "error": f"{type(exc).__name__}: {exc}"[:500],
        }, separators=(",", ":")))


if __name__ == "__main__":
    # The scout is the durable reconciliation backstop even while claiming is
    # administratively disabled by an incomplete workflow binding.
    rc = cli(["reconcile", *sys.argv[1:]])
    if rc != 0:
        raise SystemExit(rc)

    # Learning is one sidecar boundary, not a growing list of scout-owned
    # mechanisms. Rejection/approval/publication outcomes are captured first;
    # the miner then derives unverified candidates from the resulting case
    # corpus. Any failure here is deliberately non-fatal to ticket processing.
    _run_learning_cycle_best_effort()

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
