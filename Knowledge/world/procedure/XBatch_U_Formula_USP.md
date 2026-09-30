---
type: procedure
title: "XBatch_U_Formula_USP"
built: "2026-09-24T11:36:36"
---

# XBatch_U_Formula_USP

Parameters: @ID varchar, @Name varchar, @ItemNumber varchar, @Quantity decimal, @Unit varchar, @Description varchar, @Isenabled bit, @UserID varchar.

## Writes

- XBatch_Formula_Mst_Tbl: Description, IsEnabled, ModifiedBy, ModifiedOn, Name, ParentID, Quantity, Source, UnitID

## Reads

- XBatch_Formula_Mst_Tbl: ID
- XBatch_Material_Mst_Tbl: ID, IsDeleted, Number
- XBatch_Measurement_Unit_Mst_Tbl: ID, IsDeleted, Name
