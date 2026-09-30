---
type: procedure
title: "XSTUDIO_WORKFLOW_61EFD8FE-EDF5-4077-BE99-35EF68C5AFCB_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_61EFD8FE-EDF5-4077-BE99-35EF68C5AFCB_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Reads

- XMES_SAP_API_GoodsMovement_Error: Batch, Body, EntryDateTime, ErrorMessage, ID, IsProcessed, ManufacturingOrder, Material, MovementType, RecordID, ReportDate, TransactionID, Type

## Writes (named in its SQL text)

- XMES_SAP_API_GoodsMovement_Error
