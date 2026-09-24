---
type: procedure
title: "XBatch_Material_Consumed_Split_Validate_Usp"
built: "2026-09-24T11:36:36"
---

# XBatch_Material_Consumed_Split_Validate_Usp

Parameters: @ID varchar, @UserID varchar, @HeatNo int, @FristLotNumber varchar, @Quantity decimal, @MaterialID varchar, @UOMID varchar, @IsMulitLots bit, @SecondLotNumber varchar, @SecondLotQuantity decimal.

## Reads

- XBatch_Material_Inventory_Mst_Tbl: IsDeleted, LotNumber, ParentID, Quantity, UOMID
