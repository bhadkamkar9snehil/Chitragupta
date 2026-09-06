#!/usr/bin/env bash
set -euo pipefail

# Deploy deterministic lifecycle, typed evidence, outcome-conditioned learning,
# and the non-executing corrective-action planning surface.
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPTS_DIR="$HOME/.hermes/profiles/l2-investigator/scripts"
ACTIVE_PROFILES=(l2-investigator l2-investigator-primary l2-reviewer-primary l2-reviewer-fallback)
INVESTIGATOR_PROFILES=(l2-investigator l2-investigator-primary)
REVIEWER_PROFILES=(l2-reviewer-primary l2-reviewer-fallback)
RETIRED_DEPLOYED_SCRIPTS=(dispatch_l2_review.py kanban_forward_bridge.py nudge_unpublished_runs.py)
LEARNING_VAULT="${CHITRAGUPTA_L2_LEARNING_VAULT:-$HOME/.hermes/l2-learning}"

mkdir -p "$SCRIPTS_DIR"
for retired in "${RETIRED_DEPLOYED_SCRIPTS[@]}"; do
  if [[ -e "$SCRIPTS_DIR/$retired" ]]; then
    rm -f "$SCRIPTS_DIR/$retired"
    echo "removed retired deployed script: $retired"
  fi
done

# Only scripts valid from the deployed profile location are copied here.
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
  sync_l2_outcomes.py
 do
  cp "$ROOT/Model_Bench/$f" "$SCRIPTS_DIR/$f"
 done
chmod +x "$SCRIPTS_DIR"/*.py

test -f "$ROOT/Model_Bench/xstudio_l2_tool_bridge.py" \
  || { echo "FATAL: Model_Bench/xstudio_l2_tool_bridge.py is missing" >&2; exit 1; }
cp "$ROOT/deploy/helpdesk_workflow_binding.json" "$SCRIPTS_DIR/helpdesk_workflow_binding.json"
cp "$ROOT/deploy/xstudio_action_capabilities.json" "$SCRIPTS_DIR/xstudio_action_capabilities.json"

# zvec is operator-installed, never model-installed during a ticket.
if ! command -v zg >/dev/null 2>&1; then
  cat >&2 <<'EOF'
FATAL: zvec-grep (`zg`) is required by the adaptive-learning branch but is not on PATH.
Run:
  bash Model_Bench/install_l2_learning_prereqs.sh
Then rerun this deployment.
EOF
  exit 1
fi

echo "== Learning corpus sync =="
python3 "$ROOT/Model_Bench/sync_l2_learning_corpus.py" --vault "$LEARNING_VAULT"
if [[ "${CHITRAGUPTA_ZVEC_SERVER:-1}" != "0" ]]; then
  zg server on >/dev/null 2>&1 || echo "WARNING: zg server did not start; direct mode remains available"
fi

# Convert already-known reviewer/publisher history into outcome-labelled cases.
# This is best-effort learning data; deployment must not fail because a historical
# SQL read or stale card cannot be materialized.
echo "== Outcome case sync (best effort) =="
python3 "$ROOT/Model_Bench/sync_l2_outcomes.py" --vault "$LEARNING_VAULT" \
  || echo "WARNING: outcome case sync reported errors; lifecycle deployment continues"

deploy_plugins() {
  local profile="$1" plugin src dir
  for plugin in xstudio-l2-orchestrator xstudio-l2-tools xstudio-l2-learning xstudio-l2-actions; do
    case "$plugin" in
      xstudio-l2-orchestrator) src="$ROOT/Model_Bench/xstudio_l2_orchestrator_plugin" ;;
      xstudio-l2-tools)        src="$ROOT/Model_Bench/xstudio_l2_tools_plugin" ;;
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
echo "  evidence toolset:    xstudio_l2"
echo "  learning toolset:    l2_learning (explicit recall + candidate lessons)"
echo "  action toolset:      l2_actions (list/describe/plan/plans/validate_plan; NO execute)"
echo "  session recording:   ON"
echo "  outcome case capture: ON, best effort, lifecycle-independent"
echo "  automatic prefetch:  OFF by design"
echo "  mem0 provider:       unchanged"
echo "  action execution:    unavailable until a separate deterministic executor is deliberately introduced"
echo "Next: bash $ROOT/Model_Bench/validate_l2_pipeline_local.sh"
