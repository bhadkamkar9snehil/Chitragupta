---
name: xstudio-sohar-heat-execution
description: "Investigate EAF/LRF/CCM per-heat data and billet events."
version: 1.0.0
author: Snehil Bhadkamkar, Hermes Agent
license: MIT
platforms: [linux, windows]
metadata:
  hermes:
    tags: [xstudio, xbatch, sohar, eaf, lrf, ccm, billet, heat]
    related_skills: [xstudio-l2-ticket-workflow, xstudio-sql-write-discipline]
---

# XStudio Sohar Heat Execution Skill

Use for tickets about EAF/LRF/CCM values, missing/wrong per-heat data, heat attribution, billet count/weight, furnace/yard tracking, or SMS Plant Process Time.

Primary reference: `Knowledge/sohar-sms-event-workflows.md`. Treat its formulas/state maps as routing knowledge; verify current ticket-specific facts and any exact SQL definition live through `xstudio_l2`.

## Procedure

1. **Identify the chain position:** EAF -> LRF -> CCM -> billet production, with SMS Plant Process Time tracking related process timing.
2. **Prefer comprehensive verified views first.** For many per-heat questions start with `XBatch_Tracability_Heat_Details_Vw` or `Vw_XBatch_Tracability_SMS_Process_Time`; fall back to `EAF_PER_HEAT`, `LRF_Per_Heat`, `CCM_Per_Heat`, `SMS_Plant_Process_EventTime`, or `BilletsCastCount` when necessary.
3. **Read the specific heat live.** Do not infer current state from the reference document's examples.
4. **For a wrong/missing value, trace which workflow stage writes it.** Use `xstudio_l2.find_objects` to locate the real workflow object and `xstudio_l2.get_definition` to read its current definition. Do not execute a write procedure merely because its name appears in the reference.
5. **Validate identifiers before composing a narrow query.** Use `validate_identifiers` rather than carrying plausible schema names from memory.
6. **If the evidence points to SAP/API rather than process execution, switch to `xstudio-sap-api-investigation`.**

## Known patterns to verify before calling them defects

These are durable leads from prior verified analysis, not substitutes for current-ticket evidence:

- SMS Plant Process Time logic has used `@ActualHeatID = @HeatID - 1` for later states. An exactly-one-heat attribution difference may therefore be intentional workflow behavior.
- EAF/LRF entered-stage and later completed-stage flows have used different lot prefixes (`LS_` vs `GLS_`).
- CCM billet weight logic has included a hardcoded multiplier in the workflow formula; read the current definition before recomputing or declaring drift.
- Operator-declared billet count can differ from raw tag-driven count and may be the value used by final production logic.
- CCM heat/arm resolution can depend on recent matching event order rather than an explicit arm parameter.
- Multiple CCM rows for one heat can occur across workflow stages; verify which row/view the affected UI or downstream process consumes.

## Mutation boundary

If current evidence proves a production/configuration correction is required, do not call the writing workflow procedure from the L2 worker. Return `NEEDS_HUMAN_ACTION` with the exact evidence and corrective path when known, or `L3_ESCALATION` when it is not safely determined.

## Verification

- [ ] The ticket's actual heat/billet row(s) were read live.
- [ ] A reference formula/pattern was confirmed against the current object definition when it materially supports the answer.
- [ ] Comprehensive views were preferred before unnecessary manual joins.
- [ ] No write procedure was executed through a model-created path.
