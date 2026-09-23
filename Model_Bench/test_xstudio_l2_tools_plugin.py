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


def test_definition_accepts_discovered_qualified_names_and_rejects_schema_conflicts() -> None:
    client = mock.Mock()
    client.get_sql_object_definition.return_value = {}
    with mock.patch.object(bridge, "_client", return_value=client):
        for name in ("dbo.LRF_Per_Heat", "[dbo].[LRF_Per_Heat]", "LRF_Per_Heat"):
            result = bridge.dispatch({"operation": "get_definition", "database": "XStudio_Xbatch",
                                      "object_name": name})
            assert result["ok"], result
            client.get_sql_object_definition.assert_called_with(
                database_name="XStudio_Xbatch", schema_name="dbo", object_name="LRF_Per_Heat")
        client.get_sql_object_definition.reset_mock()
        try:
            bridge.dispatch({"operation": "get_definition", "database": "XStudio_Xbatch",
                             "object_name": "dbo.LRF_Per_Heat", "schema": "other"})
        except ValueError as exc:
            assert "conflicts" in str(exc)
        else:
            raise AssertionError("conflicting schemas must be rejected")
        client.get_sql_object_definition.assert_not_called()


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
        "xstudio_select": {"database", "table"},  # columns optional: bridge resolves
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
        "xstudio_read_table": {"table"},  # filter + columns chosen by the harness
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


def test_probe_table_uses_real_identifier_and_never_broad_fishes() -> None:
    class FakeOrchestrator:
        @staticmethod
        def build_query_mechanically(**kwargs):
            assert kwargs["table"] == "dbo.Heat_Vw"
            assert "[HeatNo] = N'H123'" in kwargs["where"]
            assert "HeatNo" in kwargs["columns"]
            return {"ok": True, "sql": "SELECT ...", "table": "dbo.Heat_Vw"}

        @staticmethod
        def run_readonly_query(client, sql, database, run_id=None):
            assert database == "XStudio_Xbatch"
            assert run_id == "r1"
            return [{"HeatNo": "H123", "Status": "Running"}]

    allowlist = {"XStudio_Xbatch": {"dbo.Heat_Vw": ["HeatNo", "Status", "Reason", "EventTime"]}}
    with mock.patch.object(bridge, "_load_allowlist", return_value=allowlist), \
         mock.patch.object(bridge, "_orchestrator", return_value=FakeOrchestrator()):
        result = bridge._probe_table({
            "operation": "probe_table",
            "database": "XStudio_Xbatch",
            "table": "dbo.Heat_Vw",
            "ticket": {"HeatNo": "H123"},
            "run_id": "r1",
            "matched_columns": ["Status"],
        }, object())
    assert result["ok"] is True
    assert result["probe_possible"] is True
    assert result["identifier"] == {"column": "HeatNo", "value": "H123"}
    assert result["rows"][0]["Status"] == "Running"


def test_probe_table_requires_run_id_before_a_live_read() -> None:
    """Real-data batch finding: select/query/probe_table treated run_id as
    optional, so a real successful evidence read left no row in
    Hermes_L2_SQL_Action_Trn_Tbl, and a later reviewer's get_run_actions
    cross-check saw nothing and rejected the proposal (Ticket_242
    ACTION_AUTHORITY). run_id is not a database-style judgment call -- the
    task body hands it to the model once -- so it is required, not
    silently defaulted, before any live probe_table read happens."""
    class FakeOrchestrator:
        @staticmethod
        def build_query_mechanically(**kwargs):
            raise AssertionError("must not build a query before run_id is validated")

    allowlist = {"XStudio_Xbatch": {"dbo.Heat_Vw": ["HeatNo", "Status", "Reason", "EventTime"]}}
    with mock.patch.object(bridge, "_load_allowlist", return_value=allowlist), \
         mock.patch.object(bridge, "_orchestrator", return_value=FakeOrchestrator()):
        try:
            bridge._probe_table({
                "operation": "probe_table",
                "database": "XStudio_Xbatch",
                "table": "dbo.Heat_Vw",
                "ticket": {"HeatNo": "H123"},
            }, object())
        except ValueError as exc:
            assert "run_id is required" in str(exc)
        else:
            raise AssertionError("probe_table must not succeed without run_id")


