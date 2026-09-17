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
        plugin._session_context.clear()


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


def test_typed_tool_guard_rejects_operation_without_required_fields_before_budget() -> None:
    blocked = plugin._pre_tool_call(plugin.TOOL_NAME, {
        "operation": "select", "table": "dbo.CCM_Per_Heat", "columns": ["HeatID"]
    }, task_id="shape")
    assert blocked and blocked["action"] == "block"
    assert "database" in blocked["message"]
    with plugin._lock:
        assert plugin._session_calls["shape"] == 0


def test_typed_tool_guard_requires_operation_specific_arguments() -> None:
    blocked = plugin._pre_tool_call(plugin.TOOL_NAME, {
        "operation": "get_definition", "database": "XStudio_Xbatch"
    }, task_id="shape-definition")
    assert blocked and blocked["action"] == "block"
    assert "object_name" in blocked["message"]


def test_named_tool_schemas_have_small_required_contracts() -> None:
    expected = {
        "xstudio_select": {"database", "table", "columns"},
        "xstudio_query": {"database", "sql"},
        "xstudio_suggest_tables": {"database", "search"},
        "xstudio_find_objects": {"database", "search"},
        "xstudio_get_definition": {"database", "object_name"},
        "xstudio_validate_identifiers": {"database", "table"},
        "xstudio_read_procedure": {"database", "procedure", "parameters"},
        "xstudio_resolve_heat": {"heat"},
        "xstudio_get_ticket_context": set(),
        "xstudio_get_run_actions": set(),
        "xstudio_save_ledger": {"ledger"},
        "xstudio_heat_context": {"heat"},
        "xstudio_sap_api_context": {"api_type"},
        "xstudio_work_order_context": {"work_order"},
        "xstudio_submit_proposal": {"response_type", "summary"},
    }
    assert set(plugin.TOOL_SCHEMAS) == set(expected)
    for name, required in expected.items():
        schema = plugin.TOOL_SCHEMAS[name]["parameters"]
        assert set(schema["required"]) == required
        assert schema["additionalProperties"] is False
        assert "operation" not in schema["properties"]
    # Effective required fields after repair must guarantee SQL safety:
    assert plugin._EFFECTIVE_REQUIRED_FIELDS_BY_TOOL["xstudio_resolve_heat"] == ("database", "heat")
    assert plugin._EFFECTIVE_REQUIRED_FIELDS_BY_TOOL["xstudio_get_ticket_context"] == ("ticket_id",)
    assert plugin._EFFECTIVE_REQUIRED_FIELDS_BY_TOOL["xstudio_get_run_actions"] == ("run_id",)
    assert plugin._EFFECTIVE_REQUIRED_FIELDS_BY_TOOL["xstudio_save_ledger"] == ("run_id", "ledger")
    assert plugin._EFFECTIVE_REQUIRED_FIELDS_BY_TOOL["xstudio_read_procedure"] == ("database", "run_id", "procedure", "parameters")


def test_register_exposes_named_tools_and_not_legacy_polymorphic_tool() -> None:
    calls = []

    class Context:
        def register_tool(self, **kwargs):
            calls.append(kwargs)

        def register_hook(self, *args, **kwargs):
            pass

    plugin.register(Context())
    names = {call["name"] for call in calls}
    assert names == set(plugin.TOOL_SCHEMAS)
    assert "xstudio_l2" not in names


def test_repairable_context_is_injected_before_budget() -> None:
    plugin._pre_llm_call(
        task_id="task-context",
        user_message="Current run_id: RUN-1\nCurrent ticket_id: TICKET-1",
    )
    # 1. resolve_heat defaults database to XStudio_Xbatch and injects run_id:
    modified = plugin._pre_tool_call(
        "xstudio_resolve_heat", {"heat": "H99328"}, task_id="task-context"
    )
    assert modified and modified["action"] == "modify"
    assert modified["args"]["database"] == "XStudio_Xbatch"
    assert modified["args"]["run_id"] == "RUN-1"

    # 2. get_ticket_context injects ticket_id:
    mod_tc = plugin._pre_tool_call("xstudio_get_ticket_context", {}, task_id="task-context")
    assert mod_tc and mod_tc["action"] == "modify"
    assert mod_tc["args"]["ticket_id"] == "TICKET-1"

    # 3. get_run_actions injects run_id:
    mod_ra = plugin._pre_tool_call("xstudio_get_run_actions", {}, task_id="task-context")
    assert mod_ra and mod_ra["action"] == "modify"
    assert mod_ra["args"]["run_id"] == "RUN-1"

    # 4. save_ledger injects run_id:
    mod_sl = plugin._pre_tool_call("xstudio_save_ledger", {"ledger": {"ok": True}}, task_id="task-context")
    assert mod_sl and mod_sl["action"] == "modify"
    assert mod_sl["args"]["run_id"] == "RUN-1"

    # 5. read_procedure injects run_id:
    mod_rp = plugin._pre_tool_call("xstudio_read_procedure", {
        "database": "XStudio_Configuration_Xbatch",
        "procedure": "XMES_Get_API_Transaction_Summary",
        "parameters": {"APIType": "UsageDecision"},
    }, task_id="task-context")
    assert mod_rp and mod_rp["action"] == "modify"
    assert mod_rp["args"]["run_id"] == "RUN-1"


