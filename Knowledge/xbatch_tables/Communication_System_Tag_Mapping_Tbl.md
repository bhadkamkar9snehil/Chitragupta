# XStudio_Xbatch.dbo.Communication_System_Tag_Mapping_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference color, document, tag, bwhhh, bwhl, bwlll, gthh, ltll, attribute, data, equipment, hhrange.

**Primary Key:** ID  
**Row Count:** 85  
**Date Range (ModifiedOn):** 2026-07-27T08:55:46.5330000 to 2026-07-27T08:55:46.5330000  

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
| Attribute | varchar | YES | 100 | — |
| DataSourceID | varchar | YES | 36 | — |
| TagName | varchar | YES | 100 | — |
| InstrumentTag | varchar | YES | 100 | — |
| HHRange | decimal | YES | 18,4 | — |
| HRange | decimal | YES | 18,4 | — |
| LRange | decimal | YES | 18,4 | — |
| LLRange | decimal | YES | 18,4 | — |
| ColorGTHH | varchar | YES | 100 | — |
| ColorBWHHH | varchar | YES | 100 | — |
| ColorBWHL | varchar | YES | 100 | — |
| ColorBWLLL | varchar | YES | 100 | — |
| ColorLTLL | varchar | YES | 100 | — |
| DocumentGTHH | varchar | YES | 8000 | — |
| DocumentBWHHH | varchar | YES | 8000 | — |
| DocumentBWHL | varchar | YES | 8000 | — |
| DocumentBWLLL | varchar | YES | 8000 | — |
| DocumentLTLL | varchar | YES | 8000 | — |
| Type | varchar | YES | 100 | — |
| IsXBatchTag | bit | YES | — | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 19C0446D-0F6A-4FAA-9056-863942ED8CC5 | NULL | NULL | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-07-27T08:24:27.0900000 | 2026-07-27T08:55:46.5330000 | False | False | NULL |
| 136783DA-229F-472F-A7C3-15953C496263 | NULL | NULL | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-07-27T08:26:55.1270000 | 2026-07-27T08:55:46.5330000 | False | False | NULL |
| 112B389B-70A7-45BB-8750-15E1920781EB | NULL | NULL | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-07-27T08:22:09.6300000 | 2026-07-27T08:55:46.5330000 | False | False | NULL |
| 108818DD-2B29-4139-9E41-21946D755A14 | NULL | NULL | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-07-27T08:22:09.6300000 | 2026-07-27T08:55:46.5330000 | False | False | NULL |
| 10174FED-19FF-488A-BEEE-5D2FF7C87444 | NULL | NULL | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-07-27T08:36:58.8930000 | 2026-07-27T08:55:46.5330000 | False | False | NULL |
| 0E283A96-FCA7-47B3-A5A8-98253F814B0E | NULL | NULL | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-07-27T08:42:22.8930000 | 2026-07-27T08:55:46.5330000 | False | False | NULL |
| 0D743024-6BC7-4A65-B04F-28A768F0B1B6 | NULL | NULL | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-07-27T08:45:46.4200000 | 2026-07-27T08:55:46.5330000 | False | False | NULL |
| 0C6F049B-3E29-471A-81D6-5C28868C5C76 | NULL | NULL | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-07-27T08:45:23.2830000 | 2026-07-27T08:55:46.5330000 | False | False | NULL |
| 09F1FA9D-F3D6-446C-A038-88E0AAA2266D | NULL | NULL | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-07-27T08:22:09.6300000 | 2026-07-27T08:55:46.5330000 | False | False | NULL |
| 08A454E4-F8B9-4C3E-90FB-10262D0EC86B | NULL | NULL | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-07-27T08:44:13.1300000 | 2026-07-27T08:55:46.5330000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 19C0446D-0F6A-4FAA-9056-863942ED8CC5 | NULL | NULL | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-07-27T08:24:27.0900000 | 2026-07-27T08:55:46.5330000 | False | False | NULL |
| 136783DA-229F-472F-A7C3-15953C496263 | NULL | NULL | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-07-27T08:26:55.1270000 | 2026-07-27T08:55:46.5330000 | False | False | NULL |
| 112B389B-70A7-45BB-8750-15E1920781EB | NULL | NULL | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-07-27T08:22:09.6300000 | 2026-07-27T08:55:46.5330000 | False | False | NULL |
| 108818DD-2B29-4139-9E41-21946D755A14 | NULL | NULL | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-07-27T08:22:09.6300000 | 2026-07-27T08:55:46.5330000 | False | False | NULL |
| 10174FED-19FF-488A-BEEE-5D2FF7C87444 | NULL | NULL | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-07-27T08:36:58.8930000 | 2026-07-27T08:55:46.5330000 | False | False | NULL |
| 0E283A96-FCA7-47B3-A5A8-98253F814B0E | NULL | NULL | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-07-27T08:42:22.8930000 | 2026-07-27T08:55:46.5330000 | False | False | NULL |
| 0D743024-6BC7-4A65-B04F-28A768F0B1B6 | NULL | NULL | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-07-27T08:45:46.4200000 | 2026-07-27T08:55:46.5330000 | False | False | NULL |
| 0C6F049B-3E29-471A-81D6-5C28868C5C76 | NULL | NULL | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-07-27T08:45:23.2830000 | 2026-07-27T08:55:46.5330000 | False | False | NULL |
| 09F1FA9D-F3D6-446C-A038-88E0AAA2266D | NULL | NULL | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-07-27T08:22:09.6300000 | 2026-07-27T08:55:46.5330000 | False | False | NULL |
| 08A454E4-F8B9-4C3E-90FB-10262D0EC86B | NULL | NULL | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2026-07-27T08:44:13.1300000 | 2026-07-27T08:55:46.5330000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Communication_System_Tag_Mapping_Tbl.DataSourceID` -> `XStudio_Configuration_XBatch.XStudio_DataSource_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Communication_System_Tag_Mapping_Tbl.EquipmentID` -> `XStudio_XBatch.Communication_System_Mst_Tbl.ID` (Many to One)
