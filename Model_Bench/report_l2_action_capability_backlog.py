#!/usr/bin/env python3
"""Rank the real runtime corrective-capability backlog by observed evidence.

This is an operator/development report, not a risk classifier and not a promotion
mechanism. It helps choose which real repeated human action deserves executor
research next without fabricating "low risk" from wording alone.

Ranking uses only deterministic evidence already materialized by the learning
sidecar: distinct independently reviewed tickets first, then observation count.
Governance status is displayed but never inferred or changed here.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any

DEFAULT_VAULT = Path.home() / ".hermes" / "l2-learning"
ACTIVE_RESEARCH_STATES = {
    "needs_executor_design",
    "researching_executor",
    "contract_drafted",
    "shadow_ready",
}


def _vault(raw: str | None = None) -> Path:
    if raw:
        return Path(raw).expanduser()
    env = os.environ.get("CHITRAGUPTA_L2_LEARNING_VAULT", "").strip()
    return Path(env).expanduser() if env else DEFAULT_VAULT


def _load_candidate(path: Path) -> dict[str, Any] | None:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None
    if not isinstance(value, dict):
        return None
    if value.get("kind") != "xstudio_action_capability_candidate":
        return None
    return value


def backlog(vault: Path, *, include_terminal: bool = False) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    root = vault / "actions" / "candidates"
    for path in root.glob("*.json") if root.exists() else []:
        data = _load_candidate(path)
        if data is None:
            continue
        status = str(data.get("status") or "needs_executor_design")
        if not include_terminal and status not in ACTIVE_RESEARCH_STATES:
            continue
        design = data.get("design_requirements") if isinstance(data.get("design_requirements"), dict) else {}
        rows.append({
            "candidate": path.name,
            "candidate_id": data.get("candidate_id"),
            "status": status,
            "distinct_ticket_count": int(data.get("distinct_ticket_count") or 0),
            "observation_count": int(data.get("observation_count") or 0),
            "representative_human_action": data.get("representative_human_action"),
            "normalized_action": data.get("normalized_action"),
            "risk": design.get("risk") or "unclassified",
            "draft_capability_id": design.get("capability_id") or (data.get("draft_contract") or {}).get("id") if isinstance(data.get("draft_contract"), dict) else design.get("capability_id"),
            "source_cases": data.get("source_cases") if isinstance(data.get("source_cases"), list) else [],
            "ticket_ids": data.get("ticket_ids") if isinstance(data.get("ticket_ids"), list) else [],
            "first_seen_at": data.get("first_seen_at"),
            "updated_at": data.get("updated_at"),
        })
    rows.sort(key=lambda r: (
        -int(r["distinct_ticket_count"]),
        -int(r["observation_count"]),
        str(r.get("first_seen_at") or ""),
        str(r.get("candidate_id") or ""),
    ))
    for index, row in enumerate(rows, 1):
        row["rank"] = index
        row["selection_note"] = (
            f"{row['distinct_ticket_count']} distinct reviewed tickets / "
            f"{row['observation_count']} approved observations. "
            "Rank indicates automation value evidence only; inspect the real side effect before classifying risk."
        )
    return rows


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", default=None)
    ap.add_argument("--top", type=int, default=20)
    ap.add_argument("--include-terminal", action="store_true")
    ns = ap.parse_args(argv)
    rows = backlog(_vault(ns.vault), include_terminal=ns.include_terminal)
    top = max(1, ns.top)
    print(json.dumps({
        "ok": True,
        "vault": str(_vault(ns.vault)),
        "candidate_count": len(rows),
        "candidates": rows[:top],
        "warning": "Do not call the top item low-risk until its actual SP/API/service side effect, preconditions, idempotency, verification and compensation path are verified.",
    }, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
