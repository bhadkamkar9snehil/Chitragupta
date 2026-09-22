# XStudio_Xbatch.dbo.RM_Reheating_Furnace_Event_Configuration_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference event, active, entity, mst, transaction, type.

**Primary Key:** ID  
**Row Count:** 3  

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
| EventMstID | varchar | YES | 36 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F2A00B44-251D-45AD-8FC9-9217F7FD8647 | RM Delay | 8B31EC90-6F8B-4C62-95D3-54B982DAE1A8 | NULL | NULL | 2025-09-05T13:21:12.0330000 | NULL | False | False | NULL |
| 2FAB31D6-55BE-45CC-A7E5-30B5D68A2CC9 | ChargingBedToFurnance | 8B31EC90-6F8B-4C62-95D3-54B982DAE1A8 | NULL | NULL | 2026-06-05T15:14:31.3970000 | NULL | False | False | NULL |
| 0CF6B384-57C0-4C52-A41B-A9727B57F860 | BilletsTracking_In_Furnace | 8B31EC90-6F8B-4C62-95D3-54B982DAE1A8 | NULL | NULL | 2025-09-23T11:52:51.4700000 | NULL | False | False | NULL |

---
