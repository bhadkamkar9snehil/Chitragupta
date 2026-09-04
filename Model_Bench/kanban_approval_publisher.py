#!/usr/bin/env python3
"""Deterministic, no-LLM publisher: performs the real --publish-response
call for every reviewer approval, so the write is never in the model's
hands at all.

Why this exists: confirmed 2026-09-03 that the reviewer role called
`--publish-response` in 0 of 6 real completions in a row, across two
rounds of skill-text fixes emphasizing it as strongly as language allows.
Researched properly before concluding this: LM Studio does not support
forcing a specific named tool call (only a blunt "call something"), and
true forced-sequencing (grammar-constrained decoding) isn't exposed by
this stack. So the reviewer skill was changed to do judgment ONLY --
kanban_complete(summary="APPROVE: ...") or kanban_request_changes(...) --
and this script does the actual database write outside the model's
control entirely, using the ORIGINAL INVESTIGATOR's own recorded
review-request metadata (response_type, reply_text, etc.), not anything
the reviewer re-typed.

What this does, every tick:
1. Find every kanban task marked 'done' under a *-verifier assignee whose
   kanban_complete summary starts with "APPROVE" (the required format the
   reviewer skill now enforces).
2. For each, walk its run history to find the investigator's own
   'review_requested' entry and pull its metadata (run_id, response_type,
   reply_text, etc.) -- this is the real content to publish, not anything
   the reviewer said.
3. Call Hermes_Orchestrator.py --publish-response --force-run-id with
   that exact data.
4. Track which tasks have already been processed (a local state file) so
   a task is never double-published on a later tick.

Usage (intended as a --no-agent cron job, every ~3-5 min):
    python kanban_approval_publisher.py --server 10.2.6.204 [--dry-run]
"""
import os
import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

STATE_PATH = Path(__file__).parent / "kanban_published_runs.json"
# 2026-09-05: was Path(__file__).parent.parent -- see audit_kanban_completions.py
# for the full explanation. This is the actual PUBLISH script -- if this
# bug hit here too, real approved responses would silently never reach
# the ticket at all despite the reviewer approving them.
ORCHESTRATOR_PATH = r"C:\Users\Admin\Documents\Office\AIHelpdesk\Hermes_Orchestrator.py"

# 2026-09-04: Hermes_Orchestrator.py needs pyodbc, which only exists in the
# Windows Python -- confirmed live that WSL's own interpreters (bare python3
# AND the uv-managed one Hermes cron scripts actually run under) don't have
# it. This script is deployed both ways (run manually from Windows, and as
# a native WSL cron job): when 'wsl' is on PATH we're already running under
# Windows Python (sys.executable IS the right interpreter); when it's not,
# we're native WSL and must invoke the Windows interpreter by its
# WSL-visible path -- WSL can exec a Windows .exe directly via interop.
# The same rule applies to every subprocess call below that invokes
# Hermes_Orchestrator.py, not just the publish step -- a previous version
# of this file only fixed it in one place and broke on the others.
_HAS_WSL = shutil.which("wsl") is not None
ORCHESTRATOR_PYTHON = sys.executable if _HAS_WSL else r"/mnt/c/Python314/python.exe"


def load_published():
    if STATE_PATH.exists():
        return set(json.loads(STATE_PATH.read_text(encoding="utf-8")))
    return set()


def save_published(published):
    STATE_PATH.write_text(json.dumps(sorted(published)), encoding="utf-8")


# 2026-09-04 (later): single board now -- see ticket_scout.py's header for
# why the two-board split was retired in favor of native --parent gating.

def list_done_verifier_tasks():
    """status='done' here IS the approval, structurally: a reject uses
    kanban_block (see kanban_reject_bridge.py), which never reaches 'done'
    under the reviewer -- confirmed live by tracing the old shared-board
    equivalent (kanban_request_changes) end to end and finding it never
    produced status='done' either."""
    if _HAS_WSL:
        cmd = ["wsl", "-d", "Ubuntu", "--", "bash", "-lc",
               "hermes kanban list --status done --json"]
    else:
        cmd = ["hermes", "kanban", "list", "--status", "done", "--json"]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    if result.returncode != 0:
        print(f"WARNING: could not list done tasks: {result.stderr.strip()[:300]}")
        return []
    tasks = json.loads(result.stdout)
    return [t for t in tasks if "verifier" in (t.get("assignee") or "")]


