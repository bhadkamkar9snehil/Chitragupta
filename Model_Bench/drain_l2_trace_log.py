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
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
import pyodbc

TRACE_LOG_PATH = Path(r"\\wsl.localhost\Ubuntu\home\snehil\.hermes\plugin-data\xstudio-l2-trace\events.jsonl")
CURSOR_PATH = Path(__file__).parent / ".l2_trace_drain_cursor.json"

SERVER = "10.2.6.204"
DATABASE = "XStudio_Helpdesk"
USERNAME = "sa"
PASSWORD = os.environ.get("MSSQL_MCP_PASSWORD")


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
            written_at = e.get("written_at")
            event_on = None
            if written_at is not None:
                from datetime import datetime, timezone
                event_on = datetime.fromtimestamp(written_at, tz=timezone.utc)

            usage = e.get("usage")
            args_json = e.get("args")
            result_json = e.get("result")
            error = e.get("error")
            error_message = e.get("error_message") or (json.dumps(error) if error else None)
            # lmstudio_sample/gpu_sample events (2026-09-04) have no tool_name of
            # their own -- reuse that column for "boundary" (session_start/
            # session_end) rather than adding a dedicated column for two event
            # types only.
            tool_name = e.get("tool_name") or e.get("boundary")

            cur.execute(
                "EXEC dbo.Hermes_Log_Agent_Trace_Usp "
                "@EventType=?, @EventOn=?, @SessionID=?, @TaskID=?, @TurnID=?, @ToolCallID=?, "
                "@ApiRequestID=?, @ToolName=?, @Status=?, @DurationMs=?, @ArgsJson=?, "
                "@ResultJson=?, @ErrorMessage=?, @Model=?, @Provider=?, @UsageJson=?, "
                "@RunID=?, @TicketID=?;",
                (
                    e.get("event_type"), event_on, e.get("session_id"), e.get("task_id"),
                    e.get("turn_id"), e.get("tool_call_id"), e.get("api_request_id"),
                    tool_name, e.get("status"), e.get("duration_ms"),
                    json.dumps(args_json) if args_json is not None else None,
                    json.dumps(result_json) if result_json is not None else None,
                    error_message,
                    e.get("model"), e.get("provider"),
                    json.dumps(usage) if usage is not None else None,
                    e.get("run_id"), e.get("ticket_id"),
                ),
            )
            inserted += 1
        conn.commit()
    finally:
        conn.close()

    save_cursor(new_offset)
    print(f"Inserted {inserted} trace event(s). Cursor advanced to byte offset {new_offset}.")


if __name__ == "__main__":
    main()
