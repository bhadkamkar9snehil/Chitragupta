#!/usr/bin/env python3
"""Compatibility entrypoint for orphan-run recovery.

The centralized runtime owns recovery. A run is protected whenever current Kanban
state still references it, including queued/deferred-stage work and completed review
state awaiting deterministic publication. This wrapper exists for operator/backward
compatibility only; it is not a separately scheduled lifecycle authority.
"""
from l2_pipeline_runtime import cli

if __name__ == "__main__":
    raise SystemExit(cli(["recover", *__import__("sys").argv[1:]]))
