import json
import unittest
from unittest.mock import patch

import l2_pipeline_runtime as mod


class Result:
    def __init__(self, returncode=0, stdout='{}', stderr=''):
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr


class PipelineContractTests(unittest.TestCase):
    def test_priority_closes_work_before_new_claim(self):
        self.assertGreater(mod.REVIEW_PRIORITY, mod.REWORK_PRIORITY)
        self.assertGreater(mod.REWORK_PRIORITY, mod.NEW_INVESTIGATION_PRIORITY)

    def test_todo_is_live(self):
        self.assertIn('todo', mod.LIVE_KANBAN_STATUSES)

    def test_three_review_cycles_total(self):
        self.assertEqual(mod.MAX_REVIEW_CYCLES, 3)

    def test_kb_query_excludes_suspected_cause(self):
        ticket = {
            'BriefDetails': 'real symptom',
            'Description': 'description',
            'ProblemCategory': 'quality',
            'HermesAreaName': 'SMS',
            'ExtractedEntitiesJson': '{}',
            'SuspectedCause': 'CONFIRMATION_BIAS_SENTINEL',
        }
        query = mod._query_for_retrieval(ticket)
        self.assertNotIn('CONFIRMATION_BIAS_SENTINEL', query)
        self.assertIn('real symptom', query)

    def test_resolution_fails_closed_without_binding(self):
        with self.assertRaises(RuntimeError):
            mod._status_args_for_response(
                {'strict_resolution_status_binding': True, 'resolved_ticket_status': None},
                {'response_type': 'RESOLUTION', 'new_ticket_status': 'model-guessed'},
            )

    def test_binding_owns_resolution_status(self):
        argv, expected = mod._status_args_for_response(
            {
                'strict_resolution_status_binding': True,
                'resolved_ticket_status': 'REAL_RESOLVED',
                'allow_metadata_status_override': False,
            },
            {'response_type': 'RESOLUTION', 'new_ticket_status': 'MODEL_GUESS'},
        )
        self.assertEqual(expected, 'REAL_RESOLVED')
        self.assertEqual(argv, ['--new-ticket-status', 'REAL_RESOLVED'])

    def test_operational_bundle_removes_competing_kb_payloads(self):
        bundle = {
            'ticket': {'ID': 'T1'},
            'known_solutions': [{'ID': 'legacy'}],
            'kb_retrieval': {'solutions': ['legacy']},
            'prior_findings': ['keep operational provenance'],
        }
        with patch.object(mod, 'run_orchestrator', return_value=bundle):
            rendered = mod._investigation_bundle(mod.default_args(), 'T1', {'ID': 'T1'})
        self.assertNotIn('known_solutions', rendered)
        self.assertNotIn('kb_retrieval', rendered)
        self.assertIn('prior_findings', rendered)
        self.assertIn('Current-ticket operational bundle', rendered)

    def test_run_evidence_snapshot_is_bounded_and_omits_large_sql_payload_fields(self):
        captured = {}
        def fake_run(args, extra, timeout=60):
            captured['extra'] = extra
            return [{'ActionNo': 1, 'Status': 'SUCCEEDED'}]
        with patch.object(mod, 'run_orchestrator', side_effect=fake_run):
            result = mod._run_evidence_snapshot(mod.default_args(), "run'1")
        self.assertTrue(result['available'])
        sql = captured['extra'][1]
        self.assertIn('TOP 20', sql)
        self.assertIn("run''1", sql)
        self.assertNotIn('SqlText', sql)
        self.assertNotIn('BeforeJson', sql)
        self.assertNotIn('AfterJson', sql)

    def test_reviewer_card_carries_new_and_source_context_provenance(self):
        source = {
            'id': 'task-investigate',
            'body': 'run_id: run-1\nticket_id: ticket-1\nticket_no: HD-1\nreview_cycle: 0\ncontext_sha256: oldhash\ncontext_receipt: /vault/old.json\n',
        }
        proposal = {'run_id': 'run-1', 'ticket_id': 'ticket-1', 'response_type': 'RESOLUTION', 'reply_text': 'fixed'}
        original = {'context_sha256': 'a'*64, 'query_sha256': 'b'*64, 'requester_query': 'safe query', 'route': 'sap_posting', 'retrieval': {'retrieval_degraded': False}}
        envelope = {'schema_version': 1, 'context_sha256': 'c'*64, 'query_sha256': 'd'*64, 'retrieval': {'retrieval_degraded': False}}
        captured = {}
        def fake_hermes(argv, timeout=30):
            captured['argv'] = argv
            return Result(stdout=json.dumps({'id': 'review-task'}))
        with patch.object(mod, '_original_context_for_task', return_value=(original, '/vault/old.json')), \
             patch.object(mod, '_ticket_snapshot', return_value={'BriefDetails': 'safe query'}), \
             patch.object(mod, '_run_evidence_snapshot', return_value={'available': True, 'rows': []}), \
             patch.object(mod, '_build_and_persist_stage_context', return_value=(envelope, 'REVIEW CONTEXT\n', '/vault/review.json')) as build, \
             patch.object(mod, 'provenance_header', return_value='context_schema_version: 1\ncontext_sha256: '+('c'*64)+'\nretrieval_query_sha256: '+('d'*64)+'\nretrieval_degraded: false\ncontext_receipt: /vault/review.json\n'), \
             patch.object(mod, 'run_hermes', side_effect=fake_hermes):
            task_id = mod.create_reviewer_card(args=mod.default_args(), source_task=source, proposal=proposal)
        self.assertEqual(task_id, 'review-task')
        self.assertEqual(build.call_args.kwargs['stage'], 'review')
        body = captured['argv'][captured['argv'].index('--body') + 1]
        self.assertIn('context_receipt: /vault/review.json', body)
        self.assertIn('source_context_sha256: ' + 'a'*64, body)
        self.assertIn('source_context_receipt: /vault/old.json', body)
        self.assertIn('proposal_json:', body)
        self.assertIn('REVIEW CONTEXT', body)

    def test_rework_preserves_original_context_and_negative_rejection(self):
        source = {
            'id': 'review-task',
            'body': 'run_id: run-1\nticket_id: ticket-1\nticket_no: HD-1\nreview_cycle: 0\n'
                    'investigation_task_id: task-investigate\nproposal_json: {"run_id":"run-1","ticket_id":"ticket-1","response_type":"RESOLUTION","reply_text":"x"}\n'
                    'source_context_receipt: /vault/investigation.json\nsource_context_sha256: '+('a'*64)+'\n',
        }
        original = {'context_sha256': 'a'*64, 'query_sha256': 'b'*64, 'requester_query': 'safe query', 'route': 'sap_posting', 'retrieval': {'retrieval_degraded': False}}
        envelope = {'schema_version': 1, 'context_sha256': 'e'*64, 'query_sha256': 'f'*64, 'retrieval': {'retrieval_degraded': False}}
        captured = {}
        def fake_hermes(argv, timeout=30):
            captured['argv'] = argv
            return Result(stdout=json.dumps({'id': 'rework-task'}))
        with patch.object(mod, 'list_tasks', return_value=[]), \
             patch.object(mod, '_persist_rejected_ledger', return_value='prior ledger'), \
             patch.object(mod, '_original_context_for_task', return_value=(original, '/vault/investigation.json')), \
             patch.object(mod, '_ticket_snapshot', return_value={'BriefDetails': 'safe query'}), \
             patch.object(mod, '_run_evidence_snapshot', return_value={'available': True, 'rows': []}), \
             patch.object(mod, '_build_and_persist_stage_context', return_value=(envelope, 'REWORK CONTEXT\n', '/vault/rework.json')) as build, \
             patch.object(mod, 'provenance_header', return_value='context_schema_version: 1\ncontext_sha256: '+('e'*64)+'\nretrieval_query_sha256: '+('f'*64)+'\nretrieval_degraded: false\ncontext_receipt: /vault/rework.json\n'), \
             patch.object(mod, 'run_hermes', side_effect=fake_hermes):
            task_id = mod.create_rework_card(mod.default_args(), source_task=source, reason='root cause unsupported', investigation_task_id='task-investigate')
        self.assertEqual(task_id, 'rework-task')
        self.assertEqual(build.call_args.kwargs['stage'], 'rework')
        self.assertEqual(build.call_args.kwargs['rejection_reason'], 'root cause unsupported')
        self.assertEqual(build.call_args.kwargs['original_context'], original)
        body = captured['argv'][captured['argv'].index('--body') + 1]
        self.assertIn('source_context_sha256: ' + 'a'*64, body)
        self.assertIn('REWORK CONTEXT', body)
        self.assertIn('negative evidence, not trusted truth', body)
        self.assertIn('prior ledger', body)

    def test_scout_injects_governed_context_and_hash_before_worker_start(self):
        args = mod.default_args()
        poll = {'status': 'CLAIMED', 'run_id': 'run-1', 'ticket_id': 'ticket-1', 'ticket': {'TicketNo': 'HD-1', 'BriefDetails': 'delay issue'}}
        envelope = {'context_sha256': 'a'*64, 'query_sha256': 'b'*64, 'retrieval': {'retrieval_degraded': False}}
        captured = {'orchestrator': []}
        def fake_orch(args, extra, timeout=60):
            captured['orchestrator'].append(extra)
            if extra and extra[0] == '--poll': return poll
            if extra and extra[0] == '--investigate-bundle': return {'ticket': poll['ticket']}
            return None
        def fake_hermes(argv, timeout=30):
            captured['argv'] = argv
            return Result(stdout=json.dumps({'id': 'investigator-task'}))
        with patch.object(mod, 'reconcile', return_value={'ok': True}), \
             patch.object(mod, 'load_workflow_binding', return_value={'eligible_ticket_status': 'Enter', 'resolved_ticket_status': 'Closed'}), \
             patch.object(mod, '_binding_ready_for_claims', return_value=(True, None)), \
             patch.object(mod, 'query_active_runs', return_value=[]), \
             patch.object(mod, 'run_orchestrator', side_effect=fake_orch), \
             patch.object(mod, '_archive_stale_cards_for_ticket'), \
             patch.object(mod, '_build_and_persist_stage_context', return_value=(envelope, 'GOVERNED CONTEXT\n', '/vault/investigation.json')), \
             patch.object(mod, 'provenance_header', return_value='context_schema_version: 1\ncontext_sha256: '+('a'*64)+'\nretrieval_query_sha256: '+('b'*64)+'\nretrieval_degraded: false\ncontext_receipt: /vault/investigation.json\n'), \
             patch.object(mod, '_query_instructions', return_value='TOOLS\n'), \
             patch.object(mod, 'run_hermes', side_effect=fake_hermes):
            result = mod.scout(args)
        self.assertEqual(result['context_sha256'], 'a'*64)
        body = captured['argv'][captured['argv'].index('--body') + 1]
        self.assertIn('GOVERNED CONTEXT', body)
        self.assertIn('context_receipt: /vault/investigation.json', body)
        self.assertIn('Current-ticket operational bundle', body)
        self.assertLess(body.index('GOVERNED CONTEXT'), body.index('Current-ticket operational bundle'))

    def test_receipt_persistence_failure_fails_claimed_run_instead_of_starting_worker(self):
        args = mod.default_args()
        poll = {'status': 'CLAIMED', 'run_id': 'run-1', 'ticket_id': 'ticket-1', 'ticket': {'TicketNo': 'HD-1', 'BriefDetails': 'delay issue'}}
        calls = []
        def fake_orch(args, extra, timeout=60):
            calls.append(extra)
            if extra and extra[0] == '--poll': return poll
            if extra and extra[0] == '--fail-run': return {'ok': True}
            return None
        with patch.object(mod, 'reconcile', return_value={'ok': True}), \
             patch.object(mod, 'load_workflow_binding', return_value={'eligible_ticket_status': 'Enter', 'resolved_ticket_status': 'Closed'}), \
             patch.object(mod, '_binding_ready_for_claims', return_value=(True, None)), \
             patch.object(mod, 'query_active_runs', return_value=[]), \
             patch.object(mod, 'run_orchestrator', side_effect=fake_orch), \
             patch.object(mod, '_archive_stale_cards_for_ticket'), \
             patch.object(mod, '_build_and_persist_stage_context', side_effect=OSError('disk full')), \
             patch.object(mod, 'run_hermes') as hermes:
            with self.assertRaisesRegex(RuntimeError, 'context persistence failed'):
                mod.scout(args)
        hermes.assert_not_called()
        self.assertTrue(any(c and c[0] == '--fail-run' for c in calls))


if __name__ == '__main__':
    unittest.main(verbosity=2)
