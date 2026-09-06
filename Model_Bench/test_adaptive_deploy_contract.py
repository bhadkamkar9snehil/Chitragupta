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
                self.assertIn("provider: mem0", text)  # Phase 3 owns profile-specific memory changes.
                for plugin in PLUGINS:
                    self.assertIn(f"- {plugin}", text)
                for toolset in TOOLSETS:
                    self.assertGreaterEqual(text.count(f"- {toolset}"), 2)
                self.assertIn("tool_search:\n    enabled: off", text)

    def test_mirrored_manifests_exist(self):
        for plugin in PLUGINS:
            with self.subTest(plugin=plugin):
                self.assertTrue((ROOT / "deploy" / "plugins" / f"{plugin}.plugin.yaml").exists())

    def test_deployer_installs_phase2_context_runtime_dependencies(self):
        text = (ROOT / "Model_Bench" / "deploy_l2_pipeline_runtime.sh").read_text(encoding="utf-8")
        for script in (
            "l2_pipeline_runtime.py",
            "l2_pipeline_runtime_core.py",
            "l2_context_envelope.py",
            "l2_context_delivery.py",
            "l2_context_delivery_base.py",
            "l2_context_delivery_assembly.py",
            "l2_context_delivery_receipts.py",
            "kb_retrieval.py",
            "kb_retrieval_routing.py",
            "kb_retrieval_base.py",
            "kb_retrieval_corpus.py",
            "kb_retrieval_cli.py",
            "l2_pipeline_context_helpers.py",
            "l2_pipeline_context_cards.py",
            "l2_pipeline_context_scout.py",
            "l2_gbrain.py",
            "sync_l2_gbrain.py",
            "sync_l2_outcomes.py",
            "mine_l2_learning_candidates.py",
            "mine_l2_action_capability_candidates.py",
            "l2_learning_cycle.py",
            "sync_l2_approved_solutions.py",
        ):
            self.assertIn(script, text)
        self.assertIn("l2_context_policy.json", text)
        self.assertIn("knowledge_manifest.json", text)
        self.assertIn("solution_export_policy.json", text)
        self.assertNotIn("command -v zg", text)
        self.assertNotIn("xstudio_action_receipt", text)
        self.assertNotIn("hermes mcp add gbrain", text)

    def test_gbrain_is_isolated_and_has_no_independent_scheduler(self):
        adapter = (ROOT / "Model_Bench" / "l2_gbrain.py").read_text(encoding="utf-8")
        sync = (ROOT / "Model_Bench" / "sync_l2_gbrain.py").read_text(encoding="utf-8")
        deploy = (ROOT / "Model_Bench" / "deploy_l2_pipeline_runtime.sh").read_text(encoding="utf-8")
        cycle = (ROOT / "Model_Bench" / "l2_learning_cycle.py").read_text(encoding="utf-8")
        self.assertIn('env["GBRAIN_HOME"]', adapter)
        self.assertIn('".hermes" / "l2-gbrain"', adapter)
        self.assertIn('"--no-federated"', sync)
        self.assertIn("GBrain source must be non-federated", sync)
        self.assertNotIn("--watch", sync)
        self.assertNotIn("while True", sync)
        self.assertNotIn("ExecStart=", deploy)
        self.assertIn("disable --now chitragupta-gbrain-sync.service", deploy)
        self.assertIn("sync_gbrain", cycle)

    def test_gbrain_adapter_is_retrieval_only(self):
        text = (ROOT / "Model_Bench" / "l2_gbrain.py").read_text(encoding="utf-8")
        self.assertIn('"search",', text)
        self.assertNotIn('command = "query"', text)
        self.assertNotIn('["query",', text)
        self.assertIn('"deterministic_retrieval": True', text)

    def test_phase2_context_facade_owns_stage_card_context_without_lifecycle_duplication(self):
        facade = (ROOT / "Model_Bench" / "l2_pipeline_runtime.py").read_text(encoding="utf-8")
        pipeline_context = "\n".join(
            (ROOT / "Model_Bench" / name).read_text(encoding="utf-8")
            for name in ("l2_pipeline_context_helpers.py", "l2_pipeline_context_cards.py", "l2_pipeline_context_scout.py")
        )
        delivery = "\n".join(
            (ROOT / "Model_Bench" / name).read_text(encoding="utf-8")
            for name in ("l2_context_delivery.py", "l2_context_delivery_base.py", "l2_context_delivery_assembly.py", "l2_context_delivery_receipts.py")
        )
        self.assertIn("import l2_pipeline_runtime_core as _core", facade)
        self.assertIn("assemble_stage_context", pipeline_context)
        self.assertIn("persist_context_receipt", pipeline_context)
        self.assertIn('stage="investigation"', pipeline_context)
        self.assertIn('stage="review"', pipeline_context)
        self.assertIn('stage="rework"', pipeline_context)
        self.assertIn("source_context_sha256", pipeline_context)
        self.assertIn("retrieval_query_sha256", delivery)
        self.assertIn("provenance_header", facade + pipeline_context)
        self.assertNotIn("Hermes_Solution_Article_Mst_Tbl", facade + pipeline_context)

    def test_context_policy_is_bounded_and_stage_specific(self):
        policy = json.loads((ROOT / "deploy" / "l2_context_policy.json").read_text(encoding="utf-8"))
        self.assertEqual(policy["schema_version"], 1)
        self.assertLessEqual(policy["maximum_total_rendered_context_characters"], 40000)
        self.assertEqual(policy["investigation"]["facts"], 5)
        self.assertGreaterEqual(policy["review"]["rejected_cases"], policy["investigation"]["rejected_cases"])
        self.assertGreaterEqual(policy["review"]["reopened_cases"], policy["investigation"]["reopened_cases"])

    def test_governed_solution_policy_starts_fail_closed_and_explicit(self):
        policy = json.loads((ROOT / "deploy" / "solution_export_policy.json").read_text(encoding="utf-8"))
        self.assertEqual(policy["schema_version"], 1)
        self.assertIsInstance(policy["approved"], list)
        notes = "\n".join(policy.get("notes") or [])
        self.assertIn("content_sha256", notes)
        self.assertIn("not treated as governance approval", notes)
        self.assertIn("when synchronization runs", notes)

    def test_action_plugin_remains_non_executing(self):
        text = (ROOT / "Model_Bench" / "xstudio_l2_actions_plugin" / "__init__.py").read_text(encoding="utf-8")
        self.assertIn('"validate_plan"', text)
        self.assertNotIn('"execute"', text.split("_SCHEMA", 1)[-1])
        self.assertIn('"execution_authorized": False', text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
