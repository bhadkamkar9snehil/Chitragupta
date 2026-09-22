# XStudio_Xbatch.dbo.RM_Sales_Order

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference qty, material, customer, date, grade, open, order, ponumber, release, rolling, size, status.

**Primary Key:** ID  
**Row Count:** 8  
**Date Range (ModifiedOn):** 2025-07-08T15:40:41.0000000 to 2025-07-10T09:10:36.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
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
| PONumber | varchar | YES | 100 | — |
| Customer | varchar | YES | 36 | — |
| Size | varchar | YES | 100 | — |
| RollingQty | int | YES | 10,0 | — |
| OpenQty | int | YES | 10,0 | — |
| ReleaseQty | int | YES | 10,0 | — |
| OrderDate | date | YES | — | — |
| Status | varchar | YES | 100 | — |
| MaterialGrade | varchar | YES | 36 | — |
| MaterialID | varchar | YES | 36 | — |
| Name | varchar | YES | 100 | — |

### Top 10 Records

| ID | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D1743814-24F9-42EB-8090-CDB5C894F3C3 | NULL | NULL | NULL | 2025-07-08T15:59:09.2000000 | NULL | False | False | NULL | NULL |
| 4E89CC89-68CA-47EC-8C93-677483450D0B | NULL | NULL | NULL | 2025-07-08T15:46:08.4570000 | NULL | False | False | NULL | NULL |
| 3A1A19D0-4559-4FE7-BFD3-72E2357E218A | NULL | NULL | NULL | 2025-07-08T15:59:09.2000000 | NULL | False | False | NULL | NULL |
| 25E0DF89-D0BC-48B4-93E5-D548779D8F09 | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-07-08T15:40:42.7800000 | 2025-07-08T15:40:41.0000000 | False | False | NULL |  |
| 5D3BAA2E-7C7F-4E87-A2C3-A2A917872060 | NULL | NULL | F349EDFC-5CC8-48D0-B73C-81BEB5517597 | 2025-07-08T15:59:09.2000000 | 2025-07-10T09:03:38.0000000 | False | False | NULL | 10.2.18.43 |
| 6969A442-BC56-46F8-BD0F-5AB7C947B311 | NULL | NULL | F349EDFC-5CC8-48D0-B73C-81BEB5517597 | 2025-07-08T15:59:09.2000000 | 2025-07-10T09:05:08.0000000 | False | False | NULL | 10.2.18.43 |
| 63D71CC5-FCF8-4AAC-A83F-F849BA5352AF | NULL | NULL | F349EDFC-5CC8-48D0-B73C-81BEB5517597 | 2025-07-08T15:59:09.2000000 | 2025-07-10T09:08:45.0000000 | False | False | NULL | 10.2.18.43 |
| 76A73EA7-5EDD-4FBF-85B2-19A577675727 | NULL | NULL | F349EDFC-5CC8-48D0-B73C-81BEB5517597 | 2025-07-08T15:59:09.2000000 | 2025-07-10T09:10:36.0000000 | False | False | NULL | 10.2.18.43 |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.RM_Sales_Order.Customer` -> `XStudio_XBatch.XBatch_Customer_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.RM_Sales_Order.MaterialGrade` -> `XStudio_XBatch.Steel_Grade_Master.ID` (Many to One)
- `XStudio_XBatch.RM_Sales_Order.MaterialID` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
