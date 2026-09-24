---
type: procedure
title: "XSTUDIO_WORKFLOW_186ECADD-2234-409C-B747-5CC09F854A60_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_186ECADD-2234-409C-B747-5CC09F854A60_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XBatch_Work_Order_Mst_Tbl: ProgressTonnage
- XMES_Live_Billet_Charging_Bed: OutTime, Status
- XMES_Live_Charging_SECT1: BilletNo, InTIme, ModifiedOn, ParentID, ReverseWorkFlow, Status
- XMES_Live_Charging_SECT2: BilletNo, InTIme, ModifiedOn, OutTime, ParentID, Status, Weighment

## Reads

- ChargingBedToFurnance: BilletWeightTon, EndTime, EquipmentID, ID, IsProcessed, ReportDate, StartTime, Status
- RM_Operator_HeatSelection: ID, workorder
- XBatch_Work_Order_Mst_Tbl: ID, IsDeleted
- XMES_Live_Billet_Charging_Bed: BilletNo, CreatedOn, ID, IsDeleted, ParentID
- XMES_Live_Charging_SECT1: ID, IsDeleted
- XMES_Live_Charging_SECT2: ID, IsDeleted

## Writes (named in its SQL text)

- ChargingBedToFurnance

## Calls

- MES_M_Sect2_to_Furnace
- Xstudio_Historian_RM_Billet_Weight_Block_usp
