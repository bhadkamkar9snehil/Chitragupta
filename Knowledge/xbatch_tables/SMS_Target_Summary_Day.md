# XStudio_Xbatch.dbo.SMS_Target_Summary_Day

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** catalog, entities, entity, from, highlights, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference actual, billet, production, today, ton, weight, achievedpercentage, target, weekly, planned, rate, achieved.

**Primary Key:** ID  
**Row Count:** 378  
**Date Range (ModifiedOn):** 2026-07-17T17:15:24.9670000 to 2026-08-12T08:44:31.9400000  

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
| ReportDate | date | YES | — | — |
| AskingRate | decimal | YES | 18,2 | — |
| TodayPlannedProduction | decimal | YES | 18,2 | — |
| YearlyTarget | decimal | YES | 18,0 | — |
| WeeklyTarget | decimal | YES | 18,0 | — |
| ActualBilletWeightTon | decimal | YES | 18,2 | — |
| TodayAchievedpercentage | decimal | YES | 18,2 | — |
| MTDPlannedProduction | decimal | YES | 18,2 | — |
| MTDAchievedpercentage | decimal | YES | 18,2 | — |
| MonthlyTarget | decimal | YES | 18,0 | — |
| WeeklyAchievedProduction | decimal | YES | 18,2 | — |
| RunningRate | decimal | YES | 18,2 | — |
| WeeklyAchievedpercentage | decimal | YES | 18,2 | — |
| TodayAchievedpercentage_YD | decimal | YES | 18,2 | — |
| TodayPlannedProduction_YD | decimal | YES | 18,2 | — |
| ActualBilletWeightTon_YTD | decimal | YES | 18,2 | — |
| ActualBilletWeightTon_MTD | decimal | YES | 18,2 | — |
| ActualBilletWeightTon_YD | decimal | YES | 18,2 | — |
| Month | varchar | YES | 100 | — |
| HeatID | int | YES | 10,0 | — |
| Year | int | YES | 10,0 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 006C86E4-19E0-40A1-876C-A6990810C251 | NULL | NULL | 2026-08-16T01:30:23.7970000 | NULL | False | False | NULL | NULL | NULL |
| 08AF9F86-B7AE-4D86-9671-4F944746CCC9 | NULL | NULL | 2026-07-19T18:16:41.9130000 | NULL | False | False | NULL | NULL | NULL |
| 065CF9A9-22C1-4844-A96B-8A7074416B29 | NULL | NULL | 2026-08-08T01:30:24.1900000 | NULL | False | False | NULL | NULL | NULL |
| 0622646B-15A9-4113-9639-8AECCA1C2221 | NULL | NULL | 2026-07-29T01:30:21.7930000 | NULL | False | False | NULL | NULL | NULL |
| 05F86890-4774-493F-9EF5-C6384AB4A59F | NULL | NULL | 2026-08-27T06:00:34.1930000 | NULL | False | False | NULL | NULL | NULL |
| 05BC0971-029C-4334-BA8E-B08DB31025AD | NULL | NULL | 2026-08-24T06:00:32.0930000 | NULL | False | False | NULL | NULL | NULL |
| 04510979-7D1B-406D-8AE7-9AEE5A51BA45 | NULL | NULL | 2026-08-04T01:30:22.3200000 | NULL | False | False | NULL | NULL | NULL |
| 0165F08F-F66E-430C-81C6-B2CAA382DA3C | NULL | NULL | 2026-08-24T01:30:20.2030000 | NULL | False | False | NULL | NULL | NULL |
| 011E9C60-40F0-4741-A037-25A2A0C1BB25 | NULL | NULL | 2026-08-09T01:30:20.9670000 | NULL | False | False | NULL | NULL | NULL |
| 0ADABC7C-05C5-497E-9263-688B8D28283A | NULL | NULL | 2026-07-22T06:00:18.0170000 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D1273894-60D9-4A9B-AA30-6D9EA0A62A0E | NULL | NULL | 2026-07-17T14:22:39.1770000 | 2026-08-12T08:44:31.9400000 | False | False | NULL | NULL | NULL |
| F70FD987-8047-40A2-A499-4464FF23052F | NULL | NULL | 2026-07-17T14:22:39.1670000 | 2026-07-19T18:18:06.2000000 | False | False | NULL | NULL | NULL |
| 3A9ABED7-7ADD-4A61-951D-84EC0987A10D | NULL | NULL | 2026-07-17T14:22:39.1570000 | 2026-07-17T17:19:44.6470000 | False | False | NULL | NULL | NULL |
| 4DD4F08C-D350-4622-9CD5-1A656BBCE843 | NULL | NULL | 2026-07-17T14:22:39.1470000 | 2026-07-17T17:19:44.6430000 | False | False | NULL | NULL | NULL |
| 459A49B7-293B-4D6C-AE75-48A7BABB4E59 | NULL | NULL | 2026-07-17T14:22:39.1230000 | 2026-07-17T17:19:44.6400000 | False | False | NULL | NULL | NULL |
| D781EE01-8C33-473E-B5F3-AF0581F15F75 | NULL | NULL | 2026-07-17T14:22:39.1130000 | 2026-07-17T17:19:44.6370000 | False | False | NULL | NULL | NULL |
| 7CAF057F-5E4A-49B7-906A-274019CF0891 | NULL | NULL | 2026-07-17T14:22:39.1030000 | 2026-07-17T17:19:44.6330000 | False | False | NULL | NULL | NULL |
| 36254AC1-193E-4252-A86D-4C003F654F64 | NULL | NULL | 2026-07-17T14:22:39.0930000 | 2026-07-17T17:19:44.6300000 | False | False | NULL | NULL | NULL |
| BCA67630-F41D-4472-9BB0-055DCC422637 | NULL | NULL | 2026-07-17T14:22:39.0800000 | 2026-07-17T17:19:44.6230000 | False | False | NULL | NULL | NULL |
| 366E4D5C-DA36-47A3-94D1-73EFD292D5AA | NULL | NULL | 2026-07-17T14:22:39.0700000 | 2026-07-17T17:19:44.6170000 | False | False | NULL | NULL | NULL |

---
