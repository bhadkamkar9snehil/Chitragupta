#!/usr/bin/env python3
"""Jev walks the XBatch world in GBrain one step at a time; code looks at live data for each step.

Design: Knowledge/XBATCH_WORLD_KNOWLEDGE_DESIGN.md. Failure modes: Model_Bench/e2e/WALK_FAILURE_MODES.md.
Runs in WSL (GBrain lives there).  python3 Model_Bench/world_walk.py "<ticket text>"
"""
from __future__ import annotations

import json
import re
import sys
import time
from decimal import Decimal
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
import entity_resolver  # noqa: E402  (spans + SQL connection only)
from world_links import Brain, all_pages  # noqa: E402

WORLD = json.loads((Path(__file__).resolve().parent.parent / "Knowledge" / "process_world.json").read_text(encoding="utf-8"))
MAX_STEPS = 8            # mode 16
MAX_OPTIONS = 60         # mode 14: beyond this Jev first picks the kind of link
STOP_EXPLAINED = "stop_explained"
STOP_NOT_DATA = "stop_not_data"
ROLES = {
    "sees": "What the requester is seeing or complaining about (the missing or wrong result)",
    "stuck": "A record of this same failure that is stuck, pending or failed, but is not itself the reason",
    "cause": "The error or failure that made it happen",
    "unrelated": "Not part of this problem",
}
FRAMEWORK = set(WORLD["keys"]["framework_columns"])
QUERY_TIMEOUT_S = 8
_NUMBER = re.compile(r"(?<![\w.])\d{1,6}(?:\.\d+)?(?![\w])")


def jev(state: dict[str, Any], questions: dict[str, Any]) -> dict[str, Any]:
    from jev.client import system_one
    return ((system_one(state, questions) or {}).get("answers")) or {}


# ---------- start: which key holds the ticket's identifier (derived from the world, not typed) ----------

def _shape(value: str) -> str:
    return re.sub(r"[A-Za-z]+", "A", re.sub(r"\d+", lambda m: f"9{{{len(m.group())}}}", value))


KEY_SHAPES = {k: {_shape(v) for v in info["example"]} for k, info in WORLD["keys"]["keys"].items()}


def resolve(text: str, conn) -> list[dict[str, Any]]:
    """Identifier spans -> keys whose value shape matches -> confirmed in the key's columns (one query per key)."""
    found = []
    cur = conn.cursor()
    for span in entity_resolver.spans(text):
        for key, shapes in KEY_SHAPES.items():
            if _shape(span) not in shapes:
                continue
            cols = WORLD["keys"]["keys"][key]["columns"]
            parts = [f"SELECT TOP 1 '{c}' c FROM dbo.[{c.split('.')[0]}] WHERE [{c.split('.', 1)[1]}] = ?" for c in cols]
            try:
                cur.execute(" UNION ALL ".join(f"SELECT * FROM ({p}) x{i}" for i, p in enumerate(parts)), [span] * len(parts))
                holders = [r[0] for r in cur.fetchall()]
            except Exception as exc:  # the walk reports, never crashes
                holders, key = [], f"{key} (check failed: {str(exc)[:80]})"
            if holders:
                found.append({"value": span, "key": key, "holders": holders})
    return found


# ---------- look: live data for the chosen node ----------

def _rows_for(table: str, columns: list[str], value: str, conn) -> tuple[int, list[dict[str, Any]]]:
    cur = conn.cursor()
    where = " OR ".join(f"[{c}] = ?" for c in columns)
    cur.execute(f"SELECT COUNT(*) FROM dbo.[{table}] WHERE {where}", [value] * len(columns))
    count = cur.fetchone()[0]
    cur.execute(f"SELECT TOP 3 * FROM dbo.[{table}] WHERE {where}", [value] * len(columns))
    names = [d[0] for d in cur.description]
    return count, [dict(zip(names, r)) for r in cur.fetchall()]


