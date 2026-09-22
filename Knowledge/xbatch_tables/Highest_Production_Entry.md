# XStudio_Xbatch.dbo.Highest_Production_Entry

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference calc, production, date, life, availability, day, longest, sequence, highest, ladle, rejections, shell.

**Primary Key:** ID  
**Row Count:** 7  
**Date Range (ModifiedOn):** 2025-09-17T09:35:02.0000000 to 2026-03-11T15:12:15.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| HighestProduction | decimal | YES | 18,4 | — |
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
| Availability | decimal | YES | 18,4 | — |
| DayProduction | decimal | YES | 18,4 | — |
| Rejections | decimal | YES | 18,4 | — |
| LongestSequence | decimal | YES | 18,4 | — |
| LadleLife | decimal | YES | 18,4 | — |
| ShellLife | decimal | YES | 18,4 | — |
| HIghestproductionCalc | varchar | YES | 100 | — |
| AvailabilityCalc | varchar | YES | 100 | — |
| DayProductionCalc | varchar | YES | 100 | — |
| RejectionsCalc | varchar | YES | 100 | — |
| LongestSequenceCalc | varchar | YES | 100 | — |
| LadleLifeCalc | varchar | YES | 100 | — |
| ShellLifeCalc | varchar | YES | 100 | — |
| Status | varchar | YES | 100 | — |
| HighestProductionDate | date | YES | — | — |
| DayProductionDate | date | YES | — | — |
| LongestSequenceDate | date | YES | — | — |
| AvailabilityDate | date | YES | — | — |
| BestAspect | varchar | YES | -1 | — |

### Top 10 Records

| ID | HighestProduction | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4A0A1294-5DBB-41FF-A77B-7340BA6B9BCD | 60008.0000 | NULL | NULL | 2026-01-05T10:33:36.3930000 | NULL | False | False | NULL | NULL |
| CEDFD735-C6CB-4EFC-9A0C-B7420ED3C48E | 61111.0000 | NULL | NULL | 2026-03-18T09:10:02.8200000 | NULL | False | False | NULL | NULL |
| B5928495-E30D-48A4-999D-3E27F9D98712 | 61111.0000 | NULL | NULL | 2026-02-25T06:00:09.0200000 | NULL | False | False | NULL | NULL |
| 85CBFA58-A8EC-4993-A21A-8B3769219A99 | 60008.0000 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-09-17T09:34:46.6830000 | 2025-09-17T09:35:02.0000000 | False | False | NULL |  |
| 0E7B8D76-1917-4AA2-BDA0-293DEA4928E5 | 60008.0000 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-09-17T09:34:46.6830000 | 2025-09-17T09:35:02.0000000 | False | False | NULL |  |
| FA83BFC2-08A3-44A7-A7F3-16AB3E380081 | 61111.0000 | NULL | 1CCC2FD3-7917-41ED-B570-39440703F6CC | 2026-01-06T08:35:51.1830000 | 2026-02-24T16:36:29.0000000 | False | False | NULL |  |
| 224484B5-8755-4C8E-ABAF-C413BDE2C3FE | 61111.0000 | NULL | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 2026-03-09T14:29:25.0800000 | 2026-03-11T15:12:15.0000000 | False | False | NULL |  |

---
