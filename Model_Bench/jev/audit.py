"""Persist Jev semantics on the existing Hermes run + agent trace records.

Jev is another bounded reviewer/investigator for a run, not a separate business
entity. Stage summaries therefore live on Hermes_L2_Response_Trn_Tbl and every
System-One call is also an ordinary Hermes_Agent_Trace_Trn_Tbl event.
"""
from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime, timezone
from typing import Any

from .policy import AUDIT_ENABLED, POLICY_VERSION

_STAGE_COLUMNS = {
    "TICKET_TRIAGE": "JevTriageJson",
    "TICKET_SECURITY": "JevTriageJson",
    "KB_APPLICABILITY": "JevInvestigationJson",
    "JEV_EVIDENCE_PLAN": "JevInvestigationJson",
    "JEV_INVESTIGATION": "JevInvestigationJson",
    "PRIMARY_REVIEW": "JevReviewJson",
    "TRACE_ASSESSMENT": "JevTraceJson",
    "POST_RESOLUTION_KB": "JevKBCurationJson",
    "POST_RESOLUTION_KB_RERANK": "JevKBCurationJson",
}


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


def _connect():
    import pyodbc  # type: ignore

    password = os.environ.get("MSSQL_MCP_PASSWORD")
    if not password:
        raise RuntimeError("MSSQL_MCP_PASSWORD unavailable")
    server = os.environ.get("MSSQL_MCP_SERVER", "10.2.6.204")
    database = os.environ.get("MSSQL_MCP_DATABASE", "XStudio_Helpdesk")
    username = os.environ.get("MSSQL_MCP_USER", "sa")
    return pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={server};DATABASE={database};UID={username};PWD={password};"
        "TrustServerCertificate=yes;Encrypt=no;",
        timeout=10,
    )


def _row_to_answer(row: dict[str, Any]) -> dict[str, Any]:
    kind = row.get("AnswerType")
    if kind == "choice":
        answer = {
            "type": "choice",
            "choice": row.get("ChoiceValue"),
            "confidence": row.get("Confidence"),
        }
        if row.get("ProbabilitiesJson"):
            try:
                answer["probabilities"] = json.loads(row["ProbabilitiesJson"])
            except (TypeError, json.JSONDecodeError):
                pass
        return answer
    if kind == "noul":
        return {"type": "noul", "noul": row.get("NoulProbability")}
    if kind == "score":
        answer = {
            "type": "score",
            "score": row.get("ScoreValue"),
            "confidence": row.get("Confidence"),
        }
        if row.get("ProbabilitiesJson"):
            try:
                answer["probabilities"] = json.loads(row["ProbabilitiesJson"])
            except (TypeError, json.JSONDecodeError):
                pass
        return answer
    return {"type": str(kind or "unknown")}


def _merge_stage_json(existing: str | None, stage: str, payload: dict[str, Any]) -> str:
    try:
        current = json.loads(existing) if existing else {}
    except (TypeError, json.JSONDecodeError):
        current = {}
    if not isinstance(current, dict):
        current = {}
    current[stage] = payload
    return json.dumps(current, separators=(",", ":"), default=str)


def _same_stage_input(existing: str | None, stage: str, first: dict[str, Any]) -> bool:
    try:
        current = json.loads(existing) if existing else {}
    except (TypeError, json.JSONDecodeError):
        return False
    if not isinstance(current, dict):
        return False
    prior = current.get(stage)
    if not isinstance(prior, dict):
        return False
    return (
        prior.get("input_hash") == first.get("InputHash")
        and prior.get("policy_version") == first.get("PolicyVersion")
        and prior.get("question_version") == first.get("QuestionVersion")
    )


def _review_summary(answers: dict[str, Any]) -> tuple[Any, Any, Any, Any]:
    decision_a = answers.get("decision") or {}
    risk_a = answers.get("publication_risk") or {}
    decision = decision_a.get("choice") if decision_a.get("type") == "choice" else None
    confidence = decision_a.get("confidence") if decision_a.get("type") == "choice" else None
    risk = risk_a.get("score") if risk_a.get("type") == "score" else None
    local_required = 1 if decision == "LOCAL_REVIEW" else 0 if decision else None
    return decision, confidence, risk, local_required


