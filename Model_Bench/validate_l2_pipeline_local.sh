#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

LEARNING_VAULT="${CHITRAGUPTA_L2_LEARNING_VAULT:-$HOME/.hermes/l2-learning}"
GBRAIN_HOME="${CHITRAGUPTA_GBRAIN_HOME:-$HOME/.hermes/l2-gbrain}"

PY_FILES=(
  Model_Bench/l2_pipeline_runtime.py
  Model_Bench/kb_retrieval.py
  Model_Bench/ticket_scout.py
  Model_Bench/xstudio_l2_tool_bridge.py
  Model_Bench/xstudio_l2_tools_plugin/__init__.py
  Model_Bench/l2_gbrain.py
  Model_Bench/sync_l2_approved_solutions.py
  Model_Bench/sync_l2_outcomes.py
  Model_Bench/sync_l2_gbrain.py
  Model_Bench/l2_learning_cycle.py
)

CONTRACT_TESTS=(
  Model_Bench/test_l2_pipeline_runtime.py
  Model_Bench/test_l2_gbrain.py
  Model_Bench/test_sync_l2_gbrain.py
  Model_Bench/test_xstudio_l2_tools_plugin.py
  Model_Bench/test_sync_l2_outcomes.py
  Model_Bench/test_sync_l2_approved_solutions.py
  Model_Bench/test_l2_learning_cycle.py
)

SH_FILES=(
  Model_Bench/deploy_l2_pipeline_runtime.sh
  Model_Bench/install_l2_learning_prereqs.sh
  Model_Bench/validate_l2_pipeline_local.sh
)

echo "== Syntax =="
bash -n "${SH_FILES[@]}"
python3 -m py_compile "${PY_FILES[@]}" "${CONTRACT_TESTS[@]}"

echo "== Governed Solution policy =="
python3 Model_Bench/sync_l2_approved_solutions.py \
  --vault "$LEARNING_VAULT" \
  --policy deploy/solution_export_policy.json \
  --dry-run

echo "== GBrain =="
command -v gbrain >/dev/null 2>&1 || { echo "FAIL: gbrain missing" >&2; exit 1; }
GBRAIN_HOME="$GBRAIN_HOME" gbrain --version
GBRAIN_HOME="$GBRAIN_HOME" gbrain doctor --json
CHITRAGUPTA_KNOWLEDGE_PATH="$ROOT/Knowledge" \
CHITRAGUPTA_REFERENCE_PATH="$ROOT/Reference Documents" \
python3 Model_Bench/sync_l2_gbrain.py \
  --vault "$LEARNING_VAULT" \
  --knowledge "$ROOT/Knowledge" \
  --reference "$ROOT/Reference Documents" \
  --check

echo "== Outcome history / GBrain convergence =="
CHITRAGUPTA_KNOWLEDGE_PATH="$ROOT/Knowledge" \
CHITRAGUPTA_REFERENCE_PATH="$ROOT/Reference Documents" \
python3 Model_Bench/l2_learning_cycle.py --vault "$LEARNING_VAULT" --dry-run

echo "== Live read-only lifecycle checks =="
python3 Model_Bench/configure_helpdesk_workflow.py
python3 Model_Bench/l2_pipeline_runtime.py status
python3 Model_Bench/l2_pipeline_runtime.py reconcile --dry-run

cat <<'EOF'

LOCAL VALIDATION COMPLETE

Hermes owns the agent harness and durable sessions.
Chitragupta owns the Helpdesk lifecycle, typed XStudio domain boundary,
reviewed outcome history, governed Solutions, and isolated derivative GBrain retrieval.
EOF
