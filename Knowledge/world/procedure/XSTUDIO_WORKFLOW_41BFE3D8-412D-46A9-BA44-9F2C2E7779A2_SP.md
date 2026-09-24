---
type: procedure
title: "XSTUDIO_WORKFLOW_41BFE3D8-412D-46A9-BA44-9F2C2E7779A2_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_41BFE3D8-412D-46A9-BA44-9F2C2E7779A2_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Reads

- ChargingBedToFurnance: BilletWeightTon, EndTime, EquipmentID, ID, IsProcessed, ReportDate, StartTime, Status

## Writes (named in its SQL text)

- ChargingBedToFurnance

## Calls

- Xstudio_Historian_RM_Billet_Weight_Block_usp
