# XStudio_Xbatch.dbo.Electrical_Shift_B_Check_List

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** catalog, entities, entity, from, highlights, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference remark, status, room, checkforanyabnormalityin, capacitor, house, ecr, charging, acstatus, extinguisher, keeping, bank.

**Primary Key:** ID  
**Row Count:** 273  
**Date Range (ModifiedOn):** 2025-07-23T15:05:49.0000000 to 2026-09-01T22:15:07.0000000  

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
| EAFTransformerTapChangerReading | int | YES | 10,0 | — |
| EAFSeriesReactorTapChangerReading | int | YES | 10,0 | — |
| LRFTransformerTapChangerReading | int | YES | 10,0 | — |
| BoosterFanMotorCurrent | varchar | YES | 100 | — |
| IDFanMotor1Current | varchar | YES | 100 | — |
| IDFanMotor2Current | varchar | YES | 100 | — |
| IDFanMotor3Current | varchar | YES | 100 | — |
| IDFanMotor4Current | varchar | YES | 100 | — |
| BagHouse1PulsingOperation | bit | YES | — | — |
| BagHouse2PulsingOperation | bit | YES | — | — |
| BagHouse1StackEmissionAvgReadingNumber | int | YES | 10,0 | — |
| BagHouse1StackEmissionAvgReadingText | varchar | YES | 100 | — |
| BagHouse2StackEmissionAvgReadingDecimal | decimal | YES | 18,4 | — |
| BagHouse2StackEmissionAvgReadingText | varchar | YES | 100 | — |
| Checkforanyabnormalityin66kVRoom1 | bit | YES | — | — |
| CheckforanyabnormalityinLVRoom1 | bit | YES | — | — |
| BatteryChargingOPVoltageandCurrentRoom1 | int | YES | 10,0 | — |
| BatteryElectrolyteLevelRoom1 | bit | YES | — | — |
| CapacitorBankStatus400kVAr | decimal | YES | 18,4 | — |
| CapacitorBankStatus800kVAr | decimal | YES | 18,4 | — |
| ACStatusRoom1 | bit | YES | — | — |
| FirExtinguisherStatusRoom1 | bit | YES | — | — |
| HouseKeepingRoom1 | bit | YES | — | — |
| Checkforanyabnormalityin66kVRoom2 | bit | YES | — | — |
| CheckforanyabnormalityinLVRoom2 | bit | YES | — | — |
| CapacitorBankStatus1000kVAr | decimal | YES | 18,4 | — |
| ACStatusRoom2 | bit | YES | — | — |
| FireExtinguisherStatusRoom2 | bit | YES | — | — |
| HouseKeepingRoom2 | bit | YES | — | — |
| Checkforanyabnormalityin66kVRoom3 | bit | YES | — | — |
| CheckforanyabnormalityinLVRoom3 | bit | YES | — | — |
| CapacitorBankStatus300kVAr | bit | YES | — | — |
| CapacitorBankStatus300kVArNumber | decimal | YES | 18,4 | — |
| ACStatusRoom3 | bit | YES | — | — |
| FireExtinguisherStatusRoom3 | bit | YES | — | — |
| HouseKeepingRoom3 | bit | YES | — | — |
| Checkforanyabnormalityin66kVRoom4 | bit | YES | — | — |
| CheckforanyabnormalityinLVRoom4 | bit | YES | — | — |
| BatteryChargingOPVoltageandCurrentRoom4 | int | YES | 10,0 | — |
| BatteryElectrolyteLevelRoom4 | bit | YES | — | — |
| ACStatusRoom4 | bit | YES | — | — |
| FireExtinguisherStatusRoom4 | bit | YES | — | — |
| HouseKeepingRoom4 | bit | YES | — | — |
| Checkforanyabnormalityin66kVRoom5 | bit | YES | — | — |
| CheckforanyabnormalityinDriveRoom5 | bit | YES | — | — |
| BatteryChargingOPVoltageandCurrentRoom5 | int | YES | 10,0 | — |
| BatteryChargingOPVoltageandCurrentDecimalRoom5 | decimal | YES | 18,4 | — |
| ACStatusRoom5 | bit | YES | — | — |
| FireExtinguisherStatusRoom5 | bit | YES | — | — |
| HouseKeepingRoom5 | bit | YES | — | — |
| CheckforanyabnormalityinDriveRoomMaterialHandling | bit | YES | — | — |
| ACStatusMaterialHandling | bit | YES | — | — |
| FireExtinguisherStatusMaterialHandling | bit | YES | — | — |
| HouseKeepingMaterialHandling | bit | YES | — | — |
| CheckforanyabnormalityinDrivePanelRoom1 | bit | YES | — | — |
| ACStatusHotChargingRoom1 | bit | YES | — | — |
| FireExtinguisherStatusHotChargingRoom1 | bit | YES | — | — |
| HouseKeepingHotChargingRoom1 | bit | YES | — | — |
| CheckforanyabnormalityinDrivePanelRoom2 | bit | YES | — | — |
| ACStatusHotChargingRoom2 | bit | YES | — | — |
| FireExtinguisherStatusHotChargingRoom2 | bit | YES | — | — |
| HouseKeepingHotChargingRoom2 | bit | YES | — | — |
| EAFTemperatureLance | bit | YES | — | — |
| LRFTemperatureLance | bit | YES | — | — |
| CCMTemperatureLance | bit | YES | — | — |
| ScarpShearMachineMotorandPanelsStatus | bit | YES | — | — |
| ScarpShearMachineSensorsandHMIStatus | bit | YES | — | — |
| CopexMachineMotorandPanelsStatus | bit | YES | — | — |
| CopexMachineSensorsandHMIStatus | bit | YES | — | — |
| CopexMachineCoolingWaterTemperature | decimal | YES | 18,4 | — |
| ShedLightingIlluminationatScarpYard | bit | YES | — | — |
| ShedLightingIlluminationatTeemingBay | bit | YES | — | — |
| ShedLightingIlluminationatCastingBay | bit | YES | — | — |
| ShedLightingIlluminationatBilletBay | bit | YES | — | — |
| SampleConveyorSystemStatus | bit | YES | — | — |
| EAFCarbonInjectionMachineStatus | bit | YES | — | — |
| EAFFieldLimitSwitchesandSensorStatus | bit | YES | — | — |
| EAFWaterFlowMetersStatus | bit | YES | — | — |
| EAFBottomRTDsStatus | bit | YES | — | — |
| EAFShellRTDsStatus | bit | YES | — | — |
| LRFFieldLimitSwitchesandSensorStatus | bit | YES | — | — |
| LRFWaterFlowMetersStatus | bit | YES | — | — |
| LRFRTDsStatus | bit | YES | — | — |
| MaterialHandlingSystemFieldSensorsStatus | bit | YES | — | — |
| MaterialHandlingSystemFieldLSWsStatus | bit | YES | — | — |
| MHSWeighingSystemStatus | bit | YES | — | — |
| LadleTransferCarWeighingSystemStatus | bit | YES | — | — |
| CCMTurretWeighingSystemStatus | bit | YES | — | — |
| CCMTundishCar1and2WeighingSystemStatus | bit | YES | — | — |
| EAFLFandSpectroUPSStatus | bit | YES | — | — |
| MHSandHCCCMUPSStatus | bit | YES | — | — |
| SubStationandECR2AUPSStatus | bit | YES | — | — |
| HBIDRIandECR3AUPSStatus | bit | YES | — | — |
| O2PlantandSVCPUPSStatus | bit | YES | — | — |
| CapacitorBankStatus1000kVArRoom4 | decimal | YES | 18,4 | — |
| NOofHeatTapped | int | YES | 10,0 | — |
| NameofEngineers | varchar | YES | -1 | — |
| NameofElectrician | varchar | YES | -1 | — |
| ContractManpower | varchar | YES | -1 | — |
| Date | datetime | YES | — | — |
| ACStatusHotChargingRoom1Remark | varchar | YES | 100 | — |
| ACStatusHotChargingRoom2Remark | varchar | YES | 100 | — |
| ACStatusMaterialHandlingRemark | varchar | YES | 100 | — |
| ACStatusRoom1Remark | varchar | YES | 100 | — |
| ACStatusRoom2Remark | varchar | YES | 100 | — |
| ACStatusRoom3Remark | varchar | YES | 100 | — |
| ACStatusRoom4Remark | varchar | YES | 100 | — |
| ACStatusRoom5Remark | varchar | YES | 100 | — |
| BagHouse1PulsingOperationRemark | varchar | YES | 100 | — |
| BagHouse2PulsingOperationRemark | varchar | YES | 100 | — |
| BatteryElectrolyteLevelRoom1Remark | varchar | YES | 100 | — |
| BatteryElectrolyteLevelRoom4Remark | varchar | YES | 100 | — |
| CapacitorBankStatus300kVArRemark | varchar | YES | 100 | — |
| CCMTemperatureLanceRemark | varchar | YES | 100 | — |
| CCMTundishCar1and2WeighingSystemStatusRemark | varchar | YES | 100 | — |
| CCMTurretWeighingSystemStatusRemark | varchar | YES | 100 | — |
| Checkforanyabnormalityin66kVRoom1Remark | varchar | YES | 100 | — |
| Checkforanyabnormalityin66kVRoom2Remark | varchar | YES | 100 | — |
| Checkforanyabnormalityin66kVRoom3Remark | varchar | YES | 100 | — |
| Checkforanyabnormalityin66kVRoom4Remark | varchar | YES | 100 | — |
| Checkforanyabnormalityin66kVRoom5Remark | varchar | YES | 100 | — |
| CheckforanyabnormalityinDrivePanelRoom1Remark | varchar | YES | 100 | — |
| CheckforanyabnormalityinDrivePanelRoom2Remark | varchar | YES | 100 | — |
| CheckforanyabnormalityinDriveRoom5Remark | varchar | YES | 100 | — |
| CheckforanyabnormalityinDriveRoomMaterialHandlingRemark | varchar | YES | 100 | — |
| CheckforanyabnormalityinLVRoom1Remark | varchar | YES | 100 | — |
| CheckforanyabnormalityinLVRoom2Remark | varchar | YES | 100 | — |
| CheckforanyabnormalityinLVRoom3Remark | varchar | YES | 100 | — |
| CheckforanyabnormalityinLVRoom4Remark | varchar | YES | 100 | — |
| CopexMachineMotorandPanelsStatusRemark | varchar | YES | 100 | — |
| CopexMachineSensorsandHMIStatusRemark | varchar | YES | 100 | — |
| EAFBottomRTDsStatusRemark | varchar | YES | 100 | — |
| EAFCarbonInjectionMachineStatusRemark | varchar | YES | 100 | — |
| EAFFieldLimitSwitchesandSensorStatusRemark | varchar | YES | 100 | — |
| EAFLFandSpectroUPSStatusRemark | varchar | YES | 100 | — |
| EAFShellRTDsStatusRemark | varchar | YES | 100 | — |
| EAFTemperatureLanceRemark | varchar | YES | 100 | — |
| EAFWaterFlowMetersStatusRemark | varchar | YES | 100 | — |
| FireExtinguisherStatusHotChargingRoom1Remark | varchar | YES | 100 | — |
| FireExtinguisherStatusHotChargingRoom2Remark | varchar | YES | 100 | — |
| FireExtinguisherStatusMaterialHandlingRemark | varchar | YES | 100 | — |
| FireExtinguisherStatusRoom2Remark | varchar | YES | 100 | — |
| FireExtinguisherStatusRoom3Remark | varchar | YES | 100 | — |
| FireExtinguisherStatusRoom4Remark | varchar | YES | 100 | — |
| FireExtinguisherStatusRoom5Remark | varchar | YES | 100 | — |
| FirExtinguisherStatusRoom1Remark | varchar | YES | 100 | — |
| HBIDRIandECR3AUPSStatusRemark | varchar | YES | 100 | — |
| HouseKeepingHotChargingRoom1Remark | varchar | YES | 100 | — |
| HouseKeepingHotChargingRoom2Remark | varchar | YES | 100 | — |
| HouseKeepingMaterialHandlingRemark | varchar | YES | 100 | — |
| HouseKeepingRoom1Remark | varchar | YES | 100 | — |
| HouseKeepingRoom2Remark | varchar | YES | 100 | — |
| HouseKeepingRoom3Remark | varchar | YES | 100 | — |
| HouseKeepingRoom4Remark | varchar | YES | 100 | — |
| HouseKeepingRoom5Remark | varchar | YES | 100 | — |
| IsProcessedRemark | varchar | YES | 100 | — |
| LadleTransferCarWeighingSystemStatusRemark | varchar | YES | 100 | — |
| LRFFieldLimitSwitchesandSensorStatusRemark | varchar | YES | 100 | — |
| LRFRTDsStatusRemark | varchar | YES | 100 | — |
| LRFTemperatureLanceRemark | varchar | YES | 100 | — |
| LRFWaterFlowMetersStatusRemark | varchar | YES | 100 | — |
| MaterialHandlingSystemFieldLSWsStatusRemark | varchar | YES | 100 | — |
| MaterialHandlingSystemFieldSensorsStatusRemark | varchar | YES | 100 | — |
| MHSandHCCCMUPSStatusRemark | varchar | YES | 100 | — |
| MHSWeighingSystemStatusRemark | varchar | YES | 100 | — |
| O2PlantandSVCPUPSStatusRemark | varchar | YES | 100 | — |
| SampleConveyorSystemStatusRemark | varchar | YES | 100 | — |
| ScarpShearMachineMotorandPanelsStatusRemark | varchar | YES | 100 | — |
| ScarpShearMachineSensorsandHMIStatusRemark | varchar | YES | 100 | — |
| ShedLightingIlluminationatBilletBayRemark | varchar | YES | 100 | — |
| ShedLightingIlluminationatCastingBayRemark | varchar | YES | 100 | — |
| ShedLightingIlluminationatScarpYardRemark | varchar | YES | 100 | — |
| ShedLightingIlluminationatTeemingBayRemark | varchar | YES | 100 | — |
| SubStationandECR2AUPSStatusRemark | varchar | YES | 100 | — |
| BoosterFanMotorSpeed | varchar | YES | 100 | — |
| IDFanMotor1Speed | varchar | YES | 100 | — |
| IDFanMotor2Speed | varchar | YES | 100 | — |
| IDFanMotor3Speed | varchar | YES | 100 | — |
| IDFanMotor4Speed | varchar | YES | 100 | — |
| BoosterFanMotorSpeedRPM | varchar | YES | 100 | — |
| IDFanMotor1SpeedRPM | varchar | YES | 100 | — |
| IDFanMotor2SpeedRPM | varchar | YES | 100 | — |
| IDFanMotor3SpeedRPM | varchar | YES | 100 | — |
| IDFanMotor4SpeedRPM | varchar | YES | 100 | — |
| BatteryChargingOPCurrentRoom4 | int | YES | 10,0 | — |
| BatteryChargingOPCurrentRoom1 | int | YES | 10,0 | — |
| CapacitorBankStatusThreeA800kvar | decimal | YES | 18,4 | — |
| CapacitorBankStatusThreeA800kvarBool | bit | YES | — | — |
| CapacitorBankStatusThreeA800kvarRemark | varchar | YES | 100 | — |
| CapacitorStatusECR41000kvarRoom4 | bit | YES | — | — |
| CapacitorStatusECR4A1000kvarRoom2 | bit | YES | — | — |
| CapacitorStatusECR4A1000kvarRoom2Remark | varchar | YES | 100 | — |
| CapacitorStatusECR2A1000kVar | decimal | YES | 18,4 | — |
| CapacitorStatusECR21000kVar | bit | YES | — | — |
| SubStationandECR2UPSStatusRemark | varchar | YES | 100 | — |
| SubStationandECR2UPSStatus | bit | YES | — | — |
| CapacitorBankStatusECR41000kVAr | decimal | YES | 18,4 | — |
| CapacitorStatusECR4A1000kvarRoom4 | bit | YES | — | — |
| CapacitorStatusECR21000KvarRemark | varchar | YES | 100 | — |
| CapacitorStatusECR21000KvarDecimal | decimal | YES | 18,4 | — |
| CapacitorStatusECR4A1000kvarRemark | varchar | YES | 100 | — |
| CapacitorStatusECR41000kvarRemark | varchar | YES | 100 | — |
| CapacitorBankStatus400KvarECR1 | bit | YES | — | — |
| CapacitorBankStatus400KvarECR1Remarks | varchar | YES | 100 | — |
| CapacitorBankStatus800KvarECR1 | bit | YES | — | — |
| CapacitorBankStatus800KvarECR1Remarks | varchar | YES | 100 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F7EAA82B-D0C6-4F1C-8FD4-0C25C47FCBCE | NULL | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-07-21T18:22:15.5670000 | 2025-07-23T15:05:49.0000000 | False | False | NULL |
| 88F8F2E3-DB4B-41D6-B721-B4464506524A | NULL | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-08-02T10:15:33.4170000 | 2025-08-02T10:15:33.0000000 | False | False | NULL |
| AFC1EE15-BB11-48FE-B2EA-25DA523936E1 | NULL | NULL | 969C5F05-2376-479F-B8F6-BA23EFF1DE90 | 969C5F05-2376-479F-B8F6-BA23EFF1DE90 | 2025-08-02T18:05:36.2530000 | 2025-08-02T18:05:36.0000000 | False | False | NULL |
| 90C0E267-071D-40ED-AD3D-45A29B2AA742 | NULL | NULL | 969C5F05-2376-479F-B8F6-BA23EFF1DE90 | 969C5F05-2376-479F-B8F6-BA23EFF1DE90 | 2025-08-07T03:05:15.4730000 | 2025-08-07T03:06:26.0000000 | False | False | NULL |
| C1930924-71C3-418F-8BAC-6779726EE2BD | NULL | NULL | 969C5F05-2376-479F-B8F6-BA23EFF1DE90 | 969C5F05-2376-479F-B8F6-BA23EFF1DE90 | 2025-08-16T22:02:57.3600000 | 2025-08-16T22:02:57.0000000 | False | False | NULL |
| B367CBC3-ABB8-4D5E-B885-39E9FD87F14A | NULL | NULL | 969C5F05-2376-479F-B8F6-BA23EFF1DE90 | 969C5F05-2376-479F-B8F6-BA23EFF1DE90 | 2025-08-17T19:42:44.4330000 | 2025-08-17T19:42:44.0000000 | False | False | NULL |
| A42F34DA-E6CC-444A-9B56-07A4EDC0E026 | NULL | NULL | 90FDFA67-A316-4D8C-90F0-5D819193E52E | 90FDFA67-A316-4D8C-90F0-5D819193E52E | 2025-09-19T18:01:16.6770000 | 2025-09-19T18:01:16.0000000 | False | False | NULL |
| A30C649A-A539-4F59-B3F4-BB26596AEA94 | NULL | NULL | 83E3F386-31EE-476F-9651-39B924B01514 | 83E3F386-31EE-476F-9651-39B924B01514 | 2025-11-01T21:11:51.7730000 | 2025-11-01T21:11:51.0000000 | False | False | NULL |
| 2EA0EE3A-8E7E-42BF-A99A-AE48612E782D | NULL | NULL | 83E3F386-31EE-476F-9651-39B924B01514 | 83E3F386-31EE-476F-9651-39B924B01514 | 2025-11-08T20:28:43.5800000 | 2025-11-08T20:28:43.0000000 | False | False | NULL |
| C7591C38-F440-4710-80F1-FF0EBC14C3D6 | NULL | NULL | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 2025-11-09T19:17:06.2430000 | 2025-11-09T19:35:05.0000000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7249FF9C-FCD9-438D-99EA-8308F593C9CF | NULL | NULL | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-09-01T22:15:07.2970000 | 2026-09-01T22:15:07.0000000 | False | False | NULL |
| 4199BDD0-B590-435F-8EEC-8D4F6FBEB0F8 | NULL | NULL | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-08-19T02:11:27.2030000 | 2026-08-19T02:14:35.0000000 | False | False | NULL |
| A1079A4B-CF78-45F1-8B35-83832E8AF54F | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-08T23:37:17.4830000 | 2026-07-09T00:52:41.0000000 | False | False | NULL |
| 53CE0FD0-D3BD-4D0A-8EA1-04201CCAE30A | NULL | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-01-27T23:28:33.5200000 | 2026-07-07T21:22:37.0000000 | False | False | NULL |
| 6E76A462-D827-4C74-8CBF-2BB312447FB5 | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-06T19:46:11.4700000 | 2026-07-06T19:54:26.0000000 | False | False | NULL |
| 5C0FDC95-2C1B-472D-A353-A4548305CC2F | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-07-04T20:19:34.2200000 | 2026-07-05T21:01:40.0000000 | False | False | NULL |
| 3DBE02DC-DDF2-4965-80DD-165A0B0989B9 | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | CBFAF584-0011-45B1-9D0F-02CBED97CCAA | 2026-07-05T19:37:01.3700000 | 2026-07-05T21:00:38.0000000 | False | False | NULL |
| 6257C3C3-E05D-482F-A390-E8682F4B01E2 | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-03T19:48:02.8270000 | 2026-07-04T01:53:48.0000000 | False | False | NULL |
| F86D9126-D503-41BF-8D9F-349AA385D68F | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-02T19:53:06.2530000 | 2026-07-02T20:05:29.0000000 | False | False | NULL |
| 194FAA76-2432-430D-BF63-26DC60C2C8A4 | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-07-01T20:07:56.1870000 | 2026-07-01T20:14:11.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Electrical_Shift_B_Check_List.ContractManpower` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Electrical_Shift_B_Check_List.NameofElectrician` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Electrical_Shift_B_Check_List.NameofEngineers` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
