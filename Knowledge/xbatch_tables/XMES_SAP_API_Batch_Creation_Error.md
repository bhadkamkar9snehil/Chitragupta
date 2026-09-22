# XStudio_Xbatch.dbo.XMES_SAP_API_Batch_Creation_Error

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference message, batch, body, error, record, status, success, transaction.

**Primary Key:** ID  
**Row Count:** 249  
**Date Range (ModifiedOn):** 2026-02-02T14:36:23.4470000 to 2026-06-28T12:51:16.3000000  

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
| ParentID | varchar | YES | 36 | — |
| Status | varchar | YES | 50 | — |
| RecordID | varchar | YES | 100 | — |
| Name | varchar | YES | 100 | — |
| TransactionID | varchar | YES | 100 | — |
| ReportDate | date | YES | — | — |
| ErrorMessage | varchar | YES | -1 | — |
| IsProcessed | bit | YES | — | — |
| Body | varchar | YES | -1 | — |
| EntryDateTime | datetime | YES | — | — |
| BatchNo | varchar | YES | 100 | — |
| SuccessMessage | varchar | YES | -1 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1B85115E-DB1D-433E-A57C-BA9827AA43AD | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2026-02-02T14:36:23.4470000 | 2026-02-02T14:36:23.4470000 | False | False | NULL | NULL | NULL |
| 4F3CFC0B-3E48-497B-9143-3D0B788573F1 | NULL | NULL | 2026-02-02T15:39:49.9930000 | 2026-02-02T15:39:49.9930000 | False | False | NULL | NULL | NULL |
| E4C77DBE-269B-4B66-A968-C7A23C6F5752 | NULL | NULL | 2026-02-02T15:39:52.9970000 | 2026-02-02T15:39:52.9970000 | False | False | NULL | NULL | NULL |
| BBC1EF98-A21F-44A6-A39A-A62047E3B5D1 | NULL | NULL | 2026-02-02T16:45:01.7800000 | 2026-02-02T16:45:01.7800000 | False | False | NULL | NULL | NULL |
| 4236EB8B-8AB9-4CB9-8ACF-4659E4F43A78 | NULL | NULL | 2026-02-02T17:02:41.3630000 | 2026-02-02T17:02:41.3630000 | False | False | NULL | NULL | NULL |
| D4ADC9CB-02B8-4FD3-96CB-EED3863BF4CF | NULL | NULL | 2026-02-02T17:13:41.8030000 | 2026-02-02T17:13:41.8030000 | False | False | NULL | NULL | NULL |
| A6F4D674-83F3-448D-BB92-42894124071F | NULL | NULL | 2026-02-02T17:13:51.1500000 | 2026-02-02T17:13:51.1500000 | False | False | NULL | NULL | NULL |
| 5A2EC623-5791-4EAD-A6F5-F0A89B281F5D | NULL | NULL | 2026-02-02T17:17:32.0870000 | 2026-02-02T17:17:32.0870000 | False | False | NULL | NULL | NULL |
| EAC66909-FF6E-45F7-89F9-786301D4E66A | NULL | NULL | 2026-02-02T17:44:19.3370000 | 2026-02-02T17:44:19.3370000 | False | False | NULL | NULL | NULL |
| AF694C70-9EFC-4D72-9C4E-DB0CE561FED1 | NULL | NULL | 2026-02-02T17:48:13.6230000 | 2026-02-02T17:48:13.6230000 | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B94C019D-3A14-4063-8BD1-9DB0A9B4B0BB | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-06-28T12:51:16.3000000 | 2026-06-28T12:51:16.3000000 | False | False | NULL | NULL | NULL |
| A51D5BE6-8039-4983-A9DF-800A5A4D9336 | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-06-28T10:56:51.2100000 | 2026-06-28T10:56:51.2100000 | False | False | NULL | NULL | NULL |
| C1C712F9-8ED0-4E15-A37A-7493B339B7E3 | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-06-28T10:56:49.7500000 | 2026-06-28T10:56:49.7500000 | False | False | NULL | NULL | NULL |
| B17B5919-A5EC-4FD4-ABB7-21481742A2F8 | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-06-27T18:56:16.1700000 | 2026-06-27T18:56:16.1700000 | False | False | NULL | NULL | NULL |
| 6755D21A-47CE-4623-A143-7CD8749A0B7F | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-06-27T18:56:07.8170000 | 2026-06-27T18:56:07.8170000 | False | False | NULL | NULL | NULL |
| E97A0859-92A9-4D45-9752-14D03DC9A09B | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-06-27T02:35:23.6800000 | 2026-06-27T02:35:23.6800000 | False | False | NULL | NULL | NULL |
| 82AC514D-9115-46C9-AE02-0ECBEB237555 | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-06-27T02:29:03.0470000 | 2026-06-27T02:29:03.0470000 | False | False | NULL | NULL | NULL |
| F1F59E09-AA1D-41C1-8F3A-6692E7D95293 | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-06-27T02:27:17.9630000 | 2026-06-27T02:27:17.9630000 | False | False | NULL | NULL | NULL |
| 3E3467EE-204D-4A28-A1FD-808054C59839 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-06-24T08:20:08.0870000 | 2026-06-24T08:20:08.0870000 | False | False | NULL | NULL | NULL |
| 5E841E64-D047-4D3E-931C-19B1E1BB637D | CF587DA9-0FDF-494E-8044-7620D00418AE | CF587DA9-0FDF-494E-8044-7620D00418AE | 2026-06-24T01:49:34.3200000 | 2026-06-24T01:49:34.3200000 | False | False | NULL | NULL | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XMES_SAP_CreateBatch_Mst_Tbl.SAPTransactionID` -> `XStudio_XBatch.XMES_SAP_API_Batch_Creation_Error.TransactionID` (One to One)
