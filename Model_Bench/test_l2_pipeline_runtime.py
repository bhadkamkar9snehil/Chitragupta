import importlib.util
import json
import sys
import tempfile
import unittest
from datetime import datetime, timedelta
from pathlib import Path
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location("l2_pipeline_runtime", "Model_Bench/l2_pipeline_runtime.py")
mod = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(mod)

ORCH_SPEC = importlib.util.spec_from_file_location("hermes_orchestrator", "Hermes_Orchestrator.py")
orchestrator = importlib.util.module_from_spec(ORCH_SPEC)
assert ORCH_SPEC.loader
ORCH_SPEC.loader.exec_module(orchestrator)

SUMMARY_SPEC = importlib.util.spec_from_file_location(
    "generate_readable_trace_summary", "Model_Bench/generate_readable_trace_summary.py"
)
summary = importlib.util.module_from_spec(SUMMARY_SPEC)
assert SUMMARY_SPEC.loader
SUMMARY_SPEC.loader.exec_module(summary)


class PipelineContractTests(unittest.TestCase):
    def test_incomplete_update_requires_concrete_continuation(self):
        proposal = {"response_type": "UPDATE", "evidence_status": "INCOMPLETE"}
        self.assertTrue(mod.continuation_issues(proposal))
        proposal["next_investigation_step"] = "Inspect the update procedure for the identified record."
        self.assertEqual([], mod.continuation_issues(proposal))
        proposal["response_type"] = "QUESTION"
        proposal.pop("next_investigation_step")
        self.assertEqual([], mod.continuation_issues(proposal))

    def test_omitted_material_flag_cannot_bypass_evidence_validation(self):
        valid, issues = mod.validate_claims_contract([
            {"id": "C1", "claim": "Fixed", "status": "VERIFIED"}])
        self.assertFalse(valid)
        self.assertTrue(issues)

    def test_failed_action_is_not_evidence_for_verified_claim(self):
        valid, issues = mod.validate_claims_contract([
            {"id": "C1", "claim": "Fixed", "material": True, "status": "VERIFIED",
             "evidence": [{"action_id": "a"}]}], run_id="r", ticket_id="t",
            actions=[{"ID": "a", "RunID": "r", "TicketID": "t", "Status": "FAILED"}])
        self.assertFalse(valid)
        self.assertTrue(issues)

    def test_resolution_requires_complete_verified_outcome(self):
        proposal = {"response_type": "RESOLUTION", "evidence_status": "INCOMPLETE",
                    "claims": [{"id": "C1", "status": "UNVERIFIED", "material": True}],
                    "reply_text": "The cause is not established."}
        self.assertTrue(mod.resolution_issues(proposal))
        proposal.update(evidence_status="COMPLETE", resolution="The reported record is visible now.")
        proposal["claims"][0].update(status="VERIFIED", evidence=[{"action_id": "a"}])
        self.assertEqual([], mod.resolution_issues(proposal))
        proposal.pop("resolution")
        self.assertTrue(mod.resolution_issues(proposal))

    def test_incomplete_resolution_goes_to_rework_before_publication(self):
        proposal = {"run_id": "run-1", "ticket_id": "ticket-1", "response_type": "RESOLUTION",
                    "reply_text": "Evidence status: INCOMPLETE. Proposed correction only.",
                    "evidence_status": "INCOMPLETE", "claims": [
                        {"id": "C1", "claim": "Proposed fix", "status": "UNVERIFIED", "material": True}]}
        task = {"id": "reviewer-1", "assignee": mod.REVIEWER_PROFILE, "status": "done",
                "body": f"run_id: run-1\nticket_id: ticket-1\nproposal_json: {json.dumps(proposal)}"}
        with patch.object(mod, "list_tasks", return_value=[task]), \
             patch.object(mod, "query_active_runs", return_value=[{"ID": "run-1"}]), \
             patch.object(mod, "_query_published_state", return_value=[]), \
             patch.object(mod, "safe_query_active_run", return_value=[{"ID": "run-1"}]), \
             patch.object(mod, "load_workflow_binding", return_value={}), \
             patch.object(mod, "get_run_actions", return_value=[]), \
             patch.object(mod, "create_rework_card", return_value=True) as rework, \
             patch.object(mod, "run_orchestrator") as publish:
            result = mod.process_approvals(mod.default_args())
        self.assertEqual(1, result["rework_created"])
        rework.assert_called_once()
        publish.assert_not_called()

    def test_lifecycle_busy_is_a_successful_retry_exit(self):
        with patch.object(mod, "lifecycle_lock", side_effect=RuntimeError("LIFECYCLE_BUSY: held")):
            self.assertEqual(mod.cli(["reconcile"]), 0)

    def test_gbrain_dependency_failure_pauses_new_claims(self):
        result = type("R", (), {"returncode": 1, "stdout": '{"status":"DEGRADED"}', "stderr": "coverage 37.8%"})()
        with patch.object(mod.subprocess, "run", return_value=result):
            with self.assertRaisesRegex(RuntimeError, "GBrain knowledge is not ready"):
                mod.check_gbrain_dependency(mod.default_args())

    def test_reconcile_and_wip_run_before_gbrain_claim_gate(self):
        order = []
        with patch.object(mod, "reconcile", side_effect=lambda *a, **k: order.append("reconcile") or {}), \
             patch.object(mod, "load_workflow_binding", return_value={"eligible_ticket_status":"Enter", "strict_resolution_status_binding":False}), \
             patch.object(mod, "query_active_runs", side_effect=lambda a: order.append("wip") or []), \
             patch.object(mod, "check_worker_dependencies", side_effect=lambda: order.append("worker")), \
             patch.object(mod, "check_gbrain_dependency", side_effect=lambda a: order.append("gbrain") or (_ for _ in ()).throw(RuntimeError("WORKER_DEPENDENCY_UNAVAILABLE: not ready"))):
            result = mod.scout(mod.default_args())
        self.assertEqual(order, ["reconcile", "wip", "worker", "gbrain"])
        self.assertEqual(result["status"], "DEPENDENCY_UNAVAILABLE")

    def test_gbrain_hits_surface_as_context_chunks(self):
        """kb_retrieval's gbrain hits must reach the investigator, not just known_solutions."""
        gbrain = {
            "status": "READY", "source_id": "xstudio-knowledge", "abstained": False,
            "hits": [{"kb_id": "gbrain:x:k", "source_ref": "xstudio-knowledge:knowledge/sap",
                      "title": "SAP", "excerpt": "lead", "retrieval_score": 0.9,
                      "verification_required": True}],
        }
        chunks = mod._make_context_chunks(
            ticket_context={"ID": "t1"}, routing_context={}, prior_ledger=None,
            prior_attempts=None, candidates=[], known_solutions=[],
            evidence_plan={}, probes=[], gbrain=gbrain,
        )
        gbrain_chunks = [c for c in chunks if c["id"] == "gbrain_hit_0"]
        self.assertEqual(len(gbrain_chunks), 1)
        chunk = gbrain_chunks[0]
        self.assertEqual(chunk["authority"], "UNVERIFIED_KB_LEAD")
        self.assertEqual(chunk["summary"]["source_ref"], "xstudio-knowledge:knowledge/sap")
        self.assertTrue(chunk["summary"]["verification_required"])

    def test_gbrain_abstention_surfaces_as_context_chunk(self):
        gbrain = {"status": "UNAVAILABLE", "hits": [], "abstained": True,
                  "abstention_reason": "GBrain retrieval failed: timeout"}
        chunks = mod._make_context_chunks(
            ticket_context={"ID": "t1"}, routing_context={}, prior_ledger=None,
            prior_attempts=None, candidates=[], known_solutions=[],
            evidence_plan={}, probes=[], gbrain=gbrain,
        )
        abstained = [c for c in chunks if c["id"] == "gbrain_abstained"]
        self.assertEqual(len(abstained), 1)
        self.assertEqual(abstained[0]["content"]["abstention_reason"], "GBrain retrieval failed: timeout")

    def test_reviewer_block_is_audit_only_not_an_l3_escalation(self):
        """A normal reviewer rejection must stay inside the bounded rework loop."""
        event = type("Event", (), {
            "tool_name": "kanban_block",
            "event_type": "pre_tool_call",
            "args_json": json.dumps({"reason": "Need one more evidence query."}),
        })()
        self.assertIsNone(summary._find_block_reason([event]))

    def test_sql_failure_is_not_an_inactive_run(self):
        with patch.object(mod, "run_orchestrator", side_effect=RuntimeError("SQL unavailable")):
            with self.assertRaises(RuntimeError):
                mod.safe_query_active_run("run", mod.default_args())

    def test_failed_worker_recovery_requires_terminal_attempt(self):
        task = {"id": "task", "status": "blocked", "assignee": mod.INVESTIGATOR_PROFILE,
                "body": "run_id: run\nticket_id: ticket\nreview_cycle: 1"}
        for attempt, expected in [
            ({"status": "crashed", "ended_at": 1, "error": "protocol violation"}, 1),
            ({"status": "timed_out", "ended_at": 1}, 1),
            ({"status": "running", "ended_at": None}, 0),
            ({"status": "blocked", "ended_at": 1}, 0),
            ({"status": "crashed", "ended_at": None}, 0),
            ({"status": "gave_up", "ended_at": 1, "error": "iteration budget exhausted"}, 1),
        ]:
            with self.subTest(attempt=attempt), \
                    patch.object(mod, "list_tasks", return_value=[task]), \
                    patch.object(mod, "query_active_runs", return_value=[{"ID": "run"}]), \
                    patch.object(mod, "get_runs", return_value=[attempt]), \
                    patch.object(mod, "check_worker_dependencies"), \
                    patch.object(mod, "_finish_local_model_work", return_value={}) as finish, \
                    patch.object(mod, "create_rework_card", return_value="rework") as create:
                self.assertEqual(mod.recover_failed_workers(mod.default_args()), expected)
                self.assertEqual(create.call_count, expected)
                self.assertEqual(finish.call_count, expected)

    def test_failed_worker_recovery_does_not_duplicate_rework(self):
        task = {"id": "task", "status": "blocked", "assignee": mod.INVESTIGATOR_PROFILE,
                "body": "run_id: run\nticket_id: ticket"}
        successor = {"id": "next", "body": "rework_source_id: task"}
        with patch.object(mod, "list_tasks", return_value=[task, successor]), \
                patch.object(mod, "query_active_runs", return_value=[{"ID": "run"}]), \
                patch.object(mod, "create_rework_card") as create:
            self.assertEqual(mod.recover_failed_workers(mod.default_args()), 0)
            create.assert_not_called()

    def test_recovery_releases_stale_lease_before_requeuing(self):
        """A terminated worker's own SQL lease must be released before rework
        is queued for the same run, or the queue call collides with it."""
        task = {"id": "t_cffde6ec", "status": "blocked", "assignee": mod.INVESTIGATOR_PROFILE,
                "body": "run_id: run-301\nticket_id: ticket-301\nreview_cycle: 1"}
        calls: list[str] = []
        with patch.object(mod, "list_tasks", return_value=[task]), \
                patch.object(mod, "query_active_runs", return_value=[{"ID": "run-301"}]), \
                patch.object(mod, "get_runs", return_value=[{"status": "timed_out", "ended_at": 1}]), \
                patch.object(mod, "check_worker_dependencies"), \
                patch.object(mod, "_finish_local_model_work",
                              side_effect=lambda *a, **k: calls.append("finish") or {}) as finish, \
                patch.object(mod, "create_rework_card",
                              side_effect=lambda *a, **k: calls.append("rework") or "queued") as create:
            self.assertEqual(mod.recover_failed_workers(mod.default_args()), 1)
            finish.assert_called_once_with(mod.default_args(), run_id="run-301",
                                            task_id="t_cffde6ec", outcome="DONE")
            create.assert_called_once()
            self.assertEqual(calls, ["finish", "rework"])

    def test_recovery_proceeds_when_lease_already_released(self):
        """Live 2026-09-23 regression: if the lease was already released through
        the normal completion path, SQL's finish raises 'No matching running
        local-model work was found'. That must not crash the whole tick --
        recovery should still queue rework for this task."""
        task = {"id": "task", "status": "blocked", "assignee": mod.INVESTIGATOR_PROFILE,
                "body": "run_id: run\nticket_id: ticket\nreview_cycle: 1"}
        with patch.object(mod, "list_tasks", return_value=[task]), \
                patch.object(mod, "query_active_runs", return_value=[{"ID": "run"}]), \
                patch.object(mod, "get_runs", return_value=[{"status": "timed_out", "ended_at": 1}]), \
                patch.object(mod, "check_worker_dependencies"), \
                patch.object(mod, "_finish_local_model_work",
                              side_effect=RuntimeError("No matching running local-model work was found")), \
                patch.object(mod, "create_rework_card", return_value="rework") as create:
            self.assertEqual(mod.recover_failed_workers(mod.default_args()), 1)
            create.assert_called_once()

    def test_recovery_dry_run_does_not_release_lease(self):
        task = {"id": "task", "status": "blocked", "assignee": mod.INVESTIGATOR_PROFILE,
                "body": "run_id: run\nticket_id: ticket\nreview_cycle: 1"}
        with patch.object(mod, "list_tasks", return_value=[task]), \
                patch.object(mod, "query_active_runs", return_value=[{"ID": "run"}]), \
                patch.object(mod, "get_runs", return_value=[{"status": "timed_out", "ended_at": 1}]), \
                patch.object(mod, "_finish_local_model_work") as finish, \
                patch.object(mod, "create_rework_card", return_value="dry_run"):
            mod.recover_failed_workers(mod.default_args(), dry_run=True)
            finish.assert_not_called()

    def test_dependency_failure_prevents_worker_retry(self):
        task = {"id": "task", "status": "blocked", "assignee": mod.INVESTIGATOR_PROFILE,
                "body": "run_id: run\nticket_id: ticket"}
        with patch.object(mod, "list_tasks", return_value=[task]), \
                patch.object(mod, "query_active_runs", return_value=[{"ID": "run"}]), \
                patch.object(mod, "get_runs", return_value=[{"status": "crashed", "ended_at": 1}]), \
                patch.object(mod, "check_worker_dependencies", side_effect=RuntimeError("model down")), \
                patch.object(mod, "create_rework_card") as create:
            with self.assertRaises(RuntimeError):
                mod.recover_failed_workers(mod.default_args())
            create.assert_not_called()

    def test_failed_escalation_does_not_release_run(self):
        with patch.object(mod, "run_orchestrator", side_effect=RuntimeError("handoff unavailable")) as run:
            self.assertFalse(mod._escalate_run(mod.default_args(), run_id="run", ticket_id="ticket",
                                              reason="test", cycle=2, dry_run=False))
            self.assertEqual(run.call_count, 1)
            self.assertIn("--publish-response", run.call_args.args[1])

    def _update_proposal(self):
        return {"run_id": "run-u", "ticket_id": "ticket-u", "response_type": "UPDATE",
                "reply_text": "Checked the heat log; next step is the SAP posting table."}

    def test_update_below_continuation_cap_publishes_normally(self):
        with patch.object(mod, "_proposal_complete", return_value=True),                 patch.object(mod, "_query_published_state", return_value=[]),                 patch.object(mod, "safe_query_active_run", return_value=True),                 patch.object(mod, "_prior_update_continuations", return_value=mod.MAX_UPDATE_CONTINUATIONS - 1),                 patch.object(mod, "_escalate_run") as escalate:
            outcome = mod._publish_frozen_proposal(mod.default_args(), self._update_proposal(),
                                                   source="test", dry_run=True)
        self.assertEqual(outcome, "published")
        escalate.assert_not_called()

    def test_update_at_continuation_cap_escalates_instead_of_looping(self):
        """Live: Ticket_239 published 5 UPDATEs on one ticket version with no progress."""
        with patch.object(mod, "_proposal_complete", return_value=True),                 patch.object(mod, "_query_published_state", return_value=[]),                 patch.object(mod, "safe_query_active_run", return_value=True),                 patch.object(mod, "_prior_update_continuations", return_value=mod.MAX_UPDATE_CONTINUATIONS),                 patch.object(mod, "_escalate_run", return_value=True) as escalate:
            outcome = mod._publish_frozen_proposal(mod.default_args(), self._update_proposal(), source="test")
        self.assertEqual(outcome, "escalated")
        self.assertIn("continuation budget", escalate.call_args.kwargs["budget"])
        self.assertIn("SAP posting table", escalate.call_args.kwargs["reason"])

    def test_non_update_outcomes_are_never_continuation_capped(self):
        proposal = {**self._update_proposal(), "response_type": "QUESTION"}
        with patch.object(mod, "_proposal_complete", return_value=True),                 patch.object(mod, "_query_published_state", return_value=[]),                 patch.object(mod, "safe_query_active_run", return_value=True),                 patch.object(mod, "_status_args_for_response", return_value=([], None)),                 patch.object(mod, "_prior_update_continuations") as prior:
            mod._publish_frozen_proposal(mod.default_args(), proposal, source="test", dry_run=True)
        prior.assert_not_called()

    def test_escalation_reply_names_the_budget_that_was_exhausted(self):
        with patch.object(mod, "run_orchestrator") as invoke, patch.object(mod, "_post_publish_activity"):
            mod._escalate_run(mod.default_args(), run_id="r", ticket_id="t", reason="x", cycle=0,
                              dry_run=False, budget="continuation budget (3 updates with no new requester input)")
        reply = invoke.call_args.args[1][invoke.call_args.args[1].index("--reply-text") + 1]
        self.assertIn("continuation budget (3 updates", reply)
        self.assertNotIn("review/rework", reply)

    def test_embedded_jev_review_drops_the_raw_result_payload(self):
        """The raw payload made reviewer cards spill to a file (321 script writes)."""
        full = {"action": "LOCAL_REVIEW", "jev_decision": "APPROVE", "decision_confidence": 0.5,
                "reason_code": "RESPONSE_TYPE", "reason": "type mismatch", "safety": {"overclaim": 0.3},
                "result": {"answers": {"x": {"probabilities": {"a": 1}}}}}
        compact = mod._compact_jev_review(full)
        self.assertNotIn("result", compact)
        self.assertEqual(compact["reason_code"], "RESPONSE_TYPE")

    def test_reviewer_digest_states_type_claims_and_action_ids_in_plain_text(self):
        proposal = {"response_type": "RESOLUTION", "evidence_status": "COMPLETE", "reply_text": "Arc time verified.",
                    "resolution": "Matches operator log.",
                    "claims": [{"id": "C1", "status": "VERIFIED", "claim": "ArcingTime=20", "evidence": [{"action_id": "A-7"}]}],
                    "jev_primary_review": {"jev_decision": "APPROVE", "action": "LOCAL_REVIEW",
                                           "reason_code": "EVIDENCE_GAP", "reason": "check C1"}}
        digest = mod.render_proposal_digest(proposal)
        for text in ("response_type: RESOLUTION", "resolution: Matches operator log.",
                     "claim C1: [VERIFIED] action_ids=A-7", "reason=EVIDENCE_GAP"):
            self.assertIn(text, digest)

    def test_card_run_action_keeps_identity_and_bounds_result_rows(self):
        rows = [{"HeatNo": "1604014", "BilletNo": f"B{i}", "Pad": "x" * 200} for i in range(25)]
        action = {"ID": "A-1", "ActionNo": 12, "ActionType": "READ", "DatabaseName": "XStudio_Xbatch",
                  "SqlText": "SELECT " + "c," * 400, "AfterJson": json.dumps(rows), "Status": "SUCCESS",
                  "RowsAffected": 25, "CreatedBy": None}
        compact = mod.compact_run_action(action)
        self.assertEqual((compact["ID"], compact["ActionNo"], compact["Status"]), ("A-1", 12, "SUCCESS"))
        self.assertLessEqual(len(compact["ResultPreview"]), 1200)
        self.assertLessEqual(len(compact["SqlText"]), 300)
        self.assertNotIn("AfterJson", compact)
        self.assertLess(len(json.dumps(compact)), 2200)

    def test_review_cap_publishes_a_real_l3_handoff_not_a_failed_run(self):
        with patch.object(mod, "run_orchestrator") as invoke, \
                patch.object(mod, "_post_publish_activity") as activity:
            self.assertTrue(mod._escalate_run(mod.default_args(), run_id="run-1", ticket_id="ticket-1",
                                               reason="missing live API evidence", cycle=2, dry_run=False))
        command = invoke.call_args.args[1]
        self.assertIn("--publish-response", command)
        self.assertIn("L3_ESCALATION", command)
        self.assertNotIn("--fail-run", command)
        self.assertNotIn("--escalate-blocked", command)
        ledger = json.loads(command[command.index("--ledger") + 1])
        self.assertEqual(ledger["evidence_location"], "Hermes_L2_SQL_Action_Trn_Tbl")
        activity.assert_called_once()

    def test_odbc_driver_selection_prefers_installed_driver_18(self):
        self.assertEqual(
            orchestrator.select_default_driver(["ODBC Driver 18 for SQL Server"]),
            "ODBC Driver 18 for SQL Server",
        )

    def test_wsl_orchestrator_transport_stays_native(self):
        args = mod.default_args()
        with patch.object(mod, "_is_windows", return_value=False), patch.object(mod.sys, "executable", "/usr/bin/python3"):
            command = mod._base_orchestrator_args(args)
        self.assertEqual(command[0], "/usr/bin/python3")
        self.assertEqual(command[1], str(mod.REPO_ROOT_WSL / "Hermes_Orchestrator.py"))
        self.assertFalse(any("python.exe" in part.lower() for part in command[:2]))

    def test_lifecycle_task_list_is_scoped_to_l2_profiles(self):
        completed = type("Completed", (), {"returncode": 0, "stderr": "", "stdout": "[]"})()
        with patch.object(mod, "run_hermes", return_value=completed) as run:
            self.assertEqual(mod.list_tasks("done"), [])
        calls = [call.args[0] for call in run.call_args_list]
        self.assertEqual(len(calls), len(mod.INVESTIGATOR_PROFILES | mod.REVIEWER_PROFILES))
        self.assertTrue(all("--assignee" in call and "--status" in call for call in calls))
        self.assertEqual(
            {call[call.index("--assignee") + 1] for call in calls},
            mod.INVESTIGATOR_PROFILES | mod.REVIEWER_PROFILES,
        )

    def test_historical_done_cards_do_not_trigger_per_card_sql_checks(self):
        historical = {"id": "old", "status": "done", "assignee": mod.INVESTIGATOR_PROFILE,
                      "body": "run_id: old-run\nticket_id: old-ticket"}
        with patch.object(mod, "list_tasks", return_value=[historical]), \
                patch.object(mod, "query_active_runs", return_value=[{"ID": "active-run"}]), \
                patch.object(mod, "safe_query_active_run") as active_check:
            self.assertEqual(mod.ensure_missing_reviewers(mod.default_args()), 0)
        active_check.assert_not_called()

    def test_deterministic_route_extracts_heat_from_ticket_entities(self):
        ticket = {"ProblemCategory": "SAP_INTEGRATION", "SourceSystem": "Xbatch",
                  "ExtractedEntitiesJson": json.dumps({"HeatNo": "H1602522"})}
        route = mod.deterministic_ticket_route(ticket)
        self.assertEqual(route["domain"], "heat_sap")
        self.assertEqual(route["heat"], "1602522")
        self.assertEqual(route["recommended_tool"], "xstudio_heat_context")

    def test_deterministic_route_recognizes_billet_genealogy(self):
        route = mod.deterministic_ticket_route({
            "ProblemCategory": "PRODUCTION_STATE",
            "ConversationSummary": "Billet strand sequence is out of order for Heat H99707",
            "ExtractedEntitiesJson": {"HeatNo": "H99707"},
        })
        self.assertEqual("billet_genealogy", route["domain"])
        self.assertEqual("99707", route["heat"])
        self.assertEqual("xstudio_heat_context", route["recommended_tool"])

    def test_deterministic_route_maps_inventory_api_ticket_without_heat(self):
        ticket = {
            "ProblemCategory": "SAP_INTEGRATION",
            "BriefDetails": "SAP inventory sync missing for Plant/Storage on Batch B99402",
            "Description": "Was the inventory-sync API call ever made?",
            "ExtractedEntitiesJson": json.dumps({"Batch": "B99402"}),
        }
        route = mod.deterministic_ticket_route(ticket)
        self.assertEqual("sap_api", route["domain"])
        self.assertEqual("Inventory", route["api_type"])
        self.assertEqual("B99402", route["identifier"])
        self.assertEqual("xstudio_sap_api_context", route["recommended_tool"])

    def test_sap_production_posting_with_work_order_routes_to_production_api(self):
        route = mod.deterministic_ticket_route({
            "ProblemCategory": "SAP_INTEGRATION",
            "BriefDetails": "SAP posting stuck pending for Heat 1900001 / WO 199000000001",
            "Description": (
                "SAP production posting for Heat 1900001 (Work Order 199000000001) is pending; "
                "check whether the API call was sent."
            ),
            "ExtractedEntitiesJson": json.dumps({
                "HeatNo": "1900001", "WorkOrder": "199000000001"
            }),
        })
        self.assertEqual("sap_api", route["domain"])
        self.assertEqual("Production", route["api_type"])

    def test_deterministic_route_maps_work_order_and_campaign(self):
        ticket = {
            "ProblemCategory": "WORK_ORDER",
            "ExtractedEntitiesJson": json.dumps({
                "WorkOrder": "WO-99402", "Campaign": "CMP-9902"
            }),
        }
        route = mod.deterministic_ticket_route(ticket)
        self.assertEqual("work_order", route["domain"])
        self.assertEqual("WO-99402", route["work_order"])
        self.assertEqual("CMP-9902", route["campaign"])
        self.assertEqual("xstudio_work_order_context", route["recommended_tool"])

    def test_dispatch_route_context_uses_inventory_api_recipe(self):
        ticket = {
            "ProblemCategory": "SAP_INTEGRATION",
            "Description": "Was the inventory sync API call ever made?",
            "ExtractedEntitiesJson": json.dumps({"Batch": "B99402"}),
        }
        completed = type("Completed", (), {"returncode": 0, "stderr": "",
                    "stdout": json.dumps({"ok": True, "evidence_refs": [{"action_id": "api-1"}]})})()
        with patch.object(mod.subprocess, "run", return_value=completed) as bridge:
            rendered = mod._dispatch_route_context("run-1", "ticket-1", ticket)
        request = json.loads(bridge.call_args.kwargs["input"])
        self.assertEqual(request, {
            "operation": "sap_api_context", "database": "XStudio_Xbatch",
            "run_id": "run-1", "ticket_id": "ticket-1", "api_type": "Inventory",
            "identifier": "B99402", "evidence_role": "investigator",
        })
        self.assertIn('"action_id": "api-1"', rendered)

    def test_dispatch_route_context_uses_typed_heat_context_with_run_provenance(self):
        ticket = {"ExtractedEntitiesJson": json.dumps({"HeatNo": "1602522"})}
        completed = type("Completed", (), {"returncode": 0, "stderr": "",
                    "stdout": json.dumps({"ok": True, "evidence_refs": [{"action_id": "a-1"}]})})()
        with patch.object(mod.subprocess, "run", return_value=completed) as bridge:
            rendered = mod._dispatch_route_context("run-1", "ticket-1", ticket)
        request = json.loads(bridge.call_args.kwargs["input"])
        self.assertEqual(request, {"operation": "heat_context", "database": "XStudio_Xbatch",
                                   "run_id": "run-1", "ticket_id": "ticket-1", "heat": "1602522",
                                   "evidence_role": "investigator"})
        self.assertIn('"action_id": "a-1"', rendered)

    def test_dispatch_context_includes_bounded_world_recipe_and_relationships(self):
        ticket = {
            "BriefDetails": "Billet missing from yard for heat H99328",
            "ExtractedEntitiesJson": json.dumps({"HeatNo": "H99328"}),
        }
        completed = type("Completed", (), {"returncode": 0, "stderr": "",
                    "stdout": json.dumps({"ok": True, "evidence_refs": []})})()
        with patch.object(mod.subprocess, "run", return_value=completed):
            rendered = mod._dispatch_route_context("run-1", "ticket-1", ticket)
        self.assertIn('"recipe_id": "xbatch.billet-inventory.v1"', rendered)
        self.assertIn('"object": "Billet_Inventory"', rendered)
        self.assertIn('"object": "XBatch_Material_Grade_Mst_Tbl"', rendered)
        self.assertLessEqual(len(rendered), 12000)

    def test_generic_dispatch_context_abstains_to_discover_recipe_without_bridge(self):
        with patch.object(mod.subprocess, "run") as bridge:
            rendered = mod._dispatch_route_context(
                "run-1", "ticket-1", {"BriefDetails": "unclassified behaviour"}
            )
        bridge.assert_not_called()
        self.assertIn('"recipe_id": "xbatch.discover.v1"', rendered)

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

        tasks.assert_called()
        active.assert_called()
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
             patch.object(mod, "check_worker_dependencies"), \
             patch.object(mod, "check_gbrain_dependency"), \
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
        ) as queue, patch.object(mod, "run_hermes") as hermes, \
             patch.object(mod, "run_orchestrator", side_effect=RuntimeError("no live SQL in a unit test")), \
             patch.object(mod, "_build_and_persist_stage_context", return_value=("", "", None)):
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
        # Real-data canary (56-ticket seeded batch): review-stage xstudio_l2 calls
        # accounted for most missing-`database` failures because create_reviewer_card()
        # never carried the same typed-tool routing reminder investigation cards get.
        body = kwargs["spec"]["body"]
        self.assertIn("Typed XStudio investigation contract", body)
        self.assertIn("Pass database explicitly", body)

    def test_build_stage_context_degrades_on_valid_non_dict_json_from_cli(self):
        """Antigravity review (Agent_Comms/0012): the CLI always prints a JSON
        object today, but stdout is an external subprocess boundary -- valid
        JSON that isn't a dict (a bare `null`/list from a truncated or
        corrupted write) parsed fine and then crashed on response.get(...)
        one line later, outside the try/except. That exception was
        unguarded in create_reviewer_card()/create_rework_card(), so a
        rare/future CLI misbehavior could have broken card construction
        entirely despite this function's contract to never raise."""
        for bad_stdout in ("null", "[1, 2, 3]", "\"just a string\""):
            fake_proc = type("FakeProc", (), {"stdout": bad_stdout, "returncode": 0})()
            with self.subTest(stdout=bad_stdout), \
                 patch.object(mod.subprocess, "run", return_value=fake_proc):
                header, rendered, receipt = mod._build_and_persist_stage_context(
                    mod.default_args(),
                    ticket={"BriefDetails": "x"}, run_id="r1", ticket_id="t1", ticket_no="T1",
                    stage="review", review_cycle=0,
                )
        self.assertEqual((header, rendered, receipt), ("", "", None))

    def test_reviewer_card_carries_governed_context_when_delivery_succeeds(self):
        """Review cards get no canonical procedure, promoted facts, or historical
        negative cases today -- only proposal_json and instructions. Prove the
        governed-context wiring actually lands in the card body when context
        delivery succeeds, and that its provenance header/receipt appear too."""
        source = {
            "id": "t_inv",
            "body": "run_id: r1\nticket_id: t1\nticket_no: Ticket_1\nreview_cycle: 0",
        }
        proposal = {"run_id": "r1", "ticket_id": "t1", "response_type": "UPDATE", "reply_text": "Verified update"}
        with patch.object(mod, "_queue_local_model_task", side_effect=lambda *a, **kw: {"QueueStatus": "QUEUED"}) as queue, \
             patch.object(mod, "run_hermes"), \
             patch.object(mod, "run_orchestrator", side_effect=RuntimeError("no live SQL in a unit test")), \
             patch.object(
                 mod, "_build_and_persist_stage_context",
                 return_value=("context_sha256: abc123\ncontext_receipt: /tmp/r1.json\n",
                               "CANONICAL PROCEDURE / REFERENCE\nsome governed content here\n", "/tmp/r1.json"),
             ) as build_ctx:
            mod.create_reviewer_card(mod.default_args(), source_task=source, proposal=proposal)
        self.assertEqual(build_ctx.call_args.kwargs["stage"], "review")
        body = queue.call_args.kwargs["spec"]["body"]
        self.assertIn("context_sha256: abc123", body)
        self.assertIn("some governed content here", body)

    def test_rework_card_carries_governed_context_when_delivery_succeeds(self):
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
             patch.object(mod, "run_orchestrator", side_effect=RuntimeError("no live SQL in a unit test")), \
             patch.object(
                 mod, "_build_and_persist_stage_context",
                 return_value=("context_sha256: def456\ncontext_receipt: /tmp/run-1.json\n",
                               "PRIOR REJECTED REASONING\nverbatim rejection carried forward\n", "/tmp/run-1.json"),
             ) as build_ctx, \
             patch.object(mod, "_queue_local_model_task", side_effect=fake_queue):
            mod.create_rework_card(
                mod.default_args(), source_task=source_task,
                reason="ACTION_AUTHORITY mismatch", investigation_task_id="t-inv",
            )
        self.assertEqual(build_ctx.call_args.kwargs["stage"], "rework")
        self.assertEqual(build_ctx.call_args.kwargs["rejection_reason"], "ACTION_AUTHORITY mismatch")
        body = captured["spec"]["body"]
        self.assertIn("context_sha256: def456", body)
        self.assertIn("verbatim rejection carried forward", body)

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
             patch.object(mod, "run_orchestrator", side_effect=RuntimeError("no live SQL in a unit test")), \
             patch.object(mod, "_build_and_persist_stage_context", return_value=("", "", None)), \
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

    def test_incomplete_investigator_evidence_is_marked_without_claiming_verification(self):
        proposal = {
            "response_type": "UPDATE",
            "reply_text": "Verified heat format, but could not complete the genealogy query due to budget exhaustion.",
        }
        result = mod.annotate_evidence_status(proposal)
        self.assertEqual(result["evidence_status"], "INCOMPLETE")
        self.assertIn("Evidence status: INCOMPLETE", result["reply_text"])
        self.assertIn("could not complete", result["reply_text"].lower())

    def test_reviewer_prompt_does_not_treat_ticket_identifier_as_storage_proof(self):
        task = {"id": "investigation-1", "body":
                "run_id: run-1\nticket_id: ticket-1\nticket_no: Ticket_377\nreview_cycle: 0"}
        proposal = {"run_id": "run-1", "ticket_id": "ticket-1",
                    "response_type": "UPDATE", "reply_text": "Evidence status: INCOMPLETE."}
        with patch.object(mod, "_queue_local_model_task", return_value={"QueueStatus": "QUEUED"}) as queue, \
             patch.object(mod, "run_orchestrator", side_effect=RuntimeError("no live SQL in a unit test")), \
             patch.object(mod, "_build_and_persist_stage_context", return_value=("", "", None)):
            mod.create_reviewer_card(mod.default_args(), source_task=task, proposal=proposal)
        body = queue.call_args.kwargs["spec"]["body"]
        self.assertIn("not proof of database storage representation", body)

    # ------------------------------------------------------------------
    # Claim / evidence contract tests
    # ------------------------------------------------------------------

    def test_verified_claim_with_evidence_passes_validation(self):
        claims = [{"id": "C1", "claim": "Heat not found", "material": True,
                   "status": "VERIFIED", "evidence": [{"action_id": "action-3"}]}]
        valid, issues = mod.validate_claims_contract(claims)
        self.assertTrue(valid, issues)

    def test_verified_claim_without_evidence_fails_validation(self):
        claims = [{"id": "C1", "claim": "Heat not found", "material": True,
                   "status": "VERIFIED"}]
        valid, issues = mod.validate_claims_contract(claims)
        self.assertFalse(valid)
        self.assertTrue(any("evidence" in i.lower() for i in issues))

    def test_verified_claim_requires_a_current_run_action_id(self):
        claims = [{"id": "C1", "claim": "Heat found", "material": True,
                   "status": "VERIFIED", "evidence": [{"action_id": "A-1"}]}]
        valid, issues = mod.validate_claims_contract(
            claims,
            run_id="run-1",
            ticket_id="ticket-1",
            actions=[{"ID": "A-1", "RunID": "run-1", "TicketID": "ticket-1"}],
        )
        self.assertTrue(valid, issues)

    def test_verified_claim_rejects_action_from_another_run_or_ticket(self):
        claims = [{"id": "C1", "claim": "Heat found", "material": True,
                   "status": "VERIFIED", "evidence": [{"action_id": "A-1"}]}]
        valid, issues = mod.validate_claims_contract(
            claims,
            run_id="run-1",
            ticket_id="ticket-1",
            actions=[{"ID": "A-1", "RunID": "run-2", "TicketID": "ticket-1"}],
        )
        self.assertFalse(valid)
        self.assertTrue(any("current run" in issue.lower() for issue in issues))

    def test_unverified_claim_retained_if_reply_cautious(self):
        claims = [{"id": "C1", "claim": "SAP API never called", "material": True,
                   "status": "UNVERIFIED", "required_evidence": ["XMES_Get_API_Transaction_Summary"]}]
        valid, issues = mod.validate_claims_contract(claims)
        self.assertTrue(valid, "UNVERIFIED claim should pass structural validation")

    def test_contradicted_claim_cannot_become_positive_assertion(self):
        claims = [{"id": "C1", "claim": "API was called", "material": True,
                   "status": "CONTRADICTED"}]
        valid, _ = mod.validate_claims_contract(claims)
        self.assertTrue(valid, "CONTRADICTED is a valid status structurally")

    def test_incomplete_investigation_publishable_as_update(self):
        claims = [{"id": "C1", "claim": "SAP posting status", "material": True,
                   "status": "UNVERIFIED"}]
        valid, _ = mod.validate_claims_contract(claims)
        self.assertTrue(valid)
        proposal = {"response_type": "UPDATE", "reply_text": "Checked available surfaces but could not verify.",
                     "claims": claims}
        self.assertTrue(mod._proposal_complete({**proposal, "run_id": "r", "ticket_id": "t"}))

    def test_claims_optional_for_backward_compat(self):
        proposal = {"run_id": "r", "ticket_id": "t",
                    "response_type": "UPDATE", "reply_text": "Some findings."}
        self.assertTrue(mod._proposal_complete(proposal))
        valid, _ = mod.validate_claims_contract(None)
        self.assertTrue(valid)

    def test_ticket_381_regression_requires_api_provenance_for_verified_causation(self):
        """Ticket_381's causal assertion cannot be VERIFIED without an action ref.
        Whether the cited API evidence supports causation remains reviewer work."""
        claims = [
            {"id": "C1", "claim": "Heat 1900001 not found in production surfaces",
             "material": True, "status": "VERIFIED",
             "evidence": [{"action_id": "heat-action"}]},
            {"id": "C2", "claim": "SAP API never initiated due to trigger failure",
             "material": True, "status": "VERIFIED"},
        ]
        valid, issues = mod.validate_claims_contract(claims)
        self.assertFalse(valid)
        self.assertTrue(any("evidence" in issue.lower() for issue in issues))

    def test_prepublish_rejects_verified_without_evidence(self):
        """Pre-publish gate should trigger rework for invalid claims."""
        bad_claims = [{"id": "C1", "claim": "API failed", "material": True,
                       "status": "VERIFIED"}]  # no evidence!
        proposal = {"run_id": "run-1", "ticket_id": "ticket-1",
                    "response_type": "UPDATE", "reply_text": "API failed.",
                    "claims": bad_claims}
        task = {"id": "reviewer-1", "status": "done", "assignee": mod.REVIEWER_PROFILE,
                "body": f"run_id: run-1\nticket_id: ticket-1\nproposal_json: {json.dumps(proposal)}"}
        with patch.object(mod, "list_tasks", return_value=[task]), \
                patch.object(mod, "query_active_runs", return_value=[{"ID": "run-1"}]), \
                patch.object(mod, "_query_published_state", return_value=[]), \
                patch.object(mod, "safe_query_active_run", return_value=[{"ID": "run-1"}]), \
                patch.object(mod, "get_run_actions", return_value=[]), \
                patch.object(mod, "load_workflow_binding", return_value={"resolved_ticket_status": "Closed", "strict_resolution_status_binding": True}), \
                patch.object(mod, "create_rework_card", return_value="rework") as rework, \
                patch.object(mod, "run_orchestrator") as publish:
            result = mod.process_approvals(mod.default_args())
        self.assertGreater(result.get("rework_created", 0), 0)
        rework.assert_called_once()
        # Publisher should NOT have been invoked
        publish.assert_not_called()

    def test_prepublish_rejects_runtime_repaired_unstructured_proposal(self):
        proposal = {
            "run_id": "run-1", "ticket_id": "ticket-1",
            "response_type": "UPDATE", "reply_text": "Generic repaired response.",
            "claims_contract_version": 1,
            "claims": [{"id": "C1", "claim": "No structured contract was supplied.",
                        "material": True, "status": "UNVERIFIED", "evidence": []}],
            "contract_repaired_from_unstructured": True,
        }
        task = {"id": "reviewer-1", "status": "done", "assignee": mod.REVIEWER_PROFILE,
                "body": f"run_id: run-1\nticket_id: ticket-1\nproposal_json: {json.dumps(proposal)}"}
        with patch.object(mod, "list_tasks", return_value=[task]), \
                patch.object(mod, "query_active_runs", return_value=[{"ID": "run-1"}]), \
                patch.object(mod, "_query_published_state", return_value=[]), \
                patch.object(mod, "safe_query_active_run", return_value=[{"ID": "run-1"}]), \
                patch.object(mod, "load_workflow_binding", return_value={"resolved_ticket_status": "Closed", "strict_resolution_status_binding": True}), \
                patch.object(mod, "create_rework_card", return_value="rework") as rework, \
                patch.object(mod, "run_orchestrator") as publish:
            result = mod.process_approvals(mod.default_args())
        self.assertEqual(result.get("rework_created"), 1)
        self.assertIn("unstructured", rework.call_args.kwargs["reason"].lower())
        publish.assert_not_called()

    def test_prepublish_accepts_valid_claims(self):
        """Pre-publish gate passes valid claims through to publication."""
        good_claims = [{"id": "C1", "claim": "Heat found", "material": True,
                        "status": "VERIFIED",
                        "evidence": [{"action_id": "action-1"}]}]
        proposal = {"run_id": "run-1", "ticket_id": "ticket-1",
                    "response_type": "UPDATE", "reply_text": "Heat found.",
                    "claims": good_claims}
        task = {"id": "reviewer-1", "status": "done", "assignee": mod.REVIEWER_PROFILE,
                "body": f"run_id: run-1\nticket_id: ticket-1\nproposal_json: {json.dumps(proposal)}"}
        published_state = [{"ID": "run-1", "ProcessStatus": "COMPLETED", "ReplyText": "Heat found.",
                            "TicketStatus": "Enter", "ResponseType": "UPDATE"}]
        with patch.object(mod, "list_tasks", return_value=[task]), \
                patch.object(mod, "query_active_runs", return_value=[{"ID": "run-1"}]), \
                patch.object(mod, "_query_published_state", side_effect=[[], published_state]), \
                patch.object(mod, "safe_query_active_run", return_value=[{"ID": "run-1"}]), \
                patch.object(mod, "get_run_actions", return_value=[{"ID": "action-1", "RunID": "run-1", "TicketID": "ticket-1"}]), \
                patch.object(mod, "load_workflow_binding", return_value={"resolved_ticket_status": "Closed", "strict_resolution_status_binding": True}), \
                patch.object(mod, "run_orchestrator"), \
                patch.object(mod, "create_rework_card") as rework, \
                patch.object(mod, "_post_publish_activity"):
            result = mod.process_approvals(mod.default_args())
        rework.assert_not_called()
        self.assertEqual(result.get("published", 0), 1)

    def test_publication_persists_the_frozen_proposal_in_helpdesk(self):
        claims = [{"id": "C1", "claim": "Heat found", "material": True,
                   "status": "VERIFIED", "evidence": [{"action_id": "action-1"}]}]
        proposal = {"run_id": "run-1", "ticket_id": "ticket-1", "response_type": "UPDATE",
                    "reply_text": "Heat found.", "claims_contract_version": 1, "claims": claims}
        task = {"id": "reviewer-1", "status": "done", "assignee": mod.REVIEWER_PROFILE,
                "body": f"run_id: run-1\nticket_id: ticket-1\nreview_cycle: 0\nproposal_json: {json.dumps(proposal)}"}
        published_state = [{"ID": "run-1", "ProcessStatus": "COMPLETED", "ReplyText": "Heat found.",
                            "TicketStatus": "Enter", "ResponseType": "UPDATE"}]
        with patch.object(mod, "list_tasks", return_value=[task]), \
                patch.object(mod, "query_active_runs", return_value=[{"ID": "run-1"}]), \
                patch.object(mod, "_query_published_state", side_effect=[[], published_state]), \
                patch.object(mod, "safe_query_active_run", return_value=[{"ID": "run-1"}]), \
                patch.object(mod, "get_run_actions", return_value=[{"ID": "action-1", "RunID": "run-1", "TicketID": "ticket-1"}]), \
                patch.object(mod, "load_workflow_binding", return_value={"resolved_ticket_status": "Closed", "strict_resolution_status_binding": True}), \
                patch.object(mod, "run_orchestrator") as publish, \
                patch.object(mod, "_post_publish_activity"):
            mod.process_approvals(mod.default_args())
        command = publish.call_args.args[1]
        self.assertEqual("APPROVED", command[command.index("--approval-status") + 1])
        ledger = json.loads(command[command.index("--ledger") + 1])
        self.assertEqual(ledger["frozen_proposal"], proposal)
        self.assertEqual(ledger["review_task_id"], "reviewer-1")
        self.assertEqual(ledger["review_decision"], "APPROVED")
        self.assertEqual(ledger["claims_contract_version"], 1)

    def test_prepublish_skips_proposals_without_claims(self):
        """Legacy proposals without claims array should publish normally."""
        proposal = {"run_id": "run-1", "ticket_id": "ticket-1",
                    "response_type": "UPDATE", "reply_text": "Legacy finding."}
        task = {"id": "reviewer-1", "status": "done", "assignee": mod.REVIEWER_PROFILE,
                "body": f"run_id: run-1\nticket_id: ticket-1\nproposal_json: {json.dumps(proposal)}"}
        published_state = [{"ID": "run-1", "ProcessStatus": "COMPLETED", "ReplyText": "Legacy finding.",
                            "TicketStatus": "Enter", "ResponseType": "UPDATE"}]
        with patch.object(mod, "list_tasks", return_value=[task]), \
                patch.object(mod, "query_active_runs", return_value=[{"ID": "run-1"}]), \
                patch.object(mod, "_query_published_state", side_effect=[[], published_state]), \
                patch.object(mod, "safe_query_active_run", return_value=[{"ID": "run-1"}]), \
                patch.object(mod, "load_workflow_binding", return_value={"resolved_ticket_status": "Closed", "strict_resolution_status_binding": True}), \
                patch.object(mod, "run_orchestrator"), \
                patch.object(mod, "create_rework_card") as rework, \
                patch.object(mod, "_post_publish_activity"):
            result = mod.process_approvals(mod.default_args())
        rework.assert_not_called()
        self.assertEqual(result.get("published", 0), 1)

    def test_frozen_proposal_preserves_claims(self):
        """Claims array in proposal_json must survive card creation."""
        claims = [{"id": "C1", "claim": "Heat found", "material": True,
                   "status": "VERIFIED",
                   "evidence": [{"action_id": "action-1"}]}]
        task = {"id": "inv-1", "body": "run_id: r\nticket_id: t\nticket_no: T1\nreview_cycle: 0"}
        proposal = {"run_id": "r", "ticket_id": "t",
                    "response_type": "UPDATE", "reply_text": "Heat found.", "claims": claims}
        with patch.object(mod, "_queue_local_model_task", return_value={"QueueStatus": "QUEUED"}) as queue, \
             patch.object(mod, "run_orchestrator", side_effect=RuntimeError("no live SQL in a unit test")), \
             patch.object(mod, "_build_and_persist_stage_context", return_value=("", "", None)):
            mod.create_reviewer_card(mod.default_args(), source_task=task, proposal=proposal)
        body = queue.call_args.kwargs["spec"]["body"]
        # Parse the proposal_json back from the card body
        import re as test_re
        match = test_re.search(r"proposal_json: (.+)", body)
        self.assertIsNotNone(match)
        frozen = json.loads(match.group(1))
        self.assertEqual(frozen["claims"], claims)

    def test_evidence_status_flags_claim_evidence_gap(self):
        """annotate_evidence_status should set CLAIM_EVIDENCE_GAP when a material
        VERIFIED claim has no evidence reference."""
        proposal = {"response_type": "UPDATE", "reply_text": "Heat was found.",
                     "claims": [{"id": "C1", "claim": "Heat found", "material": True,
                                 "status": "VERIFIED"}]}
        result = mod.annotate_evidence_status(proposal)
        self.assertEqual(result["evidence_status"], "CLAIM_EVIDENCE_GAP")

    def test_existing_evidence_status_annotation_unchanged(self):
        """Existing INCOMPLETE detection must still work unchanged."""
        proposal = {"response_type": "UPDATE",
                    "reply_text": "Could not verify the SAP posting status."}
        result = mod.annotate_evidence_status(proposal)
        self.assertEqual(result["evidence_status"], "INCOMPLETE")

    def test_investigation_card_contains_claim_instructions(self):
        instructions = mod._query_instructions("run-1", "ticket-1")
        self.assertIn("claims array", instructions)
        self.assertIn("VERIFIED", instructions)
        self.assertIn("Absence of records is evidence of absence", instructions)

    def test_unstructured_completion_normalizes_to_unverified_claim(self):
        claims = mod.normalized_fallback_claims("No matching API row was found.")
        self.assertEqual("UNVERIFIED", claims[0]["status"])
        self.assertTrue(claims[0]["material"])
        self.assertEqual([], claims[0]["evidence"])
        self.assertNotIn("No matching API row", claims[0]["claim"])
        requirement = claims[0]["required_evidence"][0].lower()
        self.assertIn("current-run actions", requirement)
        self.assertIn("investigator_notes", requirement)

    def test_investigation_card_lists_semantic_context_tools(self):
        instructions = mod._query_instructions("run-1", "ticket-1")
        self.assertIn("heat_context", instructions)
        self.assertIn("sap_api_context", instructions)

    def test_rework_card_repeats_typed_context_contract(self):
        task = {"id": "review-1", "body": "run_id: r\nticket_id: t\nticket_no: T1\nreview_cycle: 0"}
        with patch.object(mod, "list_tasks", return_value=[]), \
                patch.object(mod, "_ticket_for_route", return_value={"ExtractedEntitiesJson": '{"HeatNo":"1602522"}'}), \
                patch.object(mod, "_dispatch_route_context", return_value="\n--- Deterministic live route/context ---\n{}\n") as route, \
                patch.object(mod, "_queue_local_model_task", return_value={"QueueStatus": "QUEUED"}) as queue, \
                patch.object(mod, "run_orchestrator", side_effect=RuntimeError("no live SQL in a unit test")), \
                patch.object(mod, "_build_and_persist_stage_context", return_value=("", "", None)):
            mod.create_rework_card(mod.default_args(), source_task=task, reason="missing evidence",
                                   investigation_task_id="investigation-1")
        body = queue.call_args.kwargs["spec"]["body"]
        self.assertIn("heat_context", body)
        self.assertIn("Deterministic live route/context", body)
        route.assert_called_once_with("r", "t", {"ExtractedEntitiesJson": '{"HeatNo":"1602522"}'})

    def test_reviewer_card_contains_claim_verification_instruction(self):
        task = {"id": "inv-1", "body": "run_id: r\nticket_id: t\nticket_no: T1\nreview_cycle: 0"}
        proposal = {"run_id": "r", "ticket_id": "t",
                    "response_type": "UPDATE", "reply_text": "Finding."}
        with patch.object(mod, "_queue_local_model_task", return_value={"QueueStatus": "QUEUED"}) as queue, \
             patch.object(mod, "run_orchestrator", side_effect=RuntimeError("no live SQL in a unit test")), \
             patch.object(mod, "_build_and_persist_stage_context", return_value=("", "", None)):
            mod.create_reviewer_card(mod.default_args(), source_task=task, proposal=proposal)
        body = queue.call_args.kwargs["spec"]["body"]
        self.assertIn("claims_contract_version", body)
        self.assertIn("VERIFIED", body)

    def test_missing_reviewer_receives_recipe_evidence_matrix(self):
        proposal = {
            "run_id": "r", "ticket_id": "t", "response_type": "UPDATE",
            "reply_text": "EAF state verified from the current row.",
            "claims": [{"id": "C1", "claim": "EAF row exists", "status": "VERIFIED",
                        "material": True, "evidence": [{"action_id": "A1"}]}],
        }
        source = {
            "id": "inv-1", "status": "done", "assignee": mod.INVESTIGATOR_PROFILE,
            "body": "run_id: r\nticket_id: t\nticket_no: T1\nreview_cycle: 0",
        }
        actions = [{"ID": "A1", "RunID": "r", "TicketID": "t",
                    "OperationName": "l2_heat_eaf", "ObjectName": "EAF_PER_HEAT"}]
        with patch.object(mod, "list_tasks", return_value=[source]), \
                patch.object(mod, "query_active_runs", return_value=[{"ID": "r"}]), \
                patch.object(mod, "get_runs", return_value=[{"status": "done", "metadata": proposal}]), \
                patch.object(mod, "_ticket_for_route", return_value={
                    "BriefDetails": "heat H99328 EAF state", "ExtractedEntitiesJson": '{"HeatNo":"H99328"}'
                }), \
                patch.object(mod, "get_run_actions", return_value=actions), \
                patch.object(mod, "_dispatch_route_context", return_value="\nreview live context\n"), \
                patch.object(mod, "create_reviewer_card", return_value="rev-1") as create:
            self.assertEqual(1, mod.ensure_missing_reviewers(mod.default_args()))
        verification = create.call_args.kwargs["verification_context"]
        self.assertIn("Reviewer evidence matrix", verification)
        self.assertIn('"status": "REFERENCED"', verification)
        self.assertIn('"evidence_categories": ["heat_process_state"]', verification)


