---
type: procedure
title: "AllocateBilletsToStacksByBilletNo"
built: "2026-09-24T11:36:36"
---

# AllocateBilletsToStacksByBilletNo

Parameters: @HeatNo nvarchar.

## Writes

- XBatch_Material_Inventory_Mst_Tbl: LocationID

## Reads

- XBatch_Material_Inventory_Mst_Tbl: ID, LotNumber, SublotNumber
- XBatch_Storage_Rack_Mst_Tbl: Capacity, ID, Name, Number
