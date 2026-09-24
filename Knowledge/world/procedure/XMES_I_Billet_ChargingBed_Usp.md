---
type: procedure
title: "XMES_I_Billet_ChargingBed_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_I_Billet_ChargingBed_Usp

Parameters: @UserId varchar, @SystemId varchar, @RecordId varchar, @Status varchar.

## Writes

- RM_Operator_HeatSelection: ModifiedOn, ReleaseDate, Released, Remainingbilletincharging, Source, Status, TotalBillet
- XMES_Billet_Movement_Dtl_Tbl: ChargingBedBilletNo, CreatedOn, Section1BilletNo, Section2BilletNo, ZonewiseBilletNo
- XMES_Live_Billet_Charging_Bed: BatchNo, BilletNo, BilletTrackingStatus, InTIme, ParentID, SequenceNo, Source

## Reads

- CCM_Per_Heat: HeatID, IsDeleted, TotalPostedBilletCount
- RM_Operator_HeatSelection: Batch, BilletMaterialType, BilletQty, Heatno, ID, TotalBillet
- XMES_Billet_Tracking_Per_Strand: BilletNo, HeatNo, IsDeleted
- XMES_Billet_Tracking_Trn_Tbl: Batch, BilletNo, HeatNo, IsDeleted, PostingMaterialType, StatePosition
- XMES_Live_Billet_Charging_Bed: BedNo, BilletNo, CreatedOn, IsDeleted, ParentID, Status
- XMES_Live_Charging_SECT1: BilletNo, IsDeleted, Status
- XMES_Live_Charging_SECT2: BilletNo, IsDeleted, Status
- XMES_State_Position_State_Mst_Tbl: ID, IsDeleted, SequenceNumber
