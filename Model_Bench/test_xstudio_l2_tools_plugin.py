#!/usr/bin/env python3
"""Focused contracts for Chitragupta's Hermes XStudio plugin and Windows bridge."""
from __future__ import annotations

import importlib.util
import json
import sys
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


def test_identity_binds_current_run() -> None:
    with mock.patch.object(plugin, "_task_context", return_value={"run_id": "RUN-1", "ticket_id": "TICKET-1"}):
        bound = plugin._bind_identity(
            {"operation": "select", "database": "XStudio_Xbatch", "table": "dbo.X", "columns": ["ID"]},
            "t_abcdef",
        )
    assert bound["run_id"] == "RUN-1"


def test_identity_rejects_cross_run_request() -> None:
    with mock.patch.object(plugin, "_task_context", return_value={"run_id": "RUN-1", "ticket_id": "TICKET-1"}):
        try:
            plugin._bind_identity({"operation": "get_run_actions", "run_id": "RUN-OTHER"}, "t_abcdef")
        except ValueError:
            pass
        else:
            raise AssertionError("cross-run request must be rejected")


def test_identity_binds_current_ticket() -> None:
    with mock.patch.object(plugin, "_task_context", return_value={"run_id": "RUN-1", "ticket_id": "TICKET-1"}):
        bound = plugin._bind_identity({"operation": "get_ticket_context"}, "t_abcdef")
    assert bound["ticket_id"] == "TICKET-1"


def test_non_identity_operation_is_unchanged() -> None:
    request = {"operation": "suggest_tables", "database": "XStudio_Xbatch", "search": "SAP posting"}
    assert plugin._bind_identity(request, "") == request


def test_bridge_transport_is_harness_owned() -> None:
    completed = mock.Mock(returncode=0, stdout='{"ok":true}', stderr="")
    with mock.patch.object(plugin.subprocess, "run", return_value=completed) as run:
        result = json.loads(plugin._invoke_bridge({"operation": "query"}))
    assert result["ok"] is True
    assert run.call_args.args[0] == [plugin.WINDOWS_PYTHON, plugin.BRIDGE_WIN]


def test_plugin_registers_only_xstudio_domain_tool() -> None:
    class Ctx:
        def __init__(self):
            self.tools = []
        def register_tool(self, **kwargs):
            self.tools.append((kwargs["name"], kwargs["toolset"]))
    ctx = Ctx()
    plugin.register(ctx)
    assert ctx.tools == [("xstudio_l2", "xstudio_l2")]


def test_read_only_sql_guard() -> None:
    assert bridge.is_read_only_sql("SELECT TOP 10 * FROM dbo.X")
    assert not bridge.is_read_only_sql("UPDATE dbo.X SET A=1")
    assert not bridge.is_read_only_sql("SELECT 1; DROP TABLE dbo.X")
    assert bridge.is_read_only_sql("SELECT 'no update available' AS Note")


def test_procedure_allowlist_rejects_arbitrary_exec() -> None:
    result = bridge._read_procedure({
        "operation": "read_procedure",
        "database": "XStudio_Xbatch",
        "run_id": "RUN-1",
        "procedure": "Dangerous_Write_Usp",
        "parameters": {},
    }, object())
    assert result["ok"] is False
    assert "XMES_Get_API_Transaction_Summary" in result["allowed_procedures"]


def test_result_bounding_caps_rows() -> None:
    bounded = bridge._bounded_response({
        "ok": True, "operation": "query", "rows": [{"i": i} for i in range(500)]
    })
    assert len(bounded["rows"]) == bridge.MAX_LIST_ITEMS + 1


def test_fresh_cards_teach_typed_tool_not_raw_transport() -> None:
    runtime = _load("l2_pipeline_runtime_test", ROOT / "l2_pipeline_runtime.py")
    body = runtime._query_instructions("RUN-1", "TICKET-1")
    assert "xstudio_l2" in body
    for retired in ("/mnt/c/Python314/python.exe", "Hermes_Orchestrator.py", "sqlcmd", "pip install"):
        assert retired not in body


def main() -> int:
    tests = [value for name, value in sorted(globals().items())
             if name.startswith("test_") and callable(value)]
    failures = []
    for test in tests:
        try:
            test()
            print(f"PASS {test.__name__}")
        except Exception as exc:
            failures.append((test.__name__, exc))
            print(f"FAIL {test.__name__}: {type(exc).__name__}: {exc}")
    if failures:
        print(f"\n{len(failures)} of {len(tests)} tool-boundary tests FAILED.")
        return 1
    print(f"\n{len(tests)} tool-boundary tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
