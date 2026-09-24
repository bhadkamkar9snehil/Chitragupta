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
from datetime import date, timedelta
from decimal import Decimal
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_process_world import connect  # noqa: E402  (the world's SQL connection owner)
from l2_gbrain import Brain  # noqa: E402  (the one GBrain owner)

ROOT = Path(__file__).resolve().parent.parent
WORLD = json.loads((ROOT / "Knowledge" / "process_world.json").read_text(encoding="utf-8"))
WORLD_INDEX = ROOT / ".cache" / "world_index.sqlite"  # built by build_process_world.py
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


# ---------- where an identifier lives (build-time value index over the world's keys) ----------

# Shared keys plus identifiers held by one table only (e.g. a material document names one posting).
# Only base tables: a view's rows come from them.
KEY_COLUMNS = {k: [c for c in info["columns"] if is_table(c.split(".")[0])] for k, info in WORLD["keys"]["keys"].items()}
KEY_COLUMNS.update({c: [c] for c in WORLD["keys"].get("identifiers", {}) if is_table(c.split(".")[0])})
KEY_OF_COLUMN = {c: k for k, cols in KEY_COLUMNS.items() for c in cols}


def _index(sql: str, *params) -> list[tuple]:
    if not WORLD_INDEX.exists():
        return []
    db = sqlite3.connect(f"file:{WORLD_INDEX}?mode=ro", uri=True)
    rows = db.execute(sql, params).fetchall()
    db.close()
    return rows


def holders(key: str, value: str) -> list[str]:
    """Columns of this key that hold the value (value index; no live scan)."""
    cols = set(KEY_COLUMNS.get(key, []))
    return [c for (c,) in _index("SELECT colref FROM value_columns WHERE value = ?", value) if c in cols]


_DATES = re.compile(r"\d{4}-\d{2}-\d{2}(?:[ T]\d{2}:\d{2}(?::\d{2})?(?:\.\d+)?)?|\b\d{1,2}:\d{2}(?::\d{2})?\b")
# A trailing full stop ends a sentence ("heat 1604014."); only ".<digit>" makes it a decimal.
_SPAN = re.compile(r"(?<![\d.])(\d{7}_S\d+_\d+|\d{7,12})(?!\d|\.\d)")


def spans(text: str) -> list[str]:
    """Identifier-like spans: 7-12 digit numbers and billet codes, glued or not. Dates/times first
    removed; decimals and short numbers never match (e2e/ENTITY_FAILURE_MODES.md modes 2, 6-8)."""
    cleaned = _DATES.sub(" ", text)
    cleaned = re.sub(r"(?i)\b(?:heat|ht|h|wo|doc)(?=\d)", " ", cleaned)  # heat1604015, H1604014
    return list(dict.fromkeys(_SPAN.findall(cleaned)))[:6]


