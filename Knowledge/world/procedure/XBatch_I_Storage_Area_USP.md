---
type: procedure
title: "XBatch_I_Storage_Area_USP"
built: "2026-09-24T11:36:36"
---

# XBatch_I_Storage_Area_USP

Parameters: @Name varchar, @StorageLocation varchar, @Capacity decimal, @CapacityUnit varchar, @Description varchar, @IsEnabled bit, @UserID varchar.

## Writes

- XBatch_Storage_Area_Mst_Tbl: Capacity, CapacityUnitID, CreatedBy, CreatedOn, Description, ID, IsEnabled, Name, ParentID, Source

## Reads

- XBatch_Measurement_Unit_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Store_Mst_Tbl: ID, IsDeleted, Name
