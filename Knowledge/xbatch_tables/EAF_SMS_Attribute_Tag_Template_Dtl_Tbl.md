# XStudio_Xbatch.dbo.EAF_SMS_Attribute_Tag_Template_Dtl_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference color, document, type, equation, extend, transaction, bwhhh, bwhl, bwlll, gthh, ltll, retrieval.

**Primary Key:** ID  
**Row Count:** 149  
**Date Range (ModifiedOn):** 2025-07-16T09:49:52.0000000 to 2025-07-16T09:49:52.0000000  

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
| 0D304145-7B04-4D33-B7E4-C0D15786D3BE | NULL | 232A34B5-AA22-43AD-8D3E-DFB85B9ECDB3 | NULL | NULL | 2025-07-11T11:47:32.6600000 | NULL | False | False | NULL |
| 0D1761C6-EAF0-43C0-8ABE-686A1762235B | NULL | 232A34B5-AA22-43AD-8D3E-DFB85B9ECDB3 | NULL | NULL | 2026-05-22T10:25:49.2930000 | NULL | False | False | NULL |
| 0B421839-0628-4BF3-9276-23D290D74C60 | NULL | 232A34B5-AA22-43AD-8D3E-DFB85B9ECDB3 | NULL | NULL | 2025-07-14T10:00:29.2400000 | NULL | False | False | NULL |
| 06908651-6F73-4C1C-B931-16D3D57F6587 | NULL | 232A34B5-AA22-43AD-8D3E-DFB85B9ECDB3 | NULL | NULL | 2025-07-11T11:47:32.6600000 | NULL | False | False | NULL |
| 0502647F-36B5-475B-84ED-437B5AC1EF19 | NULL | 232A34B5-AA22-43AD-8D3E-DFB85B9ECDB3 | NULL | NULL | 2026-05-22T10:28:23.1930000 | NULL | False | False | NULL |
| 04F3E6E9-A8CE-44B4-B8E9-C3979FD308C7 | NULL | 232A34B5-AA22-43AD-8D3E-DFB85B9ECDB3 | NULL | NULL | 2025-09-16T15:15:28.7100000 | NULL | False | False | NULL |
| 13C2D197-00FA-4C49-BC31-3D0F20356ECF | NULL | 232A34B5-AA22-43AD-8D3E-DFB85B9ECDB3 | NULL | NULL | 2025-09-09T09:38:05.4070000 | NULL | False | False | NULL |
| 1200FD82-D688-4ACE-A1FF-7A10E08ABA02 | NULL | 232A34B5-AA22-43AD-8D3E-DFB85B9ECDB3 | NULL | NULL | 2025-10-15T11:19:58.6130000 | NULL | False | False | NULL |
| 11C4F8E7-5A26-4460-89D0-88117CAE03C0 | NULL | 232A34B5-AA22-43AD-8D3E-DFB85B9ECDB3 | NULL | NULL | 2025-07-16T08:31:39.5030000 | NULL | False | False | NULL |
| 11A8D9D9-2FA4-42E9-9543-CB751021A922 | NULL | 232A34B5-AA22-43AD-8D3E-DFB85B9ECDB3 | NULL | NULL | 2025-10-06T14:02:48.8200000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10FF72CC-CCBC-4B35-B01E-115533F5E617 | NULL | 232A34B5-AA22-43AD-8D3E-DFB85B9ECDB3 | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-07-16T08:35:05.1030000 | 2025-07-16T09:49:52.0000000 | False | False | NULL |
| 13C2D197-00FA-4C49-BC31-3D0F20356ECF | NULL | 232A34B5-AA22-43AD-8D3E-DFB85B9ECDB3 | NULL | NULL | 2025-09-09T09:38:05.4070000 | NULL | False | False | NULL |
| 1200FD82-D688-4ACE-A1FF-7A10E08ABA02 | NULL | 232A34B5-AA22-43AD-8D3E-DFB85B9ECDB3 | NULL | NULL | 2025-10-15T11:19:58.6130000 | NULL | False | False | NULL |
| 11C4F8E7-5A26-4460-89D0-88117CAE03C0 | NULL | 232A34B5-AA22-43AD-8D3E-DFB85B9ECDB3 | NULL | NULL | 2025-07-16T08:31:39.5030000 | NULL | False | False | NULL |
| 11A8D9D9-2FA4-42E9-9543-CB751021A922 | NULL | 232A34B5-AA22-43AD-8D3E-DFB85B9ECDB3 | NULL | NULL | 2025-10-06T14:02:48.8200000 | NULL | False | False | NULL |
| 0D304145-7B04-4D33-B7E4-C0D15786D3BE | NULL | 232A34B5-AA22-43AD-8D3E-DFB85B9ECDB3 | NULL | NULL | 2025-07-11T11:47:32.6600000 | NULL | False | False | NULL |
| 0D1761C6-EAF0-43C0-8ABE-686A1762235B | NULL | 232A34B5-AA22-43AD-8D3E-DFB85B9ECDB3 | NULL | NULL | 2026-05-22T10:25:49.2930000 | NULL | False | False | NULL |
| 0B421839-0628-4BF3-9276-23D290D74C60 | NULL | 232A34B5-AA22-43AD-8D3E-DFB85B9ECDB3 | NULL | NULL | 2025-07-14T10:00:29.2400000 | NULL | False | False | NULL |
| 06908651-6F73-4C1C-B931-16D3D57F6587 | NULL | 232A34B5-AA22-43AD-8D3E-DFB85B9ECDB3 | NULL | NULL | 2025-07-11T11:47:32.6600000 | NULL | False | False | NULL |
| 0502647F-36B5-475B-84ED-437B5AC1EF19 | NULL | 232A34B5-AA22-43AD-8D3E-DFB85B9ECDB3 | NULL | NULL | 2026-05-22T10:28:23.1930000 | NULL | False | False | NULL |

---
