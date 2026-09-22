# XStudio_Xbatch.dbo.BilletsPosition_InFurnace

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** catalog, entities, entity, from, highlights, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference position, grade, heat.

**Primary Key:** ID  
**Row Count:** 1  
**Date Range (ModifiedOn):** 2026-07-27T16:34:38.0000000 to 2026-07-27T16:34:38.0000000  

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
| Position1 | varchar | YES | 100 | — |
| Position2 | varchar | YES | 100 | — |
| Position3 | varchar | YES | 100 | — |
| Position4 | varchar | YES | 100 | — |
| Position5 | varchar | YES | 100 | — |
| Position6 | varchar | YES | 100 | — |
| Position7 | varchar | YES | 100 | — |
| Position8 | varchar | YES | 100 | — |
| Position9 | varchar | YES | 100 | — |
| Position10 | varchar | YES | 100 | — |
| Position11 | varchar | YES | 100 | — |
| Position12 | varchar | YES | 100 | — |
| Position13 | varchar | YES | 100 | — |
| Position14 | varchar | YES | 100 | — |
| Position15 | varchar | YES | 100 | — |
| Position16 | varchar | YES | 100 | — |
| Position17 | varchar | YES | 100 | — |
| Position18 | varchar | YES | 100 | — |
| Position19 | varchar | YES | 100 | — |
| Position20 | varchar | YES | 100 | — |
| Position21 | varchar | YES | 100 | — |
| Position22 | varchar | YES | 100 | — |
| Position23 | varchar | YES | 100 | — |
| Position24 | varchar | YES | 100 | — |
| Position26 | varchar | YES | 100 | — |
| Position25 | varchar | YES | 100 | — |
| Position27 | varchar | YES | 100 | — |
| Position28 | varchar | YES | 100 | — |
| Position29 | varchar | YES | 100 | — |
| Position30 | varchar | YES | 100 | — |
| Position31 | varchar | YES | 100 | — |
| Position32 | varchar | YES | 100 | — |
| Position34 | varchar | YES | 100 | — |
| Position35 | varchar | YES | 100 | — |
| Position36 | varchar | YES | 100 | — |
| Position37 | varchar | YES | 100 | — |
| Position38 | varchar | YES | 100 | — |
| Position39 | varchar | YES | 100 | — |
| Position40 | varchar | YES | 100 | — |
| Position42 | varchar | YES | 100 | — |
| Position33 | varchar | YES | 100 | — |
| Position41 | varchar | YES | 100 | — |
| Position43 | varchar | YES | 100 | — |
| Position44 | varchar | YES | 100 | — |
| Position45 | varchar | YES | 100 | — |
| Position46 | varchar | YES | 100 | — |
| Position47 | varchar | YES | 100 | — |
| Position48 | varchar | YES | 100 | — |
| Position49 | varchar | YES | 100 | — |
| Position50 | varchar | YES | 100 | — |
| Position51 | varchar | YES | 100 | — |
| Position52 | varchar | YES | 100 | — |
| Position53 | varchar | YES | 100 | — |
| Position54 | varchar | YES | 100 | — |
| Position55 | varchar | YES | 100 | — |
| Position56 | varchar | YES | 100 | — |
| Position57 | varchar | YES | 100 | — |
| Position58 | varchar | YES | 100 | — |
| Position59 | varchar | YES | 100 | — |
| Position60 | varchar | YES | 100 | — |
| Position61 | varchar | YES | 100 | — |
| Position63 | varchar | YES | 100 | — |
| Position62 | varchar | YES | 100 | — |
| Position64 | varchar | YES | 100 | — |
| Position65 | varchar | YES | 100 | — |
| Position66 | varchar | YES | 100 | — |
| Position67 | varchar | YES | 100 | — |
| Position68 | varchar | YES | 100 | — |
| Position69 | varchar | YES | 100 | — |
| Position70 | varchar | YES | 100 | — |
| Position1Grade | varchar | YES | 100 | — |
| Position1HeatNo | varchar | YES | 100 | — |
| Position2Grade | varchar | YES | 100 | — |
| Position2HeatNo | varchar | YES | 100 | — |
| Position3Grade | varchar | YES | 100 | — |
| Position4Grade | varchar | YES | 100 | — |
| Position5Grade | varchar | YES | 100 | — |
| Position6Grade | varchar | YES | 100 | — |
| Position7Grade | varchar | YES | 100 | — |
| Position8Grade | varchar | YES | 100 | — |
| Position9Grade | varchar | YES | 100 | — |
| Position10Grade | varchar | YES | 100 | — |
| Position11Grade | varchar | YES | 100 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FCEFA80C-2EDA-4937-B2D0-4EB5901E7640 | NULL | NULL | 19F651E7-FC5E-4A24-8D95-48F5FE661683 | 19F651E7-FC5E-4A24-8D95-48F5FE661683 | 2026-06-15T14:06:21.1530000 | 2026-07-27T16:34:38.0000000 | False | False | NULL |

---
