# XStudio_Xbatch.dbo.Organization_Mst_Tbl

**table_kind:** production_data

### What this table is for

- No curated business description or distinguishing column vocabulary found for this table; treat as low-confidence for semantic matching.

**Primary Key:** ID  
**Row Count:** 1  
**Date Range (ModifiedOn):** 2025-07-11T11:45:51.0000000 to 2025-07-11T11:45:51.0000000  

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

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E92DA561-DC73-44B1-BDF4-5E375A53D06F | Sohar Steel Limited | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-11T11:45:51.4300000 | 2025-07-11T11:45:51.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Plant_Mst_Tbl.ParentID` -> `XStudio_XBatch.Organization_Mst_Tbl.ID` (Many to One)
