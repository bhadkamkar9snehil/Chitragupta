#!/bin/bash
# Mirrors everything that only exists inside WSL profile directories into
# the Windows-side repo tree (deploy/), so the repo is actually a complete,
# portable record of the system -- not just the Windows-visible half of it.
# Re-run this any time SOUL.md/skills/config.yaml/plugins change, before a
# commit.
set -e
SRC_HERMES=~/.hermes/profiles
DST=/mnt/c/Users/Admin/Documents/Office/AIHelpdesk/deploy

# 2026-09-05: l2-eval-investigator (the live investigator profile since
# the qwopus3.5-9b-coder swap) was missing from this list -- confirmed
# real gap: deploy/profiles/ had no l2-eval-investigator/ dir at all,
# meaning a fresh install from this repo could not reconstruct the
# actual current topology. l2-gemma kept even though retired -- it's
# still a real historical profile dir, not worth a special case here.
PROFILES="l2-investigator l2-investigator-primary l2-gemma l2-reviewer-primary l2-reviewer-fallback"
SKILLS="xstudio-l2-ticket-workflow xstudio-sap-api-investigation xstudio-sohar-heat-execution xstudio-quality-delay-workorder xstudio-sql-write-discipline xstudio-l2-draft-verifier"

mkdir -p "$DST"

for p in $PROFILES; do
  mkdir -p "$DST/profiles/$p"
  cp "$SRC_HERMES/$p/SOUL.md" "$DST/profiles/$p/SOUL.md" 2>/dev/null || true
  cp "$SRC_HERMES/$p/config.yaml" "$DST/profiles/$p/config.yaml" 2>/dev/null || true
  echo "mirrored $p SOUL.md + config.yaml"
done

mkdir -p "$DST/skills/xstudio"
for s in $SKILLS; do
  # Skills are identical across profiles that carry them -- take the first
  # profile dir that actually has this skill.
  for p in $PROFILES; do
    if [ -f "$SRC_HERMES/$p/skills/xstudio/$s/SKILL.md" ]; then
      mkdir -p "$DST/skills/xstudio/$s"
      cp "$SRC_HERMES/$p/skills/xstudio/$s/SKILL.md" "$DST/skills/xstudio/$s/SKILL.md"
      echo "mirrored skill $s (from $p)"
      break
    fi
  done
done

mkdir -p "$DST/plugins"
cp -r ~/.hermes/profiles/l2-investigator/plugins/xstudio-l2-orchestrator/plugin.yaml "$DST/plugins/xstudio-l2-orchestrator.plugin.yaml" 2>/dev/null || true
cp -r ~/.hermes/profiles/l2-investigator/plugins/xstudio-l2-trace/plugin.yaml "$DST/plugins/xstudio-l2-trace.plugin.yaml" 2>/dev/null || true

# Cron job definitions -- documentation only (no secrets in these), so a
# fresh install can recreate the same schedule instead of guessing it.
# 2026-09-05: `cron list --json` is not a real flag on this hermes version
# at all (confirmed: argparse rejects it with "unrecognized arguments:
# --json", exit 0, empty stdout) -- the old `--json ... || ... .txt` form
# never actually fell through to the .txt branch because the command
# "succeeded" (exit 0) with empty output, so cron_jobs.json shipped as a
# permanently empty, silently-misleading file and cron_jobs.txt went
# stale. There is no JSON form; .txt is the only real output this command
# has. Delete any old cron_jobs.json rather than regenerate a fake one.
rm -f "$DST/cron_jobs.json"
hermes -p l2-investigator cron list > "$DST/cron_jobs.txt" 2>&1

echo "Done. Review $DST before committing (config.yaml files especially)."
