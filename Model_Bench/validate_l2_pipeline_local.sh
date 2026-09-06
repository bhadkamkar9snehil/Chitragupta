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
  Model_Bench/mine_l2_learning_candidates.py
  Model_Bench/l2_learning_curator.py
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
  Model_Bench/test_mine_l2_learning_candidates.py
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
python3 Model_Bench/sync_l2_gbrain.py \
  --vault "$LEARNING_VAULT" \
  --knowledge "$ROOT/Knowledge" \
  --check

echo "== Learning cycle =="
CHITRAGUPTA_KNOWLEDGE_PATH="$ROOT/Knowledge" \
python3 Model_Bench/l2_learning_cycle.py --vault "$LEARNING_VAULT" --dry-run

echo "== Retired deployment guard =="
DEPLOYED_SCRIPTS="$HOME/.hermes/profiles/l2-investigator/scripts"
for retired in \
  dispatch_l2_review.py kanban_forward_bridge.py nudge_unpublished_runs.py \
  reconcile_l2_pipeline.py kanban_approval_publisher.py kanban_reject_bridge.py \
  repair_incomplete_completions.py enforce_publish_safety_net.py audit_kanban_completions.py \
  l2_pipeline_runtime_core.py l2_pipeline_context_helpers.py \
  l2_pipeline_context_cards.py l2_pipeline_context_scout.py \
  l2_context_envelope.py l2_context_delivery.py l2_context_delivery_base.py \
  l2_context_delivery_assembly.py l2_context_delivery_receipts.py \
  kb_retrieval_base.py kb_retrieval_cli.py kb_retrieval_corpus.py kb_retrieval_routing.py \
  setup_mem0.py seed_mem0_lessons.py reapply_mem0_patch.py \
  run_coalesced.py drain_l2_trace_log.py drain_and_summarize.py \
  generate_readable_trace_summary.py validate_action_capabilities.py \
  mine_l2_action_capability_candidates.py l2_action_capability_curator.py \
  sync_l2_learning_corpus.py build_l2_historical_retrieval_eval.py \
  benchmark_l2_learning_retrieval.py validate_knowledge_manifest.py
do
  [[ ! -e "$DEPLOYED_SCRIPTS/$retired" ]] || {
    echo "FAIL: retired script still deployed: $retired" >&2
    exit 1
  }
done
if systemctl --user is-enabled chitragupta-gbrain-sync.service >/dev/null 2>&1; then
  echo "FAIL: retired independent GBrain watcher is enabled" >&2
  exit 1
fi

echo "== Live read-only lifecycle checks =="
python3 Model_Bench/configure_helpdesk_workflow.py
python3 Model_Bench/l2_pipeline_runtime.py status
python3 Model_Bench/l2_pipeline_runtime.py reconcile --dry-run

cat <<'EOF'

LOCAL VALIDATION COMPLETE

Hermes owns the agent harness and durable sessions.
Chitragupta owns the Helpdesk lifecycle, typed XStudio domain boundary,
review-governed reusable learning, and isolated derivative GBrain retrieval.
EOF