def get_runs(task_id):
    if _HAS_WSL:
        cmd = ["wsl", "-d", "Ubuntu", "--", "bash", "-lc", f"hermes kanban runs {task_id} --json"]
    else:
        cmd = ["hermes", "kanban", "runs", task_id, "--json"]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    if result.returncode != 0:
        return []
    return json.loads(result.stdout)


def extract_field(body, field):
    for line in (body or "").splitlines():
        line = line.strip()
        if line.startswith(f"{field}:"):
            return line.split(":", 1)[1].strip()
    return None


def extract_run_id(body):
    return extract_field(body, "run_id")


def extract_ticket_id(body):
    return extract_field(body, "ticket_id")


def find_review_metadata(review_task_body):
    """The publish content is the ORIGINAL investigator's kanban_complete
    metadata, not anything the reviewer wrote -- the reviewer only judges,
    it doesn't retype the finding. Same-board lookup via the
    investigation_task_id ticket_scout.py embedded in the review card's own
    body (also available via native --parent handoff, but this direct
    lookup is kept as the explicit, auditable source of truth for what
    gets published)."""
    investigation_task_id = extract_field(review_task_body, "investigation_task_id")
    if not investigation_task_id:
        return None
    runs = get_runs(investigation_task_id)
    candidates = [
        r for r in runs
        if r.get("status") == "done" and r.get("metadata")
        and r.get("metadata", {}).get("response_type")
    ]
    if not candidates:
        return None
    return candidates[-1]["metadata"]


def is_approved(runs):
    """Structural signal (2026-09-04): a reviewer run that reached
    status='done' IS the approval -- reject uses kanban_block instead
    (see kanban_reject_bridge.py), which never produces 'done'. No
    free-text or metadata-key parsing needed; confirmed unreliable in
    both forms previously (neither the "APPROVE:" prefix nor a
    metadata.decision key ever showed up reliably in real completions)."""
    done_runs = [r for r in runs if r.get("status") == "done" and "verifier" in (r.get("profile") or "")]
    return bool(done_runs)


def fetch_route(args, run_id):
    """Via Hermes_Orchestrator.py --query (portable, no direct pyodbc
    dependency in this script -- see ORCHESTRATOR_PYTHON note above)."""
    cmd = [
        ORCHESTRATOR_PYTHON, str(ORCHESTRATOR_PATH),
        "--server", args.server, "--database", args.database,
        "--username", args.username, "--password", args.password,
        "--query", f"SELECT Route FROM dbo.Hermes_L2_Response_Trn_Tbl WHERE ID = '{run_id}'",
    ]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    if r.returncode != 0:
        return None
    try:
        rows = json.loads(r.stdout)
        return rows[0].get("Route") if rows else None
    except (json.JSONDecodeError, IndexError, AttributeError):
        return None


ACTIVITY_TYPE_BY_RESPONSE = {
    "RESOLUTION": "Resolution",
    "L3_ESCALATION": "Escalation",
    "QUESTION": "Note",
    "UPDATE": "Note",
}


