---
type: procedure
title: "XMES_entry_for_RAW_Material_Consumption_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_entry_for_RAW_Material_Consumption_Usp

Parameters: @ReportDate date.

## Writes

- MES_Raw_Material_Consumptions_Trn_Tbl: CapturedQuantity, DeclaredQuantity, LotNumber, OrderType, ParentID, Price, ReportDate, SAPWorkflowStatus, Source, Unit, WorkOrder, WorkOrderNo

## Reads

- EAF_PER_HEAT: HeatID, HeatReportDate, IsDeleted, WorkOrder
- Heat_End_Selection_Trn_Tbl: CreatedOn, FirstHeatNo, IsDeleted, LastHeatNo, ReportDate
- MES_Raw_Material_Consumptions_Mapping_Mst_Tbl: ID, IsDeleted, Materialid, RawMaterialName, Unitid
- MES_Raw_Material_Consumptions_Trn_Tbl: IsDeleted, ParentID, ReportDate, Unit
- XBatch_Material_Item_Cons_Trn_Tbl: HeatNo, IsDeleted, LotNumber, MaterialID, ParentID, Price, Quantity, UOMID
- XBatch_Work_Order_Mst_Tbl: ID, IsDeleted, ManufacturingOrderType, WorkOrderNumber
