#!/usr/bin/env python3
"""Scheduled L2 entrypoint: lifecycle scout plus reviewed-outcome materialization."""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

from l2_pipeline_runtime import cli
from sync_l2_outcomes import sync_outcomes

DEFAULT_VAULT = Path.home() / ".hermes" / "l2-learning"


def _vault() -> Path:
    raw = os.environ.get("CHITRAGUPTA_L2_LEARNING_VAULT", "").strip()
    return Path(raw).expanduser() if raw else DEFAULT_VAULT


def main() -> int:
    rc = cli(["scout", *sys.argv[1:]])
    try:
        result = sync_outcomes(vault=_vault())
        print(json.dumps({"outcome_sync": result}, separators=(",", ":"), default=str))
    except Exception as exc:
        print(json.dumps({
            "warning": "outcome materialization failed; ticket lifecycle result is unchanged",
            "error": f"{type(exc).__name__}: {exc}"[:500],
        }, separators=(",", ":")))
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
