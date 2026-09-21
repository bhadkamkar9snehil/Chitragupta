import importlib.util
import json
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location("l2_pipeline_runtime", "Model_Bench/l2_pipeline_runtime.py")
mod = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(mod)


class PipelineContractTests(unittest.TestCase):
    def test_priority_closes_work_before_new_claim(self):
        self.assertGreater(mod.REVIEW_PRIORITY, mod.REWORK_PRIORITY)
        self.assertGreater(mod.REWORK_PRIORITY, mod.NEW_INVESTIGATION_PRIORITY)

    def test_todo_is_live(self):
        self.assertIn("todo", mod.LIVE_KANBAN_STATUSES)

    def test_three_review_cycles_total(self):
        self.assertEqual(mod.MAX_REVIEW_CYCLES, 3)

    def test_kb_query_excludes_suspected_cause(self):
        args = mod.default_args()
        ticket = {
            "BriefDetails": "real symptom",
            "Description": "description",
            "ProblemCategory": "quality",
            "HermesAreaName": "SMS",
            "ExtractedEntitiesJson": "{}",
            "SuspectedCause": "CONFIRMATION_BIAS_SENTINEL",
        }
        captured = {}

        class Result:
            returncode = 0
            stdout = json.dumps({"solutions": []})
            stderr = ""

        def fake_run(cmd, **kwargs):
            captured["cmd"] = cmd
            return Result()

        with patch.object(mod.subprocess, "run", fake_run):
            mod._run_kb_retrieval(args, ticket)
        query = captured["cmd"][captured["cmd"].index("--query") + 1]
        self.assertNotIn("CONFIRMATION_BIAS_SENTINEL", query)
        self.assertIn("real symptom", query)

    def test_default_investigator_is_jev_first_profile(self):
        self.assertEqual(mod.INVESTIGATOR_PROFILE, "l2-jev-investigator")

    def test_jev_primary_review_can_directly_approve_safe_proposal(self):
        proposal = {
            "run_id": "r1", "ticket_id": "t1", "response_type": "RESOLUTION",
            "reply_text": "Verified resolution.", "root_cause": "Confirmed cause",
        }
        result = {
            "ok": True,
            "answers": {
                "decision": {
                    "type": "choice", "choice": "APPROVE", "confidence": 0.96,
                    "probabilities": {"APPROVE": 0.96, "LOCAL_REVIEW": 0.04},
                },
                "rework_reason": {
                    "type": "choice", "choice": "OTHER", "confidence": 0.8,
                    "probabilities": {"OTHER": 0.8},
                },
                "evidence_supports_core_claim": {"type": "noul", "noul": 0.96},
                "reply_overstates_evidence": {"type": "noul", "noul": 0.04},
                "reply_claims_action_was_performed": {"type": "noul", "noul": 0.05},
                "audit_shows_claimed_action": {"type": "noul", "noul": 0.95},
                "root_cause_established": {"type": "noul", "noul": 0.90},
                "response_type_fit": {"type": "noul", "noul": 0.94},
                "needs_deep_local_reasoning": {"type": "noul", "noul": 0.06},
                "publication_risk": {
                    "type": "score", "score": 0.2, "confidence": 0.9,
                    "probabilities": {"0": 0.8, "1": 0.2},
                },
            },
        }
        with patch.object(mod, "_proposal_preflight_state", return_value={"proposal": proposal}), \
             patch.object(mod, "_run_jev_workflow", return_value={"ok": True, "result": result}):
            review = mod._jev_primary_review(mod.default_args(), proposal)
        self.assertEqual(review["action"], "APPROVE")
        self.assertGreater(review["decision_confidence"], 0.9)

    def test_jev_approve_falls_to_local_review_when_safety_gate_disagrees(self):
        proposal = {
            "run_id": "r1", "ticket_id": "t1", "response_type": "RESOLUTION",
            "reply_text": "Fixed.", "root_cause": "Maybe",
        }
        result = {
            "ok": True,
            "answers": {
                "decision": {
                    "type": "choice", "choice": "APPROVE", "confidence": 0.95,
                    "probabilities": {"APPROVE": 0.95},
                },
                "rework_reason": {
                    "type": "choice", "choice": "ROOT_CAUSE", "confidence": 0.8,
                    "probabilities": {"ROOT_CAUSE": 0.8},
                },
                "evidence_supports_core_claim": {"type": "noul", "noul": 0.55},
                "reply_overstates_evidence": {"type": "noul", "noul": 0.75},
                "reply_claims_action_was_performed": {"type": "noul", "noul": 0.9},
                "audit_shows_claimed_action": {"type": "noul", "noul": 0.1},
                "root_cause_established": {"type": "noul", "noul": 0.3},
                "response_type_fit": {"type": "noul", "noul": 0.5},
                "needs_deep_local_reasoning": {"type": "noul", "noul": 0.8},
                "publication_risk": {
                    "type": "score", "score": 2.8, "confidence": 0.95,
                    "probabilities": {"3": 0.8},
                },
            },
        }
        with patch.object(mod, "_proposal_preflight_state", return_value={"proposal": proposal}), \
             patch.object(mod, "_run_jev_workflow", return_value={"ok": True, "result": result}):
            review = mod._jev_primary_review(mod.default_args(), proposal)
        self.assertEqual(review["action"], "LOCAL_REVIEW")

    def test_jev_high_confidence_rework_skips_local_reviewer(self):
        proposal = {
            "run_id": "r1", "ticket_id": "t1", "response_type": "UPDATE",
            "reply_text": "Current update.",
        }
        result = {
            "ok": True,
            "answers": {
                "decision": {
                    "type": "choice", "choice": "REWORK", "confidence": 0.94,
                    "probabilities": {"REWORK": 0.94},
                },
                "rework_reason": {
                    "type": "choice", "choice": "EVIDENCE_GAP", "confidence": 0.91,
                    "probabilities": {"EVIDENCE_GAP": 0.91},
                },
                "evidence_supports_core_claim": {"type": "noul", "noul": 0.2},
                "reply_overstates_evidence": {"type": "noul", "noul": 0.2},
                "reply_claims_action_was_performed": {"type": "noul", "noul": 0.1},
                "audit_shows_claimed_action": {"type": "noul", "noul": 1.0},
                "root_cause_established": {"type": "noul", "noul": 0.2},
                "response_type_fit": {"type": "noul", "noul": 0.7},
                "needs_deep_local_reasoning": {"type": "noul", "noul": 0.2},
                "publication_risk": {
                    "type": "score", "score": 1.2, "confidence": 0.9,
                    "probabilities": {"1": 0.8},
                },
            },
        }
        with patch.object(mod, "_proposal_preflight_state", return_value={"proposal": proposal}), \
             patch.object(mod, "_run_jev_workflow", return_value={"ok": True, "result": result}):
            review = mod._jev_primary_review(mod.default_args(), proposal)
        self.assertEqual(review["action"], "REWORK")
        self.assertEqual(review["reason_code"], "EVIDENCE_GAP")

    def test_jev_first_investigation_gathers_only_selected_bounded_probe(self):
        plan = {
            "ok": True,
            "answers": {
                "inspect_c0": {"type": "noul", "noul": 0.95},
                "value_c0": {"type": "score", "score": 2.7, "confidence": 0.9},
                "inspect_c1": {"type": "noul", "noul": 0.20},
                "value_c1": {"type": "score", "score": 1.0, "confidence": 0.8},
                "needs_local_reasoning_before_probe": {"type": "noul", "noul": 0.1},
                "plan_complexity": {"type": "score", "score": 0.8, "confidence": 0.9},
            },
        }
        assessment = {
            "ok": True,
            "answers": {
                "evidence_sufficient": {"type": "noul", "noul": 0.95},
                "response_type": {
                    "type": "choice", "choice": "UPDATE", "confidence": 0.95,
                    "probabilities": {"UPDATE": 0.95},
                },
                "execution_mode": {
                    "type": "choice", "choice": "COMPOSE_ONLY", "confidence": 0.95,
                    "probabilities": {"COMPOSE_ONLY": 0.95},
                },
                "needs_additional_probe": {"type": "noul", "noul": 0.10},
                "needs_local_model": {"type": "noul", "noul": 0.10},
                "needs_route_skill": {"type": "noul", "noul": 0.10},
                "human_action_required": {"type": "noul", "noul": 0.10},
                "confidence_quality": {"type": "score", "score": 2.5, "confidence": 0.95},
            },
        }

        def fake_jev(workflow, state, **kwargs):
            if workflow == "evidence_plan":
                return {"ok": True, "result": plan}
            if workflow == "investigation_assessment":
                self.assertEqual(len(state["live_probes"]), 1)
                return {"ok": True, "result": assessment}
            raise AssertionError(workflow)

        with patch.object(mod, "_run_jev_workflow", side_effect=fake_jev), \
             patch.object(mod, "_run_xstudio_bridge", return_value={"ok": True, "probe_possible": True, "rows": [{"HeatNo": "H1"}]}) as probe:
            package = mod._jev_first_investigation(
                ticket={"HeatNo": "H1"},
                ticket_context={"TicketNo": "T1", "HeatNo": "H1", "BriefDetails": "heat issue"},
                run_id="r1",
                ticket_id="t1",
                suggested_tables=[
                    {"database": "XStudio_Xbatch", "table": "dbo.Heat_A", "matched_columns": ["HeatNo"]},
                    {"database": "XStudio_Xbatch", "table": "dbo.Heat_B", "matched_columns": ["HeatNo"]},
                ],
                kb_retrieval={"solutions": [], "ticket_characterization": {}, "route_candidates": []},
            )
        self.assertEqual(probe.call_count, 1)
        self.assertEqual(package["execution_mode"], "COMPOSE_ONLY")
        self.assertEqual(package["local_model_scope"], "COMPOSE_ONLY")
        self.assertEqual(package["max_additional_live_reads"], 0)
        self.assertFalse(package["load_route_skill"])

    def test_execution_contract_allows_qwen_free_only_for_high_confidence_handoff(self):
        assessment = {
            "ok": True,
            "answers": {
                "evidence_sufficient": {"type": "noul", "noul": 0.97},
                "response_type": {
                    "type": "choice", "choice": "L3_ESCALATION", "confidence": 0.96,
                    "probabilities": {"L3_ESCALATION": 0.96},
                },
                "execution_mode": {
                    "type": "choice", "choice": "QWEN_FREE", "confidence": 0.95,
                    "probabilities": {"QWEN_FREE": 0.95},
                },
                "needs_additional_probe": {"type": "noul", "noul": 0.05},
                "needs_local_model": {"type": "noul", "noul": 0.03},
                "needs_route_skill": {"type": "noul", "noul": 0.1},
                "human_action_required": {"type": "noul", "noul": 0.1},
                "confidence_quality": {"type": "score", "score": 2.9, "confidence": 0.95},
            },
        }
        contract = mod._resolve_execution_contract(assessment)
        self.assertEqual(contract["execution_mode"], "QWEN_FREE")
        self.assertEqual(contract["local_model_scope"], "COMPOSE_ONLY")
        self.assertEqual(contract["max_additional_live_reads"], 0)
        self.assertFalse(contract["load_route_skill"])

    def test_execution_contract_loads_route_skill_only_when_jev_says_it_matters(self):
        assessment = {
            "ok": True,
            "answers": {
                "evidence_sufficient": {"type": "noul", "noul": 0.55},
                "response_type": {
                    "type": "choice", "choice": "UPDATE", "confidence": 0.8,
                    "probabilities": {"UPDATE": 0.8},
                },
                "execution_mode": {
                    "type": "choice", "choice": "FOCUSED_REASONING", "confidence": 0.9,
                    "probabilities": {"FOCUSED_REASONING": 0.9},
                },
                "needs_additional_probe": {"type": "noul", "noul": 0.7},
                "needs_local_model": {"type": "noul", "noul": 0.9},
                "needs_route_skill": {"type": "noul", "noul": 0.9},
                "human_action_required": {"type": "noul", "noul": 0.1},
                "confidence_quality": {"type": "score", "score": 1.5, "confidence": 0.9},
            },
        }
        contract = mod._resolve_execution_contract(assessment)
        self.assertEqual(contract["execution_mode"], "FOCUSED_REASONING")
        self.assertTrue(contract["load_route_skill"])
        self.assertEqual(contract["max_additional_live_reads"], 3)

    def test_execution_contract_downgrades_qwen_free_resolution_to_compose_only(self):
        assessment = {
            "ok": True,
            "answers": {
                "evidence_sufficient": {"type": "noul", "noul": 0.98},
                "response_type": {
                    "type": "choice", "choice": "RESOLUTION", "confidence": 0.98,
                    "probabilities": {"RESOLUTION": 0.98},
                },
                "execution_mode": {
                    "type": "choice", "choice": "QWEN_FREE", "confidence": 0.98,
                    "probabilities": {"QWEN_FREE": 0.98},
                },
                "needs_additional_probe": {"type": "noul", "noul": 0.02},
                "needs_local_model": {"type": "noul", "noul": 0.02},
                "needs_route_skill": {"type": "noul", "noul": 0.1},
                "human_action_required": {"type": "noul", "noul": 0.0},
                "confidence_quality": {"type": "score", "score": 3.0, "confidence": 0.98},
            },
        }
        contract = mod._resolve_execution_contract(assessment)
        self.assertEqual(contract["execution_mode"], "COMPOSE_ONLY")
        self.assertIsNone(mod._qwen_free_proposal(
            run_id="r1",
            ticket_id="t1",
            ticket_context={"BriefDetails": "known issue"},
            probes=[],
            execution_contract=contract,
        ))

    def test_qwen_free_proposal_is_deterministic_handoff_not_resolution(self):
        contract = {
            "execution_mode": "QWEN_FREE",
            "response_type": "NEEDS_HUMAN_ACTION",
        }
        proposal = mod._qwen_free_proposal(
            run_id="r1",
            ticket_id="t1",
            ticket_context={"BriefDetails": "configuration correction required"},
            probes=[{
                "candidate": {"database": "XStudio_Xbatch", "table": "dbo.Config"},
                "probe": {
                    "ok": True,
                    "probe_possible": True,
                    "identifier": {"column": "BatchNo", "value": "B1"},
                    "rows": [{"BatchNo": "B1"}],
                },
            }],
            execution_contract=contract,
        )
        self.assertIsNotNone(proposal)
        self.assertEqual(proposal["response_type"], "NEEDS_HUMAN_ACTION")
        self.assertEqual(proposal["execution_mode"], "QWEN_FREE")
        self.assertNotIn("resolved", proposal["reply_text"].lower())
        self.assertIn("did not apply", proposal["reply_text"].lower())

    def test_qwen_free_handoff_requires_exact_workflow_binding_before_review(self):
        proposal = {
            "run_id": "r1",
            "ticket_id": "t1",
            "response_type": "L3_ESCALATION",
            "reply_text": "handoff",
        }
        with patch.object(mod, "_jev_primary_review") as review, \
             patch.object(mod, "_publish_frozen_proposal") as publish:
            result, reason = mod._try_qwen_free_handoff(
                mod.default_args(),
                {"l3_ticket_status": None},
                proposal,
            )
        self.assertIsNone(result)
        self.assertIn("no exact terminal status", reason)
        review.assert_not_called()
        publish.assert_not_called()

    def test_qwen_free_handoff_still_requires_jev_primary_approval(self):
        proposal = {
            "run_id": "r1",
            "ticket_id": "t1",
            "response_type": "L3_ESCALATION",
            "reply_text": "handoff",
        }
        with patch.object(
            mod, "_jev_primary_review",
            return_value={"action": "APPROVE", "ok": True},
        ) as review, patch.object(
            mod, "_publish_frozen_proposal",
            return_value="published",
        ) as publish:
            result, reason = mod._try_qwen_free_handoff(
                mod.default_args(),
                {"l3_ticket_status": "Escalated"},
                proposal,
            )
        self.assertIsNone(reason)
        self.assertEqual(result["status"], "JEV_QWEN_FREE_PUBLISHED")
        self.assertEqual(result["investigator_task_id"], None)
        review.assert_called_once()
        publish.assert_called_once()

    def test_context_budget_is_smaller_for_compose_only_than_focused_reasoning(self):
        self.assertLess(
            mod._context_budget_for_mode("COMPOSE_ONLY"),
            mod._context_budget_for_mode("FOCUSED_REASONING"),
        )
        self.assertLess(
            mod._context_budget_for_mode("QWEN_FREE"),
            mod._context_budget_for_mode("COMPOSE_ONLY"),
        )

    def test_jev_disabled_still_builds_deterministic_context_chunks(self):
        with patch.dict(
            mod.os.environ,
            {"CHITRAGUPTA_JEV_FIRST_INVESTIGATION_ENABLED": "0"},
            clear=False,
        ), patch.object(mod, "_run_jev_workflow") as jev, patch.object(
            mod, "_run_xstudio_bridge"
        ) as probe:
            package = mod._jev_first_investigation(
                ticket={"HeatNo": "H1"},
                ticket_context={"TicketNo": "T1", "HeatNo": "H1", "BriefDetails": "heat issue"},
                run_id="r1",
                ticket_id="t1",
                suggested_tables=[
                    {"database": "XStudio_Xbatch", "table": "dbo.Heat_A", "matched_columns": ["HeatNo"]},
                ],
                kb_retrieval={
                    "solutions": [{"kb_id": "solution:1", "title": "Known issue"}],
                    "ticket_characterization": {},
                    "route_candidates": [{"route": "heat_execution"}],
                },
                prior_ledger={"summary": "prior verified fact"},
                prior_attempts=[{"ProcessStatus": "FAILED"}],
            )
        jev.assert_not_called()
        probe.assert_not_called()
        self.assertFalse(package["enabled"])
        self.assertEqual(package["local_model_scope"], "FOCUSED_REASONING")
        self.assertEqual(package["max_additional_live_reads"], 3)
        chunk_ids = {chunk["id"] for chunk in package["context_chunks"]}
        self.assertIn("ticket", chunk_ids)
        self.assertIn("routing", chunk_ids)
        self.assertIn("prior_ledger", chunk_ids)
        self.assertIn("candidate_backlog", chunk_ids)
        view = mod._compile_model_context(
            package["context_chunks"], package["assessment"], budget_chars=5000
        )
        self.assertIn("ticket", {row["id"] for row in view["chunks"]})

    def test_context_compiler_pins_ticket_and_live_evidence_even_when_jev_scores_low(self):
        chunks = [
            {
                "id": "ticket", "kind": "ticket", "authority": "CURRENT_TICKET",
                "source": "ticket", "attention_question": "context_c0",
                "minimum_level": 2, "fallback_level": 3,
                "content": {"BriefDetails": "current symptom"},
                "compact": {"BriefDetails": "current symptom"},
                "summary": {"BriefDetails": "current symptom"},
            },
            {
                "id": "kb_solution_0", "kind": "knowledge", "authority": "APPROVED_KB_LEAD",
                "source": "solution:1", "attention_question": "context_c1",
                "minimum_level": 0, "fallback_level": 1,
                "content": {"title": "old issue"}, "compact": {"title": "old issue"},
                "summary": {"title": "old issue"},
            },
            {
                "id": "live_probe_0", "kind": "live_evidence", "authority": "LIVE_SQL_EVIDENCE",
                "source": "XStudio_Xbatch.dbo.Heat", "attention_question": "context_c2",
                "minimum_level": 2, "fallback_level": 3,
                "content": {"rows": [{"HeatNo": "H1", "Status": "Failed"}]},
                "compact": {"rows": [{"HeatNo": "H1", "Status": "Failed"}]},
                "summary": {"row_count": 1},
            },
        ]
        assessment = {
            "ok": True,
            "answers": {
                "context_c0": {"type": "score", "score": 0.0, "confidence": 0.9},
                "context_c1": {"type": "score", "score": 0.0, "confidence": 0.9},
                "context_c2": {"type": "score", "score": 0.0, "confidence": 0.9},
                "known_solution": {"type": "choice", "choice": "NONE", "confidence": 0.9},
            },
        }
        view = mod._compile_model_context(chunks, assessment, budget_chars=4000)
        included = {row["id"]: row for row in view["chunks"]}
        self.assertIn("ticket", included)
        self.assertIn("live_probe_0", included)
        self.assertEqual(included["ticket"]["presentation"], "COMPACT")
        self.assertEqual(included["live_probe_0"]["presentation"], "COMPACT")
        self.assertNotIn("kb_solution_0", included)
        self.assertEqual(view["omitted"][0]["id"], "kb_solution_0")

    def test_context_compiler_pins_jev_selected_known_solution(self):
        chunks = [{
            "id": "kb_solution_0", "kind": "knowledge", "authority": "APPROVED_KB_LEAD",
            "source": "solution:1", "attention_question": "context_c0",
            "minimum_level": 0, "fallback_level": 1,
            "content": {"title": "known fix", "resolution_steps": "verified steps"},
            "compact": {"title": "known fix", "resolution_steps": "verified steps"},
            "summary": {"title": "known fix"},
        }]
        assessment = {
            "ok": True,
            "answers": {
                "known_solution": {"type": "choice", "choice": "s0", "confidence": 0.95},
                "context_c0": {"type": "score", "score": 0.0, "confidence": 0.9},
            },
        }
        view = mod._compile_model_context(chunks, assessment, budget_chars=2000)
        self.assertEqual(view["chunks"][0]["id"], "kb_solution_0")
        self.assertEqual(view["chunks"][0]["presentation"], "COMPACT")

    def test_context_compiler_omits_whole_low_value_chunk_instead_of_global_truncation(self):
        huge = "x" * 12000
        chunks = [{
            "id": "history", "kind": "history", "authority": "HISTORICAL_RUNS",
            "source": "prior attempts", "attention_question": "context_c0",
            "minimum_level": 0, "fallback_level": 1,
            "content": {"text": huge}, "compact": {"text": huge},
            "summary": {"text": huge},
        }]
        assessment = {
            "ok": True,
            "answers": {"context_c0": {"type": "score", "score": 2.9, "confidence": 0.9}},
        }
        view = mod._compile_model_context(chunks, assessment, budget_chars=100)
        self.assertEqual(view["chunks"], [])
        self.assertEqual(view["omitted"][0]["reason"], "context budget")
        # The compiler result remains valid structured JSON; no assembled JSON string is sliced.
        json.loads(json.dumps(view))

    def test_process_approvals_skips_inactive_history_without_publish_queries(self):
        tasks = [
            {
                "id": "review-new",
                "status": "done",
                "assignee": mod.REVIEWER_PROFILE,
                "body": (
                    "run_id: r-new\n"
                    "ticket_id: t-new\n"
                    'proposal_json: {"run_id":"r-new","ticket_id":"t-new","response_type":"UPDATE","reply_text":"new"}'
                ),
            },
            {
                "id": "review-old",
                "status": "done",
                "assignee": mod.REVIEWER_PROFILE,
                "body": (
                    "run_id: r-old\n"
                    "ticket_id: t-old\n"
                    'proposal_json: {"run_id":"r-old","ticket_id":"t-old","response_type":"UPDATE","reply_text":"old"}'
                ),
            },
        ]

        with patch.object(
            mod, "_publish_frozen_proposal", return_value="published"
        ) as publish:
            counts = mod.process_approvals(
                mod.default_args(),
                dry_run=True,
                tasks=tasks,
                active_run_ids={"r-new"},
            )

        self.assertEqual(counts["published"], 1)
        self.assertEqual(counts["inactive_skipped"], 1)
        self.assertEqual(counts["blocked_configuration"], 0)
        self.assertEqual(counts["rework_created"], 0)
        publish.assert_called_once()
        self.assertEqual(publish.call_args.args[1]["run_id"], "r-new")

    def test_reconcile_with_no_active_runs_does_not_walk_historical_completions(self):
        historical = [{
            "id": "old-investigator",
            "status": "done",
            "assignee": mod.INVESTIGATOR_PROFILE,
            "body": "run_id: old-run\nticket_id: old-ticket",
        }]
        with patch.object(mod, "list_tasks", return_value=historical) as tasks, \
             patch.object(mod, "query_active_runs", return_value=[]) as active, \
             patch.object(mod, "latest_done_run") as latest, \
             patch.object(mod, "_publish_frozen_proposal") as publish:
            result = mod.reconcile(mod.default_args(), dry_run=True)

        tasks.assert_called_once()
        active.assert_called_once()
        latest.assert_not_called()
        publish.assert_not_called()
        self.assertEqual(result["snapshot"]["active_run_count"], 0)
        self.assertEqual(result["snapshot"]["kanban_task_count"], 1)
        self.assertEqual(result["local_reviewer_approvals"]["published"], 0)


    def test_resolution_fails_closed_without_binding(self):
        with self.assertRaises(RuntimeError):
            mod._status_args_for_response(
                {"strict_resolution_status_binding": True, "resolved_ticket_status": None},
                {"response_type": "RESOLUTION", "new_ticket_status": "model-guessed"},
            )

    def test_binding_owns_resolution_status(self):
        argv, expected = mod._status_args_for_response(
            {
                "strict_resolution_status_binding": True,
                "resolved_ticket_status": "REAL_RESOLVED",
                "allow_metadata_status_override": False,
            },
            {"response_type": "RESOLUTION", "new_ticket_status": "MODEL_GUESS"},
        )
        self.assertEqual(expected, "REAL_RESOLVED")
        self.assertEqual(argv, ["--new-ticket-status", "REAL_RESOLVED"])

    def test_hermes_executable_resolution(self):
        with patch.object(mod.shutil, "which", return_value="/custom/bin/hermes"):
            self.assertEqual(mod._hermes_executable(), "/custom/bin/hermes")
        with patch.object(mod.shutil, "which", return_value=None), \
             patch.object(mod.Path, "exists", return_value=False):
            self.assertEqual(mod._hermes_executable(), "hermes")

    def test_is_reviewer_rejection_detection(self):
        task_blocked = {"id": "t1", "status": "blocked", "assignee": mod.REVIEWER_PROFILE}
        self.assertTrue(mod.is_reviewer_rejection(task_blocked))

        task_reject_result = {"id": "t2", "status": "done", "result": "REJECT", "assignee": mod.REVIEWER_PROFILE}
        self.assertTrue(mod.is_reviewer_rejection(task_reject_result))

        task_reject_run = {"id": "t3", "status": "done", "result": "", "assignee": mod.REVIEWER_PROFILE}
        with patch.object(mod, "get_runs", return_value=[{"profile": mod.REVIEWER_PROFILE, "summary": "Rejected frozen proposal for Ticket_123: unsupported"}]):
            self.assertTrue(mod.is_reviewer_rejection(task_reject_run))

        task_approved = {"id": "t4", "status": "done", "result": "SUCCESS", "assignee": mod.REVIEWER_PROFILE}
        with patch.object(mod, "get_runs", return_value=[{"profile": mod.REVIEWER_PROFILE, "summary": "Approved frozen proposal"}]):
            self.assertFalse(mod.is_reviewer_rejection(task_approved))

    def test_process_approvals_skips_rejected_done_tasks(self):
        tasks = [
            {
                "id": "review-rejected",
                "assignee": mod.REVIEWER_PROFILE,
                "status": "done",
                "result": "REJECT",
                "body": (
                    "run_id: r-rej\n"
                    "ticket_id: t-rej\n"
                    'proposal_json: {"run_id":"r-rej","ticket_id":"t-rej","response_type":"UPDATE","reply_text":"bad"}'
                ),
            },
        ]
        with patch.object(mod, "list_tasks", return_value=tasks), \
             patch.object(mod, "query_active_runs", return_value=[{"ID": "r-rej"}]), \
             patch.object(mod, "_publish_frozen_proposal") as publish:
            counts = mod.process_approvals(mod.default_args(), dry_run=True)
        publish.assert_not_called()
        self.assertEqual(counts["published"], 0)

    def test_process_rejections_handles_done_tasks_with_rejection(self):
        task = {
            "id": "t-done-rej",
            "assignee": mod.REVIEWER_PROFILE,
            "status": "done",
            "result": "REJECT",
            "body": "run_id: r1\nticket_id: t1\ninvestigation_task_id: t-inv\nreview_cycle: 0\n",
        }
        with patch.object(mod, "list_tasks", return_value=[task]), \
             patch.object(mod, "query_active_runs", return_value=[{"ID": "r1"}]), \
             patch.object(mod, "_source_has_rework", return_value=False), \
             patch.object(mod, "get_runs", return_value=[{"summary": "Rejected: bad claims"}]), \
             patch.object(mod, "create_rework_card", return_value="created") as rework:
            count = mod.process_rejections(mod.default_args(), dry_run=True)
        self.assertEqual(count, 1)
        rework.assert_called_once()


if __name__ == "__main__":
    unittest.main()
