# XStudio_Xbatch.dbo.RM_Mill_Attribute_Tag_Template_Dtl_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference color, document, type, equation, extend, transaction, bwhhh, bwhl, bwlll, gthh, ltll, retrieval.

**Primary Key:** ID  
**Row Count:** 239  

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
| 0B228738-96F5-4E7A-A750-BAA3EDD9997B | NULL | 9D13728A-C1EF-42F5-8DA2-4DCAD011A553 | NULL | NULL | 2025-10-30T10:34:29.2200000 | NULL | False | False | NULL |
| 09F9A2B6-E532-4F9C-8E8C-E69836C4CD25 | NULL | 2A8AAB24-987D-443D-8097-F964CAA94A16 | NULL | NULL | 2025-09-24T14:38:31.4300000 | NULL | False | False | NULL |
| 06F65A2C-ADCA-480C-8DBD-13392009BDA2 | NULL | 9D13728A-C1EF-42F5-8DA2-4DCAD011A553 | NULL | NULL | 2025-10-30T10:34:29.2200000 | NULL | False | False | NULL |
| 05FBC260-F939-4E45-98F0-940052B797A4 | NULL | 9D13728A-C1EF-42F5-8DA2-4DCAD011A553 | NULL | NULL | 2025-10-30T10:34:29.2200000 | NULL | False | False | NULL |
| 05AF0F38-8D87-4E81-8D4E-FDB6DEFA3D39 | NULL | 2A8AAB24-987D-443D-8097-F964CAA94A16 | NULL | NULL | 2025-09-24T13:56:09.8700000 | NULL | False | False | NULL |
| 056F2A5C-0CDA-45A4-B94C-74F829B38D24 | NULL | 9D13728A-C1EF-42F5-8DA2-4DCAD011A553 | NULL | NULL | 2025-10-30T10:34:29.2200000 | NULL | False | False | NULL |
| 02C2E9FD-9FE2-44F5-9409-0256B9B16106 | NULL | 9D13728A-C1EF-42F5-8DA2-4DCAD011A553 | NULL | NULL | 2025-10-30T10:34:29.2200000 | NULL | False | False | NULL |
| 023D66F3-A8E8-4F35-A811-2C8A104E7FAE | NULL | 2A8AAB24-987D-443D-8097-F964CAA94A16 | NULL | NULL | 2025-09-24T13:41:25.5100000 | NULL | False | False | NULL |
| 021C0E63-CE61-4EB3-B221-22932BB352C4 | NULL | 2A8AAB24-987D-443D-8097-F964CAA94A16 | NULL | NULL | 2025-09-22T12:32:02.6900000 | NULL | False | False | NULL |
| 01F29D4D-7E4D-4D69-A652-F4D909F98053 | NULL | 9D13728A-C1EF-42F5-8DA2-4DCAD011A553 | NULL | NULL | 2025-10-30T10:34:29.2200000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0B228738-96F5-4E7A-A750-BAA3EDD9997B | NULL | 9D13728A-C1EF-42F5-8DA2-4DCAD011A553 | NULL | NULL | 2025-10-30T10:34:29.2200000 | NULL | False | False | NULL |
| 09F9A2B6-E532-4F9C-8E8C-E69836C4CD25 | NULL | 2A8AAB24-987D-443D-8097-F964CAA94A16 | NULL | NULL | 2025-09-24T14:38:31.4300000 | NULL | False | False | NULL |
| 06F65A2C-ADCA-480C-8DBD-13392009BDA2 | NULL | 9D13728A-C1EF-42F5-8DA2-4DCAD011A553 | NULL | NULL | 2025-10-30T10:34:29.2200000 | NULL | False | False | NULL |
| 05FBC260-F939-4E45-98F0-940052B797A4 | NULL | 9D13728A-C1EF-42F5-8DA2-4DCAD011A553 | NULL | NULL | 2025-10-30T10:34:29.2200000 | NULL | False | False | NULL |
| 05AF0F38-8D87-4E81-8D4E-FDB6DEFA3D39 | NULL | 2A8AAB24-987D-443D-8097-F964CAA94A16 | NULL | NULL | 2025-09-24T13:56:09.8700000 | NULL | False | False | NULL |
| 056F2A5C-0CDA-45A4-B94C-74F829B38D24 | NULL | 9D13728A-C1EF-42F5-8DA2-4DCAD011A553 | NULL | NULL | 2025-10-30T10:34:29.2200000 | NULL | False | False | NULL |
| 02C2E9FD-9FE2-44F5-9409-0256B9B16106 | NULL | 9D13728A-C1EF-42F5-8DA2-4DCAD011A553 | NULL | NULL | 2025-10-30T10:34:29.2200000 | NULL | False | False | NULL |
| 023D66F3-A8E8-4F35-A811-2C8A104E7FAE | NULL | 2A8AAB24-987D-443D-8097-F964CAA94A16 | NULL | NULL | 2025-09-24T13:41:25.5100000 | NULL | False | False | NULL |
| 021C0E63-CE61-4EB3-B221-22932BB352C4 | NULL | 2A8AAB24-987D-443D-8097-F964CAA94A16 | NULL | NULL | 2025-09-22T12:32:02.6900000 | NULL | False | False | NULL |
| 01F29D4D-7E4D-4D69-A652-F4D909F98053 | NULL | 9D13728A-C1EF-42F5-8DA2-4DCAD011A553 | NULL | NULL | 2025-10-30T10:34:29.2200000 | NULL | False | False | NULL |

---
