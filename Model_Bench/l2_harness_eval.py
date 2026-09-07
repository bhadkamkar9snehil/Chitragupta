#!/usr/bin/env python3
"""Score one fixed-model Hermes L2 run from trace, SQL evidence and lifecycle data.

The evaluator deliberately treats the model as a constant. Experiment variants
change harness inputs (tool exposure, routing context and proposal contract),
while this module exposes one small interface: ``evaluate_run(bundle, oracle)``.
It is also usable against JSON exports so early harness iterations do not need a
new Helpdesk schema.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import mean
from typing import Any, Dict, Iterable, List


INVESTIGATOR = "l2-investigator-primary"
REVIEWER = "l2-reviewer-primary"


def _role_events(events: Iterable[Dict[str, Any]], role: str) -> List[Dict[str, Any]]:
    return [event for event in events if event.get("profile_name") == role]


def _successful_calls(events: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    pre = {
        event.get("tool_call_id"): event
        for event in events
        if event.get("event_type") == "pre_tool_call" and event.get("tool_call_id")
    }
    calls = []
    for event in events:
        if event.get("event_type") != "post_tool_call" or event.get("status") != "ok":
            continue
        before = pre.get(event.get("tool_call_id"))
        if before and before.get("tool_name") == event.get("tool_name"):
            calls.append(before)
    return calls


def _averaged(events: Iterable[Dict[str, Any]], key: str) -> int | None:
    values = [event.get(key) for event in events if isinstance(event.get(key), (int, float))]
    return round(mean(values)) if values else None


def _maximum(events: Iterable[Dict[str, Any]], result_key: str) -> int | float | None:
    values = [
        (event.get("result") or {}).get(result_key)
        for event in events
        if isinstance(event.get("result"), dict)
        and isinstance((event.get("result") or {}).get(result_key), (int, float))
    ]
    return max(values) if values else None


def _has_tool_continuation(events: List[Dict[str, Any]], role: str) -> bool:
    role_events = sorted(_role_events(events, role), key=lambda event: event.get("written_at") or 0)
    success_indexes = {
        index for index, event in enumerate(role_events)
        if event.get("event_type") == "post_tool_call" and event.get("status") == "ok"
    }
    return any(
        later.get("event_type") == "post_api_request"
        for index in success_indexes
        for later in role_events[index + 1:]
    )


def _material_claims(proposal: Dict[str, Any]) -> List[Dict[str, Any]]:
    return [claim for claim in proposal.get("claims") or [] if claim.get("material", True)]


def evaluate_run(bundle: Dict[str, Any], oracle: Dict[str, Any]) -> Dict[str, Any]:
    events = list(bundle.get("events") or [])
    successful = _successful_calls(events)
    all_pre_calls = [event for event in events if event.get("event_type") == "pre_tool_call"]
    required_tools = oracle.get("required_tools") or {}

    missing_tools = []
    argument_errors = []
    for role, role_requirements in required_tools.items():
        role_calls = _role_events(successful, role)
        for tool_name, required_args in role_requirements.items():
            matching = [call for call in role_calls if call.get("tool_name") == tool_name]
            if not matching:
                missing_tools.append(f"{role}:{tool_name}")
                continue
            if not any(all((call.get("args") or {}).get(key) == value for key, value in required_args.items())
                       for call in matching):
                argument_errors.append(f"{role}:{tool_name}")

    run = bundle.get("run") or {}
    run_id = str(run.get("ID") or "")
    ticket_id = str(run.get("TicketID") or "")
    actions = {
        str(action.get("ID")): action for action in bundle.get("actions") or []
        if str(action.get("RunID") or "") == run_id and str(action.get("TicketID") or "") == ticket_id
    }
    claims = _material_claims(bundle.get("proposal") or {})
    invalid_evidence_claims = []
    for claim in claims:
        if str(claim.get("status") or "").upper() != "VERIFIED":
            continue
        refs = [str(ref.get("action_id")) for ref in claim.get("evidence") or [] if ref.get("action_id")]
        if not refs or any(ref not in actions for ref in refs):
            invalid_evidence_claims.append(claim.get("id") or claim.get("claim") or "unnamed")

    forbidden = [phrase.lower() for phrase in oracle.get("forbidden_claim_phrases") or []]
    unsupported = []
    for claim in claims:
        text = str(claim.get("claim") or "")
        status = str(claim.get("status") or "").upper()
        if status in {"VERIFIED", "INFERRED"} and any(phrase in text.lower() for phrase in forbidden):
            unsupported.append({"claim": text, "status": status, "reason": "oracle-forbidden material assertion"})
    unsupported.extend(
        {"claim": claim_id, "status": "VERIFIED", "reason": "missing current-run evidence"}
        for claim_id in invalid_evidence_claims
    )

    investigator_events = _role_events(events, INVESTIGATOR)
    reviewer_events = _role_events(events, REVIEWER)
    investigator_calls = _role_events(all_pre_calls, INVESTIGATOR)
    reviewer_calls = _role_events(all_pre_calls, REVIEWER)
    investigator_api = [event for event in investigator_events if event.get("event_type") == "post_api_request"]
    reviewer_api = [event for event in reviewer_events if event.get("event_type") == "post_api_request"]
    compute_events = [event for event in events if event.get("event_type") in {"compute_sample", "gpu_sample"}]
    lifecycle = {str(item).lower() for item in bundle.get("lifecycle_events") or []}
    recovery_markers = {"recovery", "rework", "gave_up", "orphan_recovery", "unreviewable_rework"}
    approved = str((bundle.get("review") or {}).get("decision") or "").upper() == "APPROVE"

    return {
        "valid_hermes_tool_calls": len(successful) == len(all_pre_calls)
            and all(str(call.get("tool_name") or "").startswith("xstudio_") for call in all_pre_calls),
        "correct_tool_choice": not missing_tools,
        "missing_required_tools": missing_tools,
        "correct_required_arguments": not argument_errors,
        "argument_errors": argument_errors,
        "successful_multi_turn_tool_continuation": all(
            _has_tool_continuation(events, role) for role in required_tools
        ),
        "live_evidence_grounding": not invalid_evidence_claims and bool(claims),
        "invalid_evidence_claims": invalid_evidence_claims,
        "unsupported_material_claims": unsupported,
        "reviewer_false_approval": approved and bool(unsupported),
        "investigator_tool_calls": len(investigator_calls),
        "reviewer_tool_calls": len(reviewer_calls),
        "investigator_model_turns": len(investigator_api),
        "reviewer_model_turns": len(reviewer_api),
        "investigator_ttft_ms_avg": _averaged(investigator_api, "ttft_ms"),
        "reviewer_ttft_ms_avg": _averaged(reviewer_api, "ttft_ms"),
        "investigator_total_latency_ms": sum(event.get("api_duration_ms") or 0 for event in investigator_api),
        "reviewer_total_latency_ms": sum(event.get("api_duration_ms") or 0 for event in reviewer_api),
        "investigator_tokens": sum((event.get("usage") or {}).get("total_tokens") or 0 for event in investigator_api),
        "reviewer_tokens": sum((event.get("usage") or {}).get("total_tokens") or 0 for event in reviewer_api),
        "peak_gpu_vram_mb": _maximum(compute_events, "gpu_mem_used_mb") or _maximum(compute_events, "mem_used_mb"),
        "gpu_vram_total_mb": _maximum(compute_events, "gpu_mem_total_mb") or _maximum(compute_events, "mem_total_mb"),
        "peak_cpu_util_pct": _maximum(compute_events, "cpu_util_pct"),
        "peak_system_memory_mb": _maximum(compute_events, "system_mem_used_mb"),
        "pipeline_completed_without_recovery": str(run.get("ProcessStatus") or "").upper() == "COMPLETED"
            and "published" in lifecycle and not lifecycle.intersection(recovery_markers),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", required=True, type=Path)
    parser.add_argument("--oracle", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = evaluate_run(
        json.loads(args.bundle.read_text(encoding="utf-8")),
        json.loads(args.oracle.read_text(encoding="utf-8")),
    )
    rendered = json.dumps(report, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)


if __name__ == "__main__":
    main()
