# XStudio_Xbatch.dbo.RM_Furnace_Combustion_Attribute_Tag_Template_Mst_Tbl

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
| 76346B2C-25CB-421C-B92B-A1551E33B4A3 | Combustion Report | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | NULL | 2026-08-14T12:48:55.4530000 | NULL | False | False | NULL |

---
