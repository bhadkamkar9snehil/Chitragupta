---
name: xstudio-sohar-heat-execution
description: "Investigate EAF/LRF/CCM per-heat data and billet events."
version: 0.1.0
author: Snehil Bhadkamkar, Hermes Agent
license: MIT
platforms: [linux, windows]
metadata:
  hermes:
    tags: [xstudio, xbatch, sohar, eaf, lrf, ccm, billet, heat]
    related_skills: [xstudio-l2-ticket-workflow, xstudio-sql-write-discipline]
---

# XStudio Sohar Heat Execution Skill

For tickets about a heat's EAF/LRF/CCM values, per-heat data missing or
attributed to the wrong heat, billet count/weight, furnace/yard tracking,
or SMS Plant Process Time timing — the production chain at Sohar Steel
Oman (confirmed: `XStudio_Xbatch` on 10.2.6.204 **is** this plant).

**Full reference:**
`C:\Users\Admin\Documents\Office\AIHelpdesk\Knowledge\sohar-sms-event-workflows.md`
has the complete event state-machine and workflow-SP SQL this skill
summarizes — read it for the exact condition/procedure text on a specific
state; this skill is the investigation triggers and the traps, not the
full reference.

## When to Use

- Ticket names EAF, LRF, CCM, a heat number, tapping/arcing/casting
  position, turret, billet count/weight, furnace/yard position, or "SMS
  Plant Process Time."
- Don't use for: SAP posting itself (`xstudio-sap-api-investigation`,
  though heat data often feeds SAP posting — start here, hand off if the
  root cause turns out to be SAP-side).

## Procedure

1. **Identify the chain position**: EAF (melt) → LRF (ladle refining) →
   CCM (casting) → Billets Cast Count, with SMS Plant Process Time running
   in parallel tracking ladle-car/turret timing across all three.
2. **Read the live event/workflow row** for the relevant heat in
   `EAF_PER_HEAT` / `LRF_Per_Heat` / `CCM_Per_Heat` /
   `SMS_Plant_Process_EventTime` / `BilletsCastCount` before assuming
   anything from the reference doc — schema drifts.
3. **For "why is this value wrong/missing," find which stage wrote it**:
   Entered actions resolve identity + post consumption; Completed actions
   post the calculated production totals. A missing Completed-stage value
   usually means that workflow transition never fired — check the
   triggering state's live tag condition, not just the target row.
4. **Get the current SQL** for the specific workflow action via
   `get_sql_object_definition` on the `XSTUDIO_WORKFLOW_<GUID>_SP` named in
   `sohar-sms-event-workflows.md`'s event map, rather than trusting that
   file's point-in-time text for an exact current formula/threshold.

## Pitfalls (each confirmed against live data at least once)

- **`@ActualHeatID = @HeatID - 1` is real and intentional** in the SMS
  Plant Process Time workflow (states 11+) — confirmed live 2026-09-02
  (Heat 1604015 → `ActualHeatID` 1604014). A ticket reporting an event
  "attributed to the wrong heat" by exactly one is very likely this
  decrement working as designed, not a bug — verify against this before
  calling it a defect.
- **Two lot-number prefixes for one heat is expected**, not a duplicate
  posting: `LS_<HeatID>` at the Entered stage (EAF/LRF), `GLS_<HeatID>` at
  the Completed stage (LRF/CCM).
- **CCM billet weight formula has a hardcoded `12`**:
  `TotalBilletWeight = ActualBilletsCountByOperator * 12 * SetWeight`
  (`SetWeight` from `Billet_Cross_Section.MaterialSpecificWeight` for the
  heat's cross-section). If a plant convention ever changes this multiplier,
  it's a real drift risk — flag it rather than silently recomputing.
- **Billet item name is a hardcoded cross-section split**: `CrossSection
  = 130` → `Billet_130X130`, anything else → `Billet_150X150`. An unusual
  cross-section still falls into the "150" bucket by this fallback — not a
  config lookup miss.
- **The operator-declared count, not the raw tag count, drives the final
  weight** — `ActualBilletCountByOperator` (manual override) is what the
  Completed action actually uses, distinct from the live-tag-driven
  `CCMTotalBilletsCount`. A "count doesn't match the historian trend"
  ticket may be comparing the wrong one of these two on purpose.
- **CCM's Entered action resolves which arm/heat by querying the most
  recent matching event**, not an arm-specific parameter — both Arm 1 and
  Arm 2 share one workflow action. A "wrong arm's data mixed into a heat"
  ticket is a concurrency/ordering question on this shared query.
- **Two rows for the same heat in `CCM_Per_Heat` (one with blank
  CrossSection) can be legitimate** — the Entered stage can insert before
  cross-section-driven fields are known; verify which row the UI actually
  reads before calling it corrupt data.

## Verification

- [ ] The specific heat's live row(s) were read, not assumed from the
      reference doc's example values.
- [ ] Before calling any heat-attribution or lot-number pattern a bug,
      checked whether it matches one of the documented-as-intentional
      patterns above.
