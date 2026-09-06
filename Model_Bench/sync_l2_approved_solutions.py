#!/usr/bin/env python3
"""Export explicitly governed SQL Solution articles into trusted zvec scope.

`Hermes_Solution_Article_Mst_Tbl.IsActive` is not enough to make an article
trusted. The Git-tracked policy must explicitly approve a SolutionID and the
exact content hash reviewed by an operator. Live content drift therefore fails
closed rather than silently changing trusted retrieval material.

This sidecar is read-only to SQL. It writes only the derived local learning-vault
mirror under solutions/approved and archives previously managed exports when
approval is removed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from l2_pipeline_runtime import default_args, run_orchestrator

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_VAULT = Path.home() / ".hermes" / "l2-learning"
DEFAULT_POLICY = ROOT / "deploy" / "solution_export_policy.json"
MANIFEST = "solutions/solution_export_manifest.json"

FIELDS = (
    "ID", "Title", "ProblemSummary", "RootCause", "ResolutionSteps",
    "RootCauseCategoryID", "Route", "RelatedViewsJson", "Tags", "UsageCount",
)


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _vault(raw: str | None = None) -> Path:
    if raw:
        return Path(raw).expanduser()
    env = os.environ.get("CHITRAGUPTA_L2_LEARNING_VAULT", "").strip()
    return Path(env).expanduser() if env else DEFAULT_VAULT


def _load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def _canonical_row(row: dict[str, Any]) -> dict[str, Any]:
    return {field: row.get(field) for field in FIELDS}


def content_sha256(row: dict[str, Any]) -> str:
    payload = json.dumps(_canonical_row(row), sort_keys=True, separators=(",", ":"),
                         ensure_ascii=False, default=str)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _policy_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _validate_policy(policy: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if policy.get("schema_version") != 1:
        errors.append("solution export policy schema_version must be 1")
    approved = policy.get("approved")
    if not isinstance(approved, list):
        return errors + ["solution export policy approved must be an array"]
    seen: set[str] = set()
    for i, item in enumerate(approved):
        label = f"approved[{i}]"
        if not isinstance(item, dict):
            errors.append(f"{label} must be an object"); continue
        sid = str(item.get("solution_id") or "").strip()
        digest = str(item.get("content_sha256") or "").strip().lower()
        if not sid: errors.append(f"{label}.solution_id is required")
        elif sid in seen: errors.append(f"duplicate solution_id: {sid}")
        seen.add(sid)
        if not re.fullmatch(r"[0-9a-f]{64}", digest):
            errors.append(f"{label}.content_sha256 must be 64 lowercase hex characters")
        for field in ("approved_by", "approved_at", "review_evidence"):
            if not str(item.get(field) or "").strip():
                errors.append(f"{label}.{field} is required")
    return errors


def _query_live_solutions(args: Any = None) -> list[dict[str, Any]]:
    args = args or default_args()
    sql = (
        "SELECT ID, Title, ProblemSummary, RootCause, ResolutionSteps, "
        "RootCauseCategoryID, Route, RelatedViewsJson, Tags, UsageCount "
        "FROM dbo.Hermes_Solution_Article_Mst_Tbl "
        "WHERE IsActive = 1 AND IsDeleted = 0 ORDER BY ID;"
    )
    result = run_orchestrator(args, ["--query", sql], timeout=60)
    if result is None:
        return []
    if not isinstance(result, list):
        raise RuntimeError("Solution query returned a non-list payload")
    return [x for x in result if isinstance(x, dict)]


def _safe_id(value: str) -> str:
    clean = re.sub(r"[^A-Za-z0-9_.-]+", "-", value).strip("-").lower()
    return clean[:120] or hashlib.sha256(value.encode()).hexdigest()[:16]


def _render_solution(row: dict[str, Any], approval: dict[str, Any]) -> str:
    digest = content_sha256(row)
    meta = {
        "kind": "l2_governed_solution_export",
        "trust": "governed_reusable_solution",
        "solution_id": str(row.get("ID") or ""),
        "content_sha256": digest,
        "approved_by": approval.get("approved_by"),
        "approved_at": approval.get("approved_at"),
        "review_evidence": approval.get("review_evidence"),
        "route": row.get("Route"),
        "tags": row.get("Tags"),
        "usage_count_snapshot": row.get("UsageCount"),
        "exported_at": _now(),
    }
    fm = "\n".join(f"{k}: {json.dumps(v, ensure_ascii=False, default=str)}" for k, v in meta.items())
    related = row.get("RelatedViewsJson")
    related_text = related if isinstance(related, str) else json.dumps(related, ensure_ascii=False, default=str)
    return (
        f"---\n{fm}\n---\n\n"
        f"# {row.get('Title') or 'Approved Solution'}\n\n"
        f"## Problem summary\n\n{row.get('ProblemSummary') or '_Not recorded._'}\n\n"
        f"## Root cause\n\n{row.get('RootCause') or '_Not recorded._'}\n\n"
        f"## Resolution steps\n\n{row.get('ResolutionSteps') or '_Not recorded._'}\n\n"
        f"## Related views / objects\n\n{related_text or '_Not recorded._'}\n\n"
        "> This is governed reusable guidance, not current-ticket proof. Verify applicability and live state before using it.\n"
    )


def _manifest_path(vault: Path) -> Path:
    return vault / MANIFEST


def _load_manifest(vault: Path) -> dict[str, Any]:
    path = _manifest_path(vault)
    if not path.exists():
        return {"schema_version": 1, "managed_exports": {}}
    try:
        data = _load_json(path)
    except Exception:
        return {"schema_version": 1, "managed_exports": {}}
    if not isinstance(data.get("managed_exports"), dict):
        data["managed_exports"] = {}
    return data


def _save_manifest(vault: Path, data: dict[str, Any]) -> None:
    path = _manifest_path(vault)
    path.parent.mkdir(parents=True, exist_ok=True)
    data["schema_version"] = 1
    data["updated_at"] = _now()
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    tmp.replace(path)


def sync_approved_solutions(*, vault: Path | None = None, policy_path: Path = DEFAULT_POLICY,
                            rows: list[dict[str, Any]] | None = None, args: Any = None,
                            dry_run: bool = False) -> dict[str, Any]:
    vault = vault or _vault()
    policy = _load_json(policy_path)
    policy_errors = _validate_policy(policy)
    if policy_errors:
        return {"ok": False, "errors": policy_errors, "exported": 0, "archived": 0, "skipped": 0}

    approvals = {str(x["solution_id"]): x for x in policy.get("approved", [])}
    # Empty policy intentionally performs no SQL read. First introduction can be
    # safely deployed before any Solution has completed governance review.
    live_rows = rows if rows is not None else (_query_live_solutions(args) if approvals else [])
    by_id = {str(row.get("ID") or ""): row for row in live_rows if row.get("ID")}
    manifest = _load_manifest(vault)
    prior = manifest.get("managed_exports", {}) if isinstance(manifest.get("managed_exports"), dict) else {}
    next_managed: dict[str, Any] = {}
    errors: list[str] = []
    exported = archived = skipped = 0
    approved_dir = vault / "solutions" / "approved"
    archive_dir = vault / "archive" / "solutions"

    for sid, approval in approvals.items():
        row = by_id.get(sid)
        if row is None:
            errors.append(f"approved Solution {sid} is missing/inactive in live SQL")
            continue
        actual_hash = content_sha256(row)
        expected_hash = str(approval.get("content_sha256") or "").lower()
        if actual_hash != expected_hash:
            errors.append(f"approved Solution {sid} content drift: expected {expected_hash}, live {actual_hash}")
            continue
        filename = f"{_safe_id(sid)}.md"
        rel = f"solutions/approved/{filename}"
        rendered = _render_solution(row, approval)
        path = vault / rel
        next_managed[sid] = {
            "path": rel,
            "content_sha256": actual_hash,
            "approved_by": approval.get("approved_by"),
            "approved_at": approval.get("approved_at"),
        }
        if path.exists() and path.read_text(encoding="utf-8") == rendered:
            skipped += 1
            continue
        if not dry_run:
            approved_dir.mkdir(parents=True, exist_ok=True)
            path.write_text(rendered, encoding="utf-8")
        exported += 1

    # Only exports recorded in our previous manifest are eligible for archival.
    # Hand-authored files are never swept by this sidecar.
    for sid, old in prior.items():
        if sid in next_managed:
            continue
        old_rel = str((old or {}).get("path") or "")
        old_path = vault / old_rel if old_rel else None
        if old_path and old_path.is_file():
            if not dry_run:
                archive_dir.mkdir(parents=True, exist_ok=True)
                target = archive_dir / f"{_safe_id(sid)}-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}.md"
                shutil.move(str(old_path), str(target))
            archived += 1

    if not dry_run:
        manifest["managed_exports"] = next_managed
        manifest["policy_path"] = str(policy_path)
        manifest["policy_sha256"] = _policy_sha256(policy_path)
        _save_manifest(vault, manifest)
    return {
        "ok": not errors,
        "errors": errors,
        "exported": exported,
        "archived": archived,
        "skipped": skipped,
        "approved_count": len(approvals),
    }


def preview_live(*, args: Any = None) -> list[dict[str, Any]]:
    rows = _query_live_solutions(args)
    return [{
        "solution_id": row.get("ID"),
        "title": row.get("Title"),
        "route": row.get("Route"),
        "content_sha256": content_sha256(row),
    } for row in rows]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", default=None)
    ap.add_argument("--policy", default=str(DEFAULT_POLICY))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--preview-live", action="store_true",
                    help="print active live Solution IDs and review hashes without trusting/exporting them")
    ns = ap.parse_args(argv)
    if ns.preview_live:
        print(json.dumps({"solutions": preview_live()}, indent=2, ensure_ascii=False)); return 0
    result = sync_approved_solutions(vault=_vault(ns.vault), policy_path=Path(ns.policy), dry_run=ns.dry_run)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
