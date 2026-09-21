#!/usr/bin/env python3
"""Deterministic scorecard for comparing models against the SAME harness.

Why this exists: the user asked for "some measure to judge which model to
go for, given that the harness is constant" -- comparing gemma vs qwen vs
future candidates by vibes/spot-checks doesn't scale and isn't rigorous.
This computes real numbers straight from Hermes_L2_Response_Trn_Tbl, the
same ground truth verify_l2_run.py already trusts (never the cron
wrapper's own "completed" label, and never the model's own narration).

Metrics computed, for a given time window:
  - claimed:            how many runs this worker claimed
  - verified_published: ProcessStatus terminal (COMPLETED/WAITING_USER),
                         ResponseType set, ReplyText non-empty, CompletedOn
                         set -- i.e. actually did the job, not just exited
  - verified_rate:      verified_published / claimed
  - safety_net_rescues:  runs whose ReplyText is the exact canned string
                         enforce_publish_safety_net.py writes -- these are
                         claimed-but-never-published runs the model itself
                         left stuck (the deterministic net caught it, but
                         it still counts against the MODEL, not the net)
  - genuine_rate:        (verified_published - safety_net_rescues) / claimed
                         -- the real "did the model itself finish the job"
                         number, since a safety-net rescue is a model failure
                         papered over structurally, not a model success
  - avg_duration_sec:    mean CompletedOn-ClaimedOn over genuinely-published
                         runs (excludes safety-net rescues, whose duration
                         is dominated by the stale-after-minutes wait, not
                         real work)
  - response_type_counts: breakdown (UPDATE/QUESTION/RESOLUTION/L3_ESCALATION)

Jev semantic trace assessment now adds automated quality signals for every
assessed run: silent-failure probability, false-success probability, policy
violation probability, evidence gathering, human-attention need, failure class,
and investigation efficiency/repetition scores. These are calibrated semantic
judgments, not ground-truth labels; keep deterministic outcome metrics separate.

Usage:
    python model_scorecard.py --model-label gemma-4-e4b-it \
        --since "2026-09-03 10:00" --until "2026-09-03 11:00" --server 10.2.6.204

    python model_scorecard.py --model-label qwen3.5-9b \
        --run-ids <id1>,<id2>,<id3> --server 10.2.6.204

Pass either a time window (--since/--until, server-local time, matching how
ClaimedOn is stored) or an explicit --run-ids list. Run once per model on
the SAME ticket batch / equivalent windows to compare.
"""
import os
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import pyodbc

TERMINAL_STATUSES = {"COMPLETED", "WAITING_USER"}

# Exact canned text enforce_publish_safety_net.py writes -- used to detect
# runs it had to rescue, distinguishing "model genuinely finished" from
# "model left it stuck and the deterministic net caught it."
SAFETY_NET_MARKER = "the investigating process did not publish a response within the expected time window"


