# XStudio_Xbatch.dbo.RM_WRM_Attribute_Tag_Template_Dtl_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference color, document, type, equation, extend, transaction, bwhhh, bwhl, bwlll, gthh, ltll, retrieval.

**Primary Key:** ID  
**Row Count:** 227  

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
| 0CFEB9E0-7F62-446B-B55C-4AD471F7CA10 | NULL | 93E7AE83-9638-4B90-BFF7-06872AA41C55 | NULL | NULL | 2025-11-26T09:06:49.0130000 | NULL | False | False | NULL |
| 0A946CC1-2DEA-4A0D-A304-F6844F659CFE | NULL | 93E7AE83-9638-4B90-BFF7-06872AA41C55 | NULL | NULL | 2025-09-16T15:26:07.1570000 | NULL | False | False | NULL |
| 0A276CC5-C580-4D20-B1F6-E9CD44D7079B | NULL | 93E7AE83-9638-4B90-BFF7-06872AA41C55 | NULL | NULL | 2025-09-16T15:26:07.1570000 | NULL | False | False | NULL |
| 0A00FEF8-16A7-43DA-8757-8ECBF011F9FA | NULL | 93E7AE83-9638-4B90-BFF7-06872AA41C55 | NULL | NULL | 2025-11-26T09:26:23.8730000 | NULL | False | False | NULL |
| 09D6B244-AAB6-48DF-AA7F-D90696FB7221 | NULL | 93E7AE83-9638-4B90-BFF7-06872AA41C55 | NULL | NULL | 2025-09-24T12:53:27.2100000 | NULL | False | False | NULL |
| 09A30D4D-F649-4DA3-94F6-AB3B4EB80219 | NULL | 93E7AE83-9638-4B90-BFF7-06872AA41C55 | NULL | NULL | 2025-09-16T15:26:07.1570000 | NULL | False | False | NULL |
| 07FCFD83-6C77-4225-A70C-357E8F4AF108 | NULL | 93E7AE83-9638-4B90-BFF7-06872AA41C55 | NULL | NULL | 2025-09-16T15:26:07.1570000 | NULL | False | False | NULL |
| 079EBDBA-41AF-406F-A9C5-C14C1F7E0231 | NULL | 93E7AE83-9638-4B90-BFF7-06872AA41C55 | NULL | NULL | 2025-09-24T10:37:34.5070000 | NULL | False | False | NULL |
| 0782F1B2-E67E-4C91-BB0E-5024475DE5F4 | NULL | 93E7AE83-9638-4B90-BFF7-06872AA41C55 | NULL | NULL | 2025-09-24T11:07:52.1300000 | NULL | False | False | NULL |
| 046E401C-CFC5-4991-97FD-F7239BCEADD5 | NULL | 93E7AE83-9638-4B90-BFF7-06872AA41C55 | NULL | NULL | 2025-11-26T09:31:33.6430000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0CFEB9E0-7F62-446B-B55C-4AD471F7CA10 | NULL | 93E7AE83-9638-4B90-BFF7-06872AA41C55 | NULL | NULL | 2025-11-26T09:06:49.0130000 | NULL | False | False | NULL |
| 0A946CC1-2DEA-4A0D-A304-F6844F659CFE | NULL | 93E7AE83-9638-4B90-BFF7-06872AA41C55 | NULL | NULL | 2025-09-16T15:26:07.1570000 | NULL | False | False | NULL |
| 0A276CC5-C580-4D20-B1F6-E9CD44D7079B | NULL | 93E7AE83-9638-4B90-BFF7-06872AA41C55 | NULL | NULL | 2025-09-16T15:26:07.1570000 | NULL | False | False | NULL |
| 0A00FEF8-16A7-43DA-8757-8ECBF011F9FA | NULL | 93E7AE83-9638-4B90-BFF7-06872AA41C55 | NULL | NULL | 2025-11-26T09:26:23.8730000 | NULL | False | False | NULL |
| 09D6B244-AAB6-48DF-AA7F-D90696FB7221 | NULL | 93E7AE83-9638-4B90-BFF7-06872AA41C55 | NULL | NULL | 2025-09-24T12:53:27.2100000 | NULL | False | False | NULL |
| 09A30D4D-F649-4DA3-94F6-AB3B4EB80219 | NULL | 93E7AE83-9638-4B90-BFF7-06872AA41C55 | NULL | NULL | 2025-09-16T15:26:07.1570000 | NULL | False | False | NULL |
| 07FCFD83-6C77-4225-A70C-357E8F4AF108 | NULL | 93E7AE83-9638-4B90-BFF7-06872AA41C55 | NULL | NULL | 2025-09-16T15:26:07.1570000 | NULL | False | False | NULL |
| 079EBDBA-41AF-406F-A9C5-C14C1F7E0231 | NULL | 93E7AE83-9638-4B90-BFF7-06872AA41C55 | NULL | NULL | 2025-09-24T10:37:34.5070000 | NULL | False | False | NULL |
| 0782F1B2-E67E-4C91-BB0E-5024475DE5F4 | NULL | 93E7AE83-9638-4B90-BFF7-06872AA41C55 | NULL | NULL | 2025-09-24T11:07:52.1300000 | NULL | False | False | NULL |
| 046E401C-CFC5-4991-97FD-F7239BCEADD5 | NULL | 93E7AE83-9638-4B90-BFF7-06872AA41C55 | NULL | NULL | 2025-11-26T09:31:33.6430000 | NULL | False | False | NULL |

---
