---
type: view
title: "XStudio_List_XBatch_Batch_BOM_Mst_Tbl_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_List_XBatch_Batch_BOM_Mst_Tbl_Vw

View in XStudio_Xbatch. Rows: unknown.

## Reads

- XBatch_Batch_BOM_Mst_Tbl
- XBatch_Batch_Mst_Tbl
- XBatch_Batch_Operation_Mst_Tbl
- XBatch_Batch_Phase_Group_Mst_Tbl
- XBatch_Batch_Phase_Mst_Tbl
- XBatch_Batch_Unit_Procedure_Mst_Tbl
- XBatch_Material_Item_Cons_Trn_Tbl
- XBatch_Material_Mst_Tbl
- XBatch_Material_Type_Mst_Tbl
- XBatch_Measurement_Unit_Mst_Tbl

## Read by

- XBatch_MR_Get_Batch_Material_List_Usp

## Columns

- Edit varchar(236)
- ID varchar(36)
- ItemID varchar(36)
- ItemType varchar(100)
- Item varchar(100)
- Unit varchar(100)
- Quantity decimal
- ActualQuantity decimal
- QuantityDeviation decimal
- UnitProcedure varchar(100)
- BatchNumber varchar(100)
- Operation varchar(100)
- PhaseGroup varchar(100)
- OperationID varchar(36)
- ParentID varchar(36)
- Phase varchar(100)
- PhaseGroupID varchar(36)
- Delete varchar(100)
- PhaseID varchar(36)
- UnitProcedureID varchar(36)
- UOMID varchar(36)
- Details varchar(-1)
- UnitProcedure_SrNo int
- Operation_SrNo int
- PhaseGroup_SrNo int
- Phase_SrNo int
- SourceType varchar(100)
