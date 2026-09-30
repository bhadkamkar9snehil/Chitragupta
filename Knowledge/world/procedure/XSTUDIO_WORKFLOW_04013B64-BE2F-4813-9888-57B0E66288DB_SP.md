---
type: procedure
title: "XSTUDIO_WORKFLOW_04013B64-BE2F-4813-9888-57B0E66288DB_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_04013B64-BE2F-4813-9888-57B0E66288DB_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Reads

- Billet_Track_Per_Strand: EndTime, EquipmentID, HeatNo, ID, IsProcessed, ReportDate, S1BilletCount, S2BilletCount, S3BilletCount, S4BilletCount, S5BilletCount, S6BilletCount, StartTime, Status, StrandwiseCount

## Writes (named in its SQL text)

- Billet_Track_Per_Strand

## Calls

- XMES_CCM_BILLET_CUT_USP
- XMES_CCM_BILLET_MASTER_CREATE_USP
- XMES_CCM_BILLET_PRODUCED_USP
