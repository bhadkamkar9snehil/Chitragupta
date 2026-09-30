"""SQL-backed Kanban card store: the board Hermes kept in SQLite, now owned by Chitragupta.

Two tables next to the run tables (created on first use, like L1's own tables). Card and run dicts keep
the shape the lifecycle runtime already reads (`id`, `status`, `assignee`, `body`, `result`; run
`status`, `outcome`, `summary`, `profile`, `ended_at`, `metadata`), so the runtime changed only where it
called `hermes kanban`. See docs/plans/no-hermes-architecture.md (D3).

Card status: ready -> running -> done | blocked (| archived). Run status: running | done | blocked |
crashed | timed_out. A reviewer approves with done and rejects with blocked (run outcome "blocked").
"""
from __future__ import annotations

import json
import os
import re
import threading
import time
import uuid
from contextlib import contextmanager
from typing import Any, Iterable, Optional

import pyodbc

_DDL = """
IF OBJECT_ID('dbo.L2_Card_Tbl') IS NULL
    CREATE TABLE dbo.L2_Card_Tbl (
        ID varchar(20) NOT NULL PRIMARY KEY, Title nvarchar(200) NOT NULL, Assignee varchar(60) NOT NULL,
        Body nvarchar(max) NOT NULL, Priority int NOT NULL DEFAULT 0, Skills nvarchar(400) NULL,
        Status varchar(20) NOT NULL DEFAULT 'ready', Result nvarchar(500) NULL, Comments nvarchar(max) NULL,
        IdempotencyKey varchar(120) NULL, MaxRuntimeSec int NOT NULL DEFAULT 1200,
        CreatedOn datetime NOT NULL DEFAULT GETDATE(), ModifiedOn datetime NOT NULL DEFAULT GETDATE());
IF NOT EXISTS (SELECT 1 FROM sys.indexes WHERE name = 'UX_L2_Card_Idem')
    CREATE UNIQUE INDEX UX_L2_Card_Idem ON dbo.L2_Card_Tbl (IdempotencyKey) WHERE IdempotencyKey IS NOT NULL;
IF NOT EXISTS (SELECT 1 FROM sys.indexes WHERE name = 'IX_L2_Card_Status')
    CREATE INDEX IX_L2_Card_Status ON dbo.L2_Card_Tbl (Status, Priority DESC, CreatedOn);
IF OBJECT_ID('dbo.L2_Card_Run_Tbl') IS NULL
    CREATE TABLE dbo.L2_Card_Run_Tbl (
        ID int IDENTITY PRIMARY KEY, CardID varchar(20) NOT NULL, Profile varchar(60) NOT NULL,
        Status varchar(20) NOT NULL, Outcome varchar(20) NULL, Summary nvarchar(max) NULL,
        MetadataJson nvarchar(max) NULL, StartedOn datetime NOT NULL DEFAULT GETDATE(), EndedOn datetime NULL);
IF NOT EXISTS (SELECT 1 FROM sys.indexes WHERE name = 'IX_L2_Card_Run_Card')
    CREATE INDEX IX_L2_Card_Run_Card ON dbo.L2_Card_Run_Tbl (CardID);
"""

# A card is board-visible while live, or for this long after it was made; older history stays in SQL only.
HISTORY_DAYS = 14
_CARD_COLS = ("ID, Title, Assignee, Body, Priority, Skills, Status, Result, Comments, IdempotencyKey, "
              "MaxRuntimeSec, CreatedOn, ModifiedOn")
_migrated = False
_lock = threading.Lock()


def _connection() -> pyodbc.Connection:
    cs = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={os.environ.get('MSSQL_MCP_SERVER') or '10.2.6.204'};"
        f"DATABASE={os.environ.get('L2_CARD_DATABASE') or 'XStudio_Helpdesk'};"
        f"UID={os.environ.get('MSSQL_MCP_USER') or 'sa'};PWD={os.environ.get('MSSQL_MCP_PASSWORD') or ''};"
        "TrustServerCertificate=yes;Connection Timeout=30;"
    )
    return pyodbc.connect(cs, autocommit=False)


_tls = threading.local()
_IDLE_CHECK_SECONDS = 30


def _shared_connection() -> pyodbc.Connection:
    """One connection per thread: a login over the Tailscale relay costs seconds, so never one per call."""
    con = getattr(_tls, "con", None)
    if con is not None and time.time() - _tls.used > _IDLE_CHECK_SECONDS:
        try:
            con.cursor().execute("SELECT 1").fetchone()
            con.rollback()
        except pyodbc.Error:
            con = None
    if con is None:
        con = _connection()
        _tls.con = con
    _tls.used = time.time()
    return con


