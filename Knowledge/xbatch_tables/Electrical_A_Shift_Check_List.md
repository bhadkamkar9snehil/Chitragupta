# XStudio_Xbatch.dbo.Electrical_A_Shift_Check_List

**table_kind:** production_data

### What this table is for

- **Indexed under investigation keywords:** catalog, entities, entity, from, highlights, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference remark, status, air, compressor, motor, motors, controller, pump, panel, scrap, motorsand, sensors.

**Primary Key:** ID  
**Row Count:** 238  
**Date Range (ModifiedOn):** 2025-07-23T14:48:50.0000000 to 2026-09-02T08:15:14.0000000  

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
| EAFTransformerOilTemperature | decimal | YES | 18,4 | — |
| EAFTransformerOilLevel | decimal | YES | 18,4 | — |
| EAFTransformerWindingTemperature | varchar | YES | 100 | — |
| EAFTransformerCoolingWaterFlow | decimal | YES | 18,4 | — |
| EAFTransformerTapChangerReading | decimal | YES | 18,4 | — |
| SeriesReactorOilTemperature | decimal | YES | 18,4 | — |
| SeriesReactorOilLevel | decimal | YES | 18,4 | — |
| SeriesReactorCoolingWaterFlow | decimal | YES | 18,4 | — |
| SeriesReactorTapChangerReading | decimal | YES | 18,4 | — |
| VCBPanelstatus33Kv | bit | YES | — | — |
| EAFFireExtinguisherStatus | bit | YES | — | — |
| EAFHouseKeeping | bit | YES | — | — |
| LRFTransformerOilTemperature | decimal | YES | 18,4 | — |
| LRFTransformerOilLevel | decimal | YES | 18,4 | — |
| LRFTransformerWindingTemperature | varchar | YES | 100 | — |
| LRFTransformerCoolingWaterFlow | decimal | YES | 18,4 | — |
| LRFTransformerTapChangerReading | decimal | YES | 18,4 | — |
| VaccumSwitchesStatus | bit | YES | — | — |
| SurgeCounterReadingRYBWeekly | bit | YES | — | — |
| LRFFireExtinguisherStatus | bit | YES | — | — |
| LRFHouseKeeping | bit | YES | — | — |
| LadleTransferCarWeighingSystemStatus | bit | YES | — | — |
| IDFanMotor1Current | varchar | YES | 100 | — |
| IDFanMotor2Current | varchar | YES | 100 | — |
| IDFanMotor3Current | varchar | YES | 100 | — |
| IDFanMotor4Current | varchar | YES | 100 | — |
| BagHouse1PulsingOperation | bit | YES | — | — |
| BagHouse2PulsingOperation | bit | YES | — | — |
| BagHouse1StackEmissionAvgReading | decimal | YES | 18,4 | — |
| BagHouse2StackEmissionAvgReading | decimal | YES | 18,4 | — |
| FESFireExtinguisherStatus | bit | YES | — | — |
| FESHouseKeeping | bit | YES | — | — |
| TurretTundishCarWeighingSystems | bit | YES | — | — |
| AMLCCamerasMonitorsandJBs | bit | YES | — | — |
| MouldandSprayCoolingInstruments | bit | YES | — | — |
| MouldOscillatorMotorsStatus | bit | YES | — | — |
| WithdrawlPinchRollMotorsStatus | bit | YES | — | — |
| BilletShearMotorsandSensorsStatus | bit | YES | — | — |
| RollerTableMotorsStatus | bit | YES | — | — |
| HMDsStatus | bit | YES | — | — |
| BilletLifterPusherLimitSwitchesStatus | bit | YES | — | — |
| CrossTransferLimitSwitchesStatus | bit | YES | — | — |
| HotChargingRollerTableMotorsStatus | bit | YES | — | — |
| HCTurnTable12MatorsStatus | bit | YES | — | — |
| HCFieldLimitSwitchesSensorsStatus | bit | YES | — | — |
| FurnaceCoolingwaterPumpMotors | varchar | YES | 100 | — |
| EAFDuctCoolingWaterPumpMotors | varchar | YES | 100 | — |
| TransformerCoolingwaterPumpMotors | varchar | YES | 100 | — |
| ElectricalEquipmentsCWPumpMotors | varchar | YES | 100 | — |
| MechnicalEquipmentsCWPumpMotors | varchar | YES | 100 | — |
| CCMMouldCoolingWaterPumpMotors | varchar | YES | 100 | — |
| CCMMachineCoolingWaterPumpMotors | varchar | YES | 100 | — |
| CCMSorayCoolingWaterPumpMotors | varchar | YES | 100 | — |
| CoolingTower12Motors | varchar | YES | 100 | — |
| SVCCoolingWaterPumpMotors | decimal | YES | 18,4 | — |
| OxygenPlant12CWPumpMotors | varchar | YES | 100 | — |
| EmergencyDGPump | varchar | YES | 100 | — |
| EmergencyWaterTankLevel | varchar | YES | 100 | — |
| Operatorfeedback | varchar | YES | 100 | — |
| PumpDG1BatteryVoltage | varchar | YES | 100 | — |
| PumpDG2BatteryVoltage | varchar | YES | 100 | — |
| PumpDG1ControlPanelSelectorSwitchPosition | varchar | YES | 100 | — |
| PumpDG2ControlPanelSelectorSwitchPosition | varchar | YES | 100 | — |
| PumpDG1DG2MainOutGoingMCCBON | bit | YES | — | — |
| PumpSynchronousPanelSelectorSwitchPostion | varchar | YES | 100 | — |
| SMSDG1BatteryVoltage | varchar | YES | 100 | — |
| SMSDG2BatteryVoltage | varchar | YES | 100 | — |
| SMSDG3BatteryVoltage | varchar | YES | 100 | — |
| SMSDG1ControlPanelSelectorSwitchPosition | varchar | YES | 100 | — |
| SMSDG2ControlPanelSelectorSwitchPosition | varchar | YES | 100 | — |
| SMSDG3ControlPanelSelectorSwitchPosition | varchar | YES | 100 | — |
| SMSDG12DG3MainOutGoingMCCBON | bit | YES | — | — |
| SMSSynchronousPanelSelectorSwitchPostion | varchar | YES | 100 | — |
| EAF | varchar | YES | 100 | — |
| LRF | varchar | YES | 100 | — |
| CCM | varchar | YES | 100 | — |
| MotorsandPanels1 | bit | YES | — | — |
| InstrumentsandSensors1 | bit | YES | — | — |
| Heaters1 | bit | YES | — | — |
| MotorsandPanels2 | bit | YES | — | — |
| InstrumentsandSensors2 | bit | YES | — | — |
| Heaters2 | bit | YES | — | — |
| AirCompressor1Motor | bit | YES | — | — |
| AirCompressor2Motor | bit | YES | — | — |
| AirCompressor3Motor | bit | YES | — | — |
| AirCompressor4Motor | bit | YES | — | — |
| AirCompressor5Motor | bit | YES | — | — |
| AirCompressor6Motor | bit | YES | — | — |
| AirCompressor1Controller | bit | YES | — | — |
| AirCompressor2Controller | bit | YES | — | — |
| AirCompressor3Controller | bit | YES | — | — |
| AirCompressor4Controller | bit | YES | — | — |
| AirCompressor5Controller | bit | YES | — | — |
| AirCompressor6Controller | bit | YES | — | — |
| ScrapDieselTrolley1PanelSensorStatus | bit | YES | — | — |
| ScrapDieselTrolley2PanelSensorStatus | bit | YES | — | — |
| ScrapDieselTrolley3PanelSensorStatus | bit | YES | — | — |
| ScrapYard1WeighingSystemStatus | bit | YES | — | — |
| ScrapYard2WeighingSystemStatus | bit | YES | — | — |
| ScrapShearMachineMotorsandPanelsStatus | bit | YES | — | — |
| ScrapShearMachineSensorsHMIStatus | bit | YES | — | — |
| CopexMachineMotorsandPanelsStatus | bit | YES | — | — |
| CopexMachineSensorsHMIStatus | bit | YES | — | — |
| CopexMachineCoolingwaterTemperature | decimal | YES | 18,4 | — |
| MotorsandStartersPanelStatus | bit | YES | — | — |
| FieldSafetySonsorsFunctionalty | bit | YES | — | — |
| NOofHeatsTapped | int | YES | 10,0 | — |
| BoosterFanMotorCurrent | varchar | YES | 100 | — |
| NameofShiftEngineers | varchar | YES | -1 | — |
| NameofShiftELectricians | varchar | YES | -1 | — |
| NameGEngineers | varchar | YES | -1 | — |
| NameGElectricians | varchar | YES | -1 | — |
| ContractManpower | varchar | YES | -1 | — |
| AirCompressor1ControllerRemark | varchar | YES | 100 | — |
| AirCompressor1MotorRemark | varchar | YES | 100 | — |
| AirCompressor2ControllerRemark | varchar | YES | 100 | — |
| AirCompressor2MotorRemark | varchar | YES | 100 | — |
| AirCompressor3ControllerRemark | varchar | YES | 100 | — |
| AirCompressor3MotorRemark | varchar | YES | 100 | — |
| AirCompressor4ControllerRemark | varchar | YES | 100 | — |
| AirCompressor4MotorRemark | varchar | YES | 100 | — |
| AirCompressor5ControllerRemark | varchar | YES | 100 | — |
| AirCompressor5MotorRemark | varchar | YES | 100 | — |
| AirCompressor6ControllerRemark | varchar | YES | 100 | — |
| AirCompressor6MotorRemark | varchar | YES | 100 | — |
| AMLCCamerasMonitorsandJBsRemark | varchar | YES | 100 | — |
| BagHouse1PulsingOperationRemark | varchar | YES | 100 | — |
| BagHouse2PulsingOperationRemark | varchar | YES | 100 | — |
| BilletLifterPusherLimitSwitchesStatusRemark | varchar | YES | 100 | — |
| BilletShearMotorsandSensorsStatusRemark | varchar | YES | 100 | — |
| CopexMachineMotorsandPanelsStatusRemark | varchar | YES | 100 | — |
| CopexMachineSensorsHMIStatusRemark | varchar | YES | 100 | — |
| CrossTransferLimitSwitchesStatusRemark | varchar | YES | 100 | — |
| EAFFireExtinguisherStatusRemark | varchar | YES | 100 | — |
| EAFHouseKeepingRemark | varchar | YES | 100 | — |
| FESFireExtinguisherStatusRemark | varchar | YES | 100 | — |
| FESHouseKeepingRemark | varchar | YES | 100 | — |
| FieldSafetySonsorsFunctionaltyRemark | varchar | YES | 100 | — |
| HCFieldLimitSwitchesSensorsStatusRemark | varchar | YES | 100 | — |
| HCTurnTable12MatorsStatusRemark | varchar | YES | 100 | — |
| Heaters1Remark | varchar | YES | 100 | — |
| Heaters2Remark | varchar | YES | 100 | — |
| HMDsStatusRemark | varchar | YES | 100 | — |
| HotChargingRollerTableMotorsStatusRemark | varchar | YES | 100 | — |
| InstrumentsandSensors1Remark | varchar | YES | 100 | — |
| InstrumentsandSensors2Remark | varchar | YES | 100 | — |
| IsProcessedRemark | varchar | YES | 100 | — |
| LadleTransferCarWeighingSystemStatusRemark | varchar | YES | 100 | — |
| LRFFireExtinguisherStatusRemark | varchar | YES | 100 | — |
| LRFHouseKeepingRemark | varchar | YES | 100 | — |
| MotorsandPanels1Remark | varchar | YES | 100 | — |
| MotorsandPanels2Remark | varchar | YES | 100 | — |
| MotorsandStartersPanelStatusRemark | varchar | YES | 100 | — |
| MouldandSprayCoolingInstrumentsRemark | varchar | YES | 100 | — |
| MouldOscillatorMotorsStatusRemark | varchar | YES | 100 | — |
| PumpDG1DG2MainOutGoingMCCBONRemark | varchar | YES | 100 | — |
| RollerTableMotorsStatusRemark | varchar | YES | 100 | — |
| ScrapDieselTrolley1PanelSensorStatusRemark | varchar | YES | 100 | — |
| ScrapDieselTrolley2PanelSensorStatusRemark | varchar | YES | 100 | — |
| ScrapDieselTrolley3PanelSensorStatusRemark | varchar | YES | 100 | — |
| ScrapShearMachineMotorsandPanelsStatusRemark | varchar | YES | 100 | — |
| ScrapShearMachineSensorsHMIStatusRemark | varchar | YES | 100 | — |
| ScrapYard1WeighingSystemStatusRemark | varchar | YES | 100 | — |
| ScrapYard2WeighingSystemStatusRemark | varchar | YES | 100 | — |
| SMSDG12DG3MainOutGoingMCCBONRemark | varchar | YES | 100 | — |
| SurgeCounterReadingRYBWeeklyRemark | varchar | YES | 100 | — |
| TurretTundishCarWeighingSystemsRemark | varchar | YES | 100 | — |
| VaccumSwitchesStatusRemark | varchar | YES | 100 | — |
| VCBPanelstatus33KvRemark | varchar | YES | 100 | — |
| WithdrawlPinchRollMotorsStatusRemark | varchar | YES | 100 | — |
| BoosterFanMotorSpeed | varchar | YES | 100 | — |
| IDFanMotor1Speed | varchar | YES | 100 | — |
| IDFanMotor2Speed | varchar | YES | 100 | — |
| IDFanMotor3Speed | varchar | YES | 100 | — |
| IDFanMotor4Speed | varchar | YES | 100 | — |
| PumpDG1BatteryElectrolyteLevel | varchar | YES | 100 | — |
| PumpDG2BatteryElectrolyteLevel | varchar | YES | 100 | — |
| SMSDG2BatteryElectrolyteLevel | varchar | YES | 100 | — |
| SMSDG1BatteryElectrolyteLevel | varchar | YES | 100 | — |
| SMSDG3BatteryElectrolyteLevel | varchar | YES | 100 | — |
| LadleCarMotorLimitSwitch | bit | YES | — | — |
| LadleCarMotorLimitSwitchRemarks | varchar | YES | 100 | — |
| AirCompressor7Motor | bit | YES | — | — |
| AirCompressor7MotorRemarks | varchar | YES | 100 | — |
| AirCompressor7Controller | bit | YES | — | — |
| AirCompressor7ControllerRemarks | varchar | YES | 100 | — |
| AirCompressor8Controller | bit | YES | — | — |
| AirCompressor8ControllerRemarks | varchar | YES | 100 | — |
| AirCompressor8Motor | bit | YES | — | — |
| AirCompressor8MotorRemarks | varchar | YES | 100 | — |

