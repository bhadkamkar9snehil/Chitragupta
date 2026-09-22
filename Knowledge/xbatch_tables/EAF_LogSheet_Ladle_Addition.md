# XStudio_Xbatch.dbo.EAF_LogSheet_Ladle_Addition

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** billet, furnace, heat, production, tracking (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference cpc, aiingots, hcfe, heat, lime, quality, spar, stamp, tag, time.

**Primary Key:** ID  
**Row Count:** 2  
**Date Range (ModifiedOn):** 2025-08-02T10:28:10.0000000 to 2025-08-19T10:03:51.5570000  

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
| SiMn | decimal | YES | 18,4 | — |
| HCFeMn | decimal | YES | 18,4 | — |
| FeSi | decimal | YES | 18,4 | — |
| AIingots | decimal | YES | 18,4 | — |
| CPC | decimal | YES | 18,4 | — |
| CPC_Tag | varchar | YES | 100 | — |
| CPC_TimeStamp | datetime | YES | — | — |
| CPC_Quality | int | YES | 10,0 | — |
| Lime | decimal | YES | 18,4 | — |
| Spar | decimal | YES | 18,4 | — |
| HeatID | varchar | YES | 100 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B6B3D06C-BDE3-4312-9896-C082A883285C | NULL | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-21T18:12:32.3570000 | 2025-08-02T10:28:10.0000000 | False | False | NULL |
| 36F3B69F-95C7-49B9-8ACE-559F2B24B4F7 | NULL | NULL | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 15865600-2B9C-4FB6-8497-AD5DC62E2327 | 2025-08-19T10:02:49.6270000 | 2025-08-19T10:03:51.5570000 | True | False | NULL |

---
