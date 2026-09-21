#!/usr/bin/env python3
"""Windows-side bridge for Chitragupta Jev workflows.

JSON in on stdin, JSON out on stdout. This keeps TypeSafe network access and
SQL judgment persistence deterministic and harness-owned when the caller is a
WSL lifecycle process.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from Model_Bench.jev.audit import persist_rows, rows_for_result
from Model_Bench.jev.candidate_rerank import rerank_candidates
from Model_Bench.jev.kb_applicability import assess_kb_candidates
from Model_Bench.jev.kb_curation import assess_curation
from Model_Bench.jev.model_routing import assess_model_route
from Model_Bench.jev.l1_action import assess_l1_action
from Model_Bench.jev.proposal_preflight import assess_proposal
from Model_Bench.jev.review_risk import assess_review_risk
from Model_Bench.jev.security import assess_context_items, assess_untrusted_context
from Model_Bench.jev.ticket_triage import assess_ticket
from Model_Bench.jev.trace_assessment import assess_trace


def dispatch(req: dict[str, Any]) -> dict[str, Any]:
    workflow = str(req.get("workflow") or "")
    state = req.get("state") or {}
    if workflow == "proposal_preflight":
        result = assess_proposal(state)
    elif workflow == "review_risk":
        result = assess_review_risk(state)
    elif workflow == "trace_assessment":
        result = assess_trace(state)
    elif workflow == "kb_curation":
        result = assess_curation(state)
    elif workflow == "security":
        result = assess_untrusted_context(str(req.get("source") or "untrusted"), state)
    elif workflow == "security_batch":
        result = assess_context_items(list(req.get("items") or []))
    elif workflow == "candidate_rerank":
        result = rerank_candidates(
            str(req.get("query") or ""),
            list(req.get("candidates") or []),
            top=int(req.get("top") or 5),
            candidate_kind=str(req.get("candidate_kind") or "candidate"),
        )
    elif workflow == "kb_applicability":
        result = assess_kb_candidates(dict(req.get("ticket") or {}), list(req.get("candidates") or []))
    elif workflow == "ticket_triage":
        result = assess_ticket(
            dict(req.get("ticket") or {}),
            dict(req.get("manifest") or {}),
            allowed_routes=req.get("allowed_routes"),
        )
    elif workflow == "model_routing":
        result = assess_model_route(state, dict(req.get("profiles") or {}))
    elif workflow == "l1_action":
        result = assess_l1_action(state, actions=req.get("actions"))
    else:
        raise ValueError(f"unsupported Jev workflow: {workflow}")

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
        try:
            audit = persist_rows(rows)
        except Exception as exc:
            audit = {"ok": False, "persisted": 0, "reason": f"{type(exc).__name__}: {exc}"}
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
