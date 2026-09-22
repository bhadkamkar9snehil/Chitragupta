# XStudio_Xbatch.dbo.SMS_Production_Data_Audit

**table_kind:** audit_shadow

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference achieved, percentage, today, yesterday, mtdachieved, planned, rate, asking, monthly, mtdplanned, running, target.

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
| MonthlyTarget | decimal | YES | 18,4 | — |
| YesterdayPlanned | decimal | YES | 18,4 | — |
| YesterdayAchieved | decimal | YES | 18,4 | — |
| YesterdayAchievedPercentage | decimal | YES | 18,4 | — |
| MTDPlanned | decimal | YES | 18,4 | — |
| MTDAchieved | decimal | YES | 18,4 | — |
| MTDAchievedPercentage | decimal | YES | 18,4 | — |
| AskingRate | decimal | YES | 18,4 | — |
| YTD | decimal | YES | 18,4 | — |
| TodayPlanned | decimal | YES | 18,4 | — |
| TodayAchieved | decimal | YES | 18,4 | — |
| TodayAchievedPercentage | decimal | YES | 18,4 | — |
| RunningRate | decimal | YES | 18,4 | — |

---
