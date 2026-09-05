#!/usr/bin/env python3
"""Contract tests for the typed/guarded XStudio L2 investigation interface.

These assert structural safety, not documented intent. Each test maps to a rule
the Ticket_424/Ticket_441 postmortem required: transport is harness-owned, the
retired shell paths are blocked, benign inspection still works, raw SQL is
read-only, EXEC is allowlist-only, and no single call or retry loop can eat the
worker's context window.
"""
from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


plugin = _load("xstudio_l2_tools_plugin_test", ROOT / "xstudio_l2_tools_plugin" / "__init__.py")
bridge = _load("xstudio_l2_tool_bridge_test", ROOT / "xstudio_l2_tool_bridge.py")
patcher = _load("patch_profile_config_test", ROOT / "patch_profile_config.py")


def setup_function() -> None:
    with plugin._lock:
        plugin._session_calls.clear()
        plugin._session_failures.clear()


# --------------------------------------------------------------------------
# Terminal execution guard
# --------------------------------------------------------------------------

def test_terminal_guard_blocks_ticket_424_failure_signature() -> None:
    """The exact malformed transport Ticket_424 retried five times."""
    blocked = plugin._pre_tool_call("terminal", {
        "command": 'python3 /mnt/c/Python314/python.exe "C:/x/Hermes_Orchestrator.py" --query "SELECT 1"'
    }, task_id="ticket-424")
    assert blocked and blocked["action"] == "block" and "xstudio_l2" in blocked["message"]


def test_terminal_guard_blocks_wrapped_retries_of_the_same_shape() -> None:
    """Ticket_424 also tried `timeout N ...` wrappers around the same command."""
    for command in (
        'timeout 120 python3 /mnt/c/Python314/python.exe "/x/Hermes_Orchestrator.py" --query "SELECT 1"',
        'python3 -u "/mnt/c/Users/Admin/Documents/Office/AIHelpdesk/Hermes_Orchestrator.py" --query "SELECT 1"',
    ):
        assert plugin._pre_tool_call("terminal", {"command": command}, task_id="s")["action"] == "block"


def test_terminal_guard_blocks_alternate_sql_transports() -> None:
    for command in (
        "sqlcmd -S 10.2.6.204 -Q 'SELECT 1'",
        'python3 -c "import pyodbc; pyodbc.connect(...)"',
        'python3 -c "from pyodbc import connect"',
    ):
        assert plugin._pre_tool_call("terminal", {"command": command}, task_id="s")["action"] == "block"


def test_terminal_guard_blocks_dependency_installation() -> None:
    """Ticket_424 fell back to installing the driver; Tirith then failed closed."""
    for command in (
        "pip install pyodbc",
        "pip3 install pyodbc",
        "python3 -m pip install pyodbc",
        "uv pip install pyodbc --no-deps",
        "source .venv/bin/activate && pip install pyodbc -q",
        "sudo apt-get install -y unixodbc-dev",
    ):
        blocked = plugin._pre_tool_call("terminal", {"command": command}, task_id="s")
        assert blocked and blocked["action"] == "block", command


def test_terminal_guard_leaves_benign_inspection_available() -> None:
    """Requirement 13: do not turn the guard into a general terminal ban."""
    for command in (
        "grep -R 'SAP_Posting_Tbl' Knowledge/",
        "ls -la /home/snehil/.hermes",
        "cat Knowledge/task-router.md",
        "git diff --stat",
        "ls -la | grep -i pyodbc",
    ):
        assert plugin._pre_tool_call("terminal", {"command": command}, task_id="s") is None, command


def test_terminal_guard_inspects_alternate_argument_keys() -> None:
    assert plugin._pre_tool_call("terminal", {"cmd": "sqlcmd -Q 'SELECT 1'"}, task_id="s")["action"] == "block"


# --------------------------------------------------------------------------
# Bridge transport
# --------------------------------------------------------------------------

