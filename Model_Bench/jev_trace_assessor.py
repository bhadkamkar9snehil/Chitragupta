#!/usr/bin/env python3
"""Assess completed Chitragupta runs with Jev using persisted agent traces.

Runs after drain_l2_trace_log.py, never inside the hot observer hook. The job is
idempotent through Hermes_Jev_Judgment_Trn_Tbl.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Any

import pyodbc

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from Model_Bench.jev.audit import persist_rows, rows_for_result
from Model_Bench.jev.policy import TRACE_ASSESSMENT_ENABLED
from Model_Bench.jev.trace_assessment import assess_trace

SERVER = os.environ.get("MSSQL_MCP_SERVER", "10.2.6.204")
DATABASE = os.environ.get("MSSQL_MCP_DATABASE", "XStudio_Helpdesk")
USERNAME = os.environ.get("MSSQL_MCP_USER", "sa")
PASSWORD = os.environ.get("MSSQL_MCP_PASSWORD")


def connect():
    if not PASSWORD:
        raise RuntimeError("MSSQL_MCP_PASSWORD is required")
    return pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};"
        "TrustServerCertificate=yes;Encrypt=no;",
        timeout=10,
    )


def _dict_rows(cur) -> list[dict[str, Any]]:
    cols = [d[0] for d in cur.description]
    return [dict(zip(cols, row)) for row in cur.fetchall()]


def pending_runs(cur, top: int = 20) -> list[dict[str, Any]]:
    cur.execute(
        """
        SELECT TOP (?)
            r.ID AS RunID, r.TicketID, r.ProcessStatus, r.ResponseType,
            r.ProblemSummary, r.Findings, r.RootCause, r.Resolution, r.ReplyText,
            r.InvestigationJson, r.ErrorMessage, r.CompletedOn,
            c.TicketNo, c.BriefDetails, c.Description, c.ProblemCategory,
            c.Status AS TicketStatus, c.AskStatus, c.SupportExecutiveRemarks
        FROM dbo.Hermes_L2_Response_Trn_Tbl r
        JOIN dbo.Complaint_Mst_Tbl c ON c.ID = r.TicketID
        WHERE r.IsDeleted = 0
          AND (
              r.CompletedOn IS NOT NULL
              OR r.ProcessStatus IN ('COMPLETED','WAITING_USER','FAILED','ESCALATED','NEEDS_HUMAN_ACTION')
          )
          AND EXISTS (
              SELECT 1 FROM dbo.Hermes_Agent_Trace_Trn_Tbl t
              WHERE t.RunID = r.ID AND t.IsDeleted = 0
          )
          AND NOT EXISTS (
              SELECT 1 FROM dbo.Hermes_Jev_Judgment_Trn_Tbl j
              WHERE j.RunID = r.ID AND j.Stage = 'TRACE_ASSESSMENT'
                AND j.IsDeleted = 0
          )
        ORDER BY COALESCE(r.CompletedOn, r.ModifiedOn, r.CreatedOn) ASC;
        """,
        top,
    )
    return _dict_rows(cur)


def trace_events(cur, run_id: str) -> list[dict[str, Any]]:
    cur.execute(
        """
        SELECT EventType, EventOn, SessionID, TaskID, TurnID, ToolCallID,
               ToolName, Status, DurationMs, ArgsJson, ResultJson, ErrorMessage,
               Model, Provider, UsageJson
        FROM dbo.Hermes_Agent_Trace_Trn_Tbl
        WHERE RunID = ? AND IsDeleted = 0
        ORDER BY EventOn ASC;
        """,
        run_id,
    )
    rows = _dict_rows(cur)
    if len(rows) > 70:
        rows = rows[:10] + rows[-60:]
    compact = []
    for row in rows:
        item = dict(row)
        for key in ("ArgsJson", "ResultJson", "ErrorMessage"):
            if item.get(key) is not None:
                text = str(item[key])
                item[key] = text[:1600] + ("...[truncated]" if len(text) > 1600 else "")
        compact.append(item)
    return compact


def ticket_feedback(cur, ticket_id: str) -> list[dict[str, Any]]:
    """Later CSAT/reopen feedback, when available, is valuable calibration context."""
    cur.execute(
        """
        SELECT TOP 10 SatisfactionRating, FeedbackText, IsReopen,
               ReopenedFromTicketID, SubmittedOn
        FROM dbo.Hermes_Ticket_Feedback_Trn_Tbl
        WHERE TicketID = ? AND IsDeleted = 0
        ORDER BY SubmittedOn DESC;
        """,
        ticket_id,
    )
    return _dict_rows(cur)


def sql_actions(cur, run_id: str) -> list[dict[str, Any]]:
    cur.execute(
        """
        SELECT TOP 40 ActionNo, ActionType, DatabaseName, SchemaName, ObjectName,
               OperationName, Purpose, Status, RowsAffected, ErrorMessage,
               StartedOn, CompletedOn
        FROM dbo.Hermes_L2_SQL_Action_Trn_Tbl
        WHERE RunID = ? AND IsDeleted = 0
        ORDER BY ActionNo ASC;
        """,
        run_id,
    )
    return _dict_rows(cur)


def state_for(cur, run: dict[str, Any]) -> dict[str, Any]:
    proposal = {
        k: run.get(k)
        for k in (
            "ResponseType", "ProblemSummary", "Findings", "RootCause",
            "Resolution", "ReplyText", "InvestigationJson", "ErrorMessage",
        )
    }
    ticket = {
        k: run.get(k)
        for k in (
            "TicketNo", "BriefDetails", "Description", "ProblemCategory",
            "TicketStatus", "AskStatus", "SupportExecutiveRemarks",
        )
    }
    return {
        "ticket": ticket,
        "proposal_or_result": proposal,
        "run_state": {
            "process_status": run.get("ProcessStatus"),
            "completed_on": run.get("CompletedOn"),
        },
        "worker_policy": {
            "database_transport": "xstudio_l2 typed tool only",
            "raw_sql_writes": "forbidden to ordinary investigator",
            "arbitrary_exec": "forbidden",
            "publication": "deterministic publisher after independent review",
            "live_evidence": "required for current ticket factual claims",
        },
        "tool_and_model_trace": trace_events(cur, str(run["RunID"])),
        "sql_action_audit": sql_actions(cur, str(run["RunID"])),
        "customer_feedback_and_reopen": ticket_feedback(cur, str(run["TicketID"])),
    }


def main() -> int:
    if not TRACE_ASSESSMENT_ENABLED:
        print("Jev trace assessment disabled.")
        return 0
    if not os.environ.get("TYPESAFE_API_KEY"):
        print("TYPESAFE_API_KEY not configured; skipping Jev trace assessment.")
        return 0

    conn = connect()
    assessed = 0
    try:
        cur = conn.cursor()
        for run in pending_runs(cur):
            state = state_for(cur, run)
            result = assess_trace(state)
            if not result.get("ok"):
                print(f"Jev trace assessment unavailable for {run['RunID']}: {result.get('reason')}")
                continue
            audit = persist_rows(rows_for_result(
                result=result,
                stage="TRACE_ASSESSMENT",
                state=state,
                ticket_id=str(run["TicketID"]),
                run_id=str(run["RunID"]),
            ))
            assessed += int(audit.get("persisted") or 0) > 0
            failure = (result.get("answers") or {}).get("failure_class") or {}
            human = (result.get("answers") or {}).get("human_attention_needed") or {}
            print(
                f"Jev trace {run['RunID']}: "
                f"class={failure.get('choice')} attention={human.get('noul')} "
                f"audit={audit.get('persisted', 0)}"
            )
    finally:
        conn.close()
    print(f"Jev trace assessment complete: {assessed} newly assessed run(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
