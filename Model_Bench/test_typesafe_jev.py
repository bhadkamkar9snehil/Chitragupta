#!/usr/bin/env python3
from __future__ import annotations

import os
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
import typesafe_jev as jev  # noqa: E402


MANIFEST = {
    "routes": [
        {
            "route": "sap_posting",
            "description": "SAP posting failed or is missing a material document.",
            "keywords": ["SAP", "posting", "material document"],
        },
        {
            "route": "api_transaction",
            "description": "API transaction failed or returned an error.",
            "keywords": ["API", "transaction ID", "response error"],
        },
        {
            "route": "discover",
            "description": "Unknown or cross-domain symptom.",
            "keywords": [],
        },
    ]
}


class JevRouteTests(unittest.TestCase):
    def test_missing_key_is_cleanly_disabled(self):
        with patch.dict(os.environ, {}, clear=True):
            result = jev.choose_route("SAP posting failed", MANIFEST)
        self.assertFalse(result["enabled"])
        self.assertFalse(result["accepted"])
        self.assertIn("TYPESAFE_API_KEY", result["reason"])

    def test_valid_choice_is_accepted_and_request_is_canonical(self):
        seen = {}

        def sender(url, payload, headers, timeout):
            seen.update(url=url, payload=payload, headers=headers, timeout=timeout)
            return {
                "model": "jev-test",
                "answers": {
                    "route": {
                        "type": "choice",
                        "choice": "sap_posting",
                        "confidence": 0.91,
                        "probabilities": {
                            "sap_posting": 0.91,
                            "api_transaction": 0.06,
                            "discover": 0.03,
                        },
                    }
                },
            }

        with patch.dict(os.environ, {"CHITRAGUPTA_JEV_ENABLED": "1"}, clear=True):
            result = jev.choose_route(
                "Production posting is stuck and no material document was created.",
                MANIFEST,
                api_key="test-key",
                sender=sender,
            )

        self.assertTrue(result["accepted"])
        self.assertEqual(result["choice"], "sap_posting")
        self.assertEqual(seen["payload"]["model"], "jev-latest")
        criteria = seen["payload"]["questions"]["route"]["criteria"]
        self.assertEqual(set(criteria), {"sap_posting", "api_transaction", "discover"})
        self.assertNotIn("test-key", str(seen["payload"]))
        self.assertTrue(seen["headers"]["Authorization"].startswith("Bearer "))

    def test_low_confidence_is_not_accepted(self):
        def sender(url, payload, headers, timeout):
            return {
                "model": "jev-test",
                "answers": {
                    "route": {
                        "type": "choice",
                        "choice": "api_transaction",
                        "confidence": 0.55,
                        "probabilities": {
                            "sap_posting": 0.40,
                            "api_transaction": 0.55,
                            "discover": 0.05,
                        },
                    }
                },
            }

        with patch.dict(os.environ, {"CHITRAGUPTA_JEV_ENABLED": "1"}, clear=True):
            result = jev.choose_route(
                "Something failed around an integration call.",
                MANIFEST,
                min_confidence=0.70,
                api_key="test-key",
                sender=sender,
            )
        self.assertFalse(result["accepted"])
        self.assertEqual(result["choice"], "api_transaction")
        self.assertIn("below", result["reason"])

    def test_allowed_routes_constrain_the_question(self):
        seen = {}

        def sender(url, payload, headers, timeout):
            seen["criteria"] = payload["questions"]["route"]["criteria"]
            return {
                "model": "jev-test",
                "answers": {
                    "route": {
                        "type": "choice",
                        "choice": "api_transaction",
                        "confidence": 0.88,
                        "probabilities": {"sap_posting": 0.12, "api_transaction": 0.88},
                    }
                },
            }

        with patch.dict(os.environ, {"CHITRAGUPTA_JEV_ENABLED": "1"}, clear=True):
            result = jev.choose_route(
                "TransactionID 123 failed before posting.",
                MANIFEST,
                allowed_routes=["sap_posting", "api_transaction"],
                api_key="test-key",
                sender=sender,
            )
        self.assertTrue(result["accepted"])
        self.assertEqual(set(seen["criteria"]), {"sap_posting", "api_transaction"})

    def test_invalid_choice_fails_closed_to_caller_fallback(self):
        def sender(url, payload, headers, timeout):
            return {
                "model": "jev-test",
                "answers": {
                    "route": {
                        "type": "choice",
                        "choice": "made_up_route",
                        "confidence": 0.99,
                        "probabilities": {"made_up_route": 0.99},
                    }
                },
            }

        with patch.dict(os.environ, {"CHITRAGUPTA_JEV_ENABLED": "1"}, clear=True):
            result = jev.choose_route("SAP failed", MANIFEST, api_key="test-key", sender=sender)
        self.assertFalse(result["accepted"])
        self.assertEqual(result["error_type"], "ValueError")


if __name__ == "__main__":
    unittest.main()
