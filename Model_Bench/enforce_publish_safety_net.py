#!/usr/bin/env python3
"""Compatibility entrypoint: recover only true active-run orphans.

A run is not stale merely because it is old. The centralized reconciler
protects every run referenced by Kanban at any stage, including parent-gated
`todo` reviewer cards and approved-but-not-yet-published reviewer cards.
"""
import sys
from l2_pipeline_runtime import cli

if __name__ == "__main__":
    raise SystemExit(cli(["recover", *sys.argv[1:]]))
