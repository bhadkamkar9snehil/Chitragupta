# XStudio_Xbatch.dbo.XMES_Work_Order_Trn_Tbl

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** execution, order, work (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference campaign, order, work.

**Primary Key:** ID  
**Row Count:** 20  
**Date Range (ModifiedOn):** 2026-07-28T15:57:28.0000000 to 2026-08-07T08:43:42.0000000  

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
| WorkOrder | varchar | YES | 36 | — |
| CampaignID | varchar | YES | 36 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 82CF0304-1B55-46CA-ADD0-7BB39B055F88 | NULL | NULL | NULL | NULL | 2026-08-24T16:05:08.7070000 | NULL | False | False | NULL |
| 587E1840-8172-4BBC-BD13-0032ED4AB015 | NULL | NULL | NULL | NULL | 2026-08-17T18:07:08.8570000 | NULL | False | False | NULL |
| 92041667-C131-4220-815A-D791E353C07E | NULL | NULL | NULL | NULL | 2026-08-21T15:57:57.2770000 | NULL | False | False | NULL |
| B19F830E-AC7D-4226-941D-B3F6A2EB4D41 | NULL | NULL | NULL | NULL | 2026-09-01T00:00:00.6970000 | NULL | False | False | NULL |
| CE3818AA-F457-4C26-9229-5F4A362049C8 | NULL | NULL | NULL | NULL | 2026-08-11T09:18:41.4070000 | NULL | False | False | NULL |
| CF42B20D-D55E-4F59-BA90-BA1544A2B47E | NULL | NULL | NULL | NULL | 2026-08-12T16:29:00.0170000 | NULL | False | False | NULL |
| E4A450E7-0B94-4787-AD78-2FEC19F1AF47 | NULL | NULL | NULL | NULL | 2026-08-11T17:08:10.4670000 | NULL | False | False | NULL |
| AE22528C-7CA3-4953-BF88-0D6FEB52AA72 | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-28T15:56:38.9830000 | 2026-07-28T15:57:28.0000000 | False | False | NULL |
| 19034199-3FC3-4D81-8F2E-FD7B4509FC0D | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-28T10:10:43.9070000 | 2026-07-30T15:22:04.0000000 | False | False | NULL |
| 5543695C-B3ED-4734-82D9-BC1D067EA06E | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-28T15:57:09.9170000 | 2026-07-30T15:22:05.0000000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 044F8822-9A26-4093-B627-474B94FD84F5 | NULL | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-08-07T08:43:42.9770000 | 2026-08-07T08:43:42.0000000 | False | False | NULL |
| 2567B711-3C6B-452E-B0B8-BB87FB58262B | NULL | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-08-06T08:58:45.4230000 | 2026-08-06T08:58:45.0000000 | False | False | NULL |
| C3DBB95D-64BA-4EA1-ABBA-E1F8B015042B | NULL | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-08-06T08:57:27.6830000 | 2026-08-06T08:57:27.0000000 | False | False | NULL |
| CE86CD3F-9AD0-4C52-BC18-AD3511E96244 | NULL | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-08-06T08:56:12.0370000 | 2026-08-06T08:56:12.0000000 | False | False | NULL |
| 9035FE02-61B4-441C-A6CF-F754CF118678 | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-31T09:57:10.4900000 | 2026-07-31T09:57:10.0000000 | False | False | NULL |
| 8D2FC27E-9118-44B1-B89F-4D1C71405A78 | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-31T09:55:25.4930000 | 2026-07-31T09:55:25.0000000 | False | False | NULL |
| D4624BAE-3BE2-4BAA-8C5B-D78C80AECE9C | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-28T10:09:12.7700000 | 2026-07-30T15:26:15.0000000 | False | False | NULL |
| EDB79AFB-9C77-44AB-9BA7-BF775EE3B10A | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-28T10:00:11.6600000 | 2026-07-30T15:26:15.0000000 | False | False | NULL |
| FDDF492F-7E84-4348-87BA-7292CD81C3A9 | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-28T10:07:32.6000000 | 2026-07-30T15:26:15.0000000 | False | False | NULL |
| 5543695C-B3ED-4734-82D9-BC1D067EA06E | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-28T15:57:09.9170000 | 2026-07-30T15:22:05.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XMES_Work_Order_Trn_Tbl.CampaignID` -> `XStudio_XBatch.XMES_Campaign_Plan_Mst.ID` (Many to One)
- `XStudio_XBatch.XMES_Work_Order_Trn_Tbl.WorkOrder` -> `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.ID` (Many to One)
