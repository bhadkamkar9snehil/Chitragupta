---
type: procedure
title: "SAP_Posting_Data_ByHeat_Usp"
built: "2026-09-24T11:36:36"
---

# SAP_Posting_Data_ByHeat_Usp

Parameters: @HeatNo nvarchar.

## Writes

- SAP_Posting_Tbl: BatchNo, CreatedOn, HeatNo, MaterialCode, MovementType, PlantCode, PostingDate, PostingType, Quantity, SAP_Status, StorageLocation, UOM, WorkOrderNo

## Reads

- CCM_Per_Heat: CreatedOn, CrossSection, HeatID, TotalProduction
- XBatch_Material_Item_Cons_Trn_Tbl: CreatedOn, HeatNo, LotNumber, MaterialID, Quantity, UOMID
- XBatch_Material_Item_Prod_Trn_Tbl: CreatedOn, HeatNo, MaterialID, Quantity, SublotNumber, UOMID
- XBatch_Material_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Measurement_Unit_Mst_Tbl: ID, Name
- XBatch_Work_Order_Mst_Tbl: HeatNo, WorkOrderNumber
