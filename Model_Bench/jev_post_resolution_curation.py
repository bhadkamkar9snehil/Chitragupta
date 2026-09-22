#!/usr/bin/env python3
"""Post-resolution Jev knowledge-curation suggestions, and the deterministic
write step that acts on them.

Jev never writes to the Solution Article table directly -- it only produces
an auditable REUSE_EXISTING / UPDATE_EXISTING / CREATE_CANDIDATE / NONE
judgment (assess_curation()). This module's write_curation_action() is the
harness-owned deterministic code that decides what, if anything, to persist
based on that judgment plus the run's own already-VERIFIED resolution
fields -- never inventing new article content. Per the governance flags in
`state["governance"]`, no ticket auto-approves an article: CREATE_CANDIDATE
and UPDATE_EXISTING both land as ArticleStatus='Candidate' rows awaiting
human/governed review; UPDATE_EXISTING never mutates an existing article's
authoritative content in place, it links a new candidate via
SupersedesSolutionID so a reviewer can compare old vs proposed. Only
REUSE_EXISTING touches an existing row, and only its usage bookkeeping
(UsageCount, LastVerifiedOn/RunID), never its content.
"""
from __future__ import annotations

import hashlib
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
from Model_Bench.jev.client import typesafe_available
from Model_Bench.jev.kb_curation import assess_curation, rerank_articles
from Model_Bench.jev.policy import KB_JUDGMENTS_ENABLED

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


def pending_resolutions(cur, top: int = 20) -> list[dict[str, Any]]:
    cur.execute(
        """
        SELECT TOP (?)
            r.ID AS RunID, r.TicketID, r.Route, r.ResponseType,
            r.ProblemSummary, r.Findings, r.RootCause, r.Resolution, r.ReplyText,
            r.InvestigationJson, r.CompletedOn,
            c.TicketNo, c.BriefDetails, c.Description, c.ProblemCategory
        FROM dbo.Hermes_L2_Response_Trn_Tbl r
        JOIN dbo.Complaint_Mst_Tbl c ON c.ID = r.TicketID
        WHERE r.IsDeleted = 0
          AND r.ResponseType = 'RESOLUTION'
          AND r.CompletedOn IS NOT NULL
          AND NULLIF(LTRIM(RTRIM(r.RootCause)), '') IS NOT NULL
          AND JSON_VALUE(r.JevKBCurationJson, '$.POST_RESOLUTION_KB.stage') IS NULL
        ORDER BY r.CompletedOn ASC;
        """,
        top,
    )
    return _dict_rows(cur)


def candidate_articles(cur, run: dict[str, Any], top: int = 8) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    route = run.get("Route")
    cur.execute(
        """
        SELECT TOP 24
            ID, Title, ProblemSummary, RootCause, ResolutionSteps, Route, Tags,
            UsageCount, CreatedOn, ModifiedOn, KnowledgeType, ArticleStatus,
            CanonicalKey, RevisionNo, LastVerifiedOn, ApplicabilityJson,
            NegativeIndicatorsJson, VerificationJson, DiagnosticSteps,
            VerificationSteps, ExpectedResult
        FROM dbo.Hermes_Solution_Article_Mst_Tbl
        WHERE IsDeleted = 0
          AND ArticleStatus IN ('Approved','Candidate')
        ORDER BY
            CASE WHEN Route = ? THEN 0 ELSE 1 END,
            UsageCount DESC,
            COALESCE(ModifiedOn, CreatedOn) DESC;
        """,
        route,
    )
    pool = _dict_rows(cur)
    query = " ".join(str(run.get(k) or "") for k in (
        "ProblemSummary", "RootCause", "Resolution", "Findings", "Route"
    )).strip()
    rerank = rerank_articles(
        query,
        pool,
        top=min(top, len(pool) or top),
    )
    return (list(rerank.get("ranked") or pool[:top]), rerank)


def _content_hash(*parts: Any) -> str:
    blob = "\x1f".join(str(p or "") for p in parts)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


