#!/usr/bin/env python3
"""Deterministic, no-LLM cron job: run one dispatch pass against the
l2-review board.

Why this exists (2026-09-04 incident): the gateway's embedded dispatcher
(dispatch_in_gateway: true, dispatch_interval_seconds: 30) only ever
drives the profile's default board automatically. l2-review is a second,
separate board (its own kanban.db, per Hermes's own multi-board design)
that nothing was ever periodically dispatching -- confirmed live via its
own diagnostic ("Ready for 2.6h with no worker") on a task that had been
sitting since the very first forward-bridge run. A manual
`hermes kanban --board l2-review dispatch` immediately spawned both
waiting reviewer workers, proving the mechanism itself is fine; it was
simply never being invoked for this board. This cron job is that missing
invocation, run every minute so a review task never waits meaningfully
longer than that for its worker.
"""
import subprocess
import sys

result = subprocess.run(
    ["hermes", "kanban", "--board", "l2-review", "dispatch"],
    capture_output=True, text=True, timeout=60,
)
print(result.stdout.strip())
if result.stderr.strip():
    print(result.stderr.strip(), file=sys.stderr)
sys.exit(result.returncode)
