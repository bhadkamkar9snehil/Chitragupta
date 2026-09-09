#!/usr/bin/env python3
"""Deterministic state machine for the Chitragupta L2 Helpdesk pipeline.

The pipeline has one safe LM Studio inference slot. Correct throughput therefore means
finishing the active ticket before claiming another one, not accumulating a queue of
higher-priority investigations that starves review/rework.

Lifecycle owned here (no LLM choreography):

    SQL claim
      -> investigator
      -> reviewer
         -> approve -> publish
         -> reject  -> rework investigator -> reviewer -> ... (bounded)

Important design choice: reviewer cards are created only *after* an investigator/rework
completion has been normalized into the required metadata contract. We do not pre-create
a parent-gated reviewer anymore. That removes the race where Hermes could promote/start
the reviewer before the deterministic metadata-repair step had finished.

Every operation is idempotent and may be triggered both by the observer hook and by the
2-minute ticket-scout backstop.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import subprocess
import sys
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterable, Optional

try:
    from Model_Bench.xbatch_world import build_evidence_matrix, load_world, select_recipes, world_context
except ImportError:  # deployed scripts live beside xbatch_world.py
    from xbatch_world import build_evidence_matrix, load_world, select_recipes, world_context

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

# Finish work before starting work. With max_in_progress=1 this is the scheduling
# policy that prevents reviewer/rework starvation.
NEW_INVESTIGATION_PRIORITY = 10
REWORK_PRIORITY = 20
REVIEW_PRIORITY = 30

# Review cycles are deliberately distinct from SQL AttemptNo. SQL AttemptNo increments
# only when a ticket is claimed into a genuinely new Hermes run; a reject/rework stays
# inside the same run.
MAX_REVIEW_CYCLES = 3  # cycle 0 initial + cycle 1/2 rework reviews; reject at 2 escalates
ORPHAN_GRACE_MINUTES = 45
MIN_SUMMARY_CHARS = 40

# Kept broad for diagnostics/compatibility. `todo` remains a live state even though the
# new reconciler no longer relies on pre-created parent-gated reviewers.
LIVE_KANBAN_STATUSES = {"todo", "ready", "blocked", "triage", "running", "review", "scheduled"}

REPO_ROOT_WSL = Path("/mnt/c/Users/Admin/Documents/Office/AIHelpdesk")
BINDING_CANDIDATES = [
    Path(os.environ["L2_HELPDESK_WORKFLOW_BINDING"]) if os.environ.get("L2_HELPDESK_WORKFLOW_BINDING") else None,
    REPO_ROOT_WSL / "deploy" / "helpdesk_workflow_binding.json",
    Path(__file__).resolve().parent / "helpdesk_workflow_binding.json",
    Path(__file__).resolve().parent.parent / "deploy" / "helpdesk_workflow_binding.json",
]

_RESPONSE_TYPE_PATTERNS = [
    ("NEEDS_HUMAN_ACTION", re.compile(r"\bneeds? human action\b|\bhuman (?:must|needs to)\b", re.I)),
    ("L3_ESCALATION", re.compile(r"\bl3 escalat|\bescalat\w* to l3|\bescalating\b", re.I)),
    ("RESOLUTION", re.compile(r"\bresolved\b|\bfix(?:ed)? confirmed\b|\bverified live\b.*\bfix", re.I)),
    ("QUESTION", re.compile(r"\?\s*$|need(?:s)? (?:more info|clarification) from|requester\b.*\bconfirm", re.I)),
]

_INCOMPLETE_EVIDENCE_MARKERS = re.compile(
    r"\b(?:could not|unable to|not established|not verified|unverified|"
    r"budget exhaustion|budget exhausted|need(?:s)? to verify|insufficient evidence|"
    r"unclear|unknown|cannot confirm)\b",
    re.I,
)


def annotate_evidence_status(metadata: dict[str, Any]) -> dict[str, Any]:
    """Make incomplete evidence explicit before a reviewer sees a proposal.

    A bounded worker may run out of typed-tool budget after discovering useful
    facts but before proving the material claim. Preserve its wording, while
    adding a machine-readable status and an unmistakable reviewer-facing
    limitation so an incomplete UPDATE cannot read like a verified result.
    """
    out = dict(metadata)
    text = " ".join(
        str(out.get(key) or "")
        for key in ("reply_text", "findings", "root_cause", "resolution", "summary")
    )
    if _INCOMPLETE_EVIDENCE_MARKERS.search(text):
        out["evidence_status"] = "INCOMPLETE"
        reply = str(out.get("reply_text") or "").strip()
        if reply and not reply.lower().startswith("evidence status: incomplete"):
            out["reply_text"] = (
                "Evidence status: INCOMPLETE. No material claim below should be treated "
                "as verified until the missing live evidence is obtained.\n\n" + reply
            )
    # Also flag proposals where material VERIFIED claims lack evidence references.
    claims = out.get("claims")
    if isinstance(claims, list):
        for claim in claims:
            if not isinstance(claim, dict):
                continue
            if (claim.get("material") and claim.get("status") == "VERIFIED"
                    and not claim.get("evidence")):
                out["evidence_status"] = "CLAIM_EVIDENCE_GAP"
                break
    return out


# Claim statuses recognised by the pipeline.  Semantic truth belongs to the
# independent reviewer; this module only validates provenance structure.
VALID_CLAIM_STATUSES = {"VERIFIED", "INFERRED", "UNVERIFIED", "CONTRADICTED"}
CLAIMS_CONTRACT_VERSION = 1


def validate_claims_contract(
    claims: Any, *, run_id: Optional[str] = None, ticket_id: Optional[str] = None,
    actions: Optional[list[dict[str, Any]]] = None,
) -> tuple[bool, list[str]]:
    """Validate structural correctness of a claims array.

    Returns (valid, issues). Does NOT evaluate semantic truth -- that is the
    reviewer's job. This only enforces:
      - every claim has id, claim text, material flag, status
      - VERIFIED claims have at least one immutable audit ActionID reference
      - when current-run actions are supplied, every reference belongs to that
        exact run and ticket
      - status is from the recognised enum
    """
    if claims is None:
        return True, []  # claims are optional for backward compat
    if not isinstance(claims, list):
        return False, ["claims must be an array"]

    issues: list[str] = []
    seen_ids: set[str] = set()
    for i, claim in enumerate(claims):
        label = f"claims[{i}]"
        if not isinstance(claim, dict):
            issues.append(f"{label}: must be an object")
            continue
        cid = claim.get("id")
        if not cid or not isinstance(cid, str):
            issues.append(f"{label}: missing or invalid id")
        elif cid in seen_ids:
            issues.append(f"{label}: duplicate id {cid!r}")
        else:
            seen_ids.add(cid)
        if not claim.get("claim"):
            issues.append(f"{label}: missing claim text")
        status = claim.get("status")
        if status not in VALID_CLAIM_STATUSES:
            issues.append(f"{label}: status {status!r} not in {sorted(VALID_CLAIM_STATUSES)}")
        if claim.get("material") and status == "VERIFIED":
            evidence = claim.get("evidence")
            if not evidence or not isinstance(evidence, list) or len(evidence) == 0:
                issues.append(f"{label} ({cid}): material VERIFIED claim has no evidence reference")
            else:
                action_index = {str(row.get("ID")): row for row in (actions or []) if row.get("ID")}
                for j, ref in enumerate(evidence):
                    if not isinstance(ref, dict) or not isinstance(ref.get("action_id"), str):
                        issues.append(f"{label}.evidence[{j}]: must have an action_id")
                        continue
                    if actions is not None:
                        action = action_index.get(ref["action_id"])
                        if not action:
                            issues.append(f"{label}.evidence[{j}]: action_id is not in the current run")
                        elif str(action.get("RunID")) != str(run_id) or str(action.get("TicketID")) != str(ticket_id):
                            issues.append(f"{label}.evidence[{j}]: action_id does not belong to the current run/ticket")

    return (len(issues) == 0), issues


def get_run_actions(args: argparse.Namespace, run_id: str) -> list[dict[str, Any]]:
    """Return the audited action trail used to validate frozen evidence refs."""
    rows = run_orchestrator(args, ["--get-run-actions", run_id])
    return rows if isinstance(rows, list) else []


# ---------------------------------------------------------------------------
# Process / transport helpers
# ---------------------------------------------------------------------------

def _is_windows() -> bool:
    return os.name == "nt"


def _orch_python() -> str:
    return sys.executable


def _orch_path() -> str:
    return ORCHESTRATOR_WIN if _is_windows() else str(REPO_ROOT_WSL / "Hermes_Orchestrator.py")


def _kb_retriever_path() -> str:
    return KB_RETRIEVER_WIN if _is_windows() else str(REPO_ROOT_WSL / "Model_Bench" / "kb_retrieval.py")


def _base_orchestrator_args(args: argparse.Namespace) -> list[str]:
    cmd = [
        _orch_python(), _orch_path(),
        "--server", args.server,
        "--database", args.database,
        "--username", args.username,
    ]
    # Passing a literal None in argv crashes subprocess before the native
    # interpreter can start, so omit the flag when the environment lacks it.
    if args.password:
        cmd += ["--password", args.password]
    return cmd


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


def list_all_tasks(status: Optional[str] = None) -> list[dict[str, Any]]:
    """Read the whole Kanban board only when an orphan check truly needs it."""
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


def list_tasks(status: Optional[str] = None) -> list[dict[str, Any]]:
    """Return lifecycle-owned cards without serializing unrelated historical work.

    The board retains large completed task bodies. A full ``kanban list`` can exceed
    the lifecycle command timeout and wedge global WIP. All cards created by this
    runtime are assigned to one of these profiles, so query each profile directly.
    ``recover_orphan_runs`` performs a full-board fallback only for an active run
    that has no such card at all.
    """
    tasks_by_id: dict[str, dict[str, Any]] = {}
    for profile in sorted(INVESTIGATOR_PROFILES | REVIEWER_PROFILES):
        argv = ["kanban", "list", "--assignee", profile]
        if status:
            argv += ["--status", status]
        argv += ["--json"]
        r = run_hermes(argv)
        if r.returncode != 0:
            raise RuntimeError(f"kanban list failed for {profile}: {r.stderr.strip()[:300]}")
        try:
            data = json.loads(r.stdout)
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"kanban list returned invalid JSON for {profile}: {r.stdout[:300]}") from exc
        for task in data if isinstance(data, list) else []:
            task_id = str(task.get("id") or "")
            if task_id:
                tasks_by_id[task_id] = task
    return list(tasks_by_id.values())


def get_runs(task_id: str) -> list[dict[str, Any]]:
    r = run_hermes(["kanban", "runs", task_id, "--json"])
    if r.returncode != 0:
        raise RuntimeError(f"Kanban attempt history unavailable for {task_id}")
    try:
        data = json.loads(r.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Invalid Kanban attempt history for {task_id}") from exc
    return data if isinstance(data, list) else []


# ---------------------------------------------------------------------------
# Kanban/task metadata helpers
# ---------------------------------------------------------------------------

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


def task_proposal(task: dict[str, Any]) -> Optional[dict[str, Any]]:
    raw = body_field(task.get("body"), "proposal_json")
    if not raw:
        return None
    try:
        value = json.loads(raw)
    except json.JSONDecodeError:
        return None
    return value if isinstance(value, dict) else None


def latest_done_run(task_id: str) -> Optional[dict[str, Any]]:
    done = [r for r in get_runs(task_id) if r.get("status") == "done"]
    return done[-1] if done else None


def _source_has_reviewer(tasks: list[dict[str, Any]], source_task_id: str) -> bool:
    return any(body_field(t.get("body"), "investigation_task_id") == source_task_id for t in tasks)


def _source_has_rework(tasks: list[dict[str, Any]], source_task_id: str) -> bool:
    return any(body_field(t.get("body"), "rework_source_id") == source_task_id for t in tasks)


def _completion_metadata(task: dict[str, Any]) -> Optional[dict[str, Any]]:
    latest = latest_done_run(task["id"])
    if not latest:
        return None
    md = dict(latest.get("metadata") or {})
    if not md.get("run_id"):
        md["run_id"] = task_run_id(task)
    if not md.get("ticket_id"):
        md["ticket_id"] = task_ticket_id(task)
    if body_field(task.get("body"), "claims_contract_version"):
        md["claims_contract_version"] = CLAIMS_CONTRACT_VERSION
    return annotate_evidence_status(md)


def _proposal_complete(md: Optional[dict[str, Any]]) -> bool:
    basic = bool(
        md
        and md.get("run_id")
        and md.get("ticket_id")
        and md.get("response_type") in {"UPDATE", "QUESTION", "RESOLUTION", "L3_ESCALATION", "NEEDS_HUMAN_ACTION"}
        and str(md.get("reply_text") or "").strip()
    )
    return basic and (md.get("claims_contract_version") != CLAIMS_CONTRACT_VERSION or isinstance(md.get("claims"), list))


# ---------------------------------------------------------------------------
# Workflow binding
# ---------------------------------------------------------------------------

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
        "allow_metadata_status_override": False,
        "_path": None,
    }


def _binding_ready_for_claims(binding: dict[str, Any]) -> tuple[bool, Optional[str]]:
    if binding.get("strict_resolution_status_binding", True) and not binding.get("resolved_ticket_status"):
        return False, (
            "resolved_ticket_status is not configured; run Model_Bench/configure_helpdesk_workflow.py "
            "against the live Helpdesk and bind the exact observed terminal status before new claims."
        )
    return True, None


def _status_args_for_response(binding: dict[str, Any], metadata: dict[str, Any]) -> tuple[list[str], Optional[str]]:
    response_type = str(metadata.get("response_type") or "").upper()
    out: list[str] = []
    expected_status: Optional[str] = None

    # Workflow transitions are harness-owned. Model-provided new_ticket_status is ignored
    # unless a deployment explicitly opts into overrides.
    allow_override = bool(binding.get("allow_metadata_status_override", False))
    override = metadata.get("new_ticket_status") if allow_override else None

    if response_type == "RESOLUTION":
        expected_status = override or binding.get("resolved_ticket_status")
        if not expected_status and binding.get("strict_resolution_status_binding", True):
            raise RuntimeError(
                "RESOLUTION approved but workflow binding has no resolved_ticket_status; "
                "refusing to complete Hermes while leaving Helpdesk visibly unresolved."
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


# ---------------------------------------------------------------------------
# SQL/run state helpers
# ---------------------------------------------------------------------------

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
    args = args or default_args()
    safe = run_id.replace("'", "''")
    sql = (
        "SELECT ID, TicketID, ProcessStatus, IsActive, ResponseType, ReplyText, ClaimedOn, HeartbeatOn "
        "FROM dbo.Hermes_L2_Response_Trn_Tbl "
        f"WHERE ID = '{safe}' AND IsDeleted = 0 AND IsActive = 1"
    )
    rows = run_orchestrator(args, ["--query", sql])
    return rows if isinstance(rows, list) else []


def query_active_runs(args: argparse.Namespace) -> list[dict[str, Any]]:
    sql = (
        "SELECT ID, TicketID, ProcessStatus, ClaimedOn, HeartbeatOn, "
        "DATEDIFF(MINUTE, ISNULL(HeartbeatOn, ClaimedOn), GETDATE()) AS AgeMinutes "
        "FROM dbo.Hermes_L2_Response_Trn_Tbl "
        "WHERE IsActive = 1 AND IsDeleted = 0 ORDER BY ClaimedOn"
    )
    rows = run_orchestrator(args, ["--query", sql])
    return rows if isinstance(rows, list) else []


def _query_published_state(args: argparse.Namespace, run_id: str) -> list[dict[str, Any]]:
    safe = run_id.replace("'", "''")
    sql = (
        "SELECT r.ID, r.TicketID, r.ProcessStatus, r.ResponseType, r.ReplyText, r.IsResolved, "
        "r.NextEligibleOn, c.Status AS TicketStatus, c.AskStatus, c.SupportExecutiveRemarks "
        "FROM dbo.Hermes_L2_Response_Trn_Tbl r "
        "JOIN dbo.Complaint_Mst_Tbl c ON c.ID = r.TicketID "
        f"WHERE r.ID = '{safe}' AND r.IsDeleted = 0"
    )
    rows = run_orchestrator(args, ["--query", sql])
    return rows if isinstance(rows, list) else []


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


# ---------------------------------------------------------------------------
# Completion normalization and reviewer creation
# ---------------------------------------------------------------------------

def infer_response_type(summary: str) -> str:
    for response_type, pattern in _RESPONSE_TYPE_PATTERNS:
        if pattern.search(summary):
            return response_type
    # Safest fallback. A verifier may reject/downgrade/upgrade based on evidence, but
    # the repair layer never invents a terminal outcome from ambiguous prose.
    return "UPDATE"


def normalized_fallback_claims(summary: str) -> list[dict[str, Any]]:
    """Preserve an unstructured completion without pretending it is verified.

    Small models often put a useful finding in ``summary`` while leaving the
    generic Kanban metadata object empty. A second model session just to copy
    that prose into JSON is wasted compute. The safe deterministic repair is a
    material UNVERIFIED claim: it is reviewable, cannot satisfy VERIFIED
    provenance gates, and tells the reviewer exactly what still needs checking.
    """
    return [{
        "id": "C1",
        "claim": "The worker completed without supplying a structured claim/evidence contract.",
        "material": True,
        "status": "UNVERIFIED",
        "evidence": [],
        "required_evidence": ["Review the preserved investigator_notes and current-run actions before making any factual claim."],
    }]


def normalize_investigator_completions(*, dry_run: bool = False, active_run_ids: Optional[set[str]] = None) -> int:
    repaired = 0
    for task in list_tasks("done"):
        if active_run_ids is not None and task_run_id(task) not in active_run_ids:
            continue
        if (task.get("assignee") or "") not in INVESTIGATOR_PROFILES:
            continue
        latest = latest_done_run(task["id"])
        if not latest:
            continue
        metadata = dict(latest.get("metadata") or {})
        if _proposal_complete({
            **metadata,
            "run_id": metadata.get("run_id") or task_run_id(task),
            "ticket_id": metadata.get("ticket_id") or task_ticket_id(task),
        }):
            continue
        summary = (latest.get("summary") or "").strip()
        if len(summary) < MIN_SUMMARY_CHARS:
            continue
        run_id = metadata.get("run_id") or task_run_id(task)
        ticket_id = metadata.get("ticket_id") or task_ticket_id(task)
        if not run_id or not ticket_id:
            continue
        had_structured_reply = bool(metadata.get("reply_text"))
        metadata.update({
            "run_id": run_id,
            "ticket_id": ticket_id,
            "response_type": metadata.get("response_type") or infer_response_type(summary),
            "reply_text": metadata.get("reply_text") or (
                "Live investigation actions were recorded, but the investigator did not provide a "
                "structurally reviewable claim/evidence proposal. No cause or resolution is verified. "
                "The complete evidence trail has been preserved for reviewer and human follow-up."
            ),
            "normalized_by": "l2_pipeline_runtime.py",
        })
        if body_field(task.get("body"), "claims_contract_version"):
            metadata["claims_contract_version"] = CLAIMS_CONTRACT_VERSION
            if not isinstance(metadata.get("claims"), list):
                metadata["claims"] = normalized_fallback_claims(summary)
                metadata["contract_repaired_from_unstructured"] = True
                metadata["investigator_notes"] = summary
                if not had_structured_reply:
                    metadata["response_type"] = "UPDATE"
        metadata = annotate_evidence_status(metadata)
        if dry_run:
            print(f"[DRY RUN] normalize investigator task {task['id']}")
            repaired += 1
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


def create_reviewer_card(
    *,
    source_task: dict[str, Any],
    proposal: dict[str, Any],
    verification_context: str = "",
    dry_run: bool = False,
) -> Optional[str]:
    run_id = str(proposal["run_id"])
    ticket_id = str(proposal["ticket_id"])
    ticket_no = body_field(source_task.get("body"), "ticket_no") or ticket_id
    cycle = task_review_cycle(source_task)
    proposal_json = json.dumps(proposal, separators=(",", ":"), default=str)

    # Proposal is frozen into the reviewer card. The reviewer and publisher therefore
    # judge/publish the exact same payload; neither has to reconstruct it from prose or
    # from mutable parent state later.
    body = (
        f"run_id: {run_id}\n"
        f"ticket_id: {ticket_id}\n"
        f"ticket_no: {ticket_no}\n"
        f"investigation_task_id: {source_task['id']}\n"
        f"review_cycle: {cycle}\n"
        f"claims_contract_version: {proposal.get('claims_contract_version') or body_field(source_task.get('body'), 'claims_contract_version') or 'legacy'}\n"
        "pipeline_stage: review\n"
        f"proposal_json: {proposal_json}\n\n"
        + verification_context
        +
        "The ticket identifier is not proof of database storage representation (for example, "
        "H99328 may map to a numeric key); establish the physical key and format from live "
        "schema/rows.\n"
        "Verify the frozen proposal above against live evidence. Approve with kanban_complete; "
        "reject with kanban_block. The deterministic reconciler owns publication/rework.\n"
        "The harness has collected a fresh reviewer verification context below when a deterministic route exists. "
        "Inspect it and call only the smallest additional live context tool if it does not cover a material claim. "
        "Reject a VERIFIED material claim if its action_id is not in this "
        "run/ticket or the evidence does not support its strength. Do not infer causation from absence."
    )
    argv = [
        "kanban", "create", f"REVIEW[{cycle}]: L2 {ticket_no}",
        "--assignee", REVIEWER_PROFILE,
        "--body", body,
        "--priority", str(REVIEW_PRIORITY),
        "--skill", "xstudio-l2-draft-verifier",
        "--skill", "xstudio-sql-write-discipline",
        "--idempotency-key", f"review-{run_id}-{cycle}-{source_task['id']}",
        "--max-runtime", "15m",
        "--max-retries", "1",
        "--json",
    ]
    if dry_run:
        print(f"[DRY RUN] create reviewer for {source_task['id']} cycle={cycle}")
        return "dry-run"
    r = run_hermes(argv)
    if r.returncode != 0:
        print(f"WARNING: reviewer create failed for {source_task['id']}: {r.stderr.strip()[:300]}")
        return None
    try:
        return (json.loads(r.stdout) or {}).get("id")
    except json.JSONDecodeError:
        return None


def _review_evidence_context(args: argparse.Namespace, proposal: dict[str, Any],
                             ticket: dict[str, Any]) -> str:
    """Package recipe expectations against the frozen proposal's action refs."""
    try:
        world = load_world()
        selection = select_recipes(ticket, world)
        actions = get_run_actions(args, str(proposal["run_id"]))
        matrix = build_evidence_matrix(proposal, selection["primary"], actions)
        return (
            "\n--- Reviewer evidence matrix ---\n"
            "This matrix maps frozen claims to current-run action references and recipe evidence categories. "
            "It is an audit aid; validate whether the cited rows actually support each claim.\n"
            + json.dumps(matrix, default=str) + "\n"
        )
    except (OSError, RuntimeError, ValueError, KeyError, json.JSONDecodeError) as exc:
        return f"\n--- Reviewer evidence matrix ---\nUnavailable: {type(exc).__name__}: {exc}\n"


