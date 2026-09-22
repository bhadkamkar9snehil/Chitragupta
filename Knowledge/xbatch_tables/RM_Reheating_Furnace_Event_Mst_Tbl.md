# XStudio_Xbatch.dbo.RM_Reheating_Furnace_Event_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference active, entity, event, transaction, type.

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2026-06-06T10:27:07.0000000 to 2026-06-06T10:27:07.0000000  

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
| EventType | varchar | YES | 100 | — |
| TransactionEntity | varchar | YES | 100 | — |
| IsActive | bit | YES | — | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 603FB3BA-3736-499E-8C46-6A6920C5074A | RM Delay | 909bd316-14f2-421e-8cda-1b2329c7f352 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | NULL | 2025-09-05T13:21:12.0000000 | NULL | False | False | NULL |
| 5359CB08-6D63-4837-A715-E70C6649AA89 | BilletsTracking_In_Furnace | 909bd316-14f2-421e-8cda-1b2329c7f352 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | NULL | 2025-09-23T11:52:51.0000000 | NULL | False | False | NULL |
| D9655AF0-93D5-41EF-85F9-B20F781CA938 | ChargingBedToFurnance | 909bd316-14f2-421e-8cda-1b2329c7f352 | 19F651E7-FC5E-4A24-8D95-48F5FE661683 | 19F651E7-FC5E-4A24-8D95-48F5FE661683 | 2026-06-05T15:14:31.0000000 | 2026-06-06T10:27:07.0000000 | False | False | NULL |

---