def _fmt(v: Any) -> str:
    if isinstance(v, Decimal):
        v = float(v)
    text = re.sub(r"(?s).*Response Error Message:", "", str(v)).strip()
    return text[:140]


def look_table(name: str, value: str, conn) -> dict[str, Any]:
    cols = [c.split(".", 1)[1] for k in WORLD["keys"]["keys"].values() for c in k["columns"] if c.split(".", 1)[0] == name]
    if not cols:
        return {"text": f"{name}: holds no identifier column, so its rows cannot be matched to {value}", "observed": False}
    count, rows = _rows_for(name, cols, value, conn)
    if not count:
        return {"text": f"{name}: no rows for {value}", "rows": 0}
    shown = {}
    for row in rows:
        for col, v in row.items():
            if col.lower() not in FRAMEWORK and v not in (None, "") and col not in shown:
                shown[col] = _fmt(v)
    numbers = {c: float(v) for row in rows for c, v in row.items()
               if isinstance(v, (int, float, Decimal)) and not isinstance(v, bool)}
    return {"rows": count, "columns": shown, "numbers": numbers,
            "text": f"{name}: {count} row(s) for {value}"}


def pick_columns(ticket: str, observation: dict[str, Any]) -> list[str]:
    """Jev marks which columns of the rows matter for this ticket (one batched call); code never guesses by name."""
    cols = list(observation.get("columns", {}))[:120]
    if not cols:
        return []
    questions = {f"c{i}": {"type": "noul", "instructions": {
        "task": "Does this column's value help answer the requester's problem?",
        "ticket_path": "ticket", "column_path": f"columns.c{i}"}} for i in range(len(cols))}
    answers = jev({"ticket": ticket, "columns": {f"c{i}": f"{c} = {observation['columns'][c]}" for i, c in enumerate(cols)}},
                  questions)
    scored = sorted(((float((answers.get(f"c{i}") or {}).get("noul") or 0.0), c) for i, c in enumerate(cols)), reverse=True)
    return [c for score, c in scored if score >= 0.60][:15]  # same threshold as jev/relationship_hops.py


LOG_SCAN_TIMEOUT_S = 90


def log_runs(value: str, conn) -> dict[str, list[tuple[str, str]]]:
    """Every procedure log step that mentions this identifier: one scan per ticket.

    XMES_Log_Trn_Tbl (4.8M rows) has no index on Name, so a per-procedure lookup is a 10 s full scan
    each time. One scan for the value, cached, answers every procedure step of the walk (mode 18)."""
    conn.timeout = LOG_SCAN_TIMEOUT_S
    cur = conn.cursor()
    cur.execute("""SELECT Name, CreatedOn, Status FROM dbo.XMES_Log_Trn_Tbl
                   WHERE ExecutionQuery LIKE ? ORDER BY CreatedOn DESC""", f"%{value}%")
    runs: dict[str, list[tuple[str, str]]] = {}
    for r in cur.fetchall():
        runs.setdefault(r.Name, []).append((str(r.CreatedOn)[:19], str(r.Status or "")))
    return runs


def look_procedure(name: str, value: str, runs_by_proc: dict[str, list[tuple[str, str]]]) -> dict[str, Any]:
    """What the procedure's own log shows for this identifier (mode 18: none logged is evidence too)."""
    runs = [type("Run", (), {"CreatedOn": t, "Status": s}) for t, s in runs_by_proc.get(name, [])[:12]]
    info = WORLD["procedures"].get(name, {})
    writes = ", ".join(f"{t} ({', '.join(c[:6])})" if c else t for t, c in list(info.get("writes", {}).items())[:6])
    if not runs:
        logged = "it keeps a log, but no runs mention" if info.get("runtime") else "it keeps no log, so runs for"
        return {"text": f"procedure {name}: {logged} {value}. It writes {writes or 'nothing known'}."}
    steps = [f"{str(r.CreatedOn)[:19]} {r.Status}" for r in runs]
    errors = [s for s in steps if re.search(r"error|fail|exception", s, re.I)]
    return {"text": f"procedure {name}: {len(runs)} logged steps for {value}, latest {steps[0]}"
                    + (f"; error steps: {'; '.join(errors[:4])}" if errors else "; no error steps")
                    + f". It writes {writes or 'nothing known'}.", "steps": steps}


