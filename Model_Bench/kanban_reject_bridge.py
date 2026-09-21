#!/usr/bin/env python3
"""Compatibility entrypoint for reviewer-rejection reconciliation.

Lifecycle logic is centralized in l2_pipeline_runtime.py. Routing through
reconcile ensures execution through the single lifecycle reconciliation authority.
"""
import sys
from l2_pipeline_runtime import cli

if __name__ == "__main__":
    raise SystemExit(cli(["reconcile", *sys.argv[1:]]))
