# XStudio_Xbatch.dbo.RM_Furnace_Combustion_Attribute_Tag_Template_Dtl_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference color, document, type, equation, extend, transaction, bwhhh, bwhl, bwlll, gthh, ltll, retrieval.

**Primary Key:** ID  
**Row Count:** 62  

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
| Attribute | varchar | YES | 100 | — |
| HHRange | decimal | YES | 18,4 | — |
| HRange | decimal | YES | 18,4 | — |
| LRange | decimal | YES | 18,4 | — |
| LLRange | decimal | YES | 18,4 | — |
| ColorGTHH | varchar | YES | 100 | — |
| ColorBWHHH | varchar | YES | 100 | — |
| ColorBWHL | varchar | YES | 100 | — |
| ColorBWLLL | varchar | YES | 100 | — |
| ColorLTLL | varchar | YES | 100 | — |
| DocumentGTHH | varchar | YES | 8000 | — |
| DocumentBWHHH | varchar | YES | 8000 | — |
| DocumentBWHL | varchar | YES | 8000 | — |
| DocumentBWLLL | varchar | YES | 8000 | — |
| DocumentLTLL | varchar | YES | 8000 | — |
| ExtendRetrievalType | varchar | YES | 36 | — |
| ExtendEquationType | varchar | YES | 36 | — |
| ExtendEquation | varchar | YES | -1 | — |
| TransactionRetrievalType | varchar | YES | 36 | — |
| Procedure | varchar | YES | 36 | — |
| PWherecolumn | varchar | YES | 36 | — |
| POperator | varchar | YES | 36 | — |
| PConditionType | varchar | YES | 36 | — |
| PMSTAttribute | varchar | YES | 36 | — |
| PWhereValue | varchar | YES | 100 | — |
| IType | varchar | YES | 36 | — |
| TransactionEquationType | varchar | YES | 36 | — |
| TransactionEquation | varchar | YES | -1 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2ECCF20A-FF27-4FB8-B023-EA6C648F8742 | NULL | 76346B2C-25CB-421C-B92B-A1551E33B4A3 | NULL | NULL | 2026-08-14T13:22:00.1270000 | NULL | False | False | NULL |
| 2DBB2CA2-EAA4-4FD5-8D13-D48942B3779B | NULL | 76346B2C-25CB-421C-B92B-A1551E33B4A3 | NULL | NULL | 2026-08-14T13:12:19.4430000 | NULL | False | False | NULL |
| 2AC53106-7804-4051-AD36-44992B2951AF | NULL | 76346B2C-25CB-421C-B92B-A1551E33B4A3 | NULL | NULL | 2026-08-14T13:23:17.3430000 | NULL | False | False | NULL |
| 2220BE58-1F75-46FB-BAE1-4F4F504BA809 | NULL | 76346B2C-25CB-421C-B92B-A1551E33B4A3 | NULL | NULL | 2026-08-14T13:30:40.7600000 | NULL | False | False | NULL |
| 1E7250A0-47DE-47C5-8322-4B37412A4F89 | NULL | 76346B2C-25CB-421C-B92B-A1551E33B4A3 | NULL | NULL | 2026-08-14T13:20:58.0600000 | NULL | False | False | NULL |
| 1B1B0877-8874-48F9-9540-7AFBD6B1507C | NULL | 76346B2C-25CB-421C-B92B-A1551E33B4A3 | NULL | NULL | 2026-08-14T13:28:18.7000000 | NULL | False | False | NULL |
| 182B5783-BA3A-4318-9ABE-FAFABB208398 | NULL | 76346B2C-25CB-421C-B92B-A1551E33B4A3 | NULL | NULL | 2026-08-14T13:36:42.3800000 | NULL | False | False | NULL |
| 181CF1A5-A6A7-42AB-9116-C7151FE3EB9B | NULL | 76346B2C-25CB-421C-B92B-A1551E33B4A3 | NULL | NULL | 2026-08-14T13:30:17.9730000 | NULL | False | False | NULL |
| 07E826A0-07D2-41B1-9F8F-136A6E3CD92F | NULL | 76346B2C-25CB-421C-B92B-A1551E33B4A3 | NULL | NULL | 2026-08-14T13:21:41.4370000 | NULL | False | False | NULL |
| 04410E4F-76AB-4D40-A86B-F6E1D0B9A717 | NULL | 76346B2C-25CB-421C-B92B-A1551E33B4A3 | NULL | NULL | 2026-08-14T12:55:29.3970000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2ECCF20A-FF27-4FB8-B023-EA6C648F8742 | NULL | 76346B2C-25CB-421C-B92B-A1551E33B4A3 | NULL | NULL | 2026-08-14T13:22:00.1270000 | NULL | False | False | NULL |
| 2DBB2CA2-EAA4-4FD5-8D13-D48942B3779B | NULL | 76346B2C-25CB-421C-B92B-A1551E33B4A3 | NULL | NULL | 2026-08-14T13:12:19.4430000 | NULL | False | False | NULL |
| 2AC53106-7804-4051-AD36-44992B2951AF | NULL | 76346B2C-25CB-421C-B92B-A1551E33B4A3 | NULL | NULL | 2026-08-14T13:23:17.3430000 | NULL | False | False | NULL |
| 2220BE58-1F75-46FB-BAE1-4F4F504BA809 | NULL | 76346B2C-25CB-421C-B92B-A1551E33B4A3 | NULL | NULL | 2026-08-14T13:30:40.7600000 | NULL | False | False | NULL |
| 1E7250A0-47DE-47C5-8322-4B37412A4F89 | NULL | 76346B2C-25CB-421C-B92B-A1551E33B4A3 | NULL | NULL | 2026-08-14T13:20:58.0600000 | NULL | False | False | NULL |
| 1B1B0877-8874-48F9-9540-7AFBD6B1507C | NULL | 76346B2C-25CB-421C-B92B-A1551E33B4A3 | NULL | NULL | 2026-08-14T13:28:18.7000000 | NULL | False | False | NULL |
| 182B5783-BA3A-4318-9ABE-FAFABB208398 | NULL | 76346B2C-25CB-421C-B92B-A1551E33B4A3 | NULL | NULL | 2026-08-14T13:36:42.3800000 | NULL | False | False | NULL |
| 181CF1A5-A6A7-42AB-9116-C7151FE3EB9B | NULL | 76346B2C-25CB-421C-B92B-A1551E33B4A3 | NULL | NULL | 2026-08-14T13:30:17.9730000 | NULL | False | False | NULL |
| 07E826A0-07D2-41B1-9F8F-136A6E3CD92F | NULL | 76346B2C-25CB-421C-B92B-A1551E33B4A3 | NULL | NULL | 2026-08-14T13:21:41.4370000 | NULL | False | False | NULL |
| 04410E4F-76AB-4D40-A86B-F6E1D0B9A717 | NULL | 76346B2C-25CB-421C-B92B-A1551E33B4A3 | NULL | NULL | 2026-08-14T12:55:29.3970000 | NULL | False | False | NULL |

---
