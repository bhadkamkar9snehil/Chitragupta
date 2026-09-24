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


def score(expect: dict, got: dict) -> tuple[bool, list[str]]:
    """The whole chain must be right: the cause found, the involved records kept, the numbers traced."""
    chain = got.get("chain") or {}
    flagged = {t for tables in chain.values() for t in tables}
    notes = []
    if expect.get("none"):
        if flagged:
            notes.append(f"expected no data fault, flagged {sorted(flagged)}")
        return not notes, notes
    for table in expect.get("cause", []):
        if table not in chain.get("cause", []):
            notes.append(f"cause {table} not judged as cause")
    for table in expect.get("involved", []):
        if table not in flagged:
            notes.append(f"{table} dropped from the chain")
    for n, sources in expect.get("numbers", {}).items():
        src = ((got.get("numbers") or {}).get(n) or {}).get("source") or ""
        if not any(src.startswith(s) for s in sources):
            notes.append(f"number {n} traced to {src or 'nothing'}, want {sources}")
    return not notes, notes


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
        ok, notes = score(case["expect"], got)
        passed += ok
        print(f"{'PASS' if ok else 'FAIL'} {case['id']:20} {time.perf_counter() - start:5.1f}s  "
              f"chain={got.get('chain')} numbers={ {n: v.get('source') for n, v in (got.get('numbers') or {}).items()} }"
              + (f"  {got['error']}" if got.get("error") else "") + (f"\n       MISSED: {notes}" if notes else ""))
        if only or not ok:
            for table, r in (got.get("roles") or {}).items():
                if r["role"] != "unrelated":
                    print(f"       {r['role']:6} {r['confidence']}  {table}")
    print(f"\n{passed}/{len(cases)} passed")
    return 0 if passed == len(cases) else 1


if __name__ == "__main__":
    raise SystemExit(main())
