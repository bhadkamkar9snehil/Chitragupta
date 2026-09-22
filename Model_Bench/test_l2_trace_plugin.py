import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


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
    def test_write_event_stamps_uuid_and_ist_offset(self):
        with tempfile.TemporaryDirectory() as tmp:
            events_path = Path(tmp) / "events.jsonl"
            with patch.object(plugin, "_EVENTS_PATH", events_path):
                plugin._write_event({"event_type": "pre_tool_call"})

            event = json.loads(events_path.read_text(encoding="utf-8"))

        self.assertRegex(event["trace_event_id"], r"^[0-9a-f-]{36}$")
        self.assertTrue(event["event_on_ist"].endswith("+05:30"))

    def test_task_resolution_writes_context_and_correlation_events(self):
        events = []
        result = type("Result", (), {
            "returncode": 0,
            "stdout": json.dumps({"body": "run_id: run-1\nticket_id: ticket-1"}),
        })()
        original_write = plugin._write_event
        original_cache = dict(plugin._TASK_CACHE)
        original_resolving = set(plugin._RESOLVING)
        try:
            plugin._write_event = events.append
            plugin._TASK_CACHE.clear()
            plugin._RESOLVING.add("t_abc123")
            with patch.object(plugin.subprocess, "run", return_value=result):
                plugin._resolve_task_ids_blocking("t_abc123")
        finally:
            plugin._write_event = original_write
            plugin._TASK_CACHE.clear()
            plugin._TASK_CACHE.update(original_cache)
            plugin._RESOLVING.clear()
            plugin._RESOLVING.update(original_resolving)

        # Two distinct trace_context events by design: the resolution-status
        # event, and a separate correlation record the drain uses to backfill
        # hook events written before run_id/ticket_id were known.
        self.assertEqual(2, len(events))
        self.assertEqual("trace_context", events[0]["event_type"])
        self.assertEqual("resolved", events[0]["status"])
        self.assertEqual("run-1", events[0]["run_id"])
        self.assertEqual("ticket-1", events[0]["ticket_id"])
        self.assertEqual("trace_context", events[1]["event_type"])
        self.assertNotIn("status", events[1])
        self.assertEqual("run-1", events[1]["run_id"])
        self.assertEqual("ticket-1", events[1]["ticket_id"])

    def test_failed_task_resolution_writes_failed_context_without_ids(self):
        events = []
        result = type("Result", (), {"returncode": 1, "stdout": ""})()
        original_write = plugin._write_event
        try:
            plugin._write_event = events.append
            with patch.object(plugin.subprocess, "run", return_value=result):
                plugin._resolve_task_ids_blocking("t_def456")
        finally:
            plugin._write_event = original_write

        self.assertEqual(1, len(events))
        self.assertEqual("trace_context", events[0]["event_type"])
        self.assertEqual("failed", events[0]["status"])
        self.assertIsNone(events[0]["run_id"])
        self.assertIsNone(events[0]["ticket_id"])

    def test_drain_parameters_keep_event_identity_and_ist_offset(self):
        event = {
            "trace_event_id": "00000000-0000-0000-0000-000000000001",
            "event_on_ist": "2026-09-18T12:00:00.000+05:30",
        }

        params = drain.trace_procedure_parameters(event)

        self.assertEqual(event["trace_event_id"], params[0])
        self.assertEqual("+05:30", params[1].isoformat()[-6:])

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

    def test_hardware_samples_keep_the_worker_profile_for_compute_kpis(self):
        events = []
        original_write = plugin._write_event
        original_profile = plugin._PROFILE_NAME
        original_thread = plugin.threading.Thread
        original_lm = plugin._sample_lmstudio
        original_compute = plugin._sample_compute

        class ImmediateThread:
            def __init__(self, target, args=(), daemon=False):
                self.target = target
                self.args = args

            def start(self):
                self.target(*self.args)

        try:
            plugin._write_event = events.append
            plugin._PROFILE_NAME = "l2-reviewer-primary"
            plugin.threading.Thread = ImmediateThread
            plugin._sample_lmstudio = lambda: {"latency_s": 0.1}
            plugin._sample_compute = lambda: {"gpu_util_pct": 75}
            plugin._sample_hardware_async("session_start", {"session_id": "s1"})
        finally:
            plugin._write_event = original_write
            plugin._PROFILE_NAME = original_profile
            plugin.threading.Thread = original_thread
            plugin._sample_lmstudio = original_lm
            plugin._sample_compute = original_compute

        self.assertEqual(2, len(events))
        self.assertTrue(all(e["profile_name"] == "l2-reviewer-primary" for e in events))


if __name__ == "__main__":
    unittest.main()
