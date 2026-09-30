---
type: procedure
title: "XBatch_I_Material_Consume_NoBOM_USP"
built: "2026-09-24T11:36:36"
---

# XBatch_I_Material_Consume_NoBOM_USP

Parameters: @ItemName varchar, @LotNumber varchar, @SublotNumber varchar, @Quantity decimal, @UOMName varchar, @Grade varchar, @UserID varchar, @HeatNo int, @ProduceItem bit.

## Writes

- XBatch_Material_Item_Cons_Trn_Tbl: CreatedBy, CreatedOn, GradeID, HeatNo, ID, LotNumber, MaterialID, ParentID, Quantity, Source, SublotNumber, UOMID
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type
- Xbatch_Material_Inventory_Trn_Tbl: CreatedOn, LotNumber, MaterialGrade, ParentID, PlantName, PostingMaterialType, Quantity, QuantityinCount, Source, StorageLocation, UOMID

## Reads

- EAF_PER_HEAT: HeatID, IsDeleted, SteelGrade, WorkOrder
- XBatch_Material_Grade_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Material_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Measurement_Unit_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Work_Order_Mst_Tbl: ID, Plant, StorageLocation

## Writes (named in its SQL text)

- XBatch_Material_Inventory_Mst_Tbl

## What its own log shows

24,982 log rows, 2026-05-21 13:21 to 2026-08-12 08:44.

Steps:
- 1 Entered
- 2 Get Material id from Material Master Using material name B500BLMNHC_GLS Start
- 2 Get Material id from Material Master Using material name B500B_GLS Start
- 2 Get Material id from Material Master Using material name HHMNB500B_GLS Start
- 2 Get Material id from Material Master Using material name LIQUID METAL Start
- 2 Get Material id from Material Master Using material name SP3/PS_GLS Start
- 2 Get Material id from Material Master Using material name Start
- 3 Get Material id 1500E229-B686-4B06-9646-FFDFF2877A03 from Material Master Using material name LIQUID METAL End
- 3 Get Material id 74C3C03E-B548-4326-96E2-50A95D104D2E from Material Master Using material name SP3/PS_GLS End
- 3 Get Material id 89D5F6CE-6338-41EF-846A-A52D59A71CA2 from Material Master Using material name B500BLMNHC_GLS End
- 3 Get Material id 95E67680-E7E8-4BF5-9474-0F84AD24F154 from Material Master Using material name HHMNB500B_GLS End
- 3 Get Material id FA79F4DB-F0A9-4ACF-BD99-3B97065F6C48 from Material Master Using material name B500B_GLS End
- 3 Get Material id from Material Master Using material name End
- 4 Get Unit of Measurement id from Measurement unit Master Using Unit name Start
- 4 Get Unit of Measurement id from Measurement unit Master Using Unit name ton Start
- 5 Get Unit of Measurement id 5EB5C70D-852F-404D-A8E5-5C75C7AFE43F from Measurement unit Master Using Unit name ton End
- 5 Get Unit of Measurement id from Measurement unit Master Using Unit name End
- 6 Get grade id from material grade Master Using Grade of  (TBD) Start
- 6 Get grade id from material grade Master Using Grade of TBD Start
- 7 Get grade id DE050F43-AE27-4043-B45A-8F062CD3D7CC from material grade Master Using Grade of (TBD) End
- 7 Get grade id from material grade Master Using Grade of TBD End
- 8 Add Material Inventory transaction records Start
- 8 Get steelGrade from eaf per heat of heatno 1604013 Start
- 8 Get steelGrade from eaf per heat of heatno 1604014 Start
- 8 Store Consumption data in Material item cons Start
- 8 Update Material Quantity which is consumed in material inventory for material 1500E229-B686-4B06-9646-FFDFF2877A03, lotnumber LS_1603945 and UOM ID 5EB5C70D-852F-404D-A8E5-5C75C7AFE43F Start
- 8 Update Material Quantity which is consumed in material inventory for material 1500E229-B686-4B06-9646-FFDFF2877A03, lotnumber LS_1603951 and UOM ID 5EB5C70D-852F-404D-A8E5-5C75C7AFE43F Start
- 8 Update Material Quantity which is consumed in material inventory for material 95E67680-E7E8-4BF5-9474-0F84AD24F154, lotnumber GLS_1603943 and UOM ID 5EB5C70D-852F-404D-A8E5-5C75C7AFE43F Start
- 8 Update Material Quantity which is consumed in material inventory for material 95E67680-E7E8-4BF5-9474-0F84AD24F154, lotnumber GLS_1603951 and UOM ID 5EB5C70D-852F-404D-A8E5-5C75C7AFE43F Start
- 8 Update Material Quantity which is consumed in material inventory for material, lotnumber Start

Example call: `EXEC XStudio_Xbatch.dbo.XBatch_I_Material_Consume_NoBOM_USP @ItemName='SP3/PS_GLS', @LotNumber='GLS_1603802', @SublotNumber=NULL, @Quantity='77.1300', @UOMName='ton', @Grade='TBD', @UserID='TBD', @HeatNo='', @ProduceItem='1603802'`
