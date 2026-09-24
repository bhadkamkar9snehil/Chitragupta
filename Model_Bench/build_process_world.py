#!/usr/bin/env python3
"""Build XBatch's process world: who writes/reads what, what triggers it, and what actually ran.

Read-only. Sources, each chosen because it is authoritative for its edge type:
  static  - sys.dm_sql_referenced_entities: SQL Server's own binder gives, per procedure, every
            table/column read (is_selected), written (is_updated) and procedure called.
  runtime - XStudio_Xbatch.dbo.XMES_Log_Trn_Tbl: the procedures' own transaction log. Per
            procedure: how often it ran, when, the ordered steps it logs, its error steps, the
            parameters it is called with (entity keys such as @HeatNo), and calls observed at runtime.
  events  - <Area>_Event_* configuration: event -> TransactionEntity (table), state conditions over
            historian tags, workflow on/off, and CaptureTagValue attribute -> column mappings.
  jobs    - msdb: SQL Agent job -> procedure.

Output: Knowledge/process_world.json (nodes + typed edges with source and confidence), plus an
acceptance report that checks the graph against chains documented in the vendor handover
(Knowledge/sohar-sms-event-workflows.md).

    python Model_Bench/build_process_world.py
"""
from __future__ import annotations

import json
import os
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import pyodbc

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "Knowledge" / "process_world.json"
DB = "XStudio_Xbatch"
DYNAMIC_SQL = re.compile(r"sp_executesql|EXEC\s*\(|EXECUTE\s*\(", re.I)
PARAM = re.compile(r"@(\w+)\s*=\s*('(?:[^']|'')*'|[^,\s]+)")
STEP_NO = re.compile(r"^\s*(\d+)\s")
ERROR_STEP = re.compile(r"error|fail|exception|raise", re.I)
CALL_STEP = re.compile(r"\b(?:EXEC(?:UTE)?|Procedure)\s+(?:dbo\.)?\[?([A-Za-z_][\w-]*)", re.I)

# Chains the vendor documented; the graph must reproduce them without being told.
ACCEPTANCE = [
    ("XMES_I_Billets_Tracking_Usp", "reads", "CCM_Per_Heat"),
    ("XSTUDIO_WORKFLOW_94F414DB-7BB1-4CCF-B50D-65A1E6101382_SP", "calls", "XMES_I_Billets_Tracking_Usp"),
    ("XSTUDIO_WORKFLOW_94F414DB-7BB1-4CCF-B50D-65A1E6101382_SP", "calls", "XMES_BackCalculation_GLS_Usp"),
    ("XSTUDIO_WORKFLOW_94F414DB-7BB1-4CCF-B50D-65A1E6101382_SP", "calls", "XBatch_SMS_Heat_Tracking_Daily_Production_Data"),
    ("XSTUDIO_WORKFLOW_94F414DB-7BB1-4CCF-B50D-65A1E6101382_SP", "writes", "CCM_Per_Heat"),
    ("XSTUDIO_WORKFLOW_CB83D9D0-0256-44F8-BC97-461935B736D8_SP", "writes", "EAF_PER_HEAT"),
    ("XSTUDIO_WORKFLOW_CB83D9D0-0256-44F8-BC97-461935B736D8_SP", "calls", "HeatChargeMixConsumption"),
    ("XSTUDIO_WORKFLOW_CB83D9D0-0256-44F8-BC97-461935B736D8_SP", "calls", "XBatch_I_Material_Produce_NoBOM_USP"),
    ("XSTUDIO_WORKFLOW_1A5F9D1B-7093-4BA2-9EAA-4ACD7371B992_SP", "calls", "XMES_LRF_I_Raw_Material_Cons_Usp"),
    ("XSTUDIO_WORKFLOW_18207AB4-8668-4F3C-B913-03CF7068BB96_SP", "writes", "CCM_Data"),
    ("XSTUDIO_WORKFLOW_64B14ECC-2663-434D-B0DC-FF705136AA3A_SP", "writes", "CCM_Data"),
]