def test_ambiguous_missing_database_is_rejected_before_budget() -> None:
    blocked = plugin._pre_tool_call(
        "xstudio_suggest_tables", {"search": "SAP posting pending"}, task_id="ambiguous"
    )
    assert blocked and blocked["action"] == "block"
    assert "database" in blocked["message"]
    with plugin._lock:
        assert plugin._session_calls["ambiguous"] == 0


def test_named_handler_injects_operation_without_exposing_it() -> None:
    captured = {}

    def fake_invoke(args):
        captured.update(args)
        return '{"ok":true}'

    with mock.patch.object(plugin, "_invoke_bridge", side_effect=fake_invoke):
        result = plugin.TOOL_HANDLERS["xstudio_query"](
            {"database": "XStudio_Xbatch", "sql": "SELECT 1"}, task_id="task-1"
        )
    assert json.loads(result)["ok"] is True
    assert captured["operation"] == "query"
    assert "operation" not in {"database": "XStudio_Xbatch", "sql": "SELECT 1"}


def test_plugin_manifest_declares_registered_toolset() -> None:
    manifest = (ROOT / "xstudio_l2_tools_plugin" / "plugin.yaml").read_text(encoding="utf-8")
    assert "provides_tools:" in manifest
    assert "  - xstudio_select" in manifest
    assert "  - xstudio_save_ledger" in manifest
    assert "  - xstudio_l2\n" not in manifest


def test_terminal_guard_inspects_alternate_argument_keys() -> None:
    assert plugin._pre_tool_call("terminal", {"cmd": "sqlcmd -Q 'SELECT 1'"}, task_id="s")["action"] == "block"


# --------------------------------------------------------------------------
# Bridge transport
# --------------------------------------------------------------------------

def test_bridge_transport_uses_the_current_wsl_python_directly() -> None:
    completed = mock.Mock(returncode=0, stdout='{"ok":true,"rows":[]}', stderr="")
    with mock.patch.object(plugin.subprocess, "run", return_value=completed) as run:
        result = json.loads(plugin._invoke_bridge(
            {"operation": "query", "database": "XStudio_Xbatch", "sql": "SELECT 1"}))
    assert result["ok"] is True
    argv = run.call_args.args[0]
    assert argv == [sys.executable, plugin.BRIDGE_PATH]
    # The test runner can be Windows; the invariant is that production uses
    # its current interpreter, not a hard-coded Windows interpreter path.
    assert argv[0] == sys.executable
    assert json.loads(run.call_args.kwargs["input"])["operation"] == "query"


def test_semantic_context_tools_have_tiny_typed_inputs() -> None:
    heat = plugin.TOOL_SCHEMAS["xstudio_heat_context"]["parameters"]
    api = plugin.TOOL_SCHEMAS["xstudio_sap_api_context"]["parameters"]
    work_order = plugin.TOOL_SCHEMAS["xstudio_work_order_context"]["parameters"]
    assert set(heat["required"]) == {"heat"}
    assert set(api["required"]) == {"api_type"}
    assert set(work_order["required"]) == {"work_order"}
    assert heat["additionalProperties"] is False
    assert api["additionalProperties"] is False
    assert work_order["additionalProperties"] is False


