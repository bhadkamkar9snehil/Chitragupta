---
type: procedure
title: "XMES_I_SAP_GLS_LS_Production_Trn_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_I_SAP_GLS_LS_Production_Trn_Usp

Parameters: @HeatNo int.

## Writes

- EAF_PER_HEAT: ModifiedOn, SAPWorkflowStatus, Source, SteelGrade
- LRF_Per_Heat: ModifiedOn, SAPWorkflowStatus, Source
- MES_SAP_Production_Trn_Tbl: Batch, EntryUnit, GoodsMovementType, Grade, HeatNo, ManufacturingOrder, Material, Plant, PostingDate, PostingMaterialType, QuantityInCount, QuantityInEntryUnit, SAPPostingStatus, Sampleid, Saptransactionid, Source, StorageLocation
- Xbatch_Material_Inventory_Trn_Tbl: CreatedBy, CreatedOn, LotNumber, MaterialGrade, ParentID, PlantName, PostingMaterialType, Quantity, QuantityinCount, Source, StorageLocation, UOMID

## Reads

- EAF_PER_HEAT: CalcLiquidMetalWeight, HeatID, HeatReportDate, IsDeleted, SteelGrade, WorkOrder
- Heat_Chemistry_Quality_Data: HeatNo, ID, IsDeleted, SampleType
- LRF_Per_Heat: CalcLiquidMetalWeight, Grade, HeatID, HeatReportDate, IsDeleted, WorkOrder
- MES_SAP_Production_Trn_Tbl: Batch, CreatedBy, HeatNo, PostingMaterialType
- XBatch_Material_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Measurement_Unit_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Work_Order_Mst_Tbl: ID, IsDeleted, ItemID, Plant, ProductionPlant, StorageLocation, WorkOrderNumber

## Writes (named in its SQL text)

- XBatch_Material_Inventory_Mst_Tbl
