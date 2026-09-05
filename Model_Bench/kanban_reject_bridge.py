#!/usr/bin/env python3
"""Compatibility entrypoint for reviewer-rejection reconciliation.

The centralized runtime owns the transition. A rejected reviewer causes one rework
investigator card; only after that rework completes and is normalized does the
reconciler create a fresh reviewer with a new frozen proposal. This wrapper is not
an independent workflow engine.
"""
from l2_pipeline_runtime import cli

if __name__ == "__main__":
    raise SystemExit(cli(["reject", *__import__("sys").argv[1:]]))
