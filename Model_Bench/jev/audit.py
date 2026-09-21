"""Persist Jev judgments as first-class audit data when SQL connectivity exists."""
from __future__ import annotations

import hashlib
import json
import os
from typing import Any

from .policy import AUDIT_ENABLED, POLICY_VERSION


def input_hash(state: Any) -> str:
    raw = json.dumps(state, sort_keys=True, separators=(",", ":"), default=str)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _answer_fields(answer: dict[str, Any]) -> dict[str, Any]:
    kind = answer.get("type")
    return {
        "AnswerType": kind,
        "ChoiceValue": answer.get("choice") if kind == "choice" else None,
        "NoulProbability": answer.get("noul") if kind == "noul" else None,
        "ScoreValue": answer.get("score") if kind == "score" else None,
        "Confidence": answer.get("confidence") if kind in {"choice", "score"} else None,
        "ProbabilitiesJson": json.dumps(answer.get("probabilities"), separators=(",", ":"), default=str)
            if answer.get("probabilities") is not None else None,
    }


def rows_for_result(
    *,
    result: dict[str, Any],
    stage: str,
    state: Any,
    ticket_id: str | None = None,
    run_id: str | None = None,
    question_version: str = "v1",
    accepted: bool | None = None,
) -> list[dict[str, Any]]:
    ih = input_hash(state)
    rows = []
    for name, answer in (result.get("answers") or {}).items():
        if not isinstance(answer, dict):
            continue
        rows.append({
            "TicketID": ticket_id,
            "RunID": run_id,
            "Stage": stage,
            "JudgmentName": str(name),
            "QuestionVersion": question_version,
            "Model": result.get("model"),
            **_answer_fields(answer),
            "InputHash": ih,
            "PolicyVersion": POLICY_VERSION,
            "Accepted": accepted,
            "LatencyMs": result.get("latency_ms"),
        })
    return rows


def persist_rows(rows: list[dict[str, Any]]) -> dict[str, Any]:
    if not AUDIT_ENABLED or not rows:
        return {"ok": True, "persisted": 0, "reason": "audit disabled or no rows"}
    try:
        import pyodbc  # type: ignore
    except ImportError:
        return {"ok": False, "persisted": 0, "reason": "pyodbc unavailable"}

    password = os.environ.get("MSSQL_MCP_PASSWORD")
    if not password:
        return {"ok": False, "persisted": 0, "reason": "MSSQL_MCP_PASSWORD unavailable"}
    server = os.environ.get("MSSQL_MCP_SERVER", "10.2.6.204")
    database = os.environ.get("MSSQL_MCP_DATABASE", "XStudio_Helpdesk")
    username = os.environ.get("MSSQL_MCP_USER", "sa")
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={server};DATABASE={database};UID={username};PWD={password};"
        "TrustServerCertificate=yes;Encrypt=no;",
        timeout=10,
    )
    insert_sql = """
    INSERT INTO dbo.Hermes_Jev_Judgment_Trn_Tbl
    (TicketID, RunID, Stage, JudgmentName, QuestionVersion, Model, AnswerType,
     ChoiceValue, NoulProbability, ScoreValue, Confidence, ProbabilitiesJson,
     InputHash, PolicyVersion, Accepted, LatencyMs)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    exists_sql = """
    SELECT TOP 1 1
    FROM dbo.Hermes_Jev_Judgment_Trn_Tbl
    WHERE RunID = ? AND Stage = ? AND JudgmentName = ? AND InputHash = ?
      AND PolicyVersion = ? AND IsDeleted = 0;
    """
    persisted = 0
    try:
        cur = conn.cursor()
        for row in rows:
            run_id = row.get("RunID")
            if run_id:
                cur.execute(
                    exists_sql,
                    run_id,
                    row.get("Stage"),
                    row.get("JudgmentName"),
                    row.get("InputHash"),
                    row.get("PolicyVersion"),
                )
                if cur.fetchone():
                    continue
            cur.execute(insert_sql, *(row.get(k) for k in (
                "TicketID", "RunID", "Stage", "JudgmentName", "QuestionVersion", "Model",
                "AnswerType", "ChoiceValue", "NoulProbability", "ScoreValue", "Confidence",
                "ProbabilitiesJson", "InputHash", "PolicyVersion", "Accepted", "LatencyMs"
            )))
            persisted += 1
        conn.commit()
        return {"ok": True, "persisted": persisted, "skipped_existing": len(rows) - persisted}
    finally:
        conn.close()
