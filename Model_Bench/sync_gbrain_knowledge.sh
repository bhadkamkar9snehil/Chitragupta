#!/usr/bin/env bash
# GBrain holds one thing: the generated XBatch world (Knowledge/world), pages + typed links.
# Build it first on Windows:  python Model_Bench/build_process_world.py && python Model_Bench/build_world_pages.py
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
GBRAIN_BIN="${GBRAIN_BIN:-/home/snehil/.bun/bin/gbrain}"
export GBRAIN_HOME="${GBRAIN_HOME:-/home/snehil/.hermes/xstudio-gbrain}"
export PATH="$(dirname "$GBRAIN_BIN"):${PATH}"

test -x "$GBRAIN_BIN" || { echo "FATAL: GBrain binary not found: $GBRAIN_BIN" >&2; exit 1; }
test -f "$ROOT/Knowledge/world/links.jsonl" || { echo "FATAL: world not built (Knowledge/world/links.jsonl)" >&2; exit 1; }

# The world's page types and link verbs (writes, reads, calls, holds, records_to) live in a schema pack.
PACK_DIR="$GBRAIN_HOME/.gbrain/schema-packs/xbatch-world"
mkdir -p "$PACK_DIR"
cp "$ROOT/deploy/gbrain/xbatch-world/pack.yaml" "$PACK_DIR/pack.yaml"
"$GBRAIN_BIN" schema validate xbatch-world
"$GBRAIN_BIN" schema use xbatch-world

"$GBRAIN_BIN" sources current --source xstudio-knowledge --json
"$GBRAIN_BIN" sync --source xstudio-knowledge --repo "$ROOT" --src-subpath Knowledge/world --no-pull --no-extract --yes --json
"$GBRAIN_BIN" embed --stale --include-null-signature
python3 "$ROOT/Model_Bench/world_links.py"
python3 "$ROOT/Model_Bench/e2e/run_world.py"
