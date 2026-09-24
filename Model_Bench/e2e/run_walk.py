#!/usr/bin/env python3
"""E2E thermometer for the world walk: realistic ticket -> Jev steps through the GBrain world -> live XBatch.

Runs in WSL (GBrain lives there).

    python Model_Bench/e2e/run_walk.py              # all cases
    python Model_Bench/e2e/run_walk.py ud_access    # one case, prints the findings Jev saw
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import world_walk  # noqa: E402


def score(expect: dict, got: dict) -> tuple[bool, list[str]]:
    """The whole chain must be right: the cause found, the involved records kept, the numbers traced."""
    chain = {}
    for step in got.get("trail", []):
        chain.setdefault(step.get("role"), []).append(step["node"])
    chain.pop("unrelated", None)
    chain.pop("not_observed", None)
    flagged = {t for tables in chain.values() for t in tables}
    notes = []

    def covers(nodes, table: str) -> bool:
        # A view that reads the table shows the same rows (world: view -> reads -> table).
        return any(n == table or table in world_walk.OBJS.get(n, {}).get("reads", []) for n in nodes)

    if expect.get("none"):
        if flagged:
            notes.append(f"expected no data fault, flagged {sorted(flagged)}")
        return not notes, notes
    for table in expect.get("cause", []):
        if not covers(chain.get("cause", []), table):
            notes.append(f"cause {table} not judged as cause")
    for table in expect.get("involved", []):
        if not covers(flagged, table):
            notes.append(f"{table} dropped from the chain")
    for n, sources in expect.get("numbers", {}).items():
        traced = (got.get("numbers") or {}).get(n) or {}
        src = traced.get("source") or ""
        if not any(src.startswith(s) for s in sources):
            notes.append(f"number {n}: Jev chose {src or 'nothing'} of {traced.get('candidates')}, want {sources}")
    return not notes, notes


def main() -> int:
    only = set(sys.argv[1:])
    cases = [json.loads(l) for l in (HERE / "walk_cases.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    cases = [c for c in cases if not only or c["id"] in only]
    passed = 0
    world = world_walk.World()  # one gbrain serve session for all cases
    for case in cases:
        start = time.perf_counter()
        try:
            got = world_walk.walk(case["text"], world)
        except Exception as exc:  # the thermometer reports, never crashes
            got = {"trail": [], "error": f"{type(exc).__name__}: {exc}"}
        ok, notes = score(case["expect"], got)
        passed += ok
        print(f"{'PASS' if ok else 'FAIL'} {case['id']:20} {time.perf_counter() - start:5.1f}s  "
              f"steps={len(got.get('trail', []))} stopped={got.get('stopped')}"
              + (f"  {got['error']}" if got.get("error") else "") + (f"\n       MISSED: {notes}" if notes else ""))
        for i, step in enumerate(got.get("trail", []), 1):
            print(f"       {i}. [{step.get('role')} {step.get('confidence')}] {step['step'][:110]}\n"
                  f"          saw: {step['observation']['text'][:220]}")
    print(f"\n{passed}/{len(cases)} passed")
    return 0 if passed == len(cases) else 1


if __name__ == "__main__":
    raise SystemExit(main())
