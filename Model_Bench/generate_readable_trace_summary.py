#!/usr/bin/env python3
"""Turns raw Hermes_Agent_Trace_Trn_Tbl events into one human-readable
activity note per investigation attempt (run_id), written into the
existing Hermes_Ticket_Activity_Trn_Tbl -- not a new table.

Why this exists (2026-09-04): the user explicitly asked for "humanly
readable and proper and in depth trace of what's going on... even if a
ticket doesn't get resolved." The trace table (Hermes_Agent_Trace_Trn_Tbl)
is complete and ground-truth, but it's raw JSON tool-call/arg/result dumps
-- exactly what a person browsing the Ticket Activity timeline in XStudio
Helpdesk does NOT want to read. Deterministic, no extra LLM call: this
just formats what already happened into plain sentences. It runs whether
or not the investigation ever reached --publish-response, which is the
whole point -- Hermes_Ticket_Activity_Trn_Tbl today only gets written to
on a real publish (kanban_approval_publisher.py's post_publish_data_entry)
or when the model remembers to call --log-activity mid-investigation;
neither happens for the ~83% of runs that don't complete cleanly.

A run is summarized once its trace shows a terminal signal -- a
kanban_complete or kanban_block tool call, or (fallback, for a run that
never got that far) once no new trace event has appeared for it for
--stale-minutes. Tracked in a local idempotency file so a run is never
summarized twice.

Usage (intended as a --no-agent cron job, every ~3-5 min):
    python generate_readable_trace_summary.py [--dry-run]
"""
import os
import argparse
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
import pyodbc

SERVER = "10.2.6.204"
DATABASE = "XStudio_Helpdesk"
USERNAME = "sa"
PASSWORD = os.environ.get("MSSQL_MCP_PASSWORD")
STALE_MINUTES = 20  # fallback: summarize a run even without an explicit terminal event

STATE_PATH = Path(__file__).parent / ".summarized_runs.json"

_TERMINAL_TOOLS = {"kanban_complete", "kanban_block"}


def load_state() -> set:
    if STATE_PATH.exists():
        return set(json.loads(STATE_PATH.read_text(encoding="utf-8")))
    return set()


def save_state(state: set) -> None:
    STATE_PATH.write_text(json.dumps(sorted(state)), encoding="utf-8")


def _fmt_tool_call(row) -> str:
    """One readable line for a post_tool_call row. Falls back to a plain
    "Called X" for any tool this doesn't have special-case phrasing for --
    never silently drops an event just because it's unfamiliar."""
    tool = row.tool_name or "(unknown tool)"
    status_word = {"ok": "succeeded", "error": "FAILED", "blocked": "was blocked", "cancelled": "was cancelled"}.get(row.status, row.status or "")
    dur = f" ({row.duration_ms}ms)" if row.duration_ms else ""

    if tool == "terminal":
        args = _safe_json(row.args_json)
        cmd = (args or {}).get("command", "") if isinstance(args, dict) else ""
        if "--query" in cmd:
            # Pull out the quoted SQL for a compact summary, not the whole command line.
            import re
            m = re.search(r"--query\s+\"(.*?)\"", cmd)
            sql = (m.group(1) if m else cmd)[:160]
            return f"Ran a SQL query{dur}: {sql}{status_word and ' -- ' + status_word or ''}"
        if "--log-activity" in cmd:
            return f"Logged a work-log note{dur}"
        if "--publish-response" in cmd:
            return f"Published the response back to the ticket{dur} -- {status_word}"
        return f"Ran a terminal command{dur}: {cmd[:160]}"

    if tool == "kanban_complete":
        result = _safe_json(row.result_json)
        summary = (result or {}).get("summary") if isinstance(result, dict) else None
        return f"Marked the investigation complete{dur}" + (f": {summary}" if summary else "")

    if tool == "kanban_block":
        result = _safe_json(row.result_json)
        reason = (result or {}).get("reason") if isinstance(result, dict) else None
        return f"Blocked, needs input{dur}" + (f": {reason}" if reason else "")

    return f"Called {tool}{dur} -- {status_word}"


def _safe_json(text):
    if not text:
        return None
    try:
        return json.loads(text)
    except (json.JSONDecodeError, TypeError):
        return None


