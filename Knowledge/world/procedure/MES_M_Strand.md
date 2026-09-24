---
type: procedure
title: "MES_M_Strand"
built: "2026-09-24T11:36:36"
---

# MES_M_Strand

Parameters: @UserId varchar, @SystemId varchar, @RecordId varchar, @Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- MES_SAP_Consumption_Trn_Tbl: Batch, BilletNo, CreationDate, CreationTime, Cutlength, EntryUnit, FurnaceBilletStatus, GoodsMovementType, Grade, HeatNo, ManufacturingOrder, Material, ModifiedOn, Plant, PostingDate, PostingMaterialType, QuantityInCount, QuantityInEntryUnit, SAPPostingStatus, SAPQuantity, Saptransactionid, Source, StorageLocation
- XBatch_Work_Order_Mst_Tbl: BilletDischarged, BilletDischargedWeight, BilletsCobble, BilletsHotout, BilletsRemaining, BilletsRolled, BundlesProduce, BundlesRemaining, ProgressTonnage, RemainingTonnage
- XMES_Billet_Tracking_Trn_Tbl: Batch, BilletNo, BilletQuantity, BilletWeight, CreatedOn, CutLength, EntryDateTime, HeatNo, ManufacturingOrder, Materialid, Plant, PostingMaterialType, ProcessStage, Qualitygradeid, ReportDate, Source, StatePosition, StorageLocation, UOMID
- XMES_Campaign_Plan_Mst: ProgressTonnage, RemaningTonnage
- XMES_RM_Production_Data: IsHotOut, IsSapConsumed
- Xbatch_Material_Inventory_Trn_Tbl: BilletNo, CreatedBy, CreatedOn, LotNumber, MaterialGrade, ParentID, PlantName, PostingMaterialType, Quantity, QuantityinCount, Source, StorageLocation, UOMID

## Reads

- MES_SAP_Consumption_Trn_Tbl: Batch, BilletNo, CreatedBy, FurnaceBilletStatus, Grade, IsDeleted, ManufacturingOrder, Plant, PostingMaterialType, QuantityInCount, SAPQuantity, StorageLocation
- XBatch_Material_Mst_Tbl: Grade, ID, IsDeleted, Name
- XBatch_Work_Order_Mst_Tbl: CampaignId, ID, IsDeleted, MaxBundles, ProgressTonnage, Quantity, RemainingTonnage, TotalBillets, WorkOrderNumber
- XMES_Billet_Strand_tracking: BIlletNo, ID, IsDeleted, Stand, Status
- XMES_Billet_Tracking_Trn_Tbl: IsDeleted
- XMES_Campaign_Plan_Mst: ID
- XMES_RM_Production_Data: BilletNo, BundleWeightTon, CreatedOn, ID, IsDeleted, IsHotOut, Workorderid
- XMES_Stage_Position_Mapping_Mst_Tbl: IsDeleted, PositionType, StageCode
- XMES_State_Position_State_Mst_Tbl: ID, IsDeleted, SequenceNumber

## Writes (named in its SQL text)

- XMES_Billet_Strand_tracking