@contextmanager
def _cursor():
    global _migrated
    con = _shared_connection()
    try:
        cur = con.cursor()
        if not _migrated:
            with _lock:
                if not _migrated:
                    cur.execute(_DDL)
                    con.commit()
                    _migrated = True
        yield cur
        con.commit()
    except Exception:
        try:
            con.rollback()
        except pyodbc.Error:
            _tls.con = None  # broken connection: the next call logs in again
        raise


def _dict(cur: pyodbc.Cursor, row: Any) -> dict[str, Any]:
    return {c[0]: (v.isoformat(sep=" ") if hasattr(v, "isoformat") else v) for c, v in zip(cur.description, row)}


def _seconds(value: Any) -> int:
    m = re.fullmatch(r"\s*(\d+)\s*([smh]?)\s*", str(value))
    if not m:
        return 1200
    return int(m.group(1)) * {"": 1, "s": 1, "m": 60, "h": 3600}[m.group(2)]


def _card(cur: pyodbc.Cursor, row: Any) -> dict[str, Any]:
    d = _dict(cur, row)
    return {
        "id": d["ID"], "title": d["Title"], "assignee": d["Assignee"], "body": d["Body"],
        "priority": d["Priority"], "skills": [s for s in (d["Skills"] or "").split(",") if s],
        "status": d["Status"], "result": d["Result"], "comments": json.loads(d["Comments"] or "[]"),
        "idempotency_key": d["IdempotencyKey"], "max_runtime_seconds": d["MaxRuntimeSec"],
        "created_at": d["CreatedOn"], "modified_at": d["ModifiedOn"],
    }


def _run(cur: pyodbc.Cursor, row: Any) -> dict[str, Any]:
    d = _dict(cur, row)
    return {
        "id": d["ID"], "card_id": d["CardID"], "profile": d["Profile"], "status": d["Status"],
        "outcome": d["Outcome"], "summary": d["Summary"], "metadata": json.loads(d["MetadataJson"] or "{}"),
        "started_at": d["StartedOn"], "ended_at": d["EndedOn"],
    }


