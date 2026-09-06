#!/usr/bin/env bash
set -euo pipefail

# Operator-owned prerequisite installer for Chitragupta's adaptive learning plane.
# Workers never install dependencies. GBrain is installed only from its GitHub
# repository; the unrelated npm package named `gbrain` must never be used.

GBRAIN_REF="${CHITRAGUPTA_GBRAIN_REF:-5cfb84f1d3a809c70064c292c23db3d538d5c551}"
PACKAGE="github:garrytan/gbrain#${GBRAIN_REF}"

if ! command -v bun >/dev/null 2>&1; then
  echo "ERROR: Bun is required for GBrain. Install Bun first: https://bun.sh" >&2
  exit 1
fi

echo "Installing pinned GBrain prerequisite: ${PACKAGE}"
bun install -g "$PACKAGE"

if ! command -v gbrain >/dev/null 2>&1; then
  echo "ERROR: GBrain installation completed but gbrain is not on PATH." >&2
  exit 1
fi

echo "gbrain path: $(command -v gbrain)"
gbrain --version

# Chitragupta uses a deliberately tight retrieval shape for small local models.
# This affects GBrain search budgeting only; it does not enable ambient context.
if gbrain doctor --json >/dev/null 2>&1; then
  gbrain config set search.mode conservative >/dev/null
  echo "GBrain brain already initialized; search.mode=conservative"
else
  echo
  echo "GBrain CLI is installed but no healthy brain is configured yet."
  echo "Initialize once with one of these supported paths:"
  echo "  keyword/local baseline: gbrain init --pglite"
  echo "  LM Studio embeddings:   gbrain init --pglite --embedding-model lmstudio:<model-id> --embedding-dimensions <N>"
  echo "Then run: gbrain config set search.mode conservative"
fi

cat <<EOF

Pinned GBrain installed.
  ref: ${GBRAIN_REF}
  ambient/push context: not enabled by this installer
  Chitragupta model surface: remains l2_recall/l2_lesson, not raw GBrain MCP

Next:
  bash Model_Bench/deploy_l2_pipeline_runtime.sh
EOF
