# XStudio_Xbatch.dbo.RM_Operator_HeatSelection

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** catalog, entities, entity, from, highlights, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference billet, batch, bed, furnace, length, status, billetoutof, billets, campaign, charging, date, external.

**Primary Key:** ID  
**Row Count:** 73  
**Date Range (ModifiedOn):** 2026-07-30T12:57:52.4900000 to 2026-08-27T13:50:30.5970000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Heatno | varchar | NO | 36 | — |
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
| BilletQty | int | YES | 10,0 | — |
| Grade | varchar | YES | 100 | — |
| BilletLength | varchar | YES | 100 | — |
| Remainingbilletincharging | int | YES | 10,0 | — |
| Srno | int | YES | 10,0 | — |
| CampaignId | varchar | YES | 36 | — |
| workorder | varchar | YES | 36 | — |
| length | decimal | YES | 18,4 | — |
| BedNo | varchar | YES | 36 | — |
| Status | varchar | YES | 100 | ('Entered') |
| ReleaseDate | datetime | YES | — | — |
| TotalBillet | int | YES | 10,0 | — |
| BilletOnChargingBed | int | YES | 10,0 | — |
| Released | varchar | YES | 50 | ('Entered') |
| Batch | varchar | YES | 100 | — |
| BilletMaterialType | varchar | YES | 100 | — |
| BatchWeight | decimal | YES | 18,2 | — |
| BilletsFuranaceStatus | varchar | YES | 100 | — |
| BilletoutofFurnace | int | YES | 10,0 | — |
| BilletOnFurnace | int | YES | 10,0 | — |
| IsExternalBillet | bit | YES | — | — |

### Top 10 Records

| ID | Heatno | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 472BB1FB-F65A-41EC-8F12-D201B4A5D941 | 1603166 | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-30T12:57:41.4300000 | 2026-07-30T12:57:52.4900000 | False | False | NULL |
| EC0C03C2-EA03-43E2-ACE5-E34C0671FA7F | 1603168 | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-30T13:43:33.7000000 | 2026-07-30T13:43:38.7530000 | False | False | NULL |
| A465A190-EF62-4C8E-979C-2322FFAD0F87 | 1603333 | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-30T13:44:23.4200000 | 2026-07-30T13:44:28.2770000 | False | False | NULL |
| 82D4AC06-3045-430E-8A71-FE88824A7537 | 1603337 | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-30T14:06:22.5170000 | 2026-07-30T14:47:25.6330000 | False | False | NULL |
| 0A5FE6DE-76B3-4EE0-AD5A-7AD59F9572DE | 1604000 | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-30T16:07:22.0030000 | 2026-07-30T16:07:33.0900000 | False | False | NULL |
| D3FE003B-2014-4CB8-BD6F-CA7F58CEE41E | 1604001 | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-30T16:09:13.9700000 | 2026-07-30T16:09:17.7830000 | False | False | NULL |
| AD0A329C-0BB0-46D2-888F-5E2D2FB2E028 | 1604002 | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-30T17:15:34.6700000 | 2026-07-30T17:15:41.3900000 | False | False | NULL |
| AB06BD5D-FBB9-4FAC-AFC9-A1C7085DE05C | 1604003 | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-30T17:16:10.2630000 | 2026-07-30T17:16:14.2600000 | False | False | NULL |
| C783B4B8-BA07-4BD3-AAA1-A3626477ABA3 | 1604005 | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-30T17:16:38.6230000 | 2026-07-30T17:17:07.5770000 | False | False | NULL |
| 6E0F61E2-93CC-46B4-9A38-4030DF2975B6 | 1604006 | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-30T17:16:50.8070000 | 2026-07-30T17:17:09.8200000 | False | False | NULL |

### Bottom 10 Records

| ID | Heatno | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A427F348-BF0C-42ED-A2F8-913C4D440200 | 2605979 | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-08-27T13:50:26.1800000 | 2026-08-27T13:50:30.5970000 | False | False | NULL |
| 209956AD-E358-4F3E-9AD7-66B213C53DFC | 2605971 | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-08-27T13:49:15.1000000 | 2026-08-27T13:49:18.8230000 | False | False | NULL |
| 3DE01A46-1E9F-42AE-A3BE-B2229479E6BE | 2603935 | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-08-27T13:48:24.3500000 | 2026-08-27T13:48:30.1970000 | False | False | NULL |
| 9DE2D5C9-4B7C-4B05-B4E9-9A77F8C725D8 | 2603931 | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-08-27T13:47:09.9200000 | 2026-08-27T13:47:14.9230000 | False | False | NULL |
| E3194CF3-5CAC-48B8-8846-32F798C2A4EE | 1260781 | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-08-25T14:28:55.4830000 | 2026-08-25T14:28:59.6570000 | False | False | NULL |
| B44EAB30-A0C0-43B8-9032-2CC826DA1978 | 1260773 | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-08-25T13:40:33.3400000 | 2026-08-25T13:40:37.1600000 | False | False | NULL |
| 9418E30A-86F5-4CF0-8B27-22B36272A133 | 1260817 | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2026-08-25T13:04:26.1600000 | 2026-08-25T13:04:29.7270000 | False | False | NULL |
| 29F85326-B938-4A40-BEC0-A6045A0667DB | 1260817 | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2026-08-24T16:02:48.7130000 | 2026-08-24T16:02:52.2370000 | False | False | NULL |
| 413AA2AE-A378-46FE-896B-116FEE66A60C | 2605978 | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2026-08-24T09:08:40.5170000 | 2026-08-24T12:48:14.2400000 | False | False | NULL |
| 8F10486A-5D04-487D-A9A6-3602C4550A39 | 2605977 | NULL | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2026-08-24T09:08:16.6930000 | 2026-08-24T09:08:21.1470000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.RM_Operator_HeatSelection.CampaignId` -> `XStudio_XBatch.XMES_Campaign_Plan_Mst.ID` (Many to One)
- `XStudio_XBatch.RM_Operator_HeatSelection.length` -> `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.Length` (Many to Many)
- `XStudio_XBatch.RM_Operator_HeatSelection.workorder` -> `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XMES_Live_Billet_Charging_Bed.ParentID` -> `XStudio_XBatch.RM_Operator_HeatSelection.ID` (Many to One)
