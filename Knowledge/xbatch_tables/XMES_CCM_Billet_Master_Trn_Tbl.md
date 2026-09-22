# XStudio_Xbatch.dbo.XMES_CCM_Billet_Master_Trn_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference billet, batch, cut, heat, length, location, manufacturing, material, materialid, order, plant, position.

**Primary Key:** ID  
**Row Count:** 12,862  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
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
| CutLength | decimal | YES | 18,4 | — |
| Plant | varchar | YES | 100 | — |
| ParentID | varchar | YES | 36 | — |
| StatePosition | varchar | YES | 100 | — |
| Qualitygradeid | varchar | YES | 36 | — |
| BilletQuantity | int | YES | 10,0 | — |
| EntryDateTime | datetime | YES | — | — |
| BilletWeight | decimal | YES | 18,4 | — |
| BilletNo | varchar | YES | 100 | — |
| ProcessStage | varchar | YES | 100 | — |
| HeatNo | varchar | YES | 100 | — |
| UOMID | varchar | YES | 36 | — |
| Batch | varchar | YES | 100 | — |
| IsProcessed | bit | YES | — | — |
| ManufacturingOrder | varchar | YES | 100 | — |
| ReportDate | date | YES | — | — |
| Name | varchar | YES | 100 | — |
| PostingMaterialType | varchar | YES | 100 | — |
| StorageLocation | varchar | YES | 100 | — |
| Materialid | varchar | YES | 36 | — |

### Top 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 003C7A96-9137-4A81-B08A-463A68D8F1DF | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-06-24T20:47:40.8130000 | NULL | False | False | NULL | NULL | NULL |
| 00380800-08F8-4EB4-815F-E551BCD2F7F2 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-06-24T20:19:32.6900000 | NULL | False | False | NULL | NULL | NULL |
| 0032FFC9-06FA-4F75-BF58-AC35A227B24A | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-07-05T23:29:23.9870000 | NULL | False | False | NULL | NULL | NULL |
| 0025C085-A9C1-4FE2-8283-119CAC0FFADB | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-07-03T05:47:04.8930000 | NULL | False | False | NULL | NULL | NULL |
| 00194768-48EE-4ABE-928C-38B2DA6A1EEE | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-06-22T17:34:00.8100000 | NULL | False | False | NULL | NULL | NULL |
| 00188CDB-7A2F-49B9-B5D3-A7DFE64F6ED0 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-06-29T23:56:58.9530000 | NULL | False | False | NULL | NULL | NULL |
| 0014ADAE-7FF8-4FAB-B5DA-83F4181C94DF | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-06-22T23:51:55.5570000 | NULL | False | False | NULL | NULL | NULL |
| 000EFE68-38F1-43E9-A94E-35D5524F5C5F | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-07-06T06:01:40.8330000 | NULL | False | False | NULL | NULL | NULL |
| 000DED28-08C1-4E8F-9A97-044C3C71D765 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-06-27T15:09:14.9500000 | NULL | False | False | NULL | NULL | NULL |
| 000D1AC1-1C4F-423E-8EBF-A4B5EF209C5F | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-07-04T20:46:48.5970000 | NULL | False | False | NULL | NULL | NULL |

### Bottom 10 Records

| ID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress | DbSyncStatus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 003C7A96-9137-4A81-B08A-463A68D8F1DF | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-06-24T20:47:40.8130000 | NULL | False | False | NULL | NULL | NULL |
| 00380800-08F8-4EB4-815F-E551BCD2F7F2 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-06-24T20:19:32.6900000 | NULL | False | False | NULL | NULL | NULL |
| 0032FFC9-06FA-4F75-BF58-AC35A227B24A | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-07-05T23:29:23.9870000 | NULL | False | False | NULL | NULL | NULL |
| 0025C085-A9C1-4FE2-8283-119CAC0FFADB | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-07-03T05:47:04.8930000 | NULL | False | False | NULL | NULL | NULL |
| 00194768-48EE-4ABE-928C-38B2DA6A1EEE | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-06-22T17:34:00.8100000 | NULL | False | False | NULL | NULL | NULL |
| 00188CDB-7A2F-49B9-B5D3-A7DFE64F6ED0 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-06-29T23:56:58.9530000 | NULL | False | False | NULL | NULL | NULL |
| 0014ADAE-7FF8-4FAB-B5DA-83F4181C94DF | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-06-22T23:51:55.5570000 | NULL | False | False | NULL | NULL | NULL |
| 000EFE68-38F1-43E9-A94E-35D5524F5C5F | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-07-06T06:01:40.8330000 | NULL | False | False | NULL | NULL | NULL |
| 000DED28-08C1-4E8F-9A97-044C3C71D765 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-06-27T15:09:14.9500000 | NULL | False | False | NULL | NULL | NULL |
| 000D1AC1-1C4F-423E-8EBF-A4B5EF209C5F | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-07-04T20:46:48.5970000 | NULL | False | False | NULL | NULL | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XMES_CCM_Billet_Master_Trn_Tbl.Materialid` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XMES_CCM_Billet_Master_Trn_Tbl.ProcessStage` -> `XStudio_XBatch.XMES_Process_Stage_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XMES_CCM_Billet_Master_Trn_Tbl.Qualitygradeid` -> `XStudio_XBatch.XBatch_Material_Grade_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XMES_CCM_Billet_Master_Trn_Tbl.StatePosition` -> `XStudio_XBatch.XMES_State_Position_State_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XMES_CCM_Billet_Master_Trn_Tbl.UOMID` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
