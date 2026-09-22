# XStudio_Xbatch.dbo.RM_Furnace_Combustion_5

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference zone, flow, water, circuit, temp, air, gas, outlet, actual, combustion, point, set.

**Primary Key:** ID  
**Row Count:** 0  

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
| EntryDateTime | datetime | YES | — | — |
| ReportDate | date | YES | — | — |
| IsProcessed | bit | YES | — | — |
| CombustionAirPressure | decimal | YES | 18,4 | — |
| CombustionAirTemperature | decimal | YES | 18,4 | — |
| WasteGasO2 | decimal | YES | 18,4 | — |
| WasteGasTemperatureAfterRecuperator | decimal | YES | 18,4 | — |
| WasteGasTemperatureBeforeRecuperator | decimal | YES | 18,4 | — |
| FurnacePressure1 | decimal | YES | 18,4 | — |
| GasTotalizer1 | decimal | YES | 18,4 | — |
| WbWaterInletT | decimal | YES | 18,4 | — |
| WbWaterOutletTFixCircuit01 | decimal | YES | 18,4 | — |
| WbWaterFlowFixCircuit01 | decimal | YES | 18,4 | — |
| WbWaterOutletTFixCircuit02 | decimal | YES | 18,4 | — |
| WbWaterFlowFixCircuit02 | decimal | YES | 18,4 | — |
| WbWaterOutletTFixCircuit03 | decimal | YES | 18,4 | — |
| WbWaterFlowFixCircuit03 | decimal | YES | 18,4 | — |
| WbWaterOutletTFixCircuit04 | decimal | YES | 18,4 | — |
| WbWaterFlowFixCircuit04 | decimal | YES | 18,4 | — |
| WbWaterOutletTFixCircuit05 | decimal | YES | 18,4 | — |
| WbWaterFlowFixCircuit05 | decimal | YES | 18,4 | — |
| WbWaterOutletTFixCircuit06 | decimal | YES | 18,4 | — |
| WbWaterFlowFixCircuit06 | decimal | YES | 18,4 | — |
| WbWaterOutletTMovCircuit01 | decimal | YES | 18,4 | — |
| WbWaterFlowMovCircuit01 | decimal | YES | 18,4 | — |
| WbWaterOutletTMovCircuit02 | decimal | YES | 18,4 | — |
| WbWaterFlowMovCircuit02 | decimal | YES | 18,4 | — |
| WbWaterOutletTMovCircuit03 | decimal | YES | 18,4 | — |
| WbWaterFlowMovCircuit03 | decimal | YES | 18,4 | — |
| WbWaterOutletTMovCircuit04 | decimal | YES | 18,4 | — |
| WbWaterFlowMovCircuit04 | decimal | YES | 18,4 | — |
| CombustionAirFan1ShaftVibration | decimal | YES | 18,4 | — |
| CombustionAirFan1ShaftBearingTemp1 | decimal | YES | 18,4 | — |
| CombustionAirFan1ShaftBearingTemp2 | decimal | YES | 18,4 | — |
| CombustionAirFan2ShaftVibration | decimal | YES | 18,4 | — |
| CombustionAirFan2ShaftBearingTemp1 | decimal | YES | 18,4 | — |
| CombustionAirFan2ShaftBearingTemp2 | decimal | YES | 18,4 | — |
| Zone01SetPointTemp | decimal | YES | 18,4 | — |
| Zone01ActualTemp | decimal | YES | 18,4 | — |
| Zone02SetPointTemp | decimal | YES | 18,4 | — |
| Zone02ActualTemp | decimal | YES | 18,4 | — |
| Zone03SetPointTemp | decimal | YES | 18,4 | — |
| Zone03ActualTemp | decimal | YES | 18,4 | — |
| Zone04SetPointTemp | decimal | YES | 18,4 | — |
| Zone04ActualTemp | decimal | YES | 18,4 | — |
| Zone05SetPointTemp | decimal | YES | 18,4 | — |
| Zone05ActualTemp | decimal | YES | 18,4 | — |
| Zone06SetPointTemp | decimal | YES | 18,4 | — |
| Zone06ActualTemp | decimal | YES | 18,4 | — |
| Zone07SetPointTemp | decimal | YES | 18,4 | — |
| Zone07ActualTemp | decimal | YES | 18,4 | — |
| Zone08SetPointTemp | decimal | YES | 18,4 | — |
| Zone08ActualTemp | decimal | YES | 18,4 | — |
| Zone03AirFlow1 | decimal | YES | 18,4 | — |
| Zone03GasFlow1 | decimal | YES | 18,4 | — |
| Zone04AirFlow1 | decimal | YES | 18,4 | — |
| Zone04GasFlow1 | decimal | YES | 18,4 | — |
| Zone05AirFlow1 | decimal | YES | 18,4 | — |
| Zone05GasFlow1 | decimal | YES | 18,4 | — |
| Zone06AirFlow1 | decimal | YES | 18,4 | — |
| Zone06GasFlow1 | decimal | YES | 18,4 | — |
| Zone07AirFlow1 | decimal | YES | 18,4 | — |
| Zone07GasFlow1 | decimal | YES | 18,4 | — |
| Zone08AirFlow1 | decimal | YES | 18,4 | — |
| Zone08GasFlow1 | decimal | YES | 18,4 | — |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.RM_Furnace_Combustion_5.EquipmentID` -> `XStudio_XBatch.RM_Furnace_Combustion_Mst_Tbl.ID` (Many to One)
