#!/usr/bin/env python3
"""Govern lifecycle-mined L2 candidates into reviewed reusable facts.

Candidates are produced by deterministic outcome/action miners and remain
``unverified_candidate`` until this separate curator promotes them. Promotion
requires explicit reviewer identity/evidence plus outcome-labelled source cases.
The 9B worker has no model-facing path into this control plane.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DEFAULT_VAULT = Path.home() / ".hermes" / "l2-learning"
ALLOWED_CASE_TRUST = {
    "reviewed_published_historical_case",
    "reviewed_negative_example",
    "observed_resolution_regression",
}


def _vault(raw: str | None) -> Path:
    if raw:
        return Path(raw).expanduser()
    env = os.environ.get("CHITRAGUPTA_L2_LEARNING_VAULT", "").strip()
    return Path(env).expanduser() if env else DEFAULT_VAULT


def _resolve_candidate(vault: Path, value: str) -> Path:
    p = Path(value)
    resolved = p if p.is_absolute() else vault / "candidates" / value
    resolved = resolved.resolve()
    root = (vault / "candidates").resolve()
    if root not in resolved.parents:
        raise ValueError("candidate must be under vault/candidates")
    if not resolved.is_file():
        raise FileNotFoundError(resolved)
    return resolved


def _parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n") or (end := text.find("\n---\n", 4)) < 0:
        return {}, text
    meta: dict[str, Any] = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, raw = line.split(":", 1)
        raw = raw.strip()
        try:
            meta[key.strip()] = json.loads(raw)
        except Exception:
            meta[key.strip()] = raw.strip("'\"")
    return meta, text[end + 5:]


def _frontmatter(meta: dict[str, Any]) -> str:
    return "\n".join(f"{k}: {json.dumps(v, ensure_ascii=False, default=str)}" for k, v in meta.items())


def _case_path(vault: Path, value: str) -> Path:
    p = Path(value)
    if not p.is_absolute():
        p = vault / value
    resolved = p.resolve()
    cases = (vault / "cases").resolve()
    if cases not in resolved.parents:
        raise ValueError(f"source case is outside vault/cases: {value}")
    if not resolved.is_file():
        raise FileNotFoundError(resolved)
    return resolved


def _candidate_provenance(vault: Path, candidate_text: str) -> dict[str, Any]:
    meta, _ = _parse_frontmatter(candidate_text)
    if str(meta.get("trust") or "") != "unverified_candidate":
        raise ValueError("candidate trust must be unverified_candidate")
    raw_cases = meta.get("source_cases")
    if not isinstance(raw_cases, list) or not raw_cases:
        raise ValueError("candidate requires outcome-labelled source_cases before promotion")

    source_cases: list[str] = []
    source_case_ids: list[str] = []
    ticket_ids: list[str] = []
    run_ids: list[str] = []
    source_trust: list[str] = []
    for raw in raw_cases:
        path = _case_path(vault, str(raw))
        case_meta, _ = _parse_frontmatter(path.read_text(encoding="utf-8"))
        trust = str(case_meta.get("trust") or "")
        if trust not in ALLOWED_CASE_TRUST:
            raise ValueError(f"source case is not outcome-labelled/trusted: {path.name} trust={trust!r}")
        rel = str(path.relative_to(vault))
        source_cases.append(rel)
        source_trust.append(trust)
        case_id = str(case_meta.get("case_id") or "")
        ticket_id = str(case_meta.get("ticket_id") or case_meta.get("ticket_no") or "")
        run_id = str(case_meta.get("run_id") or "")
        if not case_id or not ticket_id or not run_id:
            raise ValueError(f"source case lacks complete case/ticket/run provenance: {path.name}")
        if case_id and case_id not in source_case_ids:
            source_case_ids.append(case_id)
        if ticket_id and ticket_id not in ticket_ids:
            ticket_ids.append(ticket_id)
        if run_id and run_id not in run_ids:
            run_ids.append(run_id)
    return {
        "candidate_meta": meta,
        "source_cases": source_cases,
        "source_case_ids": source_case_ids,
        "ticket_ids": ticket_ids,
        "run_ids": run_ids,
        "source_case_trust": sorted(set(source_trust)),
    }


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
    provenance = _candidate_provenance(vault, content)
    now = datetime.now(timezone.utc).isoformat()
    fact_name = candidate.name.replace("l2_learning_candidate", "")
    fact_path = vault / "facts" / fact_name
    fact_path.parent.mkdir(parents=True, exist_ok=True)

    body = (
        "# Reviewed operational lesson\n\n"
        "The original unverified candidate follows verbatim for provenance.\n\n"
        + content
    )
    content_digest = hashlib.sha256(body.encode("utf-8")).hexdigest()
    meta = {
        "kind": "l2_operational_fact",
        "trust": "reviewed_operational",
        "promoted_at": now,
        "reviewed_at": now,
        "reviewed_by": reviewed_by,
        "promotion_evidence": evidence,
        "source_candidate": candidate.name,
        "source_cases": provenance["source_cases"],
        "source_case_ids": provenance["source_case_ids"],
        "ticket_ids": provenance["ticket_ids"],
        "run_ids": provenance["run_ids"],
        "source_case_trust": provenance["source_case_trust"],
        "content_sha256": content_digest,
    }
    fact_path.write_text(
        "---\n" + _frontmatter(meta) + "\n---\n\n" + body,
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
