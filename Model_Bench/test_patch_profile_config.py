#!/usr/bin/env python3
"""Contract tests for comment-preserving Chitragupta profile/root config patching."""
from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE = Path(__file__).resolve().parent / "patch_profile_config.py"
_spec = importlib.util.spec_from_file_location("patch_profile_config_tested", MODULE)
mod = importlib.util.module_from_spec(_spec)
assert _spec.loader
_spec.loader.exec_module(mod)


class ProfileConfigPatchTests(unittest.TestCase):
    def _tmp(self, text: str) -> Path:
        root = Path(tempfile.mkdtemp())
        path = root / "config.yaml"
        path.write_text(text, encoding="utf-8")
        self.addCleanup(lambda: __import__("shutil").rmtree(root, ignore_errors=True))
        return path

    def test_root_bootstrap_creates_plugins_enabled_and_is_idempotent(self):
        path = self._tmp("model:\n  provider: lmstudio\n# keep me\n")
        changed, added, warnings = mod.patch_file(path, bootstrap_root_plugins=True)
        self.assertTrue(changed)
        self.assertEqual(warnings, [])
        self.assertEqual(len(added), 2)
        first = path.read_text(encoding="utf-8")
        self.assertIn("plugins:\n  enabled:\n    - xstudio-l2-tools\n    - xstudio-l2-learning", first)
        self.assertIn("# keep me", first)

        changed, added, warnings = mod.patch_file(path, bootstrap_root_plugins=True)
        self.assertFalse(changed)
        self.assertEqual(added, [])
        self.assertEqual(warnings, [])
        self.assertEqual(path.read_text(encoding="utf-8"), first)

    def test_root_bootstrap_adds_enabled_under_existing_plugins_block(self):
        path = self._tmp(
            "plugins:\n"
            "  # operator comment\n"
            "  some_setting: true\n"
            "model:\n"
            "  provider: lmstudio\n"
        )
        mod.patch_file(path, bootstrap_root_plugins=True)
        text = path.read_text(encoding="utf-8")
        self.assertIn("plugins:\n  enabled:\n", text)
        self.assertIn("  # operator comment", text)
        self.assertIn("  some_setting: true", text)
        self.assertEqual(text.count("xstudio-l2-learning"), 1)

    def test_profile_patch_adds_learning_without_switching_memory_or_destroying_comments(self):
        path = self._tmp(
            "memory:\n"
            "  provider: mem0\n"
            "approvals:\n"
            "  deny:\n"
            "    - '*sqlcmd*'\n"
            "plugins:\n"
            "  enabled:\n"
            "    - xstudio-l2-tools\n"
            "platform_toolsets:\n"
            "  cli:\n"
            "    - xstudio_l2\n"
            "known_plugin_toolsets:\n"
            "  cli:\n"
            "    - xstudio_l2\n"
            "# Security comment must survive\n"
        )
        changed, _added, warnings = mod.patch_file(path)
        self.assertTrue(changed)
        self.assertEqual(warnings, [])
        text = path.read_text(encoding="utf-8")
        self.assertIn("provider: mem0", text)
        self.assertIn("# Security comment must survive", text)
        self.assertEqual(text.count("xstudio-l2-learning"), 1)
        self.assertEqual(text.count("l2_learning"), 2)
        self.assertIn("'*Hermes_Orchestrator.py*'", text)

        changed, added, warnings = mod.patch_file(path)
        self.assertFalse(changed)
        self.assertEqual(added, [])
        self.assertEqual(warnings, [])

    def test_check_only_reports_change_without_writing(self):
        path = self._tmp("plugins:\n  enabled:\n    - xstudio-l2-tools\n")
        before = path.read_text(encoding="utf-8")
        changed, added, _warnings = mod.patch_file(path, check_only=True, bootstrap_root_plugins=True)
        self.assertTrue(changed)
        self.assertTrue(any("xstudio-l2-learning" in x for x in added))
        self.assertEqual(path.read_text(encoding="utf-8"), before)


if __name__ == "__main__":
    unittest.main(verbosity=2)
