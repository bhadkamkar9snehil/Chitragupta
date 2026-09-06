#!/usr/bin/env python3
"""Build deterministic zvec retrieval-evaluation cases from real L2 history.

The static branch smoke set proves policy text remains retrievable. This builder
creates a second, runtime-derived set that asks a more useful question:

    Given the *earliest recorded user/task context* from an actual L2 run, can
    retrieval find the historical reviewer/publisher outcome for that same run?

No LLM judge is used. The generated JSONL points at an exact historical case
filename and the existing benchmark checks whether zvec returns that file in its
bounded result set.

Runtime data stays under the learning vault and is never committed to Git.
"""
from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from typing import Any

DEFAULT_VAULT = Path.home() / ".hermes" / "l2-learning"
DEFAULT_OUTPUT = Path("eval") / "historical_retrieval_cases.jsonl"
MAX_QUERY_CHARS = 900
MIN_QUERY_CHARS = 24

_SCOPE_FOR_BUCKET = {
    "approved": "approved_cases",
    "rejected": "rejected_cases",
    "reopened": "reopened_cases",
}


def _vault(value: str | None = None) -> Path:
    if value:
        return Path(value).expanduser()
    raw = os.environ.get("CHITRAGUPTA_L2_LEARNING_VAULT", "").strip()
    return Path(raw).expanduser() if raw else DEFAULT_VAULT


def _frontmatter(text: str) -> dict[str, Any]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    out: dict[str, Any] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line:
            continue
        key, raw = line.split(":", 1)
        key, raw = key.strip(), raw.strip()
        if not key:
            continue
        try:
            out[key] = json.loads(raw)
        except Exception:
            out[key] = raw.strip("'\"")
    return out


def _section(text: str, heading: str) -> str:
    match = re.search(rf"(?ms)^#\s+{re.escape(heading)}\s*\n+(.*?)(?=^#\s+|\Z)", text)
    return match.group(1).strip() if match else ""


def _clean_query(text: str) -> str:
    # Session user text can contain the full Kanban card. Keep its useful lexical
    # evidence while removing giant whitespace runs and inline data-image residue.
    value = re.sub(r"data:image/[^;]+;base64,[A-Za-z0-9+/=\\]+", " [image] ", text, flags=re.I)
    value = " ".join(value.split())
    return value[:MAX_QUERY_CHARS].strip()


def _session_queries(vault: Path) -> dict[str, list[tuple[str, Path]]]:
    by_run: dict[str, list[tuple[str, Path]]] = {}
    for path in sorted((vault / "sessions").rglob("*.md")):
        try:
            text = path.read_text(encoding="utf-8")
            meta = _frontmatter(text)
            run_id = str(meta.get("run_id") or "").strip()
            if not run_id:
                continue
            query = _clean_query(_section(text, "User"))
            if len(query) < MIN_QUERY_CHARS:
                continue
            by_run.setdefault(run_id, []).append((query, path))
        except Exception:
            continue
    return by_run


def build_cases(vault: Path, *, max_cases: int = 500) -> list[dict[str, Any]]:
    queries = _session_queries(vault)
    cases: list[dict[str, Any]] = []
    seen_case_ids: set[str] = set()

    for bucket, scope in _SCOPE_FOR_BUCKET.items():
        for path in sorted((vault / "cases" / bucket).glob("*.md")):
            if len(cases) >= max_cases:
                return cases
            try:
                meta = _frontmatter(path.read_text(encoding="utf-8"))
            except Exception:
                continue
            run_id = str(meta.get("run_id") or "").strip()
            case_id = str(meta.get("case_id") or path.stem).strip()
            if not run_id or case_id in seen_case_ids or run_id not in queries:
                continue

            # Earliest lexical file order is a stable proxy for the first recorded
            # turn. We deliberately do not use the outcome text itself as the query.
            query, session_path = sorted(queries[run_id], key=lambda item: str(item[1]))[0]
            cases.append({
                "id": f"history-{bucket}-{case_id}",
                "query": query,
                "scope": scope,
                "expected_any": [path.name],
                "metadata": {
                    "run_id": run_id,
                    "ticket_id": str(meta.get("ticket_id") or ""),
                    "outcome": str(meta.get("outcome") or bucket),
                    "source_session": str(session_path.relative_to(vault)),
                    "expected_case": str(path.relative_to(vault)),
                },
            })
            seen_case_ids.add(case_id)
    return cases


def write_cases(vault: Path, output: Path, cases: list[dict[str, Any]]) -> Path:
    path = output if output.is_absolute() else vault / output
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(case, ensure_ascii=False) + "\n" for case in cases), encoding="utf-8")
    return path


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", default=None)
    ap.add_argument("--output", default=str(DEFAULT_OUTPUT))
    ap.add_argument("--max-cases", type=int, default=500)
    ap.add_argument("--require-cases", action="store_true")
    ns = ap.parse_args(argv)
    vault = _vault(ns.vault)
    cases = build_cases(vault, max_cases=max(1, ns.max_cases))
    path = write_cases(vault, Path(ns.output), cases)
    print(json.dumps({
        "ok": bool(cases) or not ns.require_cases,
        "cases": len(cases),
        "output": str(path),
        "note": "0 cases is valid until correlated sessions and outcome cases exist" if not cases else "real historical retrieval cases generated",
    }, indent=2))
    return 1 if ns.require_cases and not cases else 0


if __name__ == "__main__":
    raise SystemExit(main())
