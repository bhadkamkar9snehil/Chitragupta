#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

LEARNING_VAULT="${CHITRAGUPTA_L2_LEARNING_VAULT:-$HOME/.hermes/l2-learning}"
GBRAIN_HOME="${XSTUDIO_GBRAIN_HOME:-$HOME/.hermes/xstudio-gbrain}"

PY_FILES=(
  Model_Bench/l2_pipeline_runtime.py
  Model_Bench/configure_helpdesk_workflow.py
  Model_Bench/xstudio_l2_tool_bridge.py
  Model_Bench/xstudio_l2_tools_plugin/__init__.py
  Model_Bench/sync_l2_approved_solutions.py
  Model_Bench/sync_l2_outcomes.py
)

CONTRACT_TESTS=(
  Model_Bench/test_l2_pipeline_runtime.py
  Model_Bench/test_xstudio_l2_tools_plugin.py
  Model_Bench/test_sync_l2_outcomes.py
  Model_Bench/test_sync_l2_approved_solutions.py
)

echo "== Syntax =="
bash -n Model_Bench/deploy_l2_pipeline_runtime.sh Model_Bench/validate_l2_pipeline_local.sh
python3 -m py_compile "${PY_FILES[@]}" "${CONTRACT_TESTS[@]}"

echo "== Focused owner tests =="
python3 -m unittest \
  Model_Bench/test_l2_pipeline_runtime.py \
  Model_Bench/test_xstudio_l2_tools_plugin.py \
  Model_Bench/test_sync_l2_outcomes.py \
  Model_Bench/test_sync_l2_approved_solutions.py

echo "== Governed Solution policy =="
python3 Model_Bench/sync_l2_approved_solutions.py \
  --vault "$LEARNING_VAULT" \
  --policy deploy/solution_export_policy.json \
  --dry-run

echo "== Reviewed outcome materialization =="
python3 Model_Bench/sync_l2_outcomes.py --vault "$LEARNING_VAULT" --dry-run

echo "== Shared GBrain =="
command -v gbrain >/dev/null 2>&1 || { echo "FAIL: gbrain missing" >&2; exit 1; }
GBRAIN_HOME="$GBRAIN_HOME" gbrain --version
GBRAIN_HOME="$GBRAIN_HOME" gbrain doctor --json
GBRAIN_HOME="$GBRAIN_HOME" gbrain sources list --json

echo "== Hermes native GBrain MCP =="
hermes mcp test gbrain

echo "== Hermes L2 scout cron =="
CRON_STATE="$(hermes -p l2-investigator cron list --all)"
printf '%s\n' "$CRON_STATE"
grep -q "L2 Ticket Scout" <<<"$CRON_STATE" || { echo "FAIL: L2 Ticket Scout cron missing" >&2; exit 1; }
grep -q "l2_pipeline_runtime.py" <<<"$CRON_STATE" || { echo "FAIL: scout cron does not use l2_pipeline_runtime.py" >&2; exit 1; }
if grep -q "ticket_scout.py" <<<"$CRON_STATE"; then
  echo "FAIL: retired ticket_scout.py is still scheduled" >&2
  exit 1
fi
hermes -p l2-investigator cron doctor

echo "== Retired compatibility guard =="
for path in \
  Model_Bench/kb_retrieval.py \
  Model_Bench/l2_gbrain.py \
  Model_Bench/test_l2_gbrain.py \
  Model_Bench/ticket_scout.py \
  deploy/skills/xstudio/xstudio-l2-ticket-workflow/SKILL.md \
  deploy/skills/xstudio/xstudio-l2-draft-verifier/SKILL.md \
  deploy/skills/xstudio/xstudio-sql-write-discipline/SKILL.md
do
  [[ ! -e "$path" ]] || { echo "FAIL: retired repo artifact exists: $path" >&2; exit 1; }
done

DEPLOYED_SCRIPTS="$HOME/.hermes/profiles/l2-investigator/scripts"
for retired in kb_retrieval.py l2_gbrain.py ticket_scout.py sync_l2_gbrain.py l2_learning_cycle.py
do
  [[ ! -e "$DEPLOYED_SCRIPTS/$retired" ]] || {
    echo "FAIL: retired deployed script exists: $retired" >&2
    exit 1
  }
done

echo "== Live read-only lifecycle checks =="
python3 Model_Bench/configure_helpdesk_workflow.py
python3 Model_Bench/l2_pipeline_runtime.py status
python3 Model_Bench/l2_pipeline_runtime.py reconcile --dry-run

cat <<'EOF'

L2 VALIDATION COMPLETE

Hermes owns agent execution, sessions, Kanban and native GBrain MCP.
GBrain owns retrieval/index/graph/maintenance.
Chitragupta owns only the deterministic Helpdesk lifecycle, typed live
XStudio evidence, reviewed outcome materialization and governed Solution export.
EOF
