# XStudio_Xbatch.dbo.RM_Mill_Data

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference millstand, mill, billet, currentaprm, speedmsprm, stand, status, torquenmprm, trigger, shear, descaler, equipment.

**Primary Key:** ID  
**Row Count:** 19  
**Date Range (ModifiedOn):** 2026-08-31T10:35:09.0900000 to 2026-08-31T10:35:09.0900000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| ParentID | varchar | YES | 36 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| EquipmentID | varchar | YES | 36 | — |
| MILLSTAND01CURRENTAPRM | decimal | YES | 18,4 | — |
| MILLSTAND01SPEEDMSPRM | decimal | YES | 18,4 | — |
| MILLSTAND01TORQUENMPRM | decimal | YES | 18,4 | — |
| MILLSTAND02CURRENTAPRM | decimal | YES | 18,4 | — |
| MILLSTAND02SPEEDMSPRM | decimal | YES | 18,4 | — |
| MILLSTAND02TORQUENMPRM | decimal | YES | 18,4 | — |
| MILLSTAND13CURRENTAPRM | decimal | YES | 18,4 | — |
| MILLSTAND03SPEEDMSPRM | decimal | YES | 18,4 | — |
| MILLSTAND03TORQUENMPRM | decimal | YES | 18,4 | — |
| MILLSTAND04CURRENTAPRM | decimal | YES | 18,4 | — |
| MILLSTAND04SPEEDMSPRM | decimal | YES | 18,4 | — |
| MILLSTAND04TORQUENMPRM | decimal | YES | 18,4 | — |
| MILLSTAND05CURRENTAPRM | decimal | YES | 18,4 | — |
| MILLSTAND05SPEEDMSPRM | decimal | YES | 18,4 | — |
| MILLSTAND05TORQUENMPRM | decimal | YES | 18,4 | — |
| MILLSTAND06CURRENTAPRM | decimal | YES | 18,4 | — |
| MILLSTAND06SPEEDMSPRM | decimal | YES | 18,4 | — |
| MILLSTAND06TORQUENMPRM | decimal | YES | 18,4 | — |
| MILLSTAND07CURRENTAPRM | decimal | YES | 18,4 | — |
| MILLSTAND07SPEEDMSPRM | decimal | YES | 18,4 | — |
| MILLSTAND07TORQUENMPRM | decimal | YES | 18,4 | — |
| MILLSTAND08CURRENTAPRM | decimal | YES | 18,4 | — |
| MILLSTAND08SPEEDMSPRM | decimal | YES | 18,4 | — |
| MILLSTAND08TORQUENMPRM | decimal | YES | 18,4 | — |
| RoughingMill | decimal | YES | 18,4 | — |
| Shear1HL | decimal | YES | 18,4 | — |
| Shear1TL | decimal | YES | 18,4 | — |
| MILLSTAND09CURRENTAPRM | decimal | YES | 18,4 | — |
| MILLSTAND09SPEEDMSPRM | decimal | YES | 18,4 | — |
| MILLSTAND09TORQUENMPRM | decimal | YES | 18,4 | — |
| MILLSTAND10CURRENTAPRM | decimal | YES | 18,4 | — |
| MILLSTAND10SPEEDMSPRM | decimal | YES | 18,4 | — |
| MILLSTAND10TORQUENMPRM | decimal | YES | 18,4 | — |
| MILLSTAND11CURRENTAPRM | decimal | YES | 18,4 | — |
| MILLSTAND11TORQUENMPRM | decimal | YES | 18,4 | — |
| MILLSTAND12CURRENTAPRM | decimal | YES | 18,4 | — |
| MILLSTAND12SPEEDMSPRM | decimal | YES | 18,4 | — |
| MILLSTAND12TORQUENMPRM | decimal | YES | 18,4 | — |
| MILLSTAND03CURRENTAPRM | decimal | YES | 18,4 | — |
| MILLSTAND13SPEEDMSPRM | decimal | YES | 18,4 | — |
| MILLSTAND13TORQUENMPRM | decimal | YES | 18,4 | — |
| MILLSTAND14CURRENTAPRM | decimal | YES | 18,4 | — |
| MILLSTAND14SPEEDMSPRM | decimal | YES | 18,4 | — |
| MILLSTAND14TORQUENMPRM | decimal | YES | 18,4 | — |
| IntermidiateMill | decimal | YES | 18,4 | — |
| Shear2HL | decimal | YES | 18,4 | — |
| Shear2TL | decimal | YES | 18,4 | — |
| MILLSTAND15CURRENTAPRM | decimal | YES | 18,4 | — |
| MILLSTAND15SPEEDMSPRM | decimal | YES | 18,4 | — |
| MILLSTAND15TORQUENMPRM | decimal | YES | 18,4 | — |
| MILLSTAND16CURRENTAPRM | decimal | YES | 18,4 | — |
| MILLSTAND16SPEEDMSPRM | decimal | YES | 18,4 | — |
| MILLSTAND16TORQUENMPRM | decimal | YES | 18,4 | — |
| MILLSTAND17CURRENTAPRM | decimal | YES | 18,4 | — |
| MILLSTAND17SPEEDMSPRM | decimal | YES | 18,4 | — |
| MILLSTAND17TORQUENMPRM | decimal | YES | 18,4 | — |
| MILLSTAND18CURRENTAPRM | decimal | YES | 18,4 | — |
| MILLSTAND18SPEEDMSPRM | decimal | YES | 18,4 | — |
| MILLSTAND18TORQUENMPRM | decimal | YES | 18,4 | — |
| FinishingMill | decimal | YES | 18,4 | — |
| DescalerPressure | decimal | YES | 18,4 | — |
| DescalerTemperature | decimal | YES | 18,4 | — |
| MILLPRODUCTSIZEMMPRM | decimal | YES | 18,4 | — |
| MILLSPEEDMPSPRM | decimal | YES | 18,4 | — |
| MILLSTAND11SPEEDMSPRM | decimal | YES | 18,4 | — |
| MillStand01BilletTriggerStatus | decimal | YES | 18,4 | — |
| MillStand02BilletTriggerStatus | decimal | YES | 18,4 | — |
| MillStand03BilletTriggerStatus | decimal | YES | 18,4 | — |
| MillStand04BilletTriggerStatus | decimal | YES | 18,4 | — |
| MillStand05BilletTriggerStatus | decimal | YES | 18,4 | — |
| MillStand06BilletTriggerStatus | decimal | YES | 18,4 | — |
| MillStand07BilletTriggerStatus | decimal | YES | 18,4 | — |
| MillStand08BilletTriggerStatus | decimal | YES | 18,4 | — |
| MillStand09BilletTriggerStatus | decimal | YES | 18,4 | — |
| MillStand10BilletTriggerStatus | decimal | YES | 18,4 | — |
| MillStand11BilletTriggerStatus | decimal | YES | 18,4 | — |
| MillStand12BilletTriggerStatus | decimal | YES | 18,4 | — |
| MillStand13BilletTriggerStatus | decimal | YES | 18,4 | — |
| MillStand14BilletTriggerStatus | decimal | YES | 18,4 | — |
| MillStand15BilletTriggerStatus | decimal | YES | 18,4 | — |
| MillStand16BilletTriggerStatus | decimal | YES | 18,4 | — |
| MillStand17BilletTriggerStatus | decimal | YES | 18,4 | — |
| MillStand18BilletTriggerStatus | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0E6C942A-82A4-4499-808A-BE153F1E1DAC | NULL | NULL | NULL | NULL | 2025-10-30T10:47:03.1770000 | NULL | False | False | NULL |
| 961C84C0-D5CB-4CA7-B44A-83266C88BF1C | NULL | NULL | NULL | NULL | 2025-10-30T10:46:22.9830000 | NULL | False | False | NULL |
| 6BD19325-E5C7-4358-806A-6B3EB715D869 | NULL | NULL | NULL | NULL | 2025-10-30T10:43:10.8770000 | NULL | False | False | NULL |
| 6BA0FC7D-5ED5-4A44-92A6-A82E7018744D | NULL | NULL | NULL | NULL | 2025-10-30T10:37:22.5930000 | NULL | False | False | NULL |
| 652AB0C3-E8BB-4B0A-8C8B-9CA75F2A1FC8 | NULL | NULL | NULL | NULL | 2025-10-30T10:36:29.0730000 | NULL | False | False | NULL |
| 5C2D786B-6A7A-4B37-AD10-991C931BAB17 | NULL | NULL | NULL | NULL | 2025-10-30T10:44:29.6400000 | NULL | False | False | NULL |
| 565E7021-5C10-476F-B43C-EA72F7B7BD20 | NULL | NULL | NULL | NULL | 2025-10-30T10:38:09.2900000 | NULL | False | False | NULL |
| 48F696BD-2396-4F86-9E07-592E6D78EBD1 | NULL | NULL | NULL | NULL | 2025-10-30T10:37:10.8300000 | NULL | False | False | NULL |
| 44ED0F5E-7B86-4F9A-9A36-C6D368CC5E8C | NULL | NULL | NULL | NULL | 2025-10-30T10:38:38.4030000 | NULL | False | False | NULL |
| 3578FCC6-4349-4D7E-9114-1E9841734FC8 | NULL | NULL | NULL | NULL | 2025-10-30T10:38:26.0000000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1EBEF1CC-24E3-4391-B8AE-602DFB3CFBA2 | NULL | NULL | NULL | NULL | 2025-09-22T12:35:11.4170000 | 2026-08-31T10:35:09.0900000 | False | False | NULL |
| 0E6C942A-82A4-4499-808A-BE153F1E1DAC | NULL | NULL | NULL | NULL | 2025-10-30T10:47:03.1770000 | NULL | False | False | NULL |
| 961C84C0-D5CB-4CA7-B44A-83266C88BF1C | NULL | NULL | NULL | NULL | 2025-10-30T10:46:22.9830000 | NULL | False | False | NULL |
| 6BD19325-E5C7-4358-806A-6B3EB715D869 | NULL | NULL | NULL | NULL | 2025-10-30T10:43:10.8770000 | NULL | False | False | NULL |
| 6BA0FC7D-5ED5-4A44-92A6-A82E7018744D | NULL | NULL | NULL | NULL | 2025-10-30T10:37:22.5930000 | NULL | False | False | NULL |
| 652AB0C3-E8BB-4B0A-8C8B-9CA75F2A1FC8 | NULL | NULL | NULL | NULL | 2025-10-30T10:36:29.0730000 | NULL | False | False | NULL |
| 5C2D786B-6A7A-4B37-AD10-991C931BAB17 | NULL | NULL | NULL | NULL | 2025-10-30T10:44:29.6400000 | NULL | False | False | NULL |
| 565E7021-5C10-476F-B43C-EA72F7B7BD20 | NULL | NULL | NULL | NULL | 2025-10-30T10:38:09.2900000 | NULL | False | False | NULL |
| 48F696BD-2396-4F86-9E07-592E6D78EBD1 | NULL | NULL | NULL | NULL | 2025-10-30T10:37:10.8300000 | NULL | False | False | NULL |
| 44ED0F5E-7B86-4F9A-9A36-C6D368CC5E8C | NULL | NULL | NULL | NULL | 2025-10-30T10:38:38.4030000 | NULL | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.RM_Mill_Data.EquipmentID` -> `XStudio_XBatch.RM_Mill_Mst_Tbl.ID` (Many to One)
