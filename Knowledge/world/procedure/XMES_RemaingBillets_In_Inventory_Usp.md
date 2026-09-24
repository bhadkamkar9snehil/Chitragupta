---
type: procedure
title: "XMES_RemaingBillets_In_Inventory_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_RemaingBillets_In_Inventory_Usp


## Reads

- Billets_InFurnace_Tracking_Trn: BilletNo, IsDeleted
- XBatch_Material_Mst_Tbl: Grade, ID, Name, Number, TypeID
- XBatch_Material_Type_Mst_Tbl: ID, Name
- XBatch_Measurement_Unit_Mst_Tbl: ID, Name
- XMES_Billet_Strand_tracking: BIlletNo
- XMES_Billet_Tracking_Trn_Tbl: Batch, BilletNo, BilletQuantity, BilletWeight, HeatNo, Materialid, PostingMaterialType, StatePosition
- XMES_Live_Billet_Charging_Bed: BilletNo, IsDeleted
- XMES_Live_Charging_SECT1: BilletNo, IsDeleted
- XMES_Live_Charging_SECT2: BilletNo, IsDeleted
- XMES_State_Position_State_Mst_Tbl: ID, SequenceNumber
- Xbatch_Material_Inventory_Trn_Tbl: IsDeleted, LotNumber, ParentID, PostingMaterialType, Quantity, QuantityinCount, UOMID
