#!/usr/bin/env bash
set -euo pipefail

# Operator-owned prerequisite installer for Chitragupta's adaptive learning plane.
# Workers never install dependencies. GBrain is installed only from its GitHub
# repository; the unrelated npm package named `gbrain` must never be used.

GBRAIN_REF="${CHITRAGUPTA_GBRAIN_REF:-5cfb84f1d3a809c70064c292c23db3d538d5c551}"
GBRAIN_VERSION="0.48.2.0"
PACKAGE="github:garrytan/gbrain#${GBRAIN_REF}"

if ! command -v bun >/dev/null 2>&1; then
  echo "ERROR: Bun is required for GBrain. Install Bun first: https://bun.sh" >&2
  exit 1
fi

echo "Installing pinned GBrain prerequisite: ${PACKAGE}"
bun install -g "$PACKAGE"
hash -r

if ! command -v gbrain >/dev/null 2>&1; then
  echo "ERROR: GBrain installation completed but gbrain is not on PATH." >&2
  exit 1
fi

VERSION_OUTPUT="$(gbrain --version 2>&1 || true)"
if [[ "$VERSION_OUTPUT" != *"$GBRAIN_VERSION"* ]]; then
  echo "ERROR: expected GBrain ${GBRAIN_VERSION}; got: ${VERSION_OUTPUT:-unknown}" >&2
  exit 1
fi

echo "gbrain path: $(command -v gbrain)"
echo "gbrain version: $VERSION_OUTPUT"

cat <<EOF

Pinned GBrain installed.
  ref: ${GBRAIN_REF}
  version: ${GBRAIN_VERSION}
  raw GBrain MCP: not exposed to L2 workers
  ambient/push context: not enabled
  isolated L2 brain: ~/.hermes/l2-gbrain (initialized by the harness on first sync)

The installer deliberately does not initialize or modify your default personal
GBrain. Chitragupta owns a separate GBRAIN_HOME and its learning sidecar creates
and synchronizes that brain deterministically.

Next:
  bash Model_Bench/deploy_l2_pipeline_runtime.sh
EOF
