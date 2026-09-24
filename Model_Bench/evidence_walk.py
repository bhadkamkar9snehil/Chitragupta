"""Heat -> every process-world table that holds it -> plain-words findings -> Jev picks the one that explains the ticket.

Failure modes this is built against: Model_Bench/e2e/WALK_FAILURE_MODES.md.
E2E thermometer: python Model_Bench/e2e/run_walk.py
"""
from __future__ import annotations

import json
import re
import time
from decimal import Decimal
from pathlib import Path
from typing import Any

import entity_resolver

WORLD = Path(__file__).resolve().parent.parent / "Knowledge" / "process_world.json"
HEAT_COLUMNS = ("HeatID", "HeatNo", "ActualHeatID", "Batch", "HeatNumber")  # mode 2
SIGNAL = re.compile(r"(?i)error|message|status|processed|count$")
TABLE_TIMEOUT_S = 4   # mode 6: one slow table cannot sink the walk


def heat_tables(conn) -> dict[str, list[str]]:
    """World tables that actually carry a heat key -> their heat columns (one entry per table)."""
    world = set(json.loads(WORLD.read_text(encoding="utf-8"))["tables"])
    cur = conn.cursor()
    cur.execute("SELECT OBJECT_NAME(object_id), name FROM sys.columns WHERE name IN (%s) "
                "AND OBJECTPROPERTY(object_id,'IsUserTable')=1" % ",".join("?" * len(HEAT_COLUMNS)), HEAT_COLUMNS)
    tables: dict[str, list[str]] = {}
    for table, column in sorted(cur.fetchall()):
        if table in world:
            tables.setdefault(table, []).append(column)
    return tables


def _clean(value: Any) -> str:
    text = str(value).strip()
    text = re.sub(r"(?s).*Response Error Message:", "", text).strip()  # drop the CPI URL preamble
    return text[:160]


def scan(heat: str, conn) -> list[dict[str, Any]]:
    """Rows per table for the heat, with the signal columns code can read off (modes 2, 3, 6, 7)."""
    hits = []
    conn.timeout = TABLE_TIMEOUT_S
    for table, columns in heat_tables(conn).items():
        where = " OR ".join(f"CONVERT(varchar(60),[{c}]) = ? OR CONVERT(varchar(60),[{c}]) LIKE ?" for c in columns)
        params = [heat, heat + "[_]%"] * len(columns)
        cur = conn.cursor()
        try:
            cur.execute(f"SELECT TOP 3 * FROM dbo.[{table}] WHERE {where}", params)
            rows = cur.fetchall()
            if not rows:
                continue
            cur.execute(f"SELECT COUNT(*) FROM dbo.[{table}] WHERE {where}", params)
            count = cur.fetchone()[0]
        except Exception as exc:
            hits.append({"table": table, "error": f"{type(exc).__name__}: {str(exc)[:120]}"})
            continue
        names = [d[0] for d in rows[0].cursor_description]
        signals, numbers = [], {}
        for row in rows:
            for name, value in zip(names, row):
                if isinstance(value, (int, float, Decimal)) and not isinstance(value, bool) and name not in numbers:
                    numbers[name] = float(value)
                if SIGNAL.search(name) and value not in (None, "", 0) and f"{name}={_clean(value)}" not in signals:
                    signals.append(f"{name}={_clean(value)}")
        hits.append({"table": table, "rows": count, "signals": signals[:6], "numbers": numbers})
    return hits


def finding(hit: dict[str, Any]) -> str:
    """One short line per table; numbers stay as code wrote them (mode 7)."""
    if "error" in hit:
        return f"{hit['table']}: could not read ({hit['error']})"
    return f"{hit['table']}: {hit['rows']} row(s)" + (f"; {'; '.join(hit['signals'])}" if hit["signals"] else "")


ROLES = {
    "sees": "What the requester is seeing or complaining about (the missing or wrong result)",
    "stuck": "A record of this same failure that is stuck, pending or failed, but is not itself the reason",
    "cause": "The error or failure that made it happen (an error message that explains the problem)",
    "unrelated": "Not part of this problem",
}
# Letters glued to digits make a code ("HHMNB500B"), not a quantity.
_NUMBER = re.compile(r"(?<![\w.])\d{1,6}(?:\.\d+)?(?![\w])")