### Top 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 640452EA-3A4E-4CEA-BC63-5AE8627E93BD | NULL | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 3ADE6546-3C9A-49C4-A001-234025F2F901 | 2025-07-23T11:44:32.0200000 | 2025-07-23T14:48:50.0000000 | False | False | NULL |
| D8AC8478-CFB4-4B6F-AB83-01E7D84E4136 | NULL | NULL | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | C9710FC1-E4FF-4FDC-991A-A1B54F059E59 | 2025-08-02T10:12:55.4000000 | 2025-08-02T10:14:06.0000000 | False | False | NULL |
| 1140D098-B0BC-467D-8BC0-2B006B135401 | NULL | NULL | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 14686A56-A210-4ECA-8D19-FA0FCB95EC0E | 2025-09-28T12:25:06.4830000 | 2025-09-28T12:25:06.0000000 | False | False | NULL |
| F7407F0E-EBA3-41A9-944B-55D9D55F5907 | NULL | NULL | 83E3F386-31EE-476F-9651-39B924B01514 | 83E3F386-31EE-476F-9651-39B924B01514 | 2025-10-31T09:18:15.9230000 | 2025-10-31T09:21:08.0000000 | False | False | NULL |
| D61EA5D1-1D65-44AB-95E4-13F3198CC944 | NULL | NULL | 83E3F386-31EE-476F-9651-39B924B01514 | 83E3F386-31EE-476F-9651-39B924B01514 | 2025-11-02T09:38:49.4670000 | 2025-11-02T09:43:40.0000000 | False | False | NULL |
| 56D0027A-2D0E-4FAC-B5F6-83205D9B393D | NULL | NULL | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 83E3F386-31EE-476F-9651-39B924B01514 | 2025-11-04T11:11:21.2900000 | 2025-11-04T16:59:41.0000000 | False | False | NULL |
| CF8E4672-CC1C-4E2A-A175-CDF7A93152A6 | NULL | NULL | 83E3F386-31EE-476F-9651-39B924B01514 | 83E3F386-31EE-476F-9651-39B924B01514 | 2025-11-01T08:33:26.8770000 | 2025-11-05T12:30:02.0000000 | False | False | NULL |
| 5EB16BDE-C242-46B1-A01D-E23FADECBEDD | NULL | NULL | D10B9DCF-718A-4AB4-A7AD-97FC97D77E26 | 83E3F386-31EE-476F-9651-39B924B01514 | 2025-11-06T07:50:39.5730000 | 2025-11-06T13:54:14.0000000 | False | False | NULL |
| 4231E13A-3281-4619-89FF-8FE80B59FB08 | NULL | NULL | 969C5F05-2376-479F-B8F6-BA23EFF1DE90 | F3334E28-CABA-4154-903B-3B1355F07CF8 | 2025-08-02T11:47:04.5570000 | 2025-11-11T21:01:08.0000000 | False | False | NULL |
| CF2CFBAE-CCCC-49DF-98D2-4C4E3C27A121 | NULL | NULL | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2025-11-15T08:46:30.5130000 | 2025-11-15T09:28:31.0000000 | False | False | NULL |

