---
type: procedure
title: "XMES_I_SAP_LS_Production_Trn"
built: "2026-09-24T11:36:36"
---

# XMES_I_SAP_LS_Production_Trn

Parameters: @UserId varchar, @SystemId varchar, @RecordIds varchar, @Status varchar, @DataCollection nvarchar.

## Writes

- EAF_PER_HEAT: ModifiedOn, SAPWorkflowStatus, Source
- MES_SAP_Production_Trn_Tbl: Batch, EntryUnit, GoodsMovementType, Grade, HeatNo, ManufacturingOrder, Material, Plant, PostingMaterialType, QuantityInCount, QuantityInEntryUnit, SAPPostingStatus, Saptransactionid, Source, StorageLocation

## Reads

- EAF_PER_HEAT: ID
- XBatch_Material_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Work_Order_Mst_Tbl: ID, IsDeleted, ItemID, Plant, StorageLocation, WorkOrderNumber
