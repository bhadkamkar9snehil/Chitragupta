# XStudio_Xbatch.dbo.Billet_ChargingPlan

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference billet, grade, heat, sequence.

**Primary Key:** ID  
**Row Count:** 18  
**Date Range (ModifiedOn):** 2025-06-26T15:47:56.0000000 to 2025-06-27T15:42:05.0000000  

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
| BilletNo | varchar | YES | 100 | — |
| Sequence | int | YES | 10,0 | — |
| Grade | varchar | YES | 100 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 605D8012-674D-4B5F-A074-EE528C2E43E5 | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | NULL | 2025-06-26T12:43:06.1700000 | NULL | False | False | NULL |
| 45A710C0-0CB1-483D-8BE9-59CC576ED598 | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | NULL | 2025-06-26T12:43:06.1700000 | NULL | False | False | NULL |
| 39E487C7-CB69-42E8-A366-0C0F944D96E3 | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | NULL | 2025-06-26T12:43:06.1700000 | NULL | False | False | NULL |
| 368A20F2-10CE-4AAC-BDBD-13143EC2E725 | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | NULL | 2025-06-26T12:43:06.1700000 | NULL | False | False | NULL |
| 2EA55BBF-CA6D-418F-A46A-E426F0689181 | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | NULL | 2025-06-26T12:43:06.1700000 | NULL | False | False | NULL |
| 2DEBB5E1-8CBC-4B5F-8AB7-1ADB158A9464 | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | NULL | 2025-06-26T12:43:06.1700000 | NULL | False | False | NULL |
| 237F6247-9271-4C7A-8807-A2699D4B772D | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | NULL | 2025-06-26T12:43:06.1700000 | NULL | False | False | NULL |
| 0F594786-5D6E-4E6A-8264-A8CE6F81596D | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | NULL | 2025-06-26T12:43:06.1700000 | NULL | False | False | NULL |
| 0EBF5192-B97E-43C1-897E-9671BBCECE44 | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | NULL | 2025-06-26T12:43:06.1700000 | NULL | False | False | NULL |
| 6792C0AA-4FA4-4808-8A55-FFC93A375339 | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | NULL | 2025-06-26T12:43:06.1700000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D5F1C474-4BB0-4036-8A9B-AE69A5137166 | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-06-27T15:42:05.8270000 | 2025-06-27T15:42:05.0000000 | False | False | NULL |
| 29AAAEFD-11B4-4D03-BEA1-33B74F3E4639 | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-06-26T17:35:50.7170000 | 2025-06-26T17:35:50.0000000 | False | False | NULL |
| 67323245-8AFE-4CA0-9BA3-AA6E198B4015 | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-06-26T15:47:56.8870000 | 2025-06-26T15:47:56.0000000 | False | False | NULL |
| 605D8012-674D-4B5F-A074-EE528C2E43E5 | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | NULL | 2025-06-26T12:43:06.1700000 | NULL | False | False | NULL |
| 45A710C0-0CB1-483D-8BE9-59CC576ED598 | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | NULL | 2025-06-26T12:43:06.1700000 | NULL | False | False | NULL |
| 39E487C7-CB69-42E8-A366-0C0F944D96E3 | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | NULL | 2025-06-26T12:43:06.1700000 | NULL | False | False | NULL |
| 368A20F2-10CE-4AAC-BDBD-13143EC2E725 | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | NULL | 2025-06-26T12:43:06.1700000 | NULL | False | False | NULL |
| 2EA55BBF-CA6D-418F-A46A-E426F0689181 | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | NULL | 2025-06-26T12:43:06.1700000 | NULL | False | False | NULL |
| 2DEBB5E1-8CBC-4B5F-8AB7-1ADB158A9464 | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | NULL | 2025-06-26T12:43:06.1700000 | NULL | False | False | NULL |
| 237F6247-9271-4C7A-8807-A2699D4B772D | NULL | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | NULL | 2025-06-26T12:43:06.1700000 | NULL | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Billet_ChargingPlan.entityid` -> `XStudio_Configuration_XBatch.XStudio_Entities_Mst_Tbl.ID` (Many to One)
