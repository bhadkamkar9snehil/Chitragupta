#!/usr/bin/env python3
"""Windows-side bridge for the four runtime Jev workflows.

JSON in on stdin, JSON out on stdout. The Hermes model never calls this bridge
or chooses a Jev workflow; deterministic Chitragupta runtime code does.
"""
from __future__ import annotations

import json
import sys
from collections.abc import Callable
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from Model_Bench.jev.audit import persist_rows, rows_for_result
from Model_Bench.jev.evidence_plan import plan_evidence
from Model_Bench.jev.investigation_assessment import assess_investigation
from Model_Bench.jev.reviewer import review_proposal
from Model_Bench.jev.ticket_triage import assess_ticket_security


WorkflowHandler = Callable[[dict[str, Any], dict[str, Any]], dict[str, Any]]


def _ticket_security(_req: dict[str, Any], state: dict[str, Any]) -> dict[str, Any]:
    return assess_ticket_security(dict(state.get("ticket") or state))


def _evidence_plan(req: dict[str, Any], state: dict[str, Any]) -> dict[str, Any]:
    return plan_evidence(
        dict(req.get("ticket") or state.get("ticket") or {}),
        list(req.get("candidates") or state.get("candidates") or []),
        known_solutions=list(req.get("known_solutions") or state.get("known_solutions") or []),
    )


def _investigation_assessment(_req: dict[str, Any], state: dict[str, Any]) -> dict[str, Any]:
    return assess_investigation(state)


def _primary_review(_req: dict[str, Any], state: dict[str, Any]) -> dict[str, Any]:
    return review_proposal(state)


_WORKFLOWS: dict[str, WorkflowHandler] = {
    "ticket_security": _ticket_security,
    "evidence_plan": _evidence_plan,
    "investigation_assessment": _investigation_assessment,
    "primary_review": _primary_review,
}


def dispatch(req: dict[str, Any]) -> dict[str, Any]:
    workflow = str(req.get("workflow") or "")
    handler = _WORKFLOWS.get(workflow)
    if handler is None:
        raise ValueError(f"unsupported harness Jev workflow: {workflow}")

    state = req.get("state") or {}
    if not isinstance(state, dict):
        raise ValueError("state must be a JSON object")
    result = handler(req, state)

    audit = {"ok": True, "persisted": 0}
    if result.get("ok") and req.get("audit_stage"):
        rows = rows_for_result(
            result=result,
            stage=str(req["audit_stage"]),
            state=state,
            ticket_id=req.get("ticket_id"),
            run_id=req.get("run_id"),
            question_version=str(req.get("question_version") or "v1"),
            accepted=req.get("accepted"),
        )
        audit = persist_rows(rows)
    return {"workflow": workflow, "result": result, "audit": audit}


def main() -> int:
    try:
        req = json.loads(sys.stdin.read() or "{}")
        if not isinstance(req, dict):
            raise ValueError("request must be a JSON object")
        out = {"ok": True, **dispatch(req)}
    except Exception as exc:
        out = {"ok": False, "error": f"{type(exc).__name__}: {exc}"}
    print(json.dumps(out, default=str, separators=(",", ":")))
    return 0 if out.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
