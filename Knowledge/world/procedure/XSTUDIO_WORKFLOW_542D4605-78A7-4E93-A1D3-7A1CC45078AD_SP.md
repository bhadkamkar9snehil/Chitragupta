---
type: procedure
title: "XSTUDIO_WORKFLOW_542D4605-78A7-4E93-A1D3-7A1CC45078AD_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_542D4605-78A7-4E93-A1D3-7A1CC45078AD_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XMES_Billet_Strand_tracking: S18OT, S1OT, Source, Stand, Status
- XMES_Live_Billet_Charging_Bed: BilletTrackingStatus

## Reads

- XMES_Billet_Strand_tracking: BIlletNo, CreatedOn, ID, IsDeleted
- XMES_Live_Billet_Charging_Bed: BilletNo, IsDeleted
- XMES_RM_Stand_WRM: EndTime, EquipmentID, ID, IsProcessed, ReportDate, StartTime, Status

## Writes (named in its SQL text)

- XMES_RM_Stand_WRM
