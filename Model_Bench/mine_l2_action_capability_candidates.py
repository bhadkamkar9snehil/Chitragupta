#!/usr/bin/env python3
"""Mine repeated reviewed NEEDS_HUMAN_ACTION outcomes into capability candidates.

This is the bridge from "the AI keeps diagnosing the same human fix" to "we should
build a typed deterministic XBatch capability for that fix".

It does NOT modify deploy/xstudio_action_capabilities.json and does not invent an
executor, parameter schema, risk level, or approval policy. A candidate is only a
control-plane backlog item saying: multiple independently reviewed/published
incidents required materially the same human action; investigate whether that
action can become a real typed capability.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DEFAULT_VAULT = Path.home() / ".hermes" / "l2-learning"
MIN_DISTINCT_TICKETS = max(2, int(os.environ.get("L2_CAPABILITY_CANDIDATE_MIN_TICKETS", "2")))


def _vault(value: str | None = None) -> Path:
    if value:
        return Path(value).expanduser()
    raw = os.environ.get("CHITRAGUPTA_L2_LEARNING_VAULT", "").strip()
    return Path(raw).expanduser() if raw else DEFAULT_VAULT


def _frontmatter(text: str) -> dict[str, Any]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    out: dict[str, Any] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line:
            continue
        key, raw = line.split(":", 1)
        try:
            out[key.strip()] = json.loads(raw.strip())
        except Exception:
            out[key.strip()] = raw.strip().strip("'\"")
    return out


def _section(text: str, heading: str) -> str:
    match = re.search(rf"(?ms)^##\s+{re.escape(heading)}\s*\n+(.*?)(?=^##\s+|^>\s|\Z)", text)
    return match.group(1).strip() if match else ""


def _normalize_action(text: str) -> str:
    value = " ".join(text.lower().split())
    value = re.sub(r"\bt_[0-9a-f]{6,}\b", "<task>", value, flags=re.I)
    value = re.sub(r"\b[0-9a-f]{8}-[0-9a-f-]{20,}\b", "<id>", value, flags=re.I)
    value = re.sub(r"\b\d{4,}\b", "<n>", value)
    return value.strip()


def _id(normalized: str) -> str:
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()[:24]


def mine_capability_candidates(vault: Path | None = None, *, dry_run: bool = False,
                               min_tickets: int = MIN_DISTINCT_TICKETS) -> dict[str, int]:
    vault = vault or _vault()
    groups: dict[str, dict[str, Any]] = {}
    counts = {"eligible_groups": 0, "created": 0, "updated": 0, "unchanged": 0, "errors": 0}

    for path in sorted((vault / "cases" / "approved").glob("*.md")):
        try:
            text = path.read_text(encoding="utf-8")
            meta = _frontmatter(text)
            if str(meta.get("response_type") or "").upper() != "NEEDS_HUMAN_ACTION":
                continue
            action = _section(text, "Resolution / proposed action")
            normalized = _normalize_action(action)
            if len(normalized) < 24:
                continue
            key = _id(normalized)
            group = groups.setdefault(key, {
                "normalized_action": normalized,
                "representative_action": action,
                "source_cases": [],
                "ticket_ids": set(),
                "run_ids": set(),
            })
            group["source_cases"].append(str(path))
            ticket = str(meta.get("ticket_id") or meta.get("ticket_no") or "").strip()
            run_id = str(meta.get("run_id") or "").strip()
            if ticket:
                group["ticket_ids"].add(ticket)
            if run_id:
                group["run_ids"].add(run_id)
        except Exception:
            counts["errors"] += 1

    out_dir = vault / "actions" / "candidates"
    if not dry_run:
        out_dir.mkdir(parents=True, exist_ok=True)

    for candidate_id, group in groups.items():
        ticket_ids = sorted(group["ticket_ids"])
        if len(ticket_ids) < max(2, min_tickets):
            continue
        counts["eligible_groups"] += 1
        path = out_dir / f"{candidate_id}.json"
        existing: dict[str, Any] = {}
        if path.exists():
            try:
                loaded = json.loads(path.read_text(encoding="utf-8"))
                existing = loaded if isinstance(loaded, dict) else {}
            except Exception:
                existing = {}

        candidate = {
            "schema_version": 1,
            "kind": "xstudio_action_capability_candidate",
            "candidate_id": candidate_id,
            "trust": "unverified_capability_candidate",
            "status": existing.get("status") or "needs_executor_design",
            "first_seen_at": existing.get("first_seen_at") or datetime.now(timezone.utc).isoformat(),
            "updated_at": datetime.now(timezone.utc).isoformat(),
            "observation_count": len(group["source_cases"]),
            "distinct_ticket_count": len(ticket_ids),
            "ticket_ids": ticket_ids,
            "run_ids": sorted(group["run_ids"]),
            "source_cases": sorted(group["source_cases"]),
            "representative_human_action": group["representative_action"],
            "normalized_action": group["normalized_action"],
            "design_requirements": {
                "capability_id": None,
                "risk": "unclassified",
                "parameter_schema": None,
                "preconditions": [],
                "execution": None,
                "idempotency": None,
                "verification": [],
                "rollback": None,
                "required_evidence": [],
                "approval_policy": None,
            },
            "promotion_gate": (
                "Do not add to the executable registry until the real supported XBatch/SP/API/service path, "
                "exact parameters, preconditions, idempotency, verification, rollback/compensation and risk policy are verified."
            ),
        }

        # Ignore volatile updated_at when deciding whether evidence changed.
        comparable_new = dict(candidate); comparable_new.pop("updated_at", None)
        comparable_old = dict(existing); comparable_old.pop("updated_at", None)
        if comparable_new == comparable_old:
            counts["unchanged"] += 1
            continue
        if dry_run:
            counts["updated" if existing else "created"] += 1
            continue
        path.write_text(json.dumps(candidate, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        counts["updated" if existing else "created"] += 1

    return counts


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", default=None)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--min-tickets", type=int, default=MIN_DISTINCT_TICKETS)
    ns = ap.parse_args(argv)
    counts = mine_capability_candidates(_vault(ns.vault), dry_run=ns.dry_run, min_tickets=ns.min_tickets)
    print(json.dumps({"ok": counts["errors"] == 0, "dry_run": ns.dry_run,
                      "vault": str(_vault(ns.vault)), "counts": counts}, indent=2))
    return 1 if counts["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