def ensure_missing_reviewers(
    args: argparse.Namespace,
    *,
    dry_run: bool = False,
    active_run_ids: Optional[set[str]] = None,
) -> int:
    tasks = list_tasks()
    active = active_run_ids if active_run_ids is not None else {
        str(row["ID"]) for row in query_active_runs(args)
    }
    created = 0
    for task in tasks:
        if task.get("status") != "done" or (task.get("assignee") or "") not in INVESTIGATOR_PROFILES:
            continue
        run_id = task_run_id(task)
        if not run_id or run_id not in active:
            continue
        if _source_has_reviewer(tasks, task["id"]) or _source_has_rework(tasks, task["id"]):
            continue
        proposal = _completion_metadata(task)
        if not _proposal_complete(proposal):
            continue
        verification_context = ""
        if not dry_run:
            route_ticket = _ticket_for_route(args, str(proposal.get("ticket_id") or task_ticket_id(task) or ""))
            verification_context = _dispatch_route_context(
                str(proposal.get("run_id") or run_id),
                str(proposal.get("ticket_id") or task_ticket_id(task) or ""),
                route_ticket, evidence_role="reviewer",
            ).replace("Deterministic live route/context", "Independent reviewer live verification context")
            verification_context += _review_evidence_context(args, proposal, route_ticket)
        if create_reviewer_card(source_task=task, proposal=proposal or {},
                                verification_context=verification_context, dry_run=dry_run):
            created += 1
    return created


