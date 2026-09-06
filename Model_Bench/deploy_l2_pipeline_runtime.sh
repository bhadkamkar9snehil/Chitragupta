#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPTS_DIR="$HOME/.hermes/profiles/l2-investigator/scripts"
ACTIVE_PROFILES=(l2-investigator l2-investigator-primary l2-reviewer-primary)
INVESTIGATOR_PROFILES=(l2-investigator l2-investigator-primary)
LEARNING_VAULT="${CHITRAGUPTA_L2_LEARNING_VAULT:-$HOME/.hermes/l2-learning}"

mkdir -p "$SCRIPTS_DIR"

# One-time cleanup of names deployed by retired Chitragupta layers.
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
  benchmark_l2_learning_retrieval.py
do
  rm -f "$SCRIPTS_DIR/$retired"
done

# Only scheduled-runtime dependencies are copied into the Hermes profile.
for f in \
  l2_pipeline_runtime.py ticket_scout.py l2_gbrain.py \
  sync_l2_outcomes.py mine_l2_learning_candidates.py \
  sync_l2_gbrain.py l2_learning_cycle.py
do
  cp "$ROOT/Model_Bench/$f" "$SCRIPTS_DIR/$f"
done
chmod +x "$SCRIPTS_DIR"/*.py
cp "$ROOT/deploy/helpdesk_workflow_binding.json" "$SCRIPTS_DIR/helpdesk_workflow_binding.json"

echo "== Governed reusable solutions =="
python3 "$ROOT/Model_Bench/sync_l2_approved_solutions.py" \
  --vault "$LEARNING_VAULT" --policy "$ROOT/deploy/solution_export_policy.json" \
  || echo "WARNING: governed Solution sync found missing/drifted approvals"

echo "== Outcome learning / GBrain convergence =="
CHITRAGUPTA_KNOWLEDGE_PATH="$ROOT/Knowledge" \
python3 "$ROOT/Model_Bench/l2_learning_cycle.py" --vault "$LEARNING_VAULT" \
  || echo "WARNING: learning cycle reported errors; lifecycle deployment continues"

deploy_plugin() {
  local profile="$1"
  local src="$ROOT/Model_Bench/xstudio_l2_tools_plugin"
  local dst="$HOME/.hermes/profiles/$profile/plugins/xstudio-l2-tools"
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

profile_soul() {
  case "$1" in
    l2-investigator|l2-investigator-primary)
      printf '%s\n' "$ROOT/deploy/profiles/l2-investigator-primary/SOUL.md"
      ;;
    l2-reviewer-primary)
      printf '%s\n' "$ROOT/deploy/profiles/l2-reviewer-primary/SOUL.md"
      ;;
  esac
}

for profile in "${ACTIVE_PROFILES[@]}"; do
  mkdir -p "$HOME/.hermes/profiles/$profile"
  cp "$ROOT/deploy/profiles/$profile/config.yaml" "$HOME/.hermes/profiles/$profile/config.yaml"
  cp "$(profile_soul "$profile")" "$HOME/.hermes/profiles/$profile/SOUL.md"
  rm -rf \
    "$HOME/.hermes/profiles/$profile/plugins/xstudio-l2-orchestrator" \
    "$HOME/.hermes/profiles/$profile/plugins/xstudio-l2-trace" \
    "$HOME/.hermes/profiles/$profile/plugins/xstudio-l2-actions" \
    "$HOME/.hermes/profiles/$profile/plugins/xstudio-l2-identity" \
    "$HOME/.hermes/profiles/$profile/plugins/xstudio-l2-learning"
  deploy_plugin "$profile"
done

for profile in "${INVESTIGATOR_PROFILES[@]}"; do
  for skill in xstudio-l2-ticket-workflow xstudio-sql-write-discipline \
               xstudio-sap-api-investigation xstudio-sohar-heat-execution \
               xstudio-quality-delay-workorder; do
    copy_skill "$profile" "$skill"
  done
done

for skill in xstudio-l2-draft-verifier xstudio-sql-write-discipline; do
  copy_skill l2-reviewer-primary "$skill"
done

# Retire the duplicate reviewer gateway/profile. The lifecycle still recognizes
# legacy cards assigned to this name, but creates no new work there.
systemctl --user disable --now hermes-gateway-l2-reviewer-fallback.service >/dev/null 2>&1 || true
rm -rf "$HOME/.hermes/profiles/l2-reviewer-fallback"

# No independent GBrain watcher: ticket_scout -> l2_learning_cycle owns convergence.
systemctl --user disable --now chitragupta-gbrain-sync.service >/dev/null 2>&1 || true
rm -f "$HOME/.config/systemd/user/chitragupta-gbrain-sync.service"
systemctl --user daemon-reload >/dev/null 2>&1 || true

if [[ "${1:-}" != "--no-restart" ]]; then
  for profile in "${ACTIVE_PROFILES[@]}"; do
    systemctl --user restart "hermes-gateway-$profile.service" 2>/dev/null || true
  done
fi

cat <<'EOF'

Deployed Chitragupta L2 on Hermes.
  harness:    Hermes
  lifecycle:  l2_pipeline_runtime.py
  evidence:   typed xstudio_l2
  retrieval:  direct Git Knowledge + reviewed learning lanes in isolated GBrain
  learning:   reviewed outcomes -> unverified candidates -> human promotion
  profiles:   dispatcher/legacy investigator + investigator worker + reviewer worker
EOF
