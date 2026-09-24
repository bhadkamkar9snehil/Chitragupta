---
type: procedure
title: "Xmes_Billet_Tracking_Move_to_Stand_18"
built: "2026-09-24T11:36:36"
---

# Xmes_Billet_Tracking_Move_to_Stand_18

Parameters: @systemid varchar, @userid varchar, @RecordId varchar, @status varchar.

## Writes

- XMES_Billet_Strand_tracking: S18IT, S18OT, S1OT, Stand, Status
- XMES_Billet_Tracking_Trn_Tbl: Batch, BilletNo, BilletQuantity, BilletWeight, CreatedOn, CutLength, EntryDateTime, HeatNo, ManufacturingOrder, Materialid, Plant, PostingMaterialType, ProcessStage, Qualitygradeid, ReportDate, Source, StatePosition, StorageLocation, UOMID
- XMES_Live_Billet_Charging_Bed: BilletTrackingStatus

## Reads

- XMES_Billet_Strand_tracking: BIlletNo, ID, IsDeleted, Stand, Status
- XMES_Live_Billet_Charging_Bed: BilletNo, ID, IsDeleted
- XMES_Stage_Position_Mapping_Mst_Tbl: IsDeleted, PositionType, StageCode
- XMES_State_Position_State_Mst_Tbl: ID, IsDeleted, SequenceNumber

## Writes (named in its SQL text)

- MES_SAP_Consumption_Trn_Tbl
- Xbatch_Material_Inventory_Trn_Tbl