def connect() -> pyodbc.Connection:
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};SERVER=" + os.environ.get("MSSQL_MCP_SERVER", "10.2.6.204")
        + ";UID=" + os.environ.get("MSSQL_MCP_USER", "sa") + ";PWD=" + os.environ["MSSQL_MCP_PASSWORD"]
        + f";TrustServerCertificate=yes;Connection Timeout=120;DATABASE={DB};", autocommit=True)
    conn.timeout = 0  # offline build: the 4.8M-row log aggregation takes minutes
    return conn


def rows(cur, sql: str, *params) -> list[dict]:
    cur.execute(sql, *params)
    names = [d[0] for d in cur.description]
    return [dict(zip(names, r)) for r in cur.fetchall()]


def object_types(cur) -> dict[str, str]:
    return {r["name"].lower(): r["type"].strip() for r in rows(cur, "SELECT name, type FROM sys.objects WHERE type IN ('U','V','P')")}


def static_references(cur, types: dict[str, str]) -> dict[str, dict]:
    """Per procedure: reads/writes (table -> columns) and calls, from SQL Server's binder."""
    procs = rows(cur, """SELECT p.name, m.definition FROM sys.procedures p
                         JOIN sys.sql_modules m ON m.object_id = p.object_id""")
    out: dict[str, dict] = {}
    for proc in procs:
        name, text = proc["name"], proc["definition"] or ""
        entry = {"reads": defaultdict(set), "writes": defaultdict(set), "calls": set(),
                 "dynamic_sql": bool(DYNAMIC_SQL.search(text)), "lines": text.count("\n") + 1, "bind_error": None}
        try:
            refs = rows(cur, "SELECT referenced_entity_name e, referenced_minor_name c, is_selected s, is_updated u "
                             "FROM sys.dm_sql_referenced_entities(?, 'OBJECT')", f"dbo.{name}")
        except pyodbc.Error as exc:
            entry["bind_error"] = str(exc).split("]")[-1][:200]
            refs = []
        for ref in refs:
            target = ref["e"]
            kind = types.get((target or "").lower())
            if kind == "P":
                entry["calls"].add(target)
            elif kind in ("U", "V"):
                bucket = entry["writes"] if ref["u"] else entry["reads"] if ref["s"] else None
                if bucket is not None:
                    bucket[target].update([ref["c"]] if ref["c"] else [])
        out[name] = entry
    return out


TEXT_WRITE = re.compile(r"\b(?:INSERT\s+INTO|UPDATE|MERGE(?:\s+INTO)?|DELETE\s+FROM)\s+"
                        r"(?:\[?\w+\]?\.)?(?:\[?dbo\]?\.)?\[?([A-Za-z_]\w*)\]?", re.I)
API_WRITE = re.compile(r"INSERT\s+INTO\s+\[?XStudio_XBatch\]?\.\[?dbo\]?\.\[?([A-Za-z_]\w*)\]?", re.I)


def text_writes(cur, types: dict[str, str]) -> dict[str, set[str]]:
    """Write targets named literally in procedure text, including inside dynamic-SQL strings.

    The binder cannot see dynamic SQL (127 procedures), e.g. the LRF workflow copies power and
    arcing values into LRF_Per_Heat via SP_EXECUTESQL. Medium confidence: text, not bound.
    """
    out: dict[str, set[str]] = defaultdict(set)
    for proc in rows(cur, "SELECT p.name, m.definition FROM sys.procedures p JOIN sys.sql_modules m ON m.object_id = p.object_id"):
        text = re.sub(r"--[^\n]*", "", proc["definition"] or "")
        for target in TEXT_WRITE.findall(text):
            if types.get(target.lower()) in ("U", "V"):
                out[proc["name"]].add(target)
    return out


def api_writes(cur) -> dict[str, set[str]]:
    """XStudio API framework inserts (SAP responses land in MES_SAP_* this way), from the config API log."""
    try:
        found = rows(cur, """SELECT ISNULL(APIName, CallerName) api, Message FROM XStudio_Configuration_Xbatch.dbo.XStudio_API_Error_Log_Mst_Tbl
                             WHERE Message LIKE '%Insertion Query%INSERT INTO%'""")
    except pyodbc.Error:
        return {}
    out: dict[str, set[str]] = defaultdict(set)
    for r in found:
        for target in API_WRITE.findall(r["Message"] or ""):
            out[f"api:{r['api'] or 'unknown'}"].add(target)
    return out


