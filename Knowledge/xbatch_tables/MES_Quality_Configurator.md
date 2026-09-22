# XStudio_Xbatch.dbo.MES_Quality_Configurator

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** chemistry, quality, spectro (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference description, operation, sample, type.

**Primary Key:** ID  
**Row Count:** 4  
**Date Range (ModifiedOn):** 2025-12-25T08:18:38.0000000 to 2025-12-25T08:19:04.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Operation | varchar | YES | 100 | — |
| SampleType | varchar | YES | 20 | — |
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
| Description | varchar | YES | 100 | — |

### Top 10 Records

| ID | Operation | SampleType | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 737B368B-0382-4D03-A15A-CFF30253A970 | 0020 | T | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-12-25T08:16:46.9400000 | 2025-12-25T08:18:38.0000000 | False | False | NULL |
| 0D5451D5-522C-46C4-B075-39DCCC6D4A96 | 0020 | L | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-12-25T08:16:58.9430000 | 2025-12-25T08:18:46.0000000 | False | False | NULL |
| 9311C256-1578-461F-96D1-8D117871A7A4 | 0020 | F | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-12-25T08:17:06.5930000 | 2025-12-25T08:18:53.0000000 | False | False | NULL |
| DB927B90-1B04-4633-9E12-FBA81A202AEF | 0030 | P | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-12-25T08:17:21.8500000 | 2025-12-25T08:19:04.0000000 | False | False | NULL |

---