class ValidTablesRenderingTests(unittest.TestCase):
    def test_query_instructions_renders_table_with_bracketed_columns(self):
        instructions = mod._query_instructions(
            "run-1", "ticket-1",
            [("XStudio_Xbatch", "dbo.EAF_SMS_Data", ["EAFHeatID", "ActivePower"])],
        )
        self.assertIn(
            "Current valid_tables: XStudio_Xbatch.dbo.EAF_SMS_Data[EAFHeatID,ActivePower]",
            instructions,
        )
        self.assertIn("rejected before reaching SQL", instructions)

    def test_query_instructions_omits_brackets_when_no_columns_known(self):
        instructions = mod._query_instructions(
            "run-1", "ticket-1", [("XStudio_Xbatch", "dbo.Grade_Master", [])],
        )
        self.assertIn("Current valid_tables: XStudio_Xbatch.dbo.Grade_Master\n", instructions)
        self.assertNotIn("Grade_Master[", instructions)

    def test_query_instructions_with_no_valid_tables_omits_the_line_entirely(self):
        instructions = mod._query_instructions("run-1", "ticket-1", None)
        self.assertNotIn("valid_tables", instructions)

    def test_extraction_includes_primary_and_relationship_hop_tables_with_columns(self):
        investigation = {
            "live_probes": [{
                "candidate": {"database": "XStudio_Xbatch", "table": "dbo.EAF_PER_HEAT"},
                "probe": {"columns": ["HeatID", "SteelGrade"]},
                "relationship_hops": [{
                    "hop": {"target_database": "XStudio_Xbatch", "target_table": "Grade_Master"},
                    "probe": {"columns": ["ID", "GradeName"]},
                }],
            }],
        }
        result = mod._valid_tables_from_investigation(investigation)
        self.assertEqual(
            result,
            [
                ("XStudio_Xbatch", "dbo.EAF_PER_HEAT", ["HeatID", "SteelGrade"]),
                ("XStudio_Xbatch", "Grade_Master", ["ID", "GradeName"]),
            ],
        )

    def test_extraction_with_no_investigation_data_returns_empty_list(self):
        self.assertEqual(mod._valid_tables_from_investigation({}), [])


