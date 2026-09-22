import importlib.util
import json
import sys
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).parent / "xstudio_l2_orchestrator_plugin" / "__init__.py"


def _load():
    spec = importlib.util.spec_from_file_location("l2_orchestrator_plugin_test", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


class OrchestratorPluginTests(unittest.TestCase):
    def test_plugin_remains_a_trigger_not_a_second_lifecycle_authority(self):
        plugin = _load()
        self.assertFalse(hasattr(plugin, "_pre_tool_call"))

    def test_registers_native_kanban_terminal_hooks(self):
        plugin = _load()
        hooks = []

        class Context:
            def register_hook(self, name, callback):
                hooks.append((name, callback))

        plugin.register(Context())
        self.assertEqual(
            {name for name, _ in hooks},
            {"post_tool_call", "kanban_task_completed", "kanban_task_blocked"},
        )


if __name__ == "__main__":
    unittest.main()
