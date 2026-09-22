# XStudio_Xbatch.dbo.Tagname_Details

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference name, tag, new, old.

**Primary Key:** ID  
**Row Count:** 5  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | int | NO | 10,0 | — |
| OldTagName | varchar | NO | -1 | — |
| NewTagName | varchar | NO | -1 | — |

### Top 10 Records

| ID | OldTagName | NewTagName |
| --- | --- | --- |
| 1 | LRF_PREV_POWER_OFF_TIME_SEC_PRM | LRF_PREV_POWER_OFF_TIME_MIN_PRM |
| 2 | LRF_PREV_POWER_ON_TIME_SEC_PRM | LRF_PREV_POWER_ON_TIME_MIN_PRM |
| 3 | LRF_ACTUAL_POWER_OFF_TIME_SEC_PRM | LRF_ACTUAL_POWER_OFF_TIME_MIN_PRM |
| 4 | LRF_ACTUAL_POWER_ON_TIME_SEC_PRM | LRF_ACTUAL_POWER_ON_TIME_MIN_PRM |
| 5 | CCM_TUNDISH_WEIGHT_KG_PRM | CCM_TUNDISH_WEIGHT_TON_PRM |

---