def test_semantic_context_tools_default_to_xbatch_and_receive_run_context() -> None:
    plugin._pre_llm_call(task_id="semantic", user_message="run_id: RUN-1\nticket_id: TICKET-1")
    heat = plugin._pre_tool_call("xstudio_heat_context", {"heat": "1900001"}, task_id="semantic")
    api = plugin._pre_tool_call("xstudio_sap_api_context", {"api_type": "UsageDecision"}, task_id="semantic")
    assert heat and heat["action"] == "modify"
    assert api and api["action"] == "modify"
    assert heat["args"]["database"] == "XStudio_Xbatch"
    assert api["args"]["database"] == "XStudio_Xbatch"
    assert heat["args"]["run_id"] == "RUN-1"
    assert api["args"]["run_id"] == "RUN-1"


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
        def execute_readonly_sql_with_rows(self, **kwargs):
            captured.update(kwargs)
            return "action-1", [{"TransactionID": "tx-1"}]
        def update_sql_action_evidence(self, *args, **kwargs):
            pass

    result = bridge._read_procedure({
        "operation": "read_procedure", "database": "XStudio_Xbatch",
        "run_id": "r1", "procedure": "XMES_Get_API_Transaction_Summary",
        "parameters": {"APIType": "UsageDecision"},
    }, FakeClient())
    assert result["ok"] is True
    assert captured["sql"] == "EXEC [dbo].[XMES_Get_API_Transaction_Summary] @APIType = N'UsageDecision';"
    assert result["result"] == [{"TransactionID": "tx-1"}]


def test_read_procedure_escapes_quotes_in_parameter_values() -> None:
    captured = {}

    class FakeClient:
        def execute_readonly_sql_with_rows(self, **kwargs):
            captured.update(kwargs)
            return "action-1", []
        def update_sql_action_evidence(self, *args, **kwargs):
            pass

    bridge._read_procedure({
        "operation": "read_procedure", "database": "XStudio_Xbatch", "run_id": "r1",
        "procedure": "XMES_Get_API_Transaction_Summary",
        "parameters": {"APIType": "O'Brien'; DROP TABLE x--"},
    }, FakeClient())
    assert "O''Brien''" in captured["sql"]


def test_semantic_read_executes_once_through_the_audited_database_path() -> None:
    captured = {}

    class FakeClient:
        def execute_readonly_sql_with_rows(self, **kwargs):
            captured.update(kwargs)
            return "action-1", [{"HeatID": 1602522}]
        def update_sql_action_evidence(self, *args, **kwargs):
            captured["evidence"] = (args, kwargs)

    rows, ref = bridge._semantic_read(
        FakeClient(), run_id="run-1", sql="SELECT HeatID FROM dbo.EAF_PER_HEAT WHERE HeatID = ?",
        parameters=(1602522,), operation_name="l2_heat_eaf", object_name="EAF_PER_HEAT",
        purpose="Canonical EAF state for heat",
    )
    assert rows == [{"HeatID": 1602522}]
    assert ref == {"action_id": "action-1", "operation": "l2_heat_eaf"}
    assert captured["database_name"] == "XStudio_Xbatch"
    assert captured["sql"].endswith("HeatID = 1602522")


def test_work_order_context_uses_fixed_validated_recipes() -> None:
    calls = []

    class FakeClient:
        def execute_readonly_sql_with_rows(self, **kwargs):
            calls.append(kwargs)
            return f"action-{len(calls)}", []
        def update_sql_action_evidence(self, *args, **kwargs):
            pass

    result = bridge._work_order_context({
        "database": "XStudio_Xbatch", "run_id": "run-1",
        "work_order": "WO-99402", "campaign": "CMP-9902",
    }, FakeClient())

    assert result["ok"] is True
    assert result["normalized_identifiers"] == {
        "work_order": "WO-99402", "campaign": "CMP-9902"
    }
    assert len(calls) == 3
    assert all(call["database_name"] == "XStudio_Xbatch" for call in calls)
    assert any("WorkOrderNumber" in call["sql"] for call in calls)
    assert any("CampaignNo" in call["sql"] for call in calls)


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


