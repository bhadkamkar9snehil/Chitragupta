#!/usr/bin/env python3
"""Static drift guard for the adaptive L2 deployment contract."""
from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROFILES = (
    "l2-investigator",
    "l2-investigator-primary",
    "l2-reviewer-primary",
    "l2-reviewer-fallback",
)
PLUGINS = (
    "xstudio-l2-tools",
    "xstudio-l2-identity",
    "xstudio-l2-learning",
    "xstudio-l2-actions",
)
TOOLSETS = ("xstudio_l2", "l2_learning", "l2_actions")


class AdaptiveDeployContractTests(unittest.TestCase):
    def test_every_active_profile_declares_required_plugins_and_toolsets(self):
        for profile in PROFILES:
            path = ROOT / "deploy" / "profiles" / profile / "config.yaml"
            text = path.read_text(encoding="utf-8")
            with self.subTest(profile=profile):
                self.assertIn("provider: mem0", text)
                for plugin in PLUGINS:
                    self.assertIn(f"- {plugin}", text)
                for toolset in TOOLSETS:
                    self.assertGreaterEqual(text.count(f"- {toolset}"), 2)
                self.assertIn("tool_search:\n    enabled: off", text)

    def test_mirrored_manifests_exist(self):
        for plugin in PLUGINS:
            with self.subTest(plugin=plugin):
                self.assertTrue(
                    (ROOT / "deploy" / "plugins" / f"{plugin}.plugin.yaml").exists()
                )

    def test_deployer_contains_adaptive_plugins_without_future_executor_scaffolding(self):
        text = (ROOT / "Model_Bench" / "deploy_l2_pipeline_runtime.sh").read_text(
            encoding="utf-8"
        )
        for plugin in PLUGINS:
            self.assertIn(plugin, text)
        for script in (
            "sync_l2_outcomes.py",
            "mine_l2_learning_candidates.py",
            "mine_l2_action_capability_candidates.py",
            "l2_learning_cycle.py",
            "sync_l2_approved_solutions.py",
        ):
            self.assertIn(script, text)
        self.assertIn("solution_export_policy.json", text)
        self.assertNotIn("xstudio_action_receipt", text)

    def test_governed_solution_policy_starts_fail_closed_and_explicit(self):
        policy = json.loads(
            (ROOT / "deploy" / "solution_export_policy.json").read_text(encoding="utf-8")
        )
        self.assertEqual(policy["schema_version"], 1)
        self.assertIsInstance(policy["approved"], list)
        notes = "\n".join(policy.get("notes") or [])
        self.assertIn("content_sha256", notes)
        self.assertIn("not treated as governance approval", notes)
        self.assertIn("when synchronization runs", notes)

    def test_action_plugin_remains_non_executing(self):
        text = (
            ROOT / "Model_Bench" / "xstudio_l2_actions_plugin" / "__init__.py"
        ).read_text(encoding="utf-8")
        self.assertIn('"validate_plan"', text)
        self.assertNotIn('"execute"', text.split("_SCHEMA", 1)[-1])
        self.assertIn('"execution_authorized": False', text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
