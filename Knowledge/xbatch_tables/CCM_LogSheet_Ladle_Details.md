# XStudio_Xbatch.dbo.CCM_LogSheet_Ladle_Details

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** billet, furnace, heat, production, tracking (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference ladle, life, teeming, weightm, arm, empty, grade, gross, heat, lifting, lrflmweightm, nuzzal.

**Primary Key:** ID  
**Row Count:** 3  
**Date Range (ModifiedOn):** 2025-07-21T17:16:53.0000000 to 2025-11-24T14:28:17.0000000  

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
| LadleNo | int | YES | 10,0 | — |
| LadleLife | int | YES | 10,0 | — |
| LadleLiftingTempC | int | YES | 10,0 | — |
| LRFLMWeightmT | int | YES | 10,0 | — |
| LadlePalcedonArmNo | varchar | YES | 100 | — |
| LadleGrossWeightmT | decimal | YES | 18,4 | — |
| EmptyLadleWeightmT | decimal | YES | 18,4 | — |
| LadleShrouldLife | int | YES | 10,0 | — |
| LadleNuzzalOpening | varchar | YES | 100 | — |
| TeemingStart | datetime | YES | — | — |
| TeemingStop | datetime | YES | — | — |
| TotalTimemin | varchar | YES | 100 | — |
| HeatNo | varchar | YES | 100 | — |
| Grade | varchar | YES | 100 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FD4FD665-7453-4655-AB92-B9E8A05B4531 | NULL | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-21T16:52:17.5500000 | 2025-07-21T17:16:53.0000000 | False | False | NULL |
| 0627CB69-41C8-4CB0-AA3F-02D1056FB4DB | NULL | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-22T15:46:30.3800000 | 2025-08-02T10:28:32.0000000 | False | False | NULL |
| 24BBB9EB-6784-4493-9D54-6D7C7460D804 | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-11-24T14:28:17.3100000 | 2025-11-24T14:28:17.0000000 | False | False | NULL |

---