def runtime_log(cur) -> dict[str, dict]:
    """Per procedure, from its own transaction log."""
    summary = rows(cur, """SELECT Name, COUNT(*) n, MIN(CreatedOn) first_seen, MAX(CreatedOn) last_seen
                           FROM dbo.XMES_Log_Trn_Tbl WHERE Name IS NOT NULL GROUP BY Name""")
    steps = rows(cur, """SELECT Name, Status, COUNT(*) n FROM dbo.XMES_Log_Trn_Tbl
                         WHERE Name IS NOT NULL AND Status IS NOT NULL GROUP BY Name, Status""")
    samples = rows(cur, """SELECT Name, MAX(ExecutionQuery) q FROM dbo.XMES_Log_Trn_Tbl
                           WHERE Name IS NOT NULL AND ExecutionQuery IS NOT NULL GROUP BY Name""")
    out: dict[str, dict] = {}
    for s in summary:
        out[s["Name"]] = {"log_rows": s["n"], "first_seen": s["first_seen"], "last_seen": s["last_seen"],
                          "steps": [], "error_steps": [], "calls_observed": set(), "params": [], "sample_call": None}
    for st in steps:
        entry = out.get(st["Name"])
        if entry is None:
            continue
        status = st["Status"].strip()
        number = STEP_NO.match(status)
        entry["steps"].append((int(number.group(1)) if number else 999, status, st["n"]))
        if ERROR_STEP.search(status):
            entry["error_steps"].append(status)
        for called in CALL_STEP.findall(status):
            entry["calls_observed"].add(called)
    for sm in samples:
        entry = out.get(sm["Name"])
        if entry is not None:
            entry["sample_call"] = (sm["q"] or "")[:400]
            entry["params"] = sorted({p for p, _ in PARAM.findall(sm["q"] or "")})
    for entry in out.values():
        entry["steps"] = [f"{s}" for _, s, _ in sorted(entry["steps"])][:60]
    return out


def events(cur) -> list[dict]:
    """Event -> table, its states (conditions over tags, workflow flags) and tag -> column mappings."""
    out = []
    # Areas come from the catalog: every <Area>_Event_Configuration_Mst_Tbl that exists.
    areas = [r["name"][:-len("_Event_Configuration_Mst_Tbl")] for r in
             rows(cur, "SELECT name FROM sys.tables WHERE name LIKE '%[_]Event[_]Configuration[_]Mst[_]Tbl' ORDER BY name")]
    for area in areas:
        try:
            configs = rows(cur, f"SELECT ID, Name, TransactionEntity, IsActive, EventMstID FROM dbo.{area}_Event_Configuration_Mst_Tbl "
                                "WHERE ISNULL(IsDeleted,0)=0")
            states = rows(cur, f"SELECT ID, ParentID, StateName, StateSequence, StateCondition, IsActive, IsErrorState, "
                               f"IsWorkFlowEnable, StateOnWorkFlow, StateOffWorkFlow FROM dbo.{area}_Event_State_Mst_Tbl "
                               "WHERE ISNULL(IsDeleted,0)=0")
            actions = rows(cur, f"SELECT StateID, ActionType, StateMode, Configuration FROM dbo.{area}_Event_Action_Mst_Tbl "
                                "WHERE ISNULL(IsDeleted,0)=0")
        except pyodbc.Error:
            continue
        by_parent = defaultdict(list)
        for st in states:
            by_parent[str(st["ParentID"]).upper()].append(st)
        acts = defaultdict(list)
        for ac in actions:
            acts[str(ac["StateID"]).upper()].append(ac)
        for cfg in configs:
            ev_states = by_parent.get(str(cfg["ID"]).upper(), []) + by_parent.get(str(cfg["EventMstID"]).upper(), [])
            out.append({
                "area": area, "event": cfg["Name"], "table": cfg["TransactionEntity"], "active": bool(cfg["IsActive"]),
                "states": [{
                    "name": st["StateName"], "sequence": st["StateSequence"], "condition": st["StateCondition"],
                    "tags": sorted(set(re.findall(r"\{(\w+)\}", st["StateCondition"] or ""))),
                    "active": bool(st["IsActive"]), "error_state": bool(st["IsErrorState"]),
                    "workflow": bool(st["IsWorkFlowEnable"]), "on": st["StateOnWorkFlow"], "off": st["StateOffWorkFlow"],
                    "column_mappings": _mappings(acts.get(str(st["ID"]).upper(), [])),
                } for st in sorted(ev_states, key=lambda s: (s["StateSequence"] or 0, s["StateName"] or ""))],
            })
    return out


