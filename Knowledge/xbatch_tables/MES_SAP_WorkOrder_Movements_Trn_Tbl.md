# XStudio_Xbatch.dbo.MES_SAP_WorkOrder_Movements_Trn_Tbl

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** errors, execution, integration, order, posting, sap, work (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference batch, count, creditindication, date, debit, document, item, location, material, movement, posting, quantity.

**Primary Key:** ID  
**Row Count:** 6,07,884  

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
| PostingDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| MaterialDocument | varchar | YES | 100 | — |
| MovementType | int | YES | 10,0 | — |
| Batch | varchar | YES | 100 | — |
| StorageLocation | int | YES | 10,0 | — |
| DebitCreditindication | varchar | YES | 100 | — |
| Quantity | decimal | YES | 18,4 | — |
| NoOfItem | int | YES | 10,0 | — |
| QuantityinCount | int | YES | 10,0 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0000D893-A9D0-407C-B04C-3AECAEACDE09 | NULL | NULL | NULL | NULL | 2026-02-22T12:11:30.3600000 | NULL | False | False | NULL |
| 0000ACBE-7166-4ACB-8E3D-91FA67A5705C | NULL | NULL | NULL | NULL | 2026-02-23T04:51:10.4370000 | NULL | False | False | NULL |
| 0000849A-21F4-4C4E-9FCE-61691D354944 | NULL | NULL | NULL | NULL | 2026-02-22T23:20:09.5700000 | NULL | False | False | NULL |
| 00007FBD-7D6F-45DD-A93E-F81A4E7D2510 | NULL | NULL | NULL | NULL | 2026-02-24T14:02:08.6930000 | NULL | False | False | NULL |
| 000071D2-8805-42BC-8D5B-A8B877DCB224 | NULL | NULL | NULL | NULL | 2026-02-25T16:48:00.5400000 | NULL | False | False | NULL |
| 000068FB-8E51-4A2D-9F75-42000761919D | NULL | NULL | NULL | NULL | 2026-02-22T09:52:37.5270000 | NULL | False | False | NULL |
| 00004DB9-B575-482B-896C-98A45B2C6FB8 | NULL | NULL | NULL | NULL | 2026-02-26T08:24:40.4700000 | NULL | False | False | NULL |
| 00004695-5E14-463D-A668-241E74547FD5 | NULL | NULL | NULL | NULL | 2026-02-23T03:21:02.2600000 | NULL | False | False | NULL |
| 000045CF-5E77-41D0-9234-15D5F683C41F | NULL | NULL | NULL | NULL | 2026-03-05T16:12:24.9830000 | NULL | False | False | NULL |
| 00003863-BC27-4824-8348-052739564A5D | NULL | NULL | NULL | NULL | 2026-02-23T02:33:22.0930000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0000D893-A9D0-407C-B04C-3AECAEACDE09 | NULL | NULL | NULL | NULL | 2026-02-22T12:11:30.3600000 | NULL | False | False | NULL |
| 0000ACBE-7166-4ACB-8E3D-91FA67A5705C | NULL | NULL | NULL | NULL | 2026-02-23T04:51:10.4370000 | NULL | False | False | NULL |
| 0000849A-21F4-4C4E-9FCE-61691D354944 | NULL | NULL | NULL | NULL | 2026-02-22T23:20:09.5700000 | NULL | False | False | NULL |
| 00007FBD-7D6F-45DD-A93E-F81A4E7D2510 | NULL | NULL | NULL | NULL | 2026-02-24T14:02:08.6930000 | NULL | False | False | NULL |
| 000071D2-8805-42BC-8D5B-A8B877DCB224 | NULL | NULL | NULL | NULL | 2026-02-25T16:48:00.5400000 | NULL | False | False | NULL |
| 000068FB-8E51-4A2D-9F75-42000761919D | NULL | NULL | NULL | NULL | 2026-02-22T09:52:37.5270000 | NULL | False | False | NULL |
| 00004DB9-B575-482B-896C-98A45B2C6FB8 | NULL | NULL | NULL | NULL | 2026-02-26T08:24:40.4700000 | NULL | False | False | NULL |
| 00004695-5E14-463D-A668-241E74547FD5 | NULL | NULL | NULL | NULL | 2026-02-23T03:21:02.2600000 | NULL | False | False | NULL |
| 000045CF-5E77-41D0-9234-15D5F683C41F | NULL | NULL | NULL | NULL | 2026-03-05T16:12:24.9830000 | NULL | False | False | NULL |
| 00003863-BC27-4824-8348-052739564A5D | NULL | NULL | NULL | NULL | 2026-02-23T02:33:22.0930000 | NULL | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.MES_SAP_WorkOrder_Movements_Trn_Tbl.ParentID` -> `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.ID` (Many to One)
