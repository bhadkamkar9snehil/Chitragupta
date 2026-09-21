#!/usr/bin/env python3
"""Compatibility entrypoint for the deterministic L2 pipeline scout.

scout() executes the central lifecycle sequence: full synchronous reconciliation
followed by workflow-binding verification and bounded ticket claiming.
"""
import sys
from l2_pipeline_runtime import cli

if __name__ == "__main__":
    raise SystemExit(cli(["scout", *sys.argv[1:]]))
