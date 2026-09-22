# XStudio_Xbatch.dbo.EAF_LogSheet_Ladle_Details

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** billet, furnace, heat, production, tracking (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference life, heat, plug, porous, after, any, checked, conditions, gate, grade, laddle, ladle.

**Primary Key:** ID  
**Row Count:** 1  
**Date Range (ModifiedOn):** 2025-08-02T10:28:02.0000000 to 2025-08-02T10:28:02.0000000  

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
| EntryDateTime | datetime | YES | — | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| Conditions | varchar | YES | 36 | — |
| Heat1stAfterRelining | int | YES | 10,0 | — |
| LadleLife | int | YES | 10,0 | — |
| PorousPlugLife | int | YES | 10,0 | — |
| SlideGatePlateLife | int | YES | 10,0 | — |
| PorousPlugChecked | int | YES | 10,0 | — |
| SpecialRemarkIfAny | varchar | YES | 100 | — |
| HeatNo | varchar | YES | 100 | — |
| Grade | varchar | YES | 100 | — |
| LaddleNumber | varchar | YES | 36 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 39B50AA4-5686-41AE-B36B-B84C74C9D29F | NULL | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-21T13:04:07.6570000 | 2025-08-02T10:28:02.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.EAF_LogSheet_Ladle_Details.LaddleNumber` -> `XStudio_XBatch.LRF_Ladle_Number_Master.LadleNumber` (Many to One)
