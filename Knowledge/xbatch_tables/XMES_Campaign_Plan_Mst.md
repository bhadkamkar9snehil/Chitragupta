# XStudio_Xbatch.dbo.XMES_Campaign_Plan_Mst

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference billets, date, status, total, upload, billet, bundles, campaign, discharged, end, max, min.

**Primary Key:** ID  
**Row Count:** 5  
**Date Range (ModifiedOn):** 2026-08-14T15:01:07.0270000 to 2026-08-24T16:05:08.6470000  

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
| Working | varchar | YES | 100 | — |
| Material | varchar | YES | 100 | — |
| Size | decimal | YES | 10,2 | — |
| Grade | varchar | YES | 100 | — |
| TotalQtyWt | decimal | YES | 18,4 | — |
| TotalPieces | int | YES | 10,0 | — |
| Status | varchar | YES | 50 | — |
| CampaignId | varchar | YES | 100 | — |
| Length | varchar | YES | 100 | — |
| StartDate | date | YES | — | — |
| EntryDateTime | datetime | YES | — | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| MinQtytoRollMT | decimal | YES | 18,4 | — |
| MaxQtytoRollMT | decimal | YES | 18,4 | — |
| MinNoOfBundles | decimal | YES | 18,4 | — |
| MaxNoOfBundles | decimal | YES | 18,4 | — |
| Action | varchar | YES | 50 | — |
| AllFilesUpload | varchar | YES | 8000 | — |
| EndDate | date | YES | — | — |
| UploadStatus | varchar | YES | 50 | — |
| Productname | varchar | YES | 36 | — |
| ProgressTonnage | decimal | YES | 18,4 | — |
| ProgressPercentage | decimal | YES | 18,4 | — |
| RemaningTonnage | decimal | YES | 18,4 | — |
| CampaignstartDate | date | YES | — | — |
| CampaignEndDate | date | YES | — | — |
| WRMExcelUpload | varchar | YES | 8000 | — |
| WRMStatus | varchar | YES | 50 | — |
| WRMUploadStatus | varchar | YES | 50 | — |
| BilletsRolled | int | YES | 10,0 | — |
| BilletsCobble | int | YES | 10,0 | — |
| BilletsHotout | int | YES | 10,0 | — |
| BilletDischarged | int | YES | 10,0 | — |
| BilletsRemaining | int | YES | 10,0 | — |
| TotalBillets | int | YES | 10,0 | — |
| BilletDischargedWeight | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0965F8E3-E3DB-44B8-8732-61F562CCFBC0 | NULL | NULL | 19F651E7-FC5E-4A24-8D95-48F5FE661683 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2026-07-28T15:02:00.8370000 | 2026-08-14T15:01:07.0270000 | False | False | NULL |
| 5EBEC3BE-19E6-44ED-9076-873432900F5B | NULL | NULL | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 2026-08-21T09:32:30.8570000 | 2026-08-21T09:41:12.5400000 | False | False | NULL |
| 7BA3E8D6-E60C-4535-807A-5054633BE6C0 | NULL | NULL | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 2026-08-21T09:33:24.5170000 | 2026-08-21T09:41:14.9570000 | False | False | NULL |
| E75E0F96-273C-4C95-B650-D24E5B3DB6E6 | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2026-08-17T16:54:00.9830000 | 2026-08-21T15:53:20.3870000 | False | False | NULL |
| C3EB832C-E44D-4178-97CB-148B02262E15 | NULL | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2026-08-21T15:50:25.6300000 | 2026-08-24T16:05:08.6470000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.RM_Operator_HeatSelection.CampaignId` -> `XStudio_XBatch.XMES_Campaign_Plan_Mst.ID` (Many to One)
- `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.CampaignId` -> `XStudio_XBatch.XMES_Campaign_Plan_Mst.ID` (Many to One)
- `XStudio_XBatch.XMES_Campaign_Plan_Mst.ID` -> `XStudio_XBatch.XMES_RM_Campaign_Plan_Trn.ParentID` (One to Many)
- `XStudio_XBatch.XMES_Campaign_Plan_Mst.Productname` -> `XStudio_XBatch.Product_Master.ID` (Many to One)
- `XStudio_XBatch.XMES_Production_Campaign_Tracking.CampaignId` -> `XStudio_XBatch.XMES_Campaign_Plan_Mst.ID` (Many to One)
- `XStudio_XBatch.XMES_RM_Campaign_Plan_Trn.ParentID` -> `XStudio_XBatch.XMES_Campaign_Plan_Mst.ID` (Many to One)
- `XStudio_XBatch.XMES_RM_Heated_Billet_trn_tbl.Campaignid` -> `XStudio_XBatch.XMES_Campaign_Plan_Mst.ID` (Many to One)
- `XStudio_XBatch.XMES_RM_Tag_Printing_TRN.Campaignid` -> `XStudio_XBatch.XMES_Campaign_Plan_Mst.ID` (Many to One)
- `XStudio_XBatch.XMES_Work_Order_Trn_Tbl.CampaignID` -> `XStudio_XBatch.XMES_Campaign_Plan_Mst.ID` (Many to One)
