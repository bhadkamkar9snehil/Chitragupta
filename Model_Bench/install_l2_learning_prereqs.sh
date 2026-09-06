#!/usr/bin/env bash
set -euo pipefail

# Operator-only prerequisite installer for the adaptive L2 learning plane.
# This is deliberately NOT called from an agent investigation or implicitly from
# deployment. Runtime workers are forbidden from installing dependencies.

ZVEC_GREP_VERSION="${ZVEC_GREP_VERSION:-0.2.1}"
PACKAGE="@zvec/zvec-grep@${ZVEC_GREP_VERSION}"

if ! command -v node >/dev/null 2>&1; then
  echo "ERROR: Node.js is not installed. Install Node.js 22+ first." >&2
  exit 1
fi
if ! command -v npm >/dev/null 2>&1; then
  echo "ERROR: npm is not installed." >&2
  exit 1
fi

NODE_VERSION="$(node --version | sed 's/^v//')"
NODE_MAJOR="${NODE_VERSION%%.*}"
if [[ ! "$NODE_MAJOR" =~ ^[0-9]+$ ]] || (( NODE_MAJOR < 22 )); then
  echo "ERROR: Node.js 22+ is required; found v${NODE_VERSION}." >&2
  exit 1
fi

echo "Installing pinned local retrieval dependency: ${PACKAGE}"
npm install -g "$PACKAGE"

if ! command -v zg >/dev/null 2>&1; then
  echo "ERROR: npm completed but zg is not on PATH." >&2
  exit 1
fi

echo "zg path: $(command -v zg)"
zg --version || true

echo
cat <<'EOF'
Prerequisite installed.

The first corpus index will download the configured local embedding model into
zvec-grep's local model cache. No remote embedding provider is configured by this
script and no Chitragupta data is uploaded.

Next:
  bash Model_Bench/deploy_l2_pipeline_runtime.sh
EOF
