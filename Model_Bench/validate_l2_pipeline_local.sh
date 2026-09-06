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
  Model_Bench/xstudio_l2_tool_bridge.py
  Model_Bench/sync_l2_learning_corpus.py
  Model_Bench/l2_learning_curator.py
  Model_Bench/validate_action_capabilities.py
  Model_Bench/test_xstudio_l2_tools_plugin.py
  Model_Bench/test_xstudio_l2_learning_plugin.py
)

echo "== Python syntax =="
python3 -m py_compile "${PY_FILES[@]}"

echo "== Deterministic lifecycle contract tests =="
python3 Model_Bench/test_l2_pipeline_runtime.py

echo "== Typed investigation-tool contract tests =="
python3 Model_Bench/test_xstudio_l2_tools_plugin.py

echo "== Adaptive learning contract tests =="
python3 Model_Bench/test_xstudio_l2_learning_plugin.py

echo "== Future action capability registry =="
python3 Model_Bench/validate_action_capabilities.py

echo "== Knowledge/skill validation =="
python3 Model_Bench/validate_knowledge_manifest.py
python3 Model_Bench/test_kb_retrieval.py

echo "== zvec learning substrate =="
if ! command -v zg >/dev/null 2>&1; then
  echo "FAIL: zg missing. Install Node.js 22+ and: npm install -g @zvec/zvec-grep" >&2
  exit 1
fi
python3 Model_Bench/sync_l2_learning_corpus.py --vault "$LEARNING_VAULT" --check
zg status "$LEARNING_VAULT" --check-ready

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

Adaptive learning plane:
  shared vault:       $LEARNING_VAULT
  session recording:  ON (post_llm_call -> redacted unverified episodic Markdown)
  automatic prefetch: OFF by design
  explicit recall:    l2_recall with trust-scoped zvec hybrid search
  candidate learning: l2_lesson -> candidates only; separate promotion required
  mem0 provider:      unchanged

Future action plane:
  registry:           deploy/xstudio_action_capabilities.json
  global mode:        observe
  executable actions: none yet
  promotion path:     observe -> recommend -> shadow -> supervised -> autonomous

SQL deployment note:
  Knowledge/00_Hermes_L2_FULL_INSTALL.sql is the generated complete bundle.
  It already includes the current 25_ticket_dispatch_hardening and
  55_update_retry_hardening sources. Do not re-apply those merely because
  the numbered source files exist.

After deploying/regenerating the SQL bundle, run:
  Knowledge/98_pipeline_postflight.sql

For the next naturally arriving fresh ticket, verify:
  - database evidence uses xstudio_l2;
  - prior experience, when useful, uses explicit l2_recall rather than prompt injection;
  - a session file is written under the shared learning vault;
  - no generic zvec-memory prefetch block appears in the model context;
  - no terminal/interpreter/pyodbc/sqlcmd/package-install SQL transport reappears.
EOF
