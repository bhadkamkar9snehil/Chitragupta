#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPTS_DIR="$HOME/.hermes/profiles/l2-investigator/scripts"
ACTIVE_PROFILES=(l2-investigator l2-investigator-primary l2-reviewer-primary)
WORKER_PROFILES=(l2-investigator-primary l2-reviewer-primary)
LEARNING_VAULT="${CHITRAGUPTA_L2_LEARNING_VAULT:-$HOME/.hermes/l2-learning}"
SCOUT_CRON_ID="${CHITRAGUPTA_L2_SCOUT_CRON_ID:-f1915c187f11}"

mkdir -p "$SCRIPTS_DIR"

# Runtime: one lifecycle script. With no args it defaults to scout for Hermes no-agent cron.
cp "$ROOT/Model_Bench/l2_pipeline_runtime.py" "$SCRIPTS_DIR/l2_pipeline_runtime.py"
cp "$ROOT/Model_Bench/sync_l2_outcomes.py" "$SCRIPTS_DIR/sync_l2_outcomes.py"
chmod +x "$SCRIPTS_DIR/l2_pipeline_runtime.py" "$SCRIPTS_DIR/sync_l2_outcomes.py"
cp "$ROOT/deploy/helpdesk_workflow_binding.json" "$SCRIPTS_DIR/helpdesk_workflow_binding.json"

# Final retired compatibility paths.
rm -f \
  "$SCRIPTS_DIR/kb_retrieval.py" \
  "$SCRIPTS_DIR/l2_gbrain.py" \
  "$SCRIPTS_DIR/ticket_scout.py" \
  "$SCRIPTS_DIR/sync_l2_gbrain.py" \
  "$SCRIPTS_DIR/l2_learning_cycle.py"

echo "== Governed reusable solutions =="
python3 "$ROOT/Model_Bench/sync_l2_approved_solutions.py" \
  --vault "$LEARNING_VAULT" \
  --policy "$ROOT/deploy/solution_export_policy.json" \
  || echo "WARNING: governed Solution sync found missing/drifted approvals"

echo "== Reviewed outcome history =="
python3 "$ROOT/Model_Bench/sync_l2_outcomes.py" --vault "$LEARNING_VAULT" \
  || echo "WARNING: outcome materialization reported errors; lifecycle deployment continues"

deploy_plugin() {
  local profile="$1"
  local src="$ROOT/Model_Bench/xstudio_l2_tools_plugin"
  local dst="$HOME/.hermes/profiles/$profile/plugins/xstudio-l2-tools"
  mkdir -p "$dst"
  cp "$src/__init__.py" "$dst/__init__.py"
  cp "$src/plugin.yaml" "$dst/plugin.yaml"
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
    "$HOME/.hermes/profiles/$profile/plugins/xstudio-l2-learning" \
    "$HOME/.hermes/profiles/$profile/skills/xstudio/xstudio-l2-ticket-workflow" \
    "$HOME/.hermes/profiles/$profile/skills/xstudio/xstudio-l2-draft-verifier" \
    "$HOME/.hermes/profiles/$profile/skills/xstudio/xstudio-sql-write-discipline"
done

# Dispatcher routes Kanban only. Workers get the single typed XStudio plugin.
rm -rf "$HOME/.hermes/profiles/l2-investigator/plugins/xstudio-l2-tools"
for profile in "${WORKER_PROFILES[@]}"; do
  deploy_plugin "$profile"
done

# Retire duplicate reviewer and old Chitragupta-owned GBrain scheduler.
systemctl --user disable --now hermes-gateway-l2-reviewer-fallback.service >/dev/null 2>&1 || true
rm -rf "$HOME/.hermes/profiles/l2-reviewer-fallback"
systemctl --user disable --now chitragupta-gbrain-sync.service >/dev/null 2>&1 || true
rm -f "$HOME/.config/systemd/user/chitragupta-gbrain-sync.service"
systemctl --user daemon-reload >/dev/null 2>&1 || true

# The old cron pointed at ticket_scout.py. Hermes script jobs cannot pass positional args,
# so l2_pipeline_runtime.py intentionally defaults to scout when invoked with no mode.
echo "== L2 scout cron =="
if ! hermes -p l2-investigator cron edit "$SCOUT_CRON_ID" \
  --name "L2 Ticket Scout" \
  --schedule "every 2m" \
  --deliver local \
  --script l2_pipeline_runtime.py \
  --no-agent; then
  echo "ERROR: could not migrate L2 scout cron $SCOUT_CRON_ID." >&2
  echo "Set CHITRAGUPTA_L2_SCOUT_CRON_ID to the current job id from:" >&2
  echo "  hermes -p l2-investigator cron list --all" >&2
  exit 1
fi

if [[ "${1:-}" != "--no-restart" ]]; then
  for profile in "${ACTIVE_PROFILES[@]}"; do
    systemctl --user restart "hermes-gateway-$profile.service" 2>/dev/null || true
  done
fi

cat <<'EOF'

Deployed Chitragupta L2 on Hermes.
  harness:    Hermes in WSL2
  lifecycle:  l2_pipeline_runtime.py (no args=scout; explicit reconcile/status)
  evidence:   typed xstudio_l2
  retrieval:  shared xstudio-gbrain through native Hermes MCP
  history:    reviewed outcomes + governed Solutions for GBrain ingestion
  schedule:   one 2-minute no-agent scout job
EOF
