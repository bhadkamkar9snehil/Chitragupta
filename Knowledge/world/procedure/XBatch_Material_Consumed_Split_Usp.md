---
type: procedure
title: "XBatch_Material_Consumed_Split_Usp"
built: "2026-09-24T11:36:36"
---

# XBatch_Material_Consumed_Split_Usp

Parameters: @ID varchar, @UserID varchar, @HeatNo int, @FristLotNumber varchar, @Quantity decimal, @MaterialID varchar, @UOMID varchar, @IsMulitLots bit, @SecondLotNumber varchar, @SecondLotQuantity varchar.

## Writes

- XBatch_Material_Inventory_Mst_Tbl: AvailableQuantityPrice, ModifiedOn, Quantity
- XBatch_Material_Item_Cons_Trn_Tbl: CreatedBy, CreatedOn, DeclareQuantity, GradeID, HeatNo, ID, LotNumber, MaterialID, ParentID, Price, Quantity, Source, SublotNumber, UOMID

## Reads

- XBatch_Material_Inventory_Mst_Tbl: AvailableQuantityPrice, GradeID, IsDeleted, LotNumber, ParentID, Price, Quantity, UOMID
