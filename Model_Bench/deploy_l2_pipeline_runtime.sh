#!/usr/bin/env bash
set -euo pipefail

# Deploy the repo's deterministic L2 pipeline runtime AND the typed XStudio
# investigation harness into the Hermes profile script/plugin/skill locations.
# Run from the Chitragupta repo under WSL. Safe to run repeatedly.
#
# The typed-tool half of this deployment exists because of Ticket_424/Ticket_441:
# the lifecycle was fine, but the investigator rebuilt SQL transport by hand
# (`python3 /mnt/c/Python314/python.exe ...`, then `pip install pyodbc`) and
# burned its whole context window. Transport is now harness-owned behind the
# `xstudio_l2` tool, and the retired shell paths are blocked.

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPTS_DIR="$HOME/.hermes/profiles/l2-investigator/scripts"
ACTIVE_PROFILES=(l2-investigator l2-investigator-primary l2-reviewer-primary l2-reviewer-fallback)
INVESTIGATOR_PROFILES=(l2-investigator l2-investigator-primary)
REVIEWER_PROFILES=(l2-reviewer-primary l2-reviewer-fallback)

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

# The typed-tool bridge is invoked by the plugin at its REPO path (it needs the
# Windows interpreter and the repo's Hermes_Orchestrator module), so it is not
# copied into the profile. Fail loudly if it is missing rather than deploying a
# plugin whose transport cannot start.
test -f "$ROOT/Model_Bench/xstudio_l2_tool_bridge.py" \
  || { echo "FATAL: Model_Bench/xstudio_l2_tool_bridge.py is missing" >&2; exit 1; }

# Keep the workflow binding beside the deployed scripts as a fallback. The
# runtime also reads the canonical repo copy directly.
cp "$ROOT/deploy/helpdesk_workflow_binding.json" "$SCRIPTS_DIR/helpdesk_workflow_binding.json"

# Deploy both observer plugins to every active role. The orchestrator plugin
# only triggers reconciliation; the tools plugin registers `xstudio_l2` and
# enforces the execution guard. Correctness never depends on the event hook,
# because ticket_scout runs the same reconciler before every new claim.
deploy_plugins() {
  local profile="$1" plugin src dir
  for plugin in xstudio-l2-orchestrator xstudio-l2-tools; do
    if [[ "$plugin" == "xstudio-l2-orchestrator" ]]; then
      src="$ROOT/Model_Bench/xstudio_l2_orchestrator_plugin"
    else
      src="$ROOT/Model_Bench/xstudio_l2_tools_plugin"
    fi
    dir="$HOME/.hermes/profiles/$profile/plugins/$plugin"
    mkdir -p "$dir"
    cp "$src/__init__.py" "$dir/__init__.py"
    cp "$src/plugin.yaml" "$dir/plugin.yaml"
  done
}

# A profile-local plugin copy is enough for HOOKS to fire, but NOT for a plugin
# to contribute a TOOLSET. Toolset gating (hermes_cli/tools_config._get_platform_tools)
# only accepts a toolset name that plugin discovery already knows about, and that
# discovery scans the SHARED plugins directory using the ROOT config's
# plugins.enabled list. A tools plugin installed only under a profile therefore
# loads its hooks, registers its tool, and still has the toolset silently dropped
# from every session -- which is exactly why the first typed-harness ticket saw
# its terminal fallback blocked but never got `xstudio_l2` as an alternative.
# xstudio-l2-trace was already installed in both places for this same reason.
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

# Enable the tools plugin/toolset and the approval-deny backstop in each live
# profile config. This is a targeted, idempotent, comment-preserving edit -- it
# never rewrites dispatch settings, API ports, model choice, or credentials.
echo "== Shared plugin install (required for toolset discovery) =="
install_shared_plugin_for_discovery xstudio-l2-tools "$ROOT/Model_Bench/xstudio_l2_tools_plugin"
echo "installed xstudio-l2-tools into $HOME/.hermes/plugins for toolset discovery"

echo "== Profile config (idempotent, additive) =="
for profile in "${ACTIVE_PROFILES[@]}"; do
  config="$HOME/.hermes/profiles/$profile/config.yaml"
  if [[ -f "$config" ]]; then
    python3 "$ROOT/Model_Bench/patch_profile_config.py" "$config"
    # Never make the worker DISCOVER xstudio_l2. Deferred tool-search is a fine
    # trade for a large model and a trap for the 9B local one: on Ticket_360 the
    # worker searched, found the tool, said it would use it, then completed with
    # "database access unavailable" without ever calling it.
    python3 "$ROOT/Model_Bench/patch_tool_search_off.py" "$config"
  else
    echo "WARNING: $config not found; skipped"
  fi
done

# The root config drives plugin discovery, which is what makes `xstudio_l2` a
# recognised toolset name instead of an unknown one that gets filtered out.
echo "== Root config (plugin discovery) =="
python3 "$ROOT/Model_Bench/patch_profile_config.py" --enable-plugin-only "$HOME/.hermes/config.yaml"

if [[ "${1:-}" != "--no-restart" ]]; then
  for profile in "${ACTIVE_PROFILES[@]}"; do
    systemctl --user restart "hermes-gateway-$profile.service" 2>/dev/null || true
  done
fi

echo
echo "Deployed deterministic L2 lifecycle + typed XStudio investigation harness."
echo "Typed tool: xstudio_l2. Retired terminal transports (Hermes_Orchestrator.py,"
echo "Windows Python, sqlcmd, pyodbc, pip) are blocked by plugin hook + approvals.deny."
echo "Next: bash $ROOT/Model_Bench/validate_l2_pipeline_local.sh"