def test_bridge_transport_never_prefixes_windows_python_with_python3() -> None:
    completed = mock.Mock(returncode=0, stdout='{"ok":true,"rows":[]}', stderr="")
    with mock.patch.object(plugin.subprocess, "run", return_value=completed) as run:
        result = json.loads(plugin._invoke_bridge(
            {"operation": "query", "database": "XStudio_Xbatch", "sql": "SELECT 1"}))
    assert result["ok"] is True
    argv = run.call_args.args[0]
    assert argv == [plugin.WINDOWS_PYTHON, plugin.BRIDGE_WIN]
    assert "python3" not in argv
    assert json.loads(run.call_args.kwargs["input"])["operation"] == "query"


def test_bridge_transport_failure_is_reported_not_retried() -> None:
    with mock.patch.object(plugin.subprocess, "run", side_effect=OSError("no interpreter")):
        result = json.loads(plugin._invoke_bridge({"operation": "query"}))
    assert result["ok"] is False and result["retry_same_call"] is False


# --------------------------------------------------------------------------
# Read-only / EXEC safety
# --------------------------------------------------------------------------

def test_read_only_guard_rejects_every_write_and_ddl_verb() -> None:
    for sql in (
        "INSERT INTO dbo.X VALUES (1)",
        "UPDATE dbo.X SET A=1",
        "DELETE FROM dbo.X",
        "MERGE dbo.X AS t USING dbo.Y AS s ON 1=1",
        "DROP TABLE dbo.X",
        "ALTER TABLE dbo.X ADD B int",
        "CREATE TABLE dbo.X (A int)",
        "TRUNCATE TABLE dbo.X",
        "GRANT SELECT ON dbo.X TO public",
        "REVOKE SELECT ON dbo.X FROM public",
        "DENY SELECT ON dbo.X TO public",
        "EXEC dbo.SomeProc",
        "EXECUTE dbo.SomeProc",
        "SELECT 1; DROP TABLE dbo.X",
    ):
        assert not bridge.is_read_only_sql(sql), sql


def test_read_only_guard_allows_plain_reads() -> None:
    for sql in (
        "SELECT TOP 20 BatchNo, Status FROM dbo.XStudio_List_XMES_SAP_API_Batch_Creation_Error_Vw",
        "SELECT a.HeatNo FROM dbo.EAF_PER_HEAT a JOIN dbo.LRF_Per_Heat b ON a.HeatNo = b.HeatNo",
    ):
        assert bridge.is_read_only_sql(sql), sql


def test_read_only_guard_does_not_false_positive_inside_string_literals() -> None:
    """Requirement: a keyword inside quoted text is data, not a statement."""
    for sql in (
        "SELECT * FROM dbo.Delay WHERE Reason = 'no update available'",
        "SELECT * FROM dbo.Log WHERE Msg = 'DROP failed' AND Note = 'insert pending'",
        "SELECT * FROM dbo.X WHERE Note = 'it''s an update'",
        "SELECT 'EXEC dbo.Whatever' AS SampleText",
    ):
        assert bridge.is_read_only_sql(sql), sql


def test_read_procedure_rejects_arbitrary_procedure_name() -> None:
    class FakeClient:
        pass
    result = bridge._read_procedure({
        "operation": "read_procedure", "database": "XStudio_Xbatch",
        "run_id": "r1", "procedure": "Dangerous_Write_Usp", "parameters": {},
    }, FakeClient())
    assert result["ok"] is False and result["retry_same_call"] is False
    assert "XMES_Get_API_Transaction_Summary" in result["allowed_procedures"]


def test_read_procedure_rejects_wrong_parameter_shape() -> None:
    class FakeClient:
        pass
    result = bridge._read_procedure({
        "operation": "read_procedure", "database": "XStudio_Xbatch",
        "run_id": "r1", "procedure": "XMES_Get_API_Transaction_Summary",
        "parameters": {"Wrong": "UsageDecision"},
    }, FakeClient())
    assert result["ok"] is False
    assert result["missing_parameters"] == ["APIType"]
    assert result["unknown_parameters"] == ["Wrong"]


