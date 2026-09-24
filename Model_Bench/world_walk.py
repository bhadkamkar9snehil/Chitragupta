#!/usr/bin/env python3
"""Jev walks the XBatch world in GBrain one step at a time; code looks at live data for each step.

Design: Knowledge/XBATCH_WORLD_KNOWLEDGE_DESIGN.md. Failure modes: Model_Bench/e2e/WALK_FAILURE_MODES.md.
Runs in WSL (GBrain lives there).  python3 Model_Bench/world_walk.py "<ticket text>"
"""
from __future__ import annotations

import json
import re
import sqlite3
import sys
import time
from decimal import Decimal
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
import entity_resolver  # noqa: E402  (spans + SQL connection only)
from world_links import Brain, all_pages  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
WORLD = json.loads((ROOT / "Knowledge" / "process_world.json").read_text(encoding="utf-8"))
LOG_INDEX = ROOT / ".cache" / "log_index.sqlite"
OBJS = WORLD["schema"]["objects"]
MAX_STEPS = 8            # mode 16
MAX_OPTIONS = 60         # mode 14: beyond this Jev first picks the kind of step
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


def is_table(name: str) -> bool:
    return OBJS.get(name, {}).get("kind") == "table"


# ---------- where an identifier lives (derived from the build, matched by value shape) ----------

def _shape(value: str) -> str:
    return re.sub(r"[A-Za-z]+", "A", re.sub(r"\d+", lambda m: f"9{{{len(m.group())}}}", value))


# Shared keys plus identifiers held by one table only (e.g. a material document names one posting).
# Only base tables are checked: a view's rows come from them, and views are joins (slow).
KEY_COLUMNS = {k: [c for c in info["columns"] if is_table(c.split(".")[0])] for k, info in WORLD["keys"]["keys"].items()}
KEY_COLUMNS.update({c: [c] for c in WORLD["keys"].get("identifiers", {}) if is_table(c.split(".")[0])})
KEY_SHAPES = {k: {_shape(v) for v in info["example"]} for k, info in WORLD["keys"]["keys"].items()}
KEY_SHAPES.update({c: {_shape(v) for v in ex} for c, ex in WORLD["keys"].get("identifiers", {}).items()})
KEY_OF_COLUMN = {c: k for k, cols in KEY_COLUMNS.items() for c in cols}


def holders(key: str, value: str, conn) -> list[str]:
    """Columns of this key that hold the value. One query; if it times out, column by column (mode 6)."""
    cols = KEY_COLUMNS.get(key, [])
    if not cols:
        return []
    cur = conn.cursor()
    part = "SELECT TOP 1 '{c}' c FROM dbo.[{t}] WHERE [{col}] = ?"
    try:
        cur.execute(" UNION ALL ".join(f"SELECT * FROM ({part.format(c=c, t=c.split('.')[0], col=c.split('.', 1)[1])}) x{i}"
                                       for i, c in enumerate(cols)), [value] * len(cols))
        return [r[0] for r in cur.fetchall()]
    except Exception:
        found = []
        for c in cols:
            try:
                cur.execute(part.format(c=c, t=c.split(".")[0], col=c.split(".", 1)[1]), value)
                found += [r[0] for r in cur.fetchall()]
            except Exception:
                continue  # one slow or type-mismatched column does not sink the rest
        return found


def resolve(text: str, conn) -> list[dict[str, Any]]:
    """Identifier spans -> keys whose value shape matches -> the columns that actually hold the value."""
    found = []
    for span in entity_resolver.spans(text):
        for key, shapes in KEY_SHAPES.items():
            if _shape(span) in shapes:
                cols = holders(key, span, conn)
                if cols:
                    found.append({"value": span, "key": key, "holders": cols})
    return found


# ---------- what ran for an identifier (build-time log index; the 3.5 GB log has no usable index) ----------

def runs_for(value: str) -> list[dict[str, Any]]:
    if not LOG_INDEX.exists():
        return []
    db = sqlite3.connect(f"file:{LOG_INDEX}?mode=ro", uri=True)
    rows = db.execute("SELECT proc, param, calls, steps, error_steps, first_on, last_on FROM runs WHERE value = ?",
                      (value,)).fetchall()
    db.close()
    return [dict(zip(("proc", "param", "calls", "steps", "error_steps", "first_on", "last_on"), r)) for r in rows]


# ---------- look: live data for the chosen node ----------

def _fmt(v: Any) -> str:
    if isinstance(v, Decimal):
        v = float(v)
    return re.sub(r"(?s).*Response Error Message:", "", str(v)).strip()[:140]


def _message_like(v: Any) -> bool:
    """Sentences (errors, statuses, messages): generic, not chosen by column name."""
    return (isinstance(v, str) and len(v.strip()) >= 15 and " " in v.strip() and re.search(r"[A-Za-z]{3}", v)
            and not v.lstrip().startswith(("Body", "{", "<", "EXEC", "SELECT")))


