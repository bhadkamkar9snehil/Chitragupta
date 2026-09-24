#!/usr/bin/env python3
"""Knowledge/process_world.json -> Knowledge/world/<kind>/<name>.md (one GBrain page per node) + links.jsonl.

Everything on a page is generated from XBatch (catalog, procedure code, runtime log, event
configuration, value-derived keys). No hand-written descriptions. GBrain syncs Knowledge/world
only; world_links.py then adds the typed links from links.jsonl.

    python Model_Bench/build_world_pages.py
"""
from __future__ import annotations

import json
import re
import shutil
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORLD_JSON = ROOT / "Knowledge" / "process_world.json"
OUT = ROOT / "Knowledge" / "world"


def slug_name(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", name).strip("_")


def page_path(kind: str, name: str) -> str:
    return f"{kind}/{slug_name(name)}"


def front(kind: str, name: str, built: str) -> str:
    return f"---\ntype: {kind}\ntitle: \"{name}\"\nbuilt: \"{built}\"\n---\n\n# {name}\n\n"


def build(world: dict) -> tuple[dict[str, str], list[dict]]:
    built, objs, params = world["built"], world["schema"]["objects"], world["schema"]["parameters"]
    pages: dict[str, str] = {}
    links: list[dict] = []
    held = defaultdict(list)  # table -> [(column, key)]
    for key, info in world["keys"]["keys"].items():
        for ref in info["columns"]:
            table, column = ref.split(".", 1)
            held[table].append((column, key))

    def link(frm: str, to: str, kind: str, context: str = "") -> None:
        links.append({"from": frm, "to": to, "type": kind, "context": context})

    # Tables and views.
    tables = world["tables"]
    for name, obj in sorted(objs.items()):
        me = page_path(obj["kind"], name)
        info = tables.get(name, {"writers": {}, "readers": [], "events": []})
        lines = [f"{obj['kind'].capitalize()} in {world['database']}. Rows: "
                 + (f"{obj['rows']:,}" if obj.get("rows") is not None else "unknown") + "."]
        if held[name]:
            lines.append("\n## Identifiers it holds\n")
            for column, key in sorted(held[name]):
                lines.append(f"- {column}: same values as key `{key}`")
                link(me, page_path("key", key), "holds", column)
        if obj["kind"] == "view" and obj.get("reads"):
            lines.append("\n## Reads\n")
            for src in obj["reads"]:
                lines.append(f"- {src}")
                link(me, page_path(objs.get(src, {}).get("kind", "table"), src), "reads")
        for title, items in (("Written by", sorted(info["writers"].items())), ("Read by", [(r, "") for r in info["readers"]])):
            if items:
                lines.append(f"\n## {title}\n")
                lines += [f"- {w}" + (f" ({how})" if how and how != "bound" else "") for w, how in items]
        if info["events"]:
            lines.append("\n## Rows created by events\n")
            lines += [f"- {e}" for e in info["events"]]
        lines.append("\n## Columns\n")
        lines += [f"- {c}" for c in obj["columns"]]
        pages[me] = front(obj["kind"], name, built) + "\n".join(lines) + "\n"

    # Procedures.
    for name, p in sorted(world["procedures"].items()):
        me = page_path("procedure", name)
        lines = []
        if params.get(name):
            lines.append("Parameters: " + ", ".join(params[name]) + ".")
        if p["dynamic_sql"]:
            lines.append("Builds SQL at runtime; some of what it touches is only visible in its text.")
        if p["bind_error"]:
            lines.append(f"SQL Server could not resolve its references: {p['bind_error']}")
        for title, kind, bag in (("Writes", "writes", p["writes"]), ("Reads", "reads", p["reads"])):
            if bag:
                lines.append(f"\n## {title}\n")
                for table, cols in sorted(bag.items()):
                    lines.append(f"- {table}" + (f": {', '.join(cols)}" if cols else ""))
                    link(me, page_path(objs.get(table, {}).get("kind", "table"), table), kind, ", ".join(cols))
        if p["writes_via_text"]:
            lines.append("\n## Writes (named in its SQL text)\n")
            for table in p["writes_via_text"]:
                lines.append(f"- {table}")
                link(me, page_path(objs.get(table, {}).get("kind", "table"), table), "writes", "named in SQL text")
        if p["calls"]:
            lines.append("\n## Calls\n")
            for c in p["calls"]:
                lines.append(f"- {c}")
                link(me, page_path("procedure", c), "calls")
        rt = p["runtime"]
        if rt:
            lines.append(f"\n## What its own log shows\n\n{rt['log_rows']:,} log rows, "
                         f"{str(rt['first_seen'])[:16]} to {str(rt['last_seen'])[:16]}.")
            if rt.get("error_steps"):
                lines.append("Error steps: " + "; ".join(rt["error_steps"][:8]))
            if rt.get("steps"):
                lines.append("\nSteps:\n" + "\n".join(f"- {s}" for s in rt["steps"][:30]))
            if rt.get("sample_call"):
                lines.append(f"\nExample call: `{str(rt['sample_call'])[:300]}`")
        pages[me] = front("procedure", name, built) + "\n".join(lines) + "\n"

    # API writers (config-DB API log).
    for name, targets in sorted(world["api_writers"].items()):
        me = page_path("api", name.removeprefix("api:"))
        for t in targets:
            link(me, page_path(objs.get(t, {}).get("kind", "table"), t), "writes", "API insert")
        pages[me] = front("api", name.removeprefix("api:"), built) + "Inserts into:\n" + "".join(f"- {t}\n" for t in targets)

    # Events. Two CCM events differ only by case (CCM_Per_Heat, CCM_PER_HEAT); GBrain slugs and the
    # Windows filesystem are case-insensitive, so the second gets a distinct name.
    for ev in world["events"]:
        name = f"{ev['area']}/{ev['event']}"
        me = page_path("event", f"{ev['area']}.{ev['event']}")
        n = 1
        while any(existing.lower() == me.lower() for existing in pages):
            n += 1
            me = page_path("event", f"{ev['area']}.{ev['event']}-{n}")
        lines = [f"Area {ev['area']}. " + ("Active." if ev["active"] else "Inactive.")]
        if ev["table"]:
            lines.append(f"Creates and updates rows in {ev['table']}.")
            link(me, page_path("table", ev["table"]), "records_to")
        for st in ev["states"]:
            lines.append(f"\n## State {st['sequence']}: {st['name']}\n\nCondition: `{st['condition']}`"
                         + (f"\nWorkflow status on: {st['on']}, off: {st['off']}." if st.get("workflow") else "")
                         + (" This is an error state." if st.get("error_state") else ""))
            maps = st.get("column_mappings") or []
            if maps:
                lines.append("Captures: " + ", ".join(f"{m['tag_attribute']} -> {m['column']}" for m in maps))
        pages[me] = front("event", name, built) + "\n".join(lines) + "\n"

    # Keys.
    for key, info in sorted(world["keys"]["keys"].items()):
        me = page_path("key", key)
        pages[me] = (front("key", key, built)
                     + f"Columns that hold the same identifier values (found by shared values), e.g. "
                     + ", ".join(f"`{v}`" for v in info["example"]) + ".\n\n"
                     + "".join(f"- {c}\n" for c in info["columns"]))

    known = set(pages)
    dangling = [l for l in links if l["to"] not in known]
    links = [l for l in links if l["to"] in known]
    return pages, links + [{"dangling": len(dangling)}]


def main() -> None:
    world = json.loads(WORLD_JSON.read_text(encoding="utf-8"))
    pages, links = build(world)
    if OUT.exists():
        shutil.rmtree(OUT)  # generated output only: a rebuild replaces it
    for rel, text in pages.items():
        path = OUT / f"{rel}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")  # LF: GBrain and WSL read these
    meta = links.pop()
    (OUT / "links.jsonl").write_text("".join(json.dumps(l) + "\n" for l in links), encoding="utf-8")
    kinds = defaultdict(int)
    for rel in pages:
        kinds[rel.split("/")[0]] += 1
    print(f"pages {len(pages)} {dict(kinds)}; links {len(links)}; dropped dangling {meta['dangling']}")


if __name__ == "__main__":
    main()
