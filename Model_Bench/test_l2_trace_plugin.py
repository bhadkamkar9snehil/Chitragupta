import importlib.util
import sys
import unittest
from pathlib import Path


PLUGIN_PATH = Path(__file__).parent / "xstudio_l2_trace_plugin" / "__init__.py"
SPEC = importlib.util.spec_from_file_location("xstudio_l2_trace_plugin_under_test", PLUGIN_PATH)
plugin = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(plugin)

DRAIN_PATH = Path(__file__).parent / "drain_l2_trace_log.py"
DRAIN_SPEC = importlib.util.spec_from_file_location("drain_l2_trace_log_under_test", DRAIN_PATH)
drain = importlib.util.module_from_spec(DRAIN_SPEC)
assert DRAIN_SPEC.loader is not None
DRAIN_SPEC.loader.exec_module(drain)


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

    def test_drain_preserves_compute_dimensions_inside_usage_json(self):
        payload = drain.usage_payload_for_event({
            "usage": {"prompt_tokens": 100, "completion_tokens": 20, "total_tokens": 120},
            "profile_name": "l2-reviewer-primary",
            "ttft_ms": 875,
            "api_duration_ms": 4100,
        })
        self.assertEqual("l2-reviewer-primary", payload["profile_name"])
        self.assertEqual(875, payload["ttft_ms"])
        self.assertEqual(4100, payload["api_duration_ms"])
        self.assertEqual(120, payload["total_tokens"])

    def test_compute_snapshot_parser_keeps_gpu_cpu_and_memory(self):
        parsed = plugin._parse_compute_snapshot(
            '{"gpu_name":"NVIDIA GeForce RTX 4060","gpu_util_pct":67,'
            '"gpu_mem_used_mb":7123,"gpu_mem_total_mb":8188,'
            '"gpu_temperature_c":71,"cpu_util_pct":34,'
            '"system_mem_used_mb":12200,"system_mem_total_mb":16268,'
            '"lmstudio_working_set_mb":8300}'
        )
        self.assertEqual(8188, parsed["gpu_mem_total_mb"])
        self.assertEqual(7123, parsed["gpu_mem_used_mb"])
        self.assertEqual(34, parsed["cpu_util_pct"])
        self.assertEqual(16268, parsed["system_mem_total_mb"])


if __name__ == "__main__":
    unittest.main()
