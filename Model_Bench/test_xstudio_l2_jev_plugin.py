#!/usr/bin/env python3
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


plugin = _load("xstudio_l2_jev_plugin_test", ROOT / "xstudio_l2_jev_plugin" / "__init__.py")


def setup_function() -> None:
    with plugin._lock:
        plugin._session_calls.clear()


def test_schema_exposes_only_reviewed_workflows() -> None:
    workflow = plugin._SCHEMA["parameters"]["properties"]["workflow"]
    allowed = set(workflow["enum"])
    assert "primary_review" in allowed
    assert "evidence_plan" in allowed
    assert "investigation_assessment" in allowed
    assert "ticket_triage" in allowed
    assert "ask_anything" not in allowed
    assert "custom_question" not in allowed


def test_plugin_calls_only_the_fixed_jev_bridge() -> None:
    completed = mock.Mock(
        returncode=0,
        stdout=json.dumps({"ok": True, "workflow": "primary_review", "result": {"ok": True}}),
        stderr="",
    )
    with mock.patch.object(plugin.subprocess, "run", return_value=completed) as run:
        result = json.loads(plugin._invoke({"workflow": "primary_review", "state": {"x": 1}}))
    assert result["ok"] is True
    argv = run.call_args.args[0]
    assert argv == [plugin.WINDOWS_PYTHON, plugin.BRIDGE_WIN]
    sent = json.loads(run.call_args.kwargs["input"])
    assert sent["workflow"] == "primary_review"


def test_jev_call_budget_is_bounded_per_session() -> None:
    old = plugin.MAX_CALLS
    plugin.MAX_CALLS = 2
    try:
        assert plugin._pre_tool_call(plugin.TOOL_NAME, {"workflow": "ticket_triage"}, task_id="a") is None
        assert plugin._pre_tool_call(plugin.TOOL_NAME, {"workflow": "evidence_plan"}, task_id="a") is None
        blocked = plugin._pre_tool_call(plugin.TOOL_NAME, {"workflow": "primary_review"}, task_id="a")
        assert blocked and blocked["action"] == "block"
        assert plugin._pre_tool_call(plugin.TOOL_NAME, {"workflow": "ticket_triage"}, task_id="b") is None
    finally:
        plugin.MAX_CALLS = old


def test_pre_llm_contract_tells_model_not_to_reimplement_jev() -> None:
    context = plugin._pre_llm_call()["context"]
    assert "xstudio_jev" in context
    assert "do not reproduce" in context.lower()
    assert "deterministic lifecycle" in context.lower()


def test_cleanup_releases_budget() -> None:
    plugin._pre_tool_call(plugin.TOOL_NAME, {"workflow": "ticket_triage"}, task_id="x")
    plugin._cleanup(task_id="x")
    with plugin._lock:
        assert "x" not in plugin._session_calls


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
        print(f"\n{len(failures)} of {len(tests)} Jev plugin contract tests FAILED.")
        return 1
    print(f"\n{len(tests)} Jev plugin contract tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