def test_resolve_heat_checks_known_numeric_and_prefixed_surfaces() -> None:
    class Client:
        def close(self):
            pass

    class Orchestrator:
        @staticmethod
        def run_readonly_query(client, sql, *, database, run_id):
            return next(Orchestrator.rows)

    Orchestrator.rows = iter([
             [{"HeatNo": "H99328", "StrandNo": 1}], [], [], []
    ])
    with mock.patch.object(bridge, "_client", return_value=Client()), \
         mock.patch.object(bridge, "_orchestrator", return_value=Orchestrator), \
         mock.patch.object(Orchestrator, "run_readonly_query", wraps=Orchestrator.run_readonly_query) as run:
        result = bridge.dispatch({
            "operation": "resolve_heat", "database": "XStudio_Xbatch",
            "heat": "H99328", "run_id": "run-1",
        })
    assert result["ok"] is True
    assert result["input"] == "H99328"
    assert result["matches"][0]["rows"] == 1
    assert run.call_count == len(bridge.HEAT_RESOLUTION_SURFACES)
    assert all("99328" in call.args[1] for call in run.call_args_list)


def test_long_strings_are_truncated_with_a_marker() -> None:
    compact = bridge._compact({"definition": "y" * (bridge.MAX_STRING_CHARS + 100)})
    assert compact["definition"].endswith("chars]")


# --------------------------------------------------------------------------
# Call budget / repeated-failure breaker
# --------------------------------------------------------------------------

def test_repeated_identical_failure_is_blocked_and_different_call_is_not() -> None:
    # 1. Test named model-facing path
    named_args = {"database": "XStudio_Xbatch", "table": "dbo.SAP_Posting_Tbl", "columns": ["ID"]}
    for _ in range(plugin.MAX_IDENTICAL_FAILURES):
        assert plugin._pre_tool_call("xstudio_select", named_args, task_id="session-named") is None
        plugin._post_tool_call("xstudio_select", named_args, '{"ok":false,"error":"same failure"}',
                               task_id="session-named")
    blocked = plugin._pre_tool_call("xstudio_select", named_args, task_id="session-named")
    assert blocked and blocked["action"] == "block" and "Repeated-failure" in blocked["message"]
    # A genuinely different named call must still be allowed.
    assert plugin._pre_tool_call("xstudio_select", dict(named_args, columns=["ID", "Status"]),
                                 task_id="session-named") is None

    # 2. Test legacy compatibility path
    args = {"operation": "select", "database": "XStudio_Xbatch",
            "table": "dbo.SAP_Posting_Tbl", "columns": ["ID"], "run_id": "run-1"}
    for _ in range(plugin.MAX_IDENTICAL_FAILURES):
        assert plugin._pre_tool_call(plugin.TOOL_NAME, args, task_id="session-a") is None
        plugin._post_tool_call(plugin.TOOL_NAME, args, '{"ok":false,"error":"same failure"}',
                               task_id="session-a")
    blocked_legacy = plugin._pre_tool_call(plugin.TOOL_NAME, args, task_id="session-a")
    assert blocked_legacy and blocked_legacy["action"] == "block" and "Repeated-failure" in blocked_legacy["message"]


def test_repaired_call_fingerprint_matches_post_tool_call_with_original_args() -> None:
    """Repaired/defaulted args must produce the exact same fingerprint in pre and post hooks.

    When Qwen calls xstudio_resolve_heat without database, _pre_tool_call modifies
    the args. Even if Hermes passes the original unmodified args to _post_tool_call,
    _post_tool_call must apply _repair_args so the failure counter matches.
    """
    plugin._pre_llm_call(
        task_id="session-repair-fp",
        user_message="Current run_id: RUN-RP\nCurrent ticket_id: TICKET-RP",
    )
    original_args = {"heat": "H99328"}
    for _ in range(plugin.MAX_IDENTICAL_FAILURES):
        res = plugin._pre_tool_call("xstudio_resolve_heat", original_args, task_id="session-repair-fp")
        assert res and res["action"] == "modify"
        # Hermes hook delivers original unmodified args to post_tool_call:
        plugin._post_tool_call("xstudio_resolve_heat", original_args, '{"ok":false,"error":"timeout"}',
                               task_id="session-repair-fp")

    # The next attempt must be blocked by the repeated failure breaker:
    blocked = plugin._pre_tool_call("xstudio_resolve_heat", original_args, task_id="session-repair-fp")
    assert blocked and blocked["action"] == "block" and "Repeated-failure" in blocked["message"]


