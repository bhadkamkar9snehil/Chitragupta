# XStudio_Xbatch.dbo.Round_Bar_Quality_Data

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** chemistry, quality, spectro (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference size, area, billet, bottom, cross, elmechanical, grade, heat, mechanical, ovality, section, shift.

**Primary Key:** ID  
**Row Count:** 2  
**Date Range (ModifiedOn):** 2025-12-12T15:39:36.0000000 to 2025-12-12T15:39:36.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
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
| ReportDate | varchar | YES | 100 | — |
| EntryDateTime | datetime | YES | — | — |
| ParentID | varchar | YES | 36 | — |
| Side | decimal | YES | 18,4 | — |
| ToporBottomSize | decimal | YES | 18,4 | — |
| OvalitySize | decimal | YES | 18,4 | — |
| WtMechanical | decimal | YES | 18,4 | — |
| Name | varchar | YES | 100 | — |
| Grade | varchar | YES | 36 | — |
| BilletNo | varchar | YES | 36 | — |
| S2Size | decimal | YES | 18,4 | — |
| CrossSectionArea | decimal | YES | 18,4 | — |
| HeatNo | varchar | YES | 36 | — |
| IsProcessed | bit | YES | — | — |
| S1Size | decimal | YES | 18,4 | — |
| YSMechanical | int | YES | 10,0 | — |
| ELMechanical | decimal | YES | 18,4 | — |
| UTSMechanical | int | YES | 10,0 | — |
| Shift | varchar | YES | 100 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F15E5C61-5156-483D-9A6F-0A48DE39BB97 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-26T09:16:43.4500000 | 2025-12-12T15:39:36.0000000 | False | False | NULL | 172.16.6.34 |  |
| 96BD76EF-5DD3-4BBA-A1BF-F5FF57385AF1 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2025-11-25T17:19:46.4300000 | 2025-12-12T15:39:36.0000000 | False | False | NULL | 172.16.6.34 |  |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Round_Bar_Quality_Data.Grade` -> `XStudio_XBatch.Grade_Master.GradeName` (Many to One)
- `XStudio_XBatch.Round_Bar_Quality_Data.HeatNo` -> `XStudio_XBatch.EAF_PER_HEAT.ID` (Many to One)
