import unittest
from pathlib import Path


SQL = (Path(__file__).parent.parent / "Knowledge" / "50_response_and_workflow.sql").read_text(encoding="utf-8")


class HelpdeskSqlContractTests(unittest.TestCase):
    def test_blocked_escalation_requires_a_terminal_deterministic_l3_outcome(self):
        start = SQL.index("CREATE OR ALTER PROCEDURE dbo.Hermes_L2_Log_Blocked_Escalation_Usp")
        procedure = SQL[start:]
        self.assertIn("ProcessStatus = 'COMPLETED'", procedure)
        self.assertIn("ResponseType IN ('L3_ESCALATION', 'NEEDS_HUMAN_ACTION')", procedure)
        self.assertIn("Refusing blocked escalation without a deterministic terminal L3 outcome.", procedure)


if __name__ == "__main__":
    unittest.main()
