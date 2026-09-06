#!/usr/bin/env python3
"""Mine outcome-labelled L2 cases into deterministic *unverified* candidates.

The miner never promotes knowledge. It converts strong lifecycle outcomes into a
review queue:

- reviewer-rejected proposals -> failure-pattern candidate;
- reopened/regressed resolutions -> failure-pattern candidate;
- the same normalized approved root cause observed on >=2 distinct tickets ->
  repeated-pattern candidate.

This is intentionally conservative and lexical. Semantic generalization belongs
in a later review/promotion step, not in an automatic background sidecar.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DEFAULT_VAULT = Path.home() / ".hermes" / "l2-learning"


def _vault(value: str | None = None) -> Path:
    if value:
        return Path(value).expanduser()
    raw = os.environ.get("CHITRAGUPTA_L2_LEARNING_VAULT", "").strip()
    return Path(raw).expanduser() if raw else DEFAULT_VAULT


def _parse_frontmatter(text: str) -> dict[str, Any]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    meta: dict[str, Any] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line:
            continue
        key, raw = line.split(":", 1)
        key = key.strip(); raw = raw.strip()
        if not key:
            continue
        try:
            meta[key] = json.loads(raw)
        except Exception:
            meta[key] = raw.strip("'\"")
    return meta


def _section(text: str, heading: str) -> str:
    pattern = re.compile(
        rf"(?ms)^##\s+{re.escape(heading)}\s*\n+(.*?)(?=^##\s+|^>\s|\Z)"
    )
    match = pattern.search(text)
    return (match.group(1).strip() if match else "")


def _digest(value: Any, length: int = 20) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, default=str)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:length]


def _normalize_root_cause(text: str) -> str:
    value = " ".join(text.lower().split())
    value = re.sub(r"\bt_[0-9a-f]{6,}\b", "<task>", value, flags=re.I)
    value = re.sub(r"\b[0-9a-f]{8}-[0-9a-f-]{20,}\b", "<id>", value, flags=re.I)
    value = re.sub(r"\b\d{4,}\b", "<n>", value)
    return value.strip()


def _write_candidate(vault: Path, *, candidate_type: str, summary: str,
                     evidence: str, source_cases: list[str], source_trust: str,
                     route: str = "") -> bool:
    identity = {
        "candidate_type": candidate_type,
        "summary": summary,
        "source_cases": sorted(source_cases),
    }
    digest = _digest(identity, 24)
    out = vault / "candidates" / f"auto-{candidate_type}-{digest}.md"
    if out.exists():
        return False
    out.parent.mkdir(parents=True, exist_ok=True)
    meta = {
        "kind": "l2_learning_candidate",
        "candidate_type": candidate_type,
        "trust": "unverified_candidate",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "created_by": "deterministic_outcome_miner",
        "source_trust": source_trust,
        "source_case_count": len(source_cases),
        "source_cases": source_cases,
        "route": route,
        "content_hash": digest,
    }
    frontmatter = "\n".join(f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in meta.items())
    body = (
        "---\n" + frontmatter + "\n---\n\n"
        "# Candidate lesson\n\n" + summary.strip() + "\n\n"
        "# Evidence / provenance\n\n" + evidence.strip() + "\n\n"
        "> Automatically mined from lifecycle outcomes. This remains untrusted until explicitly reviewed/promoted.\n"
    )
    out.write_text(body, encoding="utf-8")
    return True


def mine_candidates(vault: Path | None = None, *, dry_run: bool = False) -> dict[str, int]:
    vault = vault or _vault()
    counts = {"rejection_candidates": 0, "reopen_candidates": 0,
              "repeated_root_cause_candidates": 0, "skipped": 0, "errors": 0}

    def maybe_write(**kwargs: Any) -> bool:
        if dry_run:
            return True
        return _write_candidate(vault, **kwargs)

    # Rejected and reopened cases are high-value negative signals.
    for bucket, count_key, ctype, trust in (
        ("rejected", "rejection_candidates", "failure_pattern", "reviewed_negative_example"),
        ("reopened", "reopen_candidates", "regression_pattern", "reopen_signal"),
    ):
        for path in sorted((vault / "cases" / bucket).glob("*.md")):
            try:
                text = path.read_text(encoding="utf-8")
                meta = _parse_frontmatter(text)
                detail = _section(text, "Outcome evidence") or "See source case for outcome evidence."
                if bucket == "rejected":
                    summary = "A prior L2 proposal was independently rejected. Treat this rejection reason as a failure pattern to avoid repeating without stronger evidence:\n\n" + detail
                else:
                    summary = "A previously reviewed/published resolution later left its recorded terminal state. Treat this as a regression/reopen pattern requiring causal verification:\n\n" + detail
                created = maybe_write(
                    candidate_type=ctype,
                    summary=summary,
                    evidence=f"Source historical case: {path}\ncase_id={meta.get('case_id', '')}\nrun_id={meta.get('run_id', '')}",
                    source_cases=[str(path)],
                    source_trust=trust,
                    route=str(meta.get("route") or ""),
                )
                counts[count_key] += int(created)
                counts["skipped"] += int(not created)
            except Exception:
                counts["errors"] += 1

    # Repeated approved root cause: exact lexical normalization only. This avoids
    # inventing semantic equivalence in the background. Promotion still remains
    # a separate review step.
    groups: dict[str, list[tuple[Path, dict[str, Any], str]]] = {}
    for path in sorted((vault / "cases" / "approved").glob("*.md")):
        try:
            text = path.read_text(encoding="utf-8")
            meta = _parse_frontmatter(text)
            root = _section(text, "Root cause")
            normalized = _normalize_root_cause(root)
            if len(normalized) < 20:
                continue
            groups.setdefault(normalized, []).append((path, meta, root))
        except Exception:
            counts["errors"] += 1

    for normalized, rows in groups.items():
        distinct_tickets = {str(meta.get("ticket_id") or meta.get("ticket_no") or "") for _, meta, _ in rows}
        distinct_tickets.discard("")
        if len(distinct_tickets) < 2:
            continue
        source_cases = [str(path) for path, _, _ in rows]
        evidence = "Repeated independently reviewed/published historical cases:\n" + "\n".join(f"- {p}" for p in source_cases)
        summary = (
            "The following normalized root-cause pattern appeared in at least two distinct approved historical tickets. "
            "It is a candidate reusable diagnostic pattern, not proof for a future ticket:\n\n" + rows[0][2]
        )
        try:
            created = maybe_write(
                candidate_type="repeated_root_cause",
                summary=summary,
                evidence=evidence,
                source_cases=source_cases,
                source_trust="multiple_reviewed_published_cases",
            )
            counts["repeated_root_cause_candidates"] += int(created)
            counts["skipped"] += int(not created)
        except Exception:
            counts["errors"] += 1

    return counts


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", default=None)
    ap.add_argument("--dry-run", action="store_true")
    ns = ap.parse_args(argv)
    counts = mine_candidates(_vault(ns.vault), dry_run=ns.dry_run)
    print(json.dumps({"ok": counts["errors"] == 0, "dry_run": ns.dry_run,
                      "vault": str(_vault(ns.vault)), "counts": counts}, indent=2))
    return 1 if counts["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
