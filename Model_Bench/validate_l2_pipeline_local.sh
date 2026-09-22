#!/usr/bin/env bash
set -euo pipefail

export PATH="$HOME/.local/bin:$PATH"

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

MODE="fast"
case "${1:-}" in
  ""|--fast) MODE="fast" ;;
  --full) MODE="full" ;;
  --live-only) MODE="live-only" ;;
  -h|--help)
    cat <<'EOF'
Usage:
  bash Model_Bench/validate_l2_pipeline_local.sh             # fast local gate (default)
  bash Model_Bench/validate_l2_pipeline_local.sh --fast      # same as default
  bash Model_Bench/validate_l2_pipeline_local.sh --full      # fast gate + live SQL/Hermes checks
  bash Model_Bench/validate_l2_pipeline_local.sh --live-only # only live deployment/runtime checks

The fast gate is intended for the edit/test loop. Use --full before deployment,
after lifecycle changes, or when validating the live SQL/Kanban integration.
EOF
    exit 0
    ;;
  *)
    echo "Unknown argument: $1" >&2
    echo "Run with --help for supported modes." >&2
    exit 2
    ;;
esac

START_TOTAL=$SECONDS

section() {
  printf '\n== %s ==\n' "$1"
}

timed() {
  local label="$1"
  shift
  local start=$SECONDS
  "$@"
  local elapsed=$((SECONDS - start))
  printf '[timing] %s: %ss\n' "$label" "$elapsed"
}

PY_FILES=(
  Model_Bench/l2_pipeline_runtime.py
  Model_Bench/ticket_scout.py
  Model_Bench/reconcile_l2_pipeline.py
  Model_Bench/audit_kanban_completions.py
  Model_Bench/configure_helpdesk_workflow.py
  Model_Bench/kb_retrieval.py
  Model_Bench/jev_workflow_bridge.py
  Model_Bench/jev_trace_assessor.py
  Model_Bench/jev_post_resolution_curation.py
  Model_Bench/generate_readable_trace_summary.py
  Model_Bench/drain_and_summarize.py
  Model_Bench/jev/__init__.py
  Model_Bench/jev/policy.py
  Model_Bench/jev/client.py
  Model_Bench/jev/ticket_triage.py
  Model_Bench/jev/trace_assessment.py
  Model_Bench/jev/kb_applicability.py
  Model_Bench/jev/kb_curation.py
  Model_Bench/jev/evidence_plan.py
  Model_Bench/jev/investigation_assessment.py
  Model_Bench/jev/reviewer.py
  Model_Bench/jev/audit.py
  Model_Bench/model_scorecard.py
  Model_Bench/test_jev_fabric.py
  Model_Bench/test_kb_retrieval.py
  Model_Bench/patch_profile_config.py
  Model_Bench/patch_tool_search_off.py
  Model_Bench/xstudio_l2_orchestrator_plugin/__init__.py
  Model_Bench/xstudio_l2_tools_plugin/__init__.py
  Model_Bench/xstudio_l2_tool_bridge.py
  Model_Bench/test_xstudio_l2_tools_plugin.py
  Model_Bench/l2_gbrain.py
  Model_Bench/sync_l2_gbrain.py
  Model_Bench/l2_context_envelope.py
  Model_Bench/l2_context_delivery.py
  Model_Bench/l2_context_delivery_base.py
  Model_Bench/l2_context_delivery_assembly.py
  Model_Bench/l2_context_delivery_receipts.py
  Model_Bench/l2_context_retriever.py
  Model_Bench/l2_context_delivery_cli.py
  Model_Bench/xstudio_l2_learning_plugin/__init__.py
  Model_Bench/test_l2_gbrain.py
  Model_Bench/test_sync_l2_gbrain.py
  Model_Bench/test_l2_context_envelope.py
  Model_Bench/test_l2_context_delivery.py
  Model_Bench/test_l2_context_retriever.py
  Model_Bench/test_xstudio_l2_learning_plugin.py
)

