# XStudio_Xbatch.dbo.Billet_RollingPlan

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference qty, assigned, code, customer, date, desc, grade, material, name, ponumber, product, roll.

**Primary Key:** ID  
**Row Count:** 5  
**Date Range (ModifiedOn):** 2025-06-26T15:32:03.0000000 to 2025-06-26T17:32:45.0000000  

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
| PONumber | varchar | YES | 100 | — |
| CustomerName | varchar | YES | 100 | — |
| ProductCode | varchar | YES | 100 | — |
| MaterialDesc | varchar | YES | 100 | — |
| Size | decimal | YES | 18,4 | — |
| Grade | varchar | YES | 100 | — |
| RollingQty | int | YES | 10,0 | — |
| AssignedQty | int | YES | 10,0 | — |
| Sequence | int | YES | 10,0 | — |
| Date | date | YES | — | — |
| RollId | varchar | YES | 100 | — |
| Status | varchar | YES | 100 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2156D191-EBBC-4F43-B490-ED431AF03C42 | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | NULL | 2025-06-26T12:21:07.3270000 | NULL | False | False | NULL |
| D5EAD5E3-2FCF-41FB-8A88-21BEFFCA7A94 | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | NULL | 2025-06-26T12:21:07.3270000 | NULL | False | False | NULL |
| 94F5BB11-5715-4A85-AEF3-84C842F00ADF | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-06-26T15:32:03.0770000 | 2025-06-26T15:32:03.0000000 | False | False | NULL |
| D350CB43-7E45-4420-806B-B4CC250DE3B4 | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-06-26T12:21:07.3270000 | 2025-06-26T15:33:14.0000000 | False | False | NULL |
| 2C8D7445-F99F-4FBE-91DF-F00B95F5A674 | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-06-26T17:32:45.6430000 | 2025-06-26T17:32:45.0000000 | False | False | NULL |

---
