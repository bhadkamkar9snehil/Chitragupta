#!/usr/bin/env python3
"""Subprocess entrypoint for governed L2 context-delivery assembly.

Reads one JSON request object from stdin and writes one JSON response object
to stdout. This mirrors how l2_pipeline_runtime.py already reaches
jev_workflow_bridge.py and kb_retrieval.py: the deployed runtime script stays
dependency-light and invokes this repo-resident module (which needs
l2_gbrain.py, l2_context_delivery*.py, l2_context_retriever.py, and
kb_retrieval.py's manifest/route helpers) via absolute path, rather than
importing all of that in-process.

Request (stdin JSON):
    {
      "ticket": {...}, "run_id": "...", "ticket_id": "...", "ticket_no": "...",
      "stage": "investigation"|"review"|"rework", "review_cycle": 0,
      "proposal": {...} | null,
      "current_run_evidence": [...] | null,
      "rejection_reason": "..." | null,
      "original_context": {...} | null,
      "vault": "..." | null
    }

Response (stdout JSON):
    {"ok": true, "envelope": {...}, "rendered_context": "...", "receipt_path": "..."}
  or, if governed retrieval could not run at all (never for a missing GBrain
  lane -- that degrades inside assemble_stage_context itself and still
  returns ok=true):
    {"ok": false, "error": "...", "envelope": {...degraded...},
     "rendered_context": "...", "receipt_path": "..."}

A failure here must never block the caller from building a card -- the
caller (l2_pipeline_runtime.py) treats both shapes as usable: the envelope
and rendered_context are always present, degraded or not.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import l2_context_delivery as delivery  # noqa: E402
from l2_context_delivery_receipts import persist_context_receipt, provenance_header  # noqa: E402


def _run(req: dict) -> dict:
    stage = str(req.get("stage") or "")
    common = dict(
        ticket=req.get("ticket") or {},
        run_id=str(req.get("run_id") or ""),
        ticket_id=str(req.get("ticket_id") or ""),
        ticket_no=str(req.get("ticket_no") or ""),
        stage=stage,
        review_cycle=int(req.get("review_cycle") or 0),
        proposal=req.get("proposal"),
        current_run_evidence=req.get("current_run_evidence"),
        rejection_reason=req.get("rejection_reason"),
        original_context=req.get("original_context"),
    )
    vault = req.get("vault")
    try:
        envelope, rendered = delivery.assemble_stage_context(
            vault=Path(vault) if vault else None,
            **common,
        )
        ok = True
        error = None
    except Exception as exc:  # noqa: BLE001 -- must always return a usable envelope
        envelope, rendered = delivery.assemble_degraded_context(
            reason=f"{type(exc).__name__}: {exc}",
            **common,
        )
        ok = False
        error = f"{type(exc).__name__}: {exc}"

    try:
        receipt_path = str(persist_context_receipt(envelope, rendered, vault=Path(vault) if vault else None))
    except Exception as exc:  # noqa: BLE001
        receipt_path = None
        if ok:
            ok = False
            error = f"receipt persistence failed: {type(exc).__name__}: {exc}"

    return {
        "ok": ok,
        "error": error,
        "envelope": envelope,
        "rendered_context": rendered,
        "provenance_header": provenance_header(envelope, receipt_path) if receipt_path else "",
        "receipt_path": receipt_path,
    }


def main() -> int:
    try:
        req = json.loads(sys.stdin.read() or "{}")
    except json.JSONDecodeError as exc:
        print(json.dumps({
            "ok": False, "error": f"invalid JSON request: {exc}",
            "envelope": None, "rendered_context": "", "provenance_header": "", "receipt_path": None,
        }))
        return 1
    try:
        response = _run(req)
    except Exception as exc:  # noqa: BLE001 -- caller must always get valid JSON back
        response = {
            "ok": False, "error": f"context delivery failed entirely: {type(exc).__name__}: {exc}",
            "envelope": None, "rendered_context": "", "provenance_header": "", "receipt_path": None,
        }
    print(json.dumps(response, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
