# XStudio_Xbatch.dbo.Electricity_Meter_Bill_Amount

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** electricity (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference charge, month, calculated, current, vat, actual, amount, bill, energy, system, total, year.

**Primary Key:** ID  
**Row Count:** 16  
**Date Range (ModifiedOn):** 2026-09-02T07:10:19.6100000 to 2026-09-02T07:10:19.6100000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| MonthYear | varchar | YES | 100 | — |
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
| TotalEnergyCharge | decimal | YES | 18,4 | — |
| TransmissionSystemCharge | decimal | YES | 18,4 | — |
| ActualBillAmount | decimal | YES | 18,4 | — |
| Month | varchar | YES | 100 | — |
| Year | int | YES | 10,0 | — |
| CalculatedBillAmount | decimal | YES | 18,4 | — |
| TotalEngeryConsumptionCalculate | decimal | YES | 18,4 | — |
| FeederName | varchar | YES | 500 | — |
| Difference | decimal | YES | 18,4 | — |
| ActualEnergyCharge | decimal | YES | 18,4 | — |
| MonthNumber | int | YES | 10,0 | — |
| DistributionSystemCharge | decimal | YES | 18,4 | — |
| SupplyServiceCharge | decimal | YES | 18,4 | — |
| CurrentMonthCharge | decimal | YES | 18,4 | — |
| AccountNo | varchar | YES | 100 | — |
| VAT | decimal | YES | 18,4 | — |
| SSRT | decimal | YES | 18,4 | — |
| ToURT | decimal | YES | 18,4 | — |
| CGRT | decimal | YES | 18,4 | — |
| CPRT | decimal | YES | 18,4 | — |
| NCPRT | decimal | YES | 18,4 | — |
| CurrentMonthVAT | decimal | YES | 18,4 | — |
| CalculatedCurrentMonthCharge | decimal | YES | 18,4 | — |
| CalculatedVAT | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | MonthYear | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EF620140-A5A4-48EF-801C-4FD1785AE3D4 | Sep-2026 | NULL | NULL | NULL | 2026-09-02T07:10:19.6430000 | NULL | False | False | NULL |
| FC66A156-3B66-43C4-9C1B-D88D8FF59179 | Sep-2026 | NULL | NULL | NULL | 2026-09-02T07:10:19.6430000 | NULL | False | False | NULL |
| C0F82A0F-2ECF-4BEC-994E-E8E0D7959611 | Jul-2026 | NULL | NULL | NULL | 2026-07-03T10:39:46.7170000 | 2026-09-02T07:10:19.6100000 | False | False | NULL |
| ACD8A787-AECF-4F2F-B69E-7DD5AF6E304D | Mar-2026 | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2026-03-02T00:36:49.9200000 | 2026-09-02T07:10:19.6100000 | False | False | NULL |
| 8B7B8100-5BB3-4E21-911A-211CB286AD49 | Aug-2026 | NULL | NULL | NULL | 2026-08-03T09:12:22.6430000 | 2026-09-02T07:10:19.6100000 | False | False | NULL |
| 89C802DC-1C48-4E62-A9F7-C9BB79B4FD2E | Aug-2026 | NULL | NULL | NULL | 2026-08-03T09:12:22.6430000 | 2026-09-02T07:10:19.6100000 | False | False | NULL |
| 4854E4C5-16AD-4B65-A0CB-FF3F527E2B9E | Feb-2026 | NULL | NULL | NULL | 2026-02-16T14:22:06.3600000 | 2026-09-02T07:10:19.6100000 | False | False | NULL |
| 426DAF3A-400A-4F96-AA92-D024A3EB1EC6 | Apr-2026 | NULL | NULL | NULL | 2026-04-02T00:56:11.1370000 | 2026-09-02T07:10:19.6100000 | False | False | NULL |
| 3ED154A4-430D-4D00-9DBA-A4755C1E8A1E | May-2026 | NULL | NULL | NULL | 2026-05-02T01:00:14.6400000 | 2026-09-02T07:10:19.6100000 | False | False | NULL |
| 381BA5D1-BE65-48FA-8599-B814624FA6DA | Jun-2026 | NULL | NULL | NULL | 2026-06-02T00:32:48.6530000 | 2026-09-02T07:10:19.6100000 | False | False | NULL |

### Bottom 10 Records

| ID | MonthYear | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C0F82A0F-2ECF-4BEC-994E-E8E0D7959611 | Jul-2026 | NULL | NULL | NULL | 2026-07-03T10:39:46.7170000 | 2026-09-02T07:10:19.6100000 | False | False | NULL |
| ACD8A787-AECF-4F2F-B69E-7DD5AF6E304D | Mar-2026 | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2026-03-02T00:36:49.9200000 | 2026-09-02T07:10:19.6100000 | False | False | NULL |
| 8B7B8100-5BB3-4E21-911A-211CB286AD49 | Aug-2026 | NULL | NULL | NULL | 2026-08-03T09:12:22.6430000 | 2026-09-02T07:10:19.6100000 | False | False | NULL |
| 89C802DC-1C48-4E62-A9F7-C9BB79B4FD2E | Aug-2026 | NULL | NULL | NULL | 2026-08-03T09:12:22.6430000 | 2026-09-02T07:10:19.6100000 | False | False | NULL |
| 4854E4C5-16AD-4B65-A0CB-FF3F527E2B9E | Feb-2026 | NULL | NULL | NULL | 2026-02-16T14:22:06.3600000 | 2026-09-02T07:10:19.6100000 | False | False | NULL |
| 426DAF3A-400A-4F96-AA92-D024A3EB1EC6 | Apr-2026 | NULL | NULL | NULL | 2026-04-02T00:56:11.1370000 | 2026-09-02T07:10:19.6100000 | False | False | NULL |
| 3ED154A4-430D-4D00-9DBA-A4755C1E8A1E | May-2026 | NULL | NULL | NULL | 2026-05-02T01:00:14.6400000 | 2026-09-02T07:10:19.6100000 | False | False | NULL |
| 381BA5D1-BE65-48FA-8599-B814624FA6DA | Jun-2026 | NULL | NULL | NULL | 2026-06-02T00:32:48.6530000 | 2026-09-02T07:10:19.6100000 | False | False | NULL |
| 11A37D7E-F940-4568-B536-730FDF4774C9 | Jul-2026 | NULL | NULL | NULL | 2026-07-03T10:39:46.7170000 | 2026-09-02T07:10:19.6100000 | False | False | NULL |
| 0769959B-3B17-44CD-BCC5-C34B13F03AB6 | Feb-2026 | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-02-16T14:22:06.3600000 | 2026-09-02T07:10:19.6100000 | False | False | NULL |

---
