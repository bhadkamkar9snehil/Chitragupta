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


    def test_capacity_env_parser_fails_safe_and_clamps(self):
        with patch.dict(mod.os.environ, {"TEST_CAPACITY": "not-an-int"}, clear=False):
            self.assertEqual(
                mod._int_env("TEST_CAPACITY", 8, minimum=1, maximum=64),
                8,
            )
        with patch.dict(mod.os.environ, {"TEST_CAPACITY": "999"}, clear=False):
            self.assertEqual(
                mod._int_env("TEST_CAPACITY", 8, minimum=1, maximum=64),
                64,
            )

    def test_dispatch_local_model_does_nothing_when_sql_slot_busy(self):
        with patch.object(
            mod, "run_orchestrator", return_value={"AcquireStatus": "BUSY"}
        ) as orchestrator, patch.object(mod, "run_hermes") as hermes:
            result = mod._dispatch_next_local_model_task(mod.default_args(), tasks=[])

        self.assertEqual(result["status"], "BUSY")
        orchestrator.assert_called_once()
        hermes.assert_not_called()

    def test_dispatch_local_model_creates_exactly_one_task_and_binds_it(self):
        spec = {
            "title": "L2 Ticket_999",
            "assignee": mod.INVESTIGATOR_PROFILE,
            "body": "run_id: r1\nticket_id: t1\npipeline_stage: investigation",
            "priority": mod.NEW_INVESTIGATION_PRIORITY,
            "skills": ["xstudio-l2-ticket-workflow"],
            "idempotency_key": "l2-ticket-r1",
            "max_runtime": "20m",
        }
        acquired = {
            "AcquireStatus": "ACQUIRED",
            "RunID": "r1",
            "TicketID": "t1",
            "LocalModelPurpose": "INVESTIGATION",
            "LocalModelWorkKey": "investigation-r1-0",
            "PendingLocalModelJson": json.dumps(spec),
        }

        class HermesResult:
            returncode = 0
            stdout = '{"id":"t_qwen"}'
            stderr = ""

        def orchestrator(_args, extra, **_kwargs):
            if extra == ["--local-model-action", "acquire"]:
                return acquired
            self.assertEqual(extra[:2], ["--local-model-action", "bind"])
            self.assertIn("t_qwen", extra)
            return {"LocalModelTaskID": "t_qwen"}

        with patch.object(mod, "run_orchestrator", side_effect=orchestrator) as orch, \
             patch.object(mod, "run_hermes", return_value=HermesResult()) as hermes:
            result = mod._dispatch_next_local_model_task(mod.default_args(), tasks=[])

        self.assertEqual(result["status"], "DISPATCHED")
        self.assertEqual(result["task_id"], "t_qwen")
        self.assertEqual(result["purpose"], "INVESTIGATION")
        self.assertEqual(hermes.call_count, 1)
        self.assertEqual(orch.call_count, 2)

    def test_dispatch_local_model_requeues_when_kanban_create_fails(self):
        spec = {
            "title": "L2 Ticket_999",
            "assignee": mod.INVESTIGATOR_PROFILE,
            "body": "run_id: r1\nticket_id: t1",
            "priority": mod.NEW_INVESTIGATION_PRIORITY,
            "skills": [],
            "idempotency_key": "l2-ticket-r1",
            "max_runtime": "20m",
        }
        acquired = {
            "AcquireStatus": "ACQUIRED",
            "RunID": "r1",
            "TicketID": "t1",
            "LocalModelPurpose": "INVESTIGATION",
            "LocalModelWorkKey": "investigation-r1-0",
            "PendingLocalModelJson": json.dumps(spec),
        }

        class HermesResult:
            returncode = 1
            stdout = ""
            stderr = "create failed"

        calls = []
        def orchestrator(_args, extra, **_kwargs):
            calls.append(extra)
            if extra == ["--local-model-action", "acquire"]:
                return acquired
            self.assertIn("finish", extra)
            self.assertIn("REQUEUE", extra)
            return {"LocalModelState": "QUEUED"}

        with patch.object(mod, "run_orchestrator", side_effect=orchestrator), \
             patch.object(mod, "run_hermes", return_value=HermesResult()):
            result = mod._dispatch_next_local_model_task(mod.default_args(), tasks=[])

        self.assertEqual(result["status"], "CREATE_FAILED_REQUEUED")
        self.assertEqual(len(calls), 2)

    def test_sync_local_model_completion_releases_only_terminal_bound_task(self):
        tasks = [
            {"id": "t_done", "status": "done"},
            {"id": "t_running", "status": "running"},
        ]
        active = [
            {
                "ID": "r1",
                "LocalModelState": "RUNNING",
                "LocalModelTaskID": "t_done",
            },
            {
                "ID": "r2",
                "LocalModelState": "RUNNING",
                "LocalModelTaskID": "t_running",
            },
        ]
        with patch.object(mod, "_finish_local_model_work", return_value={}) as finish:
            released = mod._sync_local_model_completions(
                mod.default_args(), tasks, active
            )

        self.assertEqual(released, {"r1"})
        finish.assert_called_once_with(
            mod.default_args(),
            run_id="r1",
            task_id="t_done",
            outcome="DONE",
        )

    def test_dispatch_blocks_when_legacy_live_local_task_exists(self):
        tasks = [{
            "id": "legacy-qwen",
            "status": "running",
            "assignee": mod.INVESTIGATOR_PROFILE,
        }]
        with patch.object(mod, "run_orchestrator") as orchestrator:
            result = mod._dispatch_next_local_model_task(
                mod.default_args(), tasks=tasks
            )

        self.assertEqual(result["status"], "KANBAN_LOCAL_MODEL_BUSY")
        self.assertEqual(result["task_ids"], ["legacy-qwen"])
        orchestrator.assert_not_called()

    def test_dispatch_ignores_terminal_blocked_cards(self):
        tasks = [{
            "id": "legacy-blocked",
            "status": "blocked",
            "assignee": mod.REVIEWER_PROFILE,
        }]
        with patch.object(
            mod, "run_orchestrator", return_value={"AcquireStatus": "EMPTY"}
        ) as orchestrator:
            result = mod._dispatch_next_local_model_task(
                mod.default_args(), tasks=tasks
            )

        self.assertEqual(result["status"], "EMPTY")
        orchestrator.assert_called_once()

    def test_stale_local_model_lease_requeues_only_without_live_owner(self):
        active = [{
            "ID": "r1",
            "AgeMinutes": 60,
            "LocalModelState": "RUNNING",
            "LocalModelTaskID": "t_missing",
        }]
        with patch.object(mod, "_finish_local_model_work", return_value={}) as finish:
            requeued = mod._recover_stale_local_model_leases(
                mod.default_args(),
                [],
                active,
                stale_after_minutes=45,
            )

        self.assertEqual(requeued, {"r1"})
        finish.assert_called_once_with(
            mod.default_args(),
            run_id="r1",
            task_id="t_missing",
            outcome="REQUEUE",
        )

        live_task = [{
            "id": "t_live",
            "status": "running",
            "assignee": mod.INVESTIGATOR_PROFILE,
            "body": "run_id: r1\nticket_id: t1",
        }]
        with patch.object(mod, "_finish_local_model_work") as protected_finish:
            protected = mod._recover_stale_local_model_leases(
                mod.default_args(),
                live_task,
                active,
                stale_after_minutes=45,
            )

        self.assertEqual(protected, set())
        protected_finish.assert_not_called()

    def test_pending_primary_review_waits_for_existing_qwen_work(self):
        task = {
            "id": "t_inv",
            "status": "done",
            "assignee": mod.INVESTIGATOR_PROFILE,
            "body": "run_id: r1\nticket_id: t1",
        }
        self.assertIsNone(
            mod._pending_primary_review(
                task,
                [task],
                {"r1"},
                {"r1"},
            )
        )

    def test_pipeline_status_treats_qwen_queue_without_card_as_intentional(self):
        active = [{
            "ID": "r1",
            "TicketID": "t1",
            "LocalModelState": "QUEUED",
            "LocalModelPurpose": "INVESTIGATION",
            "LocalModelTaskID": None,
        }]
        binding = {
            "strict_resolution_status_binding": True,
            "resolved_ticket_status": "Closed",
        }
        with patch.object(mod, "list_tasks", return_value=[]), \
             patch.object(mod, "query_active_runs", return_value=active), \
             patch.object(mod, "load_workflow_binding", return_value=binding):
            result = mod.pipeline_status(mod.default_args())

        self.assertEqual(result["anomalies"], [])
        self.assertEqual(result["local_model"], {"running": 0, "queued": 1})
        self.assertEqual(result["contract"]["max_qwen_running"], 1)
        self.assertEqual(result["contract"]["max_pipeline_wip"], mod.MAX_PIPELINE_WIP)

    def test_scout_can_fill_multiple_jev_runs_but_dispatches_one_qwen(self):
        args = mod.default_args()
        args.max_pipeline_wip = 8
        args.max_qwen_waiting = 4
        binding = {
            "eligible_ticket_status": "Enter",
            "strict_resolution_status_binding": True,
            "resolved_ticket_status": "Closed",
        }
        polls = [
            {
                "status": "CLAIMED",
                "run_id": f"r{i}",
                "ticket_id": f"t{i}",
                "ticket": {"TicketNo": f"Ticket_{i}"},
            }
            for i in range(1, 6)
        ]
        poll_iter = iter(polls)

        def orchestrator(_args, extra, **_kwargs):
            self.assertIn("--poll", extra)
            return next(poll_iter)

        def prepared(_args, _binding, poll):
            return {
                "status": "QUEUED_LOCAL_MODEL",
                "run_id": poll["run_id"],
                "ticket_id": poll["ticket_id"],
                "execution_mode": "FOCUSED_REASONING",
                "queue_status": "QUEUED",
            }

        with patch.object(mod, "reconcile", return_value={}), \
             patch.object(mod, "load_workflow_binding", return_value=binding), \
             patch.object(mod, "query_active_runs", return_value=[]), \
             patch.object(mod, "run_orchestrator", side_effect=orchestrator), \
             patch.object(mod, "_prepare_claimed_ticket", side_effect=prepared), \
             patch.object(
                 mod,
                 "_dispatch_next_local_model_task",
                 return_value={"status": "DISPATCHED", "run_id": "r1", "task_id": "tq"},
             ) as dispatch:
            result = mod.scout(args)

        self.assertEqual(result["status"], "PIPELINE_FILLED")
        self.assertEqual(result["claim_count"], 5)
        self.assertEqual(result["local_model"], {"running": 1, "queued": 4})
        dispatch.assert_called_once()

    def test_local_reviewer_is_queued_instead_of_created_directly(self):
        source = {
            "id": "t_inv",
            "body": "run_id: r1\nticket_id: t1\nticket_no: Ticket_1\nreview_cycle: 0",
        }
        proposal = {
            "run_id": "r1",
            "ticket_id": "t1",
            "response_type": "UPDATE",
            "reply_text": "Verified update",
        }
        with patch.object(
            mod,
            "_queue_local_model_task",
            return_value={"QueueStatus": "QUEUED"},
        ) as queue, patch.object(mod, "run_hermes") as hermes:
            result = mod.create_reviewer_card(
                mod.default_args(),
                source_task=source,
                proposal=proposal,
            )

        self.assertEqual(result, "queued")
        kwargs = queue.call_args.kwargs
        self.assertEqual(kwargs["purpose"], "REVIEW")
        self.assertEqual(kwargs["priority"], mod.REVIEW_PRIORITY)
        hermes.assert_not_called()

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

    def test_process_rejections_handles_done_tasks_with_rejection_prefix(self):
        task = {
            "id": "t-done-rej-prefix",
            "assignee": mod.REVIEWER_PROFILE,
            "status": "done",
            "result": "REJECT - ACTION_AUTHORITY mismatch confirmed",
            "body": "run_id: r2\nticket_id: t2\ninvestigation_task_id: t-inv-2\nreview_cycle: 0\n",
        }
        with patch.object(mod, "list_tasks", return_value=[task]), \
             patch.object(mod, "query_active_runs", return_value=[{"ID": "r2"}]), \
             patch.object(mod, "_source_has_rework", return_value=False), \
             patch.object(mod, "get_runs", return_value=[{"summary": "Jev flag confirmed"}]), \
             patch.object(mod, "create_rework_card", return_value="created") as rework:
            count = mod.process_rejections(mod.default_args(), dry_run=True)
            self.assertEqual(count, 1)
            rework.assert_called_once()
            self.assertTrue(mod.is_reviewer_rejection(task))
            reason = mod.reviewer_block_reason(task)
            self.assertIn("Jev flag confirmed", reason)

    def test_rework_card_carries_same_typed_tool_contract_as_investigation(self):
        """Ticket_242 residual: rework omitted `database` on 2 xstudio_l2 calls because
        create_rework_card() never included the typed-tool routing reminder that
        _investigator_task_spec() gives every fresh investigation. Guard against
        regressing that omission."""
        source_task = {
            "id": "t-source",
            "body": "run_id: run-1\nticket_id: ticket-1\nticket_no: Ticket_999\nreview_cycle: 0\n",
        }
        captured = {}

        def fake_queue(args, *, run_id, purpose, execution_mode, priority, work_key, spec, dry_run=False):
            captured["spec"] = spec
            return {"QueueStatus": "QUEUED"}

        with patch.object(mod, "_persist_rejected_ledger", return_value=""), \
             patch.object(mod, "_source_has_rework", return_value=False), \
             patch.object(mod, "_queue_local_model_task", side_effect=fake_queue):
            result = mod.create_rework_card(
                mod.default_args(),
                source_task=source_task,
                reason="ACTION_AUTHORITY mismatch",
                investigation_task_id="t-inv",
            )
        self.assertEqual(result, "queued")
        body = captured["spec"]["body"]
        self.assertIn("Typed XStudio investigation contract", body)
        self.assertIn("Pass database explicitly", body)


    def test_queued_local_model_without_card_is_not_orphan(self):
        args = mod.default_args()
        active = [{"ID": "run-queued-1", "AgeMinutes": 60, "LocalModelState": "QUEUED"}]
        with patch.object(mod, "run_orchestrator") as orch:
            count = mod.recover_orphan_runs(args, tasks=[], active_runs=active)
        orch.assert_not_called()
        self.assertEqual(count, 0)

    def test_requeued_stale_lease_not_failed_as_orphan_same_reconcile(self):
        args = mod.default_args()
        active = [{
            "ID": "run-stale-1",
            "AgeMinutes": 60,
            "LocalModelState": "RUNNING",
            "LocalModelTaskID": "task-old",
        }]
        calls = []
        def fake_orch(a, argv, **kw):
            calls.append(argv)
            if "--local-model-action" in argv and "finish" in argv:
                return {"status": "FINISHED"}
            if "--local-model-action" in argv and "acquire" in argv:
                return {"AcquireStatus": "EMPTY"}
            return []

        with patch.object(mod, "list_tasks", return_value=[]), \
             patch.object(mod, "query_active_runs", return_value=active), \
             patch.object(mod, "run_orchestrator", side_effect=fake_orch):
            res = mod.reconcile(args)

        self.assertEqual(res["local_model_requeued_stale"], 1)
        self.assertEqual(res["orphans_recovered"], 0)
        fail_calls = [c for c in calls if "--fail-run" in c]
        self.assertEqual(len(fail_calls), 0)

    def test_blocked_and_done_cards_do_not_hold_qwen_slot(self):
        tasks = [
            {"id": "t-done", "assignee": mod.INVESTIGATOR_PROFILE, "status": "done"},
            {"id": "t-blocked", "assignee": mod.REVIEWER_PROFILE, "status": "blocked"},
            {"id": "t-failed", "assignee": mod.INVESTIGATOR_PROFILE, "status": "failed"},
            {"id": "t-cancelled", "assignee": mod.REVIEWER_PROFILE, "status": "cancelled"},
        ]
        live = mod._live_local_model_tasks(tasks)
        self.assertEqual(len(live), 0)

    def test_live_executing_card_prevents_parallel_dispatch(self):
        for status in ("ready", "running", "scheduled"):
            tasks = [{"id": f"t-{status}", "assignee": mod.INVESTIGATOR_PROFILE, "status": status}]
            live = mod._live_local_model_tasks(tasks)
            self.assertEqual(len(live), 1, f"Status {status} must be recognized as executing")

    def test_true_orphan_without_queue_or_kanban_recovered(self):
        args = mod.default_args()
        active = [{"ID": "run-orphan-1", "AgeMinutes": 60, "LocalModelState": None}]
        calls = []
        def fake_orch(a, argv, **kw):
            calls.append(argv)
            return {}

        with patch.object(mod, "run_orchestrator", side_effect=fake_orch):
            count = mod.recover_orphan_runs(args, tasks=[], active_runs=active)
        self.assertEqual(count, 1)
        self.assertTrue(any("--fail-run" in c and "run-orphan-1" in c for c in calls))

    def test_queue_local_model_passes_max_waiting(self):
        args = mod.default_args()
        args.max_qwen_waiting = 5
        spec = {
            "title": "title", "assignee": mod.INVESTIGATOR_PROFILE,
            "body": "b", "priority": 10, "idempotency_key": "k", "max_runtime": "10m"
        }
        captured_argv = []
        def fake_orch(a, argv, **kw):
            captured_argv.extend(argv)
            return {"QueueStatus": "QUEUED"}

        with patch.object(mod, "run_orchestrator", side_effect=fake_orch):
            mod._queue_local_model_task(
                args,
                run_id="r1",
                purpose="INVESTIGATION",
                execution_mode="COMPOSE_ONLY",
                priority=10,
                work_key="k1",
                spec=spec,
            )
        self.assertIn("--local-model-max-waiting", captured_argv)
        idx = captured_argv.index("--local-model-max-waiting")
        self.assertEqual(captured_argv[idx + 1], "5")

    def test_prepare_claimed_ticket_handles_backpressure(self):
        args = mod.default_args()
        poll = {"run_id": "r-bp", "ticket_id": "t-bp", "ticket": {"TicketNo": "TBP"}}
        binding = {"eligible_ticket_status": "Enter"}
        fail_calls = []
        def fake_orch(a, argv, **kw):
            if "--fail-run" in argv:
                fail_calls.append(argv)
                return {}
            if "--investigate-bundle" in argv:
                return {"ticket_id": "t-bp", "ticket": {}}
            return {}

        with patch.object(mod, "run_orchestrator", side_effect=fake_orch), \
             patch.object(mod, "_run_kb_retrieval", return_value={"solutions": []}), \
             patch.object(mod, "_jev_first_investigation", return_value={"execution_depth": "COMPOSE_ONLY"}), \
             patch.object(mod, "_try_qwen_free_handoff", return_value=(None, "not free")), \
             patch.object(mod, "_queue_local_model_task", return_value={"QueueStatus": "BACKPRESSURE"}):
            res = mod._prepare_claimed_ticket(args, binding, poll)

        self.assertEqual(res["status"], "BACKPRESSURE")
        self.assertEqual(len(fail_calls), 1)
        self.assertIn("r-bp", fail_calls[0])

    def test_safe_query_active_run_propagates_database_failure(self):
        args = mod.default_args()
        with patch.object(mod, "run_orchestrator", side_effect=RuntimeError("SQL Server connection timeout")):
            with self.assertRaises(RuntimeError):
                mod.safe_query_active_run("r-fail", args)

    def test_priority_aware_queue_admission(self):
        args = mod.default_args()
        args.max_qwen_waiting = 4
        # Demonstrates priority-aware queue admission:
        # When 4 priority-10 investigations are already queued in database:
        # 1. Another priority-10 investigation sees blocking_queued = 4 >= 4 => BACKPRESSURE
        # 2. But a priority-30 review task checks equal/higher priority (0 >= 4 is False) => QUEUED
        # Therefore, total LocalModelState='QUEUED' runs legitimately exceeds 4.
        def fake_sql_queue(a, argv, **kw):
            priority = int(argv[argv.index("--local-model-priority") + 1])
            max_waiting = int(argv[argv.index("--local-model-max-waiting") + 1])
            # 4 priority-10 tasks currently queued in DB
            queued_db = [{"Priority": 10}, {"Priority": 10}, {"Priority": 10}, {"Priority": 10}]
            if priority <= 10:
                blocking = len(queued_db)
            else:
                blocking = sum(1 for item in queued_db if item["Priority"] >= priority)
            if blocking >= max_waiting:
                return {"QueueStatus": "BACKPRESSURE", "BlockingQueued": blocking, "MaxWaiting": max_waiting}
            return {"QueueStatus": "QUEUED", "RunID": "r-admitted"}

        spec_inv = {
            "title": "inv", "assignee": mod.INVESTIGATOR_PROFILE,
            "body": "b", "priority": 10, "idempotency_key": "k-inv", "max_runtime": "10m"
        }
        spec_rev = {
            "title": "rev", "assignee": mod.REVIEWER_PROFILE,
            "body": "b", "priority": 30, "idempotency_key": "k-rev", "max_runtime": "15m"
        }

        with patch.object(mod, "run_orchestrator", side_effect=fake_sql_queue):
            res_inv = mod._queue_local_model_task(
                args, run_id="r-inv", purpose="INVESTIGATION",
                execution_mode="COMPOSE_ONLY", priority=10, work_key="k-inv", spec=spec_inv
            )
            res_rev = mod._queue_local_model_task(
                args, run_id="r-rev", purpose="REVIEW",
                execution_mode="FOCUSED_REASONING", priority=30, work_key="k-rev", spec=spec_rev
            )

        self.assertEqual(res_inv["QueueStatus"], "BACKPRESSURE")
        self.assertEqual(res_rev["QueueStatus"], "QUEUED")

    def test_l3_exists_propagates_database_failure(self):
        args = mod.default_args()
        with patch.object(mod, "run_orchestrator", side_effect=RuntimeError("SQL Server connection timeout")):
            with self.assertRaises(RuntimeError):
                mod._l3_exists(args, "r-fail")


if __name__ == "__main__":
    unittest.main()