def test_read_procedure_accepts_allowlisted_call_with_correct_contract() -> None:
    """The allowlist must actually permit its one reviewed procedure."""
    captured = {}

    class FakeClient:
        def execute_sql(self, **kwargs):
            captured.update(kwargs)
            return json.dumps({"rows": []})

    result = bridge._read_procedure({
        "operation": "read_procedure", "database": "XStudio_Xbatch",
        "run_id": "r1", "procedure": "XMES_Get_API_Transaction_Summary",
        "parameters": {"APIType": "UsageDecision"},
    }, FakeClient())
    assert result["ok"] is True
    assert captured["action_type"] == "READ"
    assert captured["sql"] == "EXEC [dbo].[XMES_Get_API_Transaction_Summary] @APIType = N'UsageDecision';"


def test_read_procedure_escapes_quotes_in_parameter_values() -> None:
    captured = {}

    class FakeClient:
        def execute_sql(self, **kwargs):
            captured.update(kwargs)
            return "{}"

    bridge._read_procedure({
        "operation": "read_procedure", "database": "XStudio_Xbatch", "run_id": "r1",
        "procedure": "XMES_Get_API_Transaction_Summary",
        "parameters": {"APIType": "O'Brien'; DROP TABLE x--"},
    }, FakeClient())
    assert "O''Brien''" in captured["sql"]


def test_database_must_be_explicitly_allowlisted() -> None:
    try:
        bridge._database({"database": "master"})
    except ValueError as exc:
        assert "not allowed" in str(exc)
    else:
        raise AssertionError("master must not be an allowed database")


# --------------------------------------------------------------------------
# Result bounding
# --------------------------------------------------------------------------

def test_result_rows_are_capped() -> None:
    bounded = bridge._bounded_response({"ok": True, "operation": "query",
                                        "rows": [{"i": i} for i in range(500)]})
    assert len(bounded["rows"]) == bridge.MAX_LIST_ITEMS + 1
    assert bounded["rows"][-1]["_truncated_items"] == 500 - bridge.MAX_LIST_ITEMS


def test_oversized_result_is_replaced_with_a_narrowing_instruction() -> None:
    bounded = bridge._bounded_response({
        "ok": True, "operation": "query",
        "rows": [{"blob": "x" * 5000} for _ in range(10)],
    })
    assert bounded["truncated"] is True
    assert len(json.dumps(bounded)) <= bridge.MAX_RESPONSE_CHARS + 200
    assert "narrow" in bounded["message"].lower() or "refine" in bounded["message"].lower()


def test_long_strings_are_truncated_with_a_marker() -> None:
    compact = bridge._compact({"definition": "y" * (bridge.MAX_STRING_CHARS + 100)})
    assert compact["definition"].endswith("chars]")


# --------------------------------------------------------------------------
# Call budget / repeated-failure breaker
# --------------------------------------------------------------------------

def test_repeated_identical_failure_is_blocked_and_different_call_is_not() -> None:
    args = {"operation": "select", "database": "XStudio_Xbatch",
            "table": "dbo.SAP_Posting_Tbl", "columns": ["ID"], "run_id": "run-1"}
    for _ in range(plugin.MAX_IDENTICAL_FAILURES):
        assert plugin._pre_tool_call(plugin.TOOL_NAME, args, task_id="session-a") is None
        plugin._post_tool_call(plugin.TOOL_NAME, args, '{"ok":false,"error":"same failure"}',
                               task_id="session-a")
    blocked = plugin._pre_tool_call(plugin.TOOL_NAME, args, task_id="session-a")
    assert blocked and blocked["action"] == "block" and "Repeated-failure" in blocked["message"]
    # A genuinely different call must still be allowed.
    assert plugin._pre_tool_call(plugin.TOOL_NAME, dict(args, columns=["ID", "Status"]),
                                 task_id="session-a") is None


