# XStudio_Xbatch.dbo.RM_LogBook_For_Stand_Assembly_Audit

**table_kind:** audit_shadow

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference name, technician, job, shift, description, incharge, pending.

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
| ShiftInchargeName | varchar | YES | 100 | — |
| Shift | varchar | YES | 100 | — |
| TechnicianName1 | varchar | YES | 100 | — |
| TechnicianName2 | varchar | YES | 100 | — |
| TechnicianName3 | varchar | YES | 100 | — |
| SrNo | int | YES | 10,0 | — |
| JobDescription | varchar | YES | 100 | — |
| PendingJob | varchar | YES | 100 | — |

---
