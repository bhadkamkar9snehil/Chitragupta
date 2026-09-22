# XStudio_Xbatch.dbo.CCM_SMS_Attribute_Tag_Template_Dtl_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference color, document, type, equation, extend, transaction, bwhhh, bwhl, bwlll, gthh, ltll, retrieval.

**Primary Key:** ID  
**Row Count:** 141  

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
| 0E12A6E9-9DC7-43A2-A439-6778490C2313 | NULL | 29744244-AD1E-4304-8CE8-9C702ABD88C9 | NULL | NULL | 2025-09-16T13:22:20.4570000 | NULL | False | False | NULL |
| 0E0B5947-C766-4598-A661-8ED3EA7FD799 | NULL | 29744244-AD1E-4304-8CE8-9C702ABD88C9 | NULL | NULL | 2025-09-16T13:17:06.4300000 | NULL | False | False | NULL |
| 0AC1B5EB-311F-4D91-AFA6-D69CA684EC1C | NULL | 29744244-AD1E-4304-8CE8-9C702ABD88C9 | NULL | NULL | 2025-09-16T14:04:03.7130000 | NULL | False | False | NULL |
| 099069F0-1857-4E66-A0C1-A8437334EA68 | NULL | 29744244-AD1E-4304-8CE8-9C702ABD88C9 | NULL | NULL | 2025-10-01T09:12:37.8900000 | NULL | False | False | NULL |
| 095F0ED8-6CDD-4C9B-A18D-025D5708EFE9 | NULL | 29744244-AD1E-4304-8CE8-9C702ABD88C9 | NULL | NULL | 2025-08-28T10:04:55.8500000 | NULL | False | False | NULL |
| 094C60AD-724F-4978-866C-4897303CE8F8 | NULL | 29744244-AD1E-4304-8CE8-9C702ABD88C9 | NULL | NULL | 2025-09-16T14:18:31.7330000 | NULL | False | False | NULL |
| 04E47783-3BC9-4DF6-8AFD-6ECC01B1E8DA | NULL | 29744244-AD1E-4304-8CE8-9C702ABD88C9 | NULL | NULL | 2025-08-27T17:37:42.1270000 | NULL | False | False | NULL |
| 0362B2E3-9FB1-4A8C-B66F-F031DF2EA233 | NULL | 29744244-AD1E-4304-8CE8-9C702ABD88C9 | NULL | NULL | 2025-08-27T17:36:13.0830000 | NULL | False | False | NULL |
| 0333C892-09D4-4CCF-901F-2D6BEC52CB58 | NULL | 29744244-AD1E-4304-8CE8-9C702ABD88C9 | NULL | NULL | 2025-08-30T09:10:42.8530000 | NULL | False | False | NULL |
| 0267824B-51FA-4B8C-89F2-5BFE72CDC899 | NULL | 29744244-AD1E-4304-8CE8-9C702ABD88C9 | NULL | NULL | 2025-09-16T14:09:53.0230000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0E12A6E9-9DC7-43A2-A439-6778490C2313 | NULL | 29744244-AD1E-4304-8CE8-9C702ABD88C9 | NULL | NULL | 2025-09-16T13:22:20.4570000 | NULL | False | False | NULL |
| 0E0B5947-C766-4598-A661-8ED3EA7FD799 | NULL | 29744244-AD1E-4304-8CE8-9C702ABD88C9 | NULL | NULL | 2025-09-16T13:17:06.4300000 | NULL | False | False | NULL |
| 0AC1B5EB-311F-4D91-AFA6-D69CA684EC1C | NULL | 29744244-AD1E-4304-8CE8-9C702ABD88C9 | NULL | NULL | 2025-09-16T14:04:03.7130000 | NULL | False | False | NULL |
| 099069F0-1857-4E66-A0C1-A8437334EA68 | NULL | 29744244-AD1E-4304-8CE8-9C702ABD88C9 | NULL | NULL | 2025-10-01T09:12:37.8900000 | NULL | False | False | NULL |
| 095F0ED8-6CDD-4C9B-A18D-025D5708EFE9 | NULL | 29744244-AD1E-4304-8CE8-9C702ABD88C9 | NULL | NULL | 2025-08-28T10:04:55.8500000 | NULL | False | False | NULL |
| 094C60AD-724F-4978-866C-4897303CE8F8 | NULL | 29744244-AD1E-4304-8CE8-9C702ABD88C9 | NULL | NULL | 2025-09-16T14:18:31.7330000 | NULL | False | False | NULL |
| 04E47783-3BC9-4DF6-8AFD-6ECC01B1E8DA | NULL | 29744244-AD1E-4304-8CE8-9C702ABD88C9 | NULL | NULL | 2025-08-27T17:37:42.1270000 | NULL | False | False | NULL |
| 0362B2E3-9FB1-4A8C-B66F-F031DF2EA233 | NULL | 29744244-AD1E-4304-8CE8-9C702ABD88C9 | NULL | NULL | 2025-08-27T17:36:13.0830000 | NULL | False | False | NULL |
| 0333C892-09D4-4CCF-901F-2D6BEC52CB58 | NULL | 29744244-AD1E-4304-8CE8-9C702ABD88C9 | NULL | NULL | 2025-08-30T09:10:42.8530000 | NULL | False | False | NULL |
| 0267824B-51FA-4B8C-89F2-5BFE72CDC899 | NULL | 29744244-AD1E-4304-8CE8-9C702ABD88C9 | NULL | NULL | 2025-09-16T14:09:53.0230000 | NULL | False | False | NULL |

---
