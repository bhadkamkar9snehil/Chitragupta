#!/usr/bin/env python3
"""E2E thermometer for entity resolution: real ticket text -> real resolver -> live XBatch + real Jev.

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
import entity_resolver  # noqa: E402


def check(expect: dict, got: dict) -> tuple[bool, str]:
    if expect.get("kind") is None:
        return got.get("kind") is None, "expected no entity"
    ok = got.get("kind") == expect["kind"] and str(got.get("value")) == expect["value"]
    if ok and "exists" in expect:
        ok = bool(got.get("exists")) == expect["exists"]
    return ok, f"expected {expect['kind']}={expect['value']}" + (f" exists={expect['exists']}" if "exists" in expect else "")


def main() -> int:
    only = set(sys.argv[1:])
    cases = [json.loads(line) for line in (HERE / "entity_cases.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    passed = 0
    for case in cases:
        if only and case["id"] not in only:
            continue
        start = time.perf_counter()
        try:
            got = entity_resolver.resolve(case["text"])
        except Exception as exc:  # the thermometer reports, never crashes
            got = {"error": f"{type(exc).__name__}: {exc}"}
        ms = (time.perf_counter() - start) * 1000
        ok, want = check(case["expect"], got)
        passed += ok
        shown = {k: got.get(k) for k in ("kind", "value", "exists", "error") if got.get(k) is not None}
        print(f"{'PASS' if ok else 'FAIL'} {case['id']:18} {ms:6.0f} ms  got {shown}  ({want})")
    total = len(cases) if not only else len(only)
    print(f"\n{passed}/{total} passed")
    return 0 if passed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
