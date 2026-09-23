"""Regression coverage for Hermes_Orchestrator.py's extracted CLI handlers.

Before this suite, main() had zero direct test coverage anywhere in the repo
-- its ~28 command handlers were only ever exercised live. These tests call
the extracted _cli_* functions directly with a mocked client/parser, so they
need no live DB connection. Focused on the handlers with real internal
branching (the ones a Ponytail complexity audit flagged), especially
_cli_local_model_action -- the exact function whose "queue" branch crashed
every ticket_scout tick on 2026-09-23 when a stale SQL lease was never
released before rework re-queued local-model work for the same run.
"""
import argparse
import json
import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import Hermes_Orchestrator as orch


def _args(**overrides):
    base = {
        "run_id": None, "local_model_purpose": None, "local_model_priority": None,
        "local_model_work_key": None, "local_model_work_json": None,
        "local_model_work_stdin": False, "local_model_execution_mode": None,
        "local_model_max_waiting": None, "local_model_task_id": None,
        "local_model_outcome": "DONE",
    }
    base.update(overrides)
    return argparse.Namespace(**base)


class LocalModelActionDispatchTests(unittest.TestCase):
    """The 4-way action sub-dispatch inside _cli_local_model_action."""

    def test_queue_requires_all_fields_before_touching_client(self):
        parser = MagicMock()
        parser.error.side_effect = SystemExit(2)
        client = MagicMock()
        args = _args(local_model_action="queue")  # run_id etc. all missing
        with self.assertRaises(SystemExit):
            orch._cli_local_model_action(args, parser, client)
        parser.error.assert_called_once()
        client.queue_local_model_work.assert_not_called()

    def test_queue_passes_parsed_work_json_through_to_client(self):
        parser = MagicMock()
        client = MagicMock()
        client.queue_local_model_work.return_value = {"QueueStatus": "QUEUED"}
        args = _args(
            local_model_action="queue", run_id="run-1", local_model_purpose="REWORK",
            local_model_priority=20, local_model_work_key="key-1",
            local_model_work_json=json.dumps({"title": "x"}),
        )
        orch._cli_local_model_action(args, parser, client)
        parser.error.assert_not_called()
        client.queue_local_model_work.assert_called_once_with(
            "run-1", "REWORK", 20, "key-1", {"title": "x"},
            execution_mode=None, max_waiting=None,
        )

    def test_queue_rejects_invalid_json_via_parser_error_not_a_raw_crash(self):
        parser = MagicMock()
        parser.error.side_effect = SystemExit(2)
        client = MagicMock()
        args = _args(
            local_model_action="queue", run_id="run-1", local_model_purpose="REWORK",
            local_model_priority=20, local_model_work_key="key-1",
            local_model_work_json="{not valid json",
        )
        with self.assertRaises(SystemExit):
            orch._cli_local_model_action(args, parser, client)
        client.queue_local_model_work.assert_not_called()

    def test_acquire_takes_no_arguments(self):
        parser = MagicMock()
        client = MagicMock()
        client.try_acquire_local_model_work.return_value = {"status": "NONE_WAITING"}
        orch._cli_local_model_action(_args(local_model_action="acquire"), parser, client)
        client.try_acquire_local_model_work.assert_called_once_with()

    def test_bind_requires_run_id_work_key_and_task_id(self):
        parser = MagicMock()
        parser.error.side_effect = SystemExit(2)
        client = MagicMock()
        with self.assertRaises(SystemExit):
            orch._cli_local_model_action(_args(local_model_action="bind"), parser, client)
        client.bind_local_model_task.assert_not_called()

    def test_finish_requires_run_id(self):
        parser = MagicMock()
        parser.error.side_effect = SystemExit(2)
        client = MagicMock()
        with self.assertRaises(SystemExit):
            orch._cli_local_model_action(_args(local_model_action="finish"), parser, client)
        client.finish_local_model_work.assert_not_called()

    def test_finish_passes_task_id_and_outcome(self):
        parser = MagicMock()
        client = MagicMock()
        client.finish_local_model_work.return_value = {"status": "RELEASED"}
        args = _args(local_model_action="finish", run_id="run-1",
                      local_model_task_id="t_abc", local_model_outcome="DONE")
        orch._cli_local_model_action(args, parser, client)
        client.finish_local_model_work.assert_called_once_with(
            "run-1", task_id="t_abc", outcome="DONE",
        )


class PublishResponseRunIdTests(unittest.TestCase):
    """run_id-from-last-claim recovery logic, unchanged by the extraction."""

    def test_missing_run_id_and_no_last_claim_errors(self):
        parser = MagicMock()
        parser.error.side_effect = SystemExit(2)
        client = MagicMock()
        args = _args(response_type="UPDATE", reply_text="x", run_id=None, ledger=None,
                      force_run_id=False, problem_summary=None, findings=None,
                      root_cause=None, resolution=None, new_ticket_status=None,
                      new_ask_status=None, approval_status=None,
                      mirror_to_support_remarks=False, mirror_to_ask_remarks=False)
        with patch.object(orch, "_LAST_CLAIM_STATE_PATH") as fake_path:
            fake_path.exists.return_value = False
            with self.assertRaises(SystemExit):
                orch._cli_publish_response(args, parser, client)
        client.publish_response.assert_not_called()

    def test_explicit_run_id_mismatch_without_force_errors(self):
        parser = MagicMock()
        parser.error.side_effect = SystemExit(2)
        client = MagicMock()
        args = _args(response_type="UPDATE", reply_text="x", run_id="run-B", ledger=None,
                      force_run_id=False)
        with patch.object(orch, "_LAST_CLAIM_STATE_PATH") as fake_path:
            fake_path.exists.return_value = True
            fake_path.read_text.return_value = json.dumps({"run_id": "run-A", "ticket_id": "t1"})
            with self.assertRaises(SystemExit):
                orch._cli_publish_response(args, parser, client)
        client.publish_response.assert_not_called()

    def test_force_run_id_overrides_mismatch_and_publishes(self):
        parser = MagicMock()
        client = MagicMock()
        args = _args(response_type="UPDATE", reply_text="x", run_id="run-B", ledger=None,
                      force_run_id=True, problem_summary=None, findings=None,
                      root_cause=None, resolution=None, new_ticket_status=None,
                      new_ask_status=None, approval_status=None,
                      mirror_to_support_remarks=False, mirror_to_ask_remarks=False)
        with patch.object(orch, "_LAST_CLAIM_STATE_PATH") as fake_path:
            fake_path.exists.return_value = True
            fake_path.read_text.return_value = json.dumps({"run_id": "run-A", "ticket_id": "t1"})
            orch._cli_publish_response(args, parser, client)
        client.publish_response.assert_called_once()
        self.assertEqual(client.publish_response.call_args.kwargs["run_id"], "run-B")


