# XStudio_Xbatch.dbo.Billet_AvailableHeat

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference grade, heat, qty, stack, status.

**Primary Key:** ID  
**Row Count:** 10  
**Date Range (ModifiedOn):** 2025-06-26T14:29:38.0000000 to 2025-06-26T17:34:18.0000000  

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
| HeatNo | int | YES | 10,0 | — |
| Qty | int | YES | 10,0 | — |
| Status | varchar | YES | 100 | — |
| Stack | varchar | YES | 100 | — |
| Grade | varchar | YES | 100 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F08F47AE-B138-4C2C-B3E8-164E1FE47B7A | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-06-26T12:36:37.9100000 | 2025-06-26T14:29:38.0000000 | False | False | NULL |
| D69F8498-2BDA-4AB3-8C74-82C2F97B9CF0 | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-06-26T12:36:37.9100000 | 2025-06-26T14:29:43.0000000 | False | False | NULL |
| 9A9E5F98-54D8-4BD8-BFDD-3A5AF9D03683 | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-06-26T12:36:37.9100000 | 2025-06-26T14:29:48.0000000 | False | False | NULL |
| 3E35D0D8-E9B0-4020-8569-BFE6ED5BD2C7 | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-06-26T12:36:37.9100000 | 2025-06-26T14:29:52.0000000 | False | False | NULL |
| 29FA5074-CB0E-43F8-A1AA-5E4D1FB691B8 | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-06-26T12:36:37.9100000 | 2025-06-26T14:29:57.0000000 | False | False | NULL |
| 754A8169-28F9-449F-A5EB-ADC74375B94E | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-06-26T12:36:37.9100000 | 2025-06-26T14:30:02.0000000 | False | False | NULL |
| 970795D5-97ED-4B77-A402-74014220BDA3 | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-06-26T12:36:37.9100000 | 2025-06-26T14:30:06.0000000 | False | False | NULL |
| 3F501342-3970-4B83-A862-826EFA3816A1 | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-06-26T12:36:37.9100000 | 2025-06-26T14:30:11.0000000 | False | False | NULL |
| C9145408-28A2-4B2B-9D2A-23B3B4F05F20 | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-06-26T15:46:14.6170000 | 2025-06-26T15:46:14.0000000 | False | False | NULL |
| 71AFC1A7-266E-4950-838D-93A07B055927 | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-06-26T17:34:18.8100000 | 2025-06-26T17:34:18.0000000 | False | False | NULL |

---
