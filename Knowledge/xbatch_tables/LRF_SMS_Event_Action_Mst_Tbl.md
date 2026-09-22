# XStudio_Xbatch.dbo.LRF_SMS_Event_Action_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference state, action, active, configuration, mode, type.

**Primary Key:** ID  
**Row Count:** 9  
**Date Range (ModifiedOn):** 2025-07-22T13:10:35.0000000 to 2025-09-10T21:28:03.0000000  

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
| StateID | varchar | YES | 36 | — |
| Configuration | varchar | YES | -1 | — |
| ActionType | varchar | YES | 100 | — |
| StateMode | varchar | YES | 100 | — |
| IsActive | bit | YES | — | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 342B0C40-CB6F-4AD6-92DD-C4C9775BF635 | LRFData | 3A4A0C4A-249A-4772-A956-38A6FC8699DF | 3ADE6546-3C9A-49C4-A001-234025F2F901 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-06-17T16:30:46.0000000 | 2025-07-22T13:10:35.0000000 | False | False | NULL |
| 33904A68-5470-47C6-A9B0-3A3C730A26BE | LRFStart | 3A4A0C4A-249A-4772-A956-38A6FC8699DF | 3ADE6546-3C9A-49C4-A001-234025F2F901 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-09-24T10:15:56.0000000 | 2025-07-22T13:47:14.0000000 | False | False | NULL |
| C9FB1978-C5B2-4FC1-807B-EF8D1D719819 | Ladle Car at LRF | 5964F6BE-5076-4101-BFDA-3434DA53DE8D | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-08-19T13:12:50.0700000 | 2025-08-19T13:12:50.0000000 | False | False | NULL |
| 327613B3-CC4C-42F2-B216-01F22CA7B1CC | LRF Process Start | 5964F6BE-5076-4101-BFDA-3434DA53DE8D | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-08-19T13:13:20.7630000 | 2025-08-19T13:13:20.0000000 | False | False | NULL |
| 3EE668BA-8262-425B-AE88-1C7002DA9D08 | Arcing Start | 5964F6BE-5076-4101-BFDA-3434DA53DE8D | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-08-19T13:13:55.7700000 | 2025-08-19T13:13:55.0000000 | False | False | NULL |
| 8FFAAAB5-BF72-460F-8507-B517F8882FF2 | LRF Process End | 5964F6BE-5076-4101-BFDA-3434DA53DE8D | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-08-19T13:14:28.1200000 | 2025-08-19T13:14:28.0000000 | False | False | NULL |
| 6E25913B-2987-490E-929B-1521267BF6F2 | Ladle Move From LRF To CCM | 5964F6BE-5076-4101-BFDA-3434DA53DE8D | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-09-08T21:06:17.0000000 | 2025-09-08T20:35:02.0000000 | False | False | NULL |
| 303227CF-2EA3-446B-972C-6D0D95F1AC65 | Ladle Move From LRF To CCM | 5964F6BE-5076-4101-BFDA-3434DA53DE8D | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-09-08T21:11:23.0000000 | 2025-09-08T20:36:20.0000000 | False | False | NULL |
| 27E41045-CEDD-4197-A429-D1D17B29AC61 | Treatment Start | 5964F6BE-5076-4101-BFDA-3434DA53DE8D | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-09-10T21:28:03.9700000 | 2025-09-10T21:28:03.0000000 | False | False | NULL |

---
