#!/usr/bin/env python3
"""Seed mem0 with hard-won operational lessons for the L2 investigators.

Why: memory was broken (single-process Qdrant file lock) for this project's
entire history, so every lesson the pipeline paid for in failed runs was
lost. Now that the store actually works, the models start from an empty
memory anyway unless something puts those lessons in. This does.

What belongs here (and what does not):
  YES -- durable, reusable operating facts a future investigation would
         otherwise rediscover by failing: exact command forms, environment
         gotchas, schema traps, which tool to reach for.
  NO  -- per-ticket findings. Those belong on the ticket (ledger /
         SupportExecutiveRemarks), not in shared memory, or every future
         search drowns in one-off detail.

Idempotent-ish: mem0 deduplicates semantically on add, so re-running does
not linearly grow the store. Safe to re-run after a fresh install.

Usage:
    ~/.hermes/hermes-agent/venv/bin/python seed_mem0_lessons.py [--dry-run]
"""
from __future__ import annotations

import json
import os
import pathlib
import sys

CONFIG = pathlib.Path.home() / ".hermes/profiles/l2-investigator-primary/mem0.json"

LESSONS = [
    # --- environment / exact invocation -------------------------------------
    "To query the XStudio databases, run Hermes_Orchestrator.py with the "
    "Windows Python interpreter at /mnt/c/Python314/python.exe. Plain `python` "
    "is not on PATH inside WSL; `python3` exists but lacks pyodbc, so database "
    "calls fail with a driver error.",

    "Hermes_Orchestrator.py lives at "
    "/mnt/c/Users/Admin/Documents/Office/AIHelpdesk/Hermes_Orchestrator.py when "
    "running inside WSL. A Windows-style path like "
    "C:/Users/Admin/... does not resolve there and exits with code 2. Do not "
    "search the filesystem for it.",

    "Every Hermes_Orchestrator.py database call needs --server 10.2.6.204 and an "
    "explicit --database. There is no default database: XStudio_Helpdesk holds "
    "Complaint_Mst_Tbl and the Hermes_* runtime tables, XStudio_Xbatch holds "
    "production/heat/billet/quality/delay data. Omitting --database used to "
    "silently query the wrong one and produce false 'Invalid object name' errors.",

    # --- how to actually find and query things ------------------------------
    "Prefer --build-query over raw --query. --build-query validates the table "
    "and every column against the real schema before emitting SQL, so a "
    "hallucinated identifier is rejected with the closest real name instead of "
    "silently returning nothing or erroring after the fact.",

    "When you do not know which table holds the answer, run --suggest-tables "
    "with the ticket's own text before writing any SQL. It scores real table and "
    "column names by keyword overlap and returns the top candidates with their "
    "actual columns. Guessing table names from memory is a known failure mode in "
    "this system.",

    "--investigate-bundle <ticket_id> returns the ticket, candidate tables, any "
    "prior attempt's ledger, recent prior attempts and known solution articles in "
    "ONE call. Use it to start an investigation instead of chaining "
    "--get-ticket-context, --suggest-tables and --get-ledger separately: each "
    "extra tool call resends the whole conversation and is what actually drives "
    "token cost per ticket.",

    # --- completion contract -------------------------------------------------
    "When calling kanban_complete, metadata MUST contain both response_type and "
    "reply_text. A real finding placed only in `summary`, or a response type "
    "written as a text prefix like 'UPDATE: ...', cannot be published: the "
    "deterministic publisher requires those two structured fields and has nothing "
    "to publish without them.",

    "Valid response_type values are exactly UPDATE, QUESTION, RESOLUTION, "
    "L3_ESCALATION and NEEDS_HUMAN_ACTION. Free-text values such as 'Finding' or "
    "'investigation complete' are rejected by the publishing stored procedure. "
    "Use NEEDS_HUMAN_ACTION when the cause is diagnosed but a human must act; use "
    "L3_ESCALATION when the cause could not be determined.",

    "Record findings with --save-ledger before finishing, especially if the answer "
    "is uncertain. A rejected attempt's ledger is carried verbatim into the rework "
    "card, so the next attempt builds on it instead of re-deriving everything from "
    "scratch.",

    # --- domain traps --------------------------------------------------------
    "Never write to Complaint_Mst_Tbl Status or SupportExecutiveRemarks directly. "
    "All ticket writes go through the reviewer plus the deterministic publisher "
    "via --publish-response. --query is read-only and rejects write keywords.",

    "A delay row with TotalDelayReason populated but Equipment NULL indicates a "
    "data-entry gap in equipment identification, not a genuine unattributed "
    "stoppage. Shift delay data for a heat lives in XStudio_Xbatch tables such as "
    "ShiftDelayEntry and Equipment_Wise_Delay.",
]


def main() -> int:
    dry = "--dry-run" in sys.argv
    if not CONFIG.exists():
        print(f"ERROR: {CONFIG} not found -- run setup_mem0.py first", file=sys.stderr)
        return 1
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    os.environ.setdefault("OPENAI_API_KEY", "lm-studio-local")

    if dry:
        for i, lesson in enumerate(LESSONS, 1):
            print(f"{i:2}. {lesson[:110]}...")
        print(f"\n{len(LESSONS)} lessons (dry run -- nothing written)")
        return 0

    from mem0 import Memory
    mem = Memory.from_config(cfg["oss"])
    user_id = cfg["user_id"]

    ok = 0
    for lesson in LESSONS:
        try:
            mem.add(lesson, user_id=user_id, metadata={"kind": "operational_lesson"})
            ok += 1
        except Exception as e:
            print(f"  FAILED: {type(e).__name__}: {e}\n    {lesson[:80]}...", file=sys.stderr)
    print(f"seeded {ok}/{len(LESSONS)} lessons")
    return 0 if ok == len(LESSONS) else 1


if __name__ == "__main__":
    sys.exit(main())