def build_summary(events, compute_row) -> str:
    lines = []
    for e in events:
        ts = e.EventOn.strftime("%H:%M:%S") if e.EventOn else "??:??:??"
        if e.event_type == "pre_tool_call" and e.tool_name == "kanban_block":
            args = _safe_json(e.args_json) or {}
            reason = isinstance(args, dict) and args.get("reason")
            if reason:
                lines.append(f"[{ts}] Blocked, needs input: {reason}")
        elif e.event_type == "post_tool_call":
            lines.append(f"[{ts}] {_fmt_tool_call(e)}")
        elif e.event_type == "post_api_request":
            usage = _safe_json(e.usage_json) or {}
            total = usage.get("total_tokens")
            lines.append(f"[{ts}] Model call to {e.model or 'the model'}" + (f" ({total} tokens)" if total else ""))
        elif e.event_type == "api_request_error":
            lines.append(f"[{ts}] Model call FAILED ({e.error_message or 'unknown error'})")
        elif e.event_type in ("lmstudio_sample", "gpu_sample"):
            result = _safe_json(e.result_json) or {}
            if e.event_type == "gpu_sample" and "gpu_util_pct" in result:
                lines.append(f"[{ts}] GPU snapshot ({e.tool_name}): {result.get('gpu_util_pct')}% util, "
                              f"{result.get('mem_used_mb')}/{result.get('mem_total_mb')} MiB")
    if compute_row and compute_row.TotalTokens:
        lines.append(
            f"\nTotals: {compute_row.ToolCallCount or 0} tool call(s), "
            f"{compute_row.ApiRequestCount or 0} model call(s), "
            f"{compute_row.TotalTokens or 0} token(s), "
            f"{compute_row.WallClockSeconds or 0}s wall-clock."
        )
    return "\n".join(lines) if lines else "(No trace events captured for this run.)"


def _find_block_reason(events):
    """None unless this run's terminal event was a real kanban_block (not
    kanban_complete) -- that's the "genuinely stuck, needs a human" signal
    Hermes_L2_Log_Blocked_Escalation_Usp exists for. Returns the block's own
    reason text, exactly as the agent gave it.

    The reason lives in the PRE-call event's ArgsJson (what the agent
    passed in), not the post-call ResultJson (just an {"ok": true, ...}
    ack with no reason field) -- confirmed live 2026-09-04 against a real
    kanban_block trace pair for the same tool_call_id."""
    for e in events:
        if e.tool_name == "kanban_block" and e.event_type == "pre_tool_call":
            args = _safe_json(e.args_json) or {}
            if isinstance(args, dict) and args.get("reason"):
                return args["reason"]
    for e in events:
        if e.tool_name == "kanban_block" and e.event_type == "post_tool_call":
            return "Blocked (no reason text captured)."
    return None


def find_runs_to_summarize(cur, already_summarized: set):
    """Runs with a terminal kanban_complete/kanban_block event, or old enough
    that nothing new is coming (fallback for a run that never reached one)."""
    cur.execute(
        """
        SELECT DISTINCT RunID, TicketID
        FROM dbo.Hermes_Agent_Trace_Trn_Tbl
        WHERE RunID IS NOT NULL
          AND (
              EXISTS (SELECT 1 FROM dbo.Hermes_Agent_Trace_Trn_Tbl t2
                      WHERE t2.RunID = Hermes_Agent_Trace_Trn_Tbl.RunID
                        AND t2.EventType = 'post_tool_call' AND t2.ToolName IN ('kanban_complete', 'kanban_block'))
              OR EventOn < DATEADD(MINUTE, -?, GETDATE())
          )
        """,
        STALE_MINUTES,
    )
    return [(str(r[0]), str(r[1]) if r[1] else None) for r in cur.fetchall() if str(r[0]) not in already_summarized]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    state = load_state()
    conn = pyodbc.connect(
        f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};"
        f"UID={USERNAME};PWD={PASSWORD};TrustServerCertificate=yes"
    )
    try:
        cur = conn.cursor()
        runs = find_runs_to_summarize(cur, state)
        if not runs:
            print("No runs ready to summarize.")
            return

        for run_id, ticket_id in runs:
            cur.execute(
                "SELECT EventType AS event_type, EventOn, ToolName AS tool_name, Status AS status, "
                "DurationMs AS duration_ms, ArgsJson AS args_json, "
                "ResultJson AS result_json, ErrorMessage AS error_message, Model AS model, "
                "UsageJson AS usage_json "
                "FROM dbo.Hermes_Agent_Trace_Trn_Tbl WHERE RunID = ? ORDER BY EventOn ASC",
                run_id,
            )
            events = cur.fetchall()
            cur.execute("SELECT * FROM dbo.Hermes_L2_Compute_Per_Ticket_Vw WHERE RunID = ?", run_id)
            compute_row = cur.fetchone()

            summary = build_summary(events, compute_row)
            print(f"{'[DRY RUN] ' if args.dry_run else ''}Summarizing run {run_id} (ticket {ticket_id}): {len(events)} event(s)")
            if args.dry_run:
                print(summary[:500])
                continue

            if ticket_id:
                cur.execute(
                    "EXEC dbo.Hermes_Log_Ticket_Activity_Usp @TicketID=?, @ActivityType='Note', "
                    "@ActorType='Bot', @NoteText=?, @RunID=?;",
                    ticket_id, summary[:3900], run_id,
                )

                block_reason = _find_block_reason(events)
                if block_reason:
                    cur.execute(
                        "EXEC dbo.Hermes_L2_Log_Blocked_Escalation_Usp "
                        "@RunID=?, @TicketID=?, @BlockReason=?, @Findings=?;",
                        run_id, ticket_id, block_reason[:3900], summary[:3900],
                    )
                    print(f"  -> blocked on a real gap, escalated to L3: {block_reason[:120]}")
                conn.commit()
            state.add(run_id)

        if not args.dry_run:
            save_state(state)
        print(f"\n{len(runs)} run(s) summarized.")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
