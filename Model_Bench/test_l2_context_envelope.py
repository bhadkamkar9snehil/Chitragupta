#!/usr/bin/env python3
from __future__ import annotations

import copy
import unittest

import l2_context_envelope as mod


class ContextEnvelopeTests(unittest.TestCase):
    def _item(self, *, trust="reviewed_operational", content="Known reviewed fact", rank=1):
        return mod.make_context_item(
            source_type="fact",
            source_ref="facts/f-1.md",
            trust_class=trust,
            title="Fact one",
            content=content,
            retrieval_rank=rank,
            retrieval_score=3.5,
            verification_required=True,
        )

    def _envelope(self, facts=None, *, reasons=None, sources=None):
        return mod.build_context_envelope(
            generated_at="2026-09-06T12:00:00+00:00",
            run_id="run-1",
            ticket_id="ticket-1",
            ticket_no="HD-1",
            pipeline_stage="investigation",
            review_cycle=0,
            route="performance",
            route_reasons=reasons or ["EquipmentID identifier", "keywords: delay"],
            requester_query="EquipmentID E-1 delay missing",
            promoted_facts=list(facts or [self._item()]),
            gbrain_sources=sources or ["l2-facts", "l2-knowledge"],
            gbrain_query="EquipmentID E-1 delay missing",
        )

    def test_same_input_produces_same_hash(self):
        first = self._envelope()
        second = self._envelope()
        self.assertEqual(first["context_sha256"], second["context_sha256"])
        self.assertEqual(mod.validate_context_envelope(first), [])

    def test_semantically_unordered_lists_are_normalized(self):
        first = self._envelope(
            reasons=["keywords: delay", "EquipmentID identifier"],
            sources=["l2-knowledge", "l2-facts"],
        )
        second = self._envelope(
            reasons=["EquipmentID identifier", "keywords: delay"],
            sources=["l2-facts", "l2-knowledge"],
        )
        self.assertEqual(first["context_sha256"], second["context_sha256"])
        self.assertEqual(first["route_reasons"], sorted(first["route_reasons"]))
        self.assertEqual(first["retrieval"]["gbrain_sources"], ["l2-facts", "l2-knowledge"])

    def test_ranked_collection_order_is_hash_significant(self):
        a = self._item(content="A", rank=1)
        b = self._item(content="B", rank=2)
        first = self._envelope([a, b])
        second = self._envelope([b, a])
        self.assertNotEqual(first["context_sha256"], second["context_sha256"])

    def test_changing_fact_content_changes_hash(self):
        first = self._envelope([self._item(content="first")])
        second = self._envelope([self._item(content="second")])
        self.assertNotEqual(first["promoted_facts"][0]["content_sha256"], second["promoted_facts"][0]["content_sha256"])
        self.assertNotEqual(first["context_sha256"], second["context_sha256"])

    def test_changing_trust_class_changes_hash(self):
        first = self._envelope([self._item(trust="reviewed_operational")])
        second = self._envelope([self._item(trust="reviewed_operational_heuristic")])
        self.assertNotEqual(first["context_sha256"], second["context_sha256"])

    def test_context_hash_is_excluded_from_its_own_calculation(self):
        envelope = self._envelope()
        expected = envelope["context_sha256"]
        mutated = copy.deepcopy(envelope)
        mutated["context_sha256"] = "0" * 64
        self.assertEqual(mod.compute_context_sha256(mutated), expected)

    def test_unverified_candidate_cannot_enter_trusted_fact_collection(self):
        bad = self._item(trust="unverified_candidate")
        with self.assertRaisesRegex(ValueError, "not allowed in promoted_facts"):
            self._envelope([bad])

    def test_content_hash_mismatch_is_rejected(self):
        item = self._item()
        item["content_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "does not match delivered content"):
            self._envelope([item])

    def test_query_hashes_are_validated(self):
        envelope = self._envelope()
        envelope["query_sha256"] = "0" * 64
        errors = mod.validate_context_envelope(envelope)
        self.assertIn("query_sha256 does not match requester_query", errors)


if __name__ == "__main__":
    unittest.main(verbosity=2)
