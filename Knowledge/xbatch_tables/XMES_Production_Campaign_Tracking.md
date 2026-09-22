# XStudio_Xbatch.dbo.XMES_Production_Campaign_Tracking

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference date, billet, order, pcs, production, abort, bundles, campaign, cancelled, charged, complete, completed.

**Primary Key:** ID  
**Row Count:** 125  
**Date Range (ModifiedOn):** 2026-06-25T16:07:20.3500000 to 2026-08-24T16:05:08.6130000  

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
| Work_Order | varchar | YES | 100 | — |
| Sales_Order | varchar | YES | 100 | — |
| Billet_Charged | varchar | YES | 100 | — |
| Billet_Rolled | varchar | YES | 100 | — |
| Quantity_Produce_MT | varchar | YES | 100 | — |
| Bundles | varchar | YES | 100 | — |
| Total_Pcs | varchar | YES | 100 | — |
| Remaining_Pcs | varchar | YES | 100 | — |
| PercentageComplete | varchar | YES | 100 | — |
| Status | varchar | YES | 100 | — |
| CampaignId | varchar | YES | 100 | — |
| ProductionStartDate | datetime | YES | — | — |
| ProductionEndDate | datetime | YES | — | — |
| ReleasedDate | datetime | YES | — | — |
| OnholdDate | datetime | YES | — | — |
| CancelledDate | datetime | YES | — | — |
| CompletedDate | datetime | YES | — | — |
| AbortDate | datetime | YES | — | — |
| RunningDate | datetime | YES | — | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 02A46BF7-74E3-41C1-803A-31CF734A51F4 | NULL | NULL | NULL | NULL | 2026-05-04T08:49:36.8600000 | NULL | False | False | NULL |
| 00B9A865-2492-4991-BF48-91419C713E71 | NULL | NULL | NULL | NULL | 2026-05-02T09:17:00.9130000 | NULL | False | False | NULL |
| 0092CD73-5F71-45EE-8FE3-7DB98A241944 | NULL | NULL | NULL | NULL | 2026-05-02T09:17:00.9400000 | NULL | False | False | NULL |
| 1DFDF8E4-CB5C-4E2A-964E-7BB1D2FADC8B | NULL | NULL | NULL | NULL | 2026-05-07T14:32:16.1900000 | NULL | False | False | NULL |
| 1D94FE08-5937-4C5C-8183-BCF0FC024056 | NULL | NULL | NULL | NULL | 2026-05-26T16:02:48.4330000 | NULL | False | False | NULL |
| 1BE7999F-BB9E-4908-A6AC-27839D46C8A1 | NULL | NULL | NULL | NULL | 2026-04-15T10:43:20.2170000 | NULL | False | False | NULL |
| 1748EE01-8471-4090-8375-4AFF942955D2 | NULL | NULL | NULL | NULL | 2026-05-27T09:19:31.5430000 | NULL | False | False | NULL |
| 15AFF618-17EE-4758-B8D4-DF722298230F | NULL | NULL | NULL | NULL | 2026-04-27T15:53:12.6700000 | NULL | False | False | NULL |
| 0FD7C6CF-4C25-4536-B9D8-8848173686CA | NULL | NULL | NULL | NULL | 2026-04-24T10:13:25.8900000 | NULL | False | False | NULL |
| 0B2D4149-E6B1-45AA-AB58-C57C37212ACB | NULL | NULL | NULL | NULL | 2026-05-26T15:10:54.3130000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F8EAE19F-A8F0-4590-8F70-0796A8A93E39 | NULL | NULL | NULL | NULL | 2026-08-21T15:50:37.4130000 | 2026-08-24T16:05:08.6130000 | False | False | NULL |
| F893106C-660E-4993-B40E-92CC59DC8144 | NULL | NULL | NULL | NULL | 2026-08-17T16:54:07.5730000 | 2026-08-21T15:53:20.3900000 | False | False | NULL |
| 61EAEE56-910C-4D67-9E74-35EB8ABA9BDC | NULL | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-28T15:01:08.1970000 | 2026-08-14T15:02:05.9730000 | True | False | NULL |
| 3DD3A37E-DB37-44D0-B619-7CEB4404583E | NULL | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-28T11:22:49.8500000 | 2026-08-14T15:02:03.7830000 | True | False | NULL |
| 510FAEB9-4ED1-4841-A031-F5C90A77C74F | NULL | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-28T11:15:59.6330000 | 2026-08-14T15:02:02.0130000 | True | False | NULL |
| AB56BD31-38DC-457C-AD6F-BCAC87EE958E | NULL | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-28T08:52:09.8500000 | 2026-08-14T15:02:00.1270000 | True | False | NULL |
| B03ACF88-F337-48E4-8938-20E581991FC3 | NULL | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-07-14T13:56:14.8270000 | 2026-08-14T15:01:57.9570000 | True | False | NULL |
| E2AC368F-4C25-4CB8-9A0F-FE18D33E24E5 | NULL | NULL | NULL | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2026-06-30T15:59:12.2870000 | 2026-08-14T15:01:55.6800000 | True | False | NULL |
| 8181C505-C2A6-4397-97DB-BAC5DD0448DC | NULL | NULL | NULL | NULL | 2026-07-28T15:02:08.1070000 | 2026-08-14T14:07:03.6270000 | False | False | NULL |
| 04591826-BB64-46F1-B280-58DEA611AB51 | NULL | NULL | NULL | NULL | 2026-05-07T13:24:12.3200000 | 2026-07-28T09:02:18.9900000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XMES_Production_Campaign_Tracking.CampaignId` -> `XStudio_XBatch.XMES_Campaign_Plan_Mst.ID` (Many to One)
- `XStudio_XBatch.XMES_Production_Campaign_Tracking.Work_Order` -> `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.ID` (Many to One)
