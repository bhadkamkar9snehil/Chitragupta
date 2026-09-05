#!/usr/bin/env python3
"""Compatibility entrypoint: normalize incomplete investigator completions."""
import sys
from l2_pipeline_runtime import cli

if __name__ == "__main__":
    raise SystemExit(cli(["repair", *sys.argv[1:]]))
