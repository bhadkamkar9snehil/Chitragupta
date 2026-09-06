#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

LEARNING_VAULT="${CHITRAGUPTA_L2_LEARNING_VAULT:-$HOME/.hermes/l2-learning}"
GBRAIN_HOME="${CHITRAGUPTA_GBRAIN_HOME:-$HOME/.hermes/l2-gbrain}"
HISTORICAL_EVAL="$LEARNING_VAULT/eval/historical_retrieval_cases.jsonl"

PY_FILES=(
  Model_Bench/l2_pipeline_runtime.py Model_Bench/ticket_scout.py
  Model_Bench/reconcile_l2_pipeline.py Model_Bench/kanban_approval_publisher.py
  Model_Bench/kanban_reject_bridge.py Model_Bench/repair_incomplete_completions.py
  Model_Bench/audit_kanban_completions.py Model_Bench/enforce_publish_safety_net.py
  Model_Bench/configure_helpdesk_workflow.py Model_Bench/patch_profile_config.py
  Model_Bench/patch_tool_search_off.py Model_Bench/xstudio_l2_orchestrator_plugin/__init__.py
  Model_Bench/xstudio_l2_tools_plugin/__init__.py Model_Bench/xstudio_l2_identity_plugin/__init__.py
  Model_Bench/xstudio_l2_learning_plugin/__init__.py Model_Bench/xstudio_l2_actions_plugin/__init__.py
  Model_Bench/xstudio_l2_tool_bridge.py Model_Bench/l2_gbrain.py Model_Bench/sync_l2_gbrain.py
  Model_Bench/sync_l2_learning_corpus.py Model_Bench/sync_l2_outcomes.py
  Model_Bench/sync_l2_approved_solutions.py Model_Bench/mine_l2_learning_candidates.py
  Model_Bench/mine_l2_action_capability_candidates.py Model_Bench/l2_learning_cycle.py
  Model_Bench/build_l2_historical_retrieval_eval.py Model_Bench/l2_learning_curator.py
  Model_Bench/l2_action_capability_curator.py Model_Bench/benchmark_l2_learning_retrieval.py
  Model_Bench/validate_action_capabilities.py
)

CONTRACT_TESTS=(
  Model_Bench/test_l2_pipeline_runtime.py Model_Bench/test_xstudio_l2_tools_plugin.py
  Model_Bench/test_xstudio_l2_identity_plugin.py Model_Bench/test_l2_gbrain.py
  Model_Bench/test_sync_l2_gbrain.py Model_Bench/test_xstudio_l2_learning_plugin.py
  Model_Bench/test_sync_l2_learning_corpus.py Model_Bench/test_sync_l2_outcomes.py
  Model_Bench/test_sync_l2_approved_solutions.py Model_Bench/test_mine_l2_learning_candidates.py
  Model_Bench/test_mine_l2_action_capability_candidates.py Model_Bench/test_l2_learning_cycle.py
  Model_Bench/test_build_l2_historical_retrieval_eval.py Model_Bench/test_l2_action_capability_curator.py
  Model_Bench/test_xstudio_l2_actions_plugin.py Model_Bench/test_validate_action_capabilities.py
  Model_Bench/test_patch_profile_config.py Model_Bench/test_adaptive_deploy_contract.py
)

SH_FILES=(Model_Bench/deploy_l2_pipeline_runtime.sh Model_Bench/install_l2_learning_prereqs.sh Model_Bench/mirror_wsl_artifacts.sh Model_Bench/validate_l2_pipeline_local.sh)

echo "== Syntax =="
bash -n "${SH_FILES[@]}"
python3 -m py_compile "${PY_FILES[@]}" "${CONTRACT_TESTS[@]}"

echo "== Contract tests =="
for test_file in "${CONTRACT_TESTS[@]}"; do
  echo "-- $test_file"
  python3 "$test_file"
done

echo "== Static policy validation =="
python3 Model_Bench/validate_action_capabilities.py
python3 Model_Bench/validate_knowledge_manifest.py
python3 Model_Bench/test_kb_retrieval.py

echo "== Learning vault =="
python3 Model_Bench/sync_l2_learning_corpus.py --vault "$LEARNING_VAULT" --check

