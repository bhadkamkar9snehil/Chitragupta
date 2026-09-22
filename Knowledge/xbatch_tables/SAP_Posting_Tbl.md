# XStudio_Xbatch.dbo.SAP_Posting_Tbl

**table_kind:** production_data

### What this table is for

- **Curated domain match (sap_posting):** SAP production/consumption/by-product posting failed, pending, duplicate, or missing a material document.
  (source: `Knowledge/xstudio_semantic_atlas.json` domains, human-curated, not inferred)
- **Indexed under investigation keywords:** chemistry, core, errors, integration, posting, quality, routing, sap, spectro (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference sap, code, posting, type, batch, date, document, heat, json, location, material, message.

**Primary Key:** ID  
**Row Count:** 84  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| WorkOrderNo | varchar | YES | 100 | — |
| HeatNo | varchar | YES | 100 | — |
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
| PlantCode | varchar | YES | 100 | — |
| StorageLocation | varchar | YES | 100 | — |
| MaterialCode | varchar | YES | 100 | — |
| BatchNo | varchar | YES | 100 | — |
| Quantity | decimal | YES | 18,3 | — |
| UOM | varchar | YES | 100 | — |
| MovementType | varchar | YES | 100 | — |
| PostingType | varchar | YES | 100 | — |
| PostingDate | datetime | YES | — | — |
| SAP_Status | varchar | YES | 100 | — |
| SAP_DocumentNo | varchar | YES | 100 | — |
| SAP_Message | varchar | YES | 100 | — |
| SAP_PayloadJson | varchar | YES | -1 | — |

### Top 10 Records

| ID | WorkOrderNo | HeatNo | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1A4C0D2C-93E7-4479-93E9-8BD07D97EE2F | WO_001 | 1506341 | NULL | NULL | 2025-10-30T08:01:09.1670000 | NULL | False | False | NULL |
| 1421DC0C-C650-4CD0-8D75-CB0F76D383C9 | WO_002 | 1506371 | NULL | NULL | 2025-10-31T11:57:19.7970000 | NULL | False | False | NULL |
| 115E19F9-4946-4EA2-9362-D3C0FB74694E | WO_001 | 1506340 | NULL | NULL | 2025-10-30T06:53:57.6970000 | NULL | False | False | NULL |
| 0FE3EFA1-6EAC-4D01-ADEF-BB2D94327598 | WO_002 | 1506371 | NULL | NULL | 2025-10-31T12:42:47.2330000 | NULL | False | False | NULL |
| 0F7A6A1B-87BC-4146-9B8F-9F1672908CD3 | WO_001 | 1506339 | NULL | NULL | 2025-10-30T06:06:14.8130000 | NULL | False | False | NULL |
| 0DDE9838-1261-4343-A790-6F91F1C25B17 | WO_001 | 1506339 | NULL | NULL | 2025-10-30T06:06:14.8370000 | NULL | False | False | NULL |
| 0BD10250-E93A-4617-A708-1FB3096CA392 | WO_002 | 1506373 | NULL | NULL | 2025-10-31T14:44:01.3600000 | NULL | False | False | NULL |
| 06D41AF7-8D17-4E34-B91C-79C9B383BDC5 | WO_002 | 1506373 | NULL | NULL | 2025-10-31T13:45:46.3000000 | NULL | False | False | NULL |
| 0620F7F2-CEB5-40C3-B3C2-9885CD512CE9 | WO_002 | 1506371 | NULL | NULL | 2025-10-31T12:31:23.8130000 | NULL | False | False | NULL |
| 00AB9E1D-3369-443E-A090-926DE652A8C6 | WO_001 | 1506339 | NULL | NULL | 2025-10-30T06:06:14.8270000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | WorkOrderNo | HeatNo | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1A4C0D2C-93E7-4479-93E9-8BD07D97EE2F | WO_001 | 1506341 | NULL | NULL | 2025-10-30T08:01:09.1670000 | NULL | False | False | NULL |
| 1421DC0C-C650-4CD0-8D75-CB0F76D383C9 | WO_002 | 1506371 | NULL | NULL | 2025-10-31T11:57:19.7970000 | NULL | False | False | NULL |
| 115E19F9-4946-4EA2-9362-D3C0FB74694E | WO_001 | 1506340 | NULL | NULL | 2025-10-30T06:53:57.6970000 | NULL | False | False | NULL |
| 0FE3EFA1-6EAC-4D01-ADEF-BB2D94327598 | WO_002 | 1506371 | NULL | NULL | 2025-10-31T12:42:47.2330000 | NULL | False | False | NULL |
| 0F7A6A1B-87BC-4146-9B8F-9F1672908CD3 | WO_001 | 1506339 | NULL | NULL | 2025-10-30T06:06:14.8130000 | NULL | False | False | NULL |
| 0DDE9838-1261-4343-A790-6F91F1C25B17 | WO_001 | 1506339 | NULL | NULL | 2025-10-30T06:06:14.8370000 | NULL | False | False | NULL |
| 0BD10250-E93A-4617-A708-1FB3096CA392 | WO_002 | 1506373 | NULL | NULL | 2025-10-31T14:44:01.3600000 | NULL | False | False | NULL |
| 06D41AF7-8D17-4E34-B91C-79C9B383BDC5 | WO_002 | 1506373 | NULL | NULL | 2025-10-31T13:45:46.3000000 | NULL | False | False | NULL |
| 0620F7F2-CEB5-40C3-B3C2-9885CD512CE9 | WO_002 | 1506371 | NULL | NULL | 2025-10-31T12:31:23.8130000 | NULL | False | False | NULL |
| 00AB9E1D-3369-443E-A090-926DE652A8C6 | WO_001 | 1506339 | NULL | NULL | 2025-10-30T06:06:14.8270000 | NULL | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.SAP_Posting_Tbl.CreatedBy` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.SAP_Posting_Tbl.MaterialCode` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.Name` (Many to One)
- `XStudio_XBatch.SAP_Posting_Tbl.ModifiedBy` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.SAP_Posting_Tbl.StorageLocation` -> `XStudio_XBatch.XBatch_Store_Mst_Tbl.Name` (Many to One)
- `XStudio_XBatch.SAP_Posting_Tbl.WorkOrderNo` -> `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.WorkOrderNumber` (Many to One)
