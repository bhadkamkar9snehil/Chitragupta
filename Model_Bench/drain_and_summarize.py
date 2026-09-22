#!/usr/bin/env python3
"""Drain observer traces, run best-effort Jev semantics, then write readable notes.

Trace draining is correctness-critical for the summary. Jev trace/KB assessments
are advisory and must never prevent deterministic trace summarization.
"""
import subprocess
import sys
from pathlib import Path

PYTHON = "/mnt/c/Python314/python.exe"
HERE = r"C:\Users\Admin\Documents\Office\AIHelpdesk\Model_Bench"


def run(script: str) -> int:
    return subprocess.call([PYTHON, str(Path(HERE) / script)])


# Ground-truth trace persistence must complete before anything reads the batch.
rc = run("drain_l2_trace_log.py")
if rc != 0:
    sys.exit(rc)

# System-One semantic observers run out of band from the hot Hermes hooks.
# They are fail-open: missing API key, early-access service outage, or a not-yet
# deployed Jev audit table must not block the Helpdesk's deterministic notes.
for advisory in ("jev_trace_assessor.py", "jev_post_resolution_curation.py"):
    rc = run(advisory)
    if rc != 0:
        print(f"WARNING: advisory {advisory} exited {rc}; continuing.", file=sys.stderr)

# Human-readable trace note remains deterministic and operationally important.
sys.exit(run("generate_readable_trace_summary.py"))
