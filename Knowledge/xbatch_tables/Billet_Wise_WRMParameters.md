# XStudio_Xbatch.dbo.Billet_Wise_WRMParameters

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** catalog, entities, entity, from, highlights, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference water, box, temp, pressure, meter, pyro, flow, inlet, outlet, billet.

**Primary Key:** ID  
**Row Count:** 0  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| BilletNo | varchar | YES | 100 | — |
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
| PyroMeter1Temp | decimal | YES | 18,4 | — |
| PyroMeter2Temp | decimal | YES | 18,4 | — |
| PyroMeter3Temp | decimal | YES | 18,4 | — |
| PyroMeter4Temp | decimal | YES | 18,4 | — |
| PyroMeter5Temp | decimal | YES | 18,4 | — |
| PyroMeter6Temp | decimal | YES | 18,4 | — |
| WaterBox1InletPressure | decimal | YES | 18,4 | — |
| WaterBox2InletPressure | decimal | YES | 18,4 | — |
| WaterBox3InletPressure | decimal | YES | 18,4 | — |
| WaterBox0InletPressure | decimal | YES | 18,4 | — |
| WaterBox4InletPressure | decimal | YES | 18,4 | — |
| WaterBox0OutletPressure | decimal | YES | 18,4 | — |
| WaterBox1OutletPressure | decimal | YES | 18,4 | — |
| WaterBox2OutletPressure | decimal | YES | 18,4 | — |
| WaterBox3OutletPressure | decimal | YES | 18,4 | — |
| WaterBox4OutletPressure | decimal | YES | 18,4 | — |
| WaterBox0WaterFlow | decimal | YES | 18,4 | — |
| WaterBox1WaterFlow | decimal | YES | 18,4 | — |
| WaterBox2WaterFlow | decimal | YES | 18,4 | — |
| WaterBox3WaterFlow | decimal | YES | 18,4 | — |
| WaterBox4WaterFlow | decimal | YES | 18,4 | — |
| WaterBox0Temp | decimal | YES | 18,4 | — |
| WaterBox1Temp | decimal | YES | 18,4 | — |
| WaterBox2Temp | decimal | YES | 18,4 | — |
| WaterBox3Temp | decimal | YES | 18,4 | — |
| WaterBox4Temp | decimal | YES | 18,4 | — |

---
