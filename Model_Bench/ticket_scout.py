#!/usr/bin/env python3
"""Scheduled L2 ticket-scout entrypoint."""
from __future__ import annotations

import json
import sys
from l2_pipeline_runtime import cli
from l2_learning_cycle import run_learning_cycle


def main() -> int:
    rc = cli(["scout", *sys.argv[1:]])
    try:
        result = run_learning_cycle()
        print(json.dumps({"learning_cycle": result}, separators=(",", ":"), default=str))
    except Exception as exc:
        print(json.dumps({
            "warning": "learning cycle failed; ticket lifecycle result is unchanged",
            "error": f"{type(exc).__name__}: {exc}"[:500],
        }, separators=(",", ":")))
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