def _mappings(actions: list[dict]) -> list[dict]:
    maps = []
    for ac in actions:
        try:
            cfg = json.loads(ac["Configuration"] or "[]")
        except ValueError:
            continue
        for item in cfg if isinstance(cfg, list) else []:
            if isinstance(item, dict) and item.get("EntityAttribute"):
                maps.append({"tag_attribute": item.get("EventAttribute"), "column": item["EntityAttribute"],
                             "action": ac["ActionType"], "mode": ac["StateMode"]})
    return maps


def jobs(cur) -> list[dict]:
    try:
        found = rows(cur, """SELECT j.name job, j.enabled, s.database_name db, s.command FROM msdb.dbo.sysjobs j
                             JOIN msdb.dbo.sysjobsteps s ON s.job_id = j.job_id""")
    except pyodbc.Error:
        return []
    for job in found:
        job["procedures"] = sorted(set(re.findall(r"\[?([A-Za-z_]\w*(?:_USP|_Usp|_usp|_SP|_sp))\]?", job.pop("command") or "")))
    return found


def _merge_tables(bag: dict, canon) -> dict[str, list[str]]:
    """table -> columns, keyed by the object's real name (CCM_Per_Heat / CCM_PER_HEAT are one table)."""
    merged: dict[str, set] = defaultdict(set)
    for table, cols in bag.items():
        merged[canon(table)].update(cols)
    return {t: sorted(c) for t, c in merged.items()}


def schema(cur) -> dict:
    """Catalog facts per table/view (columns, rows) and per procedure (parameters); views' sources."""
    objs = {}
    for r in rows(cur, """SELECT o.name, o.type, c.name col, ty.name typ, c.max_length len, c.column_id
            FROM sys.objects o JOIN sys.columns c ON c.object_id=o.object_id JOIN sys.types ty ON ty.user_type_id=c.user_type_id
            WHERE o.type IN ('U','V') ORDER BY o.name, c.column_id"""):
        o = objs.setdefault(r["name"], {"kind": "table" if r["type"].strip() == "U" else "view", "columns": [], "rows": None})
        o["columns"].append(f"{r['col']} {r['typ']}" + (f"({r['len']})" if r["typ"] in ("varchar", "nvarchar", "char") else ""))
    for r in rows(cur, """SELECT OBJECT_NAME(object_id) name, SUM(row_count) n FROM sys.dm_db_partition_stats
                          WHERE index_id IN (0,1) GROUP BY object_id"""):
        if r["name"] in objs:
            objs[r["name"]]["rows"] = int(r["n"])
    for v in [n for n, o in objs.items() if o["kind"] == "view"]:
        try:
            refs = rows(cur, "SELECT DISTINCT referenced_entity_name e FROM sys.dm_sql_referenced_entities(?, 'OBJECT')", f"dbo.{v}")
            objs[v]["reads"] = sorted({r["e"] for r in refs if r["e"] in objs and r["e"] != v})
        except pyodbc.Error:
            objs[v]["reads"] = []
    params = defaultdict(list)
    for r in rows(cur, """SELECT OBJECT_NAME(p.object_id) proc_name, p.name, ty.name typ FROM sys.parameters p
                          JOIN sys.types ty ON ty.user_type_id=p.user_type_id
                          WHERE OBJECTPROPERTY(p.object_id,'IsProcedure')=1 ORDER BY p.object_id, p.parameter_id"""):
        params[r["proc_name"]].append(f"{r['name']} {r['typ']}")
    return {"objects": objs, "parameters": dict(params)}


