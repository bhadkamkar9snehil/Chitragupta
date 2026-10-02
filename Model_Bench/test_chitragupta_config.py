"""Windows credential persistence and process-bootstrap regressions."""
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from Model_Bench import chitragupta_config as config


class ConfigTests(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.path = Path(self.folder.name) / "chitragupta.json"
        environment = patch.dict(os.environ, {"CHITRAGUPTA_CONFIG_FILE": str(self.path)})
        environment.start()
        self.addCleanup(environment.stop)

    def test_missing_connections_do_not_require_external_services(self):
        self.assertIsNone(config.apply())
        config.save({})
        self.assertIsNotNone(config.apply())

    def test_explicitly_cleared_address_removes_old_process_setting(self):
        os.environ["MSSQL_MCP_SERVER"] = "old-server"
        config.save({"sql": {"server": ""}})
        config.apply()
        self.assertNotIn("MSSQL_MCP_SERVER", os.environ)

    def test_failed_replace_preserves_original_and_cleans_temporary_file(self):
        config.save({"sql": {"server": "original-server"}})
        original = self.path.read_bytes()
        with patch.object(Path, "replace", side_effect=OSError("fixture failure")):
            with self.assertRaises(OSError):
                config.save({"sql": {"server": "new-server"}})
        self.assertEqual(original, self.path.read_bytes())
        self.assertFalse(list(self.path.parent.glob("*.tmp")))

    @unittest.skipUnless(os.name == "nt", "Windows DPAPI")
    def test_secrets_are_encrypted_and_readable_by_runtime(self):
        secret = "credential regression fixture"
        config.save({"sql": {"password": secret}, "jev": {"api_key": secret},
                     "gbrain": {"client_secret": secret, "token": secret}})
        self.assertNotIn(secret, self.path.read_text())
        config.apply()
        self.assertEqual(secret, os.environ["MSSQL_MCP_PASSWORD"])
        self.assertEqual(secret, os.environ["TYPESAFE_API_KEY"])
        self.assertEqual(secret, os.environ["CHITRAGUPTA_GBRAIN_CLIENT_SECRET"])
        self.assertEqual(secret, os.environ["CHITRAGUPTA_GBRAIN_TOKEN"])

    @unittest.skipUnless(os.name == "nt", "Windows DPAPI")
    def test_protected_values_survive_subsequent_engine_save(self):
        config.save({"sql": {"password": "credential regression fixture"}})
        stored = json.loads(self.path.read_text())
        ciphertext = stored["sql"]["password"]
        stored["gbrain"] = {"client_secret": "knowledge regression fixture"}
        config.save(stored)
        self.assertEqual(ciphertext, json.loads(self.path.read_text())["sql"]["password"])
        config.apply()
        self.assertEqual("credential regression fixture", os.environ["MSSQL_MCP_PASSWORD"])


if __name__ == "__main__":
    unittest.main()
