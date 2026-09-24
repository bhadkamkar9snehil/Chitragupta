---
type: procedure
title: "SP_Xbatch_YMS_GenerateLayersForStack"
built: "2026-09-24T11:36:36"
---

# SP_Xbatch_YMS_GenerateLayersForStack

Parameters: @StackID varchar.

## Writes

- XBatch_Storage_Rack_Mst_Tbl: Capacity, IsEnabled, Name, Number, ParentID

## Reads

- LayerConfiguration: IsDeleted, MinCapacity, StartCapacity, decrementValue
- XBatch_Storage_Area_Mst_Tbl: ID, IsDeleted, Name, ParentID
