# XStudio_Xbatch.dbo.RM_Rebar_Attribute_Tag_Template_Dtl_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference color, document, type, equation, extend, transaction, bwhhh, bwhl, bwlll, gthh, ltll, retrieval.

**Primary Key:** ID  
**Row Count:** 75  

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
| 2101538B-240C-45CD-A65D-98CF2A90E82C | NULL | 9FBCB1EE-E898-435E-9EE8-F15E06B2F79B | NULL | NULL | 2025-11-26T10:23:10.7900000 | NULL | False | False | NULL |
| 201D3C80-EB4C-4F1C-8E71-BFEB7F8C6970 | NULL | 9FBCB1EE-E898-435E-9EE8-F15E06B2F79B | NULL | NULL | 2025-11-26T10:56:34.5600000 | NULL | False | False | NULL |
| 1AA90B05-78A2-48BD-B82C-C03EF9D4325D | NULL | 9FBCB1EE-E898-435E-9EE8-F15E06B2F79B | NULL | NULL | 2025-11-26T10:41:37.0630000 | NULL | False | False | NULL |
| 188AF4D0-F669-4510-9B2F-DF0F21F46693 | NULL | 9FBCB1EE-E898-435E-9EE8-F15E06B2F79B | NULL | NULL | 2025-11-26T10:28:13.0600000 | NULL | False | False | NULL |
| 125A9D48-E177-4F71-858E-6279819FBA92 | NULL | 9FBCB1EE-E898-435E-9EE8-F15E06B2F79B | NULL | NULL | 2025-11-26T10:55:48.9700000 | NULL | False | False | NULL |
| 105749E6-6C75-4C7F-80B7-E3305B95C4C6 | NULL | 9FBCB1EE-E898-435E-9EE8-F15E06B2F79B | NULL | NULL | 2025-11-26T10:19:43.0730000 | NULL | False | False | NULL |
| 0FCBBA79-53D1-42D7-88D1-F35CC6580410 | NULL | 9FBCB1EE-E898-435E-9EE8-F15E06B2F79B | NULL | NULL | 2025-11-26T10:37:38.9800000 | NULL | False | False | NULL |
| 0BF328BC-8B8C-4E36-8054-DDE5B1BB4F24 | NULL | 9FBCB1EE-E898-435E-9EE8-F15E06B2F79B | NULL | NULL | 2025-11-26T10:42:56.1470000 | NULL | False | False | NULL |
| 0B26F95F-80E3-4320-A903-3EC2439C1199 | NULL | 9FBCB1EE-E898-435E-9EE8-F15E06B2F79B | NULL | NULL | 2025-11-26T10:24:34.6800000 | NULL | False | False | NULL |
| 0ABF85A2-2DE1-48D9-8BD9-EC15B2F87A43 | NULL | 9FBCB1EE-E898-435E-9EE8-F15E06B2F79B | NULL | NULL | 2025-11-26T10:30:24.7070000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2101538B-240C-45CD-A65D-98CF2A90E82C | NULL | 9FBCB1EE-E898-435E-9EE8-F15E06B2F79B | NULL | NULL | 2025-11-26T10:23:10.7900000 | NULL | False | False | NULL |
| 201D3C80-EB4C-4F1C-8E71-BFEB7F8C6970 | NULL | 9FBCB1EE-E898-435E-9EE8-F15E06B2F79B | NULL | NULL | 2025-11-26T10:56:34.5600000 | NULL | False | False | NULL |
| 1AA90B05-78A2-48BD-B82C-C03EF9D4325D | NULL | 9FBCB1EE-E898-435E-9EE8-F15E06B2F79B | NULL | NULL | 2025-11-26T10:41:37.0630000 | NULL | False | False | NULL |
| 188AF4D0-F669-4510-9B2F-DF0F21F46693 | NULL | 9FBCB1EE-E898-435E-9EE8-F15E06B2F79B | NULL | NULL | 2025-11-26T10:28:13.0600000 | NULL | False | False | NULL |
| 125A9D48-E177-4F71-858E-6279819FBA92 | NULL | 9FBCB1EE-E898-435E-9EE8-F15E06B2F79B | NULL | NULL | 2025-11-26T10:55:48.9700000 | NULL | False | False | NULL |
| 105749E6-6C75-4C7F-80B7-E3305B95C4C6 | NULL | 9FBCB1EE-E898-435E-9EE8-F15E06B2F79B | NULL | NULL | 2025-11-26T10:19:43.0730000 | NULL | False | False | NULL |
| 0FCBBA79-53D1-42D7-88D1-F35CC6580410 | NULL | 9FBCB1EE-E898-435E-9EE8-F15E06B2F79B | NULL | NULL | 2025-11-26T10:37:38.9800000 | NULL | False | False | NULL |
| 0BF328BC-8B8C-4E36-8054-DDE5B1BB4F24 | NULL | 9FBCB1EE-E898-435E-9EE8-F15E06B2F79B | NULL | NULL | 2025-11-26T10:42:56.1470000 | NULL | False | False | NULL |
| 0B26F95F-80E3-4320-A903-3EC2439C1199 | NULL | 9FBCB1EE-E898-435E-9EE8-F15E06B2F79B | NULL | NULL | 2025-11-26T10:24:34.6800000 | NULL | False | False | NULL |
| 0ABF85A2-2DE1-48D9-8BD9-EC15B2F87A43 | NULL | 9FBCB1EE-E898-435E-9EE8-F15E06B2F79B | NULL | NULL | 2025-11-26T10:30:24.7070000 | NULL | False | False | NULL |

---
