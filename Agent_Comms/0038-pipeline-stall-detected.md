---
id: 38
type: finding
from: claude
to: claude
created: 2026-09-24T08:33:57.670596
---

## Finding

Automated stall detector (check_pipeline_stall(), runs inside the existing 10-minute audit cron) found the pipeline has stopped claiming new work despite real eligible tickets waiting:

- Active runs: 0
- Eligible unclaimed tickets: 40
- Minutes since last claim: 304.0

This means scout() is either erroring before it can claim (check recent ticket_scout cron output for WORKER_DEPENDENCY_UNAVAILABLE or an unhandled exception) or something else is blocking claims. Investigate and fix before assuming this is a hard/slow ticket -- a stall this long with tickets waiting is never normal.