def create(*, title: str, assignee: str, body: str, priority: int = 0, skills: Iterable[str] = (),
           idempotency_key: Optional[str] = None, max_runtime: Any = "20m") -> dict[str, Any]:
    """Create a ready card; a repeated idempotency key returns the existing card instead."""
    with _cursor() as cur:
        if idempotency_key:
            row = cur.execute("SELECT ID FROM dbo.L2_Card_Tbl WHERE IdempotencyKey = ?", idempotency_key).fetchone()
            if row:
                return {"id": row[0], "existing": True}
        card_id = "t_" + uuid.uuid4().hex[:8]
        cur.execute(
            "INSERT INTO dbo.L2_Card_Tbl (ID, Title, Assignee, Body, Priority, Skills, IdempotencyKey, MaxRuntimeSec) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            card_id, title[:200], assignee, body, int(priority), ",".join(skills), idempotency_key, _seconds(max_runtime))
    return {"id": card_id}


def list_cards(status: Optional[str] = None, assignee: Optional[str] = None) -> list[dict[str, Any]]:
    """Board view: never archived; live cards always, finished ones for HISTORY_DAYS."""
    with _cursor() as cur:
        cur.execute(
            f"SELECT {_CARD_COLS} FROM dbo.L2_Card_Tbl WHERE Status <> 'archived' "
            "AND (? IS NULL OR Status = ?) AND (? IS NULL OR Assignee = ?) "
            "AND (Status IN ('ready', 'running', 'blocked') OR CreatedOn >= DATEADD(day, -?, GETDATE())) "
            "ORDER BY CreatedOn", status, status, assignee, assignee, HISTORY_DAYS)
        return [_card(cur, r) for r in cur.fetchall()]


def get_card(card_id: str) -> Optional[dict[str, Any]]:
    with _cursor() as cur:
        cur.execute(f"SELECT {_CARD_COLS} FROM dbo.L2_Card_Tbl WHERE ID = ?", card_id)
        row = cur.fetchone()
        return _card(cur, row) if row else None


def runs(card_id: str) -> list[dict[str, Any]]:
    with _cursor() as cur:
        cur.execute("SELECT * FROM dbo.L2_Card_Run_Tbl WHERE CardID = ? ORDER BY ID", card_id)
        return [_run(cur, r) for r in cur.fetchall()]


def claim() -> Optional[dict[str, Any]]:
    """Atomically move the best ready card (priority, then age) to running and open its run."""
    with _cursor() as cur:
        cur.execute(
            "WITH c AS (SELECT TOP 1 * FROM dbo.L2_Card_Tbl WITH (UPDLOCK, READPAST, ROWLOCK) "
            "WHERE Status = 'ready' ORDER BY Priority DESC, CreatedOn) "
            "UPDATE c SET Status = 'running', ModifiedOn = GETDATE() "
            "OUTPUT inserted.ID, inserted.Title, inserted.Assignee, inserted.Body, inserted.Priority, inserted.Skills, "
            "inserted.Status, inserted.Result, inserted.Comments, inserted.IdempotencyKey, inserted.MaxRuntimeSec, "
            "inserted.CreatedOn, inserted.ModifiedOn")
        row = cur.fetchone()
        if not row:
            return None
        card = _card(cur, row)
        cur.execute("INSERT INTO dbo.L2_Card_Run_Tbl (CardID, Profile, Status) VALUES (?, ?, 'running')",
                    card["id"], card["assignee"])
        return card


def finish(card_id: str, *, status: str, summary: str = "", metadata: Optional[dict[str, Any]] = None,
           result: Optional[str] = None) -> bool:
    """Close the card's open run. status: done | blocked | crashed | timed_out. False if nothing was running."""
    card_status = "done" if status == "done" else "blocked"
    with _cursor() as cur:
        cur.execute(
            "UPDATE dbo.L2_Card_Run_Tbl SET Status = ?, Outcome = ?, Summary = ?, MetadataJson = ?, EndedOn = GETDATE() "
            "WHERE CardID = ? AND Status = 'running'",
            status, "blocked" if status == "blocked" else None, summary,
            json.dumps(metadata, separators=(",", ":"), default=str) if metadata else None, card_id)
        if cur.rowcount < 1:
            return False
        cur.execute("UPDATE dbo.L2_Card_Tbl SET Status = ?, Result = ?, ModifiedOn = GETDATE() WHERE ID = ?",
                    card_status, (result or summary or "")[:500] or None, card_id)
        return True


def edit(card_id: str, *, result: Optional[str] = None, metadata: Optional[dict[str, Any]] = None) -> None:
    """Rewrite the latest finished run's metadata (the runtime's completion normalisation)."""
    with _cursor() as cur:
        if metadata is not None:
            cur.execute(
                "UPDATE dbo.L2_Card_Run_Tbl SET MetadataJson = ? WHERE ID = "
                "(SELECT MAX(ID) FROM dbo.L2_Card_Run_Tbl WHERE CardID = ? AND Status = 'done')",
                json.dumps(metadata, separators=(",", ":"), default=str), card_id)
        if result is not None:
            cur.execute("UPDATE dbo.L2_Card_Tbl SET Result = ?, ModifiedOn = GETDATE() WHERE ID = ?", result[:500], card_id)


def comment(card_id: str, text: str, author: str = "") -> None:
    with _cursor() as cur:
        row = cur.execute("SELECT Comments FROM dbo.L2_Card_Tbl WHERE ID = ?", card_id).fetchone()
        items = json.loads((row[0] if row else None) or "[]")
        items.append({"author": author, "text": text[:2000]})
        cur.execute("UPDATE dbo.L2_Card_Tbl SET Comments = ? WHERE ID = ?", json.dumps(items), card_id)


def archive(card_ids: Iterable[str]) -> None:
    ids = list(card_ids)
    if not ids:
        return
    with _cursor() as cur:
        cur.execute(f"UPDATE dbo.L2_Card_Tbl SET Status = 'archived', ModifiedOn = GETDATE() "
                    f"WHERE ID IN ({','.join('?' * len(ids))})", *ids)


def recover_running() -> int:
    """Engine start: workers are our children, so any card still 'running' lost its worker."""
    with _cursor() as cur:
        cur.execute("UPDATE dbo.L2_Card_Run_Tbl SET Status = 'crashed', Summary = 'engine restarted', EndedOn = GETDATE() "
                    "WHERE Status = 'running'")
        cur.execute("UPDATE dbo.L2_Card_Tbl SET Status = 'blocked', ModifiedOn = GETDATE() WHERE Status = 'running'")
        return cur.rowcount
