#!/usr/bin/env python3
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import l2_context_delivery as mod
from l2_context_envelope import make_context_item


def item(source_ref: str, trust: str, content: str, source_type: str = "fixture", rank: int = 1):
    return make_context_item(
        source_type=source_type,
        source_ref=source_ref,
        trust_class=trust,
        title=source_ref,
        content=content,
        retrieval_rank=rank,
        retrieval_score=1.0,
        verification_required=True,
    )


class ContextDeliveryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.vault = self.root / "vault"
        self.policy = {
            "schema_version": 1,
            "maximum_total_rendered_context_characters": 12000,
            "route_canonical_documents": 3,
            "investigation": {
                "facts": 5, "solutions": 3, "approved_cases": 2,
                "rejected_cases": 1, "reopened_cases": 1,
                "drop_order": ["reopened_cases", "rejected_cases", "approved_cases",
                               "governed_solutions", "promoted_facts", "route_canonical"],
            },
            "review": {
                "facts": 3, "solutions": 2, "approved_cases": 1,
                "rejected_cases": 2, "reopened_cases": 2,
                "drop_order": ["approved_cases", "governed_solutions", "promoted_facts",
                               "route_canonical", "rejected_cases", "reopened_cases"],
            },
            "rework": {
                "facts": 3, "solutions": 2, "approved_cases": 1,
                "rejected_cases": 2, "reopened_cases": 2,
                "drop_order": ["approved_cases", "governed_solutions", "promoted_facts",
                               "route_canonical", "rejected_cases", "reopened_cases"],
            },
        }
        self.ticket = {
            "BriefDetails": "SAP posting failed",
            "Description": "material document missing",
            "ProblemCategory": "SAP",
            "HermesAreaName": "XBatch",
            "ExtractedEntitiesJson": {"TransactionID": "T-100"},
            "SuspectedCause": "CONFIRMATION_BIAS_SENTINEL",
        }

    def tearDown(self):
        self.tmp.cleanup()

    def _retrieval(self, degraded=False):
        return {
            "route_candidates": [{"route": "sap_posting", "score": 30, "reasons": ["TransactionID identifier"]}],
            "canonical_documents": [
                {**item("Knowledge/mental-model.md", "canonical_reference", "M"*400, "canonical_knowledge"), "reason": "always_load"},
                {**item("Knowledge/execution-model.md", "canonical_reference", "E"*400, "canonical_knowledge", 2), "reason": "always_load"},
                {**item("Knowledge/sap.md#posting", "canonical_reference", "R"*500, "canonical_knowledge", 3), "reason": "route"},
            ],
            "live_sql_leads": [{"object": "SAP_Posting_Tbl", "route": "sap_posting", "verification_required": True}],
            "promoted_facts": [
                item(f"facts/f-{i}.md", "reviewed_operational", f"fact {i} " + "F"*200, "promoted_fact", i)
                for i in range(1, 6)
            ],
            "governed_solutions": [
                item(f"solutions/approved/s-{i}.md", "governed_reusable_solution", f"solution {i} " + "S"*250, "governed_solution", i)
                for i in range(1, 4)
            ],
            "approved_cases": [
                item(f"cases/approved/a-{i}.md", "reviewed_published_historical_case", "A"*300, "historical_approved_case", i)
                for i in range(1, 3)
            ],
            "rejected_cases": [
                item("cases/rejected/r-1.md", "reviewed_negative_example", "R"*300, "historical_rejected_case", 1)
            ],
            "reopened_cases": [
                item("cases/reopened/o-1.md", "observed_resolution_regression", "O"*300, "historical_reopened_case", 1)
            ],
            "gbrain": {
                "facts": {"ok": not degraded, "source_ids": ["l2-facts"], "results": []},
                "solutions": {"ok": not degraded, "source_ids": ["l2-solutions"], "results": []},
                "approved_cases": {"ok": not degraded, "source_ids": ["l2-approved-cases"], "results": []},
                "rejected_cases": {"ok": not degraded, "source_ids": ["l2-rejected-cases"], "results": []},
                "reopened_cases": {"ok": not degraded, "source_ids": ["l2-reopened-cases"], "results": []},
            },
            "retrieval_degraded": degraded,
            "degradation_reasons": ["gbrain unavailable"] if degraded else [],
        }

    def test_requester_query_excludes_suspected_cause_and_normalizes_whitespace(self):
        query = mod.build_requester_retrieval_query({
            **self.ticket,
            "BriefDetails": "  SAP   posting\nfailed  ",
        })
        self.assertNotIn("CONFIRMATION_BIAS_SENTINEL", query)
        self.assertEqual(query.count("  "), 0)
        self.assertIn("SAP posting failed", query)
        self.assertIn("T-100", query)

    def test_investigation_builds_hashed_governed_context(self):
        with mock.patch.object(mod.kb, "retrieve", return_value=self._retrieval()):
            envelope, rendered = mod.assemble_stage_context(
                ticket=self.ticket, run_id="run-1", ticket_id="ticket-1", ticket_no="HD-1",
                stage="investigation", review_cycle=0, policy=self.policy, vault=self.vault, manifest={},
            )
        self.assertEqual(envelope["route"], "sap_posting")
        self.assertEqual(len(envelope["context_sha256"]), 64)
        self.assertIn("HARNESS-PROVIDED GOVERNED CONTEXT", rendered)
        self.assertNotIn("CONFIRMATION_BIAS_SENTINEL", envelope["requester_query"])
        self.assertEqual(envelope["retrieval"]["stage_policy"], "investigation")
        self.assertNotIn("l2-sessions", envelope["retrieval"]["gbrain_sources"])

    def test_review_is_negative_asymmetric_and_carries_frozen_proposal(self):
        data = self._retrieval()
        with mock.patch.object(mod.kb, "retrieve", return_value=data):
            envelope, rendered = mod.assemble_stage_context(
                ticket=self.ticket, run_id="run-1", ticket_id="ticket-1", ticket_no="HD-1",
                stage="review", review_cycle=0, policy=self.policy, vault=self.vault, manifest={},
                proposal={"response_type": "RESOLUTION", "root_cause": "x", "reply_text": "done"},
                current_run_evidence=[{"operation": "select", "ok": True}],
            )
        self.assertEqual(len(envelope["rejected_cases"]), 1)
        self.assertEqual(len(envelope["reopened_cases"]), 1)
        refs = [v["source_type"] for v in envelope["prior_ticket_evidence"]]
        self.assertIn("frozen_proposal", refs)
        self.assertIn("current_run_evidence", refs)
        self.assertIn("REVIEWER-REJECTED", rendered)

    def test_rework_preserves_original_context_identity_and_rejection_as_negative(self):
        original = {"context_sha256": "a"*64, "query_sha256": "b"*64, "route": "sap_posting",
                    "retrieval": {"retrieval_degraded": False}}
        with mock.patch.object(mod.kb, "retrieve", return_value=self._retrieval()):
            envelope, _ = mod.assemble_stage_context(
                ticket=self.ticket, run_id="run-1", ticket_id="ticket-1", ticket_no="HD-1",
                stage="rework", review_cycle=1, policy=self.policy, vault=self.vault, manifest={},
                rejection_reason="Evidence did not prove current state.",
                original_context=original,
            )
        trusts = [v["trust_class"] for v in envelope["prior_ticket_evidence"]]
        self.assertIn("prior_rejected_reasoning", trusts)
        snapshots = [v for v in envelope["prior_ticket_evidence"] if v["source_ref"] == "context:" + "a"*64]
        self.assertEqual(len(snapshots), 1)
        self.assertEqual(snapshots[0]["trust_class"], "original_governed_context_snapshot")
        self.assertIn('"route":"sap_posting"', snapshots[0]["content"])

    def test_degraded_retrieval_is_explicit_not_zero_hit_success(self):
        with mock.patch.object(mod.kb, "retrieve", return_value=self._retrieval(degraded=True)):
            envelope, rendered = mod.assemble_stage_context(
                ticket=self.ticket, run_id="run-1", ticket_id="ticket-1", ticket_no="HD-1",
                stage="investigation", review_cycle=0, policy=self.policy, vault=self.vault, manifest={},
            )
        self.assertTrue(envelope["retrieval"]["retrieval_degraded"])
        self.assertIn("Historical retrieval is degraded/unavailable", rendered)

    def test_budget_drops_complete_low_priority_items_and_records_counts(self):
        policy = json.loads(json.dumps(self.policy))
        policy["maximum_total_rendered_context_characters"] = 5000
        with mock.patch.object(mod.kb, "retrieve", return_value=self._retrieval()):
            envelope, rendered = mod.assemble_stage_context(
                ticket=self.ticket, run_id="run-1", ticket_id="ticket-1", ticket_no="HD-1",
                stage="investigation", review_cycle=0, policy=policy, vault=self.vault, manifest={},
            )
        self.assertLessEqual(len(rendered), 5000)
        dropped = envelope["retrieval"]["dropped_counts"]
        self.assertGreater(sum(dropped.values()), 0)
        # Whatever remains is a full original fixture item, never a string slice.
        for collection in ("promoted_facts", "governed_solutions", "approved_cases", "rejected_cases", "reopened_cases"):
            for value in envelope[collection]:
                self.assertNotIn("TRUNCATED", value["content"])

    def test_receipt_persists_exact_envelope_and_rendered_payload(self):
        with mock.patch.object(mod.kb, "retrieve", return_value=self._retrieval()):
            envelope, rendered = mod.assemble_stage_context(
                ticket=self.ticket, run_id="run-1", ticket_id="ticket-1", ticket_no="HD-1",
                stage="investigation", review_cycle=0, policy=self.policy, vault=self.vault, manifest={},
            )
        path = mod.persist_context_receipt(envelope, rendered, vault=self.vault)
        loaded = mod.load_context_receipt(path)
        self.assertEqual(loaded["context_sha256"], envelope["context_sha256"])
        self.assertEqual(loaded["rendered_context"], rendered)
        self.assertIn("/retrieval/receipts/", str(path).replace("\\", "/"))
        header = mod.provenance_header(envelope, path)
        self.assertIn(envelope["context_sha256"], header)
        self.assertIn(envelope["query_sha256"], header)

    def test_catastrophic_context_failure_has_valid_degraded_fallback(self):
        envelope, rendered = mod.assemble_degraded_context(
            ticket=self.ticket, run_id="run-1", ticket_id="ticket-1", ticket_no="HD-1",
            stage="review", review_cycle=1, reason="manifest unavailable",
            proposal={"response_type": "RESOLUTION", "reply_text": "x"},
            current_run_evidence=[{"ActionNo": 1, "Status": "SUCCEEDED"}],
            original_context={"context_sha256": "a"*64, "query_sha256": "b"*64, "route": "sap_posting",
                              "retrieval": {"retrieval_degraded": False}},
        )
        self.assertTrue(envelope["retrieval"]["retrieval_degraded"])
        self.assertEqual(envelope["route"], "discover")
        self.assertEqual(envelope["canonical_documents"], [])
        self.assertEqual(len(envelope["prior_ticket_evidence"]), 3)
        self.assertTrue(any(v["trust_class"] == "original_governed_context_snapshot" for v in envelope["prior_ticket_evidence"]))
        self.assertIn("manifest unavailable", rendered)
        self.assertEqual(mod.validate_context_envelope(envelope), [])

    def test_deployed_policy_fallback_is_supported(self):
        deployed = self.root / "deployed-policy.json"
        deployed.write_text(json.dumps(self.policy), encoding="utf-8")
        with mock.patch.object(mod, "DEFAULT_POLICY", self.root / "missing-policy.json"), \
             mock.patch.object(mod, "DEPLOYED_POLICY", deployed), \
             mock.patch.dict("os.environ", {}, clear=False):
            loaded = mod.load_context_policy()
        self.assertEqual(loaded["schema_version"], 1)
        self.assertEqual(loaded["investigation"]["facts"], self.policy["investigation"]["facts"])

    def test_policy_validation_rejects_unbounded_values(self):
        bad = json.loads(json.dumps(self.policy))
        bad["investigation"]["facts"] = 999
        self.assertTrue(mod.validate_context_policy(bad))


if __name__ == "__main__":
    unittest.main(verbosity=2)
