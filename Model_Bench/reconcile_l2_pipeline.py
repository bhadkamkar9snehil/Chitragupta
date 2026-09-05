#!/usr/bin/env python3
"""Event/backstop entrypoint for sequential L2 pipeline reconciliation."""
import sys
from l2_pipeline_runtime import cli

if __name__ == "__main__":
    raise SystemExit(cli(["reconcile", *sys.argv[1:]]))
