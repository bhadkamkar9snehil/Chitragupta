#!/bin/bash
# Periodic commit+push. No-ops cleanly (exit 0, clear message) if no remote
# is configured yet, or if there's genuinely nothing to commit.
set -e
cd "$(dirname "$0")/.."

if ! git remote get-url origin >/dev/null 2>&1; then
  echo "No 'origin' remote configured yet -- run: git remote add origin <url>"
  exit 0
fi

# Refresh the WSL-only artifacts (SOUL.md/skills/config/cron) before diffing,
# so periodic syncs actually capture drift there too, not just Model_Bench.
if command -v wsl >/dev/null 2>&1; then
  : # invoked from Windows; the WSL-side mirror script runs separately via its own cron
fi

git add -A
if git diff --cached --quiet; then
  echo "Nothing to commit."
  exit 0
fi

git commit -m "auto: periodic sync $(date -u +%Y-%m-%dT%H:%M:%SZ)"
git push origin master
echo "Pushed."
