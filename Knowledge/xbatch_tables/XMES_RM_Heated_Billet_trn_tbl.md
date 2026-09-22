# XStudio_Xbatch.dbo.XMES_RM_Heated_Billet_trn_tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference billet, campaignid, heat, product, type, workorderid.

**Primary Key:** ID  
**Row Count:** 2,100  

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
| BilletNo | varchar | YES | 100 | — |
| HeatNO | varchar | YES | 100 | — |
| campaignid | varchar | YES | 36 | — |
| Workorderid | varchar | YES | 36 | — |
| ProductType | varchar | YES | 36 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01185B55-C052-451C-9F6E-156F788AEDF4 | NULL | NULL | NULL | NULL | 2026-08-19T19:37:17.4930000 | NULL | False | False | NULL |
| 010BE6AA-55A4-4E47-A7D0-B12C6D763ED2 | NULL | NULL | NULL | NULL | 2026-08-07T18:24:25.3300000 | NULL | False | False | NULL |
| 0100DC68-14DB-4E12-846B-631F6E7834B5 | NULL | 3211ECF6-D5AB-4949-A017-5F343E3A5872 | NULL | NULL | 2026-07-31T11:15:51.7000000 | NULL | False | False | NULL |
| 00FFC933-7B0F-4131-9585-709EA543EE7D | NULL | NULL | NULL | NULL | 2026-08-18T18:32:19.2870000 | NULL | False | False | NULL |
| 00FAC1DE-2C61-4B62-A753-9F9B9D9CB02B | NULL | NULL | NULL | NULL | 2026-07-14T10:18:45.6870000 | NULL | False | False | NULL |
| 00FA33CA-C5D3-45E2-BB2F-00AB6DDBAD5F | NULL | NULL | NULL | NULL | 2026-07-14T16:26:38.2900000 | NULL | False | False | NULL |
| 00D2789C-D658-484B-9ADD-05BB9EE038D3 | NULL | D83C68D3-CAA3-41BC-BC73-84D7E8CF2B58 | NULL | NULL | 2026-07-30T19:16:11.7430000 | NULL | False | False | NULL |
| 00B40EF5-DD4A-498A-912F-83AB6DE448D9 | NULL | 0453B15F-C174-4A03-83BE-E1CE09FE54F5 | NULL | NULL | 2026-07-30T18:01:08.9400000 | NULL | False | False | NULL |
| 00904D77-9817-404C-B928-22197586C147 | NULL | NULL | NULL | NULL | 2026-08-17T20:40:00.6800000 | NULL | False | False | NULL |
| 00699DFB-A897-4D5B-81DA-7EA74DDC94C6 | NULL | NULL | NULL | NULL | 2026-08-18T18:20:47.4400000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01185B55-C052-451C-9F6E-156F788AEDF4 | NULL | NULL | NULL | NULL | 2026-08-19T19:37:17.4930000 | NULL | False | False | NULL |
| 010BE6AA-55A4-4E47-A7D0-B12C6D763ED2 | NULL | NULL | NULL | NULL | 2026-08-07T18:24:25.3300000 | NULL | False | False | NULL |
| 0100DC68-14DB-4E12-846B-631F6E7834B5 | NULL | 3211ECF6-D5AB-4949-A017-5F343E3A5872 | NULL | NULL | 2026-07-31T11:15:51.7000000 | NULL | False | False | NULL |
| 00FFC933-7B0F-4131-9585-709EA543EE7D | NULL | NULL | NULL | NULL | 2026-08-18T18:32:19.2870000 | NULL | False | False | NULL |
| 00FAC1DE-2C61-4B62-A753-9F9B9D9CB02B | NULL | NULL | NULL | NULL | 2026-07-14T10:18:45.6870000 | NULL | False | False | NULL |
| 00FA33CA-C5D3-45E2-BB2F-00AB6DDBAD5F | NULL | NULL | NULL | NULL | 2026-07-14T16:26:38.2900000 | NULL | False | False | NULL |
| 00D2789C-D658-484B-9ADD-05BB9EE038D3 | NULL | D83C68D3-CAA3-41BC-BC73-84D7E8CF2B58 | NULL | NULL | 2026-07-30T19:16:11.7430000 | NULL | False | False | NULL |
| 00B40EF5-DD4A-498A-912F-83AB6DE448D9 | NULL | 0453B15F-C174-4A03-83BE-E1CE09FE54F5 | NULL | NULL | 2026-07-30T18:01:08.9400000 | NULL | False | False | NULL |
| 00904D77-9817-404C-B928-22197586C147 | NULL | NULL | NULL | NULL | 2026-08-17T20:40:00.6800000 | NULL | False | False | NULL |
| 00699DFB-A897-4D5B-81DA-7EA74DDC94C6 | NULL | NULL | NULL | NULL | 2026-08-18T18:20:47.4400000 | NULL | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XMES_RM_Heated_Billet_trn_tbl.Campaignid` -> `XStudio_XBatch.XMES_Campaign_Plan_Mst.ID` (Many to One)
- `XStudio_XBatch.XMES_RM_Heated_Billet_trn_tbl.ProductType` -> `XStudio_XBatch.Product_Master.ID` (Many to One)
- `XStudio_XBatch.XMES_RM_Heated_Billet_trn_tbl.Workorderid` -> `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.ID` (Many to One)
