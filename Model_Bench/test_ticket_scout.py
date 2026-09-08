import importlib.util
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))
SPEC = importlib.util.spec_from_file_location("ticket_scout_under_test", ROOT / "ticket_scout.py")
scout = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(scout)


class TicketScoutObservabilityTests(unittest.TestCase):
    def test_flushes_trace_and_ticket_activity_through_the_coalesced_runner(self):
        result = type("Result", (), {"returncode": 0, "stderr": "", "stdout": "ok"})()
        with patch.object(scout.subprocess, "run", return_value=result) as run:
            self.assertTrue(scout.flush_observability())
        command = run.call_args.args[0]
        self.assertIn("run_coalesced.py", command[1])
        self.assertIn("drain_and_summarize.py", command)
        self.assertIn("--python", command)

    def test_dry_run_does_not_flush_observability(self):
        self.assertTrue(scout.is_dry_run(["--dry-run"]))
        self.assertFalse(scout.is_dry_run([]))


if __name__ == "__main__":
    unittest.main()
