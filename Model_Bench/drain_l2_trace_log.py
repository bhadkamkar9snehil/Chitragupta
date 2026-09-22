#!/usr/bin/env python3
"""Drains the xstudio-l2-trace Hermes observer-hook plugin's local JSONL
event log into XStudio_Helpdesk.dbo.Hermes_Agent_Trace_Trn_Tbl.

Why this exists (2026-09-04): the plugin (Model_Bench/xstudio_l2_trace_plugin/,
deployed to ~/.hermes/plugins/xstudio-l2-trace/) runs inside the WSL-native
Hermes gateway process, whose venv has pyodbc installed but no ODBC driver
manager (confirmed live: `ImportError: libodbc.so.2`), so it cannot write to
SQL Server directly and never should be made to -- a slow/blocking DB call
inside an observer hook would sit on the agent's hot path. Instead the
plugin appends one JSON line per event to a local file; this script (run as
the Windows Python interpreter, which already has a working ODBC driver, via
the same WSL-cron-wrapper pattern every other bridge script in this project
uses) reads the file over the \\wsl.localhost UNC path, inserts each new
event through the official Hermes_Log_Agent_Trace_Usp SP, and remembers how
far it has read via a small local cursor file -- so a restart or a slow tick
never re-inserts or drops events.

Usage (intended as a --no-agent cron job, every ~2 min):
    python drain_l2_trace_log.py [--dry-run]
"""
import os
import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path(__file__).parent.parent))
import pyodbc

TRACE_LOG_PATH = Path(r"\\wsl.localhost\Ubuntu\home\snehil\.hermes\plugin-data\xstudio-l2-trace\events.jsonl")
CURSOR_PATH = Path(__file__).parent / ".l2_trace_drain_cursor.json"

SERVER = "10.2.6.204"
DATABASE = "XStudio_Helpdesk"
USERNAME = "sa"
PASSWORD = os.environ.get("MSSQL_MCP_PASSWORD")
IST = ZoneInfo("Asia/Kolkata")


def usage_payload_for_event(event):
    """Keep provider usage and harness-compute dimensions in one JSON value.

    The live trace table already has a UsageJson column and the current
    experiment is intentionally avoiding a schema migration. Names are kept
    explicit so a later normalized table/view can lift them losslessly.
    """
    usage = dict(event.get("usage") or {})
    for key in ("profile_name", "ttft_ms", "api_duration_ms"):
        value = event.get(key)
        if value is not None:
            usage[key] = value
    return usage or None


def trace_procedure_parameters(event):
    """Build the audited trace-procedure arguments from one durable outbox event."""
    event_on_ist = None
    raw_event_on_ist = event.get("event_on_ist")
    if raw_event_on_ist:
        event_on_ist = datetime.fromisoformat(raw_event_on_ist)
    elif event.get("written_at") is not None:
        # Legacy outbox rows predate the IST contract. Interpret their epoch in
        # IST rather than creating new UTC-facing persistence.
        event_on_ist = datetime.fromtimestamp(event["written_at"], tz=IST)
    if event_on_ist is None:
        event_on_ist = datetime.now(IST)
    if event_on_ist.tzinfo is None:
        event_on_ist = event_on_ist.replace(tzinfo=IST)

    usage = usage_payload_for_event(event)
    args_json = event.get("args")
    result_json = event.get("result")
    error = event.get("error")
    error_message = event.get("error_message") or (json.dumps(error) if error else None)
    tool_name = event.get("tool_name") or event.get("boundary")
    return (
        event.get("trace_event_id"), event_on_ist,
        event.get("event_type"), event_on_ist.replace(tzinfo=None),
        event.get("session_id"), event.get("task_id"), event.get("turn_id"),
        event.get("tool_call_id"), event.get("api_request_id"), tool_name,
        event.get("status"), event.get("duration_ms"),
        json.dumps(args_json) if args_json is not None else None,
        json.dumps(result_json) if result_json is not None else None,
        error_message, event.get("model"), event.get("provider"),
        json.dumps(usage) if usage is not None else None,
        event.get("run_id"), event.get("ticket_id"),
    )


def load_cursor() -> int:
    if CURSOR_PATH.exists():
        return json.loads(CURSOR_PATH.read_text(encoding="utf-8")).get("byte_offset", 0)
    return 0