def subject(text: str, entities: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Several identifiers confirmed (heat + material document): Jev picks the one the question is
    about, the rest stay as related (ENTITY_FAILURE_MODES mode 3). Returns entities, subject first."""
    if len({e["value"] for e in entities}) < 2:
        return entities
    options = {f"c{i}": f"{e['key']} {e['value']}" for i, e in enumerate(entities)}
    a = jev({"ticket": text, "candidates": options},
            {"subject": {"type": "choice", "criteria": options,
                         "instructions": "Which item is the requester's question actually about? The others may be mentioned as context."}}
            ).get("subject") or {}
    first = int(a["choice"][1:]) if a.get("choice") in options else 0
    return [entities[first]] + [e for i, e in enumerate(entities) if i != first]


def resolve(text: str, conn=None) -> list[dict[str, Any]]:
    """Identifier spans -> the key/identifier columns that hold each value (value index)."""
    found = []
    for span in spans(text):
        by_key: dict[str, list[str]] = {}
        for (colref,) in _index("SELECT colref FROM value_columns WHERE value = ?", span):
            if colref in KEY_OF_COLUMN:
                by_key.setdefault(KEY_OF_COLUMN[colref], []).append(colref)
        found += [{"value": span, "key": k, "holders": cols} for k, cols in by_key.items()]
    return found


# ---------- what ran for an identifier (build-time log index; the 3.5 GB log has no usable index) ----------

def runs_for(value: str) -> list[dict[str, Any]]:
    rows = _index("SELECT proc, param, calls, steps, error_steps, first_on, last_on FROM runs WHERE value = ?", value)
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


# Inside a live run the runtime passes run_id: every read then goes through the bridge's audited read
# (Hermes_L2_Execute_SQL_Usp), so each finding carries an action ID the reviewer can verify.
# ponytail: module state, because the CLI runs one ticket per process.
_AUDIT: dict[str, Any] = {}


def _literal(table: str, column: str, value: str) -> str:
    decl = next((c for c in OBJS.get(table, {}).get("columns", []) if c.split(" ")[0] == column), "")
    numeric = decl.split(" ")[1].split("(")[0] in _INT_LIMITS if " " in decl else False
    return value if numeric else "N'" + value.replace("'", "''") + "'"  # numeric: _can_hold checked digits


def _read(conn, sql: str, table: str, column: str, value: str) -> tuple[list[dict[str, Any]], str | None]:
    """One read of `sql`: audited (rows + action ID) inside a run, plain otherwise (tests)."""
    if _AUDIT:
        from xstudio_l2_tool_bridge import _audited_probe_read
        rows, action_id = _audited_probe_read(_AUDIT["client"], run_id=_AUDIT["run_id"], database="XStudio_Xbatch",
                                              table=table, sql=sql, operation="world_walk",
                                              filter_column=column, filter_value=value)
        return [r for r in rows if isinstance(r, dict)], action_id
    cur = conn.cursor()
    cur.execute(sql)
    names = [d[0] for d in cur.description]
    return [dict(zip(names, r)) for r in cur.fetchall()], None


def look_table(name: str, value: str, conn) -> dict[str, Any]:
    cols = sorted({c.split(".", 1)[1] for cs in KEY_COLUMNS.values() for c in cs if c.split(".", 1)[0] == name}
                  | {c.split(".", 1)[1] for k, info in WORLD["keys"]["keys"].items() for c in info["columns"]
                     if c.split(".", 1)[0] == name})
    cols = [c for c in cols if _can_hold(name, c, value)]
    if not cols:
        return {"text": f"{name}: holds no identifier column for a value like {value}", "observed": False}
    where = " OR ".join(f"[{c}] = {_literal(name, c, value)}" for c in cols)
    rows, action_id = _read(conn, f"SELECT TOP 3 *, COUNT(*) OVER () AS [__rows] FROM dbo.[{name}] WHERE {where}",
                            name, cols[0], value)
    count = int(rows[0].pop("__rows")) if rows else 0
    for row in rows[1:]:
        row.pop("__rows", None)
    probe = {"ok": True, "probe_possible": True, "table": name, "database": "XStudio_Xbatch",
             "identifier": {cols[0]: value}, "rows": rows, "action_id": action_id}
    if not count:
        return {"text": f"{name}: no rows for {value}", "rows": 0, "probe": probe}
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
    return {"rows": count, "columns": shown, "numbers": numbers, "messages": messages, "probe": probe,
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


# ---------- tickets without an identifier: time window and health (activity index) ----------

_MONTHS = {m: i for i, m in enumerate(("jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"), 1)}


def window(text: str, today: date | None = None) -> date | None:
    """Start of the period the requester means, parsed in code (Jev 1.13 is weak at dates).
    None when the ticket names no period."""
    today = today or date.today()
    t = text.lower()
    m = re.search(r"(?:since|after|from)\s+(\d{1,2})(?:st|nd|rd|th)?(?:\s+(?:of\s+)?([a-z]{3})[a-z]*)?", t)
    if m:
        day, named = int(m.group(1)), _MONTHS.get((m.group(2) or "")[:3])
        if named:  # "8th July": this year unless that is still ahead
            return date(today.year if (named, day) <= (today.month, today.day) else today.year - 1, named, day)
        if day <= today.day:  # "since 8th": this month, or last month if the day is still ahead
            return date(today.year, today.month, day)
        prev = today.replace(day=1) - timedelta(days=1)
        return prev.replace(day=min(day, prev.day))
    if re.search(r"last night|yesterday", t):
        return today - timedelta(days=1)
    if re.search(r"this week|last few days|past few days|last week", t):
        return today - timedelta(days=7)
    if re.search(r"since morning|today|this morning|morning shift", t):
        return today
    return None


def table_health(name: str, since: date | None) -> str:
    """Rows arriving per day vs the table's own history, said in words; all arithmetic here."""
    days = [(date.fromisoformat(d), n) for d, n in _index("SELECT day, rows FROM table_daily WHERE table_name = ? ORDER BY day", name)]
    if not days:
        return f"{name}: no dated rows (or not indexed)"
    last_day = days[-1][0]
    recent = [n for _, n in days[-30:]]
    usual = sorted(recent)[len(recent) // 2]
    text = f"{name}: last rows on {last_day} ({(date.today() - last_day).days} days ago); usually ~{usual} rows/day on active days"
    if since:
        in_window = sum(n for d, n in days if d >= since)
        text += f"; {in_window} rows since {since}"
        if since > last_day:
            text += f" (nothing has arrived since {last_day})"
    return text


def proc_health(name: str, since: date | None) -> str | None:
    """None when the procedure keeps no log: nothing was seen, so there is nothing to judge."""
    days = _index("SELECT day, steps, error_steps FROM proc_daily WHERE proc = ? ORDER BY day", name)
    if not days:
        return None
    last = days[-1]
    text = f"procedure {name}: last ran {last[0]}"
    if since:
        steps = sum(s for d, s, _ in days if d >= str(since))
        errors = sum(e for d, _, e in days if d >= str(since))
        text += f"; since {since}: {steps} steps, {errors} error steps"
    return text


_CODE = re.compile(r"\b(?=[\w/-]*[A-Za-z])(?=[\w/-]*\d)[\w/-]{4,24}\b")
MASTER_MAX_ROWS = 200_000  # only look codes up in master-sized tables; bigger ones need an identifier


def codes(text: str) -> list[str]:
    """Codes the requester names (grade B500SX, material HHMNB500B_GLS): letters and digits mixed,
    not a plain number (those are identifiers, handled by the value index)."""
    return [c for c in dict.fromkeys(_CODE.findall(text)) if not c.isdigit()][:4]


def code_presence(tables: list[str], found_codes: list[str], conn) -> list[dict[str, Any]]:
    """Is each code present in the text columns of the in-scope tables? Code checks; Jev judges."""
    out = []
    for table in dict.fromkeys(t for t in tables if is_table(t) and (OBJS[t].get("rows") or 0) <= MASTER_MAX_ROWS):
        cols = [c.split(" ")[0] for c in OBJS[table]["columns"]
                if c.split(" ")[1].split("(")[0] in ("varchar", "nvarchar", "char") and c.split(" ")[0].lower() not in FRAMEWORK]
        if not cols:
            continue
        for code in found_codes:
            sql = f"SELECT TOP 1 * FROM dbo.[{table}] WHERE " + " OR ".join(f"[{c}] = {_literal(table, c, code)}" for c in cols)
            try:
                rows, action_id = _read(conn, sql, table, cols[0], code)
            except Exception:
                continue
            text = (f"{code} is in {table}" if rows else
                    f"{code} is not in {table} (checked {', '.join(cols[:6])}{'...' if len(cols) > 6 else ''})")
            probe = {"ok": True, "probe_possible": True, "table": table, "database": "XStudio_Xbatch",
                     "identifier": {cols[0]: code}, "rows": rows, "action_id": action_id}
            out.append({"slug": None, "node": table, "kind": "table", "value": None, "obs": {"text": text, "probe": probe}})
    return out


def health(node: dict[str, Any], since: date | None) -> dict[str, Any]:
    """What code can say about a page without an identifier: activity vs history, screen filters."""
    kind, name = node["kind"], node["title"]
    if kind == "table":
        return {"text": table_health(name, since)}
    if kind == "procedure":
        text = proc_health(name, since)
        return {"text": text} if text else {"text": f"procedure {name}: keeps no log", "observed": False}
    if kind == "view":
        bases = [t for t in OBJS.get(name, {}).get("reads", []) if is_table(t)][:4]
        return {"text": f"view {name} reads " + "; ".join(table_health(t, since) for t in bases) if bases
                        else f"view {name}: reads no table directly"}
    if kind == "screen":
        s = next((s for s in WORLD.get("screens", []) if s["menu"] == name), {})
        bases = [t for t in OBJS.get(s.get("view") or "", {}).get("reads", []) if is_table(t)][:3]
        return {"text": f"screen '{name}' shows {s.get('view')}; "
                        + (f"filter: only rows where {s['filter']}" if s.get("filter") else "no filter")
                        + "".join(f"; {table_health(t, since)}" for t in bases)}
    return {"text": f"{kind} {name}: {node.get('summary', '')}"}


def look(node: dict[str, Any], value: str | None, conn, since: date | None = None) -> dict[str, Any]:
    if value is None:
        return health(node, since)
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
            self._titles = {p.get("title"): p["slug"] for p in self.brain.all_pages()}
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
            for colref in holders(key, seen) if key else []:
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
    text = _DATES.sub(" ", ticket)
    for n in dict.fromkeys(_NUMBER.findall(text.replace(value, " ") if value else text)):
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


ROUTES = {
    "data": "XBatch data, a screen, a report or the SAP interface is missing, wrong, stuck or failing",
    "how_to": "The requester asks how to do something in XBatch",
    "access": "Login, password, permission or user account problem",
    "infrastructure": "The system is slow, down or not reachable for everyone",
    "hardware": "Printer, scanner, PC, network or other device problem",
    "change_request": "A request to change, add or customise how XBatch works",
}
SCOPE_TYPES = ["screen", "table", "view", "procedure", "event", "api"]
SCOPE_MIN = 0.30  # TypeSafe skill-suggestion cookbook: nothing fits below 0.30


def understand(ticket: str) -> dict[str, Any]:
    """What kind of escalation this is (route). One call; code acts on the answer."""
    a = jev({"ticket": ticket}, {"route": {"type": "choice", "criteria": ROUTES,
                                           "instructions": "What is the requester's problem about?"}}).get("route") or {}
    return {"route": a.get("choice") or "data", "confidence": a.get("confidence")}


def scope(world: World, ticket: str) -> list[dict[str, Any]]:
    """User words -> world pages: GBrain hybrid search gives candidates, Jev scores each one
    (reranking), the best few above the gate are the scope (skill-suggestion pattern)."""
    hits = world.brain.call("search", query=ticket, limit=30, types=SCOPE_TYPES, source_id="xstudio-knowledge")
    hits = hits if isinstance(hits, list) else hits.get("results") or hits.get("hits") or []
    pages = [world.page(h["slug"]) for h in hits if h.get("slug", "").startswith("knowledge/world/")]
    pages = list({p["slug"]: p for p in pages}.values())
    if not pages:
        return []
    cands = {f"c{i}": f"{p['kind']} {p['title']}: {p['summary']}" for i, p in enumerate(pages)}
    answers = jev({"ticket": ticket, "candidates": cands},
                  {f"fit_{k}": {"type": "noul", "instructions": {
                      "task": "Is this the screen, report, table or process the requester is talking about, "
                              "or where the data they describe is kept?",
                      "ticket_path": "ticket", "candidate_path": f"candidates.{k}"}} for k in cands})
    scored = sorted(((float((answers.get(f"fit_{k}") or {}).get("noul") or 0), p) for k, p in zip(cands, pages)),
                    key=lambda x: -x[0])
    return [dict(p, fit=round(s, 2)) for s, p in scored[:5] if s >= SCOPE_MIN]


def walk(ticket: str, world: World | None = None, conn=None) -> dict[str, Any]:
    started = time.perf_counter()
    world = world or World()
    conn = conn or connect()
    conn.timeout = QUERY_TIMEOUT_S * 3
    intent = understand(ticket)
    if intent["route"] != "data":  # not an L2 data investigation: route it
        return {"route": intent["route"], "data": False, "trail": [], "stopped": f"routed: {intent['route']}",
                "seconds": round(time.perf_counter() - started, 1)}
    entities = subject(ticket, resolve(ticket, conn))
    if spans(ticket) and not entities:  # names an identifier XBatch does not hold: ask, don't guess
        return {"route": "data", "data": True, "entities": [], "trail": [], "missing": spans(ticket),
                "stopped": "no identifier from the ticket exists in XBatch", "seconds": round(time.perf_counter() - started, 1)}
    since = window(ticket)
    value = entities[0]["value"] if entities else None
    trail: list[dict[str, Any]] = []
    visited: set[str] = set()
    if entities:
        tables, frontier = survey(world, entities, conn)
        starts = [{"slug": t["slug"], "node": t["table"], "kind": "table", "value": t["value"], "obs": t["obs"]} for t in tables]
    else:  # no identifier: scope from the requester's words, evidence from activity and screen filters
        tables, frontier = [], []
        pages = scope(world, ticket)
        starts = [{"slug": p["slug"], "node": p["title"], "kind": p["kind"], "value": None, "obs": health(p, since)}
                  for p in pages]
        if codes(ticket):  # "grade B500SX not in dropdown": is the code in the scope's master tables?
            in_scope = [t for p in pages for t in [p["title"]] + OBJS.get(p["title"], {}).get("reads", [])
                        + OBJS.get(next((s["view"] for s in WORLD.get("screens", []) if s["menu"] == p["title"]), ""), {}).get("reads", [])]
            starts += code_presence(in_scope, codes(ticket), conn)
        if not starts:
            return {"route": "data", "data": True, "entities": [], "trail": [], "since": str(since),
                    "stopped": "nothing in the world matches the requester's words: ask them which screen or report",
                    "seconds": round(time.perf_counter() - started, 1)}
    observed = [s for s in starts if s["obs"].get("observed", True)]
    for s, role in zip(observed, judge_all(ticket, [s["obs"]["text"] for s in observed])):
        if s["slug"]:
            visited.add(s["slug"])
        if role["role"] != "unrelated":
            trail.append({"step": "survey", "node": s["node"], "kind": s["kind"], "value": s["value"],
                          "observation": s["obs"], **role})
            if s["slug"]:  # a code check is a finding, not a place to go from
                frontier += step_options(world, s["slug"], s["obs"], s["value"], conn)
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
        obs = look(node, pick["value"], conn, since)
        if obs.get("columns"):
            keep = pick_columns(ticket, obs)
            obs["text"] += "; " + "; ".join(f"{c}={obs['columns'][c]}" for c in keep)
        # Nothing was seen (no identifier column, unreadable): record that, never ask Jev to judge nothing.
        role = judge(ticket, obs["text"]) if obs.get("observed", True) else {"role": "not_observed", "confidence": None}
        trail.append({"step": pick["label"], "node": node["title"], "kind": node["kind"], "value": pick["value"],
                      "observation": obs, **role})
        frontier += step_options(world, pick["slug"], obs, pick["value"], conn)
    seen = [{"node": s["node"], "obs": s["obs"]} for s in starts] + [{"node": s["node"], "obs": s["observation"]} for s in trail]
    numbers = trace_numbers(ticket, value or "", seen)
    # Every read, in the shape the runtime's evidence consumers (direct_answer, reviewer) already use.
    probes = [{"probe": s["obs"]["probe"]} for s in seen if s["obs"].get("probe")]
    return {"route": "data", "data": True, "entities": entities, "since": str(since), "trail": trail, "stopped": stopped,
            "numbers": numbers, "surveyed": len(starts), "probes": probes,
            "seconds": round(time.perf_counter() - started, 1)}


def main() -> int:
    """Runtime entry: JSON request on stdin {"ticket_text", "run_id"}; JSON result on stdout.
    With a run_id every SQL read is audited against that run. Debug: world_walk.py "<ticket text>"."""
    if len(sys.argv) > 1:
        print(json.dumps(walk(" ".join(sys.argv[1:])), indent=1, default=str))
        return 0
    req = json.loads(sys.stdin.read() or "{}")
    if req.get("run_id"):
        from xstudio_l2_tool_bridge import _client
        _AUDIT.update(client=_client(), run_id=str(req["run_id"]))
    try:
        result = walk(str(req.get("ticket_text") or ""))
    except Exception as exc:  # the runtime falls back to its own path; never a traceback on stdout
        result = {"ok": False, "error": f"{type(exc).__name__}: {str(exc)[:300]}"}
    finally:
        if _AUDIT.get("client"):
            _AUDIT["client"].close()
    print(json.dumps({"ok": "error" not in result, **result}, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