# ---------------------------------------------------------------------------
# Rework/escalation
# ---------------------------------------------------------------------------

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
    return json.dumps(ledger, indent=2, default=str)[:3000]


def _escalate_run(
    args: argparse.Namespace,
    *,
    run_id: str,
    ticket_id: str,
    reason: str,
    cycle: int,
    dry_run: bool,
) -> bool:
    if dry_run:
        print(f"[DRY RUN] escalate run {run_id} after cycle {cycle}: {reason[:160]}")
        return True
    try:
        # Exhaustion is a deterministic L3 handoff, not a terminal support
        # outcome called FAILED. The publisher records the terminal response,
        # creates the L3 queue item, mirrors the human-facing note, and
        # releases WIP atomically; SQL actions remain the detailed evidence.
        handoff = {
            "schema": "chitragupta.l2.escalation-handoff.v1",
            "run_id": run_id,
            "ticket_id": ticket_id,
            "review_cycles_completed": cycle + 1,
            "reason": reason[:3000],
            "outcome": "L3_ESCALATION",
            "evidence_location": "Hermes_L2_SQL_Action_Trn_Tbl",
        }
        reply = (
            "Automated L2 did not reach an evidence-supported conclusion within its bounded "
            f"review/rework budget ({cycle + 1} cycles). A human L3 investigation has been "
            "created with the complete run audit and the specific remaining objection. "
            f"Remaining issue: {reason[:1200]}"
        )
        run_orchestrator(args, [
            "--publish-response", "--run-id", run_id, "--force-run-id",
            "--response-type", "L3_ESCALATION", "--reply-text", reply,
            "--ledger", json.dumps(handoff, separators=(",", ":")),
            "--mirror-to-support-remarks",
        ])
        _post_publish_activity(args, run_id, ticket_id, {
            "response_type": "L3_ESCALATION", "reply_text": reply,
        })
    except RuntimeError as exc:
        print(f"WARNING: escalation failed for {run_id}: {exc}")
        return False
    return True


