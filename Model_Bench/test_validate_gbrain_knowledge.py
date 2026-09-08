#!/usr/bin/env python3
import unittest

from Model_Bench.validate_gbrain_knowledge import evaluate_case


class GBrainEvaluationTests(unittest.TestCase):
    def test_positive_case_accepts_any_expected_prefix(self):
        case = {"expect_any_prefix": ["knowledge/quality/"], "forbid_prefix": ["agent_comms/"]}
        self.assertEqual(evaluate_case(case, {"hits": [{"slug": "knowledge/quality/spectro"}]}), [])

    def test_negative_case_requires_abstention(self):
        errors = evaluate_case({"expect_abstention": True}, {"hits": [{"slug": "knowledge/random"}], "abstained": False})
        self.assertIn("expected abstention", errors)

    def test_forbidden_prefix_always_fails(self):
        errors = evaluate_case({"expect_any_prefix": ["knowledge/"], "forbid_prefix": ["agent_comms/"]},
                               {"hits": [{"slug": "agent_comms/old"}]})
        self.assertTrue(any("forbidden" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
