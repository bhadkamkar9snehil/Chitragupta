---
type: procedure
title: "Xmes_Billet_Tracking_Move_to_Stand_1"
built: "2026-09-24T11:36:36"
---

# Xmes_Billet_Tracking_Move_to_Stand_1

Parameters: @systemid varchar, @userid varchar, @RecordId varchar, @status varchar.

## Writes

- MES_SAP_Consumption_Trn_Tbl: Batch, EntryUnit, GoodsMovementType, Grade, HeatNo, ManufacturingOrder, Material, Plant, PostingDate, PostingMaterialType, QuantityInCount, QuantityInEntryUnit, SAPPostingStatus, Saptransactionid, Source, StorageLocation
- XMES_Billet_Strand_tracking: S1IT, Stand, Status
- XMES_Billet_Tracking_Trn_Tbl: Batch, BilletNo, BilletQuantity, BilletWeight, CreatedOn, CutLength, EntryDateTime, HeatNo, ManufacturingOrder, Materialid, Plant, PostingMaterialType, ProcessStage, Qualitygradeid, ReportDate, Source, StatePosition, StorageLocation, UOMID
- XMES_Live_Billet_Charging_Bed: BilletTrackingStatus
- Xbatch_Material_Inventory_Trn_Tbl: BilletNo, CreatedBy, CreatedOn, LotNumber, MaterialGrade, ParentID, PlantName, PostingMaterialType, Quantity, QuantityinCount, Source, StorageLocation, UOMID

## Reads

- MES_SAP_Consumption_Trn_Tbl: Batch, CreatedBy, Grade, Plant, PostingMaterialType, StorageLocation
- XBatch_Material_Mst_Tbl: Grade, ID, IsDeleted, Name
- XMES_Billet_Strand_tracking: BIlletNo, ID, IsDeleted, S1OT, Stand, Status
- XMES_Billet_Tracking_Trn_Tbl: IsDeleted
- XMES_Live_Billet_Charging_Bed: BilletNo, ID, IsDeleted
- XMES_Stage_Position_Mapping_Mst_Tbl: IsDeleted, PositionType, StageCode
- XMES_State_Position_State_Mst_Tbl: ID, IsDeleted, SequenceNumber
