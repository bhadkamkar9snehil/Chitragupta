# XStudio_Xbatch.dbo.LRF_SMS_Attribute_Tag_Template_Mst_Tbl

**table_kind:** production_data

### What this table is for

- No curated business description or distinguishing column vocabulary found for this table; treat as low-confidence for semantic matching.

**Primary Key:** ID  
**Row Count:** 1  

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
| 8DCE2FBA-60F5-487F-950C-C1A159FA3057 | LRF | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | NULL | 2025-07-22T08:49:01.5330000 | NULL | False | False | NULL |

---
