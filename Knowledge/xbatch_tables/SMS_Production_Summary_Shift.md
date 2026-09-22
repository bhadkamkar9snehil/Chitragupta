# XStudio_Xbatch.dbo.SMS_Production_Summary_Shift

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference achievedpercentage, production, target, weekly, rate, today, achieved, asking, equipment, month, monthly, mtdachievedpercentage.

**Primary Key:** ID  
**Row Count:** 611  
**Date Range (ModifiedOn):** 2025-09-01T16:51:34.5400000 to 2026-07-08T19:30:53.4900000  

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
| Entrydatetime | datetime | YES | — | — |
| ShiftName | varchar | YES | 100 | — |
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
| WeeklyAchievedpercentage | decimal | YES | 18,4 | — |
| WeeklyAchievedProduction | decimal | YES | 18,4 | — |
| WeeklyTarget | decimal | YES | 18,4 | — |
| YearlyTarget | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 48E25EA7-280E-489F-8CA1-F6BC00257C69 | NULL | NULL | NULL | NULL | 2025-09-01T16:51:34.4770000 | 2025-09-01T16:51:34.5400000 | False | False | NULL |
| 9BAE09DE-F650-423A-8728-FB71150A9166 | NULL | NULL | NULL | NULL | 2025-09-01T16:53:41.5100000 | 2025-09-01T16:53:41.5630000 | False | False | NULL |
| 1CFF4D3E-5C77-4FD4-959B-0D52CF312C9C | NULL | NULL | NULL | NULL | 2025-09-02T07:26:35.9230000 | 2025-09-15T14:23:40.9800000 | False | False | NULL |
| 31359302-E36E-46F8-A6D6-DD83E6E82EF9 | NULL | NULL | NULL | NULL | 2025-09-02T19:09:47.9600000 | 2025-09-15T14:24:00.9300000 | False | False | NULL |
| F7CC70C8-CB94-49BE-8FC4-2ED4334196D4 | NULL | NULL | NULL | NULL | 2025-09-03T07:15:43.5230000 | 2025-09-15T14:24:02.8100000 | False | False | NULL |
| 3225E368-DBAF-430E-B8CC-C1B6BBD64263 | NULL | NULL | NULL | NULL | 2025-09-03T19:21:53.9570000 | 2025-09-15T14:24:34.5370000 | False | False | NULL |
| 070C567F-6C05-4BC6-B994-54689277B951 | NULL | NULL | NULL | NULL | 2025-09-04T07:48:37.0900000 | 2025-09-15T14:24:36.7570000 | False | False | NULL |
| 147061B8-A2A1-4B19-8247-48B481B1128F | NULL | NULL | NULL | NULL | 2025-09-04T19:43:56.4770000 | 2025-09-15T14:24:48.3670000 | False | False | NULL |
| E91DF71A-42EC-4954-8AC5-1D4DEA47B087 | NULL | NULL | NULL | NULL | 2025-09-05T07:34:31.6600000 | 2025-09-15T14:24:51.1130000 | False | False | NULL |
| 41C212B8-A196-42E5-8FCA-7436C65BFF7C | NULL | NULL | NULL | NULL | 2025-09-05T19:48:42.0500000 | 2025-09-15T14:25:38.9030000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AD5980B7-8A83-451B-A2E4-1676CCD60317 | NULL | NULL | NULL | NULL | 2026-07-08T19:15:19.8900000 | 2026-07-08T19:30:53.4900000 | False | False | NULL |
| 434BD3A6-A0C8-436E-97D3-60DA8A5B3BF6 | NULL | NULL | NULL | NULL | 2026-07-08T07:21:02.9130000 | 2026-07-08T18:23:06.4630000 | False | False | NULL |
| FB740168-072F-40E8-B277-7FF45D771312 | NULL | NULL | NULL | NULL | 2026-07-07T19:10:07.2800000 | 2026-07-08T06:30:29.5070000 | False | False | NULL |
| 329AA09A-6641-4ECC-8583-E6DE94D8F1AC | NULL | NULL | NULL | NULL | 2026-07-07T07:38:55.1500000 | 2026-07-07T18:13:48.3530000 | False | False | NULL |
| 71CCCA42-1803-45D0-9600-249A0BFB5E25 | NULL | NULL | NULL | NULL | 2026-07-06T19:25:07.6470000 | 2026-07-07T06:36:51.7670000 | False | False | NULL |
| 34F4755D-2959-4BC8-853C-0F32D2AC2570 | NULL | NULL | NULL | NULL | 2026-07-06T07:46:31.9500000 | 2026-07-06T18:23:24.5800000 | False | False | NULL |
| 90750B47-C97B-4461-80B4-7060F31984F5 | NULL | NULL | NULL | NULL | 2026-07-05T19:44:32.1600000 | 2026-07-06T06:44:04.9000000 | False | False | NULL |
| 6FF013B6-0D61-44CE-A26C-89BF21780ED2 | NULL | NULL | NULL | NULL | 2026-07-05T07:35:04.7200000 | 2026-07-05T16:40:32.1970000 | False | False | NULL |
| AD784E41-1FDC-4EDE-B8DF-9EEB6D8925FB | NULL | NULL | NULL | NULL | 2026-07-04T19:13:20.6370000 | 2026-07-05T06:37:44.1300000 | False | False | NULL |
| 3C933F70-7AB8-49D6-B6C3-C8D0F8C46D93 | NULL | NULL | NULL | NULL | 2026-07-04T07:04:00.9270000 | 2026-07-04T18:09:20.9630000 | False | False | NULL |

---