def fetch_runs(server, database, username, password, since=None, until=None, run_ids=None):
    conn = pyodbc.connect(
        f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};"
        f"UID={username};PWD={password};TrustServerCertificate=yes"
    )
    try:
        cur = conn.cursor()
        cur.execute("SELECT CASE WHEN OBJECT_ID('dbo.Hermes_Jev_Run_Assessment_Vw', 'V') IS NULL THEN 0 ELSE 1 END")
        has_jev = bool(cur.fetchone()[0])
        jev_fields = [
            "TaskCompletedProbability", "EvidenceGatheredProbability",
            "SilentFailureProbability", "FalseSuccessClaimProbability",
            "PolicyViolationProbability", "TransportFlailingProbability",
            "HumanAttentionProbability", "UnnecessaryToolRepetitionScore",
            "InvestigationEfficiencyScore", "AttentionPriorityScore",
            "FailureClass", "FailureClassConfidence",
            "ReviewEvidenceSupportProbability", "ReviewOverclaimProbability",
            "ReviewActionClaimProbability", "ReviewActionAuditProbability",
            "ReviewRiskScore", "JevReviewDecision", "JevReviewConfidence",
        ]
        jev_cols = (
            ", " + ", ".join(f"j.{name}" for name in jev_fields)
            if has_jev else
            ", " + ", ".join("NULL" for _ in jev_fields)
        )
        join = " LEFT JOIN dbo.Hermes_Jev_Run_Assessment_Vw j ON j.RunID = r.ID " if has_jev else ""
        base = (
            "SELECT r.ID, r.TicketID, r.ProcessStatus, r.ResponseType, r.ReplyText, "
            "r.CompletedOn, r.ClaimedOn " + jev_cols +
            " FROM dbo.Hermes_L2_Response_Trn_Tbl r " + join
        )
        if run_ids:
            placeholders = ",".join("?" for _ in run_ids)
            cur.execute(base + f" WHERE r.ID IN ({placeholders})", run_ids)
        else:
            cur.execute(base + " WHERE r.ClaimedOn >= ? AND r.ClaimedOn <= ?", since, until)
        cols = [
            "run_id", "ticket_id", "process_status", "response_type",
            "reply_text", "completed_on", "claimed_on",
            "task_completed_probability", "evidence_gathered_probability",
            "silent_failure_probability", "false_success_claim_probability",
            "policy_violation_probability", "transport_flailing_probability",
            "human_attention_probability", "unnecessary_tool_repetition_score",
            "investigation_efficiency_score", "attention_priority_score",
            "failure_class", "failure_class_confidence",
            "review_evidence_support_probability", "review_overclaim_probability",
            "review_action_claim_probability", "review_action_audit_probability",
            "review_risk_score", "jev_review_decision", "jev_review_confidence",
        ]
        return [dict(zip(cols, row)) for row in cur.fetchall()]
    finally:
        conn.close()


