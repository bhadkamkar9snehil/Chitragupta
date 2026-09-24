#!/usr/bin/env bash
set -euo pipefail

export PATH="$HOME/.local/bin:$PATH"

# Deploy the repo's deterministic L2 pipeline runtime AND the typed XStudio
# investigation harness into the Hermes profile script/plugin/skill locations.
# Run from the Chitragupta repo under WSL. Safe to run repeatedly.
#
# The typed-tool half of this deployment exists because of Ticket_424/Ticket_441:
# the lifecycle was fine, but the investigator rebuilt SQL transport by hand
# (`python3 /mnt/c/Python314/python.exe ...`, then `pip install pyodbc`) and
# burned its whole context window. Transport is now harness-owned behind the
# named `xstudio_*` tools in the `xstudio_l2` toolset, and the retired shell paths are blocked.

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
HERMES_PYTHON="$HOME/.hermes/hermes-agent/venv/bin/python"
SCRIPTS_DIR="$HOME/.hermes/profiles/l2-investigator/scripts"
# l2-investigator runs no worker sessions; its gateway hosts the scout/audit cron jobs.
ACTIVE_PROFILES=(l2-jev-investigator l2-investigator l2-reviewer-primary)
INVESTIGATOR_PROFILES=(l2-jev-investigator l2-investigator)
REVIEWER_PROFILES=(l2-reviewer-primary)
RETIRED_DEPLOYED_SCRIPTS=(dispatch_l2_review.py kanban_forward_bridge.py nudge_unpublished_runs.py)
RETIRED_PLUGIN_DIRS=(xstudio-l2-jev)

test -x "$HERMES_PYTHON" \
  || { echo "FATAL: Hermes Python not found at $HERMES_PYTHON" >&2; exit 1; }
odbcinst -q -d -n "ODBC Driver 18 for SQL Server" >/dev/null 2>&1 \
  || { echo "FATAL: ODBC Driver 18 for SQL Server is not installed in WSL" >&2; exit 1; }
if ! "$HERMES_PYTHON" -c 'import pyodbc' >/dev/null 2>&1; then
  "$HERMES_PYTHON" -m pip install pyodbc
fi

echo "== GBrain knowledge sync and readiness =="
bash "$ROOT/Model_Bench/sync_gbrain_knowledge.sh"
# Seed the new Jev-first Hermes profile from the repo on first deployment.
JEV_PROFILE_DIR="$HOME/.hermes/profiles/l2-jev-investigator"
mkdir -p "$JEV_PROFILE_DIR"
if [[ ! -f "$JEV_PROFILE_DIR/config.yaml" ]]; then
  cp "$ROOT/deploy/profiles/l2-jev-investigator/config.yaml" "$JEV_PROFILE_DIR/config.yaml"
fi

# Repo deletion is not deployment deletion. Earlier cleanup removed these files
# from Git but left old copies under ~/.hermes/profiles/.../scripts, which made
# the live machine look like it still had two orchestration systems. Remove the
# known retired entrypoints explicitly on every deploy so repo and live state
# converge idempotently.
for retired in "${RETIRED_DEPLOYED_SCRIPTS[@]}"; do
  if [[ -e "$SCRIPTS_DIR/$retired" ]]; then
    rm -f "$SCRIPTS_DIR/$retired"
    echo "removed retired deployed script: $retired"
  fi
done

for profile in "${ACTIVE_PROFILES[@]}"; do
  for retired_plugin in "${RETIRED_PLUGIN_DIRS[@]}"; do
    stale="$HOME/.hermes/profiles/$profile/plugins/$retired_plugin"
    if [[ -d "$stale" ]]; then
      rm -rf "$stale"
      echo "removed retired profile plugin: $stale"
    fi
  done
done
for retired_plugin in "${RETIRED_PLUGIN_DIRS[@]}"; do
  stale="$HOME/.hermes/plugins/$retired_plugin"
  if [[ -d "$stale" ]]; then
    rm -rf "$stale"
    echo "removed retired shared plugin: $stale"
  fi
done

RETIRED_SCRIPTS=(
  kanban_approval_publisher.py
  kanban_reject_bridge.py
  repair_incomplete_completions.py
  enforce_publish_safety_net.py
  xbatch_world.py
)
for retired_script in "${RETIRED_SCRIPTS[@]}"; do
  for profile in "${ACTIVE_PROFILES[@]}"; do
    stale="$HOME/.hermes/profiles/$profile/scripts/$retired_script"
    if [[ -f "$stale" ]]; then
      rm -f "$stale"
      echo "removed retired script: $stale"
    fi
  done
done

