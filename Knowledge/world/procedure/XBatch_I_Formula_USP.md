---
type: procedure
title: "XBatch_I_Formula_USP"
built: "2026-09-24T11:36:36"
---

# XBatch_I_Formula_USP

Parameters: @Name varchar, @ItemNumber varchar, @Quantity decimal, @Unit varchar, @Description varchar, @Isenabled bit, @UserID varchar.

## Writes

- XBatch_Formula_Mst_Tbl: CreatedBy, CreatedOn, Description, ID, IsEnabled, Name, ParentID, Quantity, Source, UnitID

## Reads

- XBatch_Material_Mst_Tbl: ID, IsDeleted, Number
- XBatch_Measurement_Unit_Mst_Tbl: ID, IsDeleted, Name
