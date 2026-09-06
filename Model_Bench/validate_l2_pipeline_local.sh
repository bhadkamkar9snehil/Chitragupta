#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
LEARNING_VAULT="${CHITRAGUPTA_L2_LEARNING_VAULT:-$HOME/.hermes/l2-learning}"

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
  Model_Bench/xstudio_l2_learning_plugin/__init__.py
  Model_Bench/xstudio_l2_actions_plugin/__init__.py
  Model_Bench/xstudio_l2_tool_bridge.py
  Model_Bench/sync_l2_learning_corpus.py
  Model_Bench/sync_l2_outcomes.py
  Model_Bench/l2_learning_curator.py
  Model_Bench/benchmark_l2_learning_retrieval.py
  Model_Bench/validate_action_capabilities.py
  Model_Bench/test_xstudio_l2_tools_plugin.py
  Model_Bench/test_xstudio_l2_learning_plugin.py
  Model_Bench/test_xstudio_l2_actions_plugin.py
  Model_Bench/test_sync_l2_outcomes.py
  Model_Bench/test_patch_profile_config.py
)
SH_FILES=(
  Model_Bench/deploy_l2_pipeline_runtime.sh
  Model_Bench/install_l2_learning_prereqs.sh
  Model_Bench/mirror_wsl_artifacts.sh
  Model_Bench/validate_l2_pipeline_local.sh
)

echo "== Shell syntax =="
bash -n "${SH_FILES[@]}"
echo "== Python syntax =="
python3 -m py_compile "${PY_FILES[@]}"
echo "== Deterministic lifecycle contract tests =="
python3 Model_Bench/test_l2_pipeline_runtime.py
echo "== Typed investigation-tool contract tests =="
python3 Model_Bench/test_xstudio_l2_tools_plugin.py
echo "== Adaptive learning contract tests =="
python3 Model_Bench/test_xstudio_l2_learning_plugin.py
echo "== Outcome-conditioned learning contract tests =="
python3 Model_Bench/test_sync_l2_outcomes.py
echo "== Non-executing action-planner contract tests =="
python3 Model_Bench/test_xstudio_l2_actions_plugin.py
echo "== Profile/root config patcher contract tests =="
python3 Model_Bench/test_patch_profile_config.py
echo "== Corrective-action registry =="
python3 Model_Bench/validate_action_capabilities.py
echo "== Knowledge/skill validation =="
python3 Model_Bench/validate_knowledge_manifest.py
python3 Model_Bench/test_kb_retrieval.py

echo "== zvec learning substrate =="
if ! command -v zg >/dev/null 2>&1; then
  echo "FAIL: zg missing. Run: bash Model_Bench/install_l2_learning_prereqs.sh" >&2
  exit 1
fi
python3 Model_Bench/sync_l2_learning_corpus.py --vault "$LEARNING_VAULT" --check
zg status "$LEARNING_VAULT" --check-ready

echo "== Learning retrieval smoke benchmark =="
python3 Model_Bench/benchmark_l2_learning_retrieval.py --min-hit-rate 0.80

echo "== Outcome case sync preview (read-only) =="
python3 Model_Bench/sync_l2_outcomes.py --vault "$LEARNING_VAULT" --dry-run || true

echo "== Live profile plugin/toolset config =="
for profile in l2-investigator l2-investigator-primary l2-reviewer-primary l2-reviewer-fallback; do
  config="$HOME/.hermes/profiles/$profile/config.yaml"
  if [[ ! -f "$config" ]]; then
    echo "FAIL: missing live profile config $config" >&2
    exit 1
  fi
  python3 Model_Bench/patch_profile_config.py --check "$config"
done
python3 Model_Bench/patch_profile_config.py --enable-plugin-only --check "$HOME/.hermes/config.yaml"

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
cat <<EOF
LOCAL VALIDATION COMPLETE.

Control plane:
  lifecycle:           claim -> investigate -> normalize -> frozen review -> publish/rework
  typed evidence:      xstudio_l2

Learning plane:
  shared vault:        $LEARNING_VAULT
  session recording:   ON (redacted, unverified episodic)
  automatic prefetch:  OFF by design
  outcome cases:       approved/rejected/reopened historical case classes
  explicit recall:     trusted/case/session scopes with trust labels
  candidate learning:  l2_lesson -> candidates only; separate promotion required
  mem0 provider:       unchanged

Action plane:
  registry:            deploy/xstudio_action_capabilities.json
  direct toolset:      l2_actions
  operations:          list/describe/plan/plans/validate_plan
  execution:           intentionally unavailable
  global registry mode: observe until deliberately promoted

For the next natural ticket verify:
  - current evidence uses xstudio_l2;
  - historical recall is explicit and trust-scoped;
  - sessions are recorded and outcome cases appear after review/publication;
  - l2_action cannot execute anything and rejects planning while global_mode=observe;
  - no terminal Python/pyodbc/sqlcmd/package-install SQL transport reappears.
EOF