def test_probe_table_refuses_broad_read_without_strong_identifier() -> None:
    class FakeOrchestrator:
        @staticmethod
        def build_query_mechanically(**kwargs):
            raise AssertionError("broad automatic query must not be built")

    allowlist = {"XStudio_Xbatch": {"dbo.Heat_Vw": ["HeatNo", "Status", "Reason"]}}
    with mock.patch.object(bridge, "_load_allowlist", return_value=allowlist), \
         mock.patch.object(bridge, "_orchestrator", return_value=FakeOrchestrator()):
        result = bridge._probe_table({
            "operation": "probe_table",
            "database": "XStudio_Xbatch",
            "table": "dbo.Heat_Vw",
            "ticket": {"Description": "something looks wrong"},
        }, object())
    assert result["ok"] is True
    assert result["probe_possible"] is False
    assert result["rows"] == []


def test_database_must_be_explicitly_allowlisted() -> None:
    try:
        bridge._database({"database": "master"})
    except ValueError as exc:
        assert "not allowed" in str(exc)
    else:
        raise AssertionError("master must not be an allowed database")


def test_tool_schema_describes_database_routing_and_operation_contracts() -> None:
    schema_str = json.dumps(plugin._SCHEMA)
    assert "oneOf" not in schema_str, "oneOf causes HTTP 400 with LM Studio; must remain flat"
    assert "anyOf" not in schema_str, "anyOf causes HTTP 400 with LM Studio; must remain flat"

    props = plugin._SCHEMA["parameters"]["properties"]
    assert "operation" in props
    op_desc = props["operation"]["description"]
    for op in (
        "select", "query", "probe_table", "suggest_tables", "find_objects",
        "get_definition", "validate_identifiers", "read_procedure",
        "get_ticket_context", "get_run_actions", "save_ledger"
    ):
        assert op in op_desc, f"operation {op} missing from schema description"

    db_desc = props["database"]["description"]
    assert "XStudio_Xbatch" in db_desc
    assert "XStudio_Helpdesk" in db_desc
    assert "XStudio_Configuration_Xbatch" in db_desc

    context = plugin._pre_llm_call()["context"]
    assert "DATABASE ROUTING" in context
    assert "XStudio_Xbatch" in context
    assert "XStudio_Helpdesk" in context


def test_operations_reject_missing_database_before_sql() -> None:
    fake_client = mock.MagicMock()
    db_ops = [
        ("select", {"table": "dbo.EAF_PER_HEAT", "columns": ["HeatNo"]}),
        ("query", {"sql": "SELECT 1"}),
        ("suggest_tables", {"search": "EAF"}),
        ("find_objects", {"search": "EAF"}),
        ("get_definition", {"object_name": "EAF_PER_HEAT"}),
        ("validate_identifiers", {"table": "dbo.EAF_PER_HEAT", "identifiers": ["HeatNo"]}),
        ("probe_table", {"table": "dbo.EAF_PER_HEAT", "ticket": {"HeatNo": "123"}}),
        ("read_procedure", {"run_id": "r1", "procedure": "XMES_Get_API_Transaction_Summary", "parameters": {"APIType": "UD"}}),
    ]
    for op, payload in db_ops:
        req = dict(payload, operation=op)
        handler = bridge._CONNECTED_OPERATIONS.get(op)
        if handler:
            try:
                handler(req, fake_client)
            except ValueError as exc:
                assert "database is required" in str(exc), f"op={op} did not mention database in error: {exc}"
            else:
                raise AssertionError(f"op={op} unexpectedly succeeded without database")
        elif op == "validate_identifiers":
            try:
                bridge._validate_identifiers(req)
            except ValueError as exc:
                assert "database is required" in str(exc)
            else:
                raise AssertionError(f"op={op} unexpectedly succeeded without database")
        elif op == "suggest_tables":
            try:
                bridge._database(req)
            except ValueError as exc:
                assert "database is required" in str(exc)
            else:
                raise AssertionError(f"op={op} unexpectedly succeeded without database")


