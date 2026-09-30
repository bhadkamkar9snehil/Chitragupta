---
type: procedure
title: "XBatch_U_Store_USP"
built: "2026-09-24T11:36:36"
---

# XBatch_U_Store_USP

Parameters: @ID varchar, @Name varchar, @Capacity decimal, @CapacityUnit varchar, @Description varchar, @IsEnabled bit, @UserID varchar.

## Writes

- XBatch_Store_Mst_Tbl: Capacity, CapacityUnitID, Description, IsEnabled, ModifiedBy, ModifiedOn, Name, Source

## Reads

- XBatch_Measurement_Unit_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Store_Mst_Tbl: ID
