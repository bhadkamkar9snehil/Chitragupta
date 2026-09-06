#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPTS_DIR="$HOME/.hermes/profiles/l2-investigator/scripts"
ACTIVE_PROFILES=(l2-investigator l2-investigator-primary l2-reviewer-primary l2-reviewer-fallback)
INVESTIGATOR_PROFILES=(l2-investigator l2-investigator-primary)
REVIEWER_PROFILES=(l2-reviewer-primary l2-reviewer-fallback)
RETIRED_DEPLOYED_SCRIPTS=(dispatch_l2_review.py kanban_forward_bridge.py nudge_unpublished_runs.py)
LEARNING_VAULT="${CHITRAGUPTA_L2_LEARNING_VAULT:-$HOME/.hermes/l2-learning}"
LEARNING_EMBEDDING="${CHITRAGUPTA_ZVEC_EMBEDDING:-local/potion-retrieval-32m}"

mkdir -p "$SCRIPTS_DIR"
for retired in "${RETIRED_DEPLOYED_SCRIPTS[@]}"; do
  if [[ -e "$SCRIPTS_DIR/$retired" ]]; then
    rm -f "$SCRIPTS_DIR/$retired"
    echo "removed retired deployed script: $retired"
  fi
done

for f in \
  l2_pipeline_runtime.py \
  ticket_scout.py \
  reconcile_l2_pipeline.py \
  kanban_approval_publisher.py \
  kanban_reject_bridge.py \
  repair_incomplete_completions.py \
  audit_kanban_completions.py \
  enforce_publish_safety_net.py \
  run_coalesced.py \
  drain_and_summarize.py \
  l2_learning_curator.py \
  sync_l2_outcomes.py \
  mine_l2_learning_candidates.py \
  mine_l2_action_capability_candidates.py \
  l2_learning_cycle.py
do
  cp "$ROOT/Model_Bench/$f" "$SCRIPTS_DIR/$f"