def _update_run_stage(
    cur,
    *,
    first: dict[str, Any],
    stage: str,
    column: str,
    answers: dict[str, Any],
    payload: dict[str, Any],
) -> bool:
    run_id = first.get("RunID")
    cur.execute(
        f"SELECT {column} FROM dbo.Hermes_L2_Response_Trn_Tbl WHERE ID = ? AND IsDeleted = 0",
        run_id,
    )
    found = cur.fetchone()
    if found is None:
        return True
    if _same_stage_input(found[0], stage, first):
        return False

    merged = _merge_stage_json(found[0], stage, payload)
    if stage == "PRIMARY_REVIEW":
        decision, confidence, risk, local_required = _review_summary(answers)
        cur.execute(
            f"""
            UPDATE dbo.Hermes_L2_Response_Trn_Tbl
            SET {column} = ?,
                ReviewMode = 'JEV_PRIMARY',
                JevReviewDecision = ?,
                JevReviewConfidence = ?,
                JevRiskScore = ?,
                LocalReviewRequired = ?,
                JevModel = ?,
                JevReviewedOn = GETDATE(),
                ModifiedOn = GETDATE()
            WHERE ID = ? AND IsDeleted = 0;
            """,
            merged,
            decision,
            confidence,
            risk,
            local_required,
            first.get("Model"),
            run_id,
        )
    else:
        cur.execute(
            f"UPDATE dbo.Hermes_L2_Response_Trn_Tbl "
            f"SET {column} = ?, JevModel = COALESCE(?, JevModel), ModifiedOn = GETDATE() "
            f"WHERE ID = ? AND IsDeleted = 0",
            merged,
            first.get("Model"),
            run_id,
        )
    return True


def _insert_trace_event(
    cur,
    *,
    first: dict[str, Any],
    stage: str,
    payload: dict[str, Any],
) -> None:
    cur.execute(
        """
        INSERT INTO dbo.Hermes_Agent_Trace_Trn_Tbl
        (EventType, EventOn, ToolName, Status, DurationMs, ArgsJson, ResultJson,
         Model, Provider, RunID, TicketID, Source)
        VALUES ('jev_system_one', GETDATE(), ?, 'ok', ?, ?, ?, ?, 'typesafe', ?, ?, 'Jev');
        """,
        stage,
        int(float(first.get("LatencyMs") or 0)),
        json.dumps(
            {
                "stage": stage,
                "question_version": first.get("QuestionVersion"),
                "policy_version": first.get("PolicyVersion"),
                "input_hash": first.get("InputHash"),
            },
            separators=(",", ":"),
        ),
        json.dumps(payload, separators=(",", ":"), default=str),
        first.get("Model"),
        first.get("RunID"),
        first.get("TicketID"),
    )


def _persist_group(conn, rows: list[dict[str, Any]]) -> int:
    if not rows:
        return 0
    first = rows[0]
    stage = str(first.get("Stage") or "")
    column = _STAGE_COLUMNS.get(stage)
    answers = {str(row["JudgmentName"]): _row_to_answer(row) for row in rows}
    payload = {
        "stage": stage,
        "question_version": first.get("QuestionVersion"),
        "policy_version": first.get("PolicyVersion"),
        "input_hash": first.get("InputHash"),
        "model": first.get("Model"),
        "latency_ms": first.get("LatencyMs"),
        "answers": answers,
        "recorded_on": datetime.now(timezone.utc).isoformat(),
    }

    cur = conn.cursor()
    if first.get("RunID") and column:
        if not _update_run_stage(
            cur,
            first=first,
            stage=stage,
            column=column,
            answers=answers,
            payload=payload,
        ):
            return 0
    _insert_trace_event(cur, first=first, stage=stage, payload=payload)
    return 1


def persist_rows(rows: list[dict[str, Any]]) -> dict[str, Any]:
    if not AUDIT_ENABLED or not rows:
        return {"ok": True, "persisted": 0, "reason": "audit disabled or no rows"}
    try:
        import pyodbc  # noqa: F401
    except ImportError:
        return {"ok": False, "persisted": 0, "reason": "pyodbc unavailable"}

    grouped: dict[tuple[Any, ...], list[dict[str, Any]]] = {}
    for row in rows:
        key = (
            row.get("RunID"),
            row.get("TicketID"),
            row.get("Stage"),
            row.get("InputHash"),
            row.get("PolicyVersion"),
        )
        grouped.setdefault(key, []).append(row)

    try:
        conn = _connect()
    except Exception as exc:
        return {"ok": False, "persisted": 0, "reason": f"{type(exc).__name__}: {exc}"}

    persisted = 0
    try:
        for group in grouped.values():
            persisted += _persist_group(conn, group)
        conn.commit()
        return {"ok": True, "persisted": persisted}
    except Exception as exc:
        conn.rollback()
        return {"ok": False, "persisted": persisted, "reason": f"{type(exc).__name__}: {exc}"}
    finally:
        conn.close()