def create_rework_card(
    args: argparse.Namespace,
    *,
    source_task: dict[str, Any],
    reason: str,
    investigation_task_id: Optional[str],
    dry_run: bool = False,
) -> Optional[str]:
    run_id, ticket_id = task_run_id(source_task), task_ticket_id(source_task)
    if not run_id or not ticket_id:
        return None
    current_cycle = task_review_cycle(source_task)
    next_cycle = current_cycle + 1
    if next_cycle >= MAX_REVIEW_CYCLES:
        return "escalated" if _escalate_run(
            args, run_id=run_id, ticket_id=ticket_id, reason=reason,
            cycle=current_cycle, dry_run=dry_run,
        ) else None

    tasks = list_tasks()
    if _source_has_rework(tasks, source_task["id"]):
        # Idempotency, not a new action: callers count any truthy return as
        # "created", so returning a truthy sentinel here inflated
        # rework_created/processed counters on every reconcile tick that
        # touched an already-covered source (confirmed live: counter kept
        # incrementing with zero new Kanban cards created).
        return None

    prior = "" if dry_run else _persist_rejected_ledger(args, investigation_task_id, run_id)
    # Rework is a fresh investigation stage.  It must receive the same compact,
    # current route evidence as an initial card rather than being pushed back
    # into schema discovery just because a reviewer rejected the first proposal.
    route_ticket = _ticket_for_route(args, ticket_id)
    route_context = _dispatch_route_context(run_id, ticket_id, route_ticket)
    ticket_no = body_field(source_task.get("body"), "ticket_no") or ticket_id
    body = (
        f"run_id: {run_id}\n"
        f"ticket_id: {ticket_id}\n"
        f"ticket_no: {ticket_no}\n"
        f"review_cycle: {next_cycle}\n"
        f"rework_source_id: {source_task['id']}\n"
        f"prior_investigation_task_id: {investigation_task_id or 'unknown'}\n"
        "pipeline_stage: rework\n"
        f"claims_contract_version: {CLAIMS_CONTRACT_VERSION}\n\n"
        f"REWORK REASON:\n{reason}\n\n"
        "Address this exact rejected/invalid point using current live evidence. Reuse prior verified "
        "findings; do not restart the entire investigation unless the objection invalidates them. "
        "Complete with the full structured metadata contract.\n"
        + route_context
        + _query_instructions(run_id, ticket_id)
    )
    if prior:
        body += f"\nPRIOR FINDINGS (verbatim):\n{prior}\n"

    argv = [
        "kanban", "create", f"REWORK[{next_cycle}]: L2 {ticket_no}",
        "--body", body,
        "--assignee", INVESTIGATOR_PROFILE,
        "--priority", str(REWORK_PRIORITY),
        "--skill", "xstudio-l2-ticket-workflow",
        "--skill", "xstudio-sql-write-discipline",
        "--idempotency-key", f"rework-{source_task['id']}",
        "--max-runtime", "20m",
        "--max-retries", "1",
        "--json",
    ]
    if dry_run:
        print(f"[DRY RUN] create rework from {source_task['id']} cycle={next_cycle}: {reason[:120]}")
        return "dry-run"
    r = run_hermes(argv)
    if r.returncode != 0:
        print(f"WARNING: rework create failed for {source_task['id']}: {r.stderr.strip()[:300]}")
        return None
    try:
        return (json.loads(r.stdout) or {}).get("id") or "created"
    except json.JSONDecodeError:
        return "created"


def process_unreviewable_completions(
    args: argparse.Namespace,
    *,
    dry_run: bool = False,
    active_run_ids: Optional[set[str]] = None,
) -> int:
    """Turn a terminal investigator packaging failure into bounded rework.

    A done investigator with a short/non-substantive summary and missing required metadata
    cannot be reviewed or published. Leaving it active forever is worse than a bounded rework,
    so this path creates the rework deterministically after normalization had a chance to salvage it.
    """
    tasks = list_tasks()
    active = active_run_ids if active_run_ids is not None else {
        str(row["ID"]) for row in query_active_runs(args)
    }
    processed = 0
    for task in tasks:
        if task.get("status") != "done" or (task.get("assignee") or "") not in INVESTIGATOR_PROFILES:
            continue
        run_id = task_run_id(task)
        if not run_id or run_id not in active:
            continue
        if _source_has_reviewer(tasks, task["id"]) or _source_has_rework(tasks, task["id"]):
            continue
        proposal = _completion_metadata(task)
        if _proposal_complete(proposal):
            continue
        reason = (
            "Investigator completion is not reviewable: required run_id/ticket_id/response_type/reply_text "
            "metadata is still incomplete after deterministic normalization. Re-package verified findings; "
            "do not invent new evidence."
        )
        if create_rework_card(
            args, source_task=task, reason=reason,
            investigation_task_id=task["id"], dry_run=dry_run,
        ):
            processed += 1
    return processed


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


def process_rejections(args: argparse.Namespace, *, dry_run: bool = False) -> int:
    processed = 0
    for task in list_tasks("blocked"):
        if (task.get("assignee") or "") not in REVIEWER_PROFILES:
            continue
        run_id = task_run_id(task)
        if not run_id or not safe_query_active_run(run_id, args):
            continue
        # A rework created from this exact review task is the durable idempotency marker.
        if _source_has_rework(list_tasks(), task["id"]):
            continue
        reason = reviewer_block_reason(task)
        investigation_task_id = body_field(task.get("body"), "investigation_task_id")
        if create_rework_card(
            args, source_task=task, reason=reason,
            investigation_task_id=investigation_task_id, dry_run=dry_run,
        ):
            processed += 1
    return processed


# ---------------------------------------------------------------------------
# Approval / publish
# ---------------------------------------------------------------------------

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
    # No automatic solution-article creation here. A resolved incident is episodic
    # history; KB promotion/dedupe is governed by Knowledge/KB_IMPLEMENTATION_PLAN.md.


def publication_ledger(proposal: dict[str, Any], reviewer_task: dict[str, Any]) -> dict[str, Any]:
    """Persist the immutable review payload alongside the published response.

    Tool-level provenance remains in Hermes_L2_SQL_Action_Trn_Tbl. This compact
    run-level record makes the exact material claims and their action IDs visible
    from Helpdesk without treating a mutable Kanban card as the only audit copy.
    """
    return {
        "schema": "chitragupta.l2.frozen-proposal.v1",
        "review_task_id": reviewer_task.get("id"),
        "review_cycle": task_review_cycle(reviewer_task),
        "review_decision": "APPROVED",
        "claims_contract_version": proposal.get("claims_contract_version"),
        "frozen_proposal": proposal,
    }


