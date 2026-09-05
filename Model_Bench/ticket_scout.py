#!/usr/bin/env python3
"""Compatibility entrypoint for the deterministic L2 pipeline scout.

The real implementation lives in l2_pipeline_runtime.py so claim, review,
rework, publish and recovery share one state machine instead of drifting
across independent scripts. The scout reconciles all in-flight work first
and only claims a new Helpdesk ticket when no active SQL run remains.

Fresh claiming is also disabled until the deterministic Helpdesk resolution
status binding is configured. It is cheaper and safer to refuse a new claim
than to investigate a ticket and discover at publish time that the harness
cannot move the real Helpdesk ticket to its verified terminal state.
"""
import json
import sys
from l2_pipeline_runtime import cli, load_workflow_binding

if __name__ == "__main__":
    binding = load_workflow_binding()
    if binding.get("strict_resolution_status_binding", True) and not binding.get("resolved_ticket_status"):
        print(json.dumps({
            "ok": True,
            "mode": "scout",
            "result": {
                "status": "WORKFLOW_BINDING_NOT_READY",
                "reason": "resolved_ticket_status is not configured; run Model_Bench/configure_helpdesk_workflow.py against the live Helpdesk before enabling claims.",
                "binding_path": binding.get("_path")
            }
        }, indent=2))
        raise SystemExit(0)
    raise SystemExit(cli(["scout", *sys.argv[1:]]))
