#!/usr/bin/env python3
"""Compatibility entrypoint for the deterministic L2 pipeline scout.

The real implementation lives in l2_pipeline_runtime.py so claim, review,
rework, publish and recovery share one state machine instead of drifting
across independent scripts. The scout reconciles all in-flight work first
and only claims a new Helpdesk ticket when no active SQL run remains.
"""
import sys
from l2_pipeline_runtime import cli

if __name__ == "__main__":
    raise SystemExit(cli(["scout", *sys.argv[1:]]))