def process_approvals(args: argparse.Namespace, *, dry_run: bool = False) -> dict[str, int]:
    binding = load_workflow_binding()
    counts = {"published": 0, "blocked_configuration": 0, "rework_created": 0}
    active = {str(row["ID"]) for row in query_active_runs(args)}

    for task in list_tasks("done"):
        if (task.get("assignee") or "") not in REVIEWER_PROFILES:
            continue
        run_id, ticket_id = task_run_id(task), task_ticket_id(task)
        if run_id not in active or not ticket_id:
            continue

        state = _query_published_state(args, run_id)
        if state and state[0].get("ProcessStatus") in ("COMPLETED", "WAITING_USER") and state[0].get("ReplyText"):
            continue
        if not safe_query_active_run(run_id, args):
            # Old done reviewer for a run already failed/reclaimed. Do not resurrect it.
            continue

        proposal = task_proposal(task)
        if not _proposal_complete(proposal):
            # Reviewer should never have been created without a frozen complete proposal in
            # the new topology. Legacy/pre-migration cards may violate that; bounded rework
            # is safer than publishing reconstructed prose.
            reason = "Reviewer reached done but its frozen proposal_json is missing/incomplete; re-package the original verified finding through a fresh investigation/review cycle."
            source_id = body_field(task.get("body"), "investigation_task_id")
            if create_rework_card(
                args, source_task=task, reason=reason,
                investigation_task_id=source_id, dry_run=dry_run,
            ):
                counts["rework_created"] += 1
            continue

        # Structural claim/evidence gate. If the proposal carries a claims array,
        # every material VERIFIED claim must have an evidence reference. This is a
        # deterministic structural check, not semantic judgment (that stays with the
        # reviewer). Legacy proposals without claims pass through normally.
        proposal_claims = proposal.get("claims") if proposal else None
        claims_required = proposal.get("claims_contract_version") == CLAIMS_CONTRACT_VERSION if proposal else False
        if claims_required or proposal_claims is not None:
            claims_valid, claims_issues = validate_claims_contract(
                proposal_claims, run_id=run_id, ticket_id=ticket_id,
                actions=get_run_actions(args, run_id),
            )
            if not claims_valid:
                reason = (
                    "Pre-publish claim/evidence gate: " + "; ".join(claims_issues[:5])
                    + ". Fix the material claim evidence references and resubmit."
                )
                source_id = body_field(task.get("body"), "investigation_task_id")
                if create_rework_card(
                    args, source_task=task, reason=reason,
                    investigation_task_id=source_id, dry_run=dry_run,
                ):
                    counts["rework_created"] += 1
                continue

        response_type = str(proposal["response_type"]).upper()
        try:
            workflow_args, expected_status = _status_args_for_response(binding, proposal)
        except RuntimeError as exc:
            # Deployment binding is a harness configuration problem, not an investigator
            # defect. Keep the run active and visible; global WIP prevents new claims until
            # the operator fixes the binding, then the same reconciler publishes it.
            print(f"PUBLISH BLOCKED for run {run_id}: {exc}")
            counts["blocked_configuration"] += 1
            continue

        cmd = [
            "--publish-response", "--run-id", run_id, "--force-run-id",
            "--response-type", response_type,
            "--reply-text", str(proposal["reply_text"]),
            "--approval-status", "APPROVED",
            "--mirror-to-support-remarks",
            "--ledger", json.dumps(publication_ledger(proposal, task), separators=(",", ":"), default=str),
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
            if proposal.get(key):
                cmd += [flag, str(proposal[key])]

        if dry_run:
            print(f"[DRY RUN] publish reviewer {task['id']} run={run_id} type={response_type} status={expected_status}")
            counts["published"] += 1
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
        if row.get("ProcessStatus") not in ("COMPLETED", "WAITING_USER") or not str(row.get("ReplyText") or "").strip():
            print(f"WARNING: publish postcondition failed for {run_id}: {row}")
            continue
        if expected_status and row.get("TicketStatus") != expected_status:
            print(f"WARNING: Helpdesk status postcondition failed for {run_id}: expected {expected_status!r}, got {row.get('TicketStatus')!r}")
            continue

        _post_publish_activity(args, run_id, ticket_id, proposal)
        counts["published"] += 1

    return counts


# ---------------------------------------------------------------------------
# Recovery / audit
# ---------------------------------------------------------------------------

def recover_orphan_runs(
    args: argparse.Namespace,
    *,
    dry_run: bool = False,
    stale_after_minutes: int = ORPHAN_GRACE_MINUTES,
) -> int:
    # Any Kanban card referencing the run protects it, regardless of status. This covers
    # ready/running/blocked work and a done reviewer awaiting deterministic publication.
    tasks = list_tasks()
    referenced_run_ids = {task_run_id(t) for t in tasks if task_run_id(t)}
    active_rows = query_active_runs(args)
    # A pipeline-owned card is enough to prove that an active run is not an
    # orphan. Only the rare remaining candidates require the expensive board-wide
    # lookup needed to honour manually-created cards as well.
    unresolved = [
        str(row.get("ID") or "") for row in active_rows
        if str(row.get("ID") or "") and str(row.get("ID") or "") not in referenced_run_ids
    ]
    if unresolved:
        try:
            all_tasks = list_all_tasks()
        except RuntimeError as exc:
            print(f"WARNING: full Kanban orphan check unavailable: {exc}")
            return 0
        referenced_run_ids = {task_run_id(t) for t in all_tasks if task_run_id(t)}
    recovered = 0
    for row in active_rows:
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
            print(f"[DRY RUN] fail true orphan run {run_id} age={age}m")
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
    """Read-only divergence count for reviewer-done vs SQL truth.

    The older audit wrote the same comment every cron tick and also inspected investigator
    cards. Reconciliation is now the repair mechanism; audit only reports reviewer divergence.
    """
    false_positives = 0
    for task in list_tasks("done"):
        if (task.get("assignee") or "") not in REVIEWER_PROFILES:
            continue
        run_id = task_run_id(task)
        if not run_id:
            continue
        rows = _query_published_state(args, run_id)
        ok = bool(
            rows
            and rows[0].get("ProcessStatus") in ("COMPLETED", "WAITING_USER")
            and rows[0].get("ResponseType")
            and str(rows[0].get("ReplyText") or "").strip()
        )
        if not ok:
            false_positives += 1
            print(f"{'[DRY RUN] ' if dry_run else ''}REVIEW/SQL DIVERGENCE task={task['id']} run={run_id}")
    return false_positives


# ---------------------------------------------------------------------------
# Reconciliation (ordering is a correctness contract)
# ---------------------------------------------------------------------------

def reconcile(args: argparse.Namespace, *, dry_run: bool = False) -> dict[str, Any]:
    # Synchronous ordering removes the old Popen race (publisher reading metadata before
    # repair completed). Reviewers do not exist until normalization/unreviewable handling
    # has finished for their source completion.
    failed_workers = recover_failed_workers(args, dry_run=dry_run)
    active = {str(row["ID"]) for row in query_active_runs(args)}
    normalized = normalize_investigator_completions(dry_run=dry_run, active_run_ids=active)
    unreviewable = process_unreviewable_completions(
        args, dry_run=dry_run, active_run_ids=active,
    )
    reviewers = ensure_missing_reviewers(args, dry_run=dry_run, active_run_ids=active)
    rejections = process_rejections(args, dry_run=dry_run)
    approvals = process_approvals(args, dry_run=dry_run)
    orphans = recover_orphan_runs(
        args, dry_run=dry_run, stale_after_minutes=args.stale_after_minutes,
    )
    return {
        "failed_workers_reworked": failed_workers,
        "normalized": normalized,
        "unreviewable_reworked": unreviewable,
        "reviewers_created": reviewers,
        "rejections_processed": rejections,
        "approvals": approvals,
        "orphans_recovered": orphans,
    }


def recover_failed_workers(args: argparse.Namespace, *, dry_run: bool = False) -> int:
    """Recover terminal worker failures, never a merely old/live task.

    Hermes owns process termination. Only a blocked card whose latest attempt
    has ended is eligible. Fresh rework retains the same SQL run and advances
    the existing bounded review cycle instead of resetting the retry budget.
    """
    tasks = list_tasks()
    active = {str(row["ID"]) for row in query_active_runs(args)}
    recovered = 0
    health_checked = False
    for task in tasks:
        if task.get("status") != "blocked":
            continue
        if task.get("assignee") not in INVESTIGATOR_PROFILES | REVIEWER_PROFILES:
            continue
        if task_run_id(task) not in active or _source_has_rework(tasks, task["id"]):
            continue
        attempts = get_runs(task["id"])
        if not attempts or any(r.get("status") == "running" for r in attempts):
            continue
        latest = attempts[-1]
        if latest.get("status") not in {"crashed", "timed_out", "failed", "gave_up"}:
            continue
        if not latest.get("ended_at"):
            continue
        if not dry_run and not health_checked:
            check_worker_dependencies()
            health_checked = True
        reason = "Worker infrastructure failure: " + str(latest.get("error") or latest["status"])
        source_id = body_field(task.get("body"), "investigation_task_id") or task["id"]
        if create_rework_card(args, source_task=task, reason=reason,
                              investigation_task_id=source_id, dry_run=dry_run):
            recovered += 1
    return recovered


def check_worker_dependencies() -> None:
    """Exercise the configured worker transport/model before consuming work.

    Probe output is synthetic and never written to a ticket. Dependency failure
    stops the scout/recovery tick; its next scheduled invocation probes again.
    """
    import urllib.request
    import yaml
    bridge = REPO_ROOT_WSL / "Model_Bench" / "xstudio_l2_tool_bridge.py"
    probe = subprocess.run([sys.executable, str(bridge)],
        input=json.dumps({"operation": "query", "database": DEFAULT_DATABASE,
                          "sql": "SELECT 1 AS Healthy"}),
        capture_output=True, text=True, timeout=25)
    if probe.returncode or not json.loads(probe.stdout).get("ok"):
        raise RuntimeError("WORKER_DEPENDENCY_UNAVAILABLE: typed SQL probe failed; claims paused")
    checked = set()
    for profile in (INVESTIGATOR_PROFILE, REVIEWER_PROFILE):
        config_path = Path.home() / ".hermes" / "profiles" / profile / "config.yaml"
        config = yaml.safe_load(config_path.read_text())
        toolsets = config.get("platform_toolsets", {}).get("cli", [])
        if not {"xstudio_l2", "kanban"}.issubset(toolsets):
            raise RuntimeError(f"WORKER_DEPENDENCY_UNAVAILABLE: required tools absent in {profile}")
        model = config["model"]
        key = (model["base_url"], model["default"])
        if key in checked:
            continue
        payload = {"model": key[1], "max_tokens": 256, "temperature": 0,
            "messages": [{"role": "user", "content": "Call l2_health with operation ping."}],
            "tools": [{"type": "function", "function": {"name": "l2_health",
                "description": "Synthetic health probe", "parameters": {"type": "object",
                "properties": {"operation": {"type": "string", "enum": ["ping"]}},
                "required": ["operation"]}}}],
            "tool_choice": "required"}
        req = urllib.request.Request(key[0].rstrip("/") + "/chat/completions",
            data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=25) as response:
            data = json.load(response)
        calls = data["choices"][0]["message"].get("tool_calls", [])
        if not calls or calls[0]["function"]["name"] != "l2_health" or json.loads(calls[0]["function"]["arguments"]).get("operation") != "ping":
            raise RuntimeError("WORKER_DEPENDENCY_UNAVAILABLE: model tool-call probe failed; claims paused")
        checked.add(key)


def check_gbrain_dependency(args: argparse.Namespace) -> None:
    result = subprocess.run([_orch_python(), _kb_retriever_path(), "--check-gbrain"],
                            capture_output=True, text=True, timeout=30)
    if result.returncode:
        detail = (result.stderr or result.stdout).strip()[:300]
        raise RuntimeError("WORKER_DEPENDENCY_UNAVAILABLE: GBrain knowledge is not ready: " + detail)


# ---------------------------------------------------------------------------
# Investigation bundle / claim
# ---------------------------------------------------------------------------

def _run_kb_retrieval(args: argparse.Namespace, ticket: dict[str, Any]) -> dict[str, Any]:
    # PRE_INVESTIGATION query is requester-grounded. Deliberately exclude the
    # model/L1-generated SuspectedCause so a hypothesis cannot retrieve its own confirmation.
    query = " ".join(str(ticket.get(k) or "") for k in (
        "BriefDetails", "Description", "ProblemCategory", "HermesAreaName", "ExtractedEntitiesJson"
    )).strip()
    if not query:
        return {"solutions": [], "abstained": True, "abstention_reason": "Ticket contains no searchable problem text."}

    cmd = [
        _orch_python(), _kb_retriever_path(),
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
    # Orchestrator still has the old route-only solution lookup for compatibility. Never expose
    # two competing KB paths to the worker.
    bundle.pop("known_solutions", None)
    kb = _run_kb_retrieval(args, fallback_ticket)
    ticket_context = bundle.get("ticket") if isinstance(bundle.get("ticket"), dict) else {}
    live_ticket = ticket_context.get("ticket") if isinstance(ticket_context.get("ticket"), dict) else fallback_ticket
    ticket_fields = (
        "ID", "TicketNo", "AreaID", "BriefDetails", "Description", "ProblemCategory",
        "SourceSystem", "ConversationSummary", "ExtractedEntitiesJson", "HermesAreaName",
        "HermesComplaintTypeName", "HermesPriorityName",
    )
    prior_runs = ticket_context.get("prior_runs") if isinstance(ticket_context, dict) else []
    compact = {
        "ticket": {key: live_ticket.get(key) for key in ticket_fields if live_ticket.get(key) is not None},
        "prior_attempts": [
            {key: row.get(key) for key in ("ID", "ProcessStatus", "ResponseType", "ReplyText", "ErrorMessage", "ClaimedOn")
             if row.get(key) not in (None, "")}
            for row in list(prior_runs or [])[:3]
        ],
        "prior_ledger": bundle.get("prior_ledger"),
        "suggested_tables": [
            {key: row.get(key) for key in ("table", "database", "matched_columns") if row.get(key) is not None}
            for row in list(bundle.get("suggested_tables") or [])[:3]
        ],
        "kb": {
            "solutions": list(kb.get("solutions") or [])[:2],
            "route_candidates": list(kb.get("route_candidates") or [])[:2],
            "gbrain": {
                "status": (kb.get("gbrain") or {}).get("status"),
                "source_id": (kb.get("gbrain") or {}).get("source_id"),
                "hits": [{key: hit.get(key) for key in ("kb_id", "source_ref", "title", "excerpt", "retrieval_score", "verification_required")
                          if hit.get(key) is not None} for hit in list((kb.get("gbrain") or {}).get("hits") or [])[:3]],
                "abstained": (kb.get("gbrain") or {}).get("abstained"),
                "abstention_reason": (kb.get("gbrain") or {}).get("abstention_reason"),
            },
            "abstained": kb.get("abstained"),
            "abstention_reason": kb.get("abstention_reason"),
        },
    }
    rendered = json.dumps(compact, indent=2, default=str)
    if len(rendered) > 8000:
        rendered = rendered[:8000] + "\n... [bundle truncated at 8,000 chars]"
    return (
        "\n--- Investigation bundle (single dispatch-time package) ---\n"
        "KB/GBrain hits, prior findings, relationships, and suggested tables are leads, not ticket proof. Use source_ref for provenance. Material current claims still require current audited SQL evidence.\n"
        f"{rendered}\n"
    )


def _ticket_for_route(args: argparse.Namespace, ticket_id: str) -> dict[str, Any]:
    """Read just the authoritative ticket row needed for a rework route.

    A rejected card deliberately contains only frozen prior findings.  Fetching
    the live Helpdesk ticket here keeps rework routing current without making a
    model spend a tool call or trusting the old card body.
    """
    try:
        context = run_orchestrator(args, ["--get-ticket-context", ticket_id])
    except RuntimeError:
        return {}
    if not isinstance(context, dict):
        return {}
    ticket = context.get("ticket")
    return ticket if isinstance(ticket, dict) else context


def deterministic_ticket_route(ticket: dict[str, Any]) -> dict[str, Any]:
    """Extract a small, auditable first evidence path from ticket-owned fields."""
    entities: dict[str, Any] = {}
    raw_entities = ticket.get("ExtractedEntitiesJson")
    if isinstance(raw_entities, dict):
        entities = raw_entities
    elif raw_entities:
        try:
            parsed = json.loads(str(raw_entities))
            entities = parsed if isinstance(parsed, dict) else {}
        except json.JSONDecodeError:
            entities = {}
    category = str(ticket.get("ProblemCategory") or "").upper()
    summary = " ".join(str(ticket.get(key) or "") for key in (
        "BriefDetails", "Description", "ConversationSummary"
    ))
    normalized_text = re.sub(r"[^A-Z0-9]+", " ", (category + " " + summary).upper())
    api_types = (
        (("WORK ORDER", "PROCESS ORDER"), "WorkOrderCreation"),
        (("BATCH CHARACTERISTIC",), "BatchCharacteristics"),
        (("BATCH CREATION",), "BatchCreation"),
        (("RESULT RECORDING",), "ResultRecording"),
        (("USAGE DECISION",), "UsageDecision"),
        (("INVENTORY", "STORAGE LOCATION"), "Inventory"),
        (("CONSUMPTION",), "Consumption"),
        (("BY PRODUCT", "BYPRODUCT"), "ByProduct"),
        (("REVERSAL",), "Reversal"),
        (("PRODUCTION",), "Production"),
    )
    explicit_api = "API" in normalized_text or "SAP INTEGRATION" in normalized_text
    if explicit_api:
        api_type = next((value for phrases, value in api_types if any(p in normalized_text for p in phrases)), None)
        if api_type:
            identifier = next((entities.get(key) for key in (
                "Batch", "BatchNo", "SAPTransactionID", "TransactionID", "InspectionLot",
                "ManufacturingOrder", "WorkOrderNumber", "HeatNo",
            ) if entities.get(key) not in (None, "")), None)
            return {
                "domain": "sap_api", "api_type": api_type,
                "identifier": str(identifier) if identifier is not None else None,
                "recommended_tool": "xstudio_sap_api_context",
                "reason": "The ticket explicitly asks about a reviewed SAP API family; route directly to its live diagnostic.",
            }

    work_order = next((entities.get(key) for key in (
        "WorkOrderNumber", "WorkOrder", "ManufacturingOrder", "MESWorkOrderNumber"
    ) if entities.get(key) not in (None, "")), None)
    if work_order is None:
        match = re.search(r"\b(?:work\s*order|wo)\s*[:#-]?\s*([A-Z0-9][A-Z0-9_.-]{2,99})\b", summary, re.I)
        work_order = match.group(1) if match else None
    campaign = next((entities.get(key) for key in ("CampaignNo", "Campaign")
                     if entities.get(key) not in (None, "")), None)
    if campaign is None:
        match = re.search(r"\bcampaign\s*[:#-]?\s*([A-Z0-9][A-Z0-9_.-]{2,99})\b", summary, re.I)
        campaign = match.group(1) if match else None
    if work_order and re.fullmatch(r"[A-Za-z0-9_.-]{1,100}", str(work_order)):
        return {
            "domain": "work_order", "work_order": str(work_order),
            "campaign": str(campaign) if campaign else None,
            "recommended_tool": "xstudio_work_order_context",
            "reason": "Work-order and campaign identifiers route directly to canonical fixed live projections.",
        }

    raw_heat = next((entities.get(key) for key in ("HeatNo", "HeatID", "Heat") if entities.get(key) is not None), None)
    if raw_heat is None:
        match = re.search(r"\bheat\s+(?:H\s*)?(\d{4,})\b", summary, re.I)
        raw_heat = match.group(1) if match else None
    heat_match = re.fullmatch(r"\s*[Hh]?(\d+)\s*", str(raw_heat or ""))
    if not heat_match:
        return {"domain": "generic", "recommended_tool": None, "reason": "No unambiguous numeric heat identifier."}
    sap = "SAP" in category or "SAP" in summary.upper()
    billet = "BILLET" in category or "BILLET" in summary.upper() or "STRAND" in summary.upper()
    return {
        "domain": "heat_sap" if sap else ("billet_genealogy" if billet else "heat_execution"),
        "heat": heat_match.group(1),
        "recommended_tool": "xstudio_heat_context",
        "reason": "Canonical EAF/LRF/CCM, billet genealogy, work-order and SAP production surfaces are harness-routed for this heat.",
    }


def _dispatch_route_context(run_id: str, ticket_id: str, ticket: dict[str, Any],
                            *, evidence_role: str = "investigator") -> str:
    """Collect the smallest deterministic live evidence package before dispatch.

    This is a trusted harness call, not model-generated SQL. It records the
    same per-surface action rows as the named tool and gives the investigator a
    bounded first read instead of making Qwen rediscover stable joins.
    """
    route = deterministic_ticket_route(ticket)
    rendered: dict[str, Any] = {"route": route}
    if route.get("recommended_tool") == "xstudio_heat_context":
        bridge = REPO_ROOT_WSL / "Model_Bench" / "xstudio_l2_tool_bridge.py"
        request = {"operation": "heat_context", "database": "XStudio_Xbatch",
                   "run_id": run_id, "ticket_id": ticket_id, "heat": route["heat"],
                   "evidence_role": evidence_role}
        try:
            result = subprocess.run([sys.executable, str(bridge)], input=json.dumps(request),
                                    capture_output=True, text=True, timeout=45)
            if result.returncode:
                raise RuntimeError(result.stderr.strip() or f"bridge exit {result.returncode}")
            rendered["live_context"] = json.loads(result.stdout)
        except (OSError, subprocess.TimeoutExpired, RuntimeError, json.JSONDecodeError) as exc:
            rendered["live_context_warning"] = f"Deterministic heat context unavailable: {type(exc).__name__}: {exc}"
    elif route.get("recommended_tool") == "xstudio_sap_api_context":
        bridge = REPO_ROOT_WSL / "Model_Bench" / "xstudio_l2_tool_bridge.py"
        request = {"operation": "sap_api_context", "database": "XStudio_Xbatch",
                   "run_id": run_id, "ticket_id": ticket_id, "api_type": route["api_type"],
                   "evidence_role": evidence_role}
        if route.get("identifier"):
            request["identifier"] = route["identifier"]
        try:
            result = subprocess.run([sys.executable, str(bridge)], input=json.dumps(request),
                                    capture_output=True, text=True, timeout=45)
            if result.returncode:
                raise RuntimeError(result.stderr.strip() or f"bridge exit {result.returncode}")
            rendered["live_context"] = json.loads(result.stdout)
        except (OSError, subprocess.TimeoutExpired, RuntimeError, json.JSONDecodeError) as exc:
            rendered["live_context_warning"] = f"Deterministic SAP API context unavailable: {type(exc).__name__}: {exc}"
    elif route.get("recommended_tool") == "xstudio_work_order_context":
        bridge = REPO_ROOT_WSL / "Model_Bench" / "xstudio_l2_tool_bridge.py"
        request = {"operation": "work_order_context", "database": "XStudio_Xbatch",
                   "run_id": run_id, "ticket_id": ticket_id,
                   "work_order": route["work_order"], "evidence_role": evidence_role}
        if route.get("campaign"):
            request["campaign"] = route["campaign"]
        try:
            result = subprocess.run([sys.executable, str(bridge)], input=json.dumps(request),
                                    capture_output=True, text=True, timeout=45)
            if result.returncode:
                raise RuntimeError(result.stderr.strip() or f"bridge exit {result.returncode}")
            rendered["live_context"] = json.loads(result.stdout)
        except (OSError, subprocess.TimeoutExpired, RuntimeError, json.JSONDecodeError) as exc:
            rendered["live_context_warning"] = f"Deterministic work-order context unavailable: {type(exc).__name__}: {exc}"
    try:
        world = load_world()
        selection = select_recipes(ticket, world)
        rendered["world_knowledge"] = world_context(selection, world, max_chars=2500)
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        rendered["world_knowledge_warning"] = f"World knowledge unavailable: {type(exc).__name__}: {exc}"
    text = json.dumps(rendered, indent=2, default=str)
    if len(text) > 9000:
        text = text[:9000] + "\n... [route/world context truncated at 9,000 chars]"
    return (
        "\n--- Deterministic live route/context ---\n"
        "This is current live evidence collected by the harness. Interpret only the returned rows; "
        "use the evidence_refs action IDs for VERIFIED claims. Absence does not establish causation.\n"
        f"{text}\n"
    )


def _query_instructions(run_id: str, ticket_id: str) -> str:
    """Render the typed-tool investigation contract for a fresh card body.

    This deliberately renders NO interpreter path, script path, or shell
    command. Ticket_424/Ticket_441 proved that handing a small local model a
    raw `python.exe ... Hermes_Orchestrator.py` recipe invites it to rebuild
    the transport itself, malform it, and then burn the whole context window
    retrying wrappers and `pip install pyodbc`. Transport is harness-owned and
    reachable only through the guarded named `xstudio_*` tools.
    """
    return (
        "\n--- Typed XStudio investigation contract ---\n"
        "Use only the named xstudio_* tools in the xstudio_l2 toolset for ALL XStudio/Helpdesk database, schema, ticket, "
        "run-audit and ledger work. The harness owns Windows/WSL transport, Python, "
        "pyodbc, credentials, auditing, output limits and retry guards.\n"
        f"Current run_id: {run_id}\nCurrent ticket_id: {ticket_id}\n"
        "The starting bundle and deterministic live route/context are already above; do not refetch them.\n\n"
        "Tools:\n"
        "  xstudio_select(database,table,columns,where?,order_by?,top?)\n"
        "  xstudio_query(database,sql)\n"
        "  xstudio_suggest_tables(database,search)\n"
        "  xstudio_find_objects(database,search,object_type?,schema?)\n"
        "  xstudio_get_definition(database,object_name,schema?)\n"
        "  xstudio_validate_identifiers(database,table,identifiers?)\n"
        "  xstudio_read_procedure(database,procedure,parameters,run_id?)\n"
        "  xstudio_resolve_heat(heat,database?)\n"
        "  xstudio_get_ticket_context(ticket_id?)\n"
        "  xstudio_get_run_actions(run_id?)\n"
        "  xstudio_save_ledger(ledger,run_id?)\n"
        "  xstudio_heat_context(heat) — first choice for a heat/SAP/work-order/billet ticket\n"
        "  xstudio_sap_api_context(api_type) — live API summary when whether an API ran matters\n"
        "  xstudio_work_order_context(work_order,campaign?) — canonical work-order/campaign state\n"
        "The harness injects the current run_id/ticket_id when safely known and defaults resolve_heat to XStudio_Xbatch.\n"
        "Pass database explicitly: XStudio_Helpdesk for ticket/Hermes runtime data, "
        "XStudio_Xbatch for production/heat/billet/quality/delay/SAP data.\n"
        "There is no shell path to the database. Do not use terminal to reach SQL, to run "
        "an interpreter, to import a database driver, or to install packages -- those are "
        "blocked by the harness and will waste your budget. Do not retry an identical "
        "failing call with wrappers or timeouts; correct its typed arguments or change the "
        "evidence path. If a result is truncated, narrow the query rather than repeating it.\n"
        "A ticket/user identifier is not proof of database storage representation. If a material "
        "fact is not established before the tool budget ends, report Evidence status: INCOMPLETE "
        "and list the missing evidence; do not call it verified.\n"
        "Before completing, identify material claims and label each VERIFIED/INFERRED/"
        "UNVERIFIED/CONTRADICTED. Include claims_contract_version=1 and a claims array in metadata; "
        "each material VERIFIED claim needs evidence [{action_id:<Hermes action ID>}]. Context tools return refs; otherwise use xstudio_get_run_actions. Absence of records is evidence of absence, "
        "not evidence of causation.\n"
        "Never write the live ticket directly. Complete the Kanban task with full "
        "structured metadata; deterministic review/publish owns the rest.\n"
    )


def _archive_stale_cards_for_ticket(ticket_id: str, new_run_id: str) -> None:
    # Only archive stale queued cards from OLD runs; completed/blocked history is useful
    # provenance and also prevents topology re-creation if Hermes lists those states.
    stale_statuses = {"todo", "ready", "triage", "scheduled"}
    try:
        tasks = list_tasks()
    except RuntimeError:
        return
    stale = [
        t["id"] for t in tasks
        if t.get("status") in stale_statuses
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

    # A configuration error should stop NEW work, not reconciliation of already-claimed work.
    binding = load_workflow_binding()
    ready, reason = _binding_ready_for_claims(binding)
    if not ready:
        return {
            "status": "WORKFLOW_BINDING_NOT_READY",
            "reason": reason,
            "binding_path": binding.get("_path"),
            "reconcile": reconciliation,
        }

    # Global WIP=1. Existing work always wins over a new claim.
    active = query_active_runs(args)
    if active:
        return {"status": "WIP_LIMIT", "active_runs": active, "reconcile": reconciliation}

    check_worker_dependencies()
    check_gbrain_dependency(args)

    eligible = str(binding.get("eligible_ticket_status") or args.eligible_status or DEFAULT_ELIGIBLE_STATUS)
    poll = run_orchestrator(
        args,
        ["--poll", "--eligible-status", eligible, "--bot-label", INVESTIGATOR_PROFILE],
        timeout=90,
    )
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
        f"claims_contract_version: {CLAIMS_CONTRACT_VERSION}\n"
        "pipeline_stage: investigation\n"
        + _investigation_bundle(args, ticket_id, ticket)
        + _dispatch_route_context(run_id, ticket_id, ticket)
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
        "--max-retries", "1",
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
        # Kanban creation may actually have succeeded, so do not create an untracked duplicate.
        # The active SQL run remains protected; next reconciliation/status makes the mismatch visible.
        raise RuntimeError("investigator task was created but its id could not be parsed")

    # No reviewer is pre-created. The completion hook/scout reconciler first normalizes the
    # investigator's result, then freezes that exact proposal into a new high-priority reviewer.
    return {
        "status": "CLAIMED",
        "run_id": run_id,
        "ticket_id": ticket_id,
        "investigator_task_id": investigator_id,
        "reviewer_task_id": None,
        "reviewer_creation": "deferred_until_normalized_completion",
        "priorities": {
            "investigation": NEW_INVESTIGATION_PRIORITY,
            "rework": REWORK_PRIORITY,
            "review": REVIEW_PRIORITY,
        },
        "reconcile": reconciliation,
    }


# ---------------------------------------------------------------------------
# Status / diagnosis
# ---------------------------------------------------------------------------

def pipeline_status(args: argparse.Namespace) -> dict[str, Any]:
    tasks = list_tasks()
    active = query_active_runs(args)
    by_run: dict[str, list[dict[str, Any]]] = {}
    for task in tasks:
        rid = task_run_id(task)
        if not rid:
            continue
        by_run.setdefault(rid, []).append({
            "id": task.get("id"),
            "title": task.get("title"),
            "status": task.get("status"),
            "assignee": task.get("assignee"),
            "pipeline_stage": body_field(task.get("body"), "pipeline_stage"),
            "review_cycle": task_review_cycle(task),
            "source": body_field(task.get("body"), "investigation_task_id") or body_field(task.get("body"), "rework_source_id"),
        })

    anomalies: list[dict[str, Any]] = []
    for row in active:
        rid = str(row.get("ID"))
        owned = by_run.get(rid, [])
        if not owned:
            anomalies.append({"run_id": rid, "type": "ACTIVE_SQL_WITH_NO_KANBAN"})
            continue

        investigators = [t for t in owned if t.get("assignee") in INVESTIGATOR_PROFILES]
        reviewers = [t for t in owned if t.get("assignee") in REVIEWER_PROFILES]
        if not investigators:
            anomalies.append({"run_id": rid, "type": "ACTIVE_RUN_WITHOUT_INVESTIGATOR_CARD"})
        if investigators and not reviewers and all(t.get("status") == "done" for t in investigators):
            # Could be a transient between completion and next reconcile, but it should never
            # persist across a scout tick.
            anomalies.append({"run_id": rid, "type": "DONE_INVESTIGATION_WITHOUT_REVIEWER_OR_REWORK"})
        if any(t.get("status") == "done" for t in reviewers):
            anomalies.append({"run_id": rid, "type": "REVIEW_APPROVED_PUBLISH_PENDING_OR_BLOCKED"})
        if any(t.get("status") == "blocked" for t in reviewers):
            anomalies.append({"run_id": rid, "type": "REVIEW_REJECTED_REWORK_PENDING_OR_ACTIVE"})

    binding = load_workflow_binding()
    binding_ready, binding_reason = _binding_ready_for_claims(binding)
    return {
        "active_runs": active,
        "tasks_by_run": by_run,
        "anomalies": anomalies,
        "binding": binding,
        "binding_ready_for_new_claims": binding_ready,
        "binding_block_reason": binding_reason,
        "contract": {
            "max_pipeline_wip": 1,
            "priorities": {
                "review": REVIEW_PRIORITY,
                "rework": REWORK_PRIORITY,
                "new_investigation": NEW_INVESTIGATION_PRIORITY,
            },
            "max_review_cycles": MAX_REVIEW_CYCLES,
            "reviewer_creation": "after_normalized_investigator_completion",
            "frozen_review_proposal": True,
        },
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

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


@contextmanager
def lifecycle_lock(args: argparse.Namespace):
    """One process owns mutations across scout, hooks and operator commands."""
    if args.dry_run or args.mode in {"status", "audit"}:
        yield
        return
    if _is_windows():
        raise RuntimeError("Lifecycle mutation must run in the configured WSL service environment so it shares the lifecycle lock")
    import fcntl
    path = Path.home() / ".hermes" / "plugin-data" / "xstudio-l2-orchestrator" / "lifecycle.lock"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a+") as handle:
        try:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise RuntimeError("LIFECYCLE_BUSY: another reconciler owns mutations; next scout tick will retry") from exc
        try:
            yield
        finally:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def cli(argv: Optional[list[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        with lifecycle_lock(args):
            return _cli_owned(argv)
    except Exception as exc:
        print(json.dumps({"ok": False, "error": f"{type(exc).__name__}: {exc}"}))
        return 1


def _cli_owned(argv: Optional[list[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.mode == "scout":
            result = scout(args, dry_run=args.dry_run)
        elif args.mode == "reconcile":
            result = reconcile(args, dry_run=args.dry_run)
        elif args.mode == "repair":
            result = {
                "normalized": normalize_investigator_completions(dry_run=args.dry_run),
                "unreviewable_reworked": process_unreviewable_completions(args, dry_run=args.dry_run),
                "reviewers_created": ensure_missing_reviewers(args, dry_run=args.dry_run),
            }
        elif args.mode == "publish":
            result = process_approvals(args, dry_run=args.dry_run)
        elif args.mode == "reject":
            result = {"rejections_processed": process_rejections(args, dry_run=args.dry_run)}
        elif args.mode == "recover":
            result = {"orphans_recovered": recover_orphan_runs(
                args, dry_run=args.dry_run, stale_after_minutes=args.stale_after_minutes,
            )}
        elif args.mode == "audit":
            result = {"review_sql_divergences": audit_done_reviewers(args, dry_run=args.dry_run)}
        else:
            result = pipeline_status(args)
    except Exception as exc:
        print(json.dumps({"ok": False, "error": f"{type(exc).__name__}: {exc}"}, default=str))
        return 1
    print(json.dumps({"ok": True, "mode": args.mode, "result": result}, indent=2, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(cli())
