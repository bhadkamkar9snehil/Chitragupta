---
type: procedure
title: "XSTUDIO_WORKFLOW_EF0111B5-A904-44B4-8C7F-5DAC21CE993B_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_EF0111B5-A904-44B4-8C7F-5DAC21CE993B_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- MES_WRM: Billetno, Heatno, ParentID

## Reads

- XMES_Billet_Strand_tracking: BIlletNo, EntryDateTime, ID, IsProcessed, ReportDate, S10IT, S10OT, S11IT, S11OT, S12IT, S12OT, S13IT, S13OT, S14IT, S14OT, S15IT, S15OT, S16IT, S16OT, S17IT, S17OT, S18IT, S18OT, S1IT, S1OT, S2IT, S2OT, S3IT, S3OT, S4IT, S4OT, S5IT, S5OT, S6IT, S6OT, S7IT, S7OT, S8IT, S8OT, S9IT, S9OT

## Writes (named in its SQL text)

- XMES_Billet_Strand_tracking