def look(node: dict[str, Any], value: str, conn, runs_by_proc: dict) -> dict[str, Any]:
    conn.timeout = QUERY_TIMEOUT_S
    kind, name = node["kind"], node["title"]
    try:
        if kind in ("table", "view"):
            return look_table(name, value, conn)
        if kind == "procedure":
            return look_procedure(name, value, runs_by_proc)
    except Exception as exc:
        return {"text": f"{kind} {name}: could not read ({type(exc).__name__}: {str(exc)[:100]})", "observed": False}
    return {"text": f"{kind} {name}: {node.get('summary', '')}"}


# ---------- step: the options are the links of everything visited so far ----------

class World:
    def __init__(self) -> None:
        self.brain = Brain()
        self.pages: dict[str, dict[str, Any]] = {}

    def page(self, slug: str) -> dict[str, Any]:
        if slug not in self.pages:
            p = self.brain.call("get_page", slug=slug, include_content=True)
            meta = p.get("frontmatter") or {}
            body = (p.get("compiled_truth") or p.get("content") or "").replace("\r", "")
            self.pages[slug] = {"slug": slug, "kind": meta.get("type") or p.get("type"), "title": meta.get("title") or p.get("title"),
                                "summary": re.sub(r"(?s)^.*?\n# [^\n]*\n\n", "", body)[:200].replace("\n", " ")}
        return self.pages[slug]

    def titles(self) -> dict[str, str]:
        if not hasattr(self, "_titles"):
            self._titles = {p.get("title"): p["slug"] for p in all_pages(self.brain)}
        return self._titles

    def neighbours(self, slug: str) -> list[dict[str, Any]]:
        out = []
        for direction, tool, end in (("out", "get_links", "to_slug"), ("in", "get_backlinks", "from_slug")):
            res = self.brain.call(tool, slug=slug)
            for l in res if isinstance(res, list) else res.get("links", []):
                other = l.get(end) or l.get("to") or l.get("from") or l.get("slug")
                if other:
                    out.append({"slug": other, "type": l.get("link_type") or l.get("type"), "direction": direction,
                                "context": l.get("context") or ""})
        return out


def describe(world: World, here: str, link: dict[str, Any]) -> str:
    a, b = world.page(here)["title"], world.page(link["slug"])
    verb = link["type"] if link["direction"] == "out" else f"is {link['type']} by" if link["type"] in ("writes", "reads", "calls") else f"<-{link['type']}-"
    ctx = f" ({link['context'][:80]})" if link["context"] else ""
    return f"{a} {verb} {b['kind']} {b['title']}{ctx}"


def choose(world: World, ticket: str, trail: list[dict], options: list[dict]) -> dict | str:
    seen = [f"step {i + 1}: {s['observation']['text']}" for i, s in enumerate(trail)]
    if len(options) > MAX_OPTIONS:  # mode 14: pick the kind of link first
        kinds = sorted({o["label"].split(" ")[1] + " " + world.page(o["slug"])["kind"] for o in options})
        crit = {f"k{i}": k for i, k in enumerate(kinds)}
        a = jev({"ticket": ticket, "evidence_so_far": seen},
                {"kind": {"type": "choice", "criteria": crit,
                          "instructions": "Which kind of connection should the investigation follow next?"}}).get("kind") or {}
        wanted = crit.get(a.get("choice"))
        if wanted:
            options = [o for o in options if o["label"].split(" ")[1] + " " + world.page(o["slug"])["kind"] == wanted][:250]
    crit = {f"o{i}": o["label"] for i, o in enumerate(options)}
    crit[STOP_EXPLAINED] = "Stop: the evidence so far already shows why this happened"
    crit[STOP_NOT_DATA] = "Stop: this is not a problem with the data (how-to, access, hardware)"
    a = jev({"ticket": ticket, "evidence_so_far": seen},
            {"next": {"type": "choice", "criteria": crit,
                      "instructions": "Which single next step best helps find why the requester sees this problem?"}}).get("next") or {}
    c = a.get("choice")
    return c if c in (STOP_EXPLAINED, STOP_NOT_DATA) else options[int(c[1:])] if c in crit else STOP_EXPLAINED