def test_session_isolation_context_does_not_leak_across_sessions() -> None:
    """Session A's context must never leak into Session B."""
    plugin._pre_llm_call(task_id="sess-a", user_message="Current run_id: RUN-A\nCurrent ticket_id: TICKET-A")
    plugin._pre_llm_call(task_id="sess-b", user_message="Current run_id: RUN-B\nCurrent ticket_id: TICKET-B")

    mod_a = plugin._pre_tool_call("xstudio_get_ticket_context", {}, task_id="sess-a")
    mod_b = plugin._pre_tool_call("xstudio_get_ticket_context", {}, task_id="sess-b")
    assert mod_a and mod_a["args"]["ticket_id"] == "TICKET-A"
    assert mod_b and mod_b["args"]["ticket_id"] == "TICKET-B"

    # A session with no context must fail closed rather than borrowing from another session:
    blocked_c = plugin._pre_tool_call("xstudio_get_ticket_context", {}, task_id="sess-c")
    assert blocked_c and blocked_c["action"] == "block"
    assert "ticket_id" in blocked_c["message"]


def test_kanban_show_seeds_model_hidden_run_and_ticket_context() -> None:
    plugin._post_tool_call(
        "kanban_show",
        {},
        '{"task":{"body":"run_id: RUN-CARD\\nticket_id: TICKET-CARD\\n"}}',
        task_id="card-session",
    )

    repaired = plugin._pre_tool_call(
        "xstudio_heat_context", {"heat": "1602522"}, task_id="card-session"
    )

    assert repaired and repaired["action"] == "modify"
    assert repaired["args"] == {
        "run_id": "RUN-CARD", "ticket_id": "TICKET-CARD", "database": "XStudio_Xbatch"
    }


def test_successful_calls_never_trip_the_failure_breaker() -> None:
    plugin._pre_llm_call(task_id="ok-session", user_message="Current run_id: RUN-OK")
    for _ in range(5):
        assert plugin._pre_tool_call("xstudio_get_run_actions", {}, task_id="ok-session")["action"] == "modify"
        plugin._post_tool_call("xstudio_get_run_actions", {}, '{"ok":true,"actions":[]}', task_id="ok-session")


def test_failure_breaker_is_scoped_per_session() -> None:
    args = {"database": "XStudio_Xbatch", "table": "dbo.X", "columns": ["ID"]}
    for _ in range(plugin.MAX_IDENTICAL_FAILURES):
        plugin._pre_tool_call("xstudio_select", args, task_id="session-x")
        plugin._post_tool_call("xstudio_select", args, '{"ok":false}', task_id="session-x")
    assert plugin._pre_tool_call("xstudio_select", args, task_id="session-x")["action"] == "block"
    assert plugin._pre_tool_call("xstudio_select", args, task_id="session-y") is None


def test_session_budget_blocks_excess_tool_calls() -> None:
    old = plugin.MAX_TOOL_CALLS
    plugin.MAX_TOOL_CALLS = 2
    try:
        assert plugin._pre_tool_call("xstudio_query", {"database": "XStudio_Xbatch", "sql": "SELECT 1"}, task_id="b") is None
        assert plugin._pre_tool_call("xstudio_query", {"database": "XStudio_Xbatch", "sql": "SELECT 2"}, task_id="b") is None
        blocked = plugin._pre_tool_call("xstudio_query", {"database": "XStudio_Xbatch", "sql": "SELECT 3"}, task_id="b")
        assert blocked and blocked["action"] == "block" and "budget" in blocked["message"]
    finally:
        plugin.MAX_TOOL_CALLS = old


def test_default_budget_matches_the_reviewed_contract() -> None:
    assert plugin.MAX_TOOL_CALLS == 14
    assert plugin.MAX_IDENTICAL_FAILURES == 2


def test_session_cleanup_releases_counters() -> None:
    plugin._pre_llm_call(task_id="tidy", user_message="Current run_id: RUN-TIDY")
    plugin._pre_tool_call("xstudio_get_run_actions", {}, task_id="tidy")
    plugin._cleanup_session(task_id="tidy")
    with plugin._lock:
        assert "tidy" not in plugin._session_calls
        assert "tidy" not in plugin._session_context
        assert "tidy" not in plugin._session_failures


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
    for tool_name in ("xstudio_select", "xstudio_query", "xstudio_suggest_tables",
                      "xstudio_resolve_heat", "xstudio_save_ledger"):
        assert tool_name in body
    assert "RUN-1" in body and "TICKET-1" in body
    assert "resolve_heat" in body
    assert "Evidence status: INCOMPLETE" in body
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


# --------------------------------------------------------------------------
# xstudio_submit_proposal (flat completion tool)
# --------------------------------------------------------------------------

