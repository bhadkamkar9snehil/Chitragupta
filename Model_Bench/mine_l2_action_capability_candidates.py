#!/usr/bin/env python3
"""Mine repeated reviewed NEEDS_HUMAN_ACTION outcomes into action candidates.

This is evidence collection, not capability design. The miner owns only observed
fields. Operator-owned governance fields are preserved verbatim.

If an existing candidate cannot be parsed, the miner fails closed for that item
and leaves the file untouched.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from mine_l2_learning_candidates import (
    _normalize_root_cause as _normalize_case_text,
    _parse_frontmatter,
    _section,
)

DEFAULT_VAULT = Path.home() / ".hermes" / "l2-learning"
MIN_DISTINCT_TICKETS = max(2, int(os.environ.get("L2_CAPABILITY_CANDIDATE_MIN_TICKETS", "2")))
DEFAULT_STATUS = "needs_executor_design"


def _vault(value: str | None = None) -> Path:
    if value:
        return Path(value).expanduser()
    raw = os.environ.get("CHITRAGUPTA_L2_LEARNING_VAULT", "").strip()
    return Path(raw).expanduser() if raw else DEFAULT_VAULT


def _candidate_id(normalized: str) -> str:
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()[:24]


def _read_action_case(path: Path) -> tuple[dict[str, Any], str, str] | None:
    text = path.read_text(encoding="utf-8")
    meta = _parse_frontmatter(text)
    if str(meta.get("response_type") or "").upper() != "NEEDS_HUMAN_ACTION":
        return None
    action = _section(text, "Resolution / proposed action")
    normalized = _normalize_case_text(action)
    if len(normalized) < 24:
        return None
    return meta, action, normalized


def _add_group(groups: dict[str, dict[str, Any]], path: Path,
               meta: dict[str, Any], action: str, normalized: str) -> None:
    group = groups.setdefault(_candidate_id(normalized), {
        "normalized_action": normalized,
        "representative_human_action": action,
        "source_cases": [],
        "ticket_ids": set(),
        "run_ids": set(),
    })
    group["source_cases"].append(str(path))
    ticket_id = str(meta.get("ticket_id") or meta.get("ticket_no") or "").strip()
    run_id = str(meta.get("run_id") or "").strip()
    if ticket_id:
        group["ticket_ids"].add(ticket_id)
    if run_id:
        group["run_ids"].add(run_id)


def _scan_groups(vault: Path, counts: dict[str, int]) -> dict[str, dict[str, Any]]:
    groups: dict[str, dict[str, Any]] = {}
    for path in sorted((vault / "cases" / "approved").glob("*.md")):
        try:
            parsed = _read_action_case(path)
            if parsed:
                _add_group(groups, path, *parsed)
        except Exception:
            counts["errors"] += 1
    return groups


def _load_existing(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("candidate must be a JSON object")
    if data.get("kind") != "xstudio_action_capability_candidate":
        raise ValueError("candidate kind is invalid")
    return data


def _merge_observed(existing: dict[str, Any], candidate_id: str,
                    group: dict[str, Any]) -> dict[str, Any]:
    now = datetime.now(timezone.utc).isoformat()
    ticket_ids = sorted(group["ticket_ids"])
    candidate = dict(existing)
    candidate.update({
        "schema_version": 1,
        "kind": "xstudio_action_capability_candidate",
        "candidate_id": candidate_id,
        "trust": "unverified_capability_candidate",
        "status": existing.get("status") or DEFAULT_STATUS,
        "first_seen_at": existing.get("first_seen_at") or now,
        "observation_count": len(group["source_cases"]),
        "distinct_ticket_count": len(ticket_ids),
        "ticket_ids": ticket_ids,
        "run_ids": sorted(group["run_ids"]),
        "source_cases": sorted(group["source_cases"]),
        "representative_human_action": group["representative_human_action"],
        "normalized_action": group["normalized_action"],
    })
    return candidate


def _same_without_timestamp(left: dict[str, Any], right: dict[str, Any]) -> bool:
    a = dict(left)
    b = dict(right)
    a.pop("updated_at", None)
    b.pop("updated_at", None)
    return a == b


def _write_json(path: Path, value: dict[str, Any]) -> None:
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    tmp.replace(path)


def _load_for_merge(path: Path, counts: dict[str, int]) -> dict[str, Any] | None:
    if not path.exists():
        return {}
    try:
        return _load_existing(path)
    except Exception:
        counts["errors"] += 1
        return None


def mine_capability_candidates(vault: Path | None = None, *, dry_run: bool = False,
                               min_tickets: int = MIN_DISTINCT_TICKETS) -> dict[str, int]:
    vault = vault or _vault()
    counts = {"eligible_groups": 0, "created": 0, "updated": 0, "unchanged": 0, "errors": 0}
    groups = _scan_groups(vault, counts)
    out_dir = vault / "actions" / "candidates"

    for candidate_id, group in groups.items():
        if len(group["ticket_ids"]) < max(2, min_tickets):
            continue
        counts["eligible_groups"] += 1
        path = out_dir / f"{candidate_id}.json"
        existing = _load_for_merge(path, counts)
        if existing is None:
            continue

        candidate = _merge_observed(existing, candidate_id, group)
        if _same_without_timestamp(candidate, existing):
            counts["unchanged"] += 1
            continue

        candidate["updated_at"] = datetime.now(timezone.utc).isoformat()
        key = "updated" if existing else "created"
        counts[key] += 1
        if not dry_run:
            out_dir.mkdir(parents=True, exist_ok=True)
            _write_json(path, candidate)

    return counts


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", default=None)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--min-tickets", type=int, default=MIN_DISTINCT_TICKETS)
    ns = ap.parse_args(argv)
    vault = _vault(ns.vault)
    counts = mine_capability_candidates(vault, dry_run=ns.dry_run, min_tickets=ns.min_tickets)
    print(json.dumps({
        "ok": counts["errors"] == 0,
        "dry_run": ns.dry_run,
        "vault": str(vault),
        "counts": counts,
    }, indent=2))
    return 1 if counts["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
