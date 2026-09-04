#!/usr/bin/env python3
"""The REAL fix for the false-completion bug, not just its consequence.

enforce_publish_safety_net.py (existing) only fires after 20 minutes and
always throws the real investigation away, replacing it with a blind
"escalating, no finding recorded" message -- it guarantees no ticket is
left silently stuck, but it never recovers genuine work the model already
did. Per model_scorecard.py's real numbers (qwen, 2026-09-03), a claim that
DOES get genuinely published takes ~157 seconds on average -- so a claim
still non-terminal after several minutes very likely has a model that
finished reasoning and simply narrated "done" without emitting the
--publish-response tool call (a documented failure class, "execution
hallucination" -- see AIHelpdesk/AGENTS.md).

This script closes that gap: it finds claims stale by a SHORT grace period
(default 6 minutes -- well past the observed genuine-completion time, well
short of the 20-minute safety net), resumes the EXACT Hermes session that
claimed the ticket (Hermes cron sessions are deterministically named
cron_<job_id>_<YYYYMMDD_HHMMSS>, and that session still has the full
investigation in context), and sends one hard nudge telling it to call
--publish-response NOW instead of starting over. If the nudge itself still
doesn't result in a publish, the existing 20-minute safety net remains the
unconditional backstop -- this script does not replace it, it just makes
the common case recover real findings instead of losing them.

Each DISTINCT reason to nudge a run is nudged at most once (tracked in
nudged_runs.json next to this script, keyed by run_id -> the trigger that
was last nudged) to avoid hammering the same stuck session repeatedly --
but a run whose draft got REJECTED by xstudio-l2-draft-verifier after an
earlier generic nudge is a genuinely new situation and gets nudged again,
this time with the verifier's own specific, fixable objection instead of
the generic "you forgot to publish" text -- wired in 2026-09-03 per an
explicit "wire the rejection reason obviously" instruction, since sending
the generic message after a real rejection just makes the model repeat
the same mistake with no idea what was actually wrong.

Usage (intended as a --no-agent cron job, every ~3-5 min):
    python nudge_unpublished_runs.py --server 10.2.6.204 --poll-job-id 52e0844c3c1e [--dry-run]
"""
import os
import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import pyodbc

GRACE_MINUTES_DEFAULT = 6
NUDGED_STATE_PATH = Path(__file__).parent / "nudged_runs.json"
REJECTED_DRAFTS_DIR = Path(__file__).parent / "drafts" / "rejected"

GENERIC_NUDGE_TEXT = (
    "You previously claimed this ticket for investigation but never called "
    "--draft-response, so the ticket is still stuck as unpublished. If you "
    "already worked out a finding, call --draft-response now with that "
    "finding -- do not repeat the investigation. If you genuinely could not "
    "reach a conclusion, call --draft-response with response type "
    "L3_ESCALATION and say plainly what you tried and what blocked you. "
    "Either way, call --draft-response before this turn ends."
)

SESSION_ID_RE = re.compile(r"cron_([0-9a-f]+)_(\d{8}_\d{6})")


def load_nudged():
    """run_id -> the trigger last nudged for it ("generic", or the specific
    rejected-draft filename). Migrates the old set-of-run_ids format
    transparently (pre-2026-09-03, before rejection-aware nudging)."""
    if not NUDGED_STATE_PATH.exists():
        return {}
    raw = json.loads(NUDGED_STATE_PATH.read_text(encoding="utf-8"))
    if isinstance(raw, list):
        return {run_id: "generic" for run_id in raw}
    return raw


def save_nudged(nudged):
    NUDGED_STATE_PATH.write_text(json.dumps(nudged, indent=2), encoding="utf-8")


def find_latest_rejection(run_id):
    """Most recent rejected-draft file for this run_id, if any -- filenames
    are `<run_id>_<unix_ts>.json` (see Hermes_Orchestrator.py --reject-draft),
    so lexical sort on the full name sorts by rejection time too."""
    if not REJECTED_DRAFTS_DIR.exists():
        return None
    matches = sorted(REJECTED_DRAFTS_DIR.glob(f"{run_id}_*.json"))
    if not matches:
        return None
    latest = matches[-1]
    return latest.name, json.loads(latest.read_text(encoding="utf-8"))


def build_nudge_text(run_id):
    """Returns (trigger_key, message). trigger_key is what gets recorded in
    nudged_runs.json -- a NEW rejection produces a NEW trigger_key (the
    rejection filename), so it gets nudged again even if this run_id was
    already nudged once before for a different (older) reason."""
    rejection = find_latest_rejection(run_id)
    if rejection is None:
        return "generic", GENERIC_NUDGE_TEXT
    filename, draft = rejection
    reason = draft.get("rejection_reason", "(no reason recorded)")
    message = (
        f"Your draft response for this ticket was reviewed and REJECTED, not "
        f"published. The verifier's specific objection was: \"{reason}\" -- "
        f"fix exactly that problem (don't restart the whole investigation "
        f"unless the objection genuinely requires it) and call "
        f"--draft-response again before this turn ends."
    )
    return filename, message


def find_stale_claims(server, database, username, password, grace_minutes):
    conn = pyodbc.connect(
        f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};"
        f"UID={username};PWD={password};TrustServerCertificate=yes"
    )
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT ID, TicketID, ClaimedOn FROM Hermes_L2_Response_Trn_Tbl "
            "WHERE ProcessStatus IN ('CLAIMED', 'INVESTIGATING') AND IsActive = 1 "
            "AND ClaimedOn < DATEADD(MINUTE, -?, GETDATE())",
            grace_minutes,
        )
        return [{"run_id": str(r[0]), "ticket_id": str(r[1]), "claimed_on": r[2]} for r in cur.fetchall()]
    finally:
        conn.close()


