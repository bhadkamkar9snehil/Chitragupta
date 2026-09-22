#!/usr/bin/env python3
"""Curate model-proposed L2 learning candidates into reviewed operational facts.

The model may propose a candidate through the l2_lesson tool, but it cannot make
that candidate trusted. Promotion/rejection is a separate control-plane action.
This CLI is intentionally deterministic and file-based so the promotion history
is inspectable and reversible.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_VAULT = Path.home() / ".hermes" / "l2-learning"


def _vault(raw: str | None) -> Path:
    if raw:
        return Path(raw).expanduser()
    env = os.environ.get("CHITRAGUPTA_L2_LEARNING_VAULT", "").strip()
    return Path(env).expanduser() if env else DEFAULT_VAULT


def _resolve_candidate(vault: Path, value: str) -> Path:
    p = Path(value)
    if p.is_absolute():
        resolved = p
    else:
        resolved = vault / "candidates" / value
    resolved = resolved.resolve()
    root = (vault / "candidates").resolve()
    if root not in resolved.parents:
        raise ValueError("candidate must be under vault/candidates")
    if not resolved.is_file():
        raise FileNotFoundError(resolved)
    return resolved


def _frontmatter(meta: dict) -> str:
    return "\n".join(f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in meta.items())


def list_candidates(vault: Path) -> int:
    root = vault / "candidates"
    files = sorted(p for p in root.glob("*.md") if p.is_file()) if root.exists() else []
    for p in files:
        print(p.name)
    print(f"{len(files)} candidate(s)")
    return 0


def promote(vault: Path, candidate: Path, reviewed_by: str, evidence: str) -> int:
    if not reviewed_by.strip():
        raise ValueError("--reviewed-by is required")
    if not evidence.strip():
        raise ValueError("--evidence is required")
    content = candidate.read_text(encoding="utf-8")
    now = datetime.now(timezone.utc).isoformat()
    fact_name = candidate.name.replace("l2_learning_candidate", "")
    fact_path = vault / "facts" / fact_name
    fact_path.parent.mkdir(parents=True, exist_ok=True)
    meta = {
        "kind": "l2_operational_fact",
        "trust": "reviewed_operational",
        "promoted_at": now,
        "reviewed_by": reviewed_by,
        "promotion_evidence": evidence,
        "source_candidate": candidate.name,
    }
    fact_path.write_text(
        "---\n" + _frontmatter(meta) + "\n---\n\n"
        "# Reviewed operational lesson\n\n"
        "The original candidate record follows verbatim for provenance.\n\n"
        + content,
        encoding="utf-8",
    )
    archive = vault / "archive" / "candidates" / "promoted"
    archive.mkdir(parents=True, exist_ok=True)
    shutil.move(str(candidate), str(archive / candidate.name))
    print(f"promoted -> {fact_path}")
    return 0


def reject(vault: Path, candidate: Path, reviewed_by: str, reason: str) -> int:
    if not reviewed_by.strip():
        raise ValueError("--reviewed-by is required")
    if not reason.strip():
        raise ValueError("--reason is required")
    archive = vault / "archive" / "candidates" / "rejected"
    archive.mkdir(parents=True, exist_ok=True)
    out = archive / candidate.name
    content = candidate.read_text(encoding="utf-8")
    meta = {
        "kind": "l2_learning_candidate_rejection",
        "trust": "rejected",
        "rejected_at": datetime.now(timezone.utc).isoformat(),
        "reviewed_by": reviewed_by,
        "reason": reason,
        "source_candidate": candidate.name,
    }
    out.write_text("---\n" + _frontmatter(meta) + "\n---\n\n" + content, encoding="utf-8")
    candidate.unlink()
    print(f"rejected -> {out}")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault")
    sub = ap.add_subparsers(dest="command", required=True)
    sub.add_parser("list")

    p = sub.add_parser("promote")
    p.add_argument("candidate")
    p.add_argument("--reviewed-by", required=True)
    p.add_argument("--evidence", required=True)

    r = sub.add_parser("reject")
    r.add_argument("candidate")
    r.add_argument("--reviewed-by", required=True)
    r.add_argument("--reason", required=True)

    args = ap.parse_args(argv)
    vault = _vault(args.vault)
    if args.command == "list":
        return list_candidates(vault)
    candidate = _resolve_candidate(vault, args.candidate)
    if args.command == "promote":
        return promote(vault, candidate, args.reviewed_by, args.evidence)
    return reject(vault, candidate, args.reviewed_by, args.reason)


if __name__ == "__main__":
    raise SystemExit(main())