class RelationshipHopTests(unittest.TestCase):
    def test_available_hops_only_includes_edges_this_row_can_actually_follow(self):
        relationships = [
            {"source": {"object": "EAF_PER_HEAT", "attribute": "SteelGrade"},
             "target": {"database": "XStudio_Xbatch", "object": "Grade_Master", "attribute": "GradeName"},
             "cardinality": {"source": "Many", "target": "One"}},
            {"source": {"object": "EAF_PER_HEAT", "attribute": "WorkOrder"},
             "target": {"database": "XStudio_Xbatch", "object": "XBatch_Work_Order_Mst_Tbl", "attribute": "ID"},
             "cardinality": {"source": "Many", "target": "One"}},
            {"source": {"object": "SomeOtherTable", "attribute": "X"},
             "target": {"database": "XStudio_Xbatch", "object": "Y", "attribute": "ID"},
             "cardinality": {"source": "Many", "target": "One"}},
        ]
        # WorkOrder is present but NULL on this row -- must not produce a hop.
        row = {"SteelGrade": "S355", "WorkOrder": None, "HeatNo": "1604015"}
        hops = mod._available_relationship_hops("XStudio_Xbatch", "dbo.EAF_PER_HEAT", row, relationships)
        self.assertEqual(len(hops), 1)
        self.assertEqual(hops[0]["target_table"], "Grade_Master")
        self.assertEqual(hops[0]["source_value"], "S355")

    def test_run_relationship_hops_executes_only_jev_selected_hops(self):
        relationships = [
            {"source": {"object": "EAF_PER_HEAT", "attribute": "SteelGrade"},
             "target": {"database": "XStudio_Xbatch", "object": "Grade_Master", "attribute": "GradeName"},
             "cardinality": {}},
        ]
        row = {"SteelGrade": "S355"}
        selected_hop = {
            "source_column": "SteelGrade", "source_value": "S355", "target_database": "XStudio_Xbatch",
            "target_table": "Grade_Master", "target_column": "GradeName", "jev_worth_fetching": 0.9,
        }
        with patch.object(mod, "_run_jev_workflow", return_value={
                "ok": True, "result": {"selected": [selected_hop]}}) as jev_call, \
             patch.object(mod, "_run_xstudio_bridge", return_value={
                "ok": True, "rows": [{"GradeName": "S355", "Spec": "..."}]}) as bridge_call:
            executed = mod._run_relationship_hops(
                ticket={"BriefDetails": "x"}, run_id="r", ticket_id="t",
                database="XStudio_Xbatch", table="dbo.EAF_PER_HEAT", row=row,
                relationships=relationships,
            )
        jev_call.assert_called_once()
        self.assertEqual(jev_call.call_args.args[0], "relationship_hops")
        bridge_call.assert_called_once()
        bridge_args = bridge_call.call_args.args[0]
        self.assertEqual(bridge_args["operation"], "probe_related_table")
        self.assertEqual(bridge_args["table"], "Grade_Master")
        self.assertEqual(bridge_args["filter_column"], "GradeName")
        self.assertEqual(bridge_args["filter_value"], "S355")
        self.assertEqual(len(executed), 1)

    def test_run_relationship_hops_with_no_edges_never_calls_jev(self):
        with patch.object(mod, "_run_jev_workflow") as jev_call:
            executed = mod._run_relationship_hops(
                ticket={}, run_id="r", ticket_id="t", database="XStudio_Xbatch",
                table="dbo.Unrelated_Table", row={"X": "1"}, relationships=[],
            )
        jev_call.assert_not_called()
        self.assertEqual(executed, [])