def test_operations_reject_missing_required_arguments_before_sql() -> None:
    fake_client = mock.MagicMock()
    cases = [
        ("select", {"database": "XStudio_Xbatch"}, "table is required"),
        # columns are optional: the bridge resolves them against the live schema.
        ("select", {"database": "XStudio_Xbatch", "table": "dbo.T"}, "run_id is required"),
        ("select", {"database": "XStudio_Xbatch", "table": "dbo.T", "columns": ["ID"]}, "run_id is required"),
        ("query", {"database": "XStudio_Xbatch"}, "sql is required"),
        ("query", {"database": "XStudio_Xbatch", "sql": ""}, "sql is required"),
        ("query", {"database": "XStudio_Xbatch", "sql": "SELECT 1"}, "run_id is required"),
        ("suggest_tables", {"database": "XStudio_Xbatch"}, "search is required"),
        ("find_objects", {"database": "XStudio_Xbatch"}, "search is required"),
        ("get_definition", {"database": "XStudio_Xbatch"}, "object_name is required"),
        ("validate_identifiers", {"database": "XStudio_Xbatch"}, "table is required"),
        ("validate_identifiers", {"database": "XStudio_Xbatch", "table": "dbo.T"}, "identifiers is required"),
        ("validate_identifiers", {"database": "XStudio_Xbatch", "table": "dbo.T", "identifiers": []}, "identifiers is required"),
        ("read_procedure", {"database": "XStudio_Xbatch"}, "run_id is required"),
        ("read_procedure", {"database": "XStudio_Xbatch", "run_id": "r1"}, "procedure is required"),
        ("read_procedure", {"database": "XStudio_Xbatch", "run_id": "r1", "procedure": "P"}, "parameters is required"),
        ("get_ticket_context", {}, "ticket_id is required"),
        ("get_run_actions", {}, "run_id is required"),
        ("save_ledger", {}, "run_id is required"),
        ("save_ledger", {"run_id": "r1"}, "ledger is required"),
        ("probe_table", {"database": "XStudio_Xbatch"}, "table is required"),
        ("probe_table", {"database": "XStudio_Xbatch", "table": "dbo.T"}, "ticket_id is required"),
    ]
    for op, payload, err in cases:
        req = dict(payload, operation=op)
        handler = bridge._CONNECTED_OPERATIONS.get(op)
        try:
            if handler:
                handler(req, fake_client)
            elif op == "validate_identifiers":
                bridge._validate_identifiers(req)
            elif op == "suggest_tables":
                bridge._require(req, "search")
            else:
                raise ValueError(f"unknown op: {op}")
        except ValueError as exc:
            assert err in str(exc), f"op={op} expected {err!r} in {exc!r}"
        else:
            raise AssertionError(f"op={op} unexpectedly succeeded with payload {payload}")


def test_dispatch_requires_operation() -> None:
    try:
        bridge.dispatch({})
    except ValueError as exc:
        assert "operation is required" in str(exc)
    else:
        raise AssertionError("dispatch without operation must fail")


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


def _seed_valid_tables(session: str, tables_line: str) -> None:
    plugin._post_tool_call(
        "kanban_show", {},
        json.dumps({"task": {"body": f"run_id: R\nticket_id: T\n{tables_line}\n"}}),
        task_id=session,
    )


def test_select_against_a_non_evidence_plan_table_is_blocked_before_sql() -> None:
    session = "stall-guard-1"
    _seed_valid_tables(
        session, "Current valid_tables: XStudio_Xbatch.dbo.EAF_SMS_Data, XStudio_Xbatch.dbo.Power_Consumption_LogSheet"
    )
    blocked = plugin._pre_tool_call(
        "xstudio_select",
        {"database": "XStudio_Xbatch", "table": "dbo.SomeGuessedTable", "columns": ["ID"]},
        task_id=session,
    )
    assert blocked and blocked["action"] == "block"
    assert "not one of the tables Jev's evidence plan selected" in blocked["message"]
    assert "did not consume the investigation budget" in blocked["message"]


def test_select_against_an_evidence_plan_table_is_allowed_bare_or_qualified() -> None:
    session = "stall-guard-2"
    _seed_valid_tables(session, "Current valid_tables: XStudio_Xbatch.dbo.EAF_SMS_Data")
    for table in ("dbo.EAF_SMS_Data", "EAF_SMS_Data", "XStudio_Xbatch.dbo.EAF_SMS_Data"):
        result = plugin._pre_tool_call(
            "xstudio_select",
            {"database": "XStudio_Xbatch", "table": table, "columns": ["ID"]},
            task_id=session,
        )
        assert result is None or result["action"] != "block", f"{table} should have been allowed"


def test_no_valid_tables_line_means_no_restriction_applied() -> None:
    session = "stall-guard-3"
    plugin._post_tool_call(
        "kanban_show", {}, json.dumps({"task": {"body": "run_id: R\nticket_id: T\n"}}), task_id=session,
    )
    result = plugin._pre_tool_call(
        "xstudio_select",
        {"database": "XStudio_Xbatch", "table": "dbo.AnyTableAtAll", "columns": ["ID"]},
        task_id=session,
    )
    assert result is None or result["action"] != "block"


