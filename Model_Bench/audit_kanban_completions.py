#!/usr/bin/env python3
"""Compatibility entrypoint: audit reviewer completions against SQL truth."""
import sys
from l2_pipeline_runtime import cli

if __name__ == "__main__":
    raise SystemExit(cli(["audit", *sys.argv[1:]]))