def _setup_investigator_context(task_id: str = "submit-test",
                                run_id: str = "RUN-SP", ticket_id: str = "TICKET-SP") -> None:
    """Seed session context so the handler can resolve run_id/ticket_id."""
    plugin._pre_llm_call(
        task_id=task_id,
        user_message=f"run_id: {run_id}\nticket_id: {ticket_id}\npipeline_stage: investigation",
    )


_SUBSTANTIVE_SUMMARY = (
    "Investigated the reported SAP usage decision for Heat 1900002 / Inspection Lot "
    "49900000002. The XStudio_Xbatch canonical surfaces contain no EAF, LRF, CCM, "
    "work-order, SAP posting, or billet genealogy rows for this heat. No UsageDecision "
    "API transaction exists for identifier 49900000002."
)


def test_submit_proposal_assembles_complete_metadata_from_flat_args() -> None:
    _setup_investigator_context()
    with mock.patch.object(plugin.subprocess, "run") as mock_run:
        mock_run.return_value = mock.Mock(returncode=0, stdout="", stderr="")
        result = plugin._submit_proposal_handler(
            {"response_type": "UPDATE", "summary": _SUBSTANTIVE_SUMMARY},
            task_id="submit-test",
        )
    parsed = json.loads(result)
    assert parsed["ok"] is True
    assert parsed["response_type"] == "UPDATE"
    assert parsed["claim_status"] == "UNVERIFIED"
    assert parsed["evidence_status"] == "INCOMPLETE"
    # Verify the metadata passed to hermes kanban complete
    call_args = mock_run.call_args[0][0]
    assert call_args[:4] == ["hermes", "kanban", "complete", "submit-test"]
    metadata_idx = call_args.index("--metadata")
    metadata = json.loads(call_args[metadata_idx + 1])
    assert metadata["run_id"] == "RUN-SP"
    assert metadata["ticket_id"] == "TICKET-SP"
    assert metadata["response_type"] == "UPDATE"
    assert metadata["claims_contract_version"] == 1
    assert metadata["submitted_via"] == "xstudio_submit_proposal"
    assert len(metadata["claims"]) == 1
    claim = metadata["claims"][0]
    assert claim["id"] == "C1"
    assert claim["claim"] == _SUBSTANTIVE_SUMMARY
    assert claim["material"] is True
    assert claim["status"] == "UNVERIFIED"
    assert claim["evidence"] == []


def test_submit_proposal_requires_response_type_and_summary() -> None:
    _setup_investigator_context(task_id="submit-missing")
    # Missing response_type
    result = json.loads(plugin._submit_proposal_handler(
        {"summary": _SUBSTANTIVE_SUMMARY},
        task_id="submit-missing",
    ))
    assert result["ok"] is False
    assert "response_type" in result["error"]

    # Missing summary
    result = json.loads(plugin._submit_proposal_handler(
        {"response_type": "UPDATE", "summary": "Too short"},
        task_id="submit-missing",
    ))
    assert result["ok"] is False
    assert "160" in result["error"] or "characters" in result["error"]


def test_submit_proposal_requires_action_id_for_verified_claims() -> None:
    _setup_investigator_context(task_id="submit-verified")
    result = json.loads(plugin._submit_proposal_handler(
        {"response_type": "RESOLUTION", "summary": _SUBSTANTIVE_SUMMARY,
         "claim_status": "VERIFIED"},
        task_id="submit-verified",
    ))
    assert result["ok"] is False
    assert "action_id" in result["error"]


def test_submit_proposal_verified_claim_with_action_id_passes() -> None:
    _setup_investigator_context(task_id="submit-verified-ok")
    with mock.patch.object(plugin.subprocess, "run") as mock_run:
        mock_run.return_value = mock.Mock(returncode=0, stdout="", stderr="")
        result = json.loads(plugin._submit_proposal_handler(
            {"response_type": "RESOLUTION", "summary": _SUBSTANTIVE_SUMMARY,
             "claim_status": "VERIFIED", "action_id": "ACTION-123"},
            task_id="submit-verified-ok",
        ))
    assert result["ok"] is True
    assert result["claim_status"] == "VERIFIED"
    assert result["evidence_status"] == "COMPLETE"
    metadata = json.loads(mock_run.call_args[0][0][mock_run.call_args[0][0].index("--metadata") + 1])
    assert metadata["claims"][0]["evidence"] == [{"action_id": "ACTION-123"}]


