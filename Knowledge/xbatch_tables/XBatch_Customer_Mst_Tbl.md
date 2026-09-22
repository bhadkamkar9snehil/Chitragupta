# XStudio_Xbatch.dbo.XBatch_Customer_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference address, code, contact, email, number, city, county, customer, description, state, zip.

**Primary Key:** ID  
**Row Count:** 52  
**Date Range (ModifiedOn):** 2025-07-03T17:22:29.0000000 to 2026-04-23T15:51:38.0000000  

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
| Address | varchar | YES | 1000 | — |
| City | varchar | YES | 100 | — |
| State | varchar | YES | 100 | — |
| County | varchar | YES | 100 | — |
| ZipCode | int | YES | 10,0 | — |
| ContactNumber1 | varchar | YES | 100 | — |
| ContactNumber2 | varchar | YES | 100 | — |
| EmailAddress1 | varchar | YES | 200 | — |
| EmailAddress2 | varchar | YES | 200 | — |
| Description | varchar | YES | 1000 | — |
| CustomerCode | varchar | YES | 100 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 21B95B53-5F3B-4BCC-911F-F09AE3089D72 | UTMOST Steel Manufacturing LLC | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | NULL | 2026-04-08T14:05:53.4830000 | NULL | False | False | NULL |
| 1F7CEB73-EB6C-4FED-BCBC-81C8F2E30682 | Utmost Building Materials LLC | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | NULL | 2026-04-08T14:05:53.4830000 | NULL | False | False | NULL |
| 47792BAE-85E9-4B9F-A85E-2B1979713777 | GBMT STRUCTURAL STEEL MANUFACTURING | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | NULL | 2026-04-08T14:05:53.4830000 | NULL | False | False | NULL |
| 36351507-3690-4086-AA7D-32B809BD0DB0 | Samrat wires & Metal Production LLC | NULL | NULL | NULL | 2026-04-24T10:52:54.4200000 | NULL | False | False | NULL |
| 34F1C745-7FC6-44A9-B879-DB4D87725823 | Chainlink Fencing Co LLC | NULL | NULL | NULL | 2026-04-24T10:52:54.4200000 | NULL | False | False | NULL |
| 2C4C32F6-B405-4DBF-B3EE-85377F6ABDC1 | MADAR EMIRATES FOR BUILDING MATERIALS | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | NULL | 2026-04-08T14:05:53.4830000 | NULL | False | False | NULL |
| 4A06DE66-62E9-48FE-9116-9956F1AB77E9 | AL JESSOUR BULDING MATERIALS TRADING LLC | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | NULL | 2026-04-08T14:05:53.4830000 | NULL | False | False | NULL |
| 51A88216-F06C-4A74-84D5-3CB05165A67C | Macsteel international Ltd (DMCC Branch) | NULL | NULL | NULL | 2026-04-24T10:52:54.4200000 | NULL | False | False | NULL |
| 525FC91A-4EC2-482D-9567-603AA96E8B61 | ARABIC STEEL INDUSTRY AND TRADING | NULL | NULL | NULL | 2026-04-24T10:52:54.4200000 | NULL | False | False | NULL |
| 54A18CC9-1F01-40E4-A919-6B04E3A5496C | Ghantoot Building Materials | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | NULL | 2026-04-08T14:05:53.4830000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DEE88D46-6B55-4F21-8D72-D004315DD3BD | UAE & Oman Customers | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-04-23T15:51:38.4600000 | 2026-04-23T15:51:38.0000000 | False | False | NULL |
| C2D3E8B6-E5E4-4E49-9AAB-7CFD410615D3 | SOHAR STEEL LLC | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 1C3872A0-943B-48EE-8A8B-AC75D8925A9D | 2025-12-15T17:10:35.7730000 | 2026-02-05T14:46:09.0000000 | False | False | NULL |
| AF2D2633-07FF-4B54-A5DB-1C9CFEF8B9F4 | Emirates Rebar Ltd | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-07-08T15:39:57.6970000 | 2025-07-08T15:39:56.0000000 | False | False | NULL |
| A19AF807-E8B8-4336-8604-4E63551A0BCE | BISHAH STEEL INDUSTRIES L.L.C | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-07-08T15:39:43.2870000 | 2025-07-08T15:39:42.0000000 | False | False | NULL |
| A7C53019-EBB7-4895-B6A3-37A18EC0F4C6 | Geap International (U.A.E.) LLC | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-07-08T15:39:34.6000000 | 2025-07-08T15:39:33.0000000 | False | False | NULL |
| 477DAA49-A568-4CFC-A4FA-EBA970D3E58E | BRC Arabia LLC | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-07-08T15:39:25.2630000 | 2025-07-08T15:39:24.0000000 | False | False | NULL |
| B98BF895-A7E8-4916-8403-C7CFF3A252E0 | UNION REBAR FACTORY LLC | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-07-08T15:39:16.3230000 | 2025-07-08T15:39:15.0000000 | False | False | NULL |
| 97F4D386-2D80-4AE1-950B-2F4C95DA9E52 | Dubar Metal Grating Manufacturing LLC | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-07-08T15:39:05.8400000 | 2025-07-08T15:39:04.0000000 | False | False | NULL |
| A8BA6B4A-FFB5-4E89-9BA3-AB6CB8159796 | Cicon Building Materials LLC | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-07-08T15:38:57.8270000 | 2025-07-08T15:38:56.0000000 | False | False | NULL |
| 76679563-B889-436E-94C0-8016DBD0561D | B.R.C. Weldmesh (Gulf) W.L.L | NULL | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 7F85C93F-ECB5-4C7D-91C6-C854A580014E | 2025-07-08T15:38:39.6670000 | 2025-07-08T15:38:38.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.RM_Rolling_Plan.Customer` -> `XStudio_XBatch.XBatch_Customer_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.RM_Sales_Order.Customer` -> `XStudio_XBatch.XBatch_Customer_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Sales_Order_Mst_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Customer_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XMES_RM_Campaign_Plan_Trn.Customer` -> `XStudio_XBatch.XBatch_Customer_Mst_Tbl.Name` (Many to One)
