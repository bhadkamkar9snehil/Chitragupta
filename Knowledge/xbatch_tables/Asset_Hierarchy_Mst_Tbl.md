# XStudio_Xbatch.dbo.Asset_Hierarchy_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference number, serial.

**Primary Key:** ID  
**Row Count:** 2  
**Date Range (ModifiedOn):** 2025-07-11T11:44:12.0000000 to 2025-07-11T11:44:12.0000000  

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
| SerialNumber | int | YES | 10,0 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CE80EB60-E76A-4226-A847-E46AD531EF6B | Organization | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | NULL | 2025-07-11T11:44:12.6930000 | NULL | False | False | NULL |
| 18EE262D-F915-460E-B261-851413BB007B | Plant | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-11T11:43:38.6330000 | 2025-07-11T11:44:12.0000000 | False | False | NULL |

---
