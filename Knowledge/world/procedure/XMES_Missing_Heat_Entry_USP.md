---
type: procedure
title: "XMES_Missing_Heat_Entry_USP"
built: "2026-09-24T11:36:36"
---

# XMES_Missing_Heat_Entry_USP

Parameters: @HEATID int.

## Writes

- BilletsCastCount: EndTime, EquipmentID, HeatID, Source, StartTime, Status, WorkFlowStatus
- CCM_Per_Heat: EndTime, EquipmentID, Grade, HeatID, HeatReportDate, Material, ReportDate, SalesOrder, Source, StartTime, Status, WorkOrder, WorkflowStatus

## Reads

- BilletsCastCount: ID
- CCM_Per_Heat: IsDeleted, TotalProduction
- EAF_PER_HEAT: HeatID, HeatReportDate, IsDeleted, ReportDate
- LRF_Per_Heat: CreatedOn, HeatID, HeatReportDate, IsDeleted, LiquidMetalWeight, WorkOrder
- SMS_Plant_Process_EventTime: ActualHeatID, EndTime, StartTime, StateSequence, Status
- XBatch_Material_Mst_Tbl: ID, Name
- XBatch_Work_Order_Mst_Tbl: Equipment, Grade, ID, IsDeleted, ItemID, MaterialName, SalesOrder, Status

## Calls

- XBatch_I_Material_Consume_NoBOM_USP