def post_publish_data_entry(args, run_id, ticket_id, metadata):
    """The real point of this session's work: after a genuinely APPROVED and
    PUBLISHED response (never before -- an unverified bot claim should never
    write to the knowledge base), record it properly: a work-log activity
    entry always, and for a real RESOLUTION, a reusable solution article
    linked back to the ticket. This is deliberately gated here (the
    deterministic, human/reviewer-approved publish path), not in the
    investigator's own skill -- the investigator's claim isn't verified
    until it reaches this point."""
    route = fetch_route(args, run_id)
    response_type = metadata["response_type"]
    activity_type = ACTIVITY_TYPE_BY_RESPONSE.get(response_type, "Note")

    base = [ORCHESTRATOR_PYTHON, str(ORCHESTRATOR_PATH), "--server", args.server, "--database", args.database,
            "--username", args.username, "--password", args.password]

    log_cmd = base + [
        "--log-activity", "--ticket-id", ticket_id, "--run-id", run_id,
        "--activity-type", activity_type, "--actor-type", "Bot",
        "--note-text", metadata["reply_text"][:3900],
    ]
    r = subprocess.run(log_cmd, capture_output=True, text=True, timeout=60)
    if r.returncode != 0:
        print(f"    WARNING: activity log failed: {r.stderr.strip()[:300]}")
    else:
        print(f"    Logged {activity_type} activity.")

    if response_type != "RESOLUTION":
        return

    title = (metadata.get("problem_summary") or metadata["reply_text"])[:290]
    resolution_steps = metadata.get("resolution") or metadata["reply_text"]

    create_cmd = base + [
        "--create-solution", "--solution-title", title, "--resolution-steps", resolution_steps,
    ]
    if metadata.get("problem_summary"):
        create_cmd += ["--problem-summary", metadata["problem_summary"]]
    if metadata.get("root_cause"):
        create_cmd += ["--root-cause", metadata["root_cause"]]
    if route:
        create_cmd += ["--route", route]

    r = subprocess.run(create_cmd, capture_output=True, text=True, timeout=60)
    if r.returncode != 0 or "Created solution " not in (r.stdout or ""):
        print(f"    WARNING: solution creation failed: {r.stderr.strip()[:300]}")
        return
    solution_id = r.stdout.strip().split("Created solution ", 1)[1].split()[0]
    print(f"    Created solution article {solution_id}.")

    link_cmd = base + ["--link-solution", solution_id, "--ticket-id", ticket_id, "--run-id", run_id]
    r = subprocess.run(link_cmd, capture_output=True, text=True, timeout=60)
    if r.returncode != 0:
        print(f"    WARNING: solution link failed: {r.stderr.strip()[:300]}")
    else:
        print(f"    Linked solution {solution_id} to ticket.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--server", default="10.2.6.204")
    ap.add_argument("--database", default="XStudio_Helpdesk")
    ap.add_argument("--username", default="sa")
    ap.add_argument("--password", default=os.environ.get("MSSQL_MCP_PASSWORD"))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    tasks = list_done_verifier_tasks()
    if not tasks:
        print("No done verifier tasks found.")
        return

    published = load_published()
    processed = 0

    for t in tasks:
        run_id = extract_run_id(t.get("body"))
        ticket_id = extract_ticket_id(t.get("body"))
        if not run_id:
            continue
        if run_id in published:
            continue

        runs = get_runs(t["id"])
        if not is_approved(runs):
            continue  # rejected, or done for some other reason -- not ours to publish

        metadata = find_review_metadata(t.get("body"))
        if not metadata or not metadata.get("response_type") or not metadata.get("reply_text"):
            print(f"  {t['id']} (run {run_id}): approved but no usable review metadata found, skipping")
            continue

        print(f"  {t['id']} (run {run_id}): approved, publishing {metadata['response_type']}")
        if args.dry_run:
            print(f"    [DRY RUN] Would publish: {metadata['reply_text'][:100]}")
            continue

        cmd = [
            ORCHESTRATOR_PYTHON, str(ORCHESTRATOR_PATH),
            "--server", args.server, "--database", args.database,
            "--username", args.username, "--password", args.password,
            "--publish-response", "--run-id", run_id, "--force-run-id",
            "--response-type", metadata["response_type"],
            "--reply-text", metadata["reply_text"],
            # Always mirror to the real, human-visible ticket fields --
            # confirmed live 2026-09-03 that every single "successful"
            # publish this entire session left SupportExecutiveRemarks/
            # AskRemarks NULL, because nothing in the pipeline ever passed
            # these flags. A published response nobody can see on the
            # actual ticket isn't a published response. Not something the
            # model should have to remember -- always on here.
            "--mirror-to-support-remarks",
        ]
        if metadata["response_type"] == "QUESTION":
            cmd.append("--mirror-to-ask-remarks")
        for key, flag in (("problem_summary", "--problem-summary"), ("findings", "--findings"),
                           ("root_cause", "--root-cause"), ("resolution", "--resolution"),
                           ("new_ticket_status", "--new-ticket-status")):
            if metadata.get(key):
                cmd += [flag, str(metadata[key])]

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if result.returncode != 0:
            stderr = result.stderr.strip()
            if "Active Hermes run not found" in stderr:
                # Confirmed real 2026-09-04: approved-but-unpublished runs
                # that sat too long (this pipeline was broken for hours)
                # got swept to ProcessStatus='FAILED' by the stale-run
                # recovery job, which has no idea an approval was pending.
                # That data is gone -- retrying this run_id forever every
                # cron tick just produces the same error and noise, so
                # mark it resolved (not published) and move on.
                print(f"    SKIPPED (permanently stale -- underlying run is no longer active, cannot republish)")
                published.add(run_id)
            else:
                print(f"    FAILED to publish: {stderr[:400]}")
        else:
            print(f"    Published successfully.")
            published.add(run_id)
            processed += 1

            if ticket_id:
                post_publish_data_entry(args, run_id, ticket_id, metadata)
            else:
                print(f"    WARNING: no ticket_id found in task body -- skipping activity log/solution write.")

    if not args.dry_run:
        save_published(published)
    print(f"\n{len(tasks)} done verifier task(s) checked, {processed} newly published.")


if __name__ == "__main__":
    main()
