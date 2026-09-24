---
type: procedure
title: "XBatch_I_Storage_Subarea_USP"
built: "2026-09-24T11:36:36"
---

# XBatch_I_Storage_Subarea_USP

Parameters: @Name varchar, @StorageArea varchar, @Number int, @IsEnabled bit, @UserID varchar.

## Writes

- XBatch_Storage_Rack_Mst_Tbl: CreatedBy, CreatedOn, ID, IsEnabled, Name, Number, ParentID, Source

## Reads

- XBatch_Storage_Area_Mst_Tbl: ID, IsDeleted, Name
