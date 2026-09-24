#!/usr/bin/env python3
"""E2E thermometer for tickets without an identifier (L1 escalations): route, scope, evidence.

Runs in WSL (GBrain lives there).  python3 Model_Bench/e2e/run_general.py [case_id ...]
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import world_walk  # noqa: E402


def score(expect: dict, got: dict) -> list[str]:
    if not expect["data"]:
        return [] if got.get("route") == expect["route"] else [f"route {got.get('route')}, want {expect['route']}"]
    if not got.get("data"):
        return [f"routed away as {got.get('route')}, but this is a data problem"]
    kept = [s for s in got.get("trail", []) if s.get("role") not in ("unrelated", "not_observed")]
    # Reached = judged relevant itself, or named in a relevant finding (a screen/view finding names its tables).
    hit = [t for t in expect["scope_any"] if any(t == s["node"] or t in s["observation"]["text"] for s in kept)]
    notes = [] if hit else [f"scope {expect['scope_any']} not reached"]
    # The answer must contain the fact, not just touch the right table.
    said = " | ".join(s["observation"]["text"] for s in kept)
    notes += [f"never said '{m}'" for m in expect.get("must_say", []) if m not in said]
    return notes


def check_window() -> None:
    """The date parser is code, not Jev (GENERAL_FAILURE_MODES mode 4); it must not drift."""
    from datetime import date
    today = date(2026, 9, 24)
    for text, want in {"after 8th July evening": date(2026, 7, 8), "since 30th": date(2026, 8, 30),
                       "since 8th": date(2026, 9, 8), "last night": date(2026, 9, 23), "no period": None}.items():
        assert world_walk.window(text, today) == want, (text, world_walk.window(text, today), want)


def main() -> int:
    check_window()
    only = set(sys.argv[1:])
    cases = [json.loads(l) for l in (HERE / "general_cases.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    cases = [c for c in cases if not only or c["id"] in only]
    world, conn, passed = world_walk.World(), world_walk.connect(), 0
    for case in cases:
        start = time.perf_counter()
        try:
            got = world_walk.walk(case["text"], world, conn)
        except Exception as exc:  # the thermometer reports, never crashes
            got = {"trail": [], "error": f"{type(exc).__name__}: {exc}"}
        notes = score(case["expect"], got)
        passed += not notes
        print(f"{'PASS' if not notes else 'FAIL'} {case['id']:22} {time.perf_counter() - start:5.1f}s  route={got.get('route')} "
              f"since={got.get('since')} stopped={got.get('stopped')}" + (f"  {got['error']}" if got.get("error") else "")
              + (f"\n       MISSED: {notes}\n       truth: {case['expect'].get('finding')}" if notes else ""))
        for i, s in enumerate(got.get("trail", []), 1):
            print(f"       {i}. [{s.get('role')} {s.get('confidence')}] {s['observation']['text'][:200]}")
    print(f"\n{passed}/{len(cases)} passed")
    return 0 if passed == len(cases) else 1


if __name__ == "__main__":
    raise SystemExit(main())
