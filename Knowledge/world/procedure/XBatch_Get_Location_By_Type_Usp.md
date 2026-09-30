---
type: procedure
title: "XBatch_Get_Location_By_Type_Usp"
built: "2026-09-24T11:36:36"
---

# XBatch_Get_Location_By_Type_Usp

Parameters: @Type varchar, @LocationType varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Reads

- Equipment_Type_Mst_Tbl: IsDeleted, Name
- XBatch_Storage_Area_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Storage_Rack_Mst_Tbl: ID, IsDeleted, Name, ParentID
