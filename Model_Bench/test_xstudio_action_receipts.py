#!/usr/bin/env python3
"""Contract tests for future deterministic action execution receipts."""
from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MODULE = ROOT / "xstudio_action_receipts.py"
_spec = importlib.util.spec_from_file_location("xstudio_action_receipts_tested", MODULE)
mod = importlib.util.module_from_spec(_spec)
assert _spec.loader
_spec.loader.exec_module(mod)


def plan():
    return {
        "plan_id": "a" * 32,
        "capability_id": "xbatch.sap.retry_posting",
        "capability_sha256": "b" * 64,
        "registry_sha256": "c" * 64,
        "risk": "low",
        "effective_mode": "shadow",
        "context": {"run_id": "RUN-1", "ticket_id": "TICKET-1"},
        "parameters": {"transaction_id": "TX-1"},
    }


class ActionReceiptTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.vault = Path(self.tmp.name) / "vault"

    def tearDown(self):
        self.tmp.cleanup()

    def test_begin_is_idempotent_for_same_plan_attempt(self):
        first = mod.begin_receipt(plan(), vault=self.vault, actor="executor", evidence="validated plan accepted")
        second = mod.begin_receipt(plan(), vault=self.vault, actor="executor", evidence="ignored duplicate begin")
        self.assertEqual(first["receipt_id"], second["receipt_id"])
        self.assertEqual(len(second["events"]), 1)
        self.assertEqual(second["state"], "planned")

    def test_happy_path_is_append_only_and_requires_verified_postconditions(self):
        receipt = mod.begin_receipt(plan(), vault=self.vault, actor="executor", evidence="plan loaded")
        rid = receipt["receipt_id"]
        mod.transition_receipt(rid, "approved", vault=self.vault, actor="policy", evidence="operator approval A-1")
        mod.transition_receipt(rid, "executed", vault=self.vault, actor="executor", evidence="supported SP returned success")
        with self.assertRaisesRegex(ValueError, "postconditions_verified"):
            mod.transition_receipt(rid, "verified", vault=self.vault, actor="verifier", evidence="not enough", details={})
        final = mod.transition_receipt(rid, "verified", vault=self.vault, actor="verifier",
                                       evidence="live transaction reached terminal success",
                                       details={"postconditions_verified": True, "checks": ["SAP_Status=Success"]})
        self.assertEqual(final["state"], "verified")
        self.assertEqual([e["sequence"] for e in final["events"]], [1, 2, 3, 4])
        self.assertEqual([e["state"] for e in final["events"]], ["planned", "approved", "executed", "verified"])
        self.assertEqual(mod.validate_receipt(final), [])

    def test_illegal_state_skip_is_blocked(self):
        receipt = mod.begin_receipt(plan(), vault=self.vault, actor="executor", evidence="plan loaded")
        with self.assertRaisesRegex(ValueError, "invalid action receipt transition"):
            mod.transition_receipt(receipt["receipt_id"], "executed", vault=self.vault,
                                   actor="executor", evidence="attempted to skip approval")

    def test_failure_can_be_compensated_only_with_verified_recovery(self):
        receipt = mod.begin_receipt(plan(), vault=self.vault, actor="executor", evidence="plan loaded")
        rid = receipt["receipt_id"]
        mod.transition_receipt(rid, "approved", vault=self.vault, actor="policy", evidence="approved")
        failed = mod.transition_receipt(rid, "failed", vault=self.vault, actor="executor", evidence="SP timeout")
        self.assertEqual(failed["state"], "failed")
        with self.assertRaisesRegex(ValueError, "compensation_verified"):
            mod.transition_receipt(rid, "compensated", vault=self.vault, actor="recovery", evidence="rollback attempted")
        done = mod.transition_receipt(rid, "compensated", vault=self.vault, actor="recovery",
                                      evidence="rollback state verified live",
                                      details={"compensation_verified": True})
        self.assertEqual(done["state"], "compensated")
        self.assertEqual(mod.validate_receipt(done), [])

    def test_terminal_verified_receipt_cannot_be_mutated(self):
        receipt = mod.begin_receipt(plan(), vault=self.vault, actor="executor", evidence="plan loaded")
        rid = receipt["receipt_id"]
        mod.transition_receipt(rid, "approved", vault=self.vault, actor="policy", evidence="approved")
        mod.transition_receipt(rid, "executed", vault=self.vault, actor="executor", evidence="executed")
        mod.transition_receipt(rid, "verified", vault=self.vault, actor="verifier", evidence="verified",
                               details={"postconditions_verified": True})
        with self.assertRaisesRegex(ValueError, "invalid action receipt transition"):
            mod.transition_receipt(rid, "failed", vault=self.vault, actor="executor", evidence="late mutation")


if __name__ == "__main__":
    unittest.main(verbosity=2)