_INT_LIMITS = {"int": 2**31 - 1, "bigint": 2**63 - 1, "smallint": 2**15 - 1, "tinyint": 255}


def _can_hold(table: str, column: str, value: str) -> bool:
    """Whether the column's type can hold the value: an 11-digit inspection lot overflows an int column."""
    decl = next((c for c in OBJS.get(table, {}).get("columns", []) if c.split(" ")[0] == column), "")
    typ = decl.split(" ")[1].split("(")[0] if " " in decl else ""
    if typ in _INT_LIMITS:
        return value.isdigit() and int(value) <= _INT_LIMITS[typ]
    return True


def _status_like(v: Any) -> bool:
    """Short words that describe state (Entered, OnHold, Reversal Failed, PRODUCED): text with letters,
    not an identifier (no digits) and not a sentence. Generic, not chosen by column name."""
    return isinstance(v, str) and 2 < len(v.strip()) <= 30 and re.search(r"[A-Za-z]", v) and not re.search(r"\d", v)


def look_table(name: str, value: str, conn) -> dict[str, Any]:
    cols = sorted({c.split(".", 1)[1] for cs in KEY_COLUMNS.values() for c in cs if c.split(".", 1)[0] == name}
                  | {c.split(".", 1)[1] for k, info in WORLD["keys"]["keys"].items() for c in info["columns"]
                     if c.split(".", 1)[0] == name})
    cols = [c for c in cols if _can_hold(name, c, value)]
    if not cols:
        return {"text": f"{name}: holds no identifier column for a value like {value}", "observed": False}
    cur = conn.cursor()
    where = " OR ".join(f"[{c}] = ?" for c in cols)
    cur.execute(f"SELECT COUNT(*) FROM dbo.[{name}] WHERE {where}", [value] * len(cols))
    count = cur.fetchone()[0]
    if not count:
        return {"text": f"{name}: no rows for {value}", "rows": 0}
    cur.execute(f"SELECT TOP 3 * FROM dbo.[{name}] WHERE {where}", [value] * len(cols))
    names = [d[0] for d in cur.description]
    rows = [dict(zip(names, r)) for r in cur.fetchall()]
    shown = {}
    for row in rows:
        for col, v in row.items():
            if col.lower() not in FRAMEWORK and v not in (None, "") and col not in shown:
                shown[col] = _fmt(v)
    messages = list(dict.fromkeys(_fmt(v) for row in rows for v in row.values() if _message_like(v)))[:3]
    states = list(dict.fromkeys(f"{c}={v.strip()}" for row in rows for c, v in row.items()
                                if c.lower() not in FRAMEWORK and _status_like(v)))[:6]
    numbers = {c: float(v) for row in rows for c, v in row.items()
               if isinstance(v, (int, float, Decimal)) and not isinstance(v, bool)}
    return {"rows": count, "columns": shown, "numbers": numbers, "messages": messages,
            "text": f"{name}: {count} row(s) for {value}" + (f"; says: {' | '.join(messages)}" if messages else "")
                    + (f"; {', '.join(states)}" if states else "")}


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


def look_procedure(name: str, value: str) -> dict[str, Any]:
    """What the procedure's own log shows for this identifier (mode 18: none logged is evidence too)."""
    info = WORLD["procedures"].get(name, {})
    writes = ", ".join(f"{t} ({', '.join(c[:6])})" if c else t for t, c in list(info.get("writes", {}).items())[:6])
    mine = [r for r in runs_for(value) if r["proc"] == name]
    if not mine:
        if not info.get("runtime"):  # no log at all: nothing was seen, so nothing to judge
            return {"text": f"procedure {name}: keeps no log, so its runs cannot be seen. It writes {writes or 'nothing known'}.",
                    "observed": False}
        return {"text": f"procedure {name}: its log has no calls with {value} (it did not run for it). "
                        f"It writes {writes or 'nothing known'}."}
    r = mine[0]
    return {"text": f"procedure {name}: called {r['calls']} time(s) with @{r['param']}={value}, "
                    f"{str(r['first_on'])[:16]} to {str(r['last_on'])[:16]}, {r['error_steps']} error step(s). "
                    f"It writes {writes or 'nothing known'}."}


def look(node: dict[str, Any], value: str, conn) -> dict[str, Any]:
    conn.timeout = QUERY_TIMEOUT_S
    kind, name = node["kind"], node["title"]
    try:
        if kind in ("table", "view"):
            return look_table(name, value, conn)
        if kind == "procedure":
            return look_procedure(name, value)
    except Exception as exc:
        return {"text": f"{kind} {name}: could not read ({type(exc).__name__}: {str(exc)[:100]})", "observed": False}
    return {"text": f"{kind} {name}: {node.get('summary', '')}"}


