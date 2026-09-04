#!/usr/bin/env python3
"""Runs drain_l2_trace_log.py then generate_readable_trace_summary.py, in
that order, in one process -- the summary script's find_runs_to_summarize()
reads Hermes_Agent_Trace_Trn_Tbl directly, so it must never run before the
drain has committed the batch of events that made this run terminal (e.g.
the kanban_complete event itself). Firing the two as separate independent
subprocesses off the same post_tool_call trigger raced: on a fast machine
the summary script could see zero/partial events for a run, then persist it
into .summarized_runs.json as done -- permanently skipping it.

Invoked by xstudio_l2_orchestrator_plugin as a single script instead of two
separate _PY_SCRIPTS entries.
"""
import subprocess
import sys
from pathlib import Path

PYTHON = "/mnt/c/Python314/python.exe"
HERE = r"C:\Users\Admin\Documents\Office\AIHelpdesk\Model_Bench"

for script in ("drain_l2_trace_log.py", "generate_readable_trace_summary.py"):
    rc = subprocess.call([PYTHON, str(Path(HERE) / script)])
    if rc != 0:
        sys.exit(rc)  # don't summarize against a drain that failed partway
