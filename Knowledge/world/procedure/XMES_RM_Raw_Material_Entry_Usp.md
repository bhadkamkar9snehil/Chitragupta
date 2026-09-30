---
type: procedure
title: "XMES_RM_Raw_Material_Entry_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_RM_Raw_Material_Entry_Usp

Parameters: @ReportDate date, @Type int.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- MES_Raw_Material_Consumptions_Trn_Tbl: CapturedQuantity, DeclaredQuantity, LotNumber, ModifiedOn, OrderType, ParentID, Price, ReportDate, SAPWorkflowStatus, Source, Unit, WorkOrder, WorkOrderNo
- XBatch_Material_Inventory_Mst_Tbl: AvailableQuantityPrice, ModifiedOn, Quantity

## Reads

- EAF_PER_HEAT: HeatID, HeatReportDate, IsDeleted, WorkOrder
- MES_Raw_Material_Consumptions_Mapping_Mst_Tbl: Attributeids, Entityids, ID, IsDeleted, Materialid, RawMaterialName, Unitid
- MES_Raw_Material_Consumptions_Trn_Tbl: IsDeleted, ParentID, ReportDate, Unit
- XBatch_Material_Inventory_Mst_Tbl: CreatedOn, IsDeleted, LotNumber, ParentID, Price, Quantity, UOMID
- XBatch_Material_Mst_Tbl: ID, Name, Number
- XBatch_Measurement_Unit_Mst_Tbl: ID, Name
- XBatch_Work_Order_Mst_Tbl: ID, IsDeleted, ManufacturingOrderType, WorkOrderNumber
