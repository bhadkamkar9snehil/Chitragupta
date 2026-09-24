#!/usr/bin/env python3
"""E2E thermometer for the evidence walk: realistic ticket text -> resolver -> world scan on live XBatch -> real Jev.

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
import evidence_walk  # noqa: E402


def main() -> int:
    only = set(sys.argv[1:])
    cases = [json.loads(l) for l in (HERE / "walk_cases.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    cases = [c for c in cases if not only or c["id"] in only]
    passed = 0
    for case in cases:
        start = time.perf_counter()
        try:
            got = evidence_walk.walk(case["text"])
        except Exception as exc:  # the thermometer reports, never crashes
            got = {"pick": None, "error": f"{type(exc).__name__}: {exc}"}
        want = case["expect"] or [evidence_walk.NONE]
        # The explaining table may be the symptom (hop 1) or its cause (hop 2): the chain must reach it.
        ok = got.get("pick") in want or (got.get("pick") != evidence_walk.NONE and got.get("cause") in want)
        passed += ok
        print(f"{'PASS' if ok else 'FAIL'} {case['id']:20} {time.perf_counter() - start:5.1f}s  "
              f"pick={got.get('pick')} conf={got.get('confidence')} cause={got.get('cause')} hits={len(got.get('hits', []))}  want={want}"
              + (f"  {got['error']}" if got.get("error") else ""))
        if only or not ok:
            for line in got.get("hits", []):
                print("      ", line)
    print(f"\n{passed}/{len(cases)} passed")
    return 0 if passed == len(cases) else 1


if __name__ == "__main__":
    raise SystemExit(main())
