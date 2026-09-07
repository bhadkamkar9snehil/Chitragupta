import importlib.util
import unittest
from pathlib import Path


PLUGIN_PATH = Path(__file__).parent / "xstudio_l2_trace_plugin" / "__init__.py"
SPEC = importlib.util.spec_from_file_location("xstudio_l2_trace_plugin_under_test", PLUGIN_PATH)
plugin = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(plugin)


class TracePluginTests(unittest.TestCase):
    def test_post_api_request_records_profile_and_ttft(self):
        events = []
        original_write = plugin._write_event
        original_profile = plugin._PROFILE_NAME
        try:
            plugin._write_event = events.append
            plugin._PROFILE_NAME = "l2-investigator-primary"
            plugin.on_post_api_request(
                session_id="s1",
                turn_id="turn-1",
                api_request_id="req-1",
                model="qwen/qwen3.5-9b",
                provider="lmstudio",
                started_at=100.0,
                first_chunk_at=101.234,
                api_duration=5.5,
                usage={"prompt_tokens": 100, "completion_tokens": 20, "total_tokens": 120},
                finish_reason="tool_calls",
                assistant_content_chars=0,
                assistant_tool_call_count=1,
            )
        finally:
            plugin._write_event = original_write
            plugin._PROFILE_NAME = original_profile

        self.assertEqual(1, len(events))
        event = events[0]
        self.assertEqual("l2-investigator-primary", event["profile_name"])
        self.assertEqual(1234, event["ttft_ms"])
        self.assertEqual(5500, event["api_duration_ms"])
        self.assertEqual("tool_calls", event["finish_reason"])


if __name__ == "__main__":
    unittest.main()
