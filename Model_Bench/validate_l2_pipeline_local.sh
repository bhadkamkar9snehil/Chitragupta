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
  Model_Bench/patch_tool_search_off.py
  Model_Bench/xstudio_l2_orchestrator_plugin/__init__.py
  Model_Bench/xstudio_l2_tools_plugin/__init__.py
  Model_Bench/xstudio_l2_tool_bridge.py
  Model_Bench/test_xstudio_l2_tools_plugin.py
)

echo "== Python syntax =="
python3 -m py_compile "${PY_FILES[@]}"

echo "== Deterministic lifecycle contract tests =="
python3 Model_Bench/test_l2_pipeline_runtime.py

echo "== Typed investigation-tool contract tests =="
python3 Model_Bench/test_xstudio_l2_tools_plugin.py

echo "== Knowledge/skill validation =="
python3 Model_Bench/validate_knowledge_manifest.py
python3 Model_Bench/test_kb_retrieval.py

echo "== Retired live-deployment guard =="
DEPLOYED_SCRIPTS="$HOME/.hermes/profiles/l2-investigator/scripts"
retired_found=0
for retired in dispatch_l2_review.py kanban_forward_bridge.py nudge_unpublished_runs.py; do
  if [[ -e "$DEPLOYED_SCRIPTS/$retired" ]]; then
    echo "FAIL: retired script is still deployed live: $DEPLOYED_SCRIPTS/$retired" >&2
    retired_found=1
  fi
done
if [[ "$retired_found" -ne 0 ]]; then
  echo "Run: bash Model_Bench/deploy_l2_pipeline_runtime.sh" >&2
  exit 1
fi
echo "PASS: no known retired lifecycle scripts remain in the live scripts directory"

echo "== Live workflow discovery (read-only) =="
python3 Model_Bench/configure_helpdesk_workflow.py

echo "== Pipeline status (read-only) =="
python3 Model_Bench/l2_pipeline_runtime.py status

echo "== Reconcile preview (dry-run) =="
python3 Model_Bench/l2_pipeline_runtime.py reconcile --dry-run

echo
cat <<'EOF'
LOCAL VALIDATION COMPLETE.

SQL deployment note:
  Knowledge/00_Hermes_L2_FULL_INSTALL.sql is the generated complete bundle.
  It already includes the current 25_ticket_dispatch_hardening and
  55_update_retry_hardening sources. Do not re-apply those merely because
  the numbered source files exist.

After deploying/regenerating the SQL bundle, run:
  Knowledge/98_pipeline_postflight.sql

Confirm deploy/helpdesk_workflow_binding.json still matches live workflow values.
Do not guess replacement status names.

Live deployment note:
  deploy_l2_pipeline_runtime.sh now removes known retired lifecycle scripts from
  ~/.hermes/profiles/l2-investigator/scripts. Validation fails if those stale
  copies reappear even when they are absent from Git.

For the next naturally arriving fresh ticket, verify its trace uses xstudio_l2 for
database/schema/ticket evidence and does not attempt to recreate SQL transport via
terminal, an interpreter, pyodbc/sqlcmd, or package installation.
EOF