def test_submit_proposal_generates_reply_text_when_absent() -> None:
    _setup_investigator_context(task_id="submit-reply")
    with mock.patch.object(plugin.subprocess, "run") as mock_run:
        mock_run.return_value = mock.Mock(returncode=0, stdout="", stderr="")
        plugin._submit_proposal_handler(
            {"response_type": "UPDATE", "summary": _SUBSTANTIVE_SUMMARY},
            task_id="submit-reply",
        )
    metadata = json.loads(mock_run.call_args[0][0][mock_run.call_args[0][0].index("--metadata") + 1])
    assert metadata["reply_text"].startswith("Evidence status: INCOMPLETE.")
    assert _SUBSTANTIVE_SUMMARY in metadata["reply_text"]


def test_submit_proposal_uses_explicit_reply_text_when_provided() -> None:
    _setup_investigator_context(task_id="submit-reply-explicit")
    with mock.patch.object(plugin.subprocess, "run") as mock_run:
        mock_run.return_value = mock.Mock(returncode=0, stdout="", stderr="")
        plugin._submit_proposal_handler(
            {"response_type": "UPDATE", "summary": _SUBSTANTIVE_SUMMARY,
             "reply_text": "Custom user-facing message."},
            task_id="submit-reply-explicit",
        )
    metadata = json.loads(mock_run.call_args[0][0][mock_run.call_args[0][0].index("--metadata") + 1])
    assert metadata["reply_text"] == "Custom user-facing message."


def test_submit_proposal_injects_run_and_ticket_from_context() -> None:
    _setup_investigator_context(task_id="submit-ctx", run_id="CTX-RUN", ticket_id="CTX-TICKET")
    with mock.patch.object(plugin.subprocess, "run") as mock_run:
        mock_run.return_value = mock.Mock(returncode=0, stdout="", stderr="")
        plugin._submit_proposal_handler(
            {"response_type": "UPDATE", "summary": _SUBSTANTIVE_SUMMARY},
            task_id="submit-ctx",
        )
    metadata = json.loads(mock_run.call_args[0][0][mock_run.call_args[0][0].index("--metadata") + 1])
    assert metadata["run_id"] == "CTX-RUN"
    assert metadata["ticket_id"] == "CTX-TICKET"


def test_submit_proposal_does_not_consume_xstudio_tool_budget() -> None:
    _setup_investigator_context(task_id="submit-budget")
    # Fill up the budget to MAX_TOOL_CALLS - 1
    with plugin._lock:
        plugin._session_calls["submit-budget"] = plugin.MAX_TOOL_CALLS - 1
    # The pre_tool_call should not block xstudio_submit_proposal
    result = plugin._pre_tool_call(
        "xstudio_submit_proposal",
        {"response_type": "UPDATE", "summary": _SUBSTANTIVE_SUMMARY},
        task_id="submit-budget",
    )
    assert result is None  # passes through without consuming budget
    # Budget should be unchanged
    with plugin._lock:
        assert plugin._session_calls["submit-budget"] == plugin.MAX_TOOL_CALLS - 1


def test_submit_proposal_sets_incomplete_evidence_for_update() -> None:
    _setup_investigator_context(task_id="submit-evidence")
    with mock.patch.object(plugin.subprocess, "run") as mock_run:
        mock_run.return_value = mock.Mock(returncode=0, stdout="", stderr="")
        result = json.loads(plugin._submit_proposal_handler(
            {"response_type": "UPDATE", "summary": _SUBSTANTIVE_SUMMARY,
             "claim_status": "INFERRED"},
            task_id="submit-evidence",
        ))
    assert result["evidence_status"] == "INCOMPLETE"


def test_submit_proposal_includes_optional_fields_in_metadata() -> None:
    _setup_investigator_context(task_id="submit-optional")
    with mock.patch.object(plugin.subprocess, "run") as mock_run:
        mock_run.return_value = mock.Mock(returncode=0, stdout="", stderr="")
        plugin._submit_proposal_handler(
            {"response_type": "UPDATE", "summary": _SUBSTANTIVE_SUMMARY,
             "problem_summary": "SAP posting missing",
             "root_cause": "Heat not in MES",
             "resolution": "Manual data entry required"},
            task_id="submit-optional",
        )
    metadata = json.loads(mock_run.call_args[0][0][mock_run.call_args[0][0].index("--metadata") + 1])
    assert metadata["problem_summary"] == "SAP posting missing"
    assert metadata["root_cause"] == "Heat not in MES"
    assert metadata["resolution"] == "Manual data entry required"


