---
type: procedure
title: "SP_Xbatch_SplitsBillets_From_CCM_To_Inventory"
built: "2026-09-24T11:36:36"
---

# SP_Xbatch_SplitsBillets_From_CCM_To_Inventory

Parameters: @HeatNo varchar, @ItemName varchar, @MaterialGrade varchar, @Grade varchar.

## Writes

- XBatch_Billets_Transfer_History_Tbl: BilletLength, BilletNo, CurrentStatus, ID, InventoryID, MaterialGrade, ParentID, RecievedBy, RecievedDate, SubLotNo
- XBatch_Material_Inventory_Mst_Tbl: BilletLength, BilletReceivedBy, GradeID, ID, ItemSource, LotNumber, MaterialGrade, ParentID, Quantity, ReceivedDate, SublotNumber, UOMID
- XBatch_Material_Item_Prod_Trn_Tbl: CreatedBy, CreatedOn, GradeID, HeatNo, ID, LotNumber, MaterialID, Quantity, Source, SublotNumber, UOMID

## Reads

- CCM_Per_Heat: EndTime, HeatID, IsDeleted, TotalBilletsCount, TotalProduction
- XBatch_Material_Grade_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Material_Inventory_Mst_Tbl: IsDeleted
- XBatch_Material_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Measurement_Unit_Mst_Tbl: ID, IsDeleted, Name
