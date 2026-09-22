# XStudio_Xbatch.dbo.LRF_Per_Heat

**table_kind:** production_data

### What this table is for

- **Curated domain match (heat_execution):** Heat missing, wrong EAF/LRF/CCM state, per-heat value wrong, timing, alloy, power, yield, or attribution question.
  (source: `Knowledge/xstudio_semantic_atlas.json` domains, human-curated, not inferred)
- **Indexed under investigation keywords:** area, billet, ccm, chain, confirmed, core, cross, data, entities, event, flow, from, furnace, heat, insert, lrf, map, per, plant, procedure, process, production, routing, same, sms, sohar, stored, system, time, timing, tracking, xbatch, xlsx, xstudio (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference addition, alloy, auto, manual, consumption, electrode, liquid, metal, time, weight, aluminium, carbon.

**Primary Key:** ID  
**Row Count:** 7,857  
**Date Range (ModifiedOn):** 2025-08-20T11:11:27.5530000 to 2026-07-08T23:43:08.6300000  

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
| EquipmentID | varchar | YES | 36 | — |
| StartTime | datetime | YES | — | — |
| EndTime | datetime | YES | — | — |
| Status | varchar | YES | 100 | — |
| PowerONTime | decimal | YES | 18,4 | — |
| PowerOFFTime | decimal | YES | 18,4 | — |
| ArcingTime | decimal | YES | 18,4 | — |
| ArgonConsumption | decimal | YES | 18,4 | — |
| PowerMWH | decimal | YES | 18,4 | — |
| HeatID | int | YES | 10,0 | — |
| EntryDateTime | datetime | YES | — | — |
| ReportDate | varchar | YES | 100 | — |
| IsProcessed | bit | YES | — | — |
| TapStart | datetime | YES | — | — |
| TreatmentStart | datetime | YES | — | — |
| KWHPerTon | decimal | YES | 18,4 | — |
| TreatmentStop | datetime | YES | — | — |
| ProcessTime | decimal | YES | 18,2 | — |
| CokeandNutcokepertonofsteel | decimal | YES | 18,4 | — |
| Argonpertonofsteel | decimal | YES | 18,4 | — |
| LiquidMetalWeight | decimal | YES | 18,4 | — |
| WorkFlowStatus | varchar | YES | 50 | — |
| Lime | decimal | YES | 18,4 | — |
| SiMnn | decimal | YES | 18,4 | — |
| SiMn | decimal | YES | 18,4 | — |
| FeSi | decimal | YES | 18,4 | — |
| Dolo | decimal | YES | 18,4 | — |
| Grade | varchar | YES | 100 | — |
| Avg_LiquidMetalWeight | decimal | YES | 18,4 | — |
| PurgingFlowLPM | decimal | YES | 18,4 | — |
| HeatReportDate | date | YES | — | — |
| WorkOrder | varchar | YES | 100 | — |
| CalcLiquidMetalWeight | decimal | YES | 18,2 | — |
| SAPWorkflowStatus | varchar | YES | 50 | — |
| GLSDelta | decimal | YES | 18,4 | — |
| Avg_CalcLiquidMetalWeight | decimal | YES | 18,2 | — |
| ManualAlloyAdditionLime | decimal | YES | 18,4 | — |
| ManualAlloyAdditionDolo | decimal | YES | 18,4 | — |
| ManualAlloyAdditionFeSi | decimal | YES | 18,4 | — |
| ManualAlloyAdditionSiMn | decimal | YES | 18,4 | — |
| AutoAlloyAdditionLime | decimal | YES | 18,4 | — |
| AutoAlloyAdditionDolo | decimal | YES | 18,4 | — |
| AutoAlloyAdditionFeSi | decimal | YES | 18,4 | — |
| AutoAlloyAdditionSiMn | decimal | YES | 18,4 | — |
| Carbon | decimal | YES | 18,4 | — |
| ManualAlloyAdditionCarbon | decimal | YES | 18,4 | — |
| AutoAlloyAdditionCarbon | decimal | YES | 18,4 | — |
| FlourSpar | decimal | YES | 18,4 | — |
| ManualAlloyAdditionFlourSpar | decimal | YES | 18,4 | — |
| AutoAlloyAdditionFlourSpar | decimal | YES | 18,4 | — |
| Aluminium | decimal | YES | 18,4 | — |
| ManualAlloyAdditionAluminium | decimal | YES | 18,4 | — |
| AutoAlloyAdditionAluminium | decimal | YES | 18,4 | — |
| NitrogenGasConsumption | decimal | YES | 18,4 | — |
| ElectrodeConsumption1Kg | decimal | YES | 18,4 | — |
| ElectrodeConsumption2Kg | decimal | YES | 18,4 | — |
| ElectrodeConsumption3Kg | decimal | YES | 18,4 | — |
| Temperature | decimal | YES | 18,4 | — |
| TemperatureLifting | decimal | YES | 18,4 | — |
| TotalElectrodeConsumptionKg | decimal | YES | 18,4 | — |
| LRFTemperature | decimal | YES | 18,2 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 093A0C0D-6FB6-4D4E-8C4A-901F9B1CCC4B | NULL | NULL | NULL | NULL | 2026-02-14T10:15:54.6400000 | NULL | False | False | NULL |
| 10D47769-BB20-4DC7-9891-FA6C881F8F73 | NULL | NULL | NULL | NULL | 2026-02-14T09:41:57.3230000 | NULL | False | False | NULL |
| 1552188F-B06F-4739-AA03-4915E217B122 | NULL | NULL | NULL | NULL | 2026-01-03T09:02:35.3330000 | NULL | False | False | NULL |
| 1AE2A175-91EF-4631-A188-2023F4215CE0 | NULL | NULL | NULL | NULL | 2026-02-14T09:41:57.3230000 | NULL | False | False | NULL |
| 2953FAEA-5A1D-46E3-974F-1821062A33ED | NULL | NULL | NULL | NULL | 2026-02-14T09:41:57.3230000 | NULL | False | False | NULL |
| 2AFC3775-9A08-4695-A37B-0AD6352DA24F | NULL | NULL | NULL | NULL | 2026-02-14T09:41:57.3230000 | NULL | False | False | NULL |
| 4E745AE8-B9D3-4FAB-AD6D-822A2FA67E2E | NULL | NULL | NULL | NULL | 2026-02-14T10:15:54.6400000 | NULL | False | False | NULL |
| 70593EB4-9B6B-4B36-A856-424DF5105156 | NULL | NULL | NULL | NULL | 2026-02-14T10:15:54.6400000 | NULL | False | False | NULL |
| 7CADBC51-7B2F-4C8A-A4D3-F3056AA8932E | NULL | NULL | NULL | NULL | 2026-02-14T09:41:57.3230000 | NULL | False | False | NULL |
| 7E433286-52BD-4BC5-B8FB-44B55B41C694 | NULL | NULL | NULL | NULL | 2026-02-14T09:41:57.3230000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CFBE325D-C4F7-4C5C-95B5-E2BDC8D997DD | NULL | NULL | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-07-08T17:10:40.3330000 | 2026-07-08T23:43:08.6300000 | False | False | NULL |
| 86093A4C-FE81-42D7-8218-9F0E9DBFC264 | NULL | NULL | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-07-08T16:14:50.2470000 | 2026-07-08T23:41:50.5770000 | False | False | NULL |
| B2E07BEE-388E-4DDC-BAF7-254734C1CCE7 | NULL | NULL | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-07-08T15:14:08.9300000 | 2026-07-08T18:00:23.0200000 | False | False | NULL |
| 0317916D-C2BC-47E7-AE9E-AF558030C846 | NULL | NULL | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-07-08T08:04:32.3370000 | 2026-07-08T17:10:40.9370000 | False | False | NULL |
| 10F2EFCC-A57D-47EE-A94C-7F709BB3D3DC | NULL | NULL | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-07-08T02:05:40.2300000 | 2026-07-08T17:10:40.9370000 | False | False | NULL |
| 3CA5F631-FB24-40A6-BA8A-AB8E56D31E85 | NULL | NULL | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-07-08T06:00:30.3700000 | 2026-07-08T17:10:40.9370000 | False | False | NULL |
| 48D50333-0F68-4509-A6B0-7D6CCA1A5A15 | NULL | NULL | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-07-08T11:05:52.1600000 | 2026-07-08T17:10:40.9370000 | False | False | NULL |
| 575886D1-2773-44CF-A4CC-262CF0B5F551 | NULL | NULL | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-07-08T10:06:15.1870000 | 2026-07-08T17:10:40.9370000 | False | False | NULL |
| 5B4B1978-90B5-4734-B72D-4C28A4272267 | NULL | NULL | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-07-08T05:03:43.3130000 | 2026-07-08T17:10:40.9370000 | False | False | NULL |
| 5CE56060-A987-4911-91FF-F14018FB135D | NULL | NULL | NULL | A6E924D5-B2F0-4A5F-9717-3A63F6190358 | 2026-07-08T04:02:21.9800000 | 2026-07-08T17:10:40.9370000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.LRF_Per_Heat.EquipmentID` -> `XStudio_XBatch.LRF_SMS_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.LRF_Per_Heat.Grade` -> `XStudio_XBatch.Grade_Master.GradeName` (Many to One)
- `XStudio_XBatch.LRF_Per_Heat.WorkOrder` -> `XStudio_XBatch.XBatch_Work_Order_Mst_Tbl.ID` (Many to One)