# ---------- the world in GBrain ----------

class World:
    def __init__(self) -> None:
        self.brain = Brain()
        self.pages: dict[str, dict[str, Any]] = {}
        self._titles: dict[str, str] | None = None

    def titles(self) -> dict[str, str]:
        if self._titles is None:
            self._titles = {p.get("title"): p["slug"] for p in all_pages(self.brain)}
        return self._titles

    def page(self, slug: str) -> dict[str, Any]:
        if slug not in self.pages:
            p = self.brain.call("get_page", slug=slug, include_content=True)
            meta = p.get("frontmatter") or {}
            body = (p.get("compiled_truth") or p.get("content") or "").replace("\r", "")
            self.pages[slug] = {"slug": slug, "kind": meta.get("type") or p.get("type"), "title": meta.get("title") or p.get("title"),
                                "summary": re.sub(r"(?s)^.*?\n# [^\n]*\n\n", "", body)[:200].replace("\n", " ")}
        return self.pages[slug]

    def links(self, slug: str) -> list[dict[str, Any]]:
        out = []
        for direction, tool, end in (("out", "get_links", "to_slug"), ("in", "get_backlinks", "from_slug")):
            res = self.brain.call(tool, slug=slug)
            for l in res if isinstance(res, list) else res.get("links", []):
                if l.get(end):
                    out.append({"slug": l[end], "type": l.get("link_type"), "direction": direction,
                                "context": l.get("context") or ""})
        return out


def step_options(world: World, here: str, obs: dict[str, Any], value: str, conn) -> list[dict[str, Any]]:
    """Next steps from a visited node. Links to key pages become connectors: the other tables that
    hold the identifier value seen in this node's rows (mode 13: key pages themselves show nothing)."""
    me = world.page(here)
    options = []
    for l in world.links(here):
        other = world.page(l["slug"])
        if other["kind"] == "key":
            column = l["context"]
            seen = (obs.get("columns") or {}).get(column)
            if not seen or l["direction"] != "out":
                continue
            key = KEY_OF_COLUMN.get(f"{me['title']}.{column}")
            for colref in holders(key, seen, conn) if key else []:
                table = colref.split(".")[0]
                if table != me["title"] and table in world.titles():
                    options.append({"slug": world.titles()[table], "value": seen,
                                    "label": f"{colref} also holds {column} {seen} (seen in {me['title']})"})
            continue
        verb = l["type"] if l["direction"] == "out" else {"writes": "is written by", "reads": "is read by",
                                                           "calls": "is called by", "records_to": "is filled by event"}.get(l["type"], l["type"])
        ctx = f" ({l['context'][:80]})" if l["context"] else ""
        options.append({"slug": l["slug"], "value": value, "label": f"{me['title']} {verb} {other['kind']} {other['title']}{ctx}"})
    return options


def choose(world: World, ticket: str, trail: list[dict], options: list[dict]) -> dict | str:
    seen = [f"step {i + 1}: {s['observation']['text']}" for i, s in enumerate(trail)]
    if len(options) > MAX_OPTIONS:  # mode 14: pick the kind of step first
        kind_of = lambda o: world.page(o["slug"])["kind"]  # noqa: E731
        kinds = sorted({kind_of(o) for o in options})
        crit = {f"k{i}": f"look at a {k}" for i, k in enumerate(kinds)}
        a = jev({"ticket": ticket, "evidence_so_far": seen},
                {"kind": {"type": "choice", "criteria": crit,
                          "instructions": "Which kind of place should the investigation look at next?"}}).get("kind") or {}
        if a.get("choice") in crit:
            wanted = kinds[int(a["choice"][1:])]
            options = [o for o in options if kind_of(o) == wanted][:250]
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


def survey(world: World, entities: list[dict], conn) -> tuple[list[dict], list[dict]]:
    """Every table holding the identifier, looked at once (rows, messages, states, numbers), and every
    procedure the log index says ran for it. Returns (table surveys, procedure start options)."""
    tables, procs, titles = [], [], world.titles()
    for e in entities:
        for table in dict.fromkeys(h.split(".")[0] for h in e["holders"]):
            if table not in titles:
                continue
            try:
                conn.timeout = QUERY_TIMEOUT_S
                obs = look_table(table, e["value"], conn)
            except Exception as exc:
                obs = {"text": f"{table}: could not read ({type(exc).__name__})", "observed": False}
            tables.append({"slug": titles[table], "table": table, "value": e["value"], "obs": obs})
        for r in runs_for(e["value"]):
            if r["proc"] in titles:
                procs.append({"slug": titles[r["proc"]], "value": e["value"],
                              "label": f"procedure {r['proc']} ran {r['calls']} time(s) for {e['value']}, "
                                       f"{r['error_steps']} error step(s), last {str(r['last_on'])[:16]}"})
    return tables, procs


