---
type: procedure
title: "XSTUDIO_WORKFLOW_19910303-DE98-45A2-909B-EF83E8EAD0BA_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_19910303-DE98-45A2-909B-EF83E8EAD0BA_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Reads

- XMES_RM_Production_Data: BatchNo, BilletNo, BundleWeightTon, EndProductNo, EndProductid, EntryDateTime, HeatNo, ID, IsProcessed, NoofPieces, ReportDate, SectionLength, Workorderid

## Writes (named in its SQL text)

- XMES_RM_Production_Data

## Calls

- XMES_SAP_I_EndProduct_Production_Usp
