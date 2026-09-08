#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
GBRAIN_BIN="${GBRAIN_BIN:-/home/snehil/.bun/bin/gbrain}"
export GBRAIN_HOME="${GBRAIN_HOME:-/home/snehil/.hermes/xstudio-gbrain}"
export PATH="$(dirname "$GBRAIN_BIN"):${PATH}"

test -x "$GBRAIN_BIN" || { echo "FATAL: GBrain binary not found: $GBRAIN_BIN" >&2; exit 1; }

"$GBRAIN_BIN" sources current --source xstudio-knowledge --json
"$GBRAIN_BIN" sync --source xstudio-knowledge --repo "$ROOT" --no-pull --no-extract --yes --json
"$GBRAIN_BIN" embed --stale --include-null-signature
python3 "$ROOT/Model_Bench/validate_gbrain_knowledge.py"
