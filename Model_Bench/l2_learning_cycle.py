#!/usr/bin/env python3
"""One best-effort outcome-learning cycle for Chitragupta L2.

This is not lifecycle authority. It has three jobs only:
1. materialize reviewed ticket outcomes as historical cases;
2. mine conservative unverified lesson candidates from those outcomes;
3. synchronize the trust-separated GBrain retrieval index.

It does not create executable capabilities, mutate worker memory, or perform actions.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any

from mine_l2_learning_candidates import mine_candidates
from sync_l2_gbrain import sync_gbrain
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
        "lesson_candidate_mining": None,
        "gbrain_sync": None,
        "errors": [],
    }

    try:
        outcomes = sync_outcomes(vault=vault, args=args, dry_run=dry_run)
        result["outcomes"] = outcomes
        if outcomes.get("errors"):
            result["errors"].append(f"outcome sync reported {outcomes['errors']} error(s)")
    except Exception as exc:
        result["errors"].append(f"outcome sync failed: {type(exc).__name__}: {exc}"[:1000])

    try:
        mining = mine_candidates(vault, dry_run=dry_run)
        result["lesson_candidate_mining"] = mining
        if mining.get("errors"):
            result["errors"].append(f"lesson candidate mining reported {mining['errors']} error(s)")
    except Exception as exc:
        result["errors"].append(f"lesson candidate mining failed: {type(exc).__name__}: {exc}"[:1000])

    try:
        gbrain = sync_gbrain(vault, dry_run=dry_run)
        result["gbrain_sync"] = gbrain
        if not gbrain.get("ok"):
            errors = gbrain.get("errors") or [gbrain.get("error") or "unknown error"]
            result["errors"].append(f"gbrain sync reported: {errors}"[:1000])
    except Exception as exc:
        result["errors"].append(f"gbrain sync failed: {type(exc).__name__}: {exc}"[:1000])

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
