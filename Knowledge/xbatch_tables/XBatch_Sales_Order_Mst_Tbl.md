# XStudio_Xbatch.dbo.XBatch_Sales_Order_Mst_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference order, date, completion, actual, planned, start, approved, duration, execution, item, lead, progress.

**Primary Key:** ID  
**Row Count:** 55  
**Date Range (ModifiedOn):** 2025-12-16T09:59:50.0000000 to 2026-01-30T11:07:55.6300000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 100 | — |
| ParentID | varchar | NO | 36 | — |
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
| ItemID | varchar | NO | 36 | — |
| Quantity | decimal | NO | 18,4 | — |
| UnitID | varchar | NO | 36 | — |
| ReleasedDate | datetime | YES | — | — |
| ApprovedDate | datetime | YES | — | — |
| ApprovedBy | varchar | YES | 36 | — |
| PlannedCompletionDate | datetime | YES | — | — |
| Remarks | varchar | YES | 1000 | — |
| SalesOrderNumber | varchar | NO | 100 | — |
| ColourCode | varchar | YES | 50 | — |
| Status | varchar | YES | 50 | — |
| ProgressTonnage | decimal | YES | 18,4 | — |
| ProgressPercentage | decimal | YES | 18,4 | — |
| RemainingTonnage | decimal | YES | 18,4 | — |
| ActualCompletionDate | datetime | YES | — | — |
| PlannedStartDate | datetime | YES | — | — |
| RequiredCompletionDate | datetime | YES | — | — |
| ActualStartDate | datetime | YES | — | — |
| OrderCompletionVariance | int | YES | 10,0 | — |
| OrderStartVariance | int | YES | 10,0 | — |
| ActualOrderCompletionSlack | int | YES | 10,0 | — |
| PlannedOrderCompletionSlack | int | YES | 10,0 | — |
| ActualOrderStartLeadTime | int | YES | 10,0 | — |
| ActualOrderExecutionDuration | int | YES | 10,0 | — |
| PlannedOrderExecutionDuration | int | YES | 10,0 | — |
| PlannedOrderStartLeadTime | int | YES | 10,0 | — |
| Grade | varchar | YES | 100 | — |
| SalesOrderItem | varchar | YES | 100 | — |
| Area | varchar | YES | 100 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 38F47754-11A2-4C65-8DEE-B0DFA32813BD | 239201887 | A7C53019-EBB7-4895-B6A3-37A18EC0F4C6 | NULL | NULL | 2026-04-24T09:42:35.1070000 | NULL | False | False | NULL |
| 37DB7E4D-57A8-4412-8BBA-D1C9D1EAE872 | 539200328 | 36351507-3690-4086-AA7D-32B809BD0DB0 | NULL | NULL | 2026-04-24T10:52:54.4530000 | NULL | False | False | NULL |
| 2118A5B3-6CC4-4B4E-855B-7D2B2A4CB9D3 | 539200326 | AF2D2633-07FF-4B54-A5DB-1C9CFEF8B9F4 | NULL | NULL | 2026-04-24T10:52:54.4530000 | NULL | False | False | NULL |
| 1D1DE97E-3077-4C60-A01B-4F1322A2094C | 239201935 | B98BF895-A7E8-4916-8403-C7CFF3A252E0 | NULL | NULL | 2026-04-24T09:42:35.1070000 | NULL | False | False | NULL |
| 192106B1-07C0-4418-8EB4-7364805D4B62 | 239202052 | 47792BAE-85E9-4B9F-A85E-2B1979713777 | NULL | NULL | 2026-08-21T15:52:07.2470000 | NULL | False | False | NULL |
| 16F728A5-ECA5-434F-AEB0-1B2E0012DEFE | 239202040 | 97F4D386-2D80-4AE1-950B-2F4C95DA9E52 | NULL | NULL | 2026-08-21T15:52:07.2470000 | NULL | False | False | NULL |
| 0A4EB8B5-578D-4443-9B3B-8FDD1E2B3877 | 539200321 | 76679563-B889-436E-94C0-8016DBD0561D | NULL | NULL | 2026-04-24T10:52:54.4530000 | NULL | False | False | NULL |
| 0875D66C-DC08-4A40-8679-DE3F1E008889 | 239201924 | 47792BAE-85E9-4B9F-A85E-2B1979713777 | NULL | NULL | 2026-04-24T09:42:35.1070000 | NULL | False | False | NULL |
| 0232281B-6726-48A6-AD8D-315A546F394D | 239202032 | 83B4BFB7-75F3-41AA-956B-BFABAC620117 | NULL | NULL | 2026-08-21T15:52:07.2470000 | NULL | False | False | NULL |
| 02198591-2452-49AB-A0F1-8A25DDD79686 | 239201928 | 21B95B53-5F3B-4BCC-911F-F09AE3089D72 | NULL | NULL | 2026-04-24T09:42:35.1070000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CC2A6D03-79B8-42A5-B587-FB9F19F33A71 | 123456 | C2D3E8B6-E5E4-4E49-9AAB-7CFD410615D3 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 1C3872A0-943B-48EE-8A8B-AC75D8925A9D | 2025-12-24T08:01:18.8500000 | 2026-01-30T11:07:55.6300000 | False | False | NULL |
| 60CDCFE1-23C4-47A4-9EED-34141D3B932E | 0115000011 | C2D3E8B6-E5E4-4E49-9AAB-7CFD410615D3 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2026-01-05T09:47:31.6470000 | 2026-01-05T09:47:57.5100000 | False | False | NULL |
| DA551AF3-7C4C-4CCF-8859-017E7BE8F1C7 | 0115000010 | C2D3E8B6-E5E4-4E49-9AAB-7CFD410615D3 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-12-27T10:37:16.6000000 | 2026-01-03T10:13:13.1930000 | False | False | NULL |
| 3943C5D5-A718-4DAF-8848-DA21B3178F8D | 1200003002 | EB305508-C3B7-4655-AED2-F89F2C38F8A3 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-12-16T11:13:30.8570000 | 2025-12-25T08:55:15.0000000 | False | False | NULL |
| C761987F-CDAD-497C-A2CF-CF16C191FF14 | MES_2025122217 | C2D3E8B6-E5E4-4E49-9AAB-7CFD410615D3 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-12-22T17:29:26.0670000 | 2025-12-24T14:06:46.8930000 | False | False | NULL |
| 86E07938-2AD8-461C-8A0A-4717ED7FD014 | MES_2025122216 | C2D3E8B6-E5E4-4E49-9AAB-7CFD410615D3 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-12-22T16:59:45.6000000 | 2025-12-22T17:14:08.9070000 | False | False | NULL |
| 400AA428-1976-4F69-8CDB-7381799D483D | 1200003001 | 51BC474F-259E-41BF-A973-2A7898272D97 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-12-15T17:35:36.2400000 | 2025-12-22T16:25:39.6470000 | False | False | NULL |
| AF2D7661-D600-4A03-B1CE-5C55E9C3D3D0 | 7000015001 | C2D3E8B6-E5E4-4E49-9AAB-7CFD410615D3 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-12-15T17:15:29.1470000 | 2025-12-16T10:00:02.0000000 | False | False | NULL |
| B473F200-8AFC-40DE-9495-FF9D41BE0696 | 7000015002 | C2D3E8B6-E5E4-4E49-9AAB-7CFD410615D3 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-12-15T17:35:03.0630000 | 2025-12-16T09:59:50.0000000 | False | False | NULL |
| 38F47754-11A2-4C65-8DEE-B0DFA32813BD | 239201887 | A7C53019-EBB7-4895-B6A3-37A18EC0F4C6 | NULL | NULL | 2026-04-24T09:42:35.1070000 | NULL | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.CCM_Per_Heat.SalesOrder` -> `XStudio_XBatch.XBatch_Sales_Order_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.MES_Raw_Material_Consumptions_Trn_Tbl.SalesOrder` -> `XStudio_XBatch.XBatch_Sales_Order_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Sales_Order_Mst_Tbl.ApprovedBy` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Sales_Order_Mst_Tbl.Grade` -> `XStudio_XBatch.Grade_Master.GradeName` (Many to One)
- `XStudio_XBatch.XBatch_Sales_Order_Mst_Tbl.ItemID` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Sales_Order_Mst_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Customer_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Sales_Order_Mst_Tbl.Status` -> `XStudio_XBatch.XBatch_Status_Mst_Tbl.Name` (Many to One)
- `XStudio_XBatch.XBatch_Sales_Order_Mst_Tbl.UnitID` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.SalesOrder` -> `XStudio_XBatch.XBatch_Sales_Order_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.SalesOrderItem` -> `XStudio_XBatch.XBatch_Sales_Order_Mst_Tbl.ItemID` (Many to One)
- `XStudio_XBatch.XMES_RM_Campaign_Plan_Trn.SONumber` -> `XStudio_XBatch.XBatch_Sales_Order_Mst_Tbl.SalesOrderNumber` (Many to One)
