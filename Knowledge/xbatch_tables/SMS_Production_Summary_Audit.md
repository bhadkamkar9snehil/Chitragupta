# XStudio_Xbatch.dbo.SMS_Production_Summary_Audit

**table_kind:** audit_shadow

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference best, date, day, month, ftdpercentage, ftdton, mtdpercentage, mtdton, particulars, reportdatetext, target, type.

> NOTE: this is a generated audit-history shadow of another table. Prefer the base table unless the investigation specifically needs change history.

**Primary Key:** —  
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
| Reportdatetext | varchar | YES | 100 | — |
| Target | decimal | YES | 18,4 | — |
| FTDPercentage | decimal | YES | 18,4 | — |
| BestMonth | decimal | YES | 18,4 | — |
| ReportDate | date | YES | — | — |
| Particulars | varchar | YES | 36 | — |
| Type | varchar | YES | 100 | — |
| FTDTon | decimal | YES | 18,4 | — |
| EntryDateTime | datetime | YES | — | — |
| IsProcessed | bit | YES | — | — |
| MTDTon | decimal | YES | 18,4 | — |
| ParentID | varchar | YES | 36 | — |
| BestDay | decimal | YES | 18,4 | — |
| Name | varchar | YES | 100 | — |
| UOM | varchar | YES | 36 | — |
| MTDPercentage | decimal | YES | 18,4 | — |
| BestDayDate | date | YES | — | — |
| BestMonthDate | date | YES | — | — |

---
