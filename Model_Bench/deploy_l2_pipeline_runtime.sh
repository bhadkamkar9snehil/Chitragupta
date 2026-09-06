#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPTS_DIR="$HOME/.hermes/profiles/l2-investigator/scripts"
ACTIVE_PROFILES=(l2-investigator l2-investigator-primary l2-reviewer-primary l2-reviewer-fallback)
INVESTIGATOR_PROFILES=(l2-investigator l2-investigator-primary)
REVIEWER_PROFILES=(l2-reviewer-primary l2-reviewer-fallback)
LEARNING_VAULT="${CHITRAGUPTA_L2_LEARNING_VAULT:-$HOME/.hermes/l2-learning}"

mkdir -p "$SCRIPTS_DIR"

# Remove retired compatibility/facade scripts from older deployments. The
# lifecycle now has one entry point: l2_pipeline_runtime.py.
for retired in \
  dispatch_l2_review.py kanban_forward_bridge.py nudge_unpublished_runs.py \
  reconcile_l2_pipeline.py kanban_approval_publisher.py kanban_reject_bridge.py \
  repair_incomplete_completions.py enforce_publish_safety_net.py \
  l2_pipeline_runtime_core.py l2_pipeline_context_helpers.py \
  l2_pipeline_context_cards.py l2_pipeline_context_scout.py \
  l2_context_envelope.py l2_context_delivery.py l2_context_delivery_base.py \
  l2_context_delivery_assembly.py l2_context_delivery_receipts.py \
  kb_retrieval_base.py kb_retrieval_cli.py kb_retrieval_corpus.py kb_retrieval_routing.py
do
  rm -f "$SCRIPTS_DIR/$retired"
done

for f in \
  l2_pipeline_runtime.py \
  kb_retrieval.py \
  ticket_scout.py \
  audit_kanban_completions.py \
  xstudio_l2_tool_bridge.py \
  l2_gbrain.py \
  sync_l2_learning_corpus.py \
  sync_l2_approved_solutions.py \
  sync_l2_outcomes.py \
  mine_l2_learning_candidates.py \
  mine_l2_action_capability_candidates.py \
  l2_learning_curator.py \
  l2_action_capability_curator.py \
  sync_l2_gbrain.py \
  l2_learning_cycle.py
do
  cp "$ROOT/Model_Bench/$f" "$SCRIPTS_DIR/$f"
done
chmod +x "$SCRIPTS_DIR"/*.py

cp "$ROOT/deploy/helpdesk_workflow_binding.json" "$SCRIPTS_DIR/helpdesk_workflow_binding.json"
cp "$ROOT/deploy/xstudio_action_capabilities.json" "$SCRIPTS_DIR/xstudio_action_capabilities.json"

# Materialize authoritative source files first; GBrain only indexes them.
echo "== Learning corpus sync =="
python3 "$ROOT/Model_Bench/sync_l2_learning_corpus.py" --vault "$LEARNING_VAULT" \
  || echo "WARNING: canonical learning-corpus sync failed"

echo "== Governed Solution sync =="
python3 "$ROOT/Model_Bench/sync_l2_approved_solutions.py" \
  --vault "$LEARNING_VAULT" \
  --policy "$ROOT/deploy/solution_export_policy.json" \
  || echo "WARNING: governed Solution sync found missing/drifted approvals"

echo "== Learning/GBrain convergence =="
python3 "$ROOT/Model_Bench/l2_learning_cycle.py" --vault "$LEARNING_VAULT" \
  || echo "WARNING: learning cycle reported errors; lifecycle deployment continues"

deploy_plugin() {
  local profile="$1" plugin="$2" src
  case "$plugin" in
    xstudio-l2-trace)        src="$ROOT/Model_Bench/xstudio_l2_trace_plugin" ;;
    xstudio-l2-orchestrator) src="$ROOT/Model_Bench/xstudio_l2_orchestrator_plugin" ;;
    xstudio-l2-tools)        src="$ROOT/Model_Bench/xstudio_l2_tools_plugin" ;;
    xstudio-l2-identity)     src="$ROOT/Model_Bench/xstudio_l2_identity_plugin" ;;
    xstudio-l2-learning)     src="$ROOT/Model_Bench/xstudio_l2_learning_plugin" ;;
    xstudio-l2-actions)      src="$ROOT/Model_Bench/xstudio_l2_actions_plugin" ;;
  esac
  local dst="$HOME/.hermes/profiles/$profile/plugins/$plugin"
  mkdir -p "$dst"
  cp "$src/__init__.py" "$dst/__init__.py"
  cp "$src/plugin.yaml" "$dst/plugin.yaml"
}

copy_skill() {
  local profile="$1" skill="$2"
  local src="$ROOT/deploy/skills/xstudio/$skill/SKILL.md"
  local dst="$HOME/.hermes/profiles/$profile/skills/xstudio/$skill"
  mkdir -p "$dst"
  cp "$src" "$dst/SKILL.md"
}

for profile in "${ACTIVE_PROFILES[@]}"; do
  mkdir -p "$HOME/.hermes/profiles/$profile"
  cp "$ROOT/deploy/profiles/$profile/config.yaml" "$HOME/.hermes/profiles/$profile/config.yaml"
  cp "$ROOT/deploy/profiles/$profile/SOUL.md" "$HOME/.hermes/profiles/$profile/SOUL.md"
  for plugin in xstudio-l2-trace xstudio-l2-orchestrator xstudio-l2-tools xstudio-l2-identity xstudio-l2-learning xstudio-l2-actions; do
    deploy_plugin "$profile" "$plugin"
  done
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

# Old independent watcher is explicitly retired. l2_learning_cycle owns sync.
systemctl --user disable --now chitragupta-gbrain-sync.service >/dev/null 2>&1 || true
rm -f "$HOME/.config/systemd/user/chitragupta-gbrain-sync.service"
systemctl --user daemon-reload >/dev/null 2>&1 || true

if [[ "${1:-}" != "--no-restart" ]]; then
  for profile in "${ACTIVE_PROFILES[@]}"; do
    systemctl --user restart "hermes-gateway-$profile.service" 2>/dev/null || true
  done
fi

echo
echo "Deployed Chitragupta L2 on Hermes."
echo "  harness:    Hermes"
echo "  lifecycle:  l2_pipeline_runtime.py"
echo "  evidence:   xstudio_l2 typed tools"
echo "  retrieval:  isolated GBrain via kb_retrieval.py + supplemental l2_recall"
echo "  learning:   outcome materialization -> candidates -> GBrain sync"
echo "  actions:    planning only; no execute operation"
