#!/usr/bin/env python3
"""Compatibility entrypoint for the deterministic L2 pipeline scout.

Every scout tick first reconciles work already in flight. The learning sidecar
then materializes reviewer/publisher outcomes best-effort. New Helpdesk claims
remain gated only by deterministic workflow binding and WIP state: learning must
never become lifecycle authority or block ticket processing.
"""
import json
import sys
from l2_pipeline_runtime import cli, load_workflow_binding


def _sync_learning_outcomes_best_effort() -> None:
    try:
        from sync_l2_outcomes import sync_outcomes
        counts = sync_outcomes()
        print(json.dumps({"learning_outcomes": counts}, separators=(",", ":")))
    except Exception as exc:
        print(json.dumps({
            "warning": "learning outcome sync failed; lifecycle continues",
            "error": f"{type(exc).__name__}: {exc}"[:500],
        }, separators=(",", ":")))


if __name__ == "__main__":
    # The scout is the durable reconciliation backstop even while claiming is
    # administratively disabled by an incomplete workflow binding.
    rc = cli(["reconcile", *sys.argv[1:]])
    if rc != 0:
        raise SystemExit(rc)

    # Reviewer rejection/approval and publisher postconditions are stronger
    # learning signals than raw sessions. Capture them after reconcile, but never
    # let zvec/vault/learning failures affect lifecycle correctness.
    _sync_learning_outcomes_best_effort()

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
