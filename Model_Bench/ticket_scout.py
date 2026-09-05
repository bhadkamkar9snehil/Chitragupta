#!/usr/bin/env python3
"""Compatibility entrypoint for the deterministic L2 pipeline scout.

Every scout tick first reconciles work already in flight. New Helpdesk claims are
then allowed only when the deterministic Helpdesk resolution-status binding is
configured; this prevents spending an investigation only to discover at publish
time that the harness cannot move the real ticket to its verified terminal state.
"""
import json
import sys
from l2_pipeline_runtime import cli, load_workflow_binding

if __name__ == "__main__":
    # The scout is the durable 2-minute reconciliation backstop even while new
    # claiming is administratively disabled by an incomplete workflow binding.
    rc = cli(["reconcile", *sys.argv[1:]])
    if rc != 0:
        raise SystemExit(rc)

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