class PipelineStallDetectionTests(unittest.TestCase):
    def _row(self, waiting, last_claim, server_now):
        return [{"WaitingCount": waiting, "LastClaimOn": last_claim, "ServerNow": server_now}]

    def test_empty_wip_with_waiting_work_and_long_gap_is_a_stall(self):
        now = datetime(2026, 9, 22, 23, 0, 0)
        last_claim = now - timedelta(minutes=42)
        with patch.object(mod, "query_active_runs", return_value=[]), \
             patch.object(mod, "load_workflow_binding", return_value={"eligible_ticket_status": "Enter"}), \
             patch.object(mod, "run_orchestrator", return_value=self._row(12, last_claim, now)), \
             patch.object(mod, "_write_stall_alert", return_value=True) as write_alert:
            result = mod.check_pipeline_stall(mod.default_args())
        self.assertTrue(result["stalled"])
        self.assertEqual(result["eligible_waiting_count"], 12)
        self.assertEqual(result["minutes_since_last_claim"], 42.0)
        write_alert.assert_called_once()

    def test_empty_wip_but_no_waiting_work_is_not_a_stall(self):
        now = datetime(2026, 9, 22, 23, 0, 0)
        with patch.object(mod, "query_active_runs", return_value=[]), \
             patch.object(mod, "load_workflow_binding", return_value={"eligible_ticket_status": "Enter"}), \
             patch.object(mod, "run_orchestrator", return_value=self._row(0, now - timedelta(minutes=42), now)), \
             patch.object(mod, "_write_stall_alert") as write_alert:
            result = mod.check_pipeline_stall(mod.default_args())
        self.assertFalse(result["stalled"])
        write_alert.assert_not_called()

    def test_short_gap_is_not_yet_a_stall(self):
        now = datetime(2026, 9, 22, 23, 0, 0)
        with patch.object(mod, "query_active_runs", return_value=[]), \
             patch.object(mod, "load_workflow_binding", return_value={"eligible_ticket_status": "Enter"}), \
             patch.object(mod, "run_orchestrator", return_value=self._row(5, now - timedelta(minutes=3), now)), \
             patch.object(mod, "_write_stall_alert") as write_alert:
            result = mod.check_pipeline_stall(mod.default_args())
        self.assertFalse(result["stalled"])
        write_alert.assert_not_called()

    def test_active_runs_present_is_never_a_stall_regardless_of_waiting_count(self):
        now = datetime(2026, 9, 22, 23, 0, 0)
        with patch.object(mod, "query_active_runs", return_value=[{"ID": "run-1"}]), \
             patch.object(mod, "load_workflow_binding", return_value={"eligible_ticket_status": "Enter"}), \
             patch.object(mod, "run_orchestrator", return_value=self._row(20, now - timedelta(hours=2), now)), \
             patch.object(mod, "_write_stall_alert") as write_alert:
            result = mod.check_pipeline_stall(mod.default_args())
        self.assertFalse(result["stalled"])
        write_alert.assert_not_called()

    def test_write_stall_alert_respects_cooldown_marker(self):
        with tempfile.TemporaryDirectory() as tmp:
            comms_dir = Path(tmp) / "Agent_Comms"
            comms_dir.mkdir()
            marker = comms_dir / ".stall_alert_last_written"
            marker.write_text(datetime.utcnow().isoformat(), encoding="utf-8")
            with patch.object(mod, "STALL_ALERT_MARKER", marker), \
                 patch.object(mod, "REPO_ROOT_WSL", Path(tmp)):
                written = mod._write_stall_alert(
                    {"active_run_count": 0, "eligible_waiting_count": 5, "minutes_since_last_claim": 30.0}
                )
            self.assertFalse(written, "a recent marker should suppress a duplicate alert")
            self.assertEqual(len(list(comms_dir.glob("*.md"))), 0)

    def test_write_stall_alert_writes_a_new_finding_when_no_recent_marker(self):
        with tempfile.TemporaryDirectory() as tmp:
            comms_dir = Path(tmp) / "Agent_Comms"
            comms_dir.mkdir()
            marker = comms_dir / ".stall_alert_last_written"
            with patch.object(mod, "STALL_ALERT_MARKER", marker), \
                 patch.object(mod, "REPO_ROOT_WSL", Path(tmp)):
                written = mod._write_stall_alert(
                    {"active_run_count": 0, "eligible_waiting_count": 5, "minutes_since_last_claim": 30.0}
                )
            self.assertTrue(written)
            findings = list(comms_dir.glob("0001-*.md"))
            self.assertEqual(len(findings), 1)
            self.assertIn("stall", findings[0].read_text(encoding="utf-8").lower())
            self.assertTrue(marker.exists())


if __name__ == "__main__":
    unittest.main()

