---
type: procedure
title: "XMES_SAP_I_EndProduct_Production_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_SAP_I_EndProduct_Production_Usp

Parameters: @recordid varchar.

## Writes

- MES_SAP_Production_Trn_Tbl: Batch, BilletNo, EntryUnit, GoodsMovementType, Grade, HeatNo, IsAutoPost, ManufacturingOrder, Material, ParentID, Plant, PostingDate, PostingMaterialType, QuantityInCount, QuantityInEntryUnit, SAPPostingStatus, Saptransactionid, SectionLength, Source, StorageLocation

## Reads

- Plant_Name_MST: ID, Plant
- Product_Master: ID, Name
- Storage_Location_MST: ID, Plant, StorageLocation
- XBatch_Material_Mst_Tbl: Grade, ID, Number, PlantID, StoragelocationID
- XBatch_Work_Order_Mst_Tbl: CampaignId, ID, Name, WorkOrderNumber
- XMES_Campaign_Plan_Mst: ID, Productname
- XMES_RM_Production_Data: BilletNo, BundleWeightTon, EndProductNo, EndProductid, HeatNo, ID, ReportDate, SectionLength, Workorderid
