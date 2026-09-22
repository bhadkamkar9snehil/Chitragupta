import unittest
from pathlib import Path


SQL = (Path(__file__).parent.parent / "Knowledge" / "50_response_and_workflow.sql").read_text(encoding="utf-8")
METRICS_SQL = (Path(__file__).parent.parent / "Knowledge" / "60_metrics_and_reporting.sql").read_text(encoding="utf-8")


class HelpdeskSqlContractTests(unittest.TestCase):
    def test_blocked_escalation_requires_a_terminal_deterministic_l3_outcome(self):
        start = SQL.index("CREATE OR ALTER PROCEDURE dbo.Hermes_L2_Log_Blocked_Escalation_Usp")
        procedure = SQL[start:]
        self.assertIn("ProcessStatus = 'COMPLETED'", procedure)
        self.assertIn("ResponseType IN ('L3_ESCALATION', 'NEEDS_HUMAN_ACTION')", procedure)
        self.assertIn("Refusing blocked escalation without a deterministic terminal L3 outcome.", procedure)

    def test_metrics_define_tool_failure_and_ist_observability_contract(self):
        for token in (
            "ToolErrorCount",
            "BlockedToolCallCount",
            "FirstEventOnIst",
            "Hermes_L2_Run_Observability_Vw",
            "OBSERVED",
            "PENDING",
            "GAP",
        ):
            self.assertIn(token, METRICS_SQL)


if __name__ == "__main__":
    unittest.main()
