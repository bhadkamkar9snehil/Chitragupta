# XStudio_Xbatch.dbo.XMES_SAP_API_Inventory_Error

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference message, body, code, error, location, plant, record, status, storage, success, transaction.

**Primary Key:** ID  
**Row Count:** 0  

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
| RecordID | varchar | YES | 100 | — |
| Body | varchar | YES | -1 | — |
| PlantCode | varchar | YES | 100 | — |
| IsProcessed | bit | YES | — | — |
| Name | varchar | YES | 100 | — |
| ErrorMessage | varchar | YES | -1 | — |
| EntryDateTime | datetime | YES | — | — |
| TransactionID | varchar | YES | 100 | — |
| ParentID | varchar | YES | 36 | — |
| Status | varchar | YES | 50 | — |
| ReportDate | date | YES | — | — |
| StorageLocation | varchar | YES | 100 | — |
| SuccessMessage | varchar | YES | -1 | — |

---
