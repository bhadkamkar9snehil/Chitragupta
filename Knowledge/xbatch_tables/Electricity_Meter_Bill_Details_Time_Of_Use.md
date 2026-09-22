# XStudio_Xbatch.dbo.Electricity_Meter_Bill_Details_Time_Of_Use

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference month, year, charge, consumption, feeder, name, number, rate, timeof, use.

**Primary Key:** ID  
**Row Count:** 56  
**Date Range (ModifiedOn):** 2026-05-28T16:22:02.0000000 to 2026-05-29T08:16:22.0000000  

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
| Charge | decimal | YES | 18,4 | — |
| Rate | varchar | YES | 100 | — |
| Consumption | decimal | YES | 18,4 | — |
| TimeofUse | varchar | YES | -1 | — |
| FeederName | varchar | YES | 100 | — |
| Year | int | YES | 10,0 | — |
| MonthNumber | int | YES | 10,0 | — |
| Month | varchar | YES | 100 | — |
| MonthYear | varchar | YES | -1 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 25809B39-1EDD-4FC1-80B9-AEABC486CB2C | NULL | NULL | NULL | NULL | 2026-06-02T00:32:48.6600000 | NULL | False | False | NULL |
| 25061163-848D-44AF-ABFA-854124B31257 | NULL | NULL | NULL | NULL | 2026-09-02T07:10:19.6570000 | NULL | False | False | NULL |
| 244BA96D-AFF5-4BB6-8D1B-7024E5FA5B5A | NULL | NULL | NULL | NULL | 2026-09-02T07:10:19.6570000 | NULL | False | False | NULL |
| 225F7A69-66EB-4D40-84CF-75334FA50753 | NULL | NULL | NULL | NULL | 2026-09-02T07:10:19.6570000 | NULL | False | False | NULL |
| 06EB6C19-3728-444B-B0E8-017ADCBC714C | NULL | NULL | NULL | NULL | 2026-05-28T15:21:14.8900000 | NULL | False | False | NULL |
| 04B9734F-DED8-433B-8277-3A81C3A186B9 | NULL | NULL | NULL | NULL | 2026-07-03T09:30:57.6870000 | NULL | False | False | NULL |
| 03A3A6A5-0FD7-4363-8F12-28D416EE6319 | NULL | NULL | NULL | NULL | 2026-08-03T09:12:22.6570000 | NULL | False | False | NULL |
| 3FD4EBD7-BDC2-496C-8A12-B2195909B100 | NULL | NULL | NULL | NULL | 2026-05-28T15:21:14.8900000 | NULL | False | False | NULL |
| 445812E0-EA3A-4437-8D81-3BA9961F884C | NULL | NULL | NULL | NULL | 2026-06-02T00:32:48.6600000 | NULL | False | False | NULL |
| 4476DE2D-C32D-4399-BEDA-843E39F181D6 | NULL | NULL | NULL | NULL | 2026-08-03T09:12:22.6570000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 074B6907-520C-4221-8E52-7ACA94B6F847 | NULL | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-05-28T16:14:43.6600000 | 2026-05-29T08:16:22.0000000 | False | False | NULL |
| 5448C3BC-151D-473D-8310-1358A4F93282 | NULL | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-05-28T16:14:43.6600000 | 2026-05-29T08:16:22.0000000 | False | False | NULL |
| B5F28ECC-570F-4040-90D6-2692AD68515F | NULL | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-05-28T16:14:43.6600000 | 2026-05-29T08:16:22.0000000 | False | False | NULL |
| B83B9D2F-1759-420C-8A3A-3E3AB301386A | NULL | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-05-28T16:14:43.6600000 | 2026-05-29T08:16:22.0000000 | False | False | NULL |
| 348C02A1-57B0-4216-BDB7-DEFC6F4D9959 | NULL | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-05-28T16:14:43.6600000 | 2026-05-28T16:23:52.0000000 | False | False | NULL |
| CE25DD1D-7E1F-425B-97CF-BCB79AD9B7A0 | NULL | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-05-28T16:14:43.6600000 | 2026-05-28T16:23:52.0000000 | False | False | NULL |
| F536851F-6353-490C-85A5-09C1B0D4F358 | NULL | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-05-28T16:14:43.6600000 | 2026-05-28T16:23:52.0000000 | False | False | NULL |
| 2EEE5822-55D2-43E4-86E2-BEBC53EFF0A5 | NULL | NULL | NULL | B5257AE5-62A9-42F0-BBA2-714E1EE39ED9 | 2026-05-28T16:14:43.6600000 | 2026-05-28T16:22:02.0000000 | False | False | NULL |
| 3FD4EBD7-BDC2-496C-8A12-B2195909B100 | NULL | NULL | NULL | NULL | 2026-05-28T15:21:14.8900000 | NULL | False | False | NULL |
| 25809B39-1EDD-4FC1-80B9-AEABC486CB2C | NULL | NULL | NULL | NULL | 2026-06-02T00:32:48.6600000 | NULL | False | False | NULL |

---