def test_submit_proposal_rejects_when_context_missing() -> None:
    # Don't set up context
    result = json.loads(plugin._submit_proposal_handler(
        {"response_type": "UPDATE", "summary": _SUBSTANTIVE_SUMMARY},
        task_id="submit-no-context",
    ))
    assert result["ok"] is False
    assert "run_id" in result["error"]


def test_empty_kanban_completion_is_repaired_without_another_model_turn() -> None:
    result = plugin._pre_tool_call("kanban_complete", {}, task_id="task-1")
    assert result and result["action"] == "modify"
    assert result["args"]["summary"]


def test_investigator_completion_without_proposal_metadata_is_blocked_for_same_turn_retry() -> None:
    plugin._pre_llm_call(
        task_id="investigator-completion",
        user_message=("run_id: RUN-1\nticket_id: TICKET-1\n"
                      "pipeline_stage: investigation\nclaims_contract_version: 1"),
    )
    result = plugin._pre_tool_call(
        "kanban_complete",
        {"summary": "No rows were found for the supplied heat identifier.", "metadata": {}},
        task_id="investigator-completion",
    )
    assert result and result["action"] == "block"
    assert "response_type" in result["message"]
    assert "claims" in result["message"]
    assert "retry kanban_complete" in result["message"]


def test_substantive_investigator_summary_is_packaged_without_another_model_turn() -> None:
    plugin._pre_llm_call(
        task_id="investigator-summary-package",
        user_message=("run_id: RUN-2\nticket_id: TICKET-2\n"
                      "pipeline_stage: investigation\nclaims_contract_version: 1"),
    )
    summary = (
        "Investigated the reported SAP posting and preserved the current-run action trail. "
        "The available evidence does not yet prove that the successful transaction belongs "
        "to the reported heat and work-order pair, so independent review is required."
    )
    result = plugin._pre_tool_call(
        "kanban_complete",
        {"summary": summary, "result": "Investigation complete", "metadata": {}},
        task_id="investigator-summary-package",
    )
    assert result and result["action"] == "modify"
    metadata = result["args"]["metadata"]
    assert metadata["run_id"] == "RUN-2"
    assert metadata["ticket_id"] == "TICKET-2"
    assert metadata["response_type"] == "UPDATE"
    assert metadata["claims_contract_version"] == 1
    assert metadata["claims"] == [{
        "id": "summary-1",
        "claim": summary,
        "material": True,
        "status": "UNVERIFIED",
        "evidence": [],
    }]
    assert metadata["contract_packaged_from_summary"] is True
    assert metadata["evidence_status"] == "INCOMPLETE"
    assert metadata["reply_text"].startswith("Evidence status: INCOMPLETE.")


def test_reviewer_completion_does_not_require_investigator_proposal_metadata() -> None:
    plugin._pre_llm_call(
        task_id="reviewer-completion",
        user_message="run_id: RUN-1\nticket_id: TICKET-1\npipeline_stage: review",
    )
    result = plugin._pre_tool_call(
        "kanban_complete",
        {"summary": "Approved after independent live verification."},
        task_id="reviewer-completion",
    )
    assert result is None


def test_reviewer_cannot_approve_runtime_repaired_unstructured_proposal() -> None:
    plugin._pre_llm_call(
        task_id="reviewer-repaired-proposal",
        user_message=(
            "run_id: RUN-1\nticket_id: TICKET-1\npipeline_stage: review\n"
            'proposal_json: {"response_type":"UPDATE",'
            '"contract_repaired_from_unstructured":true}'
        ),
    )
    result = plugin._pre_tool_call(
        "kanban_complete",
        {"summary": "Approved despite missing investigator contract."},
        task_id="reviewer-repaired-proposal",
    )
    assert result and result["action"] == "block"
    assert "kanban_block" in result["message"]
    assert "repaired" in result["message"].lower()


def test_empty_kanban_block_is_repaired_with_a_safe_reason() -> None:
    result = plugin._pre_tool_call("kanban_block", {}, task_id="task-1")
    assert result and result["action"] == "modify"
    assert result["args"]["reason"]


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
