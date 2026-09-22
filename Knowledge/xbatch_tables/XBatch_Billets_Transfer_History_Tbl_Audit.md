# XStudio_Xbatch.dbo.XBatch_Billets_Transfer_History_Tbl_Audit

**table_kind:** audit_shadow

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference date, billet, inward, location, outward, recieved, status, action, assigned, current, grade, inventory.

> NOTE: this is a generated audit-history shadow of another table. Prefer the base table unless the investigation specifically needs change history.

**Primary Key:** —  
**Row Count:** 0  

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
| BilletNo | varchar | YES | 100 | — |
| SubLotNo | varchar | YES | 100 | — |
| RecievedDate | datetime | YES | — | — |
| InventoryID | varchar | YES | 36 | — |
| LocationType | varchar | YES | 100 | — |
| RecievedBy | varchar | YES | 100 | — |
| StackID | varchar | YES | 36 | — |
| LayerID | varchar | YES | 36 | — |
| MaterialGrade | varchar | YES | 100 | — |
| LocationAssignedDate | datetime | YES | — | — |
| ActionBy | varchar | YES | 36 | — |
| CurrentStatus | varchar | YES | 100 | — |
| InwardStatus | varchar | YES | 100 | — |
| IsInward | bit | YES | — | — |
| Isoutward | bit | YES | — | — |
| OutwardBy | varchar | YES | 36 | — |
| outwardDate | datetime | YES | — | — |
| BilletLength | int | YES | 10,0 | — |

---
