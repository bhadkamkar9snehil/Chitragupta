---
type: view
title: "XStudio_List_XBatch_Batch_Mst_Tbl_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_List_XBatch_Batch_Mst_Tbl_Vw

View in XStudio_Xbatch. Rows: unknown.

## Identifiers it holds

- WorkOrderNumber: same values as key `ManufacturingOrder`

## Reads

- XBatch_Batch_Mst_Tbl
- XBatch_Material_Mst_Tbl
- XBatch_Measurement_Unit_Mst_Tbl
- XBatch_Process_Cell_Mst_Tbl
- XBatch_Recipe_Mst_Tbl
- XBatch_Status_Mst_Tbl
- XBatch_Work_Order_Mst_Tbl

## Columns

- Edit varchar(234)
- Delete varchar(100)
- ID varchar(36)
- ParentID varchar(36)
- BatchName varchar(100)
- BatchNumber varchar(100)
- FinishedGood varchar(100)
- Recipe varchar(100)
- Status varchar(100)
- Assign varchar(-1)
- BOM varchar(-1)
- Approval varchar(-1)
- Schedule varchar(-1)
- Run varchar(-1)
- UnitID varchar(36)
- View varchar(-1)
- Procedures varchar(-1)
- Quantity decimal
- Unit varchar(100)
- StatusID varchar(36)
- StartTime datetime
- EndTime datetime
- Version varchar(100)
- WorkOrderNumber varchar(100)
- ProcessCell varchar(100)
- WorkOrderID varchar(36)
- ActualStartTime datetime
- ActualEndTime datetime
- Status_Color varchar(50)