def list_cron_sessions(profile, poll_job_id):
    """Return [(datetime, session_id)] for this poll job's cron sessions,
    newest first, by parsing the deterministic cron_<job_id>_<timestamp> ID
    embedded in `hermes sessions list` -- no JSON output mode exists for
    this command, so this is a best-effort text parse."""
    result = subprocess.run(
        ["wsl", "-d", "Ubuntu", "--", "bash", "-lc",
         f"hermes -p {profile} sessions list --limit 100"],
        capture_output=True, text=True, timeout=60,
    )
    sessions = []
    for match in SESSION_ID_RE.finditer(result.stdout):
        job_id, ts = match.group(1), match.group(2)
        if job_id != poll_job_id:
            continue
        try:
            dt_utc = datetime.strptime(ts, "%Y%m%d_%H%M%S")
        except ValueError:
            continue
        # Session IDs embed UTC (confirmed against cron job run timestamps,
        # which are explicit +00:00). ClaimedOn is SQL Server local time
        # (~IST, UTC+5:30 -- the exact same offset bug already fixed once in
        # enforce_publish_safety_net.py). Convert here so the two are
        # comparable, or every claim looks like it happened after every
        # session and this always picks the wrong (most recent) one.
        sessions.append((dt_utc + timedelta(hours=5, minutes=30), match.group(0)))
    sessions.sort(reverse=True)
    return sessions


def find_owning_session(claimed_on, cron_sessions):
    """The session that claimed this run is the poll cycle running AT
    claim time -- the latest cron session whose start timestamp is <=
    ClaimedOn. Heuristic, not a guarantee: correct as long as the poll job
    doesn't overlap itself, which Hermes cron serializes per-job anyway."""
    candidates = [(dt, sid) for dt, sid in cron_sessions if dt <= claimed_on]
    if not candidates:
        return None
    candidates.sort(reverse=True)
    return candidates[0][1]


def nudge(profile, session_id, message, dry_run):
    if dry_run:
        print(f"[DRY RUN] Would resume session {session_id} with: {message[:100]}...")
        return True
    escaped = message.replace('"', '\\"')
    try:
        result = subprocess.run(
            ["wsl", "-d", "Ubuntu", "--", "bash", "-lc",
             f'hermes -p {profile} --resume {session_id} -z "{escaped}"'],
            capture_output=True, text=True, timeout=900,
        )
    except subprocess.TimeoutExpired:
        # The CLI call timing out client-side does NOT mean the turn failed
        # -- confirmed live 2026-09-03: a nudge that timed out here at 600s
        # had still genuinely published (verify_l2_run.py PASSED) once the
        # underlying LM Studio inference actually finished. Treat this as
        # "unknown, check the DB" rather than a failure, and -- critically
        # -- don't let it crash the whole batch and skip every other stale
        # claim, which is what an uncaught exception did the first time.
        print(f"Nudge for session {session_id} did not return within 900s "
              f"(inference may still be running) -- check verify_l2_run.py before re-nudging")
        return False
    if result.returncode != 0:
        print(f"NUDGE FAILED for session {session_id}: {result.stderr.strip()[:500]}")
        return False
    print(f"Nudged session {session_id} (exit 0)")
    return True


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--server", default="10.2.6.204")
    ap.add_argument("--database", default="XStudio_Helpdesk")
    ap.add_argument("--username", default="sa")
    ap.add_argument("--password", default=os.environ.get("MSSQL_MCP_PASSWORD"))
    ap.add_argument("--profile", default="l2-investigator")
    ap.add_argument("--poll-job-id", required=True, help="Job ID of the 'Poll Helpdesk L2 tickets' cron job")
    ap.add_argument("--grace-minutes", type=int, default=GRACE_MINUTES_DEFAULT)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    stale = find_stale_claims(args.server, args.database, args.username, args.password, args.grace_minutes)
    already_nudged = load_nudged()

    # For each stale run, figure out what the CURRENT reason to nudge it is
    # (a rejected draft, if one exists, always wins over the generic
    # not-yet-drafted case) and only nudge if that specific reason hasn't
    # already been nudged -- a run rejected a second time gets a fresh
    # trigger_key (the new rejection's filename) even if it was nudged once
    # before for an older reason.
    to_nudge = []
    for s in stale:
        trigger_key, message = build_nudge_text(s["run_id"])
        if already_nudged.get(s["run_id"]) != trigger_key:
            to_nudge.append((s, trigger_key, message))

    if not to_nudge:
        print(f"No newly-stale unpublished claims (checked {len(stale)} stale, all already nudged for their current reason).")
        return

    cron_sessions = list_cron_sessions(args.profile, args.poll_job_id)
    print(f"Found {len(to_nudge)} newly-stale claim(s); {len(cron_sessions)} known poll sessions for correlation.")

    for s, trigger_key, message in to_nudge:
        session_id = find_owning_session(s["claimed_on"], cron_sessions)
        if session_id is None:
            print(f"  run {s['run_id']} (ticket {s['ticket_id']}): no owning session found, skipping "
                  f"-- will be caught by the 30-minute safety net instead")
            continue
        reason_kind = "REJECTION" if trigger_key != "generic" else "generic (no draft found)"
        print(f"  run {s['run_id']} (ticket {s['ticket_id']}, claimed {s['claimed_on']}) -> "
              f"session {session_id} [{reason_kind}]")
        nudge(args.profile, session_id, message, args.dry_run)
        already_nudged[s["run_id"]] = trigger_key

    if not args.dry_run:
        save_nudged(already_nudged)


if __name__ == "__main__":
    main()