run_fast_checks() {
  section "Secret hygiene"
  if git ls-files | grep -E '(^|/)[^/]*\.env$' >/dev/null; then
    echo "FAIL: tracked .env credential file found; credentials must come from process/service environment" >&2
    git ls-files | grep -E '(^|/)[^/]*\.env$' >&2
    exit 1
  fi
  echo "PASS: no tracked .env credential files"

  section "Python syntax"
  timed "py_compile" python3 -m py_compile "${PY_FILES[@]}"

  section "Deterministic lifecycle contract tests"
  timed "l2 runtime tests" python3 Model_Bench/test_l2_pipeline_runtime.py

  section "Typed investigation-tool contract tests"
  timed "typed-tool tests" python3 Model_Bench/test_xstudio_l2_tools_plugin.py

  section "TypeSafe Jev fabric contract tests"
  timed "Jev fabric tests" python3 Model_Bench/test_jev_fabric.py

  section "Knowledge/skill validation"
  timed "knowledge manifest" python3 Model_Bench/validate_knowledge_manifest.py
  timed "KB retrieval tests" python3 Model_Bench/test_kb_retrieval.py

  section "GBrain adapter / governed context-delivery contract tests"
  timed "gbrain/context tests" bash -c '
    cd Model_Bench && python3 -m unittest -v \
      test_l2_gbrain test_sync_l2_gbrain test_l2_context_envelope \
      test_l2_context_delivery test_l2_context_retriever test_xstudio_l2_learning_plugin
  '
}

run_live_checks() {
  section "Retired live-deployment guard"
  local deployed_scripts="$HOME/.hermes/profiles/l2-investigator/scripts"
  local retired_found=0
  local retired
  for retired in dispatch_l2_review.py kanban_forward_bridge.py nudge_unpublished_runs.py; do
    if [[ -e "$deployed_scripts/$retired" ]]; then
      echo "FAIL: retired script is still deployed live: $deployed_scripts/$retired" >&2
      retired_found=1
    fi
  done
  if [[ "$retired_found" -ne 0 ]]; then
    echo "Run: bash Model_Bench/deploy_l2_pipeline_runtime.sh" >&2
    exit 1
  fi
  echo "PASS: no known retired lifecycle scripts remain in the live scripts directory"

  section "Live workflow discovery (read-only)"
  timed "workflow discovery" python3 Model_Bench/configure_helpdesk_workflow.py

  section "Pipeline status (read-only)"
  timed "pipeline status" python3 Model_Bench/l2_pipeline_runtime.py status

  section "Reconcile preview (dry-run)"
  timed "reconcile dry-run" python3 Model_Bench/l2_pipeline_runtime.py reconcile --dry-run
}

case "$MODE" in
  fast)
    run_fast_checks
    ;;
  full)
    run_fast_checks
    run_live_checks
    ;;
  live-only)
    run_live_checks
    ;;
esac

echo
echo "VALIDATION COMPLETE: mode=$MODE total=$((SECONDS - START_TOTAL))s"

if [[ "$MODE" == "fast" ]]; then
  cat <<'EOF'

FAST LOCAL GATE PASSED.

This mode intentionally skips live SQL/Hermes workflow discovery, status, and
reconciliation. Run the full gate before deployment or after lifecycle changes:

  bash Model_Bench/validate_l2_pipeline_local.sh --full

If only the live integration needs to be rechecked after the fast gate already
passed, use:

  bash Model_Bench/validate_l2_pipeline_local.sh --live-only
EOF
else
  cat <<'EOF'

FULL/LIVE VALIDATION COMPLETE.

SQL deployment note:
  Knowledge/00_Hermes_L2_FULL_INSTALL.sql is the generated complete bundle.
  It already includes the current 25_ticket_dispatch_hardening and
  55_update_retry_hardening sources. Do not re-apply those merely because
  the numbered source files exist.

Jev deployment note:
  Jev is harness-owned. The local reviewer is the uncertainty/deep-reasoning
  fallback; execution depth is chosen by the Jev assessment and then bounded
  by deterministic runtime policy.

After deploying/regenerating the SQL bundle, run:
  Knowledge/98_pipeline_postflight.sql

Confirm deploy/helpdesk_workflow_binding.json still matches live workflow values.
Do not guess replacement status names.

For the next naturally arriving fresh ticket, verify its trace uses xstudio_l2
for database/schema/ticket evidence and does not recreate SQL transport through
terminal, an interpreter, pyodbc/sqlcmd, or package installation.
EOF
fi
