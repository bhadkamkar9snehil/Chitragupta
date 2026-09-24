"""Heat -> every process-world table that holds it -> plain-words findings -> Jev picks the one that explains the ticket.

Failure modes this is built against: Model_Bench/e2e/WALK_FAILURE_MODES.md.
E2E thermometer: python Model_Bench/e2e/run_walk.py
"""
from __future__ import annotations

import json
import re
import time
from pathlib import Path
from typing import Any

import entity_resolver

WORLD = Path(__file__).resolve().parent.parent / "Knowledge" / "process_world.json"
HEAT_COLUMNS = ("HeatID", "HeatNo", "ActualHeatID", "Batch", "HeatNumber")  # mode 2
SIGNAL = re.compile(r"(?i)error|message|status|processed|count$")
TABLE_TIMEOUT_S = 4   # mode 6: one slow table cannot sink the walk
NONE = "none"


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
        signals = []
        for row in rows:
            for name, value in zip(names, row):
                if SIGNAL.search(name) and value not in (None, "", 0) and f"{name}={_clean(value)}" not in signals:
                    signals.append(f"{name}={_clean(value)}")
        hits.append({"table": table, "rows": count, "signals": signals[:6]})
    return hits


def finding(hit: dict[str, Any]) -> str:
    """One short line per table; numbers stay as code wrote them (mode 7)."""
    if "error" in hit:
        return f"{hit['table']}: could not read ({hit['error']})"
    return f"{hit['table']}: {hit['rows']} row(s)" + (f"; {'; '.join(hit['signals'])}" if hit["signals"] else "")


def jev_pick(text: str, hits: list[dict[str, Any]], symptom: str | None = None) -> tuple[str | None, float | None]:
    """Hop 1 (symptom is None): which finding matches the complaint. Hop 2: which finding causes the symptom."""
    try:
        from jev.client import system_one
    except ImportError:
        return None, None
    options = {f"c{i}": finding(h) for i, h in enumerate(hits)}
    if symptom is None:
        options[NONE] = "None of these explains it: the question is not about wrong or missing data"
        inputs = {"ticket": text, "findings": options}
        instructions = "Which finding explains what the requester is complaining about?"
    else:
        options[NONE] = "None of these: the symptom is itself the error message, or no cause for it is shown"
        inputs = {"ticket": text, "symptom": symptom, "findings": options}
        instructions = "Which finding is the cause of the symptom (an error or failure that made it happen)?"
    result = system_one(inputs, {"explains": {"type": "choice", "instructions": instructions, "criteria": options}})
    answer = ((result or {}).get("answers") or {}).get("explains") or {}
    choice = answer.get("choice")
    if choice == NONE:
        return NONE, answer.get("confidence")
    if choice not in options:
        return None, None
    return hits[int(choice[1:])]["table"], answer.get("confidence")


def walk(text: str, conn=None) -> dict[str, Any]:
    start = time.perf_counter()
    conn = conn or entity_resolver._connect()
    entity = entity_resolver.resolve(text, conn)
    out: dict[str, Any] = {"entity": {k: entity.get(k) for k in ("kind", "value", "exists")}}
    if entity.get("kind") not in ("heat", "billet") or not entity.get("exists"):
        out.update(pick=NONE, reason="no heat found in XBatch", hits=[])  # mode 9
        return out
    heat = str(entity["value"]).split("_")[0]
    hits = [h for h in scan(heat, conn) if "error" not in h]
    out["hits"] = [finding(h) for h in hits]
    out["scan_s"] = round(time.perf_counter() - start, 1)
    pick, confidence = jev_pick(text, hits)
    out.update(pick=pick, confidence=confidence, ranked_by="jev" if pick else "unranked (Jev unavailable)")
    picked = next((h for h in hits if h["table"] == pick), None)
    if picked and any(s.startswith("ErrorMessage=") for s in picked["signals"]):
        out.update(cause=pick, cause_confidence=None)  # the symptom already carries its error: no hop needed
    elif picked:
        rest = [h for h in hits if h is not picked]
        cause, cause_conf = jev_pick(text, rest, symptom=finding(picked))
        out.update(cause=cause, cause_confidence=cause_conf)
    return out


if __name__ == "__main__":
    import sys
    print(json.dumps(walk(" ".join(sys.argv[1:])), indent=2, default=str))
