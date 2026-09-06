#!/usr/bin/env bash
set -euo pipefail

# Deploy the deterministic L2 lifecycle, typed XStudio evidence surface, and the
# adaptive learning/experience plane into the Hermes profiles.
#
# Learning design:
#   * record completed L2 turns -> shared redacted sessions vault
#   * explicit l2_recall -> zvec BM25+vector hybrid search with trust scopes
#   * l2_lesson -> unverified candidate only
#   * NO generic automatic prefetch
#   * mem0 remains independent and is not replaced by this deploy

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

# Only copy scripts that are valid from the deployed profile location. Corpus
# sync/benchmark/registry validation intentionally stay repo-side because their
# source-of-truth inputs live in the Git checkout.
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
  l2_learning_curator.py
 do
  cp "$ROOT/Model_Bench/$f" "$SCRIPTS_DIR/$f"
 done
chmod +x "$SCRIPTS_DIR"/*.py

# Windows-side typed SQL bridge stays in the repo because it imports the repo's
# Hermes_Orchestrator and is executed by trusted harness code only.
test -f "$ROOT/Model_Bench/xstudio_l2_tool_bridge.py" \
  || { echo "FATAL: Model_Bench/xstudio_l2_tool_bridge.py is missing" >&2; exit 1; }

cp "$ROOT/deploy/helpdesk_workflow_binding.json" "$SCRIPTS_DIR/helpdesk_workflow_binding.json"
cp "$ROOT/deploy/xstudio_action_capabilities.json" "$SCRIPTS_DIR/xstudio_action_capabilities.json"

# zvec is a deliberate local dependency. Do not let the LLM install it during a
# ticket; operators install the pinned prerequisite once and deployment verifies it.
if ! command -v zg >/dev/null 2>&1; then
  cat >&2 <<'EOF'
FATAL: zvec-grep (`zg`) is required by the adaptive-learning branch but is not on PATH.
Run the explicit operator prerequisite installer:
  bash Model_Bench/install_l2_learning_prereqs.sh
Then rerun this deployment.
EOF
  exit 1
fi

# Mirror canonical Git/skill knowledge into the shared learning vault and refresh
# the disposable hybrid index. Sessions/facts/candidates are never deleted by this.
echo "== Learning corpus sync =="
python3 "$ROOT/Model_Bench/sync_l2_learning_corpus.py" --vault "$LEARNING_VAULT"

# Keep the optional shared daemon warm. `zg query --mode auto` still works direct
# if the daemon cannot start, so daemon failure is not a correctness failure.
if [[ "${CHITRAGUPTA_ZVEC_SERVER:-1}" != "0" ]]; then
  zg server on >/dev/null 2>&1 || echo "WARNING: zg server did not start; direct mode remains available"
fi

# Deploy plugins to each profile. xstudio-l2-learning is a general plugin, not a
# MemoryProvider, so this does not switch or rewrite the active mem0 provider.
deploy_plugins() {
  local profile="$1" plugin src dir
  for plugin in xstudio-l2-orchestrator xstudio-l2-tools xstudio-l2-learning; do
    case "$plugin" in
      xstudio-l2-orchestrator) src="$ROOT/Model_Bench/xstudio_l2_orchestrator_plugin" ;;
      xstudio-l2-tools)        src="$ROOT/Model_Bench/xstudio_l2_tools_plugin" ;;
      xstudio-l2-learning)     src="$ROOT/Model_Bench/xstudio_l2_learning_plugin" ;;
    esac
    dir="$HOME/.hermes/profiles/$profile/plugins/$plugin"
    mkdir -p "$dir"
    cp "$src/__init__.py" "$dir/__init__.py"
    cp "$src/plugin.yaml" "$dir/plugin.yaml"
  done
}

# Toolset names must be visible to shared plugin discovery, not only to a
# profile-local plugin copy.
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

echo "== Shared plugin install (required for direct toolset discovery) =="
install_shared_plugin_for_discovery xstudio-l2-tools "$ROOT/Model_Bench/xstudio_l2_tools_plugin"
install_shared_plugin_for_discovery xstudio-l2-learning "$ROOT/Model_Bench/xstudio_l2_learning_plugin"

echo "== Profile config (idempotent, additive) =="
for profile in "${ACTIVE_PROFILES[@]}"; do
  config="$HOME/.hermes/profiles/$profile/config.yaml"
  python3 "$ROOT/Model_Bench/patch_profile_config.py" "$config"
  # Small local models get both typed toolsets directly. Do not make them
  # discover the tools through deferred tool_search.
  python3 "$ROOT/Model_Bench/patch_tool_search_off.py" "$config"
done

# Root config controls shared plugin discovery. The patcher can bootstrap a
# missing root plugins.enabled block without YAML round-tripping comments. It
# never changes memory.provider.
echo "== Root config (plugin discovery) =="
python3 "$ROOT/Model_Bench/patch_profile_config.py" --enable-plugin-only "$HOME/.hermes/config.yaml"

if [[ "${1:-}" != "--no-restart" ]]; then
  for profile in "${ACTIVE_PROFILES[@]}"; do
    systemctl --user restart "hermes-gateway-$profile.service" 2>/dev/null || true
  done
fi

echo
echo "Deployed deterministic L2 lifecycle + typed evidence + adaptive learning plane."
echo "  evidence toolset: xstudio_l2"
echo "  learning toolset: l2_learning (l2_recall, l2_lesson)"
echo "  learning vault:   $LEARNING_VAULT"
echo "  session record:   ON (redacted, unverified episodic)"
echo "  auto prefetch:    OFF by design"
echo "  mem0 provider:    unchanged"
echo "  action registry:  observe-only unless individual capabilities are added/promoted"
echo "Next: bash $ROOT/Model_Bench/validate_l2_pipeline_local.sh"
