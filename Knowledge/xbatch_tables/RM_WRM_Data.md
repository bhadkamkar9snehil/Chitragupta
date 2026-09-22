# XStudio_Xbatch.dbo.RM_WRM_Data

**table_kind:** production_data

### What this table is for

- **Inferred from its own column names** (not human-verified): columns repeatedly reference wrm, fan, stelmore, status, conveyor, occupied, pallet, box, wrmwater, wrmpinchroll, speed, torque.

**Primary Key:** ID  
**Row Count:** 1  
**Date Range (ModifiedOn):** 2026-08-31T10:35:09.7830000 to 2026-08-31T10:35:09.7830000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| WrmStelmoreFan1SpeedRpm | decimal | YES | 18,4 | — |
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
| WRMWaterBox0WaterFlowM3HPRM | decimal | YES | 18,4 | — |
| WRMWaterBox0InletPressureBARPRM | decimal | YES | 18,4 | — |
| WRMWaterBox0OutletPressureBARPRM | decimal | YES | 18,4 | — |
| WRMWaterBox0TemperatureCPRM | decimal | YES | 18,4 | — |
| WRMPINCHROLL0CURRENTAPRM | decimal | YES | 18,4 | — |
| WRMPINCHROLL0SPEEDMSPRM | decimal | YES | 18,4 | — |
| WRMPINCHROLL0TORQUENMPRM | decimal | YES | 18,4 | — |
| Shear3HL | decimal | YES | 18,4 | — |
| Shear3TL | decimal | YES | 18,4 | — |
| ChoppingShearCurrent | decimal | YES | 18,4 | — |
| ChoppingShearSpeed | decimal | YES | 18,4 | — |
| ChoppingShearTorque | decimal | YES | 18,4 | — |
| SnappingShearCurrent | decimal | YES | 18,4 | — |
| SnappingShearSpeed | decimal | YES | 18,4 | — |
| SnappingShearTorque | decimal | YES | 18,4 | — |
| InletTemperature | decimal | YES | 18,4 | — |
| OutletTemperature | decimal | YES | 18,4 | — |
| WRMWaterBox1WaterFlowM3HPRM | decimal | YES | 18,4 | — |
| WRMWaterBox1InletPressureBARPRM | decimal | YES | 18,4 | — |
| WRMWaterBox1OutletPressureBARPRM | decimal | YES | 18,4 | — |
| WRMPINCHROLL1CURRENTAPRM | decimal | YES | 18,4 | — |
| WRMPINCHROLL1SPEEDMSPRM | decimal | YES | 18,4 | — |
| WRMPINCHROLL1TORQUENMPRM | decimal | YES | 18,4 | — |
| WRMWaterBox2WaterFlowM3HPRM | decimal | YES | 18,4 | — |
| WRMWaterBox2InletPressureBARPRM | decimal | YES | 18,4 | — |
| WRMWaterBox2OutletPressureBARPRM | decimal | YES | 18,4 | — |
| WRMWaterBox2TemperatureCPRM | decimal | YES | 18,4 | — |
| WRMPINCHROLL2CURRENTAPRM | decimal | YES | 18,4 | — |
| WRMPINCHROLL2SPEEDMSPRM | decimal | YES | 18,4 | — |
| WRMPINCHROLL2TORQUENMPRM | decimal | YES | 18,4 | — |
| WRMWaterBox3WaterFlowM3HPRM | decimal | YES | 18,4 | — |
| WRMWaterBox3InletPressureBARPRM | decimal | YES | 18,4 | — |
| WRMWaterBox3OutletPressureBARPRM | decimal | YES | 18,4 | — |
| WRMPINCHROLL3CURRENTAPRM | decimal | YES | 18,4 | — |
| WRMPINCHROLL3SPEEDMSPRM | decimal | YES | 18,4 | — |
| WRMPINCHROLL3TORQUENMPRM | decimal | YES | 18,4 | — |
| WRMWaterBox4WaterFlowM3HPRM | decimal | YES | 18,4 | — |
| WRMWaterBox4InletPressureBARPRM | decimal | YES | 18,4 | — |
| WRMWaterBox4OutletPressureBARPRM | decimal | YES | 18,4 | — |
| WRMWaterBox4TemperatureCPRM | decimal | YES | 18,4 | — |
| WRMPINCHROLL4CURRENTAPRM | decimal | YES | 18,4 | — |
| WRMPINCHROLL4SPEEDMSPRM | decimal | YES | 18,4 | — |
| WRMPINCHROLL4TORQUENMPRM | decimal | YES | 18,4 | — |
| LayingHandTemperature | decimal | YES | 18,4 | — |
| WRMPYROMETER1TEMPCPRM | decimal | YES | 18,4 | — |
| WRMPYROMETER4TEMPCPRM | decimal | YES | 18,4 | — |
| WRMPYROMETER5TEMPCPRM | decimal | YES | 18,4 | — |
| WRMWaterBox1TemperatureCPRM | decimal | YES | 18,4 | — |
| WRMWaterBox3TemperatureCPRM | decimal | YES | 18,4 | — |
| WRMPYROMETER2TEMPCPRM | decimal | YES | 18,4 | — |
| WRMPYROMETER3TEMPCPRM | decimal | YES | 18,4 | — |
| WRMPYROMETER6TEMPCPRM | decimal | YES | 18,4 | — |
| WRMCHOPPINGSHEARCURRENTAPRM | decimal | YES | 18,4 | — |
| CHOPPINGSHEARENOFFSTATUS | decimal | YES | 18,4 | — |
| WRMCHOPPINGSHEARONSTATUS | decimal | YES | 18,4 | — |
| WRMCHOPPINGSHEARSPEEDMSPRM | decimal | YES | 18,4 | — |
| WRMCHOPPINGSHEARTORQUENMPRM | decimal | YES | 18,4 | — |
| WRMLAYINGHEADCURRENTAPRM | decimal | YES | 18,4 | — |
| WRMLAYINGHEADONSTATUS | decimal | YES | 18,4 | — |
| WRMLAYINGHEADSPEEDMSPRM | decimal | YES | 18,4 | — |
| WRMLAYINGHEADTORQUENMPRM | decimal | YES | 18,4 | — |
| WRMLAYINGHEADVELOCITYMSPRM | decimal | YES | 18,4 | — |
| WRMNTMCURRENTAPRM | decimal | YES | 18,4 | — |
| WRMNTMSPEEDMSPRM | decimal | YES | 18,4 | — |
| WRMNTMTORQUENMPRM | decimal | YES | 18,4 | — |
| WRMNTMWATERPRESSUREBARPRM | decimal | YES | 18,4 | — |
| WRMSIDELOOPERACTUALDEGPRM | decimal | YES | 18,4 | — |
| WRMSIDELOOPERSETDEGPRM | decimal | YES | 18,4 | — |
| WRMWATERBOX0FLOWM3HPRM | decimal | YES | 18,4 | — |
| WRMWATERBOX0INLET_PRESSUREBARPRM | decimal | YES | 18,4 | — |
| WrmStelmoreFan1OffStatus | decimal | YES | 18,4 | — |
| WrmStelmoreFan1ReadyStatus | decimal | YES | 18,4 | — |
| WrmStelmoreFan1RunningStatus | decimal | YES | 18,4 | — |
| WrmStelmoreFan1TorqueNm | decimal | YES | 18,4 | — |
| WrmStelmoreFan2OffStatus | decimal | YES | 18,4 | — |
| WrmStelmoreFan2ReadyStatus | decimal | YES | 18,4 | — |
| WrmStelmoreFan2RunningStatus | decimal | YES | 18,4 | — |
| WrmStelmoreFan2SpeedRpm | decimal | YES | 18,4 | — |
| WrmStelmoreFan2TorqueNm | decimal | YES | 18,4 | — |
| WrmStelmoreFan3OffStatus | decimal | YES | 18,4 | — |
| WrmStelmoreFan3ReadyStatus | decimal | YES | 18,4 | — |
| WrmStelmoreFan3RunningStatus | decimal | YES | 18,4 | — |
| WrmStelmoreFan3SpeedRpm | decimal | YES | 18,4 | — |
| WrmStelmoreFan3TorqueNm | decimal | YES | 18,4 | — |
| WrmStelmoreFan4OffStatus | decimal | YES | 18,4 | — |
| WrmStelmoreFan4ReadyStatus | decimal | YES | 18,4 | — |
| WrmStelmoreFan4SpeedRpm | decimal | YES | 18,4 | — |
| WrmStelmoreFan4RunningStatus | decimal | YES | 18,4 | — |
| WrmStelmoreFan4TorqueNm | decimal | YES | 18,4 | — |
| WrmStelmoreFan5OffStatus | decimal | YES | 18,4 | — |
| WrmStelmoreFan5ReadyStatus | decimal | YES | 18,4 | — |
| WrmStelmoreFan5RunningStatus | decimal | YES | 18,4 | — |
| WrmStelmoreFan5SpeedRpm | decimal | YES | 18,4 | — |
| WrmStelmoreFan5TorqueNm | decimal | YES | 18,4 | — |
| WrmStelmoreFan6OffStatus | decimal | YES | 18,4 | — |
| WrmStelmoreFan6ReadyStatus | decimal | YES | 18,4 | — |
| WrmStelmoreFan6RunningStatus | decimal | YES | 18,4 | — |
| WrmStelmoreFan6SpeedRpm | decimal | YES | 18,4 | — |
| WrmStelmoreFan6TorqueNm | decimal | YES | 18,4 | — |
| WrmStelmoreFan7OffStatus | decimal | YES | 18,4 | — |
| WrmStelmoreFan7ReadyStatus | decimal | YES | 18,4 | — |
| WrmStelmoreFan7RunningStatus | decimal | YES | 18,4 | — |
| WrmStelmoreFan7SpeedRpm | decimal | YES | 18,4 | — |
| WrmStelmoreFan7TorqueNm | decimal | YES | 18,4 | — |
| WrmStelmoreFan8OffStatus | decimal | YES | 18,4 | — |
| WrmStelmoreFan8ReadyStatus | decimal | YES | 18,4 | — |
| WrmStelmoreFan8RunningStatus | decimal | YES | 18,4 | — |
| WrmStelmoreFan8SpeedRpm | decimal | YES | 18,4 | — |
| WrmStelmoreFan8TorqueNm | decimal | YES | 18,4 | — |
| WrmStelmoreFan9OffStatus | decimal | YES | 18,4 | — |
| WrmStelmoreFan9ReadyStatus | decimal | YES | 18,4 | — |
| WrmStelmoreFan9RunningStatus | decimal | YES | 18,4 | — |
| WrmStelmoreFan9SpeedRpm | decimal | YES | 18,4 | — |
| WrmStelmoreFan9TorqueNm | decimal | YES | 18,4 | — |
| WrmStelmoreFan10OffStatus | decimal | YES | 18,4 | — |
| WrmStelmoreFan10ReadyStatus | decimal | YES | 18,4 | — |
| WrmStelmoreFan10RunningStatus | decimal | YES | 18,4 | — |
| WrmStelmoreFan10SpeedRpm | decimal | YES | 18,4 | — |
| WrmStelmoreFan10TorqueNm | decimal | YES | 18,4 | — |
| WrmStelmoreFan11OffStatus | decimal | YES | 18,4 | — |
| WrmStelmoreFan11ReadyStatus | decimal | YES | 18,4 | — |
| WrmStelmoreFan11RunningStatus | decimal | YES | 18,4 | — |
| WrmStelmoreFan11SpeedRpm | decimal | YES | 18,4 | — |
| WrmStelmoreFan11TorqueNm | decimal | YES | 18,4 | — |
| WrmStelmoreFan12OffStatus | decimal | YES | 18,4 | — |
| WrmStelmoreFan12ReadyStatus | decimal | YES | 18,4 | — |
| WrmStelmoreFan12RunningStatus | decimal | YES | 18,4 | — |
| WrmStelmoreFan12SpeedRpm | decimal | YES | 18,4 | — |
| WrmStelmoreFan12TorqueNm | decimal | YES | 18,4 | — |
| WrmPfLineReadyStatus | decimal | YES | 18,4 | — |
| WrmPalletConveyor1OccupiedStatus | decimal | YES | 18,4 | — |
| WrmPalletConveyor2OccupiedStatus | decimal | YES | 18,4 | — |
| WrmPalletConveyor3OccupiedStatus | decimal | YES | 18,4 | — |
| WrmPalletConveyor5OccupiedStatus | decimal | YES | 18,4 | — |
| WrmPalletConveyor6OccupiedStatus | decimal | YES | 18,4 | — |
| WrmPalletConveyor7OccupiedStatus | decimal | YES | 18,4 | — |
| WrmPalletConveyor8OccupiedStatus | decimal | YES | 18,4 | — |
| WrmPalletConveyor9OccupiedStatus | decimal | YES | 18,4 | — |
| WrmPalletConveyor10OccupiedStatus | decimal | YES | 18,4 | — |
| WrmPalletConveyor12OccupiedStatus | decimal | YES | 18,4 | — |
| WrmPalletConveyor13OccupiedStatus | decimal | YES | 18,4 | — |
| WrmPalletConveyor14OccupiedStatus | decimal | YES | 18,4 | — |
| WrmPalletConveyor15OccupiedStatus | decimal | YES | 18,4 | — |
| WrmPalletConveyor17OccupiedStatus | decimal | YES | 18,4 | — |
| WrmPalletConveyor18OccupiedStatus | decimal | YES | 18,4 | — |
| WrmPalletConveyor19OccupiedStatus | decimal | YES | 18,4 | — |
| WrmPalletConveyor20OccupiedStatus | decimal | YES | 18,4 | — |
| WrmPalletConveyor21OccupiedStatus | decimal | YES | 18,4 | — |
| WrmPalletConveyor22OccupiedStatus | decimal | YES | 18,4 | — |
| WrmPalletConveyor23OccupiedStatus | decimal | YES | 18,4 | — |
| WrmPalletConveyor25OccupiedStatus | decimal | YES | 18,4 | — |
| WrmPalletConveyor26OccupiedStatus | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | WrmStelmoreFan1SpeedRpm | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0E4169A5-1218-49BD-8A87-877B274ADC9A | 0.0000 | NULL | NULL | NULL | 2025-09-16T15:26:29.7270000 | 2026-08-31T10:35:09.7830000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.RM_WRM_Data.EquipmentID` -> `XStudio_XBatch.RM_WRM_Mst_Tbl.ID` (Many to One)
