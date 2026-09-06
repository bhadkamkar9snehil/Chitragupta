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
    def test_runs_all_learning_components(self):
        with tempfile.TemporaryDirectory() as tmp, \
             mock.patch.object(mod, "sync_outcomes", return_value={"errors": 0, "approved_recorded": 1}) as outcomes, \
             mock.patch.object(mod, "mine_candidates", return_value={"errors": 0, "rejection_candidates": 1}) as lessons, \
             mock.patch.object(mod, "mine_capability_candidates", return_value={"errors": 0, "created": 1}) as actions:
            result = mod.run_learning_cycle(vault=Path(tmp))
        self.assertTrue(result["ok"])
        outcomes.assert_called_once()
        lessons.assert_called_once()
        actions.assert_called_once()
        self.assertEqual(result["outcomes"]["approved_recorded"], 1)
        self.assertEqual(result["lesson_candidate_mining"]["rejection_candidates"], 1)
        self.assertEqual(result["capability_candidate_mining"]["created"], 1)

    def test_one_component_failure_does_not_prevent_later_miners(self):
        with tempfile.TemporaryDirectory() as tmp, \
             mock.patch.object(mod, "sync_outcomes", side_effect=RuntimeError("sql unavailable")), \
             mock.patch.object(mod, "mine_candidates", return_value={"errors": 0}) as lessons, \
             mock.patch.object(mod, "mine_capability_candidates", return_value={"errors": 0}) as actions:
            result = mod.run_learning_cycle(vault=Path(tmp))
        self.assertFalse(result["ok"])
        self.assertTrue(result["errors"])
        lessons.assert_called_once()
        actions.assert_called_once()

    def test_dry_run_propagates_to_all_components(self):
        with tempfile.TemporaryDirectory() as tmp, \
             mock.patch.object(mod, "sync_outcomes", return_value={"errors": 0}) as outcomes, \
             mock.patch.object(mod, "mine_candidates", return_value={"errors": 0}) as lessons, \
             mock.patch.object(mod, "mine_capability_candidates", return_value={"errors": 0}) as actions:
            mod.run_learning_cycle(vault=Path(tmp), dry_run=True)
        self.assertTrue(outcomes.call_args.kwargs["dry_run"])
        self.assertTrue(lessons.call_args.kwargs["dry_run"])
        self.assertTrue(actions.call_args.kwargs["dry_run"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