def judge_all(ticket: str, texts: list[str]) -> list[dict[str, Any]]:
    """One batched Jev call: each finding gets its own role (never one forced pick among many)."""
    if not texts:
        return []
    findings = {f"f{i}": t for i, t in enumerate(texts)}
    answers = jev({"ticket": ticket, "findings": findings},
                  {f"role_{k}": {"type": "choice", "criteria": ROLES,
                                 "instructions": {"task": "What part does this finding play in the requester's problem?",
                                                  "ticket_path": "ticket", "finding_path": f"findings.{k}"}}
                   for k in findings})
    return [{"role": (answers.get(f"role_{k}") or {}).get("choice"),
             "confidence": (answers.get(f"role_{k}") or {}).get("confidence")} for k in findings]


def trace_numbers(ticket: str, value: str, seen: list[dict]) -> dict[str, Any]:
    """Numbers the requester quotes -> every place they are stored among what was seen (code) ->
    which of those places the requester means (Jev, from their wording). Code never does arithmetic."""
    out, questions, options_by_n = {}, {}, {}
    for n in dict.fromkeys(_NUMBER.findall(entity_resolver._DATES.sub(" ", ticket).replace(value, " "))):
        sources = [f"{s['node']}.{c}" for s in seen for c, v in (s["obs"].get("numbers") or {}).items() if v == float(n)]
        sources += [f"{s['node']} (number of rows)" for s in seen if s["obs"].get("rows") == float(n)]
        sources = list(dict.fromkeys(sources))[:40]
        if not sources:
            out[n] = {"source": None, "candidates": [], "reason": "not stored in anything looked at"}
            continue
        options = {f"s{i}": s for i, s in enumerate(sources)}
        options["none"] = "None of these is where the requester's number comes from"
        options_by_n[n] = options
        questions[f"n{len(questions)}"] = {"type": "choice", "criteria": options,
                                           "instructions": f"The requester quotes the number {n}. Which stored value is "
                                                           "the one they are looking at (match the screen or report they name)?"}
    if questions:
        answers = jev({"ticket": ticket}, questions)
        for (n, options), q in zip(options_by_n.items(), questions):
            a = answers.get(q) or {}
            out[n] = {"source": options.get(a.get("choice")) if a.get("choice") != "none" else None,
                      "confidence": a.get("confidence"), "candidates": [v for k, v in options.items() if k != "none"]}
    return out


def walk(ticket: str, world: World | None = None, conn=None) -> dict[str, Any]:
    started = time.perf_counter()
    world = world or World()
    conn = conn or entity_resolver._connect()
    conn.timeout = QUERY_TIMEOUT_S * 3
    entities = resolve(ticket, conn)
    if not entities:
        return {"entities": [], "trail": [], "stopped": "no identifier from the ticket exists in XBatch",
                "seconds": round(time.perf_counter() - started, 1)}
    value = entities[0]["value"]
    trail: list[dict[str, Any]] = []
    visited: set[str] = set()
    tables, frontier = survey(world, entities, conn)
    observed = [t for t in tables if t["obs"].get("observed", True)]
    for t, role in zip(observed, judge_all(ticket, [t["obs"]["text"] for t in observed])):
        visited.add(t["slug"])
        if role["role"] != "unrelated":
            trail.append({"step": "survey", "node": t["table"], "kind": "table", "value": t["value"],
                          "observation": t["obs"], **role})
            frontier += step_options(world, t["slug"], t["obs"], t["value"], conn)
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
        obs = look(node, pick["value"], conn)
        if obs.get("columns"):
            keep = pick_columns(ticket, obs)
            obs["text"] += "; " + "; ".join(f"{c}={obs['columns'][c]}" for c in keep)
        # Nothing was seen (no identifier column, unreadable): record that, never ask Jev to judge nothing.
        role = judge(ticket, obs["text"]) if obs.get("observed", True) else {"role": "not_observed", "confidence": None}
        trail.append({"step": pick["label"], "node": node["title"], "kind": node["kind"], "value": pick["value"],
                      "observation": obs, **role})
        frontier += step_options(world, pick["slug"], obs, pick["value"], conn)
    seen = [{"node": t["table"], "obs": t["obs"]} for t in tables] + [{"node": s["node"], "obs": s["observation"]} for s in trail]
    numbers = trace_numbers(ticket, value, seen)
    return {"entities": entities, "trail": trail, "stopped": stopped, "numbers": numbers,
            "surveyed": len(tables), "seconds": round(time.perf_counter() - started, 1)}


if __name__ == "__main__":
    print(json.dumps(walk(" ".join(sys.argv[1:])), indent=1, default=str))
