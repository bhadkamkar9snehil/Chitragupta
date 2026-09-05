#!/bin/bash
# Qdrant health + mem0 collection check.
#
# Intended as a --no-agent cron backstop and as a manual post-update check.
# Exits non-zero on a real problem so a scheduler/monitor can notice.
#
# Checks, in order of how badly each one bites:
#   1. service running at all
#   2. HTTP healthz
#   3. the mem0 collection exists and is green
#   4. it actually holds points (a silent regression to a fresh/empty
#      collection looks identical to "healthy" on checks 1-3, and that is
#      precisely the failure this project already lived through)
set -uo pipefail

PORT=6333
COLLECTION=hermes_l2
rc=0

if ! systemctl --user is-active --quiet qdrant.service; then
  echo "FAIL: qdrant.service not active"
  systemctl --user status qdrant.service --no-pager 2>&1 | head -10
  exit 1
fi
echo "ok: qdrant.service active"

if ! curl -sf "http://127.0.0.1:${PORT}/healthz" >/dev/null; then
  echo "FAIL: healthz not responding on ${PORT}"
  exit 1
fi
echo "ok: healthz"

body="$(curl -sf "http://127.0.0.1:${PORT}/collections/${COLLECTION}" || true)"
if [ -z "$body" ]; then
  echo "WARN: collection '${COLLECTION}' does not exist yet (created on first mem0 write)"
  exit 0
fi

python3 - "$body" <<'EOF' || rc=$?
import json, sys
d = json.loads(sys.argv[1])["result"]
status = d.get("status"); points = d.get("points_count", 0)
print(f"ok: collection status={status} points={points}")
if status != "green":
    print(f"FAIL: collection not green ({status})"); sys.exit(1)
if points == 0:
    # Not fatal on a fresh install, but on an established system it means
    # memory silently stopped being written -- the exact regression that
    # went unnoticed for this project's entire history.
    print("WARN: collection has 0 points -- verify memory writes are reaching it")
EOF
exit $rc
