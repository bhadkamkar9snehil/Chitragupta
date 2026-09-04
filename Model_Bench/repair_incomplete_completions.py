#!/usr/bin/env python3
"""Deterministic, no-LLM repair: salvage an investigator completion whose
kanban_complete metadata is missing response_type/reply_text -- the two
fields the whole downstream publish pipeline requires -- instead of losing
a genuinely good investigation to a metadata-packaging failure.

Why this exists (2026-09-05): confirmed live that 73% of recent l2-gemma
completions (22 of 30 checked) called kanban_complete with a real,
substantive `summary` but without ever including `response_type`/
`reply_text` in `metadata` -- in the clearest case, the actual tool call
was kanban_complete(summary="...") with NO metadata argument at all. This
is a small local model dropping the harder half of a multi-field
structured tool call, the same class of limitation as LM Studio's
forced-tool-call gap already documented in this project -- not something
more prompting alone reliably fixes. The verifier's skill now rejects
these on sight (see xstudio-l2-draft-verifier), which is correct but
throws away real, usable findings and costs a full rework cycle.

This script salvages what's salvageable BEFORE the verifier ever sees it:
if `summary` is a real, substantive sentence and metadata lacks
response_type/reply_text, use `summary` as `reply_text` verbatim (never
invent content) and infer `response_type` from its own language via
simple keyword heuristics, then write it back with `kanban edit
--metadata` (merged, not replaced -- existing fields like `findings` are
preserved). If the summary is too short/generic to trust, this does
nothing and leaves it for the verifier's reject-and-rework path.

Usage (intended as a --no-agent cron job or hook-triggered, every ~2-5 min):
    python repair_incomplete_completions.py [--dry-run]
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

STATE_PATH = Path(__file__).parent / ".repaired_tasks.json"
_HAS_WSL = shutil.which("wsl") is not None

INVESTIGATOR_PROFILES = {"l2-gemma", "l2-investigator"}
MIN_SUMMARY_CHARS = 40  # below this, too thin to trust as a real finding

# Ordered most-specific-first; first match wins. Deliberately conservative --
# defaults to UPDATE (the safest, least consequential type) rather than
# guessing RESOLUTION/L3_ESCALATION when language is ambiguous.
_RESPONSE_TYPE_PATTERNS = [
    ("L3_ESCALATION", re.compile(r"\bl3 escalat|\bescalat\w* to l3|\bescalating\b", re.IGNORECASE)),
    ("RESOLUTION", re.compile(r"\bresolved\b|\bfix(?:ed)? confirmed\b|\bverified live\b.*\bfix", re.IGNORECASE)),
    ("QUESTION", re.compile(r"\?\s*$|need(?:s)? (?:more info|clarification) from|requester\b.*\bconfirm", re.IGNORECASE)),
]


def run_hermes(args_list, timeout=30):
    if _HAS_WSL:
        import shlex
        cmd = ["wsl", "-d", "Ubuntu", "--", "bash", "-lc", "hermes " + shlex.join(args_list)]
    else:
        cmd = ["hermes"] + args_list
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)


def load_state():
    if STATE_PATH.exists():
        return set(json.loads(STATE_PATH.read_text(encoding="utf-8")))
    return set()


def save_state(state):
    STATE_PATH.write_text(json.dumps(sorted(state)), encoding="utf-8")


def find_done_investigator_tasks():
    r = run_hermes(["kanban", "list", "--status", "done", "--json"])
    if r.returncode != 0:
        print(f"WARNING: could not list done tasks: {r.stderr.strip()[:300]}")
        return []
    tasks = json.loads(r.stdout)
    return [t for t in tasks if (t.get("assignee") or "") in INVESTIGATOR_PROFILES]


def get_runs(task_id):
    r = run_hermes(["kanban", "runs", task_id, "--json"])
    if r.returncode != 0:
        return []
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        return []


def infer_response_type(summary: str) -> str:
    for response_type, pattern in _RESPONSE_TYPE_PATTERNS:
        if pattern.search(summary):
            return response_type
    return "UPDATE"


def extract_run_ticket_ids(task_body: str):
    run_id = ticket_id = None
    for line in (task_body or "").splitlines():
        line = line.strip()
        if line.startswith("run_id:"):
            run_id = line.split(":", 1)[1].strip()
        elif line.startswith("ticket_id:"):
            ticket_id = line.split(":", 1)[1].strip()
    return run_id, ticket_id


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    tasks = find_done_investigator_tasks()
    if not tasks:
        print("No done investigator tasks found.")
        return

    state = load_state()
    repaired = 0
    for t in tasks:
        task_id = t["id"]
        if task_id in state:
            continue

        runs = get_runs(task_id)
        done_runs = [r for r in runs if r.get("status") == "done"]
        if not done_runs:
            continue
        latest = done_runs[-1]
        metadata = latest.get("metadata") or {}

        if metadata.get("response_type") and metadata.get("reply_text"):
            state.add(task_id)  # already complete, never needs a look again
            continue

        summary = (latest.get("summary") or "").strip()
        if len(summary) < MIN_SUMMARY_CHARS:
            print(f"  {task_id}: metadata incomplete, summary too thin to salvage ({len(summary)} chars) -- leaving for verifier reject")
            continue

        run_id, ticket_id = metadata.get("run_id"), metadata.get("ticket_id")
        if not run_id or not ticket_id:
            run_id2, ticket_id2 = extract_run_ticket_ids(t.get("body"))
            run_id = run_id or run_id2
            ticket_id = ticket_id or ticket_id2
        if not run_id or not ticket_id:
            print(f"  {task_id}: metadata incomplete AND no run_id/ticket_id found anywhere -- cannot repair, leaving for verifier reject")
            continue

        response_type = infer_response_type(summary)
        merged_metadata = dict(metadata)
        merged_metadata["run_id"] = run_id
        merged_metadata["ticket_id"] = ticket_id
        merged_metadata["response_type"] = response_type
        merged_metadata["reply_text"] = summary
        merged_metadata["repaired_by"] = "repair_incomplete_completions.py"

        print(f"  {task_id}: repairing -- response_type={response_type} (inferred), reply_text=summary ({len(summary)} chars)")
        if args.dry_run:
            print(f"    [DRY RUN] Would edit with metadata: {json.dumps(merged_metadata)[:200]}")
            continue

        r = run_hermes([
            "kanban", "edit", task_id,
            "--result", summary[:500],
            "--metadata", json.dumps(merged_metadata),
        ])
        if r.returncode != 0:
            print(f"    FAILED to repair: {r.stderr.strip()[:300]}")
        else:
            print(f"    Repaired.")
            state.add(task_id)
            repaired += 1

    if not args.dry_run:
        save_state(state)
    print(f"\n{len(tasks)} done investigator task(s) checked, {repaired} repaired.")


if __name__ == "__main__":
    main()