KEY_TYPES = ("int", "bigint", "varchar", "nvarchar", "char", "nchar")
KEY_SAMPLE_ROWS = 500
KEY_QUERY_TIMEOUT_S = 20
KEY_MIN_SHARED = 10          # world mode 1: one shared value is coincidence
KEY_MIN_SHARED_RATIO = 0.2   # ... and it must be a real fraction of the smaller column
FRAMEWORK_TABLE_SHARE = 0.3  # world mode 3: a column on >30% of tables is framework, not a key
# Dates, clock times and durations ("00:13", "01:14", "0*:0*") are values, not identifiers.
_DATE_LIKE = re.compile(r"^\d{4}-\d{2}-\d{2}|^[\d*]{1,3}:[\d*]{2}(?::[\d*]{2})?$")


def keys(cur) -> dict:
    """Which columns hold the same identifier, derived from shared values (world modes 1-5)."""
    cols = rows(cur, """SELECT t.name tbl, c.name col, ty.name typ, c.max_length len
        FROM sys.columns c JOIN sys.tables t ON t.object_id=c.object_id JOIN sys.types ty ON ty.user_type_id=c.user_type_id""")
    n_tables = len({c["tbl"] for c in cols})
    per_col = defaultdict(set)
    for c in cols:
        per_col[c["col"].lower()].add(c["tbl"])
    framework = {name for name, tbls in per_col.items() if len(tbls) > FRAMEWORK_TABLE_SHARE * n_tables}
    by_table = defaultdict(list)
    stamps = defaultdict(dict)
    for c in cols:
        if c["col"].lower() in ("modifiedon", "createdon"):
            stamps[c["tbl"]][c["col"].lower()] = c["col"]
    # "Most recent" = ModifiedOn falling back to CreatedOn: file-imported tables (e.g.
    # Rebar_Coil_Quality_Data, 50,593 rows) never set ModifiedOn, so ordering by it alone is arbitrary.
    recency = {t: (f"COALESCE([{s['modifiedon']}], [{s['createdon']}])" if len(s) == 2 else f"[{next(iter(s.values()))}]")
               for t, s in stamps.items()}
    for c in cols:
        if (c["typ"] in KEY_TYPES and c["col"].lower() not in framework
                and (c["typ"] in ("int", "bigint") or 0 < c["len"] <= 120)):
            by_table[c["tbl"]].append(c["col"])
    values = {}  # "table.column" -> set of distinct sampled values
    skipped, unordered = [], []
    # World mode 9: one unindexed sort cannot stall the build. pyodbc applies the connection timeout
    # to cursors created after it is set, so sampling uses a fresh cursor.
    cur.connection.timeout = KEY_QUERY_TIMEOUT_S
    cur = cur.connection.cursor()
    for tbl, tcols in sorted(by_table.items()):
        select = f"SELECT TOP {KEY_SAMPLE_ROWS} {', '.join(f'[{c}]' for c in tcols)} FROM dbo.[{tbl}]"
        try:
            sample = rows(cur, select + (f" ORDER BY {recency[tbl]} DESC" if tbl in recency else ""))
        except pyodbc.Error:
            try:  # too slow to sort: sample anyway, and say the window may not line up (mode 2)
                sample = rows(cur, select)
                unordered.append(tbl)
            except pyodbc.Error as exc:
                skipped.append(f"{tbl}: {str(exc)[:80]}")
                continue
        for col in tcols:
            vals = {str(r[col]).strip() for r in sample if r[col] is not None}
            vals = {v for v in vals if len(v) >= 5 and not _DATE_LIKE.match(v)}  # modes 1, 2
            if vals:
                values[f"{tbl}.{col}"] = vals
    owners = defaultdict(set)
    for colref, vals in values.items():
        for v in vals:
            owners[v].add(colref)
    shared = defaultdict(int)
    for v, refs in owners.items():
        refs = sorted(refs)
        for i, a in enumerate(refs):
            for b in refs[i + 1:]:
                if a.split(".")[0] != b.split(".")[0]:
                    shared[(a, b)] += 1
    parent = {c: c for c in values}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    links = []
    for (a, b), n in shared.items():
        if n >= KEY_MIN_SHARED and n >= KEY_MIN_SHARED_RATIO * min(len(values[a]), len(values[b])):
            links.append({"a": a, "b": b, "shared": n})
            parent[find(a)] = find(b)
    groups = defaultdict(list)
    for colref in values:
        if any(colref in (l["a"], l["b"]) for l in links):
            groups[find(colref)].append(colref)
    groups = sorted(groups.values(), key=len, reverse=True)
    contained = _containment_pass(cur, groups, values)  # mode 2: windows that never overlapped
    out = {}
    for members in groups:
        if not members:
            continue
        names = defaultdict(int)
        for m in members:
            names[m.split(".", 1)[1]] += 1
        base = max(sorted(names), key=lambda n: names[n])
        label, n = base, 1
        while label in out:  # distinct page names for distinct keys
            n += 1
            label = f"{base}-{n}"
        out[label] = {"columns": sorted(members), "example": sorted(values[members[0]])[:3]}
    return {"keys": out, "links": links, "contained": contained, "skipped": skipped, "unordered": unordered,
            "framework_columns": sorted(framework)}


