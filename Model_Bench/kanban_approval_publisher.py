#!/usr/bin/env python3
"""Compatibility entrypoint: publish approved reviewer completions.

Lifecycle logic is centralized in l2_pipeline_runtime.py. This wrapper is
kept because existing hooks/cron/manual runbooks may still invoke the old
script name.
"""
import sys
from l2_pipeline_runtime import cli

if __name__ == "__main__":
    raise SystemExit(cli(["publish", *sys.argv[1:]]))
