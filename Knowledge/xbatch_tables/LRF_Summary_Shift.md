# XStudio_Xbatch.dbo.LRF_Summary_Shift

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference liquid, metal, weight, avg, calc, consumption, aluminium, argon, carbon, dolo, electrode, flour.

**Primary Key:** ID  
**Row Count:** 1,510  
**Date Range (ModifiedOn):** 2025-07-25T18:53:40.6770000 to 2026-07-19T18:16:42.7500000  

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
| HeatID | decimal | YES | 18,4 | — |
| PowerMWH | decimal | YES | 18,4 | — |
| ArgonConsumption | decimal | YES | 18,4 | — |
| FeSi | decimal | YES | 18,4 | — |
| Dolo | decimal | YES | 18,4 | — |
| SiMn | decimal | YES | 18,4 | — |
| SiMnn | decimal | YES | 18,4 | — |
| LiquidMetalWeight | decimal | YES | 18,4 | — |
| Avg_LiquidMetalWeight | decimal | YES | 18,4 | — |
| Lime | decimal | YES | 18,4 | — |
| CalcLiquidMetalWeight | decimal | YES | 18,4 | — |
| Avg_CalcLiquidMetalWeight | decimal | YES | 18,4 | — |
| TotalElectrodeConsumptionKg | decimal | YES | 18,4 | — |
| Carbon | decimal | YES | 18,4 | — |
| Aluminium | decimal | YES | 18,4 | — |
| FlourSpar | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00B9532C-74D4-4A2D-86FD-763C0444BE74 | NULL | NULL | NULL | NULL | 2025-12-23T00:34:39.8600000 | NULL | False | False | NULL |
| 0089FEC4-079D-4AED-A4AA-197D2F81624C | NULL | NULL | NULL | NULL | 2025-10-13T17:00:17.5870000 | NULL | False | False | NULL |
| 0070893C-7E4F-40F8-958C-6CC68407C945 | NULL | NULL | NULL | NULL | 2026-01-20T21:52:33.8970000 | NULL | False | False | NULL |
| 001DFADF-6670-4F53-8972-8FBEBDC69DDD | NULL | NULL | NULL | NULL | 2026-06-21T06:53:07.8770000 | NULL | False | False | NULL |
| 021632D4-7415-44E5-8D99-B11720E2016E | NULL | NULL | NULL | NULL | 2026-08-02T01:30:23.0800000 | NULL | False | False | NULL |
| 01F6E02C-36D1-4A73-A501-213368701675 | NULL | NULL | NULL | NULL | 2025-12-16T16:25:08.4670000 | NULL | False | False | NULL |
| 01EE3493-FA90-4866-A6AC-F4C506674529 | NULL | NULL | NULL | NULL | 2026-05-21T11:01:32.9000000 | NULL | False | False | NULL |
| 01C4DD03-ECE1-44F2-B1A3-56E749709B65 | NULL | NULL | NULL | NULL | 2026-02-14T03:08:05.4400000 | NULL | False | False | NULL |
| 0122A021-D814-4498-AAB9-0F8126A9BD28 | NULL | NULL | NULL | NULL | 2025-12-06T18:03:58.4100000 | NULL | False | False | NULL |
| 0226782E-02E8-4648-B027-3C38369B73F4 | NULL | NULL | NULL | NULL | 2026-05-15T12:32:51.9400000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2DC2D89E-7F50-4C05-949D-C75299B35367 | NULL | NULL | NULL | NULL | 2026-07-08T03:03:55.0600000 | 2026-07-19T18:16:42.7500000 | False | False | NULL |
| 712EB92A-9E82-4BCD-BBB3-7542AA122617 | NULL | NULL | NULL | NULL | 2026-07-07T05:04:57.4000000 | 2026-07-19T18:16:35.9070000 | False | False | NULL |
| 1E102E25-B8BA-458C-97BE-8FFB1395E5A5 | NULL | NULL | NULL | NULL | 2026-02-20T01:55:02.4070000 | 2026-07-17T17:19:47.7200000 | False | False | NULL |
| 90ED0EA7-0200-4DF1-9E0E-D8032D4BF12C | NULL | NULL | NULL | NULL | 2026-02-21T01:44:40.1270000 | 2026-07-17T17:19:42.1800000 | False | False | NULL |
| E9874051-2327-4E27-94A9-E4335D8AF72D | NULL | NULL | NULL | NULL | 2026-02-22T01:29:20.4070000 | 2026-07-17T17:19:40.7970000 | False | False | NULL |
| 9A278D59-B0B3-4F3A-91CB-99BA94184E90 | NULL | NULL | NULL | NULL | 2026-02-19T01:08:38.4670000 | 2026-07-17T17:19:28.6570000 | False | False | NULL |
| EF040EEF-BA56-4F8D-A250-74EEF8ACEE7E | NULL | NULL | NULL | NULL | 2026-02-24T01:41:45.8170000 | 2026-07-17T17:19:27.7500000 | False | False | NULL |
| E2186AE0-464F-444F-A86F-37C8FDF2FADC | NULL | NULL | NULL | NULL | 2026-02-23T01:40:19.8730000 | 2026-07-17T17:19:27.4830000 | False | False | NULL |
| 4392478D-F9EE-4910-B178-4631DA540CC2 | NULL | NULL | NULL | NULL | 2026-02-18T01:55:23.6330000 | 2026-07-17T17:19:27.0700000 | False | False | NULL |
| 997365E2-6DA3-4A15-9D04-649E6DB6BF0A | NULL | NULL | NULL | NULL | 2026-02-17T01:11:12.2300000 | 2026-07-17T17:19:03.6430000 | False | False | NULL |

---
