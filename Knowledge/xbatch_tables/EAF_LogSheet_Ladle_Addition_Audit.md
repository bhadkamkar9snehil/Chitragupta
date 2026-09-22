# XStudio_Xbatch.dbo.EAF_LogSheet_Ladle_Addition_Audit

**table_kind:** audit_shadow

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference cpc, aiingots, hcfe, heat, lime, quality, spar, stamp, tag, time.

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
| SiMn | decimal | YES | 18,4 | — |
| HCFeMn | decimal | YES | 18,4 | — |
| FeSi | decimal | YES | 18,4 | — |
| AIingots | decimal | YES | 18,4 | — |
| CPC | decimal | YES | 18,4 | — |
| CPC_Tag | varchar | YES | 100 | — |
| CPC_TimeStamp | datetime | YES | — | — |
| CPC_Quality | int | YES | 10,0 | — |
| Lime | decimal | YES | 18,4 | — |
| Spar | decimal | YES | 18,4 | — |
| HeatID | varchar | YES | 100 | — |

---
