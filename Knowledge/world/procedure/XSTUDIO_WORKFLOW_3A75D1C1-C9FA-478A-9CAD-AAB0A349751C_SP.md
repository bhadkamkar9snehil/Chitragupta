---
type: procedure
title: "XSTUDIO_WORKFLOW_3A75D1C1-C9FA-478A-9CAD-AAB0A349751C_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_3A75D1C1-C9FA-478A-9CAD-AAB0A349751C_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- MES_TMT: BilletNo, HeatNo, InTime, ParentID, Status, workorder

## Reads

- XMES_Billet_Strand_tracking: BIlletNo, Cobble, EntryDateTime, ID, IsProcessed, ReportDate, S0OT, S10IT, S10OT, S11IT, S11OT, S12IT, S12OT, S13IT, S13OT, S14IT, S14OT, S15IT, S15OT, S16IT, S16OT, S17IT, S17OT, S18IT, S18OT, S1IT, S1OT, S2IT, S2OT, S3IT, S3OT, S4IT, S4OT, S5IT, S5OT, S6IT, S6OT, S7IT, S7OT, S8IT, S8OT, S9IT, S9OT

## Writes (named in its SQL text)

- XMES_Billet_Strand_tracking
