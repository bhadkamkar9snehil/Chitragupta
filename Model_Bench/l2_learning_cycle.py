#!/usr/bin/env python3
"""One best-effort learning sidecar cycle for the deterministic L2 runtime.

This module is deliberately *not* lifecycle authority. It aggregates learning
work behind one call so ticket_scout does not grow a ponytail of independent
background steps as the learning system expands.

Current cycle:
  1. materialize reviewer/publisher outcomes as historical cases;
  2. mine deterministic unverified candidates from those outcomes.

Each component fails independently and the caller may continue ticket handling.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any

from mine_l2_learning_candidates import mine_candidates
from sync_l2_outcomes import sync_outcomes

DEFAULT_VAULT = Path.home() / ".hermes" / "l2-learning"


def _vault(value: str | None = None) -> Path:
    if value:
        return Path(value).expanduser()
    raw = os.environ.get("CHITRAGUPTA_L2_LEARNING_VAULT", "").strip()
    return Path(raw).expanduser() if raw else DEFAULT_VAULT


def run_learning_cycle(*, vault: Path | None = None, dry_run: bool = False,
                       args: Any = None) -> dict[str, Any]:
    vault = vault or _vault()
    result: dict[str, Any] = {
        "ok": True,
        "vault": str(vault),
        "dry_run": dry_run,
        "outcomes": None,
        "candidate_mining": None,
        "errors": [],
    }

    try:
        outcomes = sync_outcomes(vault=vault, args=args, dry_run=dry_run)
        result["outcomes"] = outcomes
        if outcomes.get("errors"):
            result["errors"].append(f"outcome sync reported {outcomes['errors']} error(s)")
    except Exception as exc:
        result["errors"].append(f"outcome sync failed: {type(exc).__name__}: {exc}"[:1000])

    # Mine whatever case corpus already exists even if this cycle's SQL outcome
    # sync had a transient failure. Mining is local-file-only and idempotent.
    try:
        mining = mine_candidates(vault, dry_run=dry_run)
        result["candidate_mining"] = mining
        if mining.get("errors"):
            result["errors"].append(f"candidate mining reported {mining['errors']} error(s)")
    except Exception as exc:
        result["errors"].append(f"candidate mining failed: {type(exc).__name__}: {exc}"[:1000])

    result["ok"] = not result["errors"]
    return result


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", default=None)
    ap.add_argument("--dry-run", action="store_true")
    ns = ap.parse_args(argv)
    result = run_learning_cycle(vault=_vault(ns.vault), dry_run=ns.dry_run)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
