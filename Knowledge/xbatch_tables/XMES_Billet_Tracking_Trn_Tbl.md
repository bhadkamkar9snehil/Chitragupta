# XStudio_Xbatch.dbo.XMES_Billet_Tracking_Trn_Tbl

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference billet, batch, cut, heat, length, location, manufacturing, material, materialid, order, plant, position.

**Primary Key:** ID  
**Row Count:** 1,80,813  
**Date Range (ModifiedOn):** 2026-06-12T12:22:04.0900000 to 2026-07-08T23:43:07.8370000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| Name | varchar | YES | 36 | — |
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
| HeatNo | varchar | YES | 100 | — |
| Batch | varchar | YES | 100 | — |
| BilletNo | varchar | YES | 100 | — |
| Plant | varchar | YES | 100 | — |
| StorageLocation | varchar | YES | 100 | — |
| StatePosition | varchar | YES | 100 | — |
| ProcessStage | varchar | YES | 100 | — |
| Materialid | varchar | YES | 36 | — |
| Qualitygradeid | varchar | YES | 36 | — |
| BilletWeight | decimal | YES | 18,3 | — |
| UOMID | varchar | YES | 36 | — |
| ManufacturingOrder | varchar | YES | 100 | — |
| BilletQuantity | int | YES | 10,0 | — |
| PostingMaterialType | varchar | YES | 100 | — |
| CutLength | decimal | YES | 18,3 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00054D2F-A206-4080-B89B-094072CB2A50 | NULL | NULL | NULL | NULL | 2026-07-31T13:28:22.0100000 | NULL | False | False | NULL |
| 00047AE0-9D76-4215-A6EC-48D8D7F2ACBA | NULL | NULL | NULL | NULL | 2026-08-01T14:37:54.2830000 | NULL | False | False | NULL |
| 0003D8F6-20D5-42B4-9F0C-1B6FD01B49E5 | NULL | NULL | NULL | NULL | 2026-07-04T06:26:19.8330000 | NULL | True | False | NULL |
| 0003C73C-3102-40F6-BFEA-ED4616F5CC7B | NULL | NULL | NULL | NULL | 2026-07-30T15:39:23.5400000 | NULL | False | False | NULL |
| 0003C054-2329-4887-B345-19A68A34044D | NULL | NULL | NULL | NULL | 2026-06-18T19:30:05.5900000 | NULL | False | False | NULL |
| 00029E0E-D53E-46ED-BDB5-880402B81AEA | NULL | NULL | NULL | NULL | 2026-06-13T14:49:08.9570000 | NULL | False | False | NULL |
| 00024996-6857-4315-81A5-8D61235E0255 | NULL | NULL | NULL | NULL | 2026-08-01T00:21:07.5000000 | NULL | False | False | NULL |
| 00018D65-BBF9-4099-AE82-86D677E70A90 | NULL | NULL | NULL | NULL | 2026-08-21T17:27:01.5730000 | NULL | False | False | NULL |
| 000172B4-C57A-4AFA-9ADF-882887BA8062 | NULL | NULL | NULL | NULL | 2026-08-21T17:18:28.1900000 | NULL | False | False | NULL |
| 00013BD0-3D92-4390-8ED3-E285C4ACDC70 | NULL | NULL | NULL | NULL | 2026-06-29T14:01:23.1200000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 02F47AC6-CC79-442A-9555-EACAFF37FCED | NULL | NULL | NULL | NULL | 2026-07-08T19:07:15.2670000 | 2026-07-08T23:43:07.8370000 | False | False | NULL |
| 11641183-1CEA-488A-A614-F839076AC096 | NULL | NULL | NULL | NULL | 2026-07-08T18:42:40.3800000 | 2026-07-08T23:43:07.8370000 | False | False | NULL |
| 135531D6-7389-44C0-8B9C-DAF185D19381 | NULL | NULL | NULL | NULL | 2026-07-08T19:07:38.2000000 | 2026-07-08T23:43:07.8370000 | False | False | NULL |
| 148A815B-BB7D-4182-AA1D-40A69AC01F2A | NULL | NULL | NULL | NULL | 2026-07-08T18:40:03.2230000 | 2026-07-08T23:43:07.8370000 | False | False | NULL |
| 21901FBF-67A9-4DDB-8E56-0F78F7A1DA8F | NULL | NULL | NULL | NULL | 2026-07-08T18:26:51.2400000 | 2026-07-08T23:43:07.8370000 | False | False | NULL |
| 29DAABEA-15F7-4DEB-92D6-E3C25B2DE50E | NULL | NULL | NULL | NULL | 2026-07-08T18:53:35.0630000 | 2026-07-08T23:43:07.8370000 | False | False | NULL |
| 2C03BD16-AB3F-4C9D-9869-AF54F1F0BC3A | NULL | NULL | NULL | NULL | 2026-07-08T18:28:49.1330000 | 2026-07-08T23:43:07.8370000 | False | False | NULL |
| 2E68E3EF-67EF-481D-801C-EC7DD9AEFD6F | NULL | NULL | NULL | NULL | 2026-07-08T18:30:49.3030000 | 2026-07-08T23:43:07.8370000 | False | False | NULL |
| 2EF408FF-651B-4558-AB72-952B38A17136 | NULL | NULL | NULL | NULL | 2026-07-08T18:36:29.9830000 | 2026-07-08T23:43:07.8370000 | False | False | NULL |
| 3E154785-C7EB-4D79-9B1F-091C5BC1369F | NULL | NULL | NULL | NULL | 2026-07-08T18:29:35.0430000 | 2026-07-08T23:43:07.8370000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.XMES_Billet_Tracking_Trn_Tbl.Materialid` -> `XStudio_XBatch.XBatch_Material_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XMES_Billet_Tracking_Trn_Tbl.ProcessStage` -> `XStudio_XBatch.XMES_Process_Stage_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XMES_Billet_Tracking_Trn_Tbl.Qualitygradeid` -> `XStudio_XBatch.XBatch_Material_Grade_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XMES_Billet_Tracking_Trn_Tbl.StatePosition` -> `XStudio_XBatch.XMES_State_Position_State_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XMES_Billet_Tracking_Trn_Tbl.UOMID` -> `XStudio_XBatch.XBatch_Measurement_Unit_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.XMES_Live_Billet_Charging_Bed.ID` -> `XStudio_XBatch.XMES_Billet_Tracking_Trn_Tbl.ParentID` (Many to One)
