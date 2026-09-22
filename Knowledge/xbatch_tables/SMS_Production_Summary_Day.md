# XStudio_Xbatch.dbo.SMS_Production_Summary_Day

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference production, total, achievedpercentage, target, today, weekly, planned, rate, achieved, asking, equipment, heat.

**Primary Key:** ID  
**Row Count:** 314  
**Date Range (ModifiedOn):** 2025-08-31T14:29:56.9330000 to 2026-07-08T19:30:53.5770000  

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
| ReportDate | date | YES | — | — |
| TodayAchievedpercentage | decimal | YES | 18,4 | — |
| MTDPlannedTon | decimal | YES | 18,4 | — |
| MonthlyTarget | decimal | YES | 18,4 | — |
| TodayPlannedProduction | decimal | YES | 18,4 | — |
| Month | varchar | YES | 100 | — |
| MTDAchievedpercentage | decimal | YES | 18,4 | — |
| RunningRate | decimal | YES | 18,4 | — |
| TotalProduction | decimal | YES | 18,4 | — |
| AskingRate | decimal | YES | 18,4 | — |
| Year | decimal | YES | 18,4 | — |
| YesterdayAchievedpercentage | decimal | YES | 18,4 | — |
| EquipmentID | varchar | YES | 36 | — |
| TotalProduction_YD | decimal | YES | 18,4 | — |
| TotalProduction_MTD | decimal | YES | 18,4 | — |
| TodayPlannedProduction_YD | decimal | YES | 18,4 | — |
| TotalProduction_YTD | decimal | YES | 18,4 | — |
| WeeklyAchievedpercentage | decimal | YES | 18,4 | — |
| WeeklyAchievedProduction | decimal | YES | 18,4 | — |
| WeeklyTarget | decimal | YES | 18,4 | — |
| YearlyTarget | decimal | YES | 18,4 | — |
| LastHeatNo | int | YES | 10,0 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1B3485D-C929-4261-8B39-EF4EB4BE8EE9 | NULL | NULL | NULL | NULL | 2025-08-30T09:53:48.2930000 | 2025-08-31T14:29:56.9330000 | False | False | NULL |
| BF52324D-8C8C-4108-91F7-6F23F5E69D5E | NULL | NULL | NULL | NULL | 2025-08-30T09:54:28.0800000 | 2025-08-31T14:30:27.1970000 | False | False | NULL |
| A6591CCF-8201-41EA-A301-08D738072164 | NULL | NULL | NULL | NULL | 2025-08-30T09:56:08.6270000 | 2025-08-31T15:18:09.8800000 | False | False | NULL |
| 42D23B72-5BB0-4A76-B504-9381FB4D0ABA | NULL | NULL | NULL | NULL | 2025-08-31T13:51:14.4330000 | 2025-09-01T00:13:08.4630000 | False | False | NULL |
| CF29BE99-2E98-42DC-8CA9-6878C803CC34 | NULL | NULL | NULL | NULL | 2025-09-01T01:10:21.9500000 | 2025-09-16T08:04:19.6230000 | False | False | NULL |
| A75D5924-AE53-46FB-8BAF-D4B2C14E36BE | NULL | NULL | NULL | NULL | 2025-09-02T01:12:29.4730000 | 2025-09-16T08:04:19.6270000 | False | False | NULL |
| 33A1B96C-0128-49AE-99AF-9E82EFE8AC8C | NULL | NULL | NULL | NULL | 2025-09-04T01:11:53.0870000 | 2025-09-16T08:04:19.6300000 | False | False | NULL |
| 415CBE3E-E916-4FCC-BEB2-854D6518E4F7 | NULL | NULL | NULL | NULL | 2025-09-03T01:39:16.8600000 | 2025-09-16T08:04:19.6300000 | False | False | NULL |
| 1C9BB519-10AF-4FF8-9E15-1CA5EE08954F | NULL | NULL | NULL | NULL | 2025-09-05T01:04:10.0600000 | 2025-09-16T08:04:19.6330000 | False | False | NULL |
| FC5BD73A-FF14-4B4F-BDF7-9D20676012AB | NULL | NULL | NULL | NULL | 2025-09-06T00:57:47.4930000 | 2025-09-16T08:04:19.6330000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CDB525BF-9F33-4603-ADED-BE5777F65B82 | NULL | NULL | NULL | NULL | 2026-07-08T01:56:06.8430000 | 2026-07-08T19:30:53.5770000 | False | False | NULL |
| B09099BB-98D8-47DE-952D-616D1283DB50 | NULL | NULL | NULL | NULL | 2026-07-07T00:52:25.7200000 | 2026-07-08T00:35:56.9970000 | False | False | NULL |
| 773791B6-FAD5-4013-AA25-B1069C74AF91 | NULL | NULL | NULL | NULL | 2026-07-06T05:33:10.0870000 | 2026-07-07T00:04:29.6100000 | False | False | NULL |
| 69190AC5-BE73-4B3E-9EAB-0774971CDC93 | NULL | NULL | NULL | NULL | 2026-07-05T05:42:58.8900000 | 2026-07-06T00:57:03.8570000 | False | False | NULL |
| 5652A605-56E1-4C61-991D-474AA509456A | NULL | NULL | NULL | NULL | 2026-07-04T01:36:53.4570000 | 2026-07-05T01:33:26.3970000 | False | False | NULL |
| 9FB727CB-96CB-4C72-AB0C-115397D247FB | NULL | NULL | NULL | NULL | 2026-07-03T02:29:40.7570000 | 2026-07-04T00:39:06.3900000 | False | False | NULL |
| 9F9B28C4-7385-41D2-8166-2D8CA881FA57 | NULL | NULL | NULL | NULL | 2026-07-02T06:49:51.7470000 | 2026-07-02T23:40:42.4200000 | False | False | NULL |
| F8E4C9D3-0BAB-4BA8-B491-5B8C00D28403 | NULL | NULL | NULL | NULL | 2026-07-01T00:07:18.2130000 | 2026-07-01T23:46:19.9770000 | False | False | NULL |
| 058C37BB-A42B-47BF-8889-A1C8A4766795 | NULL | NULL | NULL | NULL | 2026-06-30T06:19:50.1230000 | 2026-07-01T00:00:27.0000000 | False | False | NULL |
| F0AD91D7-9AC1-492A-B549-34040B28E4EB | NULL | NULL | NULL | NULL | 2026-06-29T00:27:38.4470000 | 2026-06-30T00:28:30.7770000 | False | False | NULL |

---
