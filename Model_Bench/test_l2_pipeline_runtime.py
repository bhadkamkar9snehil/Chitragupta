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
        with patch.object(mod, "_l3_exists", return_value=False), \
                patch.object(mod, "run_orchestrator", side_effect=RuntimeError("handoff unavailable")) as run:
            self.assertFalse(mod._escalate_run(mod.default_args(), run_id="run", ticket_id="ticket",
                                              reason="test", cycle=2, dry_run=False))
            self.assertEqual(run.call_count, 1)
            self.assertIn("--escalate-blocked", run.call_args.args[1])

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


if __name__ == "__main__":
    unittest.main()