def add_view_keys(world: dict) -> int:
    """A view column holds a key when a table the view reads has a same-named column in that key.

    Views are what the XStudio screens list ("billet tracking screen"), so the walk must be able to
    match their rows too. Derived from the catalog (view -> tables it reads, column names)."""
    objs, added = world["schema"]["objects"], 0
    for view, obj in objs.items():
        if obj["kind"] != "view":
            continue
        view_cols = {c.split(" ")[0] for c in obj["columns"]}
        for info in world["keys"]["keys"].values():
            for ref in list(info["columns"]):
                table, col = ref.split(".", 1)
                if table in obj.get("reads", []) and col in view_cols and f"{view}.{col}" not in info["columns"]:
                    info["columns"].append(f"{view}.{col}")
                    added += 1
    return added


def _shape(value: str) -> str:
    return re.sub(r"[A-Za-z]+", "A", re.sub(r"\d+", lambda m: f"9{{{len(m.group())}}}", value))


KEY_CONTAIN_RATIO = 0.5   # half of a column's sampled values exist in the key's biggest tables
KEY_CONTAIN_SAMPLE = 200
KEY_ANCHORS = 3


def _containment_pass(cur, groups: list[list[str]], values: dict[str, set[str]]) -> list[dict]:
    """Join columns (and smaller keys) to a larger key when their values exist in the key's biggest tables.

    Membership, not sample overlap, so a table whose rows are months older still joins. Candidates are
    limited to keys whose value shapes match (shapes come from the sampled values). Merges in place.
    """
    shapes = [{_shape(v) for m in g for v in values[m]} for g in groups]
    keyed = {m for g in groups for m in g}
    # Candidates: every unkeyed column, then every member of every smaller key (tested as a whole key).
    candidates = [([c], None) for c in values if c not in keyed] + [(g, i) for i, g in enumerate(groups)]
    distinct: dict[str, int] = {}

    def breadth(colref: str) -> int:
        """Distinct values in the column: the widest columns are the key's most complete record.
        (Largest tables are billet-level logs holding only recent values; EAF_PER_HEAT holds all heats.)"""
        if colref not in distinct:
            table, col = colref.split(".", 1)
            try:
                cur.execute(f"SELECT COUNT(DISTINCT [{col}]) FROM dbo.[{table}]")
                distinct[colref] = int(cur.fetchone()[0])
            except pyodbc.Error:
                distinct[colref] = 0  # too slow to count: not used as an anchor
        return distinct[colref]

    def contained(sample: list[str], g: list[str]) -> tuple[int, str] | None:
        anchors = sorted(g, key=lambda c: -breadth(c))[:KEY_ANCHORS]
        exists = " OR ".join(f"EXISTS (SELECT 1 FROM dbo.[{a.split('.')[0]}] WHERE [{a.split('.', 1)[1]}] = v.x)"
                             for a in anchors)
        try:
            cur.execute(f"SELECT COUNT(*) FROM (VALUES {','.join('(?)' for _ in sample)}) v(x) WHERE {exists}", sample)
            hit = cur.fetchone()[0]
        except pyodbc.Error:
            return None  # type mismatch or too slow: no evidence, no join
        ok = hit >= KEY_MIN_SHARED and hit >= KEY_CONTAIN_RATIO * len(sample)
        return (hit, anchors[0]) if ok else None

    def sample_of(cols: list[str]) -> list[str]:
        # Evenly spread over the sorted values: the first N sorted are the oldest identifiers, which
        # may predate the key's tables entirely (rebar coil heats 1260xxx vs EAF from 1504334).
        vals = sorted({v for c in cols for v in values[c]})
        step = max(1, len(vals) // KEY_CONTAIN_SAMPLE)
        return vals[::step][:KEY_CONTAIN_SAMPLE]

    merged = []
    for cols, own in candidates:
        if own is not None and not groups[own]:
            continue  # already merged away
        sample = sample_of(cols)
        col_shapes = {_shape(v) for v in sample}
        for i, g in enumerate(groups):
            if i == own or not g or not col_shapes <= shapes[i]:
                continue
            if own is None and len(g) < 2:
                continue
            # Either side may hold the wider date range: a key of old+new heats contains a key of recent
            # heats but not the reverse, so keys are tested in both directions (world mode 2).
            found = contained(sample, g) or (contained(sample_of(g), groups[own]) if own is not None else None)
            if found:
                merged.append({"columns": cols, "into": g[0], "found": found[0], "of": len(sample)})
                groups[i].extend(c for c in cols if c not in groups[i])
                shapes[i] |= col_shapes
                if own is not None:
                    groups[own] = []
                break
    return merged


def assemble(static: dict, runtime: dict, evts: list, jbs: list, txt: dict, api: dict, canon) -> dict:
    procedures, tables = {}, defaultdict(lambda: {"writers": {}, "readers": set(), "events": []})
    for name in sorted(set(static) | set(runtime)):
        st, rt = static.get(name, {}), runtime.get(name, {})
        calls = set(st.get("calls", set())) | {c for c in rt.get("calls_observed", set()) if c in static}
        writes = _merge_tables(st.get("writes", {}), canon)
        text_only = sorted({canon(t) for t in txt.get(name, set())} - set(writes))
        procedures[name] = {
            "kind": _kind(name),
            "reads": _merge_tables(st.get("reads", {}), canon),
            "writes": writes,
            "writes_via_text": text_only,
            "calls": sorted(calls),
            "dynamic_sql": st.get("dynamic_sql"), "lines": st.get("lines"), "bind_error": st.get("bind_error"),
            "runtime": {k: v for k, v in rt.items() if k != "calls_observed"} or None,
        }
        for t in writes:
            tables[t]["writers"][name] = "bound"
        for t in text_only:
            tables[t]["writers"].setdefault(name, "text")
        for t in procedures[name]["reads"]:
            tables[t]["readers"].add(name)
    for writer, targets in api.items():
        for t in targets:
            tables[canon(t)]["writers"].setdefault(writer, "api_log")
    for ev in evts:
        if ev["table"]:
            tables[canon(ev["table"])]["events"].append(f"{ev['area']}:{ev['event']}")
    edges = []
    for p, info in procedures.items():
        conf = "runtime+static" if info["runtime"] else "static"
        edges += [{"from": p, "type": "writes", "to": t, "confidence": conf} for t in info["writes"]]
        edges += [{"from": p, "type": "writes", "to": t, "confidence": "text"} for t in info["writes_via_text"]]
        edges += [{"from": t, "type": "read_by", "to": p, "confidence": conf} for t in info["reads"]]
        edges += [{"from": p, "type": "calls", "to": c, "confidence": conf} for c in info["calls"]]
    for writer, targets in api.items():
        edges += [{"from": writer, "type": "writes", "to": canon(t), "confidence": "api_log"} for t in sorted(targets)]
    for ev in evts:
        if ev["table"]:
            edges.append({"from": f"event:{ev['area']}:{ev['event']}", "type": "creates_rows_in",
                          "to": canon(ev["table"]), "confidence": "config"})
    for job in jbs:
        edges += [{"from": f"job:{job['job']}", "type": "runs", "to": p, "confidence": "msdb"} for p in job["procedures"]]
    return {
        "built": datetime.now().isoformat(timespec="seconds"), "database": DB,
        "procedures": procedures,
        "api_writers": {k: sorted(canon(t) for t in v) for k, v in api.items()},
        "tables": {t: {"writers": dict(sorted(v["writers"].items())), "readers": sorted(v["readers"]), "events": v["events"]}
                   for t, v in sorted(tables.items())},
        "events": evts, "jobs": jbs, "edges": edges,
    }


def _kind(name: str) -> str:
    n = name.lower()
    if n.startswith("xstudio_workflow"):
        return "workflow"
    if "api_error" in n:
        return "error_sink"
    if "sap" in n:
        return "sap_integration"
    if n.startswith("xstudio_") and n.endswith("_usp"):
        return "crud"
    return "procedure"


def acceptance(world: dict) -> list[tuple[str, bool]]:
    results = []
    for proc, relation, target in ACCEPTANCE:
        info = world["procedures"].get(proc) or {}
        bag = {"reads": info.get("reads", {}),
               "writes": list(info.get("writes", {})) + info.get("writes_via_text", []),
               "calls": info.get("calls", [])}[relation]
        hit = any(target.lower() == str(x).lower() for x in bag)
        results.append((f"{proc[:48]} {relation} {target}", hit))
    return results


def coverage(world: dict) -> dict:
    procs = world["procedures"]
    return {
        "procedures": len(procs),
        "bound_by_parser": sum(1 for p in procs.values() if p["lines"] and not p["bind_error"]),
        "bind_errors": sum(1 for p in procs.values() if p["bind_error"]),
        "dynamic_sql": sum(1 for p in procs.values() if p["dynamic_sql"]),
        "with_runtime_log": sum(1 for p in procs.values() if p["runtime"]),
        "tables_with_known_writer": sum(1 for t in world["tables"].values() if t["writers"]),
        "tables_total": len(world["tables"]),
        "events": len(world["events"]),
        "edges": len(world["edges"]),
    }


def main() -> None:
    cur = connect().cursor()
    if "--keys-only" in os.sys.argv or "--view-keys-only" in os.sys.argv:  # rest of the build takes ~20 min
        world = json.loads(OUT.read_text(encoding="utf-8"))
        if "--keys-only" in os.sys.argv:
            world["keys"] = keys(cur)
        print(f"view key columns added {add_view_keys(world)}")
        OUT.write_text(json.dumps(world, indent=1, default=str), encoding="utf-8")
        k = world["keys"]
        print(f"keys {len(k['keys'])}, contained joins {len(k['contained'])}, unordered {k['unordered']}")
        for c in k["contained"]:
            print(f"  joined {c['columns'][:3]} into {c['into']} ({c['found']}/{c['of']})")
        return
    types = object_types(cur)
    names = {r["name"].lower(): r["name"] for r in rows(cur, "SELECT name FROM sys.objects WHERE type IN ('U','V')")}
    canon = lambda t: names.get(str(t).lower(), t)  # noqa: E731
    world = assemble(static_references(cur, types), runtime_log(cur), events(cur), jobs(cur),
                     text_writes(cur, types), api_writes(cur), canon)
    world["schema"] = schema(cur)
    world["keys"] = keys(cur)
    add_view_keys(world)
    world["jobs"] = [j for j in world["jobs"] if j["procedures"]]  # jobs that run none of our procedures add nothing
    world["coverage"] = coverage(world)
    world["acceptance"] = [{"check": c, "passed": ok} for c, ok in acceptance(world)]
    OUT.write_text(json.dumps(world, indent=1, default=str), encoding="utf-8")
    print(json.dumps(world["coverage"], indent=1))
    passed = sum(1 for a in world["acceptance"] if a["passed"])
    print(f"acceptance: {passed}/{len(world['acceptance'])}")
    for a in world["acceptance"]:
        print(("  PASS " if a["passed"] else "  MISS ") + a["check"])
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
