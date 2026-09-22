# XStudio_Xbatch.dbo.SMS_Production_BestDay_BestMonth_Data

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference best, day, month, date, ftdpercentage, ftdton, mtdpercentage, mtdton, edit, particulars, reportdatetext, srno.

**Primary Key:** —  
**Row Count:** 114  
**Date Range (ModifiedOn):** 2026-02-26T09:36:37.0000000 to 2026-03-09T14:07:57.0000000  

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
| Particulars | varchar | YES | -1 | — |
| UOM | varchar | YES | 100 | — |
| FTDTonBestDay | decimal | YES | 18,4 | — |
| FTDPercentageBestDay | decimal | YES | 18,4 | — |
| MTDTonBestDay | decimal | YES | 18,4 | — |
| MTDPercentageBestDay | decimal | YES | 18,4 | — |
| FTDTonBestMonth | decimal | YES | 18,4 | — |
| MTDPercentageBestMonth | decimal | YES | 18,4 | — |
| FTDPercentageBestMonth | decimal | YES | 18,4 | — |
| MTDTonBestMonth | decimal | YES | 18,4 | — |
| Reportdatetext | varchar | YES | 100 | — |
| Type | varchar | YES | 100 | — |
| BestDayDate | date | YES | — | — |
| BestMonthDate | date | YES | — | — |
| EditID | varchar | YES | 36 | — |
| Srno | int | YES | 10,0 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AC03927F-F17E-414B-90FE-ABAF4A12FF93 | NULL | NULL | NULL | NULL | 2026-02-26T09:35:30.9400000 | NULL | False | False | NULL |
| D9E99582-CF97-4C26-8FBD-67AC56B4AB7A | NULL | NULL | NULL | NULL | 2026-02-26T09:35:30.9400000 | NULL | False | False | NULL |
| 0A42EFE8-7335-409D-8B1E-F7FE886771F7 | NULL | NULL | NULL | NULL | 2026-02-26T09:35:30.9400000 | NULL | False | False | NULL |
| F43CCEEE-D2FB-4F5E-9AB6-0820F3C74226 | NULL | NULL | NULL | NULL | 2026-02-26T09:35:30.9400000 | NULL | False | False | NULL |
| 6694F1F6-3F8B-4C7F-95CF-3A678B8B9703 | NULL | NULL | NULL | NULL | 2026-02-26T09:35:30.9400000 | NULL | False | False | NULL |
| 2DB9DEAE-846B-4130-B894-3CA8136CD483 | NULL | NULL | NULL | NULL | 2026-02-26T09:35:30.9400000 | NULL | False | False | NULL |
| 0401114A-E1F4-4B64-909F-4FB52233E116 | NULL | NULL | NULL | NULL | 2026-02-26T09:35:30.9400000 | NULL | False | False | NULL |
| D660FA44-A11F-4C2D-9F2B-3635249DDFF0 | NULL | NULL | NULL | NULL | 2026-02-26T09:35:30.9400000 | NULL | False | False | NULL |
| 2CF7CC36-5ADF-4655-895D-C5229480DA0D | NULL | NULL | NULL | NULL | 2026-02-26T09:35:30.9400000 | NULL | False | False | NULL |
| 3BACF7C6-5A8C-4E95-9ECE-A1CF25696922 | NULL | NULL | NULL | NULL | 2026-02-26T09:35:30.9400000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DEFD6256-D761-4885-83CF-386906A85B55 | NULL | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-03-09T13:53:12.5200000 | 2026-03-09T14:07:57.0000000 | False | False | NULL |
| 2B4FBB2F-8833-4380-A02F-6AE2838B8BF7 | NULL | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-03-09T13:53:12.5200000 | 2026-03-09T14:07:57.0000000 | False | False | NULL |
| 62CC8926-5D73-421C-A89C-DFC3FCE56BFF | NULL | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-03-09T13:53:12.5200000 | 2026-03-09T14:07:57.0000000 | False | False | NULL |
| C4342E29-4B69-40C7-B762-3CB742BC941B | NULL | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-03-09T13:53:12.5200000 | 2026-03-09T14:07:57.0000000 | False | False | NULL |
| 43E1B9CF-1054-4EAA-813E-7516269AFD55 | NULL | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-03-09T13:53:12.5200000 | 2026-03-09T14:07:57.0000000 | False | False | NULL |
| 713EB1D5-32A2-4F5A-A5C7-D4EC54FDDC0C | NULL | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-03-09T13:53:12.5200000 | 2026-03-09T14:07:56.0000000 | False | False | NULL |
| 8C1AB2EE-5BAB-4466-891F-3D674845990F | NULL | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-03-09T13:53:12.5200000 | 2026-03-09T14:07:56.0000000 | False | False | NULL |
| 98C99775-0BD8-4E6C-9985-36813C63B18D | NULL | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-03-09T13:53:12.5200000 | 2026-03-09T14:07:56.0000000 | False | False | NULL |
| C4FE7575-48B1-4107-B0F9-62BC7B4A9668 | NULL | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-03-09T13:53:12.5200000 | 2026-03-09T14:07:56.0000000 | False | False | NULL |
| 001AF314-4BCD-4BD1-ADBA-C339AAFB99EB | NULL | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-03-09T13:53:12.5200000 | 2026-03-09T14:07:55.0000000 | False | False | NULL |

---