done
chmod +x "$SCRIPTS_DIR"/*.py

test -f "$ROOT/Model_Bench/xstudio_l2_tool_bridge.py" \
  || { echo "FATAL: Model_Bench/xstudio_l2_tool_bridge.py is missing" >&2; exit 1; }
cp "$ROOT/deploy/helpdesk_workflow_binding.json" "$SCRIPTS_DIR/helpdesk_workflow_binding.json"
cp "$ROOT/deploy/xstudio_action_capabilities.json" "$SCRIPTS_DIR/xstudio_action_capabilities.json"

# Learning/KB refresh is intentionally not deployment authority. A missing zvec
# dependency or governed-Solution drift must not leave the deterministic L2
# runtime half-deployed. Local validation remains strict.
refresh_learning_vault() {
  if ! command -v zg >/dev/null 2>&1; then
    echo "WARNING: zg missing; skipping learning-vault refresh. Run Model_Bench/install_l2_learning_prereqs.sh."
    return 0
  fi

  echo "== Learning corpus sync =="
  if ! python3 "$ROOT/Model_Bench/sync_l2_learning_corpus.py" \
      --vault "$LEARNING_VAULT" --no-index; then
    echo "WARNING: canonical learning-corpus sync failed; continuing runtime deployment"
    return 0
  fi

  echo "== Governed Solution sync =="
  solution_rc=0
  python3 "$ROOT/Model_Bench/sync_l2_approved_solutions.py" \
    --vault "$LEARNING_VAULT" \
    --policy "$ROOT/deploy/solution_export_policy.json" || solution_rc=$?

  # Always refresh the index after a Solution sync attempt: a drift failure may
  # have removed stale trusted files.
  echo "== Learning vault index =="
  zg index --embedding "$LEARNING_EMBEDDING" "$LEARNING_VAULT" \
    || echo "WARNING: learning-vault indexing failed; explicit recall may be unavailable"

  if [[ "$solution_rc" -ne 0 ]]; then
    echo "WARNING: governed Solution sync found missing/drifted approvals; stale trusted exports were removed"
  fi

  if [[ "${CHITRAGUPTA_ZVEC_SERVER:-1}" != "0" ]]; then
    zg server on >/dev/null 2>&1 \
      || echo "WARNING: zg server did not start; direct mode remains available"
  fi
}

refresh_learning_vault

echo "== Learning outcome/candidate cycle (best effort) =="
python3 "$ROOT/Model_Bench/l2_learning_cycle.py" --vault "$LEARNING_VAULT" \
  || echo "WARNING: learning cycle reported errors; lifecycle deployment continues"

deploy_plugins() {
  local profile="$1" plugin src dir
  for plugin in xstudio-l2-orchestrator xstudio-l2-tools xstudio-l2-identity xstudio-l2-learning xstudio-l2-actions; do
    case "$plugin" in
      xstudio-l2-orchestrator) src="$ROOT/Model_Bench/xstudio_l2_orchestrator_plugin" ;;
      xstudio-l2-tools)        src="$ROOT/Model_Bench/xstudio_l2_tools_plugin" ;;
      xstudio-l2-identity)     src="$ROOT/Model_Bench/xstudio_l2_identity_plugin" ;;
      xstudio-l2-learning)     src="$ROOT/Model_Bench/xstudio_l2_learning_plugin" ;;
      xstudio-l2-actions)      src="$ROOT/Model_Bench/xstudio_l2_actions_plugin" ;;
    esac
    dir="$HOME/.hermes/profiles/$profile/plugins/$plugin"
    mkdir -p "$dir"
    cp "$src/__init__.py" "$dir/__init__.py"
    cp "$src/plugin.yaml" "$dir/plugin.yaml"
  done
}

install_shared_plugin_for_discovery() {
  local plugin="$1" src="$2" dir="$HOME/.hermes/plugins/$1"
  mkdir -p "$dir"
  cp "$src/__init__.py" "$dir/__init__.py"
  cp "$src/plugin.yaml" "$dir/plugin.yaml"
}

copy_soul() {
  local profile="$1" src="$ROOT/deploy/profiles/$1/SOUL.md"
  [[ -f "$src" ]] && cp "$src" "$HOME/.hermes/profiles/$1/SOUL.md"
}

copy_skill() {
  local profile="$1" skill="$2"
  local src="$ROOT/deploy/skills/xstudio/$skill/SKILL.md"
  local dst="$HOME/.hermes/profiles/$profile/skills/xstudio/$skill"
  if [[ -f "$src" ]]; then
    mkdir -p "$dst"
    cp "$src" "$dst/SKILL.md"
  fi
}

for profile in "${ACTIVE_PROFILES[@]}"; do
  deploy_plugins "$profile"
  copy_soul "$profile"
done

for profile in "${INVESTIGATOR_PROFILES[@]}"; do
  for skill in xstudio-l2-ticket-workflow xstudio-sql-write-discipline \
               xstudio-sap-api-investigation xstudio-sohar-heat-execution \
               xstudio-quality-delay-workorder; do
    copy_skill "$profile" "$skill"
  done
done

for profile in "${REVIEWER_PROFILES[@]}"; do
  for skill in xstudio-l2-draft-verifier xstudio-sql-write-discipline; do
    copy_skill "$profile" "$skill"
  done
done

echo "== Shared plugin install =="
install_shared_plugin_for_discovery xstudio-l2-tools "$ROOT/Model_Bench/xstudio_l2_tools_plugin"
install_shared_plugin_for_discovery xstudio-l2-identity "$ROOT/Model_Bench/xstudio_l2_identity_plugin"
install_shared_plugin_for_discovery xstudio-l2-learning "$ROOT/Model_Bench/xstudio_l2_learning_plugin"
install_shared_plugin_for_discovery xstudio-l2-actions "$ROOT/Model_Bench/xstudio_l2_actions_plugin"

echo "== Profile config =="
for profile in "${ACTIVE_PROFILES[@]}"; do
  config="$HOME/.hermes/profiles/$profile/config.yaml"
  python3 "$ROOT/Model_Bench/patch_profile_config.py" "$config"
  python3 "$ROOT/Model_Bench/patch_tool_search_off.py" "$config"
done

echo "== Root config =="
python3 "$ROOT/Model_Bench/patch_profile_config.py" --enable-plugin-only "$HOME/.hermes/config.yaml"

if [[ "${1:-}" != "--no-restart" ]]; then
  for profile in "${ACTIVE_PROFILES[@]}"; do
    systemctl --user restart "hermes-gateway-$profile.service" 2>/dev/null || true
  done
fi

echo
echo "Deployed Chitragupta adaptive L2 runtime."
echo "  evidence:          xstudio_l2 + harness-owned incident identity"
echo "  learning:          sessions ON; explicit l2_recall; generic prefetch OFF"
echo "  governed solutions: explicit hash-pinned sync; learning failures do not block deployment"
echo "  actions:           l2_actions planning only; NO execute operation"
echo "  capability backlog: repeated reviewed human actions -> unverified candidates"
echo "  mem0 provider:     unchanged"
echo "Next: bash $ROOT/Model_Bench/validate_l2_pipeline_local.sh"
