# XStudio_Xbatch.dbo.EAF_Manual_Entry

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference weight, billet, coke, consumption, electrode, heat, liquid, nut, rejected, steel.

**Primary Key:** ID  
**Row Count:** 14  
**Date Range (ModifiedOn):** 2025-08-02T10:29:12.0000000 to 2025-08-11T14:46:00.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
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
| Name | varchar | YES | 100 | — |
| IsProcessed | bit | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| HeatNo | varchar | YES | 100 | — |
| LiquidSteelWeight | decimal | YES | 18,4 | — |
| RejectedBilletWeight | decimal | YES | 18,4 | — |
| ElectrodeConsumption | decimal | YES | 18,4 | — |
| ReportDate | date | YES | — | — |
| NutCoke | decimal | YES | 18,4 | — |
| ParentID | varchar | YES | 36 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5EFC6E96-C7B8-4E4C-913E-17BA4E973E1C | NULL | NULL | 2025-07-25T07:58:48.3870000 | NULL | False | False | NULL | NULL |  |
| 5E286108-58B6-4D55-ABFA-FA4BDF81A252 | NULL | NULL | 2025-07-25T07:58:48.3870000 | NULL | False | False | NULL | NULL |  |
| 46EB4516-8FD4-45A9-869F-8977FA442554 | NULL | NULL | 2025-07-25T07:58:48.3870000 | NULL | False | False | NULL | NULL |  |
| 368BFEE2-C836-4853-BED8-873A11C1D360 | NULL | NULL | 2025-07-25T07:58:48.3870000 | NULL | False | False | NULL | NULL |  |
| 33EA5044-FE27-4FC0-A2DE-9B5460C8A279 | NULL | NULL | 2025-07-25T07:58:48.3870000 | NULL | False | False | NULL | NULL |  |
| 28B9181A-94AD-462B-BB6F-BAE775238759 | NULL | NULL | 2025-07-25T07:58:48.3870000 | NULL | False | False | NULL | NULL |  |
| 0E6C6565-C0D1-43AA-8359-EF0E40496939 | NULL | NULL | 2025-07-25T07:58:48.3870000 | NULL | False | False | NULL | NULL |  |
| 0CFF5814-6F32-4FCE-A494-DCB0E56E06CE | NULL | NULL | 2025-07-25T07:58:48.3870000 | NULL | False | False | NULL | NULL |  |
| 73217C16-D672-46EF-ACF7-622CC4FD954C | NULL | NULL | 2025-07-25T07:58:48.3870000 | NULL | False | False | NULL | NULL |  |
| BDE50156-2081-4F38-8291-610EFA9D166D | NULL | NULL | 2025-07-25T07:58:48.3870000 | NULL | False | False | NULL | NULL |  |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 76E1FEB0-A916-4F51-8D4F-A64F50812F42 | AE3A3D8B-EA93-450A-934E-BABBD698DA6B | AE3A3D8B-EA93-450A-934E-BABBD698DA6B | 2025-08-11T14:19:15.9200000 | 2025-08-11T14:46:00.0000000 | False | False | NULL | 172.16.100.58 |  |
| 63E9545D-1EBA-4F91-9880-850F1579FE19 | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-25T07:58:48.3870000 | 2025-08-02T10:30:36.0000000 | False | False | NULL |  |  |
| 9D8512EC-6890-40C8-9949-7142D5F3A45D | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-07-25T07:58:48.3870000 | 2025-08-02T10:29:12.0000000 | False | False | NULL |  |  |
| 73217C16-D672-46EF-ACF7-622CC4FD954C | NULL | NULL | 2025-07-25T07:58:48.3870000 | NULL | False | False | NULL | NULL |  |
| 5EFC6E96-C7B8-4E4C-913E-17BA4E973E1C | NULL | NULL | 2025-07-25T07:58:48.3870000 | NULL | False | False | NULL | NULL |  |
| 5E286108-58B6-4D55-ABFA-FA4BDF81A252 | NULL | NULL | 2025-07-25T07:58:48.3870000 | NULL | False | False | NULL | NULL |  |
| 46EB4516-8FD4-45A9-869F-8977FA442554 | NULL | NULL | 2025-07-25T07:58:48.3870000 | NULL | False | False | NULL | NULL |  |
| 368BFEE2-C836-4853-BED8-873A11C1D360 | NULL | NULL | 2025-07-25T07:58:48.3870000 | NULL | False | False | NULL | NULL |  |
| 33EA5044-FE27-4FC0-A2DE-9B5460C8A279 | NULL | NULL | 2025-07-25T07:58:48.3870000 | NULL | False | False | NULL | NULL |  |
| 28B9181A-94AD-462B-BB6F-BAE775238759 | NULL | NULL | 2025-07-25T07:58:48.3870000 | NULL | False | False | NULL | NULL |  |

---
