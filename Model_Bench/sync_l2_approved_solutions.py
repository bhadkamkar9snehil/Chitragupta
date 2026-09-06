#!/usr/bin/env python3
"""Export explicitly approved SQL Solution articles into trusted zvec scope.

`solutions/approved/` has one owner: this exporter. Git-authored knowledge lives
elsewhere. Trust requires an explicit SolutionID + semantic content hash in the
Git-tracked policy. Drift is checked when synchronization runs.

The exporter is read-only to SQL and does not mutate Helpdesk/KB tables.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
from pathlib import Path
from typing import Any

from l2_pipeline_runtime import default_args, run_orchestrator

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_VAULT = Path.home() / ".hermes" / "l2-learning"
DEFAULT_POLICY = ROOT / "deploy" / "solution_export_policy.json"

HASH_FIELDS = (
    "ID", "Title", "ProblemSummary", "RootCause", "ResolutionSteps",
    "RootCauseCategoryID", "Route", "RelatedViewsJson", "Tags",
)
APPROVAL_FIELDS = ("approved_by", "approved_at", "review_evidence")


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


def content_sha256(row: dict[str, Any]) -> str:
    governed = {field: row.get(field) for field in HASH_FIELDS}
    payload = json.dumps(
        governed,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        default=str,
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _solution_id_errors(item: dict[str, Any], label: str, seen: set[str]) -> list[str]:
    solution_id = str(item.get("solution_id") or "").strip()
    if not solution_id:
        return [f"{label}.solution_id is required"]
    if solution_id in seen:
        return [f"duplicate solution_id: {solution_id}"]
    seen.add(solution_id)
    return []


def _approval_errors(item: Any, index: int, seen: set[str]) -> list[str]:
    label = f"approved[{index}]"
    if not isinstance(item, dict):
        return [f"{label} must be an object"]
    errors = _solution_id_errors(item, label, seen)
    digest = str(item.get("content_sha256") or "").strip().lower()
    if not re.fullmatch(r"[0-9a-f]{64}", digest):
        errors.append(f"{label}.content_sha256 must be 64 lowercase hex characters")
    missing = [
        f"{label}.{field} is required"
        for field in APPROVAL_FIELDS
        if not str(item.get(field) or "").strip()
    ]
    return errors + missing


def _validate_policy(policy: dict[str, Any]) -> list[str]:
    errors = [] if policy.get("schema_version") == 1 else [
        "solution export policy schema_version must be 1"
    ]
    approved = policy.get("approved")
    if not isinstance(approved, list):
        return errors + ["solution export policy approved must be an array"]

    seen: set[str] = set()
    for index, item in enumerate(approved):
        errors.extend(_approval_errors(item, index, seen))
    return errors


def _query_live_solutions(args: Any = None) -> list[dict[str, Any]]:
    args = args or default_args()
    sql = (
        "SELECT ID, Title, ProblemSummary, RootCause, ResolutionSteps, "
        "RootCauseCategoryID, Route, RelatedViewsJson, Tags "
        "FROM dbo.Hermes_Solution_Article_Mst_Tbl "
        "WHERE IsActive = 1 AND IsDeleted = 0 ORDER BY ID;"
    )
    result = run_orchestrator(args, ["--query", sql], timeout=60)
    if result is None:
        return []
    if not isinstance(result, list):
        raise RuntimeError("Solution query returned a non-list payload")
    return [row for row in result if isinstance(row, dict)]


def _safe_id(value: str) -> str:
    clean = re.sub(r"[^A-Za-z0-9_.-]+", "-", value).strip("-").lower()
    return clean[:120] or hashlib.sha256(value.encode("utf-8")).hexdigest()[:16]


def _display(value: Any, default: str = "_Not recorded._") -> str:
    if value in (None, ""):
        return default
    if isinstance(value, str):
        return value
    return json.dumps(value, ensure_ascii=False, default=str)


def _render_solution(row: dict[str, Any], approval: dict[str, Any]) -> str:
    meta = {
        "kind": "l2_governed_solution_export",
        "trust": "governed_reusable_solution",
        "solution_id": str(row.get("ID") or ""),
        "content_sha256": content_sha256(row),
        "approved_by": approval.get("approved_by"),
        "approved_at": approval.get("approved_at"),
        "review_evidence": approval.get("review_evidence"),
        "route": row.get("Route"),
        "tags": row.get("Tags"),
    }
    frontmatter = "\n".join(
        f"{key}: {json.dumps(value, ensure_ascii=False, default=str)}"
        for key, value in meta.items()
    )
    return (
        f"---\n{frontmatter}\n---\n\n"
        f"# {_display(row.get('Title'), 'Approved Solution')}\n\n"
        f"## Problem summary\n\n{_display(row.get('ProblemSummary'))}\n\n"
        f"## Root cause\n\n{_display(row.get('RootCause'))}\n\n"
        f"## Resolution steps\n\n{_display(row.get('ResolutionSteps'))}\n\n"
        f"## Related views / objects\n\n{_display(row.get('RelatedViewsJson'))}\n\n"
        "> Governed reusable guidance is not current-ticket proof. "
        "Verify applicability and live state before using it.\n"
    )


def _approved_map(policy: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        str(item["solution_id"]): item
        for item in policy.get("approved", [])
        if isinstance(item, dict) and item.get("solution_id")
    }


def _live_map(rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {
        str(row["ID"]): row
        for row in rows
        if isinstance(row, dict) and row.get("ID")
    }


def _export_one(solution_id: str, approval: dict[str, Any],
                live: dict[str, dict[str, Any]]) -> tuple[str | None, str | None]:
    row = live.get(solution_id)
    if row is None:
        return None, f"approved Solution {solution_id} is missing/inactive in live SQL"
    actual = content_sha256(row)
    expected = str(approval.get("content_sha256") or "").lower()
    if actual != expected:
        return None, (
            f"approved Solution {solution_id} content drift: "
            f"expected {expected}, live {actual}"
        )
    return _render_solution(row, approval), None


def _desired_exports(policy: dict[str, Any],
                     rows: list[dict[str, Any]]) -> tuple[dict[str, str], list[str]]:
    desired: dict[str, str] = {}
    errors: list[str] = []
    live = _live_map(rows)
    for solution_id, approval in _approved_map(policy).items():
        text, error = _export_one(solution_id, approval, live)
        if error:
            errors.append(error)
            continue
        filename = f"{_safe_id(solution_id)}.md"
        if filename in desired:
            errors.append(f"Solution export filename collision: {filename}")
            continue
        desired[filename] = text or ""
    return desired, errors


def _directory_diff(directory: Path, desired: dict[str, str]) -> tuple[dict[str, Path], set[str], list[str], int]:
    existing = {path.name: path for path in directory.glob("*.md")} if directory.exists() else {}
    remove = set(existing) - set(desired)
    write = [
        name for name, text in desired.items()
        if name not in existing or existing[name].read_text(encoding="utf-8") != text
    ]
    unchanged = len(desired) - len(write)
    return existing, remove, write, unchanged


def _apply_directory(directory: Path, desired: dict[str, str],
                     existing: dict[str, Path], remove: set[str],
                     write: list[str]) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    for name in remove:
        existing[name].unlink()
    for name in write:
        path = directory / name
        tmp = path.with_suffix(".tmp")
        tmp.write_text(desired[name], encoding="utf-8")
        tmp.replace(path)


def _reconcile_directory(directory: Path, desired: dict[str, str], *,
                         dry_run: bool) -> tuple[int, int, int]:
    existing, remove, write, unchanged = _directory_diff(directory, desired)
    if not dry_run:
        _apply_directory(directory, desired, existing, remove, write)
    return len(write), len(remove), unchanged


def sync_approved_solutions(*, vault: Path | None = None,
                            policy_path: Path = DEFAULT_POLICY,
                            rows: list[dict[str, Any]] | None = None,
                            args: Any = None,
                            dry_run: bool = False) -> dict[str, Any]:
    vault = vault or _vault()
    policy = _load_json(policy_path)
    policy_errors = _validate_policy(policy)
    if policy_errors:
        return {
            "ok": False,
            "errors": policy_errors,
            "written": 0,
            "removed": 0,
            "unchanged": 0,
        }

    approvals = policy.get("approved") or []
    live_rows = rows if rows is not None else (_query_live_solutions(args) if approvals else [])
    desired, errors = _desired_exports(policy, live_rows)
    written, removed, unchanged = _reconcile_directory(
        vault / "solutions" / "approved",
        desired,
        dry_run=dry_run,
    )
    return {
        "ok": not errors,
        "errors": errors,
        "approved_count": len(approvals),
        "written": written,
        "removed": removed,
        "unchanged": unchanged,
    }


def preview_live(*, args: Any = None) -> list[dict[str, Any]]:
    return [{
        "solution_id": row.get("ID"),
        "title": row.get("Title"),
        "route": row.get("Route"),
        "content_sha256": content_sha256(row),
    } for row in _query_live_solutions(args)]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", default=None)
    ap.add_argument("--policy", default=str(DEFAULT_POLICY))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument(
        "--preview-live",
        action="store_true",
        help="print active Solution IDs and semantic review hashes without trusting/exporting them",
    )
    ns = ap.parse_args(argv)
    if ns.preview_live:
        print(json.dumps({"solutions": preview_live()}, indent=2, ensure_ascii=False))
        return 0

    result = sync_approved_solutions(
        vault=_vault(ns.vault),
        policy_path=Path(ns.policy),
        dry_run=ns.dry_run,
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
