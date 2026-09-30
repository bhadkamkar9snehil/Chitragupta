---
type: procedure
title: "XMES_SAP_I_RM_By_Product_Prod_Cons_Trn_Usp"
built: "2026-09-24T11:36:36"
---

# XMES_SAP_I_RM_By_Product_Prod_Cons_Trn_Usp

Parameters: @ReportDate date.

## Writes

- MES_SAP_By_Product_Trn_Tbl: EntryUnit, GoodsMovementType, ManufacturingOrder, Material, Plant, PostingDate, PostingMaterialType, QuantityInEntryUnit, SAPPostingStatus, Saptransactionid, Source, StorageLocation
- MES_SAP_Consumption_Trn_Tbl: EntryUnit, GoodsMovementType, ManufacturingOrder, Material, Plant, PostingDate, PostingMaterialType, QuantityInEntryUnit, SAPPostingStatus, Saptransactionid, Source, StorageLocation

## Reads

- MES_SAP_By_Product_Trn_Tbl: IsDeleted
- MES_SAP_Consumption_Trn_Tbl: IsDeleted
- Plant_Name_MST: ID
- Product_Master: ID, Name, ShortName
- Storage_Location_MST: ID, Plant
- XBatch_Material_Mst_Tbl: IsDeleted, Name, Number, PlantID, StoragelocationID, TypeID
- XBatch_Work_Order_Mst_Tbl: CampaignId, ID, WorkOrderNumber
- XMES_Billet_Tracking_Trn_Tbl: BilletNo, BilletWeight, StatePosition
- XMES_Campaign_Plan_Mst: ID, Productname
- XMES_RM_Production_Data: BilletNo, BundleWeightTon, IsDeleted, ReportDate, Workorderid
- XMES_State_Position_State_Mst_Tbl: ID, SequenceNumber
