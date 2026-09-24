---
type: procedure
title: "XBatch_I_Material_Produce_NoBOM_USP"
built: "2026-09-24T11:36:36"
---

# XBatch_I_Material_Produce_NoBOM_USP

Parameters: @HeatNo int, @ItemName varchar, @LotNumber varchar, @SublotNumber varchar, @Quantity decimal, @UOMName varchar, @Grade varchar, @UserID varchar.

## Writes

- XBatch_Material_Item_Prod_Trn_Tbl: CreatedBy, CreatedOn, GradeID, HeatNo, ID, LotNumber, MaterialID, Quantity, Source, SublotNumber, UOMID
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type
- Xbatch_Material_Inventory_Trn_Tbl: CreatedBy, CreatedOn, ID, LotNumber, MaterialGrade, ParentID, PlantName, PostingMaterialType, Quantity, Source, StorageLocation, UOMID

## Reads

- EAF_PER_HEAT: HeatID, IsDeleted, SteelGrade, WorkOrder
- XBatch_Material_Grade_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Material_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Measurement_Unit_Mst_Tbl: ID, IsDeleted, Name

## Writes (named in its SQL text)

- XBatch_Material_Inventory_Mst_Tbl

## What its own log shows

25,914 log rows, 2026-05-21 09:23 to 2026-07-08 18:04.

Steps:
- 1 Entered
- 2 Get Material ID from material master by material name B500BLMNHC_GLS Start
- 2 Get Material ID from material master by material name B500B_GLS Start
- 2 Get Material ID from material master by material name HHMNB500B_GLS Start
- 2 Get Material ID from material master by material name LIQUID METAL Start
- 2 Get Material ID from material master by material name SP3/PS_GLS Start
- 2 Get Material ID from material master by material name Start
- 3 Get Material ID (1500E229-B686-4B06-9646-FFDFF2877A03) from material master by material name (LIQUID METAL) End
- 3 Get Material ID (74C3C03E-B548-4326-96E2-50A95D104D2E) from material master by material name (SP3/PS_GLS) End
- 3 Get Material ID (89D5F6CE-6338-41EF-846A-A52D59A71CA2) from material master by material name (B500BLMNHC_GLS) End
- 3 Get Material ID (95E67680-E7E8-4BF5-9474-0F84AD24F154) from material master by material name (HHMNB500B_GLS) End
- 3 Get Material ID (FA79F4DB-F0A9-4ACF-BD99-3B97065F6C48) from material master by material name (B500B_GLS) End
- 3 Get Material ID from material master by material name End
- 4 Get Unit of Measurement ID from Measurement unit master by unit name Start
- 4 Get Unit of Measurement ID from Measurement unit master by unit name ton Start
- 5 Get Unit of Measurement ID (5EB5C70D-852F-404D-A8E5-5C75C7AFE43F) from Measurement unit master by unit name (ton) End
- 5 Get Unit of Measurement ID from Measurement unit master by unit name End
- 6 Get Grade ID from Material Grade master by Grade name Start
- 6 Get Grade ID from Material Grade master by Grade name TBD Start
- 7 Get Grade ID (DE050F43-AE27-4043-B45A-8F062CD3D7CC) from Material Grade master by Grade name (TBD) End
- 7 Get Grade ID from Material Grade master by Grade name End
- 8 Get steelGrade and work orderid from eaf per heat of heatno 1603086 Start
- 8 Get steelGrade and work orderid from eaf per heat of heatno 1603087 Start
- 8 Get steelGrade and work orderid from eaf per heat of heatno 1603088 Start
- 8 Get steelGrade and work orderid from eaf per heat of heatno 1603089 Start
- 8 Get steelGrade and work orderid from eaf per heat of heatno 1603090 Start
- 8 Get steelGrade and work orderid from eaf per heat of heatno 1603091 Start
- 8 Get steelGrade and work orderid from eaf per heat of heatno 1603092 Start
- 8 Get steelGrade and work orderid from eaf per heat of heatno 1603093 Start
- 8 Get steelGrade and work orderid from eaf per heat of heatno 1603094 Start

Example call: `EXEC XStudio_Xbatch.dbo.XBatch_I_Material_Produce_NoBOM_USP @HeatNo='1604015', @ItemName='LIQUID METAL', @LotNumber='LS_1604015', @SublotNumber=NULL, @Quantity='68.4525', @UOMName='ton', @Grade='TBD', @UserID='A6E924D5-B2F0-4A5F-9717-3A63F6190358'`
