#!/usr/bin/env python3
"""E2E thermometer for identifier resolution: real ticket text -> world keys -> live XBatch + real Jev.

    python Model_Bench/e2e/run_entity.py            # all cases
    python Model_Bench/e2e/run_entity.py arc_heat   # one case
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import world_walk  # noqa: E402


def main() -> int:
    only = set(sys.argv[1:])
    cases = [json.loads(line) for line in (HERE / "entity_cases.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    cases = [c for c in cases if not only or c["id"] in only]
    conn = world_walk._plain_sql_connection()
    passed = 0
    for case in cases:
        start = time.perf_counter()
        try:
            found = world_walk.subject(case["text"], world_walk.resolve(case["text"], conn))
            got = found[0]["value"] if found else None
            where = found[0]["key"] if found else ""
        except Exception as exc:  # the thermometer reports, never crashes
            got, where = None, f"error {type(exc).__name__}: {exc}"
        want = case["expect"].get("value")
        ok = got == want
        passed += ok
        print(f"{'PASS' if ok else 'FAIL'} {case['id']:18} {(time.perf_counter() - start) * 1000:6.0f} ms  "
              f"got {got} {where}  (want {want})")
    print(f"\n{passed}/{len(cases)} passed")
    return 0 if passed == len(cases) else 1


if __name__ == "__main__":
    raise SystemExit(main())