def test_select_with_an_unprobed_column_is_left_to_the_bridge() -> None:
    """Jev's plan limits tables; columns are resolved (never guessed) by the bridge,
    so a real-but-unprobed or mistyped column no longer costs the worker a call."""
    session = "stall-guard-5"
    _seed_valid_tables(
        session, "Current valid_tables: XStudio_Xbatch.dbo.EAF_SMS_Data[EAFHeatID,EAFEnergyMWH,ActivePower]"
    )
    result = plugin._pre_tool_call(
        "xstudio_select",
        {"database": "XStudio_Xbatch", "table": "dbo.EAF_SMS_Data", "columns": ["EAFHeatID", "SomeGuessedColumn"]},
        task_id=session,
    )
    assert not (result and result.get("action") == "block")


def test_select_requesting_only_probed_columns_is_allowed() -> None:
    session = "stall-guard-6"
    _seed_valid_tables(
        session, "Current valid_tables: XStudio_Xbatch.dbo.EAF_SMS_Data[EAFHeatID,EAFEnergyMWH,ActivePower]"
    )
    result = plugin._pre_tool_call(
        "xstudio_select",
        {"database": "XStudio_Xbatch", "table": "dbo.EAF_SMS_Data", "columns": ["EAFHeatID", "ActivePower"]},
        task_id=session,
    )
    assert result is None or result["action"] != "block"


def test_table_with_no_recorded_columns_does_not_restrict_columns() -> None:
    # Backward compatible: a valid_tables entry with no bracketed column list
    # (e.g. a relationship hop whose probe found no rows) must not block on
    # columns -- only the table-level check applies.
    session = "stall-guard-7"
    _seed_valid_tables(session, "Current valid_tables: XStudio_Xbatch.dbo.EAF_SMS_Data")
    result = plugin._pre_tool_call(
        "xstudio_select",
        {"database": "XStudio_Xbatch", "table": "dbo.EAF_SMS_Data", "columns": ["AnyColumnAtAll"]},
        task_id=session,
    )
    assert result is None or result["action"] != "block"


def test_blocked_select_call_does_not_consume_investigation_budget() -> None:
    session = "stall-guard-4"
    _seed_valid_tables(session, "Current valid_tables: XStudio_Xbatch.dbo.EAF_SMS_Data")
    old = plugin.MAX_TOOL_CALLS
    plugin.MAX_TOOL_CALLS = 1
    try:
        for _ in range(3):
            blocked = plugin._pre_tool_call(
                "xstudio_select",
                {"database": "XStudio_Xbatch", "table": "dbo.Wrong", "columns": ["ID"]},
                task_id=session,
            )
            assert blocked["action"] == "block"
        # Budget was never touched by the rejected calls -- a real one still fits.
        real = plugin._pre_tool_call(
            "xstudio_select",
            {"database": "XStudio_Xbatch", "table": "dbo.EAF_SMS_Data", "columns": ["ID"]},
            task_id=session,
        )
        assert real is None or real["action"] != "block"
    finally:
        plugin.MAX_TOOL_CALLS = old


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
    assert "xstudio_submit_proposal" in body and "NEXT ACTIONS" in body
    assert "l2_recall" in body
    assert "RUN-1" in body and "TICKET-1" in body
    assert "A ticket/user identifier is not proof of database storage representation" in body
    assert "Evidence status: INCOMPLETE" not in body  # banner leaked into requester replies
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


def test_config_patch_adds_all_profile_hook_plugins_on_fresh_config() -> None:
    fresh = _SAMPLE_CONFIG.replace(
        "    - xstudio-l2-trace\n    - xstudio-l2-orchestrator\n",
        "",
    )
    patched = _patch_sample(fresh)
    assert "    - xstudio-l2-orchestrator\n" in patched
    assert "    - xstudio-l2-tools\n" in patched
    assert "    - xstudio-l2-trace\n" in patched


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
    assert "[terminal, todo, xstudio_l2, l2_learning]" in patched


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


_NEXT_STEP = {"next_investigation_step": "Read SAP posting rows for Inspection Lot 49900000002."}
_OUTCOME = {"resolution": "Confirmed no UsageDecision transaction exists; requester informed."}


