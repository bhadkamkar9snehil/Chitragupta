"""Ticket text -> the plant entity it is about, confirmed against XBatch data; Jev picks among real candidates.

Failure modes this is built against: Model_Bench/e2e/ENTITY_FAILURE_MODES.md.
E2E thermometer: python Model_Bench/e2e/run_entity.py
"""
from __future__ import annotations

import os
import re
from typing import Any

import pyodbc

# Where each entity kind lives. The data decides which kind a span is: a value counts as a kind
# only if it exists in one of these columns (failure mode 5: same value, many columns).
ENTITY_KINDS: dict[str, list[tuple[str, str]]] = {
    "billet": [("XMES_CCM_Billet_Genealogy_Trn_Tbl", "BilletNo")],
    "heat": [("EAF_PER_HEAT", "HeatID"), ("LRF_Per_Heat", "HeatID"), ("CCM_Per_Heat", "HeatID"),
             ("SMS_Plant_Process_EventTime", "ActualHeatID")],
    "work_order": [("XBatch_Work_Order_Mst_Tbl", "WorkOrderNumber"), ("MES_SAP_Production_Trn_Tbl", "ManufacturingOrder")],
    "material_document": [("MES_SAP_Production_Trn_Tbl", "MaterialDocument"),
                          ("MES_SAP_Consumption_Trn_Tbl", "MaterialDocument")],
}
# Shape of each kind, used only to label a well-formed identifier that is absent from the data
# (failure mode 4). Learned from the live values: heats are 7 digits, work orders 12, docs 10.
SHAPES = {"heat": r"\d{7}", "work_order": r"\d{12}", "material_document": r"\d{10}",
          "billet": r"\d{7}_S\d+_\d+"}

_DATES = re.compile(r"\d{4}-\d{2}-\d{2}(?:[ T]\d{2}:\d{2}(?::\d{2})?(?:\.\d+)?)?|\b\d{1,2}:\d{2}(?::\d{2})?\b")
# A trailing full stop ends a sentence ("heat 1604014."); only ".<digit>" makes it a decimal.
_SPAN = re.compile(r"(?<![\d.])(\d{7}_S\d+_\d+|\d{7,12})(?!\d|\.\d)")
MAX_SPANS = 6  # failure mode 11: bounded existence checks


def spans(text: str) -> list[str]:
    """Over-collect identifier-like spans: 7-12 digit numbers and billet codes, glued or not.

    Dates/times are removed first (mode 8); decimals and short numbers never match (modes 2, 7).
    """
    cleaned = _DATES.sub(" ", text)
    cleaned = re.sub(r"(?i)\b(?:heat|ht|h|wo|doc)(?=\d)", " ", cleaned)  # mode 6: heat1604015, H1604014
    seen: list[str] = []
    for value in _SPAN.findall(cleaned):
        if value not in seen:
            seen.append(value)
    return seen[:MAX_SPANS]


def _connect() -> pyodbc.Connection:
    return pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};SERVER=" + os.environ.get("MSSQL_MCP_SERVER", "10.2.6.204")
        + ";UID=" + os.environ.get("MSSQL_MCP_USER", "sa") + ";PWD=" + os.environ["MSSQL_MCP_PASSWORD"]
        + ";TrustServerCertificate=yes;Connection Timeout=30;DATABASE=XStudio_Xbatch;", autocommit=True)


def confirm(values: list[str], conn=None) -> list[dict[str, Any]]:
    """Which (value, kind) pairs exist in XBatch: one batched read-only query."""
    if not values:
        return []
    parts, params = [], []
    for value in values:
        for kind, homes in ENTITY_KINDS.items():
            for table, column in homes:
                parts.append(f"SELECT ? v, ? k WHERE EXISTS (SELECT 1 FROM dbo.[{table}] WHERE "
                             f"CONVERT(varchar(60), [{column}]) = ?)")
                params += [value, kind, value]
    conn = conn or _connect()
    cur = conn.cursor()
    cur.execute(" UNION ".join(parts), params)
    found = {(r.v, r.k) for r in cur.fetchall()}
    return [{"value": v, "kind": k, "exists": True} for v in values for k in ENTITY_KINDS if (v, k) in found]


def _by_shape(value: str) -> str | None:
    return next((k for k, pattern in SHAPES.items() if re.fullmatch(pattern, value)), None)


def _jev_pick(text: str, candidates: list[dict[str, Any]]) -> tuple[dict[str, Any] | None, float | None]:
    """Jev chooses which confirmed entity the requester is asking about (mode 3)."""
    try:
        from jev.client import system_one
    except ImportError:
        return None, None
    options = {f"c{i}": f"{c['kind'].replace('_', ' ')} {c['value']}" for i, c in enumerate(candidates)}
    result = system_one(
        {"ticket": text, "candidates": options},
        {"subject": {"type": "choice",
                     "instructions": "Which item is the requester's question actually about? The others may be "
                                     "mentioned as context.",
                     "criteria": options}},
    )
    answer = ((result or {}).get("answers") or {}).get("subject") or {}
    choice = answer.get("choice")
    if choice not in options:
        return None, None
    return candidates[int(choice[1:])], answer.get("confidence")


def resolve(text: str, conn=None) -> dict[str, Any]:
    """{kind, value, exists, candidates, ranked_by} or {kind: None} when the ticket names no entity."""
    found_spans = spans(text)
    if not found_spans:
        return {"kind": None, "reason": "no identifier in the text", "candidates": []}
    candidates = confirm(found_spans, conn)
    # A billet also confirms its heat; keep only the most specific entity per span.
    if not candidates:
        kind = _by_shape(found_spans[0])
        if kind:
            return {"kind": kind, "value": found_spans[0], "exists": False, "candidates": [],
                    "reason": "well-formed identifier not present in XBatch"}
        return {"kind": None, "reason": "no identifier confirmed in XBatch", "candidates": []}
    distinct = {(c["kind"], c["value"]) for c in candidates}
    if len(distinct) == 1:
        return {**candidates[0], "candidates": candidates, "ranked_by": "only candidate"}
    picked, confidence = _jev_pick(text, candidates)
    if picked is None:
        return {**candidates[0], "candidates": candidates, "ranked_by": "unranked (Jev unavailable)"}
    return {**picked, "candidates": candidates, "ranked_by": "jev", "confidence": confidence}
