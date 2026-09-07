import importlib.util
import json
import sys
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location("l2_pipeline_runtime", "Model_Bench/l2_pipeline_runtime.py")
mod = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(mod)

ORCH_SPEC = importlib.util.spec_from_file_location("hermes_orchestrator", "Hermes_Orchestrator.py")
orchestrator = importlib.util.module_from_spec(ORCH_SPEC)
assert ORCH_SPEC.loader
ORCH_SPEC.loader.exec_module(orchestrator)


class PipelineContractTests(unittest.TestCase):
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
                    patch.object(mod, "create_rework_card", return_value="rework") as create:
                self.assertEqual(mod.recover_failed_workers(mod.default_args()), expected)
                self.assertEqual(create.call_count, expected)

    def test_failed_worker_recovery_does_not_duplicate_rework(self):
        task = {"id": "task", "status": "blocked", "assignee": mod.INVESTIGATOR_PROFILE,
                "body": "run_id: run\nticket_id: ticket"}
        successor = {"id": "next", "body": "rework_source_id: task"}
        with patch.object(mod, "list_tasks", return_value=[task, successor]), \
                patch.object(mod, "query_active_runs", return_value=[{"ID": "run"}]), \
                patch.object(mod, "create_rework_card") as create:
            self.assertEqual(mod.recover_failed_workers(mod.default_args()), 0)
            create.assert_not_called()

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
            "identifier": "B99402",
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
                                   "run_id": "run-1", "ticket_id": "ticket-1", "heat": "1602522"})
        self.assertIn('"action_id": "a-1"', rendered)

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
        completed = type("Completed", (), {"returncode": 0, "stdout": '{"id":"review-1"}', "stderr": ""})()
        with patch.object(mod, "run_hermes", return_value=completed) as run:
            mod.create_reviewer_card(source_task=task, proposal=proposal)
        body = run.call_args.args[0][run.call_args.args[0].index("--body") + 1]
        self.assertIn("ticket identifier is not proof of database storage representation", body)

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
        ledger = json.loads(command[command.index("--ledger") + 1])
        self.assertEqual(ledger["frozen_proposal"], proposal)
        self.assertEqual(ledger["review_task_id"], "reviewer-1")
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
        completed = type("Completed", (), {"returncode": 0, "stdout": '{"id":"rev-1"}', "stderr": ""})()
        with patch.object(mod, "run_hermes", return_value=completed) as run:
            mod.create_reviewer_card(source_task=task, proposal=proposal)
        body = run.call_args.args[0][run.call_args.args[0].index("--body") + 1]
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
        self.assertIn("independently verify", claims[0]["required_evidence"][0])

    def test_investigation_card_lists_semantic_context_tools(self):
        instructions = mod._query_instructions("run-1", "ticket-1")
        self.assertIn("xstudio_heat_context", instructions)
        self.assertIn("xstudio_sap_api_context", instructions)

    def test_rework_card_repeats_typed_context_contract(self):
        task = {"id": "review-1", "body": "run_id: r\nticket_id: t\nticket_no: T1\nreview_cycle: 0"}
        completed = type("Completed", (), {"returncode": 0, "stdout": '{"id":"rework-1"}', "stderr": ""})()
        with patch.object(mod, "list_tasks", return_value=[]), \
                patch.object(mod, "_ticket_for_route", return_value={"ExtractedEntitiesJson": '{"HeatNo":"1602522"}'}), \
                patch.object(mod, "_dispatch_route_context", return_value="\n--- Deterministic live route/context ---\n{}\n") as route, \
                patch.object(mod, "run_hermes", return_value=completed) as run:
            mod.create_rework_card(mod.default_args(), source_task=task, reason="missing evidence",
                                   investigation_task_id="investigation-1")
        body = run.call_args.args[0][run.call_args.args[0].index("--body") + 1]
        self.assertIn("xstudio_heat_context", body)
        self.assertIn("Deterministic live route/context", body)
        route.assert_called_once_with("r", "t", {"ExtractedEntitiesJson": '{"HeatNo":"1602522"}'})

    def test_reviewer_card_contains_claim_verification_instruction(self):
        task = {"id": "inv-1", "body": "run_id: r\nticket_id: t\nticket_no: T1\nreview_cycle: 0"}
        proposal = {"run_id": "r", "ticket_id": "t",
                    "response_type": "UPDATE", "reply_text": "Finding."}
        completed = type("Completed", (), {"returncode": 0, "stdout": '{"id":"rev-1"}', "stderr": ""})()
        with patch.object(mod, "run_hermes", return_value=completed) as run:
            mod.create_reviewer_card(source_task=task, proposal=proposal)
        body = run.call_args.args[0][run.call_args.args[0].index("--body") + 1]
        self.assertIn("claims_contract_version", body)
        self.assertIn("VERIFIED", body)


if __name__ == "__main__":
    unittest.main()