class PollDoesNotSweepStaleRunsTests(unittest.TestCase):
    """2026-09-23: --poll ran a blind wall-clock stale sweep before every claim.
    It could not see queued local-model work (no Kanban card by design) or a done
    reviewer awaiting publication, so it force-FAILED 11 legitimate runs in one
    morning. l2_pipeline_runtime.recover_orphan_runs is the only §6 authority."""

    def test_poll_and_claim_never_invokes_a_stale_sweep(self):
        client = MagicMock()
        client.get_candidate_tickets.return_value = []
        result = orch.poll_and_claim(client, "Enter")
        self.assertEqual(result["status"], "NO_TICKETS")
        client.recover_stale_runs.assert_not_called()
        self.assertNotIn("stale_runs_recovered", result)

    def test_client_has_no_stale_sweep_method(self):
        self.assertFalse(hasattr(orch.HermesL2Client, "recover_stale_runs"))


class ClientWriteSurfacesDeferredErrorsTests(unittest.TestCase):
    """2026-09-23: --publish-response printed PUBLISHED 20 times while SQL never changed."""

    def _client(self, cursor):
        client = object.__new__(orch.HermesL2Client)
        client.conn = MagicMock()
        client.conn.cursor.return_value = cursor
        client.hermes_user_id = None
        return client

    def test_commit_drains_every_result_set_before_committing(self):
        events = []
        cursor = MagicMock()
        cursor.nextset.side_effect = lambda: events.append("nextset") or len(events) < 2
        client = self._client(cursor)
        client.conn.commit.side_effect = lambda: events.append("commit")
        client._commit(cursor)
        self.assertEqual(events, ["nextset", "nextset", "commit"])

    def test_commit_propagates_error_hidden_in_a_later_result_set(self):
        cursor = MagicMock()
        cursor.nextset.side_effect = RuntimeError("Hermes run changed before response publication.")
        client = self._client(cursor)
        with self.assertRaises(RuntimeError):
            client._commit(cursor)
        client.conn.commit.assert_not_called()

    def test_publish_response_fails_when_row_was_not_published(self):
        cursor = MagicMock()
        cursor.nextset.return_value = False
        cursor.fetchone.return_value = ("INVESTIGATING", None)
        client = self._client(cursor)
        with self.assertRaises(RuntimeError) as ctx:
            client.publish_response(run_id="RUN-1", response_type="UPDATE", reply_text="x")
        self.assertIn("without publishing run RUN-1", str(ctx.exception))

    def test_publish_response_accepts_published_row(self):
        cursor = MagicMock()
        cursor.nextset.return_value = False
        cursor.fetchone.return_value = ("COMPLETED", "reply")
        self._client(cursor).publish_response(run_id="RUN-1", response_type="UPDATE", reply_text="x")


class ConnectRetryTests(unittest.TestCase):
    def test_transient_connect_failure_is_retried_once(self):
        err = orch.pyodbc.OperationalError("08001", "prelogin timeout")
        with patch.object(orch.pyodbc, "connect", side_effect=[err, "conn"]) as connect,                 patch.object(orch.time, "sleep"):
            self.assertEqual(orch.HermesL2Client._connect("s", "d", "u", "p", "drv"), "conn")
        self.assertEqual(connect.call_count, 2)

    def test_auth_failure_is_not_retried(self):
        err = orch.pyodbc.InterfaceError("28000", "login failed")
        with patch.object(orch.pyodbc, "connect", side_effect=err) as connect:
            with self.assertRaises(orch.pyodbc.InterfaceError):
                orch.HermesL2Client._connect("s", "d", "u", "p", "drv")
        self.assertEqual(connect.call_count, 1)


class MainDispatchOrderTests(unittest.TestCase):
    """main()'s own body must still route to exactly the right handler."""

    def _run_main_with(self, argv, handler_name):
        with patch.object(sys, "argv", ["Hermes_Orchestrator.py"] + argv), \
                patch.object(orch, "HermesL2Client") as fake_client_cls, \
                patch.object(orch, handler_name) as fake_handler:
            fake_client_cls.return_value = MagicMock()
            orch.main()
            fake_handler.assert_called_once()

    def test_discover_workflow_flag_dispatches_to_its_handler(self):
        self._run_main_with(
            ["--server", "s", "--username", "u", "--password", "p", "--discover-workflow"],
            "_cli_discover_workflow",
        )

    def test_poll_flag_dispatches_to_its_handler(self):
        self._run_main_with(
            ["--server", "s", "--username", "u", "--password", "p",
             "--poll", "--eligible-status", "Enter"],
            "_cli_poll",
        )


if __name__ == "__main__":
    unittest.main()