def test_successful_calls_never_trip_the_failure_breaker() -> None:
    args = {"operation": "get_run_actions", "run_id": "r1"}
    for _ in range(5):
        assert plugin._pre_tool_call(plugin.TOOL_NAME, args, task_id="ok-session") is None
        plugin._post_tool_call(plugin.TOOL_NAME, args, '{"ok":true,"actions":[]}', task_id="ok-session")


def test_failure_breaker_is_scoped_per_session() -> None:
    args = {"operation": "select", "table": "dbo.X", "columns": ["ID"]}
    for _ in range(plugin.MAX_IDENTICAL_FAILURES):
        plugin._pre_tool_call(plugin.TOOL_NAME, args, task_id="session-x")
        plugin._post_tool_call(plugin.TOOL_NAME, args, '{"ok":false}', task_id="session-x")
    assert plugin._pre_tool_call(plugin.TOOL_NAME, args, task_id="session-x")["action"] == "block"
    assert plugin._pre_tool_call(plugin.TOOL_NAME, args, task_id="session-y") is None


def test_session_budget_blocks_excess_tool_calls() -> None:
    old = plugin.MAX_TOOL_CALLS
    plugin.MAX_TOOL_CALLS = 2
    try:
        assert plugin._pre_tool_call(plugin.TOOL_NAME, {"operation": "get_run_actions", "run_id": "1"}, task_id="b") is None
        assert plugin._pre_tool_call(plugin.TOOL_NAME, {"operation": "get_run_actions", "run_id": "2"}, task_id="b") is None
        blocked = plugin._pre_tool_call(plugin.TOOL_NAME, {"operation": "get_run_actions", "run_id": "3"}, task_id="b")
        assert blocked and blocked["action"] == "block" and "budget" in blocked["message"]
    finally:
        plugin.MAX_TOOL_CALLS = old


def test_default_budget_matches_the_reviewed_contract() -> None:
    assert plugin.MAX_TOOL_CALLS == 14
    assert plugin.MAX_IDENTICAL_FAILURES == 2


def test_session_cleanup_releases_counters() -> None:
    plugin._pre_tool_call(plugin.TOOL_NAME, {"operation": "get_run_actions", "run_id": "1"}, task_id="tidy")
    plugin._cleanup_session(task_id="tidy")
    with plugin._lock:
        assert "tidy" not in plugin._session_calls


def test_execution_contract_is_injected_before_each_llm_turn() -> None:
    context = plugin._pre_llm_call()["context"]
    assert "xstudio_l2" in context
    assert "blocked" in context.lower()


# --------------------------------------------------------------------------
# Production card rendering
# --------------------------------------------------------------------------

def test_production_cards_render_typed_contract_and_no_raw_interpreter_recipe() -> None:
    """Fresh cards must not teach the retired transport (requirement 12)."""
    runtime = _load("l2_pipeline_runtime_test", ROOT / "l2_pipeline_runtime.py")
    body = runtime._query_instructions("RUN-1", "TICKET-1")
    assert "xstudio_l2" in body
    assert "RUN-1" in body and "TICKET-1" in body
    for retired in ("/mnt/c/Python314/python.exe", "Hermes_Orchestrator.py", "sqlcmd",
                    "--build-query", "--save-ledger", "pip install"):
        assert retired not in body, f"fresh card still teaches {retired!r}"


def test_scout_entrypoint_delegates_without_monkeypatching_the_renderer() -> None:
    source = (ROOT / "ticket_scout.py").read_text(encoding="utf-8")
    assert "_query_instructions" not in source, "typed contract belongs in the runtime default"
    assert "/mnt/c/Python314/python.exe" not in source


# --------------------------------------------------------------------------
# Profile config patching
# --------------------------------------------------------------------------

