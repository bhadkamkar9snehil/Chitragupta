# XStudio_Xbatch.dbo.RM_WRM_Pass_Card_Audit

**table_kind:** audit_shadow

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference pass, rolled, tonnage, groove, status, date, name, notch, outmm, ring, wear, diameter.

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
| SectionName | varchar | YES | 100 | — |
| StandNo | int | YES | 10,0 | — |
| GrooveNameP1 | varchar | YES | 100 | — |
| GrooveNameP2 | varchar | YES | 100 | — |
| RingNo | int | YES | 10,0 | — |
| RingDiameter | int | YES | 10,0 | — |
| P1PassDate | datetime | YES | — | — |
| P1PassStatus | varchar | YES | 100 | — |
| P1PassStatusNotch | varchar | YES | 100 | — |
| P1PassRolledTonnageDate | datetime | YES | — | — |
| P1PassTonnageRolled | int | YES | 10,0 | — |
| P1PassRolledTonnageGrooveWearOutmm | decimal | YES | 18,4 | — |
| P2PassStatus | varchar | YES | 100 | — |
| P2PassStatusNotch | varchar | YES | 100 | — |
| P2PassRolledTonnageDate | datetime | YES | — | — |
| P2PassTonnageRolled | int | YES | 10,0 | — |
| P2PassRolledTonnageGrooveWearOutmm | decimal | YES | 18,4 | — |
| TotalTunnage | int | YES | 10,0 | — |

---
