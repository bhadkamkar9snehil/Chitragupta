#!/usr/bin/env python3
"""Durable receipt/provenance helpers for deterministic L2 context delivery."""
from __future__ import annotations
from l2_context_delivery_base import *

def receipt_path(
    envelope: Mapping[str, Any], *, vault: Path | None = None
) -> Path:
    vault = vault or vault_path()
    run = re.sub(r"[^A-Za-z0-9_.-]+", "-", str(envelope["run_id"])).strip("-") or "unknown-run"
    stage = re.sub(r"[^A-Za-z0-9_.-]+", "-", str(envelope["pipeline_stage"])).strip("-") or "unknown-stage"
    cycle = int(envelope["review_cycle"])
    digest = str(envelope["context_sha256"])
    return vault / "retrieval" / "receipts" / run / f"{stage}-{cycle}-{digest[:20]}.json"


def persist_context_receipt(
    envelope: Mapping[str, Any],
    rendered_context: str,
    *,
    vault: Path | None = None,
) -> Path:
    errors = validate_context_envelope(envelope)
    if errors:
        raise ValueError("cannot persist invalid context envelope: " + "; ".join(errors))
    path = receipt_path(envelope, vault=vault)
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema_version": 1,
        "kind": "l2_context_receipt",
        "trust": "provenance_only_not_reusable_knowledge",
        "recorded_at": utc_now(),
        "context_sha256": envelope["context_sha256"],
        "query_sha256": envelope["query_sha256"],
        "run_id": envelope["run_id"],
        "ticket_id": envelope["ticket_id"],
        "ticket_no": envelope["ticket_no"],
        "pipeline_stage": envelope["pipeline_stage"],
        "review_cycle": envelope["review_cycle"],
        "envelope": envelope,
        "rendered_context": rendered_context,
    }
    serialized = json.dumps(payload, indent=2, ensure_ascii=False, default=str) + "\n"
    if path.exists() and path.read_text(encoding="utf-8") == serialized:
        return path
    tmp = path.with_suffix(".tmp")
    tmp.write_text(serialized, encoding="utf-8")
    tmp.replace(path)
    return path


def load_context_receipt(path: str | Path) -> dict[str, Any]:
    data = json.loads(Path(path).expanduser().read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("kind") != "l2_context_receipt":
        raise ValueError("not an L2 context receipt")
    envelope = data.get("envelope")
    if not isinstance(envelope, dict):
        raise ValueError("context receipt has no envelope")
    errors = validate_context_envelope(envelope)
    if errors:
        raise ValueError("context receipt envelope is invalid: " + "; ".join(errors))
    if data.get("context_sha256") != envelope.get("context_sha256"):
        raise ValueError("context receipt hash does not match envelope")
    return data


def provenance_header(envelope: Mapping[str, Any], receipt: str | Path) -> str:
    retrieval = envelope["retrieval"]
    return (
        f"context_schema_version: {envelope['schema_version']}\n"
        f"context_sha256: {envelope['context_sha256']}\n"
        f"retrieval_query_sha256: {envelope['query_sha256']}\n"
        f"retrieval_degraded: {str(retrieval['retrieval_degraded']).lower()}\n"
        f"context_receipt: {receipt}\n"
    )

__all__ = [name for name in globals() if not name.startswith("__")]
