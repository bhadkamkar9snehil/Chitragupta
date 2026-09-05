#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

PY_FILES=(
  Model_Bench/l2_pipeline_runtime.py
  Model_Bench/ticket_scout.py
  Model_Bench/reconcile_l2_pipeline.py
  Model_Bench/kanban_approval_publisher.py
  Model_Bench/kanban_reject_bridge.py
  Model_Bench/repair_incomplete_completions.py
  Model_Bench/audit_kanban_completions.py
  Model_Bench/enforce_publish_safety_net.py
  Model_Bench/configure_helpdesk_workflow.py
  Model_Bench/patch_profile_config.py
  Model_Bench/xstudio_l2_orchestrator_plugin/__init__.py
  Model_Bench/xstudio_l2_tools_plugin/__init__.py
  Model_Bench/xstudio_l2_tool_bridge.py
  Model_Bench/test_xstudio_l2_tools_plugin.py
)

echo "== Python syntax =="
python3 -m py_compile "${PY_FILES[@]}"

echo "== Deterministic contract tests =="
python3 Model_Bench/test_l2_pipeline_runtime.py

echo "== Typed investigation-tool contract tests =="
python3 Model_Bench/test_xstudio_l2_tools_plugin.py

echo "== Knowledge/skill validation =="
python3 Model_Bench/validate_knowledge_manifest.py
python3 Model_Bench/test_kb_retrieval.py

echo "== Live workflow discovery (read-only) =="
python3 Model_Bench/configure_helpdesk_workflow.py

echo "== Pipeline status (read-only) =="
python3 Model_Bench/l2_pipeline_runtime.py status

echo "== Reconcile preview (read-only / no lifecycle mutations) =="
python3 Model_Bench/l2_pipeline_runtime.py reconcile --dry-run

echo
cat <<'EOF'
LOCAL VALIDATION COMPLETE.

Before enabling normal scout flow, separately apply in XStudio_Helpdesk:
  Knowledge/25_ticket_dispatch_hardening.sql
  Knowledge/55_update_retry_hardening.sql
  Knowledge/98_pipeline_postflight.sql

Then populate deploy/helpdesk_workflow_binding.json with the exact live resolved status
observed above. Do not guess a status value.

For the next naturally-arriving fresh ticket, verify in its trace that the worker used
the typed xstudio_l2 tool and that NO terminal call invoked Hermes_Orchestrator.py,
Python314/python.exe, sqlcmd, pyodbc, pip, or package installation -- that is the
Ticket_424/Ticket_441 regression signature this harness exists to prevent.
EOF
