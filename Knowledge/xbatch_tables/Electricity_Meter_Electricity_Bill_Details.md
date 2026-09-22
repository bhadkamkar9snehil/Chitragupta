# XStudio_Xbatch.dbo.Electricity_Meter_Electricity_Bill_Details

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference consumption, month, charge, feeder, kwh, name, number, rate, time, use, year.

**Primary Key:** ID  
**Row Count:** 1,236  
**Date Range (ModifiedOn):** 2026-05-27T15:47:42.0600000 to 2026-07-16T10:43:24.5070000  

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
| Month | varchar | YES | 100 | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| Charge | decimal | YES | 18,4 | — |
| Rate | decimal | YES | 18,4 | — |
| Consumption | decimal | YES | 18,4 | — |
| TimeOfUse | varchar | YES | 100 | — |
| Year | int | YES | 10,0 | — |
| MonthNumber | int | YES | 10,0 | — |
| FeederName | varchar | YES | 500 | — |
| ConsumptionKWh | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 021534CA-62EA-492A-9744-7E21B5798C0F | NULL | NULL | NULL | NULL | 2026-05-27T16:00:31.8830000 | NULL | False | False | NULL |
| 017CF9C2-2B62-4784-82A7-472570ED1CF3 | NULL | NULL | NULL | NULL | 2026-08-31T17:29:31.9130000 | NULL | False | False | NULL |
| 0179D4E1-6B1A-4BF5-A502-82CE2197CF99 | NULL | NULL | NULL | NULL | 2026-07-09T01:20:34.9100000 | NULL | False | False | NULL |
| 01658332-6D63-4ECC-B00B-DECF5F18355D | NULL | NULL | NULL | NULL | 2026-05-27T16:00:31.5970000 | NULL | False | False | NULL |
| 0139857A-CE7B-43D3-8D77-4BD3C28BD786 | NULL | NULL | NULL | NULL | 2026-05-27T16:00:31.4470000 | NULL | False | False | NULL |
| 01059F27-2053-41AA-8562-5B0DFE673F83 | NULL | NULL | NULL | NULL | 2026-07-03T10:40:38.5730000 | NULL | False | False | NULL |
| 0103DE99-5657-4189-8C55-EC2328F2AB92 | NULL | NULL | NULL | NULL | 2026-08-22T07:38:50.8070000 | NULL | False | False | NULL |
| 00A01CB6-5CC7-44EB-A6A2-5CA5DED7C992 | NULL | NULL | NULL | NULL | 2026-05-27T16:00:31.9870000 | NULL | False | False | NULL |
| 00782658-9FB7-460C-803A-060D9154BA38 | NULL | NULL | NULL | NULL | 2026-05-28T02:21:10.0670000 | NULL | False | False | NULL |
| 00650FB5-DBAC-41D5-94B7-FA8FB71A47ED | NULL | NULL | NULL | NULL | 2026-07-13T00:47:20.3530000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 23FE6238-ACE5-467F-9D13-A8BCFD219F6C | NULL | NULL | NULL | NULL | 2026-07-14T00:33:58.5770000 | 2026-07-16T10:43:24.5070000 | False | False | NULL |
| 39C8BF48-7CC2-44A2-AC13-96C878E97735 | NULL | NULL | NULL | NULL | 2026-07-14T00:33:58.5770000 | 2026-07-16T10:43:24.5070000 | False | False | NULL |
| 75F5E75D-1D0D-40B8-A337-B89D383F53C7 | NULL | NULL | NULL | NULL | 2026-07-14T00:33:58.5770000 | 2026-07-16T10:43:24.5070000 | False | False | NULL |
| 2980A413-CA0D-41C4-A7AF-D738CF1C9CD6 | NULL | NULL | NULL | NULL | 2026-05-27T16:00:31.5330000 | 2026-05-28T15:21:14.8670000 | False | False | NULL |
| 77C409B5-33EC-4221-AA1B-D157F6349352 | NULL | NULL | NULL | NULL | 2026-05-27T16:00:31.5330000 | 2026-05-28T15:21:14.8670000 | False | False | NULL |
| 86FF11CD-0E5A-4EF3-A805-D7074033B6D7 | NULL | NULL | NULL | NULL | 2026-05-27T16:00:31.5330000 | 2026-05-28T15:21:14.8670000 | False | False | NULL |
| 8A9DA314-567B-47C6-9E3B-706305D2DDD8 | NULL | NULL | NULL | NULL | 2026-05-27T16:00:31.5330000 | 2026-05-28T15:21:14.8670000 | False | False | NULL |
| 8C44057A-E323-4EB6-A10E-016AC71F4301 | NULL | NULL | NULL | NULL | 2026-05-27T16:00:31.5330000 | 2026-05-28T15:21:14.8670000 | False | False | NULL |
| C9BEE661-AE6A-480B-8E8E-F1A7BC63309F | NULL | NULL | NULL | NULL | 2026-05-27T16:00:31.5330000 | 2026-05-28T15:21:14.8670000 | False | False | NULL |
| 06E8B2EB-A8CF-4BAC-814F-907B9437F4BA | NULL | NULL | NULL | NULL | 2026-05-27T16:00:31.9300000 | 2026-05-28T15:21:04.8030000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Electricity_Meter_Electricity_Bill_Details.TimeOfUse` -> `XStudio_XBatch.Rate_Band_Master.Name` (Many to One)
