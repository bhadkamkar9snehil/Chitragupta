---
type: procedure
title: "XBatch_U_Formula_Details_USP"
built: "2026-09-24T11:36:36"
---

# XBatch_U_Formula_Details_USP

Parameters: @ID varchar, @FormulaName varchar, @ItemNumber varchar, @Unit varchar, @Quantity decimal, @QuantityType varchar, @Description varchar, @Isenabled bit, @MinQuantity decimal, @MaxQuantity decimal, @UserID varchar.

## Writes

- XBatch_Formula_Dtl_Tbl: Description, IsEnabled, MaterialID, MaxQuantity, MinQuantity, ModifiedBy, ModifiedOn, ParentID, Quantity, QuantityType, Source, UnitID

## Reads

- XBatch_Formula_Dtl_Tbl: ID
- XBatch_Formula_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Material_Mst_Tbl: ID, IsDeleted, Number
- XBatch_Measurement_Unit_Mst_Tbl: ID, IsDeleted, Name
