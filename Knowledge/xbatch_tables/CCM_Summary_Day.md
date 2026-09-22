# XStudio_Xbatch.dbo.CCM_Summary_Day

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** catalog, entities, entity, from, highlights, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference strand, billet, counter, casting, oscspeed, speed, std, mtd, ytd, actual, count, total.

**Primary Key:** ID  
**Row Count:** 5,633  
**Date Range (ModifiedOn):** 2025-08-28T17:54:06.9430000 to 2026-08-12T08:44:32.0470000  

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
| Strand3BilletCounter | int | YES | 10,0 | — |
| Strand1BilletCounter | int | YES | 10,0 | — |
| STD2OSCSpeed | decimal | YES | 18,4 | — |
| Strand4CastingSpeed | decimal | YES | 18,4 | — |
| TotalProduction | decimal | YES | 18,4 | — |
| STD6OSCSpeed | decimal | YES | 18,4 | — |
| Strand2BilletCounter | int | YES | 10,0 | — |
| Strand5CastingSpeed | decimal | YES | 18,4 | — |
| STD1OSCSpeed | decimal | YES | 18,4 | — |
| Strand1CastingSpeed | decimal | YES | 18,4 | — |
| STD3OSCSpeed | decimal | YES | 18,4 | — |
| Strand5BilletCounter | int | YES | 10,0 | — |
| Strand6CastingSpeed | decimal | YES | 18,4 | — |
| HeatID | decimal | YES | 18,4 | — |
| Strand3CastingSpeed | decimal | YES | 18,4 | — |
| Strand6BilletCounter | int | YES | 10,0 | — |
| STD4OSCSpeed | decimal | YES | 18,4 | — |
| STD5OSCSpeed | decimal | YES | 18,4 | — |
| TotalBilletsCount | decimal | YES | 18,4 | — |
| Strand4BilletCounter | int | YES | 10,0 | — |
| Strand2CastingSpeed | decimal | YES | 18,4 | — |
| Strand6BilletCounter_MTD | int | YES | 10,0 | — |
| Strand2BilletCounter_YD | int | YES | 10,0 | — |
| Strand1BilletCounter_YTD | int | YES | 10,0 | — |
| HeatID_YTD | decimal | YES | 18,4 | — |
| Strand5BilletCounter_MTD | int | YES | 10,0 | — |
| Strand6BilletCounter_YD | int | YES | 10,0 | — |
| TotalProduction_YTD | decimal | YES | 18,4 | — |
| Strand1CastingSpeed_YD | decimal | YES | 18,4 | — |
| STD2OSCSpeed_YD | decimal | YES | 18,4 | — |
| STD6OSCSpeed_YD | decimal | YES | 18,4 | — |
| Strand4CastingSpeed_YD | decimal | YES | 18,4 | — |
| STD1OSCSpeed_YD | decimal | YES | 18,4 | — |
| Strand4BilletCounter_YTD | int | YES | 10,0 | — |
| STD4OSCSpeed_YD | decimal | YES | 18,4 | — |
| Strand5BilletCounter_YD | int | YES | 10,0 | — |
| TotalProduction_MTD | decimal | YES | 18,4 | — |
| Strand5BilletCounter_YTD | int | YES | 10,0 | — |
| TotalBilletsCount_YD | decimal | YES | 18,4 | — |
| Strand1BilletCounter_MTD | int | YES | 10,0 | — |
| STD5OSCSpeed_YD | decimal | YES | 18,4 | — |
| Strand4BilletCounter_MTD | int | YES | 10,0 | — |
| Strand4BilletCounter_YD | int | YES | 10,0 | — |
| Strand2BilletCounter_YTD | int | YES | 10,0 | — |
| Strand6BilletCounter_YTD | int | YES | 10,0 | — |
| Strand3BilletCounter_YTD | int | YES | 10,0 | — |
| Strand3CastingSpeed_YD | decimal | YES | 18,4 | — |
| HeatID_MTD | decimal | YES | 18,4 | — |
| Strand6CastingSpeed_YD | decimal | YES | 18,4 | — |
| Strand3BilletCounter_YD | int | YES | 10,0 | — |
| Strand2CastingSpeed_YD | decimal | YES | 18,4 | — |
| TotalBilletsCount_MTD | decimal | YES | 18,4 | — |
| Strand2BilletCounter_MTD | int | YES | 10,0 | — |
| Strand3BilletCounter_MTD | int | YES | 10,0 | — |
| Strand5CastingSpeed_YD | decimal | YES | 18,4 | — |
| TotalProduction_YD | decimal | YES | 18,4 | — |
| Strand1BilletCounter_YD | int | YES | 10,0 | — |
| STD3OSCSpeed_YD | decimal | YES | 18,4 | — |
| TotalBilletsCount_YTD | decimal | YES | 18,4 | — |
| HeatID_YD | decimal | YES | 18,4 | — |
| MonthlyTarget | decimal | YES | 18,4 | — |
| TodayPlannedProduction | decimal | YES | 18,4 | — |
| MTDPlannedProduction | decimal | YES | 18,4 | — |
| TodayPlannedProduction_YD | decimal | YES | 18,4 | — |
| ActualBilletCount | int | YES | 10,0 | — |
| ActualBilletWeightTon | decimal | YES | 18,4 | — |
| ActualBilletCount_YD | int | YES | 10,0 | — |
| ActualBilletWeightTon_YD | decimal | YES | 18,4 | — |
| ActualBilletCount_MTD | int | YES | 10,0 | — |
| ActualBilletWeightTon_MTD | decimal | YES | 18,4 | — |
| ActualBilletCount_YTD | int | YES | 10,0 | — |
| ActualBilletWeightTon_YTD | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 003DA5EB-A8F4-455A-B966-B52B1912B451 | NULL | NULL | NULL | NULL | 2025-12-26T08:06:10.0670000 | NULL | False | False | NULL |
| 003D3036-32F5-4136-B2B6-8B7D6D5656EA | NULL | NULL | NULL | NULL | 2026-02-09T07:28:58.0570000 | NULL | False | False | NULL |
| 0033DE73-F985-4381-BE9B-442F1E67C58B | NULL | NULL | NULL | NULL | 2026-05-15T11:53:09.4970000 | NULL | False | False | NULL |
| 0031EB8F-DBA9-4537-BD9F-4F9F4377AC51 | NULL | NULL | NULL | NULL | 2026-06-21T08:06:52.5000000 | NULL | False | False | NULL |
| 002D5E67-F734-485D-80A9-18608B4D43EE | NULL | NULL | NULL | NULL | 2026-05-22T17:35:29.2100000 | NULL | False | False | NULL |
| 002C1BC0-2001-4324-8F0D-10EFEF7BEF76 | NULL | NULL | NULL | NULL | 2026-05-30T09:54:29.9470000 | NULL | False | False | NULL |
| 002A4E56-2CA5-443B-88A3-F0D3CFFF1FC0 | NULL | NULL | NULL | NULL | 2026-05-29T21:01:08.9000000 | NULL | False | False | NULL |
| 0023CAD0-7290-490F-B825-4D0D09D08982 | NULL | NULL | NULL | NULL | 2026-05-10T21:25:26.1370000 | NULL | False | False | NULL |
| 002192BB-5FB3-4161-888B-136F10E82255 | NULL | NULL | NULL | NULL | 2026-05-23T21:40:38.8800000 | NULL | False | False | NULL |
| 001F55A6-45AE-411C-875E-AF7BE61D287D | NULL | NULL | NULL | NULL | 2026-06-25T12:52:00.7900000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D151EEA9-BA3D-468A-89E3-BFB210C90AFA | NULL | NULL | NULL | NULL | 2026-07-08T04:01:58.5600000 | 2026-08-12T08:44:32.0470000 | False | False | NULL |
| E02788AF-C33A-4807-92C6-D097D331E8AD | NULL | NULL | NULL | NULL | 2026-07-07T06:13:22.2930000 | 2026-07-19T18:16:46.6030000 | False | False | NULL |
| 545D3FF5-8A52-41C1-B2D3-68D50790C30C | NULL | NULL | NULL | NULL | 2026-07-06T06:24:27.5970000 | 2026-07-17T17:19:46.7670000 | False | False | NULL |
| 229ADA53-4416-4C58-9B25-01727BA740C5 | NULL | NULL | NULL | NULL | 2026-07-05T06:05:26.9100000 | 2026-07-17T17:19:46.7630000 | False | False | NULL |
| 07A952BA-F171-48CD-9673-D7925E893F85 | NULL | NULL | NULL | NULL | 2026-07-03T03:09:33.5130000 | 2026-07-17T17:19:46.7600000 | False | False | NULL |
| FFA60534-1A9A-4CCD-B921-C073DE6F530D | NULL | NULL | NULL | NULL | 2026-07-04T06:01:37.1270000 | 2026-07-17T17:19:46.7600000 | False | False | NULL |
| FD6C44B0-3656-416A-A406-1F20888816C7 | NULL | NULL | NULL | NULL | 2026-07-02T06:10:37.3200000 | 2026-07-17T17:19:46.7570000 | False | False | NULL |
| 3177ECB7-EF31-4F44-8A5E-27D48F557D36 | NULL | NULL | NULL | NULL | 2026-07-01T06:08:45.1500000 | 2026-07-17T17:19:46.7530000 | False | False | NULL |
| 84441900-5ED2-47D8-9A58-0E41123B00AF | NULL | NULL | NULL | NULL | 2026-06-30T05:53:20.0930000 | 2026-07-17T17:19:46.7500000 | False | False | NULL |
| 5DC89D40-87B6-433D-B389-07D4D39B8335 | NULL | NULL | NULL | NULL | 2026-06-29T06:03:47.7170000 | 2026-07-17T17:19:46.7470000 | False | False | NULL |

---