def write_curation_action(
    cur,
    *,
    run: dict[str, Any],
    disposition: str,
    top_existing: dict[str, Any] | None,
) -> dict[str, Any]:
    """Deterministic write for a Jev curation judgment. Only acts on the
    run's own already-verified fields; never generates new article prose.
    """
    ticket_no = run.get("TicketNo") or run.get("TicketID") or "unknown ticket"
    problem_summary = (run.get("ProblemSummary") or "").strip()
    root_cause = (run.get("RootCause") or "").strip()
    resolution = (run.get("Resolution") or "").strip()
    route = run.get("Route")
    run_id = str(run["RunID"])
    ticket_id = str(run["TicketID"])

    if disposition == "REUSE_EXISTING":
        if not top_existing or not top_existing.get("ID"):
            return {"action": "NONE", "reason": "REUSE_EXISTING but no existing candidate to bump"}
        cur.execute(
            """
            UPDATE dbo.Hermes_Solution_Article_Mst_Tbl
            SET UsageCount = ISNULL(UsageCount, 0) + 1,
                LastVerifiedOn = GETDATE(),
                LastVerifiedRunID = ?,
                ModifiedOn = GETDATE()
            WHERE ID = ? AND IsDeleted = 0
            """,
            run_id, top_existing["ID"],
        )
        return {"action": "REUSE_EXISTING_BUMPED", "article_id": top_existing["ID"]}

    if disposition in ("CREATE_CANDIDATE", "UPDATE_EXISTING"):
        if not resolution or not root_cause:
            return {"action": "NONE", "reason": "missing verified root_cause/resolution, refusing to write"}
        title = f"{ticket_no}: {problem_summary[:120] or root_cause[:120]}".strip()
        canonical_key = _content_hash(route, root_cause)[:32]
        content_hash = _content_hash(problem_summary, root_cause, resolution)
        supersedes = (
            top_existing["ID"]
            if disposition == "UPDATE_EXISTING" and top_existing and top_existing.get("ID")
            else None
        )
        new_id = cur.execute(
            """
            INSERT INTO dbo.Hermes_Solution_Article_Mst_Tbl
                (Title, ProblemSummary, RootCause, ResolutionSteps, Route,
                 UsageCount, IsActive, ArticleStatus, CanonicalKey, ContentHash,
                 SourceTicketID, SourceRunID, SupersedesSolutionID, KnowledgeType,
                 Source)
            OUTPUT INSERTED.ID
            VALUES (?, ?, ?, ?, ?, 0, 1, 'Candidate', ?, ?, ?, ?, ?, 'jev_post_resolution_curation', 'T-SQL')
            """,
            title, problem_summary or None, root_cause, resolution, route,
            canonical_key, content_hash, ticket_id, run_id, supersedes,
        ).fetchone()[0]
        if supersedes:
            cur.execute(
                "UPDATE dbo.Hermes_Solution_Article_Mst_Tbl SET SupersededBySolutionID = ? WHERE ID = ?",
                new_id, supersedes,
            )
        return {"action": f"{disposition}_WRITTEN", "article_id": str(new_id), "supersedes": supersedes}

    return {"action": "NONE", "reason": "disposition NONE or unrecognized"}


def main() -> int:
    if not KB_JUDGMENTS_ENABLED:
        print("Jev KB judgments disabled.")
        return 0
    if not typesafe_available():
        print("TypeSafe Jev credential not configured; skipping Jev KB curation.")
        return 0

    conn = connect()
    assessed = 0
    try:
        cur = conn.cursor()
        for run in pending_resolutions(cur):
            candidates, rerank = candidate_articles(cur, run)
            if rerank.get("ok"):
                persist_rows(rows_for_result(
                    result=rerank,
                    stage="POST_RESOLUTION_KB_RERANK",
                    state={
                        "run": str(run["RunID"]),
                        "query": " ".join(str(run.get(k) or "") for k in (
                            "ProblemSummary", "RootCause", "Resolution", "Findings", "Route"
                        )).strip(),
                        "candidate_ids": [str(row.get("ID") or "") for row in candidates],
                    },
                    ticket_id=str(run["TicketID"]),
                    run_id=str(run["RunID"]),
                ))
            state = {
                "verified_resolution": {
                    "route": run.get("Route"),
                    "problem_summary": run.get("ProblemSummary"),
                    "findings": run.get("Findings"),
                    "root_cause": run.get("RootCause"),
                    "resolution": run.get("Resolution"),
                    "reply_text": run.get("ReplyText"),
                    "investigation": run.get("InvestigationJson"),
                },
                "ticket": {
                    "ticket_no": run.get("TicketNo"),
                    "brief_details": run.get("BriefDetails"),
                    "description": run.get("Description"),
                    "problem_category": run.get("ProblemCategory"),
                },
                "existing_articles": candidates,
                "governance": {
                    "single_resolved_ticket_auto_approves_article": False,
                    "candidate_requires_governance": True,
                    "vector_or_semantic_similarity_never_auto_merges": True,
                },
            }
            result = assess_curation(state)
            if not result.get("ok"):
                print(f"Jev KB curation unavailable for {run['RunID']}: {result.get('reason')}")
                continue
            audit = persist_rows(rows_for_result(
                result=result,
                stage="POST_RESOLUTION_KB",
                state=state,
                ticket_id=str(run["TicketID"]),
                run_id=str(run["RunID"]),
            ))
            assessed += int(audit.get("persisted") or 0) > 0
            disp = (result.get("answers") or {}).get("curation_disposition") or {}
            choice = str(disp.get("choice") or "NONE")
            confidence = float(disp.get("confidence") or 0.0)
            print(f"Jev KB curation {run['RunID']}: {choice} ({confidence})")

            # Deterministic write, gated on real evidence -- not on Jev's
            # confidence alone. A low-confidence disposition still requires
            # governed review later (ArticleStatus='Candidate'), but a
            # low-confidence CREATE/UPDATE isn't even attempted.
            write_result = {"action": "NONE", "reason": "confidence below write threshold"}
            if confidence >= 0.60:
                write_result = write_curation_action(
                    cur, run=run, disposition=choice,
                    top_existing=candidates[0] if candidates else None,
                )
            conn.commit()
            print(f"  write: {write_result}")
    finally:
        conn.close()
    print(f"Jev KB curation complete: {assessed} newly assessed resolution(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
