#!/bin/bash
# Mirror deployable WSL profile artifacts into the repository's deploy/ tree.
# Runtime learning data is deliberately NOT mirrored into Git: sessions, cases,
# candidates, promoted facts, action plans and outcome manifests are runtime data.
set -euo pipefail

SRC_HERMES=~/.hermes/profiles
DST=/mnt/c/Users/Admin/Documents/Office/AIHelpdesk/deploy

PROFILES="l2-investigator l2-investigator-primary l2-reviewer-primary l2-reviewer-fallback"
SKILLS="xstudio-l2-ticket-workflow xstudio-sap-api-investigation xstudio-sohar-heat-execution xstudio-quality-delay-workorder xstudio-sql-write-discipline xstudio-l2-draft-verifier"

mkdir -p "$DST/profiles" "$DST/skills/xstudio" "$DST/plugins"
rm -rf "$DST/profiles/l2-gemma"

for p in $PROFILES; do
  mkdir -p "$DST/profiles/$p"
  cp "$SRC_HERMES/$p/SOUL.md" "$DST/profiles/$p/SOUL.md" 2>/dev/null || true
  cp "$SRC_HERMES/$p/config.yaml" "$DST/profiles/$p/config.yaml" 2>/dev/null || true
  echo "mirrored $p SOUL.md + config.yaml"
done

skill_owner() {
  case "$1" in
    xstudio-l2-draft-verifier) echo "l2-reviewer-primary l2-reviewer-fallback" ;;
    *)                         echo "l2-investigator l2-investigator-primary" ;;
  esac
}

for s in $SKILLS; do
  mirrored=""
  for p in $(skill_owner "$s"); do
    if [ -f "$SRC_HERMES/$p/skills/xstudio/$s/SKILL.md" ]; then
      mkdir -p "$DST/skills/xstudio/$s"
      cp "$SRC_HERMES/$p/skills/xstudio/$s/SKILL.md" "$DST/skills/xstudio/$s/SKILL.md"
      echo "mirrored skill $s (from $p)"
      mirrored=1
      break
    fi
  done
  [ -n "$mirrored" ] || echo "WARNING: skill $s not found in an owning profile; repo copy left untouched"
done

for plugin in xstudio-l2-orchestrator xstudio-l2-trace xstudio-l2-tools xstudio-l2-learning xstudio-l2-actions; do
  cp "$SRC_HERMES/l2-investigator/plugins/$plugin/plugin.yaml" \
    "$DST/plugins/$plugin.plugin.yaml" 2>/dev/null || true
done

rm -f "$DST/cron_jobs.json"
hermes -p l2-investigator cron list > "$DST/cron_jobs.txt" 2>&1

echo "Done. Review $DST before committing, especially profile config.yaml files."
echo "Runtime learning vault intentionally excluded: ${CHITRAGUPTA_L2_LEARNING_VAULT:-$HOME/.hermes/l2-learning}"
