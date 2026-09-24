#!/usr/bin/env python3
"""E2E thermometer for the world: the built world in GBrain + live XBatch, checked against WORLD_FAILURE_MODES.md.

Run in WSL (talks to gbrain serve):  python3 Model_Bench/e2e/run_world.py
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from l2_gbrain import Brain  # noqa: E402

WORLD = json.loads((HERE.parent.parent / "Knowledge" / "process_world.json").read_text(encoding="utf-8"))

# Mode 5: joins that must be found from values alone, never typed into the builder.
SAME_KEY = [
    ("CCM_Per_Heat.HeatID", "EAF_PER_HEAT.HeatID"),
    ("CCM_Per_Heat.HeatID", "XMES_CCM_Billet_Genealogy_Trn_Tbl.HeatNo"),
    ("CCM_Per_Heat.HeatID", "XMES_SAP_API_UsageDecision_Error.HeatNo"),
]
# Mode 4: different identifiers must stay in different keys.
DIFFERENT_KEY = [
    ("CCM_Per_Heat.HeatID", "XMES_CCM_Billet_Genealogy_Trn_Tbl.BilletNo"),
    ("CCM_Per_Heat.HeatID", "XBatch_Work_Order_Mst_Tbl.WorkOrderNumber"),
]


def key_of(ref: str) -> str | None:
    return next((k for k, v in WORLD["keys"]["keys"].items() if ref in v["columns"]), None)


def main() -> int:
    results = []
    for a, b in SAME_KEY:
        ka, kb = key_of(a), key_of(b)
        results.append((f"same key: {a} ~ {b}", ka is not None and ka == kb, f"{ka} / {kb}"))
    for a, b in DIFFERENT_KEY:
        ka, kb = key_of(a), key_of(b)
        results.append((f"different keys: {a} vs {b}", ka is None or kb is None or ka != kb, f"{ka} / {kb}"))
    framework = set(WORLD["keys"]["framework_columns"])
    results.append(("mode 3: framework columns excluded", {"createdby", "modifiedby", "id"} <= framework,
                    str(sorted(framework))[:120]))

    brain = Brain()
    pages = brain.all_pages()
    for check in WORLD["acceptance"]:  # mode 6: every vendor chain exists as a GBrain link
        proc, relation, target = check["check"].split(" ")[0], check["check"].split(" ")[1], check["check"].split(" ")[2]
        start = time.perf_counter()
        slug = next((p["slug"] for p in pages if p.get("type") == "procedure" and p.get("title", "").startswith(proc)), None)
        found = False
        if slug:
            out = brain.call("get_links", slug=slug)
            items = out if isinstance(out, list) else out.get("links", [])
            found = any(target.lower() in json.dumps(i).lower() and relation in json.dumps(i) for i in items)
        results.append((f"mode 6: link {proc[:40]} {relation} {target}", found,
                        f"{(time.perf_counter() - start) * 1000:.0f} ms"))
    unknown = [p for p in pages if p.get("type") not in ("table", "view", "procedure", "event", "key", "api", "screen")]
    results.append(("mode 8: every world page is in GBrain", len(pages) == sum(
        1 for _ in (HERE.parent.parent / "Knowledge" / "world").rglob("*.md")), f"{len(pages)} in GBrain"))
    results.append(("mode 10: brain holds only world pages", not unknown, f"{len(unknown)} other pages"))

    passed = 0
    for name, ok, detail in results:
        passed += ok
        print(f"{'PASS' if ok else 'FAIL'} {name}  ({detail})")
    print(f"\n{passed}/{len(results)} passed")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
