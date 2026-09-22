# XStudio_Xbatch.dbo.RM_Furnace_Parameter

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** catalog, entities, entity, from, highlights, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference temp, zone, actual, bottom, set, soaking, top, gas, heating, left, preheating, pressuremm.

**Primary Key:** ID  
**Row Count:** 8,185  
**Date Range (ModifiedOn):** 2025-12-09T09:52:17.0000000 to 2025-12-09T09:52:35.0000000  

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
| Shift | varchar | YES | 100 | — |
| OperatorName | varchar | YES | 36 | — |
| ProductDia | varchar | YES | 100 | — |
| BilletLength | int | YES | 10,0 | — |
| PreheatingTopZone1TempSet | decimal | YES | 18,4 | — |
| PreheatingTopZone1TempActual | decimal | YES | 18,4 | — |
| PreheatingBottomZone2TempActual | decimal | YES | 18,4 | — |
| PreheatingBottomZone2TempSet | decimal | YES | 18,4 | — |
| HeatingTopBottomZone3TempSet | decimal | YES | 18,4 | — |
| HeatingTopBottomZone3TempActual | decimal | YES | 18,4 | — |
| HeatingBottomZone4TempActual | decimal | YES | 18,4 | — |
| HeatingBottomZone4TempSet | decimal | YES | 18,4 | — |
| SoakingTopLeftZone5TempSet | decimal | YES | 18,4 | — |
| SoakingTopLeftZone5TempActual | decimal | YES | 18,4 | — |
| SoakingTopRightZone6TempActual | decimal | YES | 18,4 | — |
| SoakingTopRightZone6TempSet | decimal | YES | 18,4 | — |
| SoakingBottomLeftZone7TempSet | decimal | YES | 18,4 | — |
| SoakingBottomLeftZone7TempActual | decimal | YES | 18,4 | — |
| SoakingBottomRightZone8TempActual | decimal | YES | 18,4 | — |
| SoakingBottomRightZone8TempSet | decimal | YES | 18,4 | — |
| RecuperatorAirOutletTemp | decimal | YES | 18,4 | — |
| RecuperatorFlueGasInletTemp | decimal | YES | 18,4 | — |
| RecuperatorFlueGasOutletTemp | decimal | YES | 18,4 | — |
| RecuperatorDamperPosition | decimal | YES | 18,4 | — |
| PressuremmWCCombustionAirSet | decimal | YES | 18,4 | — |
| PressuremmWCCombustionAirActual | decimal | YES | 18,4 | — |
| PressuremmWCNaturalGasBeforePRV | decimal | YES | 18,4 | — |
| PressuremmWCNaturalGasAfterPRV | decimal | YES | 18,4 | — |
| PressureFurnaceSet | decimal | YES | 18,4 | — |
| PressureFurnaceActual | decimal | YES | 18,4 | — |
| Remarks | varchar | YES | -1 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 006AFA00-ED43-4DC8-8ADD-41BF213DC9DB | NULL | NULL | NULL | NULL | 2026-07-18T11:01:10.3030000 | NULL | False | False | NULL |
| 00681B8D-FC02-46B3-AAC5-2D82DC9CC615 | NULL | NULL | NULL | NULL | 2026-07-18T10:43:00.7700000 | NULL | False | False | NULL |
| 0062F7E1-C32E-4B42-B104-48177BF4D539 | NULL | NULL | NULL | NULL | 2026-03-19T08:00:01.3300000 | NULL | False | False | NULL |
| 0043198F-3B94-43EC-8B41-C835A9B92AA5 | NULL | NULL | NULL | NULL | 2026-07-18T10:47:45.2100000 | NULL | False | False | NULL |
| 0042EE8C-7B5F-4FC2-8800-0E456B22B103 | NULL | NULL | NULL | NULL | 2025-11-24T16:00:01.4130000 | NULL | False | False | NULL |
| 0041A43A-5389-4D78-AFBA-F4248C621C01 | NULL | NULL | NULL | NULL | 2025-11-21T12:00:00.7270000 | NULL | False | False | NULL |
| 003A6284-57E8-4120-BDC1-EF2CB68BCB1A | NULL | NULL | NULL | NULL | 2026-07-18T10:46:05.5600000 | NULL | False | False | NULL |
| 0030816F-95B2-4F14-AA37-67541F6528B1 | NULL | NULL | NULL | NULL | 2026-07-18T10:56:13.6800000 | NULL | False | False | NULL |
| 00135481-476E-4CA4-8C5D-BAACFE7CB23A | NULL | NULL | NULL | NULL | 2025-12-09T21:00:03.8900000 | NULL | False | False | NULL |
| 0006E945-857C-4F4C-9564-0619643242A0 | NULL | NULL | NULL | NULL | 2026-08-21T10:00:02.5800000 | NULL | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BC44B2BA-A301-4D96-B928-614ABE807E13 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-12-09T08:00:03.3670000 | 2025-12-09T09:52:35.0000000 | False | False | NULL |
| FFC964C9-2BF9-49F9-B494-96890981D405 | NULL | NULL | NULL | 1AAA4BA1-E521-414F-8B25-8DB9185B0642 | 2025-12-09T09:00:03.3670000 | 2025-12-09T09:52:17.0000000 | False | False | NULL |
| 006AFA00-ED43-4DC8-8ADD-41BF213DC9DB | NULL | NULL | NULL | NULL | 2026-07-18T11:01:10.3030000 | NULL | False | False | NULL |
| 00681B8D-FC02-46B3-AAC5-2D82DC9CC615 | NULL | NULL | NULL | NULL | 2026-07-18T10:43:00.7700000 | NULL | False | False | NULL |
| 0062F7E1-C32E-4B42-B104-48177BF4D539 | NULL | NULL | NULL | NULL | 2026-03-19T08:00:01.3300000 | NULL | False | False | NULL |
| 0043198F-3B94-43EC-8B41-C835A9B92AA5 | NULL | NULL | NULL | NULL | 2026-07-18T10:47:45.2100000 | NULL | False | False | NULL |
| 0042EE8C-7B5F-4FC2-8800-0E456B22B103 | NULL | NULL | NULL | NULL | 2025-11-24T16:00:01.4130000 | NULL | False | False | NULL |
| 0041A43A-5389-4D78-AFBA-F4248C621C01 | NULL | NULL | NULL | NULL | 2025-11-21T12:00:00.7270000 | NULL | False | False | NULL |
| 003A6284-57E8-4120-BDC1-EF2CB68BCB1A | NULL | NULL | NULL | NULL | 2026-07-18T10:46:05.5600000 | NULL | False | False | NULL |
| 0030816F-95B2-4F14-AA37-67541F6528B1 | NULL | NULL | NULL | NULL | 2026-07-18T10:56:13.6800000 | NULL | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.RM_Furnace_Parameter.OperatorName` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