### Bottom 10 Records

| ID | Name | ParentID | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 73D08AC7-D4E0-4A50-80E4-F3630F1C0199 | NULL | NULL | CBBFAA1E-3335-4C50-9219-32DC0D534F31 | CBBFAA1E-3335-4C50-9219-32DC0D534F31 | 2026-09-02T08:15:14.9500000 | 2026-09-02T08:15:14.0000000 | False | False | NULL |
| 9A231AD8-DB17-4DBE-984F-896A5E313646 | NULL | NULL | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 5E9CB28C-0C5A-443F-A2D2-39C496788735 | 2026-09-01T07:56:46.8330000 | 2026-09-01T07:56:46.0000000 | False | False | NULL |
| 15909225-9430-45F0-A4BB-0C1F44DFDE63 | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-08T07:40:17.5770000 | 2026-07-08T17:51:09.0000000 | False | False | NULL |
| 686F9D69-CB1B-49B7-ADCD-2DEC5945359E | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-07T07:50:11.9530000 | 2026-07-07T17:31:59.0000000 | False | False | NULL |
| 03A46145-9637-426B-A4D4-06FD97694722 | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-05T08:02:56.2700000 | 2026-07-06T12:51:50.0000000 | False | False | NULL |
| AD6A0BDF-BF8D-4FBB-AB9A-09102E9C4D1B | NULL | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-05T07:43:03.0170000 | 2026-07-06T12:49:21.0000000 | False | False | NULL |
| F0D4880E-C055-4EB2-A851-5B5F224EBFD0 | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-06T07:43:55.7700000 | 2026-07-06T11:40:38.0000000 | False | False | NULL |
| 0A43B216-E16B-44FB-AF00-1547F3DA127B | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-04T07:41:15.3300000 | 2026-07-04T07:57:14.0000000 | False | False | NULL |
| 3FD6C0B3-D18C-4DDB-989A-2A7904D3B028 | NULL | NULL | C2500F49-167C-4DAA-A825-049801878F93 | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | 2026-07-03T07:59:20.0300000 | 2026-07-03T08:04:41.0000000 | False | False | NULL |
| 844FDE78-FCA1-445A-B6AC-D83BB50B86F1 | NULL | NULL | E21F8C9A-2293-4D0C-BDB3-35B89330ACE1 | C2500F49-167C-4DAA-A825-049801878F93 | 2026-07-02T07:40:39.7500000 | 2026-07-02T17:29:03.0000000 | False | False | NULL |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Electrical_A_Shift_Check_List.ContractManpower` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Electrical_A_Shift_Check_List.NameGElectricians` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Electrical_A_Shift_Check_List.NameGEngineers` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Electrical_A_Shift_Check_List.NameofShiftELectricians` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
- `XStudio_XBatch.Electrical_A_Shift_Check_List.NameofShiftEngineers` -> `XStudio_Configuration_XBatch.XStudio_User_Mst_Tbl.ID` (Many to One)