def judge(ticket: str, observation: str) -> dict[str, Any]:
    a = jev({"ticket": ticket, "finding": observation},
            {"role": {"type": "choice", "criteria": ROLES,
                      "instructions": "What part does this finding play in the requester's problem?"}}).get("role") or {}
    return {"role": a.get("choice"), "confidence": a.get("confidence")}


def walk(ticket: str, world: World | None = None, conn=None) -> dict[str, Any]:
    started = time.perf_counter()
    world = world or World()
    conn = conn or entity_resolver._connect()
    conn.timeout = QUERY_TIMEOUT_S * 3
    entities = resolve(ticket, conn)
    if not entities:
        return {"entities": [], "trail": [], "stopped": "no identifier from the ticket exists in XBatch"}
    value = entities[0]["value"]
    runs_by_proc = log_runs(value, conn)
    trail: list[dict[str, Any]] = []
    visited: set[str] = set()
    by_title = world.titles()
    frontier = [{"slug": by_title[h.split(".")[0]], "label": f"start: {h} holds {value}"}
                for e in entities for h in e["holders"] if h.split(".")[0] in by_title]
    # What actually ran for this identifier, from the procedures' own log, is a start too.
    frontier += [{"slug": by_title[p], "label": f"start: procedure {p} logged {len(r)} steps for {value}"}
                 for p, r in runs_by_proc.items() if p in by_title]
    stopped = f"step limit {MAX_STEPS}"
    for _ in range(MAX_STEPS):
        options = [o for o in frontier if o["slug"] not in visited]  # mode 13
        if not options:
            stopped = "no unvisited links left"
            break
        pick = choose(world, ticket, trail, options)
        if isinstance(pick, str):
            stopped = pick
            break
        visited.add(pick["slug"])
        node = world.page(pick["slug"])
        obs = look(node, value, conn, runs_by_proc)
        if obs.get("columns"):
            keep = pick_columns(ticket, obs)
            obs["text"] += "; " + "; ".join(f"{c}={obs['columns'][c]}" for c in keep)
        # Nothing was seen (no identifier column, unreadable): record that, never ask Jev to judge nothing.
        role = judge(ticket, obs["text"]) if obs.get("observed", True) else {"role": "not_observed", "confidence": None}
        trail.append({"step": pick["label"], "node": node["title"], "kind": node["kind"], "observation": obs, **role})
        frontier += [{"slug": l["slug"], "label": describe(world, pick["slug"], l)} for l in world.neighbours(pick["slug"])]
    numbers = {}
    for n in dict.fromkeys(_NUMBER.findall(entity_resolver._DATES.sub(" ", ticket).replace(value, " "))):
        numbers[n] = [f"{s['node']}.{c}" for s in trail for c, v in (s["observation"].get("numbers") or {}).items() if v == float(n)] \
            + [f"{s['node']} (number of rows)" for s in trail if s["observation"].get("rows") == float(n)]
    return {"entities": entities, "trail": trail, "stopped": stopped, "numbers": numbers,
            "seconds": round(time.perf_counter() - started, 1)}


if __name__ == "__main__":
    result = walk(" ".join(sys.argv[1:]))
    print(json.dumps(result, indent=1, default=str))
