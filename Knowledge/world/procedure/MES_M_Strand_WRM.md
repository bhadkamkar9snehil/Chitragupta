---
type: procedure
title: "MES_M_Strand_WRM"
built: "2026-09-24T11:36:36"
---

# MES_M_Strand_WRM

Parameters: @UserId varchar, @SystemId varchar, @RecordId varchar, @Status varchar.

## Writes

- MES_Current_Batch: WRM
- MES_WRM: BatchNo, Billetno, Heatno, InTIme, ParentID, Workorder
- XMES_Billet_Strand_tracking: S18OT, Status
- XMES_Billet_Tracking_Trn_Tbl: Batch, BilletNo, BilletQuantity, BilletWeight, CreatedOn, CutLength, EntryDateTime, HeatNo, ManufacturingOrder, Materialid, Plant, PostingMaterialType, ProcessStage, Qualitygradeid, ReportDate, Source, StatePosition, StorageLocation, UOMID

## Reads

- MES_WRM: Billetno
- XMES_Billet_Strand_tracking: BIlletNo, ID, ParentID
- XMES_Live_Charging_SECT2: BilletNo, Weighment
- XMES_Stage_Position_Mapping_Mst_Tbl: IsDeleted, PositionType, StageCode
- XMES_State_Position_State_Mst_Tbl: ID, IsDeleted, SequenceNumber

## Writes (named in its SQL text)

- XBatch_Work_Order_Mst_Tbl
- XMES_Campaign_Plan_Mst
