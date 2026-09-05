#!/usr/bin/env python3
"""Deterministic state machine for the Chitragupta L2 Helpdesk pipeline.

One inference slot means throughput comes from finishing tickets, not pre-claiming
more work. This module therefore owns all non-LLM lifecycle choreography:

    SQL claim -> investigator -> reviewer -> publish
                               -> reject -> rework -> reviewer -> ...

Every public operation is idempotent and can be triggered both from the Hermes
observer hook and from the 2-minute ticket-scout backstop.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import subprocess
import sys
from pathlib import Path
from typing import Any, Iterable, Optional

WINDOWS_PYTHON = "/mnt/c/Python314/python.exe"
ORCHESTRATOR_WIN = r"C:\Users\Admin\Documents\Office\AIHelpdesk\Hermes_Orchestrator.py"
KB_RETRIEVER_WIN = r"C:\Users\Admin\Documents\Office\AIHelpdesk\Model_Bench\kb_retrieval.py"
DEFAULT_SERVER = "10.2.6.204"
DEFAULT_DATABASE = "XStudio_Helpdesk"
DEFAULT_USER = "sa"
DEFAULT_ELIGIBLE_STATUS = "Enter"

INVESTIGATOR_PROFILE = os.environ.get("L2_INVESTIGATOR_PROFILE", "l2-investigator-primary")
REVIEWER_PROFILE = os.environ.get("L2_REVIEWER_PROFILE", "l2-reviewer-primary")
REVIEWER_PROFILES = {REVIEWER_PROFILE, "l2-reviewer-primary", "l2-reviewer-fallback"}
INVESTIGATOR_PROFILES = {INVESTIGATOR_PROFILE, "l2-investigator-primary", "l2-investigator"}

# With LM Studio unified KV cache and max_in_progress=1, closing in-flight work
# must outrank opening new work.
NEW_INVESTIGATION_PRIORITY = 10
REWORK_PRIORITY = 20
REVIEW_PRIORITY = 30
MAX_REVIEW_CYCLES = 3  # initial review (0) + at most two rework reviews (1, 2)

# `todo` is deliberately live: parent-gated reviewer cards sit there until their
# investigator completes. Omitting it was a real stale-recovery bug.
LIVE_KANBAN_STATUSES = {"todo", "ready", "blocked", "triage", "running", "review", "scheduled"}
TERMINAL_KANBAN_STATUSES = {"done", "archived"}
ARCHIVABLE_STALE_STATUSES = {"todo", "ready", "blocked", "triage", "scheduled"}

MIN_SUMMARY_CHARS = 40
ORPHAN_GRACE_MINUTES = 45

REPO_ROOT_WSL = Path("/mnt/c/Users/Admin/Documents/Office/AIHelpdesk")
BINDING_CANDIDATES = [
    Path(os.environ["L2_HELPDESK_WORKFLOW_BINDING"]) if os.environ.get("L2_HELPDESK_WORKFLOW_BINDING") else None,
    REPO_ROOT_WSL / "deploy" / "helpdesk_workflow_binding.json",
    Path(__file__).resolve().parent / "helpdesk_workflow_binding.json",
    Path(__file__).resolve().parent.parent / "deploy" / "helpdesk_workflow_binding.json",
]

_RESPONSE_TYPE_PATTERNS = [
    ("L3_ESCALATION", re.compile(r"\bl3 escalat|\bescalat\w* to l3|\bescalating\b", re.I)),
    ("RESOLUTION", re.compile(r"\bresolved\b|\bfix(?:ed)? confirmed\b|\bverified live\b.*\bfix", re.I)),
    ("QUESTION", re.compile(r"\?\s*$|need(?:s)? (?:more info|clarification) from|requester\b.*\bconfirm", re.I)),
]


def _is_windows() -> bool:
    return os.name == "nt"


def _orch_python() -> str:
    return sys.executable if _is_windows() else WINDOWS_PYTHON


def _base_orchestrator_args(args: argparse.Namespace) -> list[str]:
    out = [
        _orch_python(), ORCHESTRATOR_WIN,
        "--server", args.server,
        "--database", args.database,
        "--username", args.username,
    ]
    if args.password:
        out += ["--password", args.password]
    return out


def run_orchestrator(args: argparse.Namespace, extra: Iterable[str], *, timeout: int = 60) -> Any:
    cmd = _base_orchestrator_args(args) + list(extra)
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise RuntimeError(f"orchestrator invocation failed: {type(exc).__name__}: {exc}") from exc
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip() or f"exit {result.returncode}")
    text = result.stdout.strip()
    if not text:
        return None
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return text


def run_hermes(argv: list[str], *, timeout: int = 30) -> subprocess.CompletedProcess[str]:
    if _is_windows():
        cmd = ["wsl", "-d", "Ubuntu", "--", "bash", "-lc", "hermes " + shlex.join(argv)]
    else:
        cmd = ["hermes", *argv]
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)


def list_tasks(status: Optional[str] = None) -> list[dict[str, Any]]:
    argv = ["kanban", "list"]
    if status:
        argv += ["--status", status]
    argv += ["--json"]
    r = run_hermes(argv)
    if r.returncode != 0:
        raise RuntimeError(f"kanban list failed: {r.stderr.strip()[:300]}")
    try:
        data = json.loads(r.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"kanban list returned invalid JSON: {r.stdout[:300]}") from exc
    return data if isinstance(data, list) else []


def get_runs(task_id: str) -> list[dict[str, Any]]:
    r = run_hermes(["kanban", "runs", task_id, "--json"])
    if r.returncode != 0:
        return []
    try:
        data = json.loads(r.stdout)
    except json.JSONDecodeError:
        return []
    return data if isinstance(data, list) else []


def body_field(body: Optional[str], key: str) -> Optional[str]:
    prefix = f"{key}:"
    for raw in (body or "").splitlines():
        line = raw.strip()
        if line.lower().startswith(prefix.lower()):
            value = line.split(":", 1)[1].strip()
            return value or None
    return None


def task_run_id(task: dict[str, Any]) -> Optional[str]:
    return body_field(task.get("body"), "run_id")


def task_ticket_id(task: dict[str, Any]) -> Optional[str]:
    return body_field(task.get("body"), "ticket_id")


def task_review_cycle(task: dict[str, Any]) -> int:
    raw = body_field(task.get("body"), "review_cycle")
    try:
        return max(0, int(raw or "0"))
    except ValueError:
        return 0


def latest_done_run(task_id: str) -> Optional[dict[str, Any]]:
    done = [r for r in get_runs(task_id) if r.get("status") == "done"]
    return done[-1] if done else None


def load_workflow_binding() -> dict[str, Any]:
    for path in BINDING_CANDIDATES:
        if not path or not path.exists():
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if isinstance(data, dict):
            data["_path"] = str(path)
            return data
    return {
        "schema_version": 1,
        "eligible_ticket_status": DEFAULT_ELIGIBLE_STATUS,
        "strict_resolution_status_binding": True,
        "_path": None,
    }


def infer_response_type(summary: str) -> str:
    for response_type, pattern in _RESPONSE_TYPE_PATTERNS:
        if pattern.search(summary):
            return response_type
    return "UPDATE"


def normalize_investigator_completions(*, dry_run: bool = False) -> int:
    repaired = 0
    for task in list_tasks("done"):
        if (task.get("assignee") or "") not in INVESTIGATOR_PROFILES:
            continue
        latest = latest_done_run(task["id"])
        if not latest:
            continue
        metadata = dict(latest.get("metadata") or {})
        if metadata.get("response_type") and metadata.get("reply_text"):
            continue
        summary = (latest.get("summary") or "").strip()
        if len(summary) < MIN_SUMMARY_CHARS:
            continue
        run_id = metadata.get("run_id") or task_run_id(task)
        ticket_id = metadata.get("ticket_id") or task_ticket_id(task)
        if not run_id or not ticket_id:
            continue
        metadata.update({
            "run_id": run_id,
            "ticket_id": ticket_id,
            "response_type": metadata.get("response_type") or infer_response_type(summary),
            "reply_text": metadata.get("reply_text") or summary,
            "normalized_by": "l2_pipeline_runtime.py",
        })
        if dry_run:
            print(f"[DRY RUN] normalize investigator task {task['id']}")
            continue
        r = run_hermes([
            "kanban", "edit", task["id"],
            "--result", summary[:500],
            "--metadata", json.dumps(metadata, separators=(",", ":")),
        ])
        if r.returncode == 0:
            repaired += 1
        else:
            print(f"WARNING: normalize failed for {task['id']}: {r.stderr.strip()[:300]}")
    return repaired


def _reviewer_for_investigation(tasks: list[dict[str, Any]], investigation_task_id: str) -> Optional[dict[str, Any]]:
    for t in tasks:
        if body_field(t.get("body"), "investigation_task_id") == investigation_task_id:
            return t
    return None


def create_reviewer_card(
    *,
    investigation_task_id: str,
    run_id: str,
    ticket_id: str,
    ticket_no: str,
    review_cycle: int,
    dry_run: bool = False,
) -> Optional[str]:
    body = (
        f"run_id: {run_id}\n"
        f"ticket_id: {ticket_id}\n"
        f"ticket_no: {ticket_no}\n"
        f"investigation_task_id: {investigation_task_id}\n"
        f"review_cycle: {review_cycle}\n"
        "pipeline_stage: review\n\n"
        "This is a parent-gated review card. Use kanban_show() and the completed parent's "
        "structured completion metadata as the proposal. Verify the core claim against live "
        "evidence. Approve with kanban_complete; reject with kanban_block."
    )
    argv = [
        "kanban", "create", f"REVIEW[{review_cycle}]: L2 {ticket_no}",
        "--assignee", REVIEWER_PROFILE,
        "--body", body,
        "--priority", str(REVIEW_PRIORITY),
        "--parent", investigation_task_id,
        "--skill", "xstudio-l2-draft-verifier",
        "--skill", "xstudio-sql-write-discipline",
        "--idempotency-key", f"review-{run_id}-{review_cycle}-{investigation_task_id}",
        "--max-runtime", "15m",
        "--json",
    ]
    if dry_run:
        print(f"[DRY RUN] create reviewer for {investigation_task_id} cycle={review_cycle}")
        return "dry-run"
    r = run_hermes(argv)
    if r.returncode != 0:
        print(f"WARNING: reviewer create failed: {r.stderr.strip()[:300]}")
        return None
    try:
        return (json.loads(r.stdout) or {}).get("id")
    except json.JSONDecodeError:
        return None


def default_args() -> argparse.Namespace:
    return argparse.Namespace(
        server=os.environ.get("MSSQL_MCP_SERVER") or DEFAULT_SERVER,
        database=DEFAULT_DATABASE,
        username=os.environ.get("MSSQL_MCP_USER") or DEFAULT_USER,
        password=os.environ.get("MSSQL_MCP_PASSWORD"),
        eligible_status=DEFAULT_ELIGIBLE_STATUS,
        stale_after_minutes=ORPHAN_GRACE_MINUTES,
        dry_run=False,
    )


def safe_query_active_run(run_id: str, args: Optional[argparse.Namespace] = None) -> list[dict[str, Any]]:
    if args is None:
        args = default_args()
    safe = run_id.replace("'", "''")
    sql = (
        "SELECT ID, TicketID, ProcessStatus, IsActive, ResponseType, ReplyText, ClaimedOn, HeartbeatOn "
        "FROM dbo.Hermes_L2_Response_Trn_Tbl "
        f"WHERE ID = '{safe}' AND IsDeleted = 0 AND IsActive = 1"
    )
    try:
        rows = run_orchestrator(args, ["--query", sql])
    except RuntimeError:
        return []
    return rows if isinstance(rows, list) else []


def ensure_missing_reviewers(*, dry_run: bool = False) -> int:
    tasks = list_tasks()
    created = 0
    for task in tasks:
        if task.get("status") != "done" or (task.get("assignee") or "") not in INVESTIGATOR_PROFILES:
            continue
        run_id, ticket_id = task_run_id(task), task_ticket_id(task)
        if not run_id or not ticket_id:
            continue
        if _reviewer_for_investigation(tasks, task["id"]):
            continue
        if not safe_query_active_run(run_id):
            continue
        cycle = task_review_cycle(task)
        ticket_no = body_field(task.get("body"), "ticket_no") or ticket_id
        if create_reviewer_card(
            investigation_task_id=task["id"], run_id=run_id, ticket_id=ticket_id,
            ticket_no=ticket_no, review_cycle=cycle, dry_run=dry_run,
        ):
            created += 1
    return created


def query_active_runs(args: argparse.Namespace) -> list[dict[str, Any]]:
    sql = (
        "SELECT ID, TicketID, ProcessStatus, ClaimedOn, HeartbeatOn, "
        "DATEDIFF(MINUTE, ISNULL(HeartbeatOn, ClaimedOn), GETDATE()) AS AgeMinutes "
        "FROM dbo.Hermes_L2_Response_Trn_Tbl "
        "WHERE IsActive = 1 AND IsDeleted = 0 ORDER BY ClaimedOn"
    )
    rows = run_orchestrator(args, ["--query", sql])
    return rows if isinstance(rows, list) else []


def reviewer_block_reason(task: dict[str, Any]) -> str:
    profile = task.get("assignee") or ""
    runs = get_runs(task["id"])
    blocks = [
        r for r in runs
        if r.get("outcome") == "blocked" and (not profile or r.get("profile") == profile)
    ]
    if not blocks:
        blocks = [r for r in runs if r.get("outcome") == "blocked"]
    return ((blocks[-1].get("summary") if blocks else None) or "Reviewer rejected without a recorded reason.").strip()


def _persist_rejected_ledger(args: argparse.Namespace, investigation_task_id: Optional[str], run_id: str) -> str:
    if not investigation_task_id:
        return ""
    done = [r for r in get_runs(investigation_task_id) if r.get("status") == "done"]
    if not done:
        return ""
    last = done[-1]
    md = last.get("metadata") or {}
    ledger = {
        "source": "rejected_attempt",
        "prior_investigation_task_id": investigation_task_id,
        "summary": (last.get("summary") or "").strip(),
        **{k: md[k] for k in ("response_type", "reply_text", "findings", "root_cause", "resolution") if md.get(k)},
    }
    try:
        run_orchestrator(args, ["--save-ledger", run_id, "--ledger", json.dumps(ledger)], timeout=45)
    except RuntimeError:
        pass
    return json.dumps(ledger, indent=2)[:3000]


def archive_task(task_id: str) -> None:
    r = run_hermes(["kanban", "archive", task_id])
    if r.returncode != 0:
        print(f"WARNING: could not archive {task_id}: {r.stderr.strip()[:200]}")


def _l3_exists(args: argparse.Namespace, run_id: str) -> bool:
    safe = run_id.replace("'", "''")
    sql = (
        "SELECT TOP 1 ID FROM dbo.Hermes_L3_Escalation_Trn_Tbl "
        f"WHERE RunID = '{safe}' AND IsDeleted = 0"
    )
    try:
        rows = run_orchestrator(args, ["--query", sql])
    except RuntimeError:
        return False
    return bool(rows)


def escalate_review_cycle(args: argparse.Namespace, task: dict[str, Any], reason: str, *, dry_run: bool) -> bool:
    run_id, ticket_id = task_run_id(task), task_ticket_id(task)
    if not run_id or not ticket_id:
        return False
    cycle = task_review_cycle(task)
    if dry_run:
        print(f"[DRY RUN] escalate run {run_id} after review cycle {cycle}: {reason[:120]}")
        return True
    if not _l3_exists(args, run_id):
        try:
            if safe_query_active_run(run_id, args):
                run_orchestrator(args, [
                    "--fail-run", "--run-id", run_id,
                    "--error-message", f"Review cycle cap reached after {cycle + 1} reviews. {reason[:500]}",
                    "--retry-after-minutes", "999999",
                ])
            run_orchestrator(args, [
                "--escalate-blocked", "--run-id", run_id,
                "--ticket-id", ticket_id,
                "--block-reason", f"Review cycle cap reached after {cycle + 1} reviews. Latest objection: {reason[:1500]}",
            ])
        except RuntimeError as exc:
            print(f"WARNING: escalation failed for {run_id}: {exc}")
            return False
    archive_task(task["id"])
    return True


def process_rejections(args: argparse.Namespace, *, dry_run: bool = False) -> int:
    processed = 0
    tasks = list_tasks("blocked")
    all_tasks = list_tasks()
    for task in tasks:
        if (task.get("assignee") or "") not in REVIEWER_PROFILES:
            continue
        run_id, ticket_id = task_run_id(task), task_ticket_id(task)
        investigation_task_id = body_field(task.get("body"), "investigation_task_id")
        if not run_id or not ticket_id:
            continue
        already = any(body_field(t.get("body"), "source_review_task_id") == task["id"] for t in all_tasks)
        if already:
            continue
        reason = reviewer_block_reason(task)
        current_cycle = task_review_cycle(task)
        next_cycle = current_cycle + 1
        if next_cycle >= MAX_REVIEW_CYCLES:
            if escalate_review_cycle(args, task, reason, dry_run=dry_run):
                processed += 1
            continue

        prior = _persist_rejected_ledger(args, investigation_task_id, run_id) if not dry_run else ""
        body = (
            f"run_id: {run_id}\n"
            f"ticket_id: {ticket_id}\n"
            f"ticket_no: {body_field(task.get('body'), 'ticket_no') or ticket_id}\n"
            f"review_cycle: {next_cycle}\n"
            f"source_review_task_id: {task['id']}\n"
            f"prior_investigation_task_id: {investigation_task_id or 'unknown'}\n"
            "pipeline_stage: rework\n\n"
            f"REVIEWER OBJECTION:\n{reason}\n\n"
            "Address the rejected point using current live evidence. Reuse prior verified findings; do not "
            "restart the entire investigation unless the objection invalidates them. Complete with the full "
            "structured metadata contract.\n"
        )
        if prior:
            body += f"\nPRIOR FINDINGS (verbatim):\n{prior}\n"
        argv = [
            "kanban", "create", f"REWORK[{next_cycle}]: {task.get('title') or ticket_id}",
            "--body", body,
            "--assignee", INVESTIGATOR_PROFILE,
            "--priority", str(REWORK_PRIORITY),
            "--skill", "xstudio-l2-ticket-workflow",
            "--skill", "xstudio-sql-write-discipline",
            "--idempotency-key", f"rework-{task['id']}",
            "--max-runtime", "20m",
            "--json",
        ]
        if dry_run:
            print(f"[DRY RUN] create rework for reviewer {task['id']} cycle={next_cycle}")
            processed += 1
            continue
        r = run_hermes(argv)
        if r.returncode != 0:
            print(f"WARNING: rework create failed for {task['id']}: {r.stderr.strip()[:300]}")
            continue
        try:
            rework_id = (json.loads(r.stdout) or {}).get("id")
        except json.JSONDecodeError:
            rework_id = None
        if not rework_id:
            print(f"WARNING: rework created but id could not be parsed for {task['id']}")
            continue
        ticket_no = body_field(task.get("body"), "ticket_no") or ticket_id
        reviewer_id = create_reviewer_card(
            investigation_task_id=rework_id, run_id=run_id, ticket_id=ticket_id,
            ticket_no=ticket_no, review_cycle=next_cycle, dry_run=False,
        )
        if not reviewer_id:
            print(f"WARNING: rework {rework_id} exists but reviewer child creation failed; reconciler will repair topology")
        archive_task(task["id"])
        processed += 1
    return processed


def _metadata_for_review(task: dict[str, Any]) -> Optional[dict[str, Any]]:
    source_id = body_field(task.get("body"), "investigation_task_id")
    if not source_id:
        return None
    done = [r for r in get_runs(source_id) if r.get("status") == "done"]
    candidates = [r for r in done if (r.get("metadata") or {}).get("response_type")]
    if not candidates:
        return None
    return dict(candidates[-1].get("metadata") or {})


def _status_args_for_response(binding: dict[str, Any], metadata: dict[str, Any]) -> tuple[list[str], Optional[str]]:
    response_type = str(metadata.get("response_type") or "").upper()
    out: list[str] = []
    expected_status: Optional[str] = None

    # Workflow transitions are harness-owned. Model-provided new_ticket_status is
    # ignored unless the deployment explicitly permits it.
    allow_override = bool(binding.get("allow_metadata_status_override", False))
    override = metadata.get("new_ticket_status") if allow_override else None

    if response_type == "RESOLUTION":
        expected_status = override or binding.get("resolved_ticket_status")
        if not expected_status and binding.get("strict_resolution_status_binding", True):
            raise RuntimeError(
                "RESOLUTION approved but deploy/helpdesk_workflow_binding.json has no resolved_ticket_status. "
                "Refusing to create an internally-completed ticket that still looks unresolved in Helpdesk."
            )
    elif response_type == "QUESTION":
        expected_status = override or binding.get("waiting_user_ticket_status")
        ask = binding.get("waiting_user_ask_status")
        if ask:
            out += ["--new-ask-status", str(ask)]
    elif response_type == "L3_ESCALATION":
        expected_status = override or binding.get("l3_ticket_status")
    elif response_type == "NEEDS_HUMAN_ACTION":
        expected_status = override or binding.get("needs_human_action_ticket_status") or binding.get("l3_ticket_status")

    if expected_status:
        out += ["--new-ticket-status", str(expected_status)]
    return out, expected_status


def _post_publish_activity(args: argparse.Namespace, run_id: str, ticket_id: str, metadata: dict[str, Any]) -> None:
    response_type = str(metadata.get("response_type") or "UPDATE").upper()
    activity_type = {
        "RESOLUTION": "Resolution",
        "L3_ESCALATION": "Escalation",
        "NEEDS_HUMAN_ACTION": "Escalation",
        "QUESTION": "Note",
        "UPDATE": "Note",
    }.get(response_type, "Note")
    try:
        run_orchestrator(args, [
            "--log-activity", "--ticket-id", ticket_id, "--run-id", run_id,
            "--activity-type", activity_type, "--actor-type", "Bot",
            "--note-text", str(metadata.get("reply_text") or "")[:3900],
        ])
    except RuntimeError as exc:
        print(f"WARNING: activity log failed for {run_id}: {exc}")
    # Deliberately no automatic solution-article creation here. A resolved
    # incident is episodic history; KB promotion/dedupe is a separate governed
    # post-resolution process (Knowledge/KB_IMPLEMENTATION_PLAN.md).


def _query_published_state(args: argparse.Namespace, run_id: str) -> list[dict[str, Any]]:
    safe = run_id.replace("'", "''")
    sql = (
        "SELECT r.ID, r.TicketID, r.ProcessStatus, r.ResponseType, r.ReplyText, r.IsResolved, "
        "c.Status AS TicketStatus, c.AskStatus, c.SupportExecutiveRemarks "
        "FROM dbo.Hermes_L2_Response_Trn_Tbl r "
        "JOIN dbo.Complaint_Mst_Tbl c ON c.ID = r.TicketID "
        f"WHERE r.ID = '{safe}' AND r.IsDeleted = 0"
    )
    rows = run_orchestrator(args, ["--query", sql])
    return rows if isinstance(rows, list) else []


def process_approvals(args: argparse.Namespace, *, dry_run: bool = False) -> int:
    binding = load_workflow_binding()
    processed = 0
    for task in list_tasks("done"):
        if (task.get("assignee") or "") not in REVIEWER_PROFILES:
            continue
        run_id, ticket_id = task_run_id(task), task_ticket_id(task)
        if not run_id or not ticket_id:
            continue
        state = _query_published_state(args, run_id)
        if state and state[0].get("ProcessStatus") in ("COMPLETED", "WAITING_USER") and state[0].get("ReplyText"):
            continue
        metadata = _metadata_for_review(task)
        if not metadata or not metadata.get("response_type") or not metadata.get("reply_text"):
            print(f"WARNING: reviewer {task['id']} is done but source completion metadata is incomplete; leaving publish pending for deterministic repair")
            continue
        response_type = str(metadata["response_type"]).upper()
        try:
            workflow_args, expected_status = _status_args_for_response(binding, metadata)
        except RuntimeError as exc:
            print(f"PUBLISH BLOCKED for run {run_id}: {exc}")
            continue
        cmd = [
            "--publish-response", "--run-id", run_id, "--force-run-id",
            "--response-type", response_type,
            "--reply-text", str(metadata["reply_text"]),
            "--mirror-to-support-remarks",
            *workflow_args,
        ]
        if response_type == "QUESTION":
            cmd.append("--mirror-to-ask-remarks")
        for key, flag in (
            ("problem_summary", "--problem-summary"),
            ("findings", "--findings"),
            ("root_cause", "--root-cause"),
            ("resolution", "--resolution"),
        ):
            if metadata.get(key):
                cmd += [flag, str(metadata[key])]
        if dry_run:
            print(f"[DRY RUN] publish reviewer {task['id']} run={run_id} type={response_type} status={expected_status}")
            processed += 1
            continue
        try:
            run_orchestrator(args, cmd, timeout=90)
        except RuntimeError as exc:
            print(f"WARNING: publish failed for run {run_id}: {exc}")
            continue
        verify = _query_published_state(args, run_id)
        if not verify:
            print(f"WARNING: publish returned success but no SQL row found for {run_id}")
            continue
        row = verify[0]
        if row.get("ProcessStatus") not in ("COMPLETED", "WAITING_USER") or not row.get("ReplyText"):
            print(f"WARNING: publish postcondition failed for {run_id}: {row}")
            continue
        if expected_status and row.get("TicketStatus") != expected_status:
            print(f"WARNING: Helpdesk status postcondition failed for {run_id}: expected {expected_status!r}, got {row.get('TicketStatus')!r}")
            continue
        _post_publish_activity(args, run_id, ticket_id, metadata)
        processed += 1
    return processed


def recover_orphan_runs(args: argparse.Namespace, *, dry_run: bool = False, stale_after_minutes: int = ORPHAN_GRACE_MINUTES) -> int:
    tasks = list_tasks()
    referenced_run_ids = {task_run_id(t) for t in tasks if task_run_id(t)}
    recovered = 0
    for row in query_active_runs(args):
        run_id = str(row.get("ID") or "")
        if not run_id or run_id in referenced_run_ids:
            continue
        try:
            age = int(row.get("AgeMinutes") or 0)
        except (TypeError, ValueError):
            age = 0
        if age < stale_after_minutes:
            continue
        if dry_run:
            print(f"[DRY RUN] fail orphan run {run_id} age={age}m")
            recovered += 1
            continue
        try:
            run_orchestrator(args, [
                "--fail-run", "--run-id", run_id,
                "--error-message", "Pipeline reconciler: active SQL run has no Kanban task at any stage; failed for clean retry.",
                "--retry-after-minutes", "5",
            ])
            recovered += 1
        except RuntimeError as exc:
            print(f"WARNING: orphan recovery failed for {run_id}: {exc}")
    return recovered


def audit_done_reviewers(args: argparse.Namespace, *, dry_run: bool = False) -> int:
    false_positives = 0
    for task in list_tasks("done"):
        if (task.get("assignee") or "") not in REVIEWER_PROFILES:
            continue
        run_id = task_run_id(task)
        if not run_id:
            continue
        rows = _query_published_state(args, run_id)
        ok = bool(rows and rows[0].get("ProcessStatus") in ("COMPLETED", "WAITING_USER") and rows[0].get("ResponseType") and str(rows[0].get("ReplyText") or "").strip())
        if ok:
            continue
        false_positives += 1
        if dry_run:
            print(f"[DRY RUN] reviewer done but SQL not terminal: {task['id']} run={run_id}")
            continue
        marker = f"PIPELINE AUDIT: reviewer done but run {run_id} is not yet published in SQL."
        r = run_hermes(["kanban", "comment", task["id"], marker])
        if r.returncode != 0:
            print(f"WARNING: audit comment failed for {task['id']}: {r.stderr.strip()[:200]}")
    return false_positives


def reconcile(args: argparse.Namespace, *, dry_run: bool = False) -> dict[str, int]:
    # Ordering is a contract. These are synchronous function calls, not the old
    # concurrent Popen launches that let publisher race ahead of metadata repair.
    return {
        "normalized": normalize_investigator_completions(dry_run=dry_run),
        "reviewers_repaired": ensure_missing_reviewers(dry_run=dry_run),
        "rejections_processed": process_rejections(args, dry_run=dry_run),
        "approvals_published": process_approvals(args, dry_run=dry_run),
        "orphans_recovered": recover_orphan_runs(args, dry_run=dry_run, stale_after_minutes=args.stale_after_minutes),
    }


def _run_kb_retrieval(args: argparse.Namespace, ticket: dict[str, Any]) -> dict[str, Any]:
    # Do not feed model-generated SuspectedCause back into PRE_INVESTIGATION
    # retrieval; that creates confirmation bias.
    query = " ".join(str(ticket.get(k) or "") for k in (
        "BriefDetails", "Description", "ProblemCategory", "HermesAreaName", "ExtractedEntitiesJson"
    )).strip()
    if not query:
        return {"solutions": [], "abstained": True, "abstention_reason": "Ticket contains no searchable problem text."}
    cmd = [
        _orch_python(), KB_RETRIEVER_WIN,
        "--server", args.server,
        "--database", args.database,
        "--username", args.username,
        "--query", query,
        "--top", "3",
    ]
    if args.password:
        cmd += ["--password", args.password]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"solutions": [], "abstained": True, "abstention_reason": f"KB retriever unavailable: {type(exc).__name__}: {exc}"}
    if r.returncode != 0:
        return {"solutions": [], "abstained": True, "abstention_reason": f"KB retriever failed: {r.stderr.strip()[:300]}"}
    try:
        data = json.loads(r.stdout)
    except json.JSONDecodeError:
        return {"solutions": [], "abstained": True, "abstention_reason": "KB retriever returned invalid JSON."}
    return data if isinstance(data, dict) else {"solutions": [], "abstained": True, "abstention_reason": "KB retriever returned a non-object."}


def _investigation_bundle(args: argparse.Namespace, ticket_id: str, fallback_ticket: dict[str, Any]) -> str:
    try:
        bundle = run_orchestrator(args, ["--investigate-bundle", ticket_id], timeout=90)
    except RuntimeError as exc:
        bundle = {
            "ticket_id": ticket_id,
            "ticket": fallback_ticket,
            "bundle_warning": f"Dispatcher could not assemble investigation bundle: {exc}",
        }
    if not isinstance(bundle, dict):
        bundle = {"ticket_id": ticket_id, "ticket": fallback_ticket, "bundle_warning": "Unexpected bundle shape."}
    bundle.pop("known_solutions", None)
    bundle["kb_retrieval"] = _run_kb_retrieval(args, fallback_ticket)
    rendered = json.dumps(bundle, indent=2, default=str)
    if len(rendered) > 14000:
        rendered = rendered[:14000] + "\n... [bundle truncated at 14,000 chars]"
    return (
        "\n--- Investigation bundle (single dispatch-time package) ---\n"
        "KB hits, prior findings, and suggested tables are leads, not proof. Final claims require current live SQL or verified Knowledge/ evidence.\n"
        f"{rendered}\n"
    )


def _query_instructions(run_id: str, ticket_id: str) -> str:
    orch = "/mnt/c/" + ORCHESTRATOR_WIN.replace("\\", "/").removeprefix("C:/")
    ledger = json.dumps({"tables_queried": [], "key_values_found": {}, "ruled_out": [], "conclusion": "..."}, separators=(",", ":"))
    return (
        "\n--- Exact investigation commands ---\n"
        f"Interpreter: {WINDOWS_PYTHON}\nScript: {orch}\n"
        "The starting bundle is already above; do not refetch the same context.\n\n"
        f'Preferred validated read:\n  {WINDOWS_PYTHON} "{orch}" --server {DEFAULT_SERVER} --database XStudio_Xbatch --build-query dbo.SomeTable --columns "ColA,ColB" --where "HeatNo = \'123\'" --top 20 --execute\n\n'
        f'If schema candidates are insufficient:\n  {WINDOWS_PYTHON} "{orch}" --server {DEFAULT_SERVER} --database XStudio_Xbatch --suggest-tables "<specific unresolved symptom>" --top 8\n\n'
        f'Read-only SQL:\n  {WINDOWS_PYTHON} "{orch}" --server {DEFAULT_SERVER} --database XStudio_Xbatch --query "SELECT TOP 20 ..."\n\n'
        f'Persist ticket-specific findings:\n  {WINDOWS_PYTHON} "{orch}" --server {DEFAULT_SERVER} --database XStudio_Helpdesk --save-ledger {run_id} --ledger \'{ledger}\'\n\n'
        f"Refresh ticket only when needed: --get-ticket-context {ticket_id} --database XStudio_Helpdesk\n"
        "Never write the live ticket directly. Complete the Kanban task with full structured metadata; reviewer + deterministic publisher own publication.\n"
    )


def _archive_stale_cards_for_ticket(ticket_id: str, new_run_id: str) -> None:
    try:
        tasks = list_tasks()
    except RuntimeError:
        return
    stale = [
        t["id"] for t in tasks
        if t.get("status") in ARCHIVABLE_STALE_STATUSES
        and task_ticket_id(t) == ticket_id
        and task_run_id(t) != new_run_id
    ]
    if not stale:
        return
    r = run_hermes(["kanban", "archive", *stale])
    if r.returncode != 0:
        print(f"WARNING: stale-card cleanup failed: {r.stderr.strip()[:300]}")


def scout(args: argparse.Namespace, *, dry_run: bool = False) -> dict[str, Any]:
    reconciliation = reconcile(args, dry_run=dry_run)
    if dry_run:
        return {"status": "DRY_RUN", "reconcile": reconciliation}

    # Global WIP=1: a single LM Studio inference slot should finish the active
    # pipeline before another SQL ticket is claimed. This removes reviewer/rework
    # starvation and makes active-run state a real backpressure signal.
    active = query_active_runs(args)
    if active:
        return {"status": "WIP_LIMIT", "active_runs": active, "reconcile": reconciliation}

    binding = load_workflow_binding()
    eligible = str(binding.get("eligible_ticket_status") or args.eligible_status or DEFAULT_ELIGIBLE_STATUS)
    poll = run_orchestrator(args, ["--poll", "--eligible-status", eligible, "--bot-label", INVESTIGATOR_PROFILE], timeout=90)
    if not isinstance(poll, dict):
        raise RuntimeError(f"unexpected poll response: {poll!r}")
    if poll.get("status") in ("NO_TICKETS", "NO_CLAIMABLE_TICKET"):
        return {"status": poll.get("status"), "reconcile": reconciliation}
    if poll.get("status") != "CLAIMED":
        raise RuntimeError(f"unexpected poll status: {poll.get('status')}")

    run_id = str(poll["run_id"])
    ticket_id = str(poll["ticket_id"])
    ticket = poll.get("ticket") or {}
    ticket_no = str(ticket.get("TicketNo") or ticket_id)
    _archive_stale_cards_for_ticket(ticket_id, run_id)

    body = (
        f"run_id: {run_id}\n"
        f"ticket_id: {ticket_id}\n"
        f"ticket_no: {ticket_no}\n"
        "review_cycle: 0\n"
        "pipeline_stage: investigation\n"
        + _investigation_bundle(args, ticket_id, ticket)
        + _query_instructions(run_id, ticket_id)
    )
    create = run_hermes([
        "kanban", "create", f"L2 {ticket_no}",
        "--assignee", INVESTIGATOR_PROFILE,
        "--body", body,
        "--skill", "xstudio-l2-ticket-workflow",
        "--skill", "xstudio-sql-write-discipline",
        "--priority", str(NEW_INVESTIGATION_PRIORITY),
        "--idempotency-key", f"l2-ticket-{run_id}",
        "--max-runtime", "20m",
        "--json",
    ])
    if create.returncode != 0:
        try:
            run_orchestrator(args, [
                "--fail-run", "--run-id", run_id,
                "--error-message", f"Dispatcher could not create investigator Kanban task: {create.stderr.strip()[:400]}",
                "--retry-after-minutes", "5",
            ])
        except RuntimeError:
            pass
        raise RuntimeError(f"investigator create failed: {create.stderr.strip()[:500]}")
    try:
        investigator_id = (json.loads(create.stdout) or {}).get("id")
    except json.JSONDecodeError:
        investigator_id = None
    if not investigator_id:
        raise RuntimeError("investigator task was created but its id could not be parsed")

    reviewer_id = create_reviewer_card(
        investigation_task_id=investigator_id, run_id=run_id, ticket_id=ticket_id,
        ticket_no=ticket_no, review_cycle=0, dry_run=False,
    )
    if not reviewer_id:
        print(f"WARNING: reviewer child creation failed for investigator {investigator_id}; reconciler will retry")

    return {
        "status": "CLAIMED",
        "run_id": run_id,
        "ticket_id": ticket_id,
        "investigator_task_id": investigator_id,
        "reviewer_task_id": reviewer_id,
        "priorities": {"investigation": NEW_INVESTIGATION_PRIORITY, "rework": REWORK_PRIORITY, "review": REVIEW_PRIORITY},
        "reconcile": reconciliation,
    }


def pipeline_status(args: argparse.Namespace) -> dict[str, Any]:
    tasks = list_tasks()
    active = query_active_runs(args)
    by_run: dict[str, list[dict[str, Any]]] = {}
    for t in tasks:
        rid = task_run_id(t)
        if rid:
            by_run.setdefault(rid, []).append({
                "id": t.get("id"), "title": t.get("title"), "status": t.get("status"),
                "assignee": t.get("assignee"), "review_cycle": task_review_cycle(t),
            })
    anomalies = []
    for row in active:
        rid = str(row.get("ID"))
        owned = by_run.get(rid, [])
        if not owned:
            anomalies.append({"run_id": rid, "type": "ACTIVE_SQL_WITH_NO_KANBAN"})
        reviewers = [t for t in owned if t.get("assignee") in REVIEWER_PROFILES]
        investigations = [t for t in owned if t.get("assignee") in INVESTIGATOR_PROFILES]
        if not investigations:
            anomalies.append({"run_id": rid, "type": "ACTIVE_RUN_WITHOUT_INVESTIGATOR_CARD"})
        if investigations and not reviewers and all(t.get("status") == "done" for t in investigations):
            anomalies.append({"run_id": rid, "type": "DONE_INVESTIGATION_WITHOUT_REVIEWER"})
    return {
        "active_runs": active,
        "tasks_by_run": by_run,
        "anomalies": anomalies,
        "binding": load_workflow_binding(),
        "contract": {
            "max_pipeline_wip": 1,
            "priorities": {"review": REVIEW_PRIORITY, "rework": REWORK_PRIORITY, "new_investigation": NEW_INVESTIGATION_PRIORITY},
            "max_review_cycles": MAX_REVIEW_CYCLES,
            "live_kanban_statuses": sorted(LIVE_KANBAN_STATUSES),
        },
    }


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("mode", choices=["scout", "reconcile", "repair", "publish", "reject", "recover", "audit", "status"])
    p.add_argument("--server", default=os.environ.get("MSSQL_MCP_SERVER") or DEFAULT_SERVER)
    p.add_argument("--database", default=DEFAULT_DATABASE)
    p.add_argument("--username", default=os.environ.get("MSSQL_MCP_USER") or DEFAULT_USER)
    p.add_argument("--password", default=os.environ.get("MSSQL_MCP_PASSWORD"))
    p.add_argument("--eligible-status", default=DEFAULT_ELIGIBLE_STATUS)
    p.add_argument("--stale-after-minutes", type=int, default=ORPHAN_GRACE_MINUTES)
    p.add_argument("--dry-run", action="store_true")
    return p


def cli(argv: Optional[list[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.mode == "scout":
            out = scout(args, dry_run=args.dry_run)
        elif args.mode == "reconcile":
            out = reconcile(args, dry_run=args.dry_run)
        elif args.mode == "repair":
            out = {"normalized": normalize_investigator_completions(dry_run=args.dry_run), "reviewers_repaired": ensure_missing_reviewers(dry_run=args.dry_run)}
        elif args.mode == "publish":
            normalize_investigator_completions(dry_run=args.dry_run)
            out = {"approvals_published": process_approvals(args, dry_run=args.dry_run)}
        elif args.mode == "reject":
            out = {"rejections_processed": process_rejections(args, dry_run=args.dry_run)}
        elif args.mode == "recover":
            out = {"orphans_recovered": recover_orphan_runs(args, dry_run=args.dry_run, stale_after_minutes=args.stale_after_minutes)}
        elif args.mode == "audit":
            out = {"false_positive_reviews": audit_done_reviewers(args, dry_run=args.dry_run)}
        else:
            out = pipeline_status(args)
    except Exception as exc:
        print(json.dumps({"ok": False, "error": f"{type(exc).__name__}: {exc}"}, default=str))
        return 1
    print(json.dumps({"ok": True, "mode": args.mode, "result": out}, indent=2, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(cli())