def save_cursor(byte_offset: int) -> None:
    CURSOR_PATH.write_text(json.dumps({"byte_offset": byte_offset}), encoding="utf-8")


def read_new_complete_lines(start_offset: int):
    """Returns (lines, new_offset). Only returns complete (newline-terminated)
    lines -- a line still being written when we read it is left for next
    tick rather than risking a truncated/invalid JSON parse."""
    if not TRACE_LOG_PATH.exists():
        return [], start_offset

    with open(TRACE_LOG_PATH, "rb") as f:
        f.seek(start_offset)
        data = f.read()

    if not data:
        return [], start_offset

    last_newline = data.rfind(b"\n")
    if last_newline == -1:
        return [], start_offset  # no complete line yet

    complete = data[: last_newline + 1]
    new_offset = start_offset + last_newline + 1
    lines = [line for line in complete.decode("utf-8", errors="replace").splitlines() if line.strip()]
    return lines, new_offset


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    start_offset = load_cursor()
    lines, new_offset = read_new_complete_lines(start_offset)

    if not lines:
        print("No new trace events.")
        return

    print(f"{len(lines)} new trace event(s) since byte offset {start_offset}.")

    parsed = []
    parse_errors = 0
    for line in lines:
        try:
            parsed.append(json.loads(line))
        except json.JSONDecodeError:
            parse_errors += 1
    if parse_errors:
        print(f"  WARNING: {parse_errors} line(s) failed to parse as JSON, skipped.")

    # Resolve per-task identity across the whole drained batch before inserting.
    # trace_context may arrive after the first tool/model events because the hot
    # hook resolves Kanban metadata asynchronously.
    task_identity = {}
    for e in parsed:
        task_id = e.get("task_id")
        if task_id and (e.get("run_id") or e.get("ticket_id")):
            task_identity[str(task_id)] = {
                "run_id": e.get("run_id"),
                "ticket_id": e.get("ticket_id"),
            }
    for e in parsed:
        task_id = e.get("task_id")
        identity = task_identity.get(str(task_id)) if task_id else None
        if identity:
            e["run_id"] = e.get("run_id") or identity.get("run_id")
            e["ticket_id"] = e.get("ticket_id") or identity.get("ticket_id")

    if args.dry_run:
        for e in parsed[:5]:
            print(f"  [DRY RUN] {e.get('event_type')} tool={e.get('tool_name')} status={e.get('status')}")
        print(f"  [DRY RUN] Would advance cursor to byte offset {new_offset}.")
        return

    conn = pyodbc.connect(
        f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};"
        f"UID={USERNAME};PWD={PASSWORD};TrustServerCertificate=yes"
    )
    inserted = 0
    try:
        cur = conn.cursor()
        for e in parsed:
            cur.execute(
                "EXEC dbo.Hermes_Log_Agent_Trace_Usp "
                "@TraceEventID=?, @EventOnIst=?, @EventType=?, @EventOn=?, @SessionID=?, @TaskID=?, @TurnID=?, @ToolCallID=?, "
                "@ApiRequestID=?, @ToolName=?, @Status=?, @DurationMs=?, @ArgsJson=?, "
                "@ResultJson=?, @ErrorMessage=?, @Model=?, @Provider=?, @UsageJson=?, "
                "@RunID=?, @TicketID=?;",
                trace_procedure_parameters(e),
            )
            inserted += 1
        # Backfill any trace rows from an earlier drain tick that belonged to
        # this same task but were inserted before correlation resolved.
        for task_id, identity in task_identity.items():
            if not (identity.get("run_id") or identity.get("ticket_id")):
                continue
            cur.execute(
                """
                UPDATE dbo.Hermes_Agent_Trace_Trn_Tbl
                SET
                    RunID = COALESCE(RunID, ?),
                    TicketID = COALESCE(TicketID, ?)
                WHERE TaskID = ?
                  AND IsDeleted = 0
                  AND (RunID IS NULL OR TicketID IS NULL);
                """,
                (identity.get("run_id"), identity.get("ticket_id"), task_id),
            )
        conn.commit()
    finally:
        conn.close()

    save_cursor(new_offset)
    print(f"Inserted {inserted} trace event(s). Cursor advanced to byte offset {new_offset}.")


if __name__ == "__main__":
    main()
