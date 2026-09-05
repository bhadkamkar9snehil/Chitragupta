#!/usr/bin/env python3
"""Compatibility entrypoint: bridge reviewer rejects into bounded rework.

The central pipeline runtime creates both the rework investigator card and
a fresh parent-gated reviewer child, and caps review cycles explicitly.
"""
import sys
from l2_pipeline_runtime import cli

if __name__ == "__main__":
    raise SystemExit(cli(["reject", *sys.argv[1:]]))