echo "== GBrain deterministic retrieval substrate =="
if ! command -v gbrain >/dev/null 2>&1; then
  echo "FAIL: gbrain missing. Run: bash Model_Bench/install_l2_learning_prereqs.sh" >&2
  exit 1
fi
GBRAIN_HOME="$GBRAIN_HOME" gbrain --version
GBRAIN_HOME="$GBRAIN_HOME" gbrain doctor --json
python3 Model_Bench/sync_l2_gbrain.py --vault "$LEARNING_VAULT" --check

echo "== Governed Solution sync preview =="
python3 Model_Bench/sync_l2_approved_solutions.py --vault "$LEARNING_VAULT" --policy deploy/solution_export_policy.json --dry-run

echo "== Retrieval smoke benchmark =="
python3 Model_Bench/benchmark_l2_learning_retrieval.py --min-hit-rate 0.80

echo "== Learning sidecar preview =="
python3 Model_Bench/l2_learning_cycle.py --vault "$LEARNING_VAULT" --dry-run

echo "== Capability backlog =="
python3 Model_Bench/l2_action_capability_curator.py --vault "$LEARNING_VAULT" list

echo "== Historical retrieval replay =="
python3 Model_Bench/build_l2_historical_retrieval_eval.py --vault "$LEARNING_VAULT"
if [[ -s "$HISTORICAL_EVAL" ]]; then
  python3 Model_Bench/benchmark_l2_learning_retrieval.py --cases "$HISTORICAL_EVAL" --min-hit-rate 0.60
else
  echo "INFO: no correlated historical session/outcome cases yet; replay benchmark skipped"
fi

echo "== Live profile plugin/toolset config =="
for profile in l2-investigator l2-investigator-primary l2-reviewer-primary l2-reviewer-fallback; do
  config="$HOME/.hermes/profiles/$profile/config.yaml"
  [[ -f "$config" ]] || { echo "FAIL: missing live profile config $config" >&2; exit 1; }
  python3 Model_Bench/patch_profile_config.py --check "$config"
done
python3 Model_Bench/patch_profile_config.py --enable-plugin-only --check "$HOME/.hermes/config.yaml"

echo "== Retired live-deployment guard =="
DEPLOYED_SCRIPTS="$HOME/.hermes/profiles/l2-investigator/scripts"
for retired in dispatch_l2_review.py kanban_forward_bridge.py nudge_unpublished_runs.py; do
  [[ ! -e "$DEPLOYED_SCRIPTS/$retired" ]] || { echo "FAIL: retired script is still deployed live: $DEPLOYED_SCRIPTS/$retired" >&2; exit 1; }
done
if systemctl --user is-enabled chitragupta-gbrain-sync.service >/dev/null 2>&1; then
  echo "FAIL: independent GBrain watcher is enabled; retrieval sync must belong to l2_learning_cycle.py" >&2
  exit 1
fi

echo "== Live read-only checks =="
python3 Model_Bench/configure_helpdesk_workflow.py
python3 Model_Bench/l2_pipeline_runtime.py status
python3 Model_Bench/l2_pipeline_runtime.py reconcile --dry-run

cat <<'EOF'

LOCAL VALIDATION COMPLETE

Control plane:
  claim -> investigate -> normalize -> frozen review -> publish/rework
  typed evidence: xstudio_l2
  run/ticket identity: harness-owned

Learning plane:
  sessions: ON, redacted, unverified
  generic model-driven prefetch: OFF
  GBrain: isolated derivative retrieval substrate behind harness contracts
  trust lanes: separate non-federated GBrain sources
  synchronization: owned by one learning sidecar; no independent watcher
  governed reusable Solutions: explicit semantic-hash approval
  historical cases/candidates: not current-ticket proof
  mem0: unchanged narrow operational-memory provider

Action plane:
  registry: deploy/xstudio_action_capabilities.json
  backlog: repeated reviewed NEEDS_HUMAN_ACTION cases
  curator: needs_executor_design -> shadow_ready -> registry_entry
  model-facing l2_actions: list/describe/plan/plans/validate_plan
  execution: unavailable
EOF
