#!/usr/bin/env python3
"""Benchmark Chitragupta's explicit GBrain-backed recall against JSONL cases.

This is a deterministic retrieval smoke/evaluation harness, not an LLM judge.
Each case declares lexical evidence that should or should not appear in the
returned bounded context. Real historical-ticket cases can be added without
changing code.

JSONL fields:
  id              stable case id
  query           recall query
  scope           l2_recall scope (default trusted)
  expected_any    at least one substring must appear (case-insensitive)
  expected_all    every substring must appear
  forbidden_any   none may appear; a hit is treated as a false-positive guard

Exit nonzero when a case violates its explicit contract or aggregate hit rate is
below --min-hit-rate.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import statistics
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "Model_Bench" / "xstudio_l2_learning_plugin" / "__init__.py"
DEFAULT_CASES = ROOT / "Model_Bench" / "l2_learning_eval_cases.jsonl"

_spec = importlib.util.spec_from_file_location("l2_learning_benchmark_plugin", PLUGIN)
_mod = importlib.util.module_from_spec(_spec)
assert _spec.loader
_spec.loader.exec_module(_mod)


def _load_cases(path: Path) -> list[dict]:
    cases: list[dict] = []
    for line_no, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        try:
            case = json.loads(line)
        except Exception as exc:
            raise ValueError(f"{path}:{line_no}: invalid JSON: {exc}") from exc
        if not case.get("id") or not case.get("query"):
            raise ValueError(f"{path}:{line_no}: id and query are required")
        cases.append(case)
    if not cases:
        raise ValueError(f"no evaluation cases found in {path}")
    return cases


def _contains(text: str, needle: str) -> bool:
    return needle.casefold() in text.casefold()


def _p(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    idx = min(len(ordered) - 1, max(0, int(round((len(ordered) - 1) * q))))
    return ordered[idx]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cases", type=Path, default=DEFAULT_CASES)
    ap.add_argument("--min-hit-rate", type=float, default=0.80)
    ap.add_argument("--limit", type=int, default=5)
    args = ap.parse_args(argv)

    cases = _load_cases(args.cases)
    latencies: list[float] = []
    context_chars: list[int] = []
    passed = 0
    failures: list[str] = []

    for case in cases:
        t0 = time.perf_counter()
        payload = json.loads(_mod._recall({
            "query": case["query"],
            "scope": case.get("scope", "trusted"),
            "mode": case.get("mode", "hybrid"),
            "limit": args.limit,
        }))
        dt = time.perf_counter() - t0
        latencies.append(dt)

        if not payload.get("ok"):
            failures.append(f"{case['id']}: recall failed: {payload.get('error')}")
            print(f"FAIL {case['id']}: recall error")
            continue

        text = str(payload.get("results") or "")
        context_chars.append(len(text))
        reasons: list[str] = []
        expected_any = [str(x) for x in case.get("expected_any", [])]
        expected_all = [str(x) for x in case.get("expected_all", [])]
        forbidden_any = [str(x) for x in case.get("forbidden_any", [])]

        if expected_any and not any(_contains(text, x) for x in expected_any):
            reasons.append("none of expected_any found")
        missing_all = [x for x in expected_all if not _contains(text, x)]
        if missing_all:
            reasons.append("missing expected_all=" + repr(missing_all))
        forbidden_hits = [x for x in forbidden_any if _contains(text, x)]
        if forbidden_hits:
            reasons.append("forbidden hit=" + repr(forbidden_hits))

        if reasons:
            failures.append(f"{case['id']}: " + "; ".join(reasons))
            print(f"FAIL {case['id']}: {'; '.join(reasons)}")
        else:
            passed += 1
            print(f"PASS {case['id']}: {len(text)} chars in {dt:.3f}s")

    hit_rate = passed / len(cases)
    print()
    print(f"cases={len(cases)} passed={passed} hit_rate={hit_rate:.3f}")
    print(f"latency p50={statistics.median(latencies):.3f}s p95={_p(latencies, .95):.3f}s")
    if context_chars:
        print(f"context chars mean={statistics.mean(context_chars):.0f} max={max(context_chars)}")

    if hit_rate < args.min_hit_rate:
        failures.append(f"aggregate hit_rate {hit_rate:.3f} < minimum {args.min_hit_rate:.3f}")
    if failures:
        print("\nEvaluation failures:")
        for failure in failures:
            print(" -", failure)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
