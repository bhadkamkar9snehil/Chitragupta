#!/usr/bin/env python3
"""Export one live Helpdesk L2 run into the harness evaluator's JSON bundle."""
from __future__ import annotations

import argparse
import json
import os
from datetime import date, datetime
from pathlib import Path
from typing import Any

import pyodbc


def _json(value: Any, fallback: Any) -> Any:
    if value in (None, ""):
        return fallback
    if isinstance(value, (dict, list)):
        return value
    try:
        return json.loads(value)
    except (TypeError, json.JSONDecodeError):
        return fallback


def _dicts(cursor) -> list[dict[str, Any]]:
    columns = [item[0] for item in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def _serial(value: Any) -> Any:
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    return str(value)


def _proposal(investigation_json: Any) -> dict[str, Any]:
    ledger = _json(investigation_json, {})
    if not isinstance(ledger, dict):
        return {}
    frozen = ledger.get("frozen_proposal")
    return frozen if isinstance(frozen, dict) else ledger


def export_run(conn, run_id: str) -> dict[str, Any]:
    cur = conn.cursor()
    cur.execute(
        "SELECT ID, TicketID, AttemptNo, WorkerID, ProcessStatus, ResponseType, ReplyText, "
        "InvestigationJson, ActionsTakenJson, ApprovalStatus, IsActive, IsResolved, "
        "ClaimedOn, CompletedOn, NextEligibleOn, ErrorMessage FROM dbo.Hermes_L2_Response_Trn_Tbl "
        "WHERE ID = ? AND IsDeleted = 0", run_id,
    )
    runs = _dicts(cur)
    if not runs:
        raise SystemExit(f"run not found: {run_id}")
    run = runs[0]

    cur.execute(
        "SELECT ID, RunID, TicketID, ActionNo, ActionType, DatabaseName, SchemaName, "
        "ObjectName, OperationName, Purpose, ParametersJson, AfterJson, Status, RowsAffected, "
        "CreatedOn, ModifiedOn FROM dbo.Hermes_L2_SQL_Action_Trn_Tbl "
        "WHERE RunID = ? AND IsDeleted = 0 ORDER BY ActionNo", run_id,
    )
    actions = _dicts(cur)

    cur.execute(
        "SELECT EventType, EventOn, SessionID, TaskID, TurnID, ToolCallID, ApiRequestID, "
        "ToolName, Status, DurationMs, ArgsJson, ResultJson, ErrorMessage, Model, Provider, UsageJson "
        "FROM dbo.Hermes_Agent_Trace_Trn_Tbl WHERE RunID = ? AND IsDeleted = 0 ORDER BY EventOn, ID",
        run_id,
    )
    events = []
    for row in _dicts(cur):
        usage = _json(row.pop("UsageJson", None), {})
        event = {
            "event_type": row.pop("EventType"),
            "written_at": row.pop("EventOn"),
            "session_id": row.pop("SessionID"),
            "task_id": row.pop("TaskID"),
            "turn_id": row.pop("TurnID"),
            "tool_call_id": row.pop("ToolCallID"),
            "api_request_id": row.pop("ApiRequestID"),
            "tool_name": row.pop("ToolName"),
            "status": row.pop("Status"),
            "duration_ms": row.pop("DurationMs"),
            "args": _json(row.pop("ArgsJson", None), {}),
            "result": _json(row.pop("ResultJson", None), {}),
            "error_message": row.pop("ErrorMessage"),
            "model": row.pop("Model"),
            "provider": row.pop("Provider"),
            "usage": {key: value for key, value in usage.items()
                      if key not in {"profile_name", "ttft_ms", "api_duration_ms"}},
            "profile_name": usage.get("profile_name"),
            "ttft_ms": usage.get("ttft_ms"),
            "api_duration_ms": usage.get("api_duration_ms"),
        }
        events.append(event)

    lifecycle = ["dispatch"]
    investigator_tasks = {
        event.get("task_id") for event in events
        if event.get("profile_name") == "l2-investigator-primary" and event.get("task_id")
    }
    if any(event.get("tool_name") == "kanban_complete" and event.get("status") == "ok" for event in events):
        lifecycle.append("investigator_complete")
    if len(investigator_tasks) > 1 or any(
        event.get("status") in {"blocked", "error"} and event.get("tool_name") == "kanban_complete"
        for event in events
    ):
        lifecycle.append("recovery")
    if any(event.get("profile_name") == "l2-reviewer-primary" for event in events):
        lifecycle.append("reviewer_created")
    ledger = _json(run.get("InvestigationJson"), {})
    approval = str(run.get("ApprovalStatus") or (
        ledger.get("review_decision") if isinstance(ledger, dict) else ""
    ) or "").upper()
    if approval:
        lifecycle.append(approval.lower())
    if str(run.get("ProcessStatus") or "").upper() in {"COMPLETED", "WAITING_USER"}:
        lifecycle.append("published")

    return {
        "run": run,
        "proposal": _proposal(run.get("InvestigationJson")),
        "review": {"decision": approval},
        "actions": actions,
        "events": events,
        "lifecycle_events": lifecycle,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    password = os.environ.get("MSSQL_MCP_PASSWORD")
    if not password:
        raise SystemExit("MSSQL_MCP_PASSWORD is required")
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={os.environ.get('MSSQL_MCP_SERVER', '10.2.6.204')};DATABASE=XStudio_Helpdesk;"
        f"UID={os.environ.get('MSSQL_MCP_USER', 'sa')};PWD={password};TrustServerCertificate=yes"
    )
    try:
        bundle = export_run(conn, args.run_id)
    finally:
        conn.close()
    rendered = json.dumps(bundle, indent=2, default=_serial) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