def _system_one(state: dict[str, Any], questions: dict[str, Any]) -> dict[str, Any] | None:
    try:
        from jev.client import system_one
    except ImportError:
        return None
    return system_one(state, questions)


def judge_roles(text: str, hits: list[dict[str, Any]]) -> dict[str, dict[str, Any]] | None:
    """One batched call: each finding gets its own role judgement (mode 10), never one forced pick."""
    findings = {f"f{i}": finding(h) for i, h in enumerate(hits)}
    questions = {f"role_{k}": {"type": "choice", "criteria": ROLES,
                               "instructions": {"task": "What part does this finding play in the requester's problem?",
                                                "ticket_path": "ticket", "finding_path": f"findings.{k}"}}
                 for k in findings}
    result = _system_one({"ticket": text, "findings": findings}, questions)
    answers = (result or {}).get("answers") or {}
    if not answers:
        return None
    return {hits[int(k[1:])]["table"]: {"role": (answers.get(f"role_{k}") or {}).get("choice"),
                                        "confidence": (answers.get(f"role_{k}") or {}).get("confidence")}
            for k in findings}


def ticket_numbers(text: str, entity_value: str | None) -> list[str]:
    cleaned = entity_resolver._DATES.sub(" ", text)
    if entity_value:
        cleaned = cleaned.replace(str(entity_value), " ")
    return list(dict.fromkeys(_NUMBER.findall(cleaned)))[:4]


def trace_numbers(text: str, numbers: list[str], hits: list[dict[str, Any]]) -> dict[str, Any]:
    """Mode 11: code finds every place each number is stored; Jev matches a place to the requester's words."""
    traced: dict[str, Any] = {}
    questions, options_by_n = {}, {}
    for n in numbers:
        value = float(n)
        sources = [f"{h['table']} (number of rows)" for h in hits if h["rows"] == value]
        sources += [f"{h['table']}.{col}" for h in hits for col, v in h["numbers"].items() if v == value]
        if not sources:
            traced[n] = {"source": None, "reason": "not stored in any table for this heat"}  # mode 12
            continue
        options = {f"s{i}": src for i, src in enumerate(sources[:40])}
        options["none"] = "None of these is where the requester's number comes from"
        options_by_n[n] = options
        questions[f"source_{n.replace('.', '_')}"] = {
            "type": "choice", "criteria": options,
            "instructions": f"The requester mentions the number {n}. Which stored value is the one they are "
                            "describing (match the screen or report they name)?"}
    if questions:
        answers = ((_system_one({"ticket": text}, questions) or {}).get("answers")) or {}
        for n, options in options_by_n.items():
            a = answers.get(f"source_{n.replace('.', '_')}") or {}
            pick = a.get("choice")
            traced[n] = {"source": options.get(pick) if pick != "none" else None,
                         "confidence": a.get("confidence"), "candidates": len(options) - 1}
    return traced


def walk(text: str, conn=None) -> dict[str, Any]:
    start = time.perf_counter()
    conn = conn or entity_resolver._connect()
    entity = entity_resolver.resolve(text, conn)
    out: dict[str, Any] = {"entity": {k: entity.get(k) for k in ("kind", "value", "exists")}}
    if entity.get("kind") not in ("heat", "billet") or not entity.get("exists"):
        out.update(chain={}, reason="no heat found in XBatch", hits=[])  # mode 9
        return out
    heat = str(entity["value"]).split("_")[0]
    hits = [h for h in scan(heat, conn) if "error" not in h]
    out["hits"] = [finding(h) for h in hits]
    roles = judge_roles(text, hits)
    if roles is None:
        out.update(chain=None, ranked_by="unranked (Jev unavailable)")  # mode 8
        return out
    out["chain"] = {role: [t for t, r in roles.items() if r["role"] == role] for role in ("sees", "stuck", "cause")}
    out["roles"] = roles
    numbers = ticket_numbers(text, entity.get("value"))
    if numbers:
        out["numbers"] = trace_numbers(text, numbers, hits)
    out["seconds"] = round(time.perf_counter() - start, 1)
    return out


if __name__ == "__main__":
    import sys
    print(json.dumps(walk(" ".join(sys.argv[1:])), indent=2, default=str))