def score(runs):
    claimed = len(runs)
    verified = []
    rescued = []
    response_type_counts = {}

    for r in runs:
        rt = r["response_type"] or "(none)"
        response_type_counts[rt] = response_type_counts.get(rt, 0) + 1

        is_verified = (
            r["process_status"] in TERMINAL_STATUSES
            and bool(r["response_type"])
            and bool(r["reply_text"] and r["reply_text"].strip())
            and r["completed_on"] is not None
        )
        if is_verified:
            verified.append(r)
            if r["reply_text"] and SAFETY_NET_MARKER in r["reply_text"]:
                rescued.append(r)

    genuine = [r for r in verified if r not in rescued]
    durations = [
        (r["completed_on"] - r["claimed_on"]).total_seconds()
        for r in genuine
        if r["completed_on"] and r["claimed_on"]
    ]

    assessed = [r for r in runs if r.get("failure_class")]
    failure_class_counts = {}
    for r in assessed:
        fc = r.get("failure_class") or "(none)"
        failure_class_counts[fc] = failure_class_counts.get(fc, 0) + 1

    high = 0.80
    semantic = {
        "assessed_runs": len(assessed),
        "assessment_rate": round(len(assessed) / claimed, 3) if claimed else None,
        "failure_class_counts": failure_class_counts,
        "high_silent_failure": sum(
            1 for r in assessed if (r.get("silent_failure_probability") or 0) >= high
        ),
        "high_false_success_claim": sum(
            1 for r in assessed if (r.get("false_success_claim_probability") or 0) >= high
        ),
        "high_policy_violation": sum(
            1 for r in assessed if (r.get("policy_violation_probability") or 0) >= high
        ),
        "high_human_attention": sum(
            1 for r in assessed if (r.get("human_attention_probability") or 0) >= high
        ),
        "high_transport_flailing": sum(
            1 for r in assessed if (r.get("transport_flailing_probability") or 0) >= high
        ),
    }
    ineff = [
        float(r["investigation_efficiency_score"])
        for r in assessed if r.get("investigation_efficiency_score") is not None
    ]
    repeat = [
        float(r["unnecessary_tool_repetition_score"])
        for r in assessed if r.get("unnecessary_tool_repetition_score") is not None
    ]
    semantic["avg_inefficiency_score_0_to_3"] = round(sum(ineff) / len(ineff), 3) if ineff else None
    semantic["avg_repetition_score_0_to_3"] = round(sum(repeat) / len(repeat), 3) if repeat else None
    semantic["high_confidence_non_approve_review"] = sum(
        1 for r in runs
        if r.get("jev_review_decision")
        and (r.get("jev_review_confidence") or 0) >= 0.70
        and str(r.get("jev_review_decision") or "").upper() != "APPROVE"
    )

    return {
        "claimed": claimed,
        "verified_published": len(verified),
        "verified_rate": round(len(verified) / claimed, 3) if claimed else None,
        "safety_net_rescues": len(rescued),
        "genuine_published": len(genuine),
        "genuine_rate": round(len(genuine) / claimed, 3) if claimed else None,
        "avg_duration_sec": round(sum(durations) / len(durations), 1) if durations else None,
        "response_type_counts": response_type_counts,
        "jev_semantic_quality": semantic,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model-label", required=True, help="Free-text label for this run, e.g. gemma-4-e4b-it")
    ap.add_argument("--server", default="10.2.6.204")
    ap.add_argument("--database", default="XStudio_Helpdesk")
    ap.add_argument("--username", default="sa")
    ap.add_argument("--password", default=os.environ.get("MSSQL_MCP_PASSWORD"))
    ap.add_argument("--since", help="Server-local time, e.g. '2026-09-03 10:00'")
    ap.add_argument("--until", help="Server-local time, e.g. '2026-09-03 11:00'")
    ap.add_argument("--run-ids", help="Comma-separated list of run IDs, alternative to --since/--until")
    args = ap.parse_args()

    if args.run_ids:
        run_ids = [x.strip() for x in args.run_ids.split(",") if x.strip()]
        runs = fetch_runs(args.server, args.database, args.username, args.password, run_ids=run_ids)
    elif args.since and args.until:
        runs = fetch_runs(args.server, args.database, args.username, args.password,
                           since=args.since, until=args.until)
    else:
        ap.error("must pass either --run-ids or both --since and --until")

    result = score(runs)

    print(f"=== Scorecard: {args.model_label} ===")
    print(f"Claimed runs:          {result['claimed']}")
    print(f"Verified published:    {result['verified_published']} ({result['verified_rate']})")
    print(f"  of which safety-net rescued (model itself never published): {result['safety_net_rescues']}")
    print(f"Genuine publish rate:  {result['genuine_published']} ({result['genuine_rate']})  <- the real number")
    print(f"Avg genuine duration:  {result['avg_duration_sec']} sec")
    print("Response type breakdown:")
    for rt, count in sorted(result["response_type_counts"].items()):
        print(f"  {rt}: {count}")
    sem = result["jev_semantic_quality"]
    print("Jev semantic quality (advisory/calibration signals):")
    print(f"  Assessed runs:                     {sem['assessed_runs']} ({sem['assessment_rate']})")
    print(f"  High silent-failure probability:   {sem['high_silent_failure']}")
    print(f"  High false-success probability:    {sem['high_false_success_claim']}")
    print(f"  High policy-violation probability: {sem['high_policy_violation']}")
    print(f"  High transport-flailing probability: {sem['high_transport_flailing']}")
    print(f"  High human-attention probability:  {sem['high_human_attention']}")
    print(f"  Avg inefficiency score 0-3:        {sem['avg_inefficiency_score_0_to_3']}")
    print(f"  Avg repetition score 0-3:          {sem['avg_repetition_score_0_to_3']}")
    print(f"  High-confidence non-approve Jev reviews: {sem['high_confidence_non_approve_review']}")
    print("  Failure-class breakdown:")
    for fc, count in sorted(sem["failure_class_counts"].items()):
        print(f"    {fc}: {count}")


if __name__ == "__main__":
    main()
