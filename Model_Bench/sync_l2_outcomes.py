#!/usr/bin/env python3
"""Materialize reviewer/publisher outcomes into the L2 learning vault.

This is an idempotent, read-only-to-SQL learning sidecar. It does not participate
in claim/review/publish correctness and must never block the deterministic ticket
lifecycle.

Raw sessions tell us what the model said. Reviewer state tells us whether the
frozen proposal was accepted or rejected. Publisher postconditions tell us
whether an accepted proposal actually reached the Helpdesk state the harness
expected. Later terminal-status drift can flag a possible reopened/regressed
resolution. Those are stronger learning signals than self-authored model prose,
but they remain historical cases rather than universal facts.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from l2_pipeline_runtime import (
    REVIEWER_PROFILES,
    _query_published_state,
    body_field,
    default_args,
    list_tasks,
    reviewer_block_reason,
    task_proposal,
    task_review_cycle,
    task_run_id,
    task_ticket_id,
)

DEFAULT_VAULT = Path.home() / ".hermes" / "l2-learning"
MANIFEST_NAME = "outcomes_manifest.json"
REOPEN_RECHECK_HOURS = max(1, int(os.environ.get("L2_OUTCOME_RECHECK_HOURS", "24")))
MAX_FIELD_CHARS = max(1000, int(os.environ.get("L2_OUTCOME_MAX_FIELD_CHARS", "12000")))

_SECRET_PATTERNS = (
    re.compile(r"(--password\s+)(\S+|'[^']*'|\"[^\"]*\")", re.IGNORECASE),
    re.compile(r"(--pwd\s+)(\S+|'[^']*'|\"[^\"]*\")", re.IGNORECASE),
    re.compile(r"(PWD\s*=\s*)([^;'\"\s]+)", re.IGNORECASE),
    re.compile(r"(password\s*[:=]\s*)('[^']*'|\"[^\"]*\"|\S+)", re.IGNORECASE),
    re.compile(r"(MSSQL_MCP_PASSWORD\s*[:=]\s*)(\S+)", re.IGNORECASE),
    re.compile(r"(API_SERVER_KEY\s*[:=]\s*)(\S+)", re.IGNORECASE),
    re.compile(r"\b(sk-[A-Za-z0-9]{10,}|pk-lf-[A-Za-z0-9_-]{10,}|sk-lf-[A-Za-z0-9_-]{10,})\b"),
    re.compile(r"\b(eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,})\b"),
)


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


def _vault(value: str | None = None) -> Path:
    if value:
        return Path(value).expanduser()
    raw = os.environ.get("CHITRAGUPTA_L2_LEARNING_VAULT", "").strip()
    return Path(raw).expanduser() if raw else DEFAULT_VAULT


def _redact(value: Any) -> str:
    if value is None:
        text = ""
    elif isinstance(value, str):
        text = value
    else:
        text = json.dumps(value, ensure_ascii=False, default=str)
    for pattern in _SECRET_PATTERNS:
        if pattern.groups >= 2:
            text = pattern.sub(lambda m: m.group(1) + "[REDACTED]", text)
        else:
            text = pattern.sub("[REDACTED]", text)
    if len(text) > MAX_FIELD_CHARS:
        text = text[:MAX_FIELD_CHARS] + f"\n[TRUNCATED: original {len(text)} chars]"
    return text


def _canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, default=str)


def _digest(value: Any, length: int = 16) -> str:
    return hashlib.sha256(_canonical(value).encode("utf-8")).hexdigest()[:length]


def _safe_id(value: str) -> str:
    clean = re.sub(r"[^A-Za-z0-9_.-]+", "-", value).strip("-").lower()
    return clean[:100] or "unknown"


def _ensure_layout(vault: Path) -> None:
    for rel in ("cases/approved", "cases/rejected", "cases/reopened", "actions/plans"):
        (vault / rel).mkdir(parents=True, exist_ok=True)


def _manifest_path(vault: Path) -> Path:
    return vault / MANIFEST_NAME


def _load_manifest(vault: Path) -> dict[str, Any]:
    path = _manifest_path(vault)
    if not path.exists():
        return {"schema_version": 1, "review_tasks": {}}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {"schema_version": 1, "review_tasks": {}}
    if not isinstance(data, dict):
        return {"schema_version": 1, "review_tasks": {}}
    if not isinstance(data.get("review_tasks"), dict):
        data["review_tasks"] = {}
    data["schema_version"] = 1
    return data


def _save_manifest(vault: Path, data: dict[str, Any]) -> None:
    path = _manifest_path(vault)
    tmp = path.with_suffix(".tmp")
    data["schema_version"] = 1
    data["updated_at"] = _utc_now().isoformat()
    tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    tmp.replace(path)


def _frontmatter(meta: dict[str, Any]) -> str:
    return "\n".join(f"{key}: {json.dumps(value, ensure_ascii=False, default=str)}" for key, value in meta.items())


def _proposal_sections(proposal: dict[str, Any] | None) -> str:
    if not proposal:
        return "_No frozen proposal available._\n"
    labels = (
        ("problem_summary", "Problem summary"),
        ("findings", "Findings"),
        ("root_cause", "Root cause"),
        ("resolution", "Resolution / proposed action"),
        ("reply_text", "Proposed user reply"),
    )
    parts: list[str] = []
    for key, label in labels:
        value = _redact(proposal.get(key))
        if value:
            parts.append(f"## {label}\n\n{value}\n")
    if not parts:
        parts.append("## Frozen proposal\n\n" + _redact(proposal) + "\n")
    return "\n".join(parts)


def _write_case(
    vault: Path,
    *,
    bucket: str,
    trust: str,
    outcome: str,
    reviewer_task: dict[str, Any],
    proposal: dict[str, Any] | None,
    detail: str,
    published_state: dict[str, Any] | None = None,
) -> tuple[Path, str]:
    reviewer_task_id = str(reviewer_task.get("id") or "")
    run_id = task_run_id(reviewer_task) or ""
    ticket_id = task_ticket_id(reviewer_task) or ""
    ticket_no = body_field(reviewer_task.get("body"), "ticket_no") or ticket_id
    investigation_task_id = body_field(reviewer_task.get("body"), "investigation_task_id") or ""
    cycle = task_review_cycle(reviewer_task)
    proposal_hash = _digest(proposal or {}, 24)
    identity = {
        "bucket": bucket,
        "reviewer_task_id": reviewer_task_id,
        "run_id": run_id,
        "review_cycle": cycle,
        "proposal_hash": proposal_hash,
        "outcome": outcome,
        "detail": detail,
        "published_ticket_status": (published_state or {}).get("TicketStatus"),
    }
    case_id = _digest(identity, 24)
    path = vault / "cases" / bucket / f"{_safe_id(ticket_no or run_id)}-{case_id}.md"
    response_type = str((proposal or {}).get("response_type") or "")
    meta = {
        "kind": "l2_historical_case",
        "case_id": case_id,
        "trust": trust,
        "outcome": outcome,
        "recorded_at": _utc_now().isoformat(),
        "reviewer_task_id": reviewer_task_id,
        "investigation_task_id": investigation_task_id,
        "run_id": run_id,
        "ticket_id": ticket_id,
        "ticket_no": ticket_no,
        "review_cycle": cycle,
        "response_type": response_type,
        "proposal_hash": proposal_hash,
    }
    if published_state:
        meta.update({
            "published_process_status": published_state.get("ProcessStatus"),
            "published_ticket_status": published_state.get("TicketStatus"),
            "published_ask_status": published_state.get("AskStatus"),
        })
    warning = {
        "approved": "This historical proposal passed independent review and deterministic publisher postconditions at the recorded time. It is evidence about that historical case, not proof that a future ticket has the same root cause or that the same fix is still valid.",
        "rejected": "This is a reviewer-rejected historical proposal. It is a negative/counterexample signal, not proof that every individual statement in the proposal is false.",
        "reopened": "This case was previously published as a resolution and later left the recorded terminal ticket status. Treat it as a regression/reopen signal requiring causal investigation.",
    }.get(bucket, "Historical outcome only; verify applicability and current state live.")
    body = (
        "---\n" + _frontmatter(meta) + "\n---\n\n"
        f"# Historical L2 case — {outcome}\n\n"
        + _proposal_sections(proposal)
        + "\n## Outcome evidence\n\n" + _redact(detail) + "\n\n"
        + f"> {warning}\n"
    )
    if published_state:
        body += "\n## Publisher postcondition snapshot\n\n```json\n" + _redact(published_state) + "\n```\n"
    if not path.exists():
        path.write_text(body, encoding="utf-8")
    return path, case_id


def _parse_time(value: Any) -> datetime | None:
    if not value:
        return None
    try:
        dt = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except Exception:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _published_ok(row: dict[str, Any]) -> bool:
    return bool(
        row.get("ProcessStatus") in ("COMPLETED", "WAITING_USER")
        and str(row.get("ReplyText") or "").strip()
        and row.get("ResponseType")
    )


def sync_outcomes(*, vault: Path | None = None, args: Any = None, dry_run: bool = False,
                  tasks: list[dict[str, Any]] | None = None) -> dict[str, int]:
    """Synchronize immutable review outcomes and bounded reopen signals."""
    vault = vault or _vault()
    _ensure_layout(vault)
    manifest = _load_manifest(vault)
    entries: dict[str, Any] = manifest.setdefault("review_tasks", {})
    args = args or default_args()
    tasks = tasks if tasks is not None else list_tasks()
    counts = {"approved_recorded": 0, "rejected_recorded": 0, "reopened_recorded": 0, "skipped": 0, "errors": 0}
    reviewer_tasks = [t for t in tasks if (t.get("assignee") or "") in REVIEWER_PROFILES and t.get("status") in {"done", "blocked"}]

    for task in reviewer_tasks:
        task_id = str(task.get("id") or "")
        run_id = task_run_id(task)
        if not task_id or not run_id:
            counts["skipped"] += 1
            continue
        proposal = task_proposal(task)

        if task.get("status") == "blocked":
            reason = reviewer_block_reason(task)
            fingerprint = _digest({"status": "blocked", "proposal": proposal, "reason": reason, "cycle": task_review_cycle(task)}, 32)
            existing = entries.get(task_id) if isinstance(entries.get(task_id), dict) else {}
            if existing.get("fingerprint") == fingerprint:
                counts["skipped"] += 1
                continue
            if dry_run:
                counts["rejected_recorded"] += 1
                continue
            try:
                path, case_id = _write_case(vault, bucket="rejected", trust="reviewed_negative_example",
                                            outcome="reviewer_rejected", reviewer_task=task, proposal=proposal,
                                            detail=reason)
                entries[task_id] = {"kind": "rejected", "case_id": case_id, "path": str(path),
                                    "fingerprint": fingerprint, "recorded_at": _utc_now().isoformat(), "run_id": run_id}
                counts["rejected_recorded"] += 1
            except Exception:
                counts["errors"] += 1
            continue

        try:
            rows = _query_published_state(args, run_id)
        except Exception:
            counts["errors"] += 1
            continue
        if not rows or not _published_ok(rows[0]):
            counts["skipped"] += 1
            continue
        row = rows[0]
        # Deliberately exclude mutable TicketStatus/AskStatus from this fingerprint.
        # A later reopen must not masquerade as a newly approved case.
        fingerprint = _digest({
            "status": "done",
            "proposal": proposal,
            "process_status": row.get("ProcessStatus"),
            "response_type": row.get("ResponseType"),
            "reply_text": row.get("ReplyText"),
        }, 32)
        existing = entries.get(task_id) if isinstance(entries.get(task_id), dict) else {}
        if existing.get("fingerprint") != fingerprint:
            if dry_run:
                counts["approved_recorded"] += 1
            else:
                try:
                    detail = (
                        "Independent reviewer completed successfully and deterministic publisher postconditions were observed: "
                        f"ProcessStatus={row.get('ProcessStatus')!r}, TicketStatus={row.get('TicketStatus')!r}, ResponseType={row.get('ResponseType')!r}."
                    )
                    path, case_id = _write_case(vault, bucket="approved", trust="reviewed_published_historical_case",
                                                outcome="reviewer_approved_and_published", reviewer_task=task,
                                                proposal=proposal, detail=detail, published_state=row)
                    entries[task_id] = {
                        "kind": "approved", "case_id": case_id, "path": str(path), "fingerprint": fingerprint,
                        "recorded_at": _utc_now().isoformat(), "last_checked_at": _utc_now().isoformat(),
                        "run_id": run_id, "ticket_id": task_ticket_id(task) or "",
                        "response_type": str((proposal or {}).get("response_type") or row.get("ResponseType") or ""),
                        "published_ticket_status": row.get("TicketStatus"), "reopened": False,
                    }
                    counts["approved_recorded"] += 1
                    existing = entries[task_id]
                except Exception:
                    counts["errors"] += 1
                    continue
        else:
            counts["skipped"] += 1

        current = entries.get(task_id) if isinstance(entries.get(task_id), dict) else {}
        if str(current.get("response_type") or "").upper() != "RESOLUTION" or current.get("reopened"):
            continue
        last_checked = _parse_time(current.get("last_checked_at"))
        if last_checked and _utc_now() - last_checked < timedelta(hours=REOPEN_RECHECK_HOURS):
            continue
        if dry_run:
            continue
        try:
            follow_rows = _query_published_state(args, run_id)
        except Exception:
            counts["errors"] += 1
            continue
        current["last_checked_at"] = _utc_now().isoformat()
        if not follow_rows:
            continue
        follow = follow_rows[0]
        initial_status = current.get("published_ticket_status")
        now_status = follow.get("TicketStatus")
        if initial_status and now_status and now_status != initial_status:
            try:
                path, case_id = _write_case(
                    vault, bucket="reopened", trust="observed_resolution_regression",
                    outcome="terminal_status_changed_after_resolution", reviewer_task=task, proposal=proposal,
                    detail=f"Ticket status changed after a published RESOLUTION: {initial_status!r} -> {now_status!r}. This is a follow-up signal, not by itself a diagnosis of why the ticket changed state.",
                    published_state=follow,
                )
                current["reopened"] = True
                current["reopened_case_id"] = case_id
                current["reopened_path"] = str(path)
                current["reopened_at"] = _utc_now().isoformat()
                current["reopened_ticket_status"] = now_status
                counts["reopened_recorded"] += 1
            except Exception:
                counts["errors"] += 1

    if not dry_run:
        _save_manifest(vault, manifest)
    return counts


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--vault", default=None)
    parser.add_argument("--dry-run", action="store_true")
    ns = parser.parse_args(argv)
    counts = sync_outcomes(vault=_vault(ns.vault), dry_run=ns.dry_run)
    print(json.dumps({"ok": counts["errors"] == 0, "dry_run": ns.dry_run, "counts": counts, "vault": str(_vault(ns.vault))}, indent=2))
    return 1 if counts["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
