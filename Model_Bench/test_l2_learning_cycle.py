#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest import mock

MODULE = Path(__file__).resolve().parent / "l2_learning_cycle.py"
_spec = importlib.util.spec_from_file_location("l2_learning_cycle_tested", MODULE)
mod = importlib.util.module_from_spec(_spec)
assert _spec.loader
_spec.loader.exec_module(mod)


class LearningCycleTests(unittest.TestCase):
    def test_runs_outcomes_then_gbrain(self):
        order = []
        with tempfile.TemporaryDirectory() as tmp, \
             mock.patch.object(mod, "sync_outcomes", side_effect=lambda **_: order.append("outcomes") or {"errors": 0}) as outcomes, \
             mock.patch.object(mod, "sync_gbrain", side_effect=lambda *_a, **_k: order.append("gbrain") or {"ok": True, "errors": []}) as gbrain:
            result = mod.run_learning_cycle(vault=Path(tmp))
        self.assertTrue(result["ok"])
        self.assertEqual(order, ["outcomes", "gbrain"])
        outcomes.assert_called_once()
        gbrain.assert_called_once()

    def test_outcome_failure_is_visible_but_gbrain_still_runs(self):
        with tempfile.TemporaryDirectory() as tmp, \
             mock.patch.object(mod, "sync_outcomes", side_effect=RuntimeError("sql unavailable")), \
             mock.patch.object(mod, "sync_gbrain", return_value={"ok": True, "errors": []}) as gbrain:
            result = mod.run_learning_cycle(vault=Path(tmp))
        self.assertFalse(result["ok"])
        gbrain.assert_called_once()

    def test_dry_run_propagates(self):
        with tempfile.TemporaryDirectory() as tmp, \
             mock.patch.object(mod, "sync_outcomes", return_value={"errors": 0}) as outcomes, \
             mock.patch.object(mod, "sync_gbrain", return_value={"ok": True, "errors": []}) as gbrain:
            mod.run_learning_cycle(vault=Path(tmp), dry_run=True)
        self.assertTrue(outcomes.call_args.kwargs["dry_run"])
        self.assertTrue(gbrain.call_args.kwargs["dry_run"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
