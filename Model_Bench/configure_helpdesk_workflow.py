#!/usr/bin/env python3
"""Inspect the live Helpdesk workflow and write the deterministic binding file.

This utility never guesses status names. With no --write arguments it only prints the
live discovery output. To persist a binding, pass the exact values observed there.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

WINDOWS_PYTHON = "/mnt/c/Python314/python.exe"
ORCHESTRATOR = r"C:\Users\Admin\Documents\Office\AIHelpdesk\Hermes_Orchestrator.py"
DEFAULT_OUTPUT = Path("/mnt/c/Users/Admin/Documents/Office/AIHelpdesk/deploy/helpdesk_workflow_binding.json")


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--server", default=os.environ.get("MSSQL_MCP_SERVER") or "10.2.6.204")
    p.add_argument("--username", default=os.environ.get("MSSQL_MCP_USER") or "sa")
    p.add_argument("--password", default=os.environ.get("MSSQL_MCP_PASSWORD"))
    p.add_argument("--resolved-status")
    p.add_argument("--waiting-user-status")
    p.add_argument("--waiting-user-ask-status")
    p.add_argument("--l3-status")
    p.add_argument("--needs-human-action-status")
    p.add_argument("--eligible-status", default="Enter")
    p.add_argument("--output", default=str(DEFAULT_OUTPUT))
    p.add_argument("--write", action="store_true")
    args = p.parse_args()

    python = sys.executable if os.name == "nt" else WINDOWS_PYTHON
    cmd = [python, ORCHESTRATOR, "--server", args.server, "--username", args.username, "--discover-workflow"]
    if args.password:
        cmd += ["--password", args.password]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if r.returncode != 0:
        print(r.stderr.strip() or r.stdout.strip(), file=sys.stderr)
        return 1
    print("LIVE WORKFLOW DISCOVERY")
    print(r.stdout.strip())

    if not args.write:
        print("\nNo binding written. Re-run with --write and exact status values from the discovery output.")
        return 0
    if not args.resolved_status:
        print("--resolved-status is required with --write; RESOLUTION must have a deterministic Helpdesk terminal state.", file=sys.stderr)
        return 2

    binding = {
        "schema_version": 1,
        "eligible_ticket_status": args.eligible_status,
        "resolved_ticket_status": args.resolved_status,
        "waiting_user_ticket_status": args.waiting_user_status,
        "waiting_user_ask_status": args.waiting_user_ask_status,
        "l3_ticket_status": args.l3_status,
        "needs_human_action_ticket_status": args.needs_human_action_status,
        "strict_resolution_status_binding": True,
        "allow_metadata_status_override": False,
        "notes": "Generated from operator-supplied values after live --discover-workflow inspection."
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(binding, indent=2) + "\n", encoding="utf-8")
    print(f"\nWrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
