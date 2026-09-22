# XStudio_Xbatch.dbo.SMS_Production_Data

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference achieved, percentage, today, yesterday, mtdachieved, planned, rate, asking, monthly, mtdplanned, running, target.

**Primary Key:** ID  
**Row Count:** 1  
**Date Range (ModifiedOn):** 2025-08-27T15:48:44.0000000 to 2025-08-27T15:48:44.0000000  

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

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 45F3436B-BB6D-468D-A2BB-6D67EBD8BA28 | NULL | NULL | E85231EB-0A04-42D6-A407-328F17EADEFE | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-08-26T18:27:30.8230000 | 2025-08-27T15:48:44.0000000 | False | False | NULL |

---