for profile in "${ACTIVE_PROFILES[@]}"; do
  scripts_dir="$HOME/.hermes/profiles/$profile/scripts"
  mkdir -p "$scripts_dir"
  for f in \
    l2_pipeline_runtime.py \
    ticket_scout.py \
    reconcile_l2_pipeline.py \
    audit_kanban_completions.py \
    run_coalesced.py \
    drain_and_summarize.py \
    l2_calltrace.py \
    l2_gbrain.py \
    direct_answer.py
  do
    cp "$ROOT/Model_Bench/$f" "$scripts_dir/$f"
  done
  chmod +x "$scripts_dir"/*.py
  cp "$ROOT/deploy/helpdesk_workflow_binding.json" "$scripts_dir/helpdesk_workflow_binding.json"
  knowledge_dir="$scripts_dir/knowledge"
  mkdir -p "$knowledge_dir"
  rm -f "$knowledge_dir/xstudio_semantic_atlas.json" "$knowledge_dir/xbatch_investigation_recipes.json"
  cp "$ROOT/Knowledge/manifest.json" "$knowledge_dir/manifest.json"
done

# The typed-tool bridge is invoked by the plugin at its repo path using the
# current Hermes WSL Python and its native ODBC driver, so it is not
# copied into the profile. Fail loudly if it is missing rather than deploying a
# plugin whose transport cannot start.
test -f "$ROOT/Model_Bench/xstudio_l2_tool_bridge.py" \
  || { echo "FATAL: Model_Bench/xstudio_l2_tool_bridge.py is missing" >&2; exit 1; }

# Deploy both observer plugins to every active role. The orchestrator plugin
# only triggers reconciliation; the tools plugin registers named `xstudio_*`
# tools in the `xstudio_l2` toolset and
# enforces the execution guard. Correctness never depends on the event hook,
# because ticket_scout runs the same reconciler before every new claim.
# KB retrieval executes directly from the repo path. Its TypeSafe Jev helper is
# likewise repo-local: there is no runtime package installation or profile copy.
test -f "$ROOT/Model_Bench/kb_retrieval.py" \
  || { echo "FATAL: Model_Bench/kb_retrieval.py is missing" >&2; exit 1; }
test -f "$ROOT/Model_Bench/jev_workflow_bridge.py" \
  || { echo "FATAL: Model_Bench/jev_workflow_bridge.py is missing" >&2; exit 1; }
test -f "$ROOT/Model_Bench/jev_trace_assessor.py" \
  || { echo "FATAL: Model_Bench/jev_trace_assessor.py is missing" >&2; exit 1; }
test -f "$ROOT/Model_Bench/jev_post_resolution_curation.py" \
  || { echo "FATAL: Model_Bench/jev_post_resolution_curation.py is missing" >&2; exit 1; }
test -f "$ROOT/Model_Bench/jev/client.py" \
  || { echo "FATAL: Model_Bench/jev fabric is missing" >&2; exit 1; }

# Keep the workflow binding beside the deployed scripts as a fallback. The
# runtime also reads the canonical repo copy directly.
cp "$ROOT/deploy/helpdesk_workflow_binding.json" "$SCRIPTS_DIR/helpdesk_workflow_binding.json"

# Deploy the orchestrator, typed-tools, and trace observer plugins to every
# active role. Trace remains a cheap local observer; all Jev network work runs
# later from the drain pipeline, never inside observer hooks. Correctness never
# depends on an event hook because ticket_scout reconciles before every claim.
deploy_plugins() {
  local profile="$1" plugin src dir
  for plugin in xstudio-l2-orchestrator xstudio-l2-tools xstudio-l2-trace xstudio-l2-learning; do
    if [[ "$plugin" == "xstudio-l2-orchestrator" ]]; then
      src="$ROOT/Model_Bench/xstudio_l2_orchestrator_plugin"
    elif [[ "$plugin" == "xstudio-l2-tools" ]]; then
      src="$ROOT/Model_Bench/xstudio_l2_tools_plugin"
    elif [[ "$plugin" == "xstudio-l2-trace" ]]; then
      src="$ROOT/Model_Bench/xstudio_l2_trace_plugin"
    else
      src="$ROOT/Model_Bench/xstudio_l2_learning_plugin"
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
# its terminal fallback blocked but never got a typed XStudio tool as an alternative.
# xstudio-l2-trace was already installed in both places for this same reason.
# from every session -- exactly what the first typed-harness live run exposed.
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
  rm -rf "$HOME/.hermes/profiles/$profile/skills/xstudio/xstudio-l2-ticket-workflow"
  for skill in xstudio-l2-draft-verifier xstudio-sql-write-discipline; do
    copy_skill "$profile" "$skill"
  done
done

# Enable the tools plugin/toolset and the approval-deny backstop in each live
# profile config. This is a targeted, idempotent, comment-preserving edit -- it
# never rewrites dispatch settings, API ports, model choice, or credentials.
echo "== Shared plugin install (required for toolset discovery) =="
install_shared_plugin_for_discovery xstudio-l2-tools "$ROOT/Model_Bench/xstudio_l2_tools_plugin"
install_shared_plugin_for_discovery xstudio-l2-trace "$ROOT/Model_Bench/xstudio_l2_trace_plugin"
echo "installed xstudio-l2-tools into $HOME/.hermes/plugins for toolset discovery"
install_shared_plugin_for_discovery xstudio-l2-learning "$ROOT/Model_Bench/xstudio_l2_learning_plugin"
echo "installed xstudio-l2-learning into $HOME/.hermes/plugins for toolset discovery"

echo "== Profile config (idempotent, additive) =="
for profile in "${ACTIVE_PROFILES[@]}"; do
  config="$HOME/.hermes/profiles/$profile/config.yaml"
  if [[ -f "$config" ]]; then
    # Converge configs after retiring the worker-facing Jev plugin/toolset.
    # Remove only the exact list entries we previously owned.
    sed -i \
      -e '/^[[:space:]]*- xstudio-l2-jev[[:space:]]*$/d' \
      -e '/^[[:space:]]*- xstudio_jev[[:space:]]*$/d' \
      "$config"
    python3 "$ROOT/Model_Bench/patch_profile_config.py" "$config"
    # Never make the worker DISCOVER xstudio_l2. Deferred tool-search is a fine
    # trade for a large model and a trap for the 9B local one: on Ticket_360 the
    # worker searched, found the tool, said it would use it, then completed with
    # "database access unavailable" without ever calling it.
    python3 "$ROOT/Model_Bench/patch_tool_search_off.py" "$config"
    if [[ "$profile" == "l2-reviewer-primary" || "$profile" == "l2-jev-investigator" ]]; then
      python3 "$ROOT/Model_Bench/patch_l2_worker_budget.py" "$config"
    fi
  else
    echo "WARNING: $config not found; skipped"
  fi
done

# The root config drives plugin discovery, which is what makes the `xstudio_l2`
# recognised toolset name instead of an unknown one that gets filtered out.
echo "== Root config (plugin discovery) =="
sed -i \
  -e '/^[[:space:]]*- xstudio-l2-jev[[:space:]]*$/d' \
  -e '/^[[:space:]]*- xstudio_jev[[:space:]]*$/d' \
  "$HOME/.hermes/config.yaml"
python3 "$ROOT/Model_Bench/patch_profile_config.py" --enable-plugin-only "$HOME/.hermes/config.yaml"

if [[ "${1:-}" != "--no-restart" ]]; then
  for profile in "${ACTIVE_PROFILES[@]}"; do
    systemctl --user restart "hermes-gateway-$profile.service" 2>/dev/null || true
  done
fi

# Post-deploy preflight: the exact dependency gate the scout runs before every claim.
# Twice on 2026-09-23 a deploy passed every test yet stopped all claims; this catches it.
if ! (set -a; source <(tr -d '\r' < "$HOME/.hermes/profiles/l2-jev-investigator/.env"); set +a
      "$HERMES_PYTHON" "$HOME/.hermes/profiles/l2-investigator/scripts/l2_pipeline_runtime.py" preflight); then
  echo "FATAL: post-deploy preflight failed -- the scout would pause all claims. Fix before leaving it." >&2
  exit 1
fi
echo "Post-deploy preflight OK: the scout can claim."

echo
echo "Deployed deterministic L2 lifecycle + typed XStudio investigation harness."
echo "Typed tools: named xstudio_* tools in xstudio_l2. SQL transport runs natively in WSL behind the harness."
echo "Model-driven terminal transports (Hermes_Orchestrator.py, Windows Python,"
echo "sqlcmd, pyodbc, pip) remain blocked by plugin hook + approvals.deny."
echo "Deployed deterministic L2 lifecycle + typed XStudio harness + trace observer + Jev System-One fabric."
echo "Typed worker tool: xstudio_l2. Jev planning/review remains harness-owned. Retired terminal transports (Hermes_Orchestrator.py,"
echo "Windows Python, sqlcmd, pyodbc, pip) are blocked by plugin hook + approvals.deny."
echo "Known retired deployed lifecycle scripts are removed on every deploy."
echo "Next: bash $ROOT/Model_Bench/validate_l2_pipeline_local.sh --full"