_SAMPLE_CONFIG = """\
model:
  default: qwen/qwen3.5-9b
approvals:
  deny:
    - '*.execute(*update *'
plugins:
  enabled:
    - xstudio-l2-trace
    - xstudio-l2-orchestrator
kanban:
  dispatch_in_gateway: true
  dispatch_interval_seconds: 30
  max_in_progress: 1
platforms:
  api_server:
    host: 0.0.0.0
    port: 8642
platform_toolsets:
  cli:
    - terminal
    - todo
known_plugin_toolsets:
  cli:
    - a2a

# ── Security ──────────────────────────────────────────────────────────
# Secret redaction is ON by default.
"""


def _patch_sample(text: str) -> str:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "config.yaml"
        path.write_text(text, encoding="utf-8")
        patcher.patch_file(path)
        return path.read_text(encoding="utf-8")


def test_config_patch_adds_plugin_toolset_and_deny_rules() -> None:
    patched = _patch_sample(_SAMPLE_CONFIG)
    assert "    - xstudio-l2-tools\n" in patched
    assert "    - xstudio_l2\n" in patched
    assert "'*sqlcmd*'" in patched and "'*Hermes_Orchestrator.py*'" in patched
    assert "'*pip install*'" in patched


def test_config_patch_is_idempotent() -> None:
    once = _patch_sample(_SAMPLE_CONFIG)
    twice = _patch_sample(once)
    assert once == twice
    assert once.count("- xstudio-l2-tools") == 1
    assert once.count("'*sqlcmd*'") == 1


def test_config_patch_preserves_comments_and_unrelated_settings() -> None:
    patched = _patch_sample(_SAMPLE_CONFIG)
    assert "# ── Security ──" in patched
    assert "# Secret redaction is ON by default." in patched
    # dispatcher + api server must survive byte-identically
    assert "  dispatch_in_gateway: true\n" in patched
    assert "  dispatch_interval_seconds: 30\n" in patched
    assert "  max_in_progress: 1\n" in patched
    assert "    host: 0.0.0.0\n" in patched
    assert "    port: 8642\n" in patched
    assert "  default: qwen/qwen3.5-9b\n" in patched
    # pre-existing deny entry preserved
    assert "'*.execute(*update *'" in patched


def test_config_patch_preserves_existing_entries_when_partially_present() -> None:
    partial = _SAMPLE_CONFIG.replace(
        "    - xstudio-l2-orchestrator\n",
        "    - xstudio-l2-orchestrator\n    - xstudio-l2-tools\n",
    ).replace("    - '*.execute(*update *'\n", "    - '*.execute(*update *'\n    - '*sqlcmd*'\n")
    patched = _patch_sample(partial)
    assert patched.count("- xstudio-l2-tools") == 1
    assert patched.count("'*sqlcmd*'") == 1
    assert "'*Hermes_Orchestrator.py*'" in patched


def test_config_patch_handles_flow_style_lists() -> None:
    flow = _SAMPLE_CONFIG.replace("  cli:\n    - terminal\n    - todo\n", "  cli: [terminal, todo]\n")
    patched = _patch_sample(flow)
    assert "xstudio_l2" in patched
    assert "[terminal, todo, xstudio_l2]" in patched


def test_config_patch_does_not_abort_when_optional_section_absent() -> None:
    without = _SAMPLE_CONFIG.replace("known_plugin_toolsets:\n  cli:\n    - a2a\n", "")
    patched = _patch_sample(without)
    assert "- xstudio-l2-tools" in patched  # other sections still applied


def main() -> int:
    tests = [value for name, value in sorted(globals().items())
             if name.startswith("test_") and callable(value)]
    failures = []
    for test in tests:
        setup_function()
        try:
            test()
            print(f"PASS {test.__name__}")
        except Exception as exc:
            failures.append((test.__name__, exc))
            print(f"FAIL {test.__name__}: {type(exc).__name__}: {exc}")
    if failures:
        print(f"\n{len(failures)} of {len(tests)} typed-tool contract tests FAILED.")
        return 1
    print(f"\n{len(tests)} typed-tool contract tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
