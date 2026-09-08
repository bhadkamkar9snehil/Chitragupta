import unittest

from Model_Bench.l2_harness_eval import evaluate_run


class HarnessEvaluationTests(unittest.TestCase):
    def test_scores_clean_grounded_two_role_run(self):
        bundle = {
            "run": {"ID": "run-1", "TicketID": "ticket-1", "ProcessStatus": "COMPLETED"},
            "proposal": {
                "claims": [{
                    "id": "C1", "claim": "Heat exists", "material": True,
                    "status": "VERIFIED", "evidence": [{"action_id": "action-1"}],
                }]
            },
            "review": {"decision": "APPROVE"},
            "actions": [{"ID": "action-1", "RunID": "run-1", "TicketID": "ticket-1"}],
            "events": [
                {"event_type": "post_api_request", "profile_name": "l2-investigator-primary",
                 "turn_id": "i1", "assistant_tool_call_count": 1, "ttft_ms": 800,
                 "api_duration_ms": 3000, "usage": {"total_tokens": 500}, "written_at": 1.0},
                {"event_type": "pre_tool_call", "profile_name": "l2-investigator-primary",
                 "turn_id": "i1", "tool_call_id": "tc1", "tool_name": "xstudio_heat_context",
                 "args": {"heat": "1602522"}, "written_at": 2.0},
                {"event_type": "post_tool_call", "profile_name": "l2-investigator-primary",
                 "turn_id": "i1", "tool_call_id": "tc1", "tool_name": "xstudio_heat_context",
                 "status": "ok", "written_at": 3.0},
                {"event_type": "post_api_request", "profile_name": "l2-investigator-primary",
                 "turn_id": "i2", "assistant_tool_call_count": 0, "ttft_ms": 600,
                 "api_duration_ms": 2000, "usage": {"total_tokens": 300}, "written_at": 4.0},
                {"event_type": "post_api_request", "profile_name": "l2-reviewer-primary",
                 "turn_id": "r1", "assistant_tool_call_count": 1, "ttft_ms": 700,
                 "api_duration_ms": 2500, "usage": {"total_tokens": 400}, "written_at": 5.0},
                {"event_type": "pre_tool_call", "profile_name": "l2-reviewer-primary",
                 "turn_id": "r1", "tool_call_id": "tc2", "tool_name": "xstudio_heat_context",
                 "args": {"heat": "1602522"}, "written_at": 6.0},
                {"event_type": "post_tool_call", "profile_name": "l2-reviewer-primary",
                 "turn_id": "r1", "tool_call_id": "tc2", "tool_name": "xstudio_heat_context",
                 "status": "ok", "written_at": 7.0},
                {"event_type": "post_api_request", "profile_name": "l2-reviewer-primary",
                 "turn_id": "r2", "assistant_tool_call_count": 0, "ttft_ms": 500,
                 "api_duration_ms": 1500, "usage": {"total_tokens": 200}, "written_at": 8.0},
                {"event_type": "compute_sample", "profile_name": "l2-investigator-primary",
                 "result": {"gpu_mem_used_mb": 7800, "gpu_mem_total_mb": 8188,
                            "cpu_util_pct": 35, "system_mem_used_mb": 14000}},
            ],
            "lifecycle_events": ["dispatch", "investigator_complete", "reviewer_created", "approved", "published"],
        }
        oracle = {
            "required_tools": {
                "l2-investigator-primary": {"xstudio_heat_context": {"heat": "1602522"}},
                "l2-reviewer-primary": {"xstudio_heat_context": {"heat": "1602522"}},
            },
            "forbidden_claim_phrases": ["api failure", "trigger failure"],
        }

        report = evaluate_run(bundle, oracle)

        self.assertTrue(report["valid_hermes_tool_calls"])
        self.assertTrue(report["correct_tool_choice"])
        self.assertTrue(report["correct_required_arguments"])
        self.assertTrue(report["successful_multi_turn_tool_continuation"])
        self.assertTrue(report["live_evidence_grounding"])
        self.assertEqual([], report["unsupported_material_claims"])
        self.assertFalse(report["reviewer_false_approval"])
        self.assertEqual(1, report["investigator_tool_calls"])
        self.assertEqual(1, report["reviewer_tool_calls"])
        self.assertEqual(2, report["investigator_model_turns"])
        self.assertEqual(2, report["reviewer_model_turns"])
        self.assertEqual(700, report["investigator_ttft_ms_avg"])
        self.assertEqual(7800, report["peak_gpu_vram_mb"])
        self.assertTrue(report["pipeline_completed_without_recovery"])

    def test_flags_cross_run_evidence_and_reviewer_false_approval(self):
        bundle = {
            "run": {"ID": "run-current", "TicketID": "ticket-1", "ProcessStatus": "COMPLETED"},
            "proposal": {
                "claims": [{
                    "id": "C1",
                    "claim": "The SAP trigger failed before the API call.",
                    "material": True,
                    "status": "VERIFIED",
                    "evidence": [{"action_id": "action-other-run"}],
                }]
            },
            "review": {"decision": "APPROVE"},
            "actions": [{
                "ID": "action-other-run", "RunID": "run-other", "TicketID": "ticket-1"
            }],
            "events": [],
            "lifecycle_events": ["approved", "published"],
        }
        oracle = {"forbidden_claim_phrases": ["trigger failed"]}

        report = evaluate_run(bundle, oracle)

        self.assertFalse(report["live_evidence_grounding"])
        self.assertEqual(["C1"], report["invalid_evidence_claims"])
        self.assertEqual(2, len(report["unsupported_material_claims"]))
        self.assertTrue(report["reviewer_false_approval"])

    def test_missing_tool_and_wrong_arguments_are_separate_failures(self):
        bundle = {
            "run": {"ID": "run-1", "TicketID": "ticket-1", "ProcessStatus": "INVESTIGATING"},
            "events": [
                {"event_type": "pre_tool_call", "profile_name": "l2-investigator-primary",
                 "tool_call_id": "tc1", "tool_name": "xstudio_heat_context",
                 "args": {"heat": "wrong"}, "written_at": 1.0},
                {"event_type": "post_tool_call", "profile_name": "l2-investigator-primary",
                 "tool_call_id": "tc1", "tool_name": "xstudio_heat_context",
                 "status": "ok", "written_at": 2.0},
            ],
        }
        oracle = {
            "required_tools": {
                "l2-investigator-primary": {
                    "xstudio_heat_context": {"heat": "1602522"},
                    "xstudio_sap_api_context": {"api_type": "Production"},
                }
            }
        }

        report = evaluate_run(bundle, oracle)

        self.assertFalse(report["correct_tool_choice"])
        self.assertEqual(
            ["l2-investigator-primary:xstudio_sap_api_context"],
            report["missing_required_tools"],
        )
        self.assertFalse(report["correct_required_arguments"])
        self.assertEqual(
            ["l2-investigator-primary:xstudio_heat_context"], report["argument_errors"]
        )
        self.assertFalse(report["successful_multi_turn_tool_continuation"])

    def test_valid_hermes_calls_include_kanban_and_flag_missing_post(self):
        base = {
            "run": {"ID": "run-1", "TicketID": "ticket-1"},
            "events": [
                {"event_type": "pre_tool_call", "profile_name": "l2-investigator-primary",
                 "tool_call_id": "k1", "tool_name": "kanban_show", "args": {}},
                {"event_type": "post_tool_call", "profile_name": "l2-investigator-primary",
                 "tool_call_id": "k1", "tool_name": "kanban_show", "status": "ok"},
            ],
        }
        self.assertTrue(evaluate_run(base, {})["valid_hermes_tool_calls"])
        base["events"].append(
            {"event_type": "pre_tool_call", "profile_name": "l2-investigator-primary",
             "tool_call_id": "bad", "tool_name": "xstudio_select", "args": {}}
        )
        report = evaluate_run(base, {})
        self.assertFalse(report["valid_hermes_tool_calls"])
        self.assertEqual(1, len(report["failed_tool_calls"]))

    def test_unverified_claim_cannot_hide_forbidden_customer_prose(self):
        bundle = {
            "run": {"ID": "r", "TicketID": "t", "ProcessStatus": "COMPLETED"},
            "proposal": {"reply_text": "The record appears orphaned or deleted.", "claims": [{
                "id": "C1", "claim": "No rows were found", "status": "UNVERIFIED", "material": True,
            }]},
            "review": {"decision": "APPROVE"},
        }
        report = evaluate_run(bundle, {"forbidden_claim_phrases": ["orphaned", "deleted"]})
        findings = report["unsupported_material_claims"]
        self.assertEqual(1, len(findings))
        self.assertEqual("PUBLISHED_PROSE", findings[0]["status"])
        self.assertTrue(report["reviewer_false_approval"])


if __name__ == "__main__":
    unittest.main()
