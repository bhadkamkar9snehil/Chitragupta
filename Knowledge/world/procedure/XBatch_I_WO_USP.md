---
type: procedure
title: "XBatch_I_WO_USP"
built: "2026-09-24T11:36:36"
---

# XBatch_I_WO_USP

Parameters: @Name varchar, @SONumber varchar, @WoNumber varchar, @SerialNumber int, @Quantity decimal, @Unit varchar, @ItemNumber varchar, @Status varchar, @Description varchar, @UserID varchar.

## Writes

- XBatch_Work_Order_Mst_Tbl: CreatedBy, CreatedOn, Description, ID, ItemID, Name, ParentID, Quantity, SerialNumber, Source, Status, UnitID, WorkOrderNumber

## Reads

- XBatch_Material_Mst_Tbl: ID, IsDeleted, Number
- XBatch_Measurement_Unit_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Sales_Order_Mst_Tbl: ID, IsDeleted, SalesOrderNumber
