# XStudio_Xbatch.dbo.XMES_SAP_API_GoodsMovement_Error

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference message, type, batch, body, error, manufacturing, material, movement, order, record, status, success.

**Primary Key:** ID  
**Row Count:** 1,371  
**Date Range (ModifiedOn):** 2026-01-12T14:31:04.0130000 to 2026-07-05T19:36:37.7770000  

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
| EntryDateTime | datetime | YES | — | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| TransactionID | varchar | YES | 100 | — |
| RecordID | varchar | YES | 100 | — |
| Body | varchar | YES | -1 | — |
| ErrorMessage | varchar | YES | -1 | — |
| Status | varchar | YES | 50 | — |
| Type | varchar | YES | 100 | — |
| Batch | varchar | YES | 100 | — |
| ManufacturingOrder | varchar | YES | 100 | — |
| Material | varchar | YES | 100 | — |
| MovementType | int | YES | 10,0 | — |
| SuccessMessage | varchar | YES | -1 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5251C0A3-A4C1-4294-AEA5-6F81EB72DB3B | NULL | NULL | NULL | NULL | 2026-01-12T14:31:04.0130000 | 2026-01-12T14:31:04.0130000 | False | False | NULL |
| B2097BB5-6A8A-4D28-B4F7-271F2EB2E250 | NULL | NULL | NULL | NULL | 2026-01-12T14:38:01.3600000 | 2026-01-12T14:38:01.3600000 | False | False | NULL |
| 12373603-2B79-4189-8B07-97A4AD3B047A | NULL | NULL | NULL | NULL | 2026-01-12T14:38:33.5170000 | 2026-01-12T14:38:33.5170000 | False | False | NULL |
| 3747AA31-5D7D-4795-B8C2-5B03C1334E43 | NULL | NULL | NULL | NULL | 2026-01-12T14:39:32.3500000 | 2026-01-12T14:39:32.3500000 | False | False | NULL |
| D872C3AE-4791-4D39-BE83-B9AB244B0179 | NULL | NULL | NULL | NULL | 2026-01-12T14:41:06.1170000 | 2026-01-12T14:41:06.1170000 | False | False | NULL |
| 8125C7CD-FA41-4FAF-962D-26A14374E281 | NULL | NULL | NULL | NULL | 2026-01-12T14:41:48.3670000 | 2026-01-12T14:41:48.3670000 | False | False | NULL |
| DF7AD4CC-7AF8-4197-BD38-EAD2F9A8C187 | NULL | NULL | NULL | NULL | 2026-01-12T14:42:07.7530000 | 2026-01-12T14:42:07.7530000 | False | False | NULL |
| CEBDCAB1-2604-4BBE-A98B-E9DE8992D470 | NULL | NULL | NULL | NULL | 2026-01-12T14:42:51.8130000 | 2026-01-12T14:42:51.8130000 | False | False | NULL |
| 581E3C0B-F1FE-49D7-9ECE-CD7A95C4F50B | NULL | NULL | NULL | NULL | 2026-01-12T14:43:33.0900000 | 2026-01-12T14:43:33.0900000 | False | False | NULL |
| 371EA4FA-7815-4AA1-8F75-BB95A2D1DB7E | NULL | NULL | NULL | NULL | 2026-01-12T14:51:23.1070000 | 2026-01-12T14:51:23.1070000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7B040D40-3C4A-40F9-831C-4AAED87521D9 | NULL | NULL | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 2026-07-05T19:36:37.7570000 | 2026-07-05T19:36:37.7770000 | False | False | NULL |
| B52D0A6D-46B0-43A5-8C67-9EAE77C14E11 | NULL | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-07-05T12:54:01.8870000 | 2026-07-05T12:54:01.8900000 | False | False | NULL |
| FF5BFD9F-C9CC-427E-B5A0-3D03104D66D8 | NULL | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-07-05T12:53:31.9500000 | 2026-07-05T12:53:31.9630000 | False | False | NULL |
| 4E443C32-F9B2-4137-818B-4035CCEBDFCD | NULL | NULL | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 2026-07-05T10:29:41.0770000 | 2026-07-05T10:29:41.0900000 | False | False | NULL |
| A623E9BC-0D43-4530-95D7-195BE5C30FFD | NULL | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-05T01:37:01.6430000 | 2026-07-05T01:37:01.6870000 | False | False | NULL |
| 1A557436-337E-46C6-B8E5-E16ED32CAC7C | NULL | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-05T01:35:41.4370000 | 2026-07-05T01:35:41.4530000 | False | False | NULL |
| 3F519A28-3C97-481F-B506-EB833C2A26F6 | NULL | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-05T01:34:32.1970000 | 2026-07-05T01:34:32.2100000 | False | False | NULL |
| 5804E0ED-0866-463B-A9BC-8E47BC03C918 | NULL | NULL | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 2026-07-01T14:13:36.0200000 | 2026-07-01T14:13:36.0500000 | False | False | NULL |
| A463F9A2-63FC-481F-8D40-A2D6F305BDF9 | NULL | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-01T12:38:25.4570000 | 2026-07-01T12:38:25.4830000 | False | False | NULL |
| 27B8E05A-17F6-4E62-B3CB-EB6BB0046807 | NULL | NULL | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-07-01T12:37:23.7600000 | 2026-07-01T12:37:23.7970000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.MES_SAP_By_Product_Trn_Tbl.Saptransactionid` -> `XStudio_XBatch.XMES_SAP_API_GoodsMovement_Error.TransactionID` (Many to One)
- `XStudio_XBatch.MES_SAP_Consumption_Trn_Tbl.Saptransactionid` -> `XStudio_XBatch.XMES_SAP_API_GoodsMovement_Error.TransactionID` (Many to One)
- `XStudio_XBatch.MES_SAP_Production_Trn_Tbl.Saptransactionid` -> `XStudio_XBatch.XMES_SAP_API_GoodsMovement_Error.TransactionID` (Many to One)
