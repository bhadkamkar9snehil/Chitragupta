#!/usr/bin/env bash
set -euo pipefail

# Deploy the repo's deterministic L2 pipeline runtime into the Hermes profile
# script/plugin/skill locations. Run from the Chitragupta repo under WSL.

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPTS_DIR="$HOME/.hermes/profiles/l2-investigator/scripts"
ACTIVE_PROFILES=(l2-investigator l2-investigator-primary l2-reviewer-primary l2-reviewer-fallback)

mkdir -p "$SCRIPTS_DIR"

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
  drain_and_summarize.py
 do
  cp "$ROOT/Model_Bench/$f" "$SCRIPTS_DIR/$f"
 done

chmod +x "$SCRIPTS_DIR"/*.py

# Keep the workflow binding beside the deployed scripts as a fallback. The
# runtime also reads the canonical repo copy directly.
cp "$ROOT/deploy/helpdesk_workflow_binding.json" "$SCRIPTS_DIR/helpdesk_workflow_binding.json"

# Deploy the observer plugin to every active role. The plugin only triggers
# reconciliation; correctness does not depend on it because ticket_scout runs
# the same reconciler before every new claim.
for profile in "${ACTIVE_PROFILES[@]}"; do
  plugin_dir="$HOME/.hermes/profiles/$profile/plugins/xstudio-l2-orchestrator"
  mkdir -p "$plugin_dir"
  cp "$ROOT/Model_Bench/xstudio_l2_orchestrator_plugin/__init__.py" "$plugin_dir/__init__.py"
  cp "$ROOT/Model_Bench/xstudio_l2_orchestrator_plugin/plugin.yaml" "$plugin_dir/plugin.yaml"

  for skill in xstudio-l2-ticket-workflow xstudio-l2-draft-verifier; do
    src="$ROOT/deploy/skills/xstudio/$skill/SKILL.md"
    dst="$HOME/.hermes/profiles/$profile/skills/xstudio/$skill"
    if [[ -f "$src" ]]; then
      mkdir -p "$dst"
      cp "$src" "$dst/SKILL.md"
    fi
  done
 done

if [[ "${1:-}" != "--no-restart" ]]; then
  for profile in "${ACTIVE_PROFILES[@]}"; do
    systemctl --user restart "hermes-gateway-$profile.service" 2>/dev/null || true
  done
fi

echo "Deployed deterministic L2 pipeline runtime."
echo "Next: populate deploy/helpdesk_workflow_binding.json from live --discover-workflow before allowing RESOLUTION publication."
echo "Then run: python3 $SCRIPTS_DIR/l2_pipeline_runtime.py status"