def test_submit_proposal_rejects_resolution_without_verified_outcome() -> None:
    """9 of 10 live RESOLUTIONs closed tickets with an empty Resolution field."""
    _setup_investigator_context(task_id="submit-no-outcome")
    result = json.loads(plugin._submit_proposal_handler(
        {"response_type": "RESOLUTION", "summary": _SUBSTANTIVE_SUMMARY,
         "claim_status": "VERIFIED", "action_id": "A-1"}, task_id="submit-no-outcome"))
    assert result["ok"] is False and "resolution" in result["error"]


def test_submit_proposal_rejects_incomplete_update_without_next_step() -> None:
    _setup_investigator_context(task_id="submit-no-step")
    result = json.loads(plugin._submit_proposal_handler(
        {"response_type": "UPDATE", "summary": _SUBSTANTIVE_SUMMARY}, task_id="submit-no-step"))
    assert result["ok"] is False and "next_investigation_step" in result["error"]


def test_submit_proposal_assembles_complete_metadata_from_flat_args() -> None:
    _setup_investigator_context()
    with mock.patch.object(plugin.subprocess, "run") as mock_run:
        mock_run.return_value = mock.Mock(returncode=0, stdout="", stderr="")
        result = plugin._submit_proposal_handler(
            {"response_type": "UPDATE", "summary": _SUBSTANTIVE_SUMMARY, **_NEXT_STEP},
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
        {"response_type": "RESOLUTION", "summary": _SUBSTANTIVE_SUMMARY, **_OUTCOME,
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
            {"response_type": "RESOLUTION", "summary": _SUBSTANTIVE_SUMMARY, **_OUTCOME,
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
            {"response_type": "UPDATE", "summary": _SUBSTANTIVE_SUMMARY, **_NEXT_STEP},
            task_id="submit-reply",
        )
    metadata = json.loads(mock_run.call_args[0][0][mock_run.call_args[0][0].index("--metadata") + 1])
    assert metadata["reply_text"] == _SUBSTANTIVE_SUMMARY
    assert metadata["evidence_status"] == "INCOMPLETE"


def test_submit_proposal_uses_explicit_reply_text_when_provided() -> None:
    _setup_investigator_context(task_id="submit-reply-explicit")
    with mock.patch.object(plugin.subprocess, "run") as mock_run:
        mock_run.return_value = mock.Mock(returncode=0, stdout="", stderr="")
        plugin._submit_proposal_handler(
            {"response_type": "UPDATE", "summary": _SUBSTANTIVE_SUMMARY, **_NEXT_STEP,
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
            {"response_type": "UPDATE", "summary": _SUBSTANTIVE_SUMMARY, **_NEXT_STEP},
            task_id="submit-ctx",
        )
    metadata = json.loads(mock_run.call_args[0][0][mock_run.call_args[0][0].index("--metadata") + 1])
    assert metadata["run_id"] == "CTX-RUN"
    assert metadata["ticket_id"] == "CTX-TICKET"


def test_submit_proposal_uses_kanban_task_id_learned_from_show() -> None:
    session_id = "worker-session"
    plugin._post_tool_call(
        "kanban_show",
        result={"task": {
            "id": "t_real_kanban_task",
            "body": "run_id: RUN-K\nticket_id: TICKET-K\npipeline_stage: investigation",
        }},
        task_id=session_id,
        session_id=session_id,
    )
    with mock.patch.object(plugin.subprocess, "run") as mock_run:
        mock_run.return_value = mock.Mock(returncode=0, stdout="", stderr="")
        result = json.loads(plugin._submit_proposal_handler(
            {"response_type": "UPDATE", "summary": _SUBSTANTIVE_SUMMARY, **_NEXT_STEP},
            task_id=session_id,
            session_id=session_id,
        ))
    assert result["ok"] is True
    assert mock_run.call_args[0][0][3] == "t_real_kanban_task"


def test_submit_proposal_targets_own_worker_task_not_inspected_prior_card() -> None:
    """Live 2026-09-22: a rework worker ran kanban_show on the prior attempt's card,
    the handler then completed that card and Hermes refused the mutation."""
    session_id = "rework-session"
    show = lambda tid, run: plugin._post_tool_call(
        "kanban_show",
        result={"task": {"id": tid, "body": f"run_id: {run}\nticket_id: TICKET-R\npipeline_stage: rework"}},
        task_id=session_id, session_id=session_id,
    )
    with mock.patch.dict(plugin.os.environ, {"HERMES_KANBAN_TASK": "t_own_rework"}):
        show("t_own_rework", "RUN-OWN")
        show("t_prior_attempt", "RUN-PRIOR")
        with mock.patch.object(plugin.subprocess, "run") as mock_run:
            mock_run.return_value = mock.Mock(returncode=0, stdout="", stderr="")
            result = json.loads(plugin._submit_proposal_handler(
                {"response_type": "UPDATE", "summary": _SUBSTANTIVE_SUMMARY, **_NEXT_STEP},
                task_id=session_id, session_id=session_id,
            ))
    assert result["ok"] is True
    cmd = mock_run.call_args[0][0]
    assert cmd[3] == "t_own_rework"
    assert json.loads(cmd[cmd.index("--metadata") + 1])["run_id"] == "RUN-OWN"


def test_submit_proposal_runs_hermes_from_a_stable_cwd() -> None:
    """Live 2026-09-22: an inherited deleted cwd made `hermes` die with getcwd()."""
    _setup_investigator_context(task_id="submit-cwd")
    with mock.patch.object(plugin.subprocess, "run") as mock_run:
        mock_run.return_value = mock.Mock(returncode=0, stdout="", stderr="")
        plugin._submit_proposal_handler(
            {"response_type": "UPDATE", "summary": _SUBSTANTIVE_SUMMARY, **_NEXT_STEP}, task_id="submit-cwd",
        )
    assert mock_run.call_args.kwargs["cwd"] == str(plugin.Path.home())


def test_leaked_qwen_parameter_markup_is_cut_and_swallowed_args_recovered() -> None:
    """Live rows 869E3F60/57D485A8: later arguments leaked inside summary."""
    leaked = {"summary": "Verified the reading.</parameter>\n<parameter=response_type>\nRESOLUTION\n"
                         "</parameter>\n<parameter=claim_status>\nVERIFIED\n</parameter>"}
    repaired = plugin._recover_leaked_parameters(leaked)
    assert repaired == {"summary": "Verified the reading.", "response_type": "RESOLUTION", "claim_status": "VERIFIED"}
    # An argument the model set explicitly is never overridden by leaked text.
    kept = plugin._recover_leaked_parameters({"summary": "x</result>\n<parameter=response_type>RESOLUTION", "response_type": "UPDATE"})
    assert kept["response_type"] == "UPDATE" and kept["summary"] == "x"
    assert plugin._recover_leaked_parameters({"summary": "a<b and <resultset>"}) == {"summary": "a<b and <resultset>"}


def test_kanban_complete_strips_leaked_markup_before_it_reaches_reply_text() -> None:
    """Live row F2DB9885 published '</result>\n<parameter=summary>' to the customer."""
    summary = "RESOLUTION: LRF arc time verified for Heat 1604013\n</result>\n<parameter=summary>\nVerified records"
    decision = plugin._pre_tool_call("kanban_complete", {"summary": summary}, task_id="leak-review")
    assert decision["action"] == "modify"
    assert "<" not in decision["args"]["summary"]


def test_submit_proposal_does_not_consume_xstudio_tool_budget() -> None:
    _setup_investigator_context(task_id="submit-budget")
    # Fill up the budget to MAX_TOOL_CALLS - 1
    with plugin._lock:
        plugin._session_calls["submit-budget"] = plugin.MAX_TOOL_CALLS - 1
    # The pre_tool_call should not block xstudio_submit_proposal
    result = plugin._pre_tool_call(
        "xstudio_submit_proposal",
        {"response_type": "UPDATE", "summary": _SUBSTANTIVE_SUMMARY, **_NEXT_STEP},
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
            {"response_type": "UPDATE", "summary": _SUBSTANTIVE_SUMMARY, **_NEXT_STEP,
             "claim_status": "INFERRED"},
            task_id="submit-evidence",
        ))
    assert result["evidence_status"] == "INCOMPLETE"


def test_submit_proposal_includes_optional_fields_in_metadata() -> None:
    _setup_investigator_context(task_id="submit-optional")
    with mock.patch.object(plugin.subprocess, "run") as mock_run:
        mock_run.return_value = mock.Mock(returncode=0, stdout="", stderr="")
        plugin._submit_proposal_handler(
            {"response_type": "UPDATE", "summary": _SUBSTANTIVE_SUMMARY, **_NEXT_STEP,
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
        {"response_type": "UPDATE", "summary": _SUBSTANTIVE_SUMMARY, **_NEXT_STEP},
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
    assert "xstudio_submit_proposal" in result["message"]


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
    args = {"summary": summary, "result": "Investigation complete", "metadata": {}}
    first = plugin._pre_tool_call("kanban_complete", args, task_id="investigator-summary-package")
    # First empty completion is redirected to the flat submit tool, not silently packaged.
    assert first and first["action"] == "block" and "xstudio_submit_proposal" in first["message"]
    result = plugin._pre_tool_call("kanban_complete", args, task_id="investigator-summary-package")
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


def test_submit_proposal_cannot_mark_unverified_claim_complete() -> None:
    _setup_investigator_context(task_id="submit-unverified-complete")
    with mock.patch.object(plugin.subprocess, "run") as mock_run:
        mock_run.return_value = mock.Mock(returncode=0, stdout="", stderr="")
        plugin._submit_proposal_handler(
            {"response_type": "UPDATE", "summary": _SUBSTANTIVE_SUMMARY, **_NEXT_STEP,
             "claim_status": "UNVERIFIED", "evidence_status": "COMPLETE"},
            task_id="submit-unverified-complete",
        )
    command = mock_run.call_args[0][0]
    metadata = json.loads(command[command.index("--metadata") + 1])
    assert metadata["evidence_status"] == "INCOMPLETE"
    assert not metadata["reply_text"].startswith("Evidence status")


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
    # No investigator contract is demanded; the harness records the review itself.
    assert result and result["action"] == "modify"
    metadata = result["args"]["metadata"]
    assert metadata["review_decision"] == "APPROVED"
    assert metadata["run_id"] == "RUN-1" and metadata["ticket_id"] == "TICKET-1"
    assert metadata["review_notes"] == "Approved after independent live verification."


def test_l2_worker_cannot_author_unrunnable_scripts() -> None:
    """Live: 321 write_file calls writing parse_proposal.py that could never execute."""
    plugin._pre_llm_call(task_id="script-guard",
                         user_message="run_id: RUN-S\nticket_id: TICKET-S\npipeline_stage: review")
    blocked = plugin._pre_tool_call("write_file", {"path": "/tmp/parse_proposal.py", "content": "x"},
                                    task_id="script-guard")
    assert blocked and blocked["action"] == "block" and "PROPOSAL DIGEST" in blocked["message"]
    notes = plugin._pre_tool_call("write_file", {"path": "/tmp/notes.md", "content": "x"}, task_id="script-guard")
    assert notes is None


def test_kanban_complete_after_successful_submit_says_stop_not_resubmit() -> None:
    """Live 13:07: the guard told a worker to resubmit an already-closed card."""
    _setup_investigator_context(task_id="submitted-then-complete")
    with mock.patch.dict(plugin.os.environ, {"HERMES_KANBAN_TASK": "t_done_card"}),             mock.patch.object(plugin.subprocess, "run") as run:
        run.return_value = mock.Mock(returncode=0, stdout="", stderr="")
        plugin._submit_proposal_handler({"response_type": "UPDATE", "summary": _SUBSTANTIVE_SUMMARY, **_NEXT_STEP},
                                        task_id="submitted-then-complete")
        blocked = plugin._pre_tool_call("kanban_complete", {"summary": "done"}, task_id="submitted-then-complete")
    assert blocked["action"] == "block" and "Already done" in blocked["message"]
    assert "xstudio_submit_proposal now" not in blocked["message"]


def test_empty_reviewer_approval_still_gets_summary_and_record() -> None:
    """Live 13:15: kanban_complete({}) from a reviewer failed in Hermes for lack of a summary."""
    plugin._pre_llm_call(task_id="empty-review",
                         user_message="run_id: RUN-E\nticket_id: TICKET-E\npipeline_stage: review")
    result = plugin._pre_tool_call("kanban_complete", {}, task_id="empty-review")
    assert result["action"] == "modify"
    assert result["args"]["summary"]
    assert result["args"]["metadata"]["review_decision"] == "APPROVED"


def test_reviewer_rejection_summary_is_recorded_as_rejected() -> None:
    """Mirrors l2_pipeline_runtime.is_reviewer_rejection so the record never contradicts it."""
    plugin._pre_llm_call(task_id="reviewer-reject",
                         user_message="run_id: RUN-9\nticket_id: TICKET-9\npipeline_stage: review\nreview_cycle: 1")
    result = plugin._pre_tool_call("kanban_complete", {"summary": "Rejected: claim C1 cites no action."},
                                   task_id="reviewer-reject")
    assert result["args"]["metadata"]["review_decision"] == "REJECTED"
    assert result["args"]["metadata"]["review_cycle"] == "1"


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


def test_requester_question_produces_question_with_customer_text() -> None:
    _setup_investigator_context(task_id="submit-question")
    question = "Please provide the affected heat number and the value you entered."
    with mock.patch.object(plugin.subprocess, "run") as run:
        run.return_value = mock.Mock(returncode=0, stdout="", stderr="")
        result = json.loads(plugin._submit_proposal_handler(
            {"response_type": "UPDATE", "summary": _SUBSTANTIVE_SUMMARY, **_NEXT_STEP,
             "requester_question": question}, task_id="submit-question"))
    assert result["response_type"] == "QUESTION"
    command = run.call_args[0][0]
    metadata = json.loads(command[command.index("--metadata") + 1])
    assert metadata["reply_text"] == question
    assert metadata["investigator_notes"] == _SUBSTANTIVE_SUMMARY


def test_question_without_explicit_customer_question_is_rejected() -> None:
    _setup_investigator_context(task_id="submit-empty-question")
    with mock.patch.object(plugin.subprocess, "run") as run:
        result = json.loads(plugin._submit_proposal_handler(
            {"response_type": "QUESTION", "summary": _SUBSTANTIVE_SUMMARY},
            task_id="submit-empty-question"))
    assert result["ok"] is False
    assert "requester_question" in result["error"]
    run.assert_not_called()


def test_reviewer_cannot_submit_replacement_proposal() -> None:
    result = plugin._pre_llm_call(task_id="review-role", user_message=(
        "run_id: RUN-1\nticket_id: TICKET-1\npipeline_stage: review"))
    assert "kanban_block" in result["context"]
    assert "When completing the investigation" not in result["context"]
    with mock.patch.object(plugin.subprocess, "run") as run:
        response = json.loads(plugin._submit_proposal_handler(
            {"response_type": "UPDATE", "summary": _SUBSTANTIVE_SUMMARY, **_NEXT_STEP}, task_id="review-role"))
    assert response["ok"] is False
    run.assert_not_called()


def test_worker_config_gives_each_role_one_completion_path_and_only_xstudio_skills() -> None:
    budget = _load("patch_l2_worker_budget_test", ROOT / "patch_l2_worker_budget.py")
    base = ("model:\n  context_length: 1\nagent:\n  max_turns: 1\n"
            "platform_toolsets:\n  cli:\n    - terminal\n")
    investigator = budget.configure(base, disabled_skills=["codex"])
    reviewer = budget.configure(base, reviewer=True, disabled_skills=["codex"])
    assert "    - l2_submit" in investigator.split("known_plugin_toolsets")[0]
    assert "    - l2_submit" not in reviewer.split("known_plugin_toolsets")[0]
    # Known-but-unlisted keeps the plugin toolset off (hermes tools_config).
    assert "known_plugin_toolsets:\n  cli:\n    - l2_submit" in reviewer
    assert "skills:\n  disabled:\n    - codex" in investigator
    assert budget.configure(investigator, disabled_skills=["codex"]) == investigator


def test_read_table_probe_filters_on_the_ticket_identifier_without_prose_punctuation() -> None:
    # Ticket_338: "Please verify LRF_Per_Heat for HeatID 1604007." probed '1604007.' -> 0 rows.
    ticket = {"Description": "Please verify LRF_Per_Heat for HeatID 1604007."}
    assert bridge._probe_filter(ticket, ["ID", "HeatID", "ArcingTime"]) == ("HeatID", "1604007")


def test_read_table_probe_picks_the_columns_the_ticket_names_not_sync_plumbing() -> None:
    lrf = ["ID", "Name", "DbSyncStatus", "MobileSyncStatus", "StartTime", "Status", "PowerONTime",
           "PowerOFFTime", "ArcingTime", "HeatID", "ArgonConsumption"]
    cols = bridge._probe_columns("HeatID", lrf, [], "Operator logged ArcingTime; confirm PowerONTime and PowerOFFTime")
    assert cols[:4] == ["HeatID", "PowerONTime", "PowerOFFTime", "ArcingTime"]
    assert not {"Name", "DbSyncStatus", "MobileSyncStatus", "ID"} & set(cols)
    chem = ["HeatNo", "C", "Si", "Mn", "SampleType", "Grade", "DbSyncStatus"]
    cols = bridge._probe_columns("HeatNo", chem, [], "chemistry shows Carbon=0.07 and Silicon=0.003")
    assert {"C", "Si", "SampleType", "Grade"} <= set(cols) and "Mn" not in cols


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

