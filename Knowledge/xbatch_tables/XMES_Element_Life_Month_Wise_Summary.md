# XStudio_Xbatch.dbo.XMES_Element_Life_Month_Wise_Summary

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference avg, life, month, down, eafavg, full, ladle, number, seq, shell, total, tundish.

**Primary Key:** ID  
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
| Month | varchar | YES | 100 | — |
| MonthNumber | int | YES | 10,0 | — |
| Year | int | YES | 10,0 | — |
| ShellFullDown | int | YES | 10,0 | — |
| EAFAvgLife | int | YES | 10,0 | — |
| LadleAvgLife | int | YES | 10,0 | — |
| TotalTundishUsed | int | YES | 10,0 | — |
| AvgSeq | int | YES | 10,0 | — |

---
