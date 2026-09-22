# XStudio_Xbatch.dbo.RM_Reheating_Furnace_Tag_Mapping_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference color, document, tag, bwhhh, bwhl, bwlll, gthh, ltll, attribute, data, equipment, hhrange.

**Primary Key:** ID  
**Row Count:** 128  
**Date Range (ModifiedOn):** 2025-09-17T18:40:24.4100000 to 2026-07-30T10:14:12.7400000  

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
| 1CCE983A-F0F8-4B65-8598-5C749603AB96 | NULL | NULL | NULL | NULL | 2025-09-17T18:15:53.0270000 | NULL | False | False | NULL |
| 1FA47388-CA31-440B-BF54-435662D4BB1C | NULL | NULL | NULL | NULL | 2025-09-17T18:15:53.0270000 | NULL | False | False | NULL |
| 2FDE514F-811B-4077-976C-A44250217CCF | NULL | NULL | NULL | NULL | 2025-09-17T18:15:53.0270000 | NULL | False | False | NULL |
| 473B095B-E8BF-45AA-8503-317888B574D1 | NULL | NULL | NULL | NULL | 2025-09-17T18:15:53.0270000 | NULL | False | False | NULL |
| 5C318874-3EE7-441D-8E0A-60B1F81929AE | NULL | NULL | NULL | NULL | 2025-09-17T18:15:53.0270000 | NULL | False | False | NULL |
| 64FD110A-A31D-4CB5-8E70-44A5D90A9540 | NULL | NULL | NULL | NULL | 2025-09-18T12:54:09.2370000 | NULL | False | False | NULL |
| 6CA173BD-C0B1-4BD0-9161-4177F0055E78 | NULL | NULL | NULL | NULL | 2025-09-17T18:15:53.0270000 | NULL | False | False | NULL |
| 6F0DAA3D-D80B-4E75-BBA9-27D0ADECC37B | NULL | NULL | NULL | NULL | 2025-09-18T12:54:09.2370000 | NULL | False | False | NULL |
| B83EAA42-A9C5-4943-A525-86B9DB1E0EA9 | NULL | NULL | NULL | NULL | 2025-10-06T09:06:34.2730000 | NULL | False | False | NULL |
| E207A0BB-531A-4930-91BA-32BFB751A636 | NULL | NULL | NULL | NULL | 2025-09-18T12:54:09.2370000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 33980263-CCEB-4189-A87D-150EC4AE6676 | NULL | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-30T10:13:49.8530000 | 2026-07-30T10:14:12.7400000 | False | False | NULL |
| 7FDEF26B-36CA-401A-B1E2-B897E76D6B6E | NULL | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-30T10:13:28.2170000 | 2026-07-30T10:14:12.7400000 | False | False | NULL |
| 9CAEB0B1-EA18-42CB-951B-7DA82568B1AD | NULL | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-09-18T12:54:09.2370000 | 2026-07-30T10:14:12.7400000 | False | False | NULL |
| C98B95C7-B7AD-455F-9B21-E2CD3C327E93 | NULL | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-06-10T09:10:05.6830000 | 2026-06-10T09:11:15.8630000 | False | False | NULL |
| A7530AE1-B2CD-418D-A444-A8EAE46CCEF9 | NULL | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-12-30T09:21:25.0970000 | 2025-12-30T09:22:13.2500000 | False | False | NULL |
| 3906BC31-938E-4FAF-9644-183DB065513C | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T13:33:26.1970000 | 2025-11-26T13:57:37.0330000 | False | False | NULL |
| 2A810172-BECE-4DEA-A3D0-320CF592C95E | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T13:31:44.6700000 | 2025-11-26T13:46:06.8170000 | False | False | NULL |
| 7AD7BD67-DDC0-4796-8DC6-8EA5BE5415C8 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T13:34:47.2470000 | 2025-11-26T13:46:06.8170000 | False | False | NULL |
| BB091C18-3E6C-41DC-B904-78B127FBDFA0 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T13:34:16.3870000 | 2025-11-26T13:46:06.8170000 | False | False | NULL |
| 0CDEE722-18A3-4EBF-88AB-90B4700C5621 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-26T08:32:13.8700000 | 2025-11-26T08:37:56.5930000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.RM_Reheating_Furnace_Tag_Mapping_Tbl.DataSourceID` -> `XStudio_Configuration_XBatch.XStudio_DataSource_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.RM_Reheating_Furnace_Tag_Mapping_Tbl.EquipmentID` -> `XStudio_XBatch.RM_Reheating_Furnace_Mst_Tbl.ID` (Many to One)
