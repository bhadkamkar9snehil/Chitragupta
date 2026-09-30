---
type: view
title: "Vw_ElectricalBShiftReport"
built: "2026-09-24T11:36:36"
---

# Vw_ElectricalBShiftReport

View in XStudio_Xbatch. Rows: unknown.

## Identifiers it holds

- EAFSeriesReactorTapChangerReading: same values as key `EAFSeriesReactorTapChangerReading`
- EAFTransformerTapChangerReading: same values as key `EAFTransformerTapChangerReading`
- LRFTransformerTapChangerReading: same values as key `LRFTransformerTapChangerReading`

## Reads

- Electrical_Shift_B_Check_List

## Columns

- ID varchar(36)
- ModifiedOn datetime
- IsDeleted bit
- IsSystem bit
- AssignedUserID varchar(36)
- HostAddress varchar(100)
- DbSyncStatus varchar(500)
- MobileSyncStatus varchar(100)
- Source varchar(20)
- EntryDateTime datetime
- ReportDate date
- IsProcessed varchar(6)
- EAFTransformerTapChangerReading int
- EAFSeriesReactorTapChangerReading int
- LRFTransformerTapChangerReading int
- BoosterFanMotorCurrent varchar(100)
- BoosterFanMotorSpeed varchar(100)
- IDFanMotor1Current varchar(100)
- IDFanMotor1Speed varchar(100)
- IDFanMotor2Current varchar(100)
- IDFanMotor2Speed varchar(100)
- IDFanMotor3Current varchar(100)
- IDFanMotor3Speed varchar(100)
- IDFanMotor4Current varchar(100)
- IDFanMotor4Speed varchar(100)
- BagHouse1PulsingOperation varchar(6)
- BagHouse2PulsingOperation varchar(6)
- BagHouse1StackEmissionAvgReadingNumber int
- BagHouse1StackEmissionAvgReadingText varchar(100)
- BagHouse2StackEmissionAvgReadingDecimal decimal
- BagHouse2StackEmissionAvgReadingText varchar(100)
- Checkforanyabnormalityin66kVRoom1 varchar(6)
- CheckforanyabnormalityinLVRoom1 varchar(6)
- BatteryChargingOPVoltageandCurrentRoom1 int
- BatteryElectrolyteLevelRoom1 varchar(6)
- CapacitorBankStatus400kVAr decimal
- CapacitorBankStatus800kVAr decimal
- ACStatusRoom1 varchar(6)
- FirExtinguisherStatusRoom1 varchar(6)
- HouseKeepingRoom1 varchar(6)
- Checkforanyabnormalityin66kVRoom2 varchar(6)
- CheckforanyabnormalityinLVRoom2 varchar(6)
- CapacitorBankStatus1000kVAr decimal
- ACStatusRoom2 varchar(10)
- FireExtinguisherStatusRoom2 varchar(6)
- HouseKeepingRoom2 varchar(6)
- Checkforanyabnormalityin66kVRoom3 varchar(6)
- CheckforanyabnormalityinLVRoom3 varchar(6)
- CapacitorBankStatus300kVAr varchar(6)
- CapacitorBankStatus300kVArNumber decimal
- ACStatusRoom3 varchar(6)
- FireExtinguisherStatusRoom3 varchar(6)
- HouseKeepingRoom3 varchar(6)
- Checkforanyabnormalityin66kVRoom4 varchar(6)
- CheckforanyabnormalityinLVRoom4 varchar(6)
- BatteryChargingOPVoltageandCurrentRoom4 int
- BatteryElectrolyteLevelRoom4 varchar(6)
- ACStatusRoom4 varchar(6)
- FireExtinguisherStatusRoom4 varchar(6)
- HouseKeepingRoom4 varchar(6)
- Checkforanyabnormalityin66kVRoom5 varchar(6)
- CheckforanyabnormalityinDriveRoom5 varchar(6)
- BatteryChargingOPVoltageandCurrentRoom5 int
- BatteryChargingOPVoltageandCurrentDecimalRoom5 decimal
- ACStatusRoom5 varchar(6)
- FireExtinguisherStatusRoom5 varchar(6)
- HouseKeepingRoom5 varchar(6)
- CheckforanyabnormalityinDriveRoomMaterialHandling varchar(6)
- ACStatusMaterialHandling varchar(6)
- FireExtinguisherStatusMaterialHandling varchar(6)
- HouseKeepingMaterialHandling varchar(6)
- CheckforanyabnormalityinDrivePanelRoom1 varchar(6)
- ACStatusHotChargingRoom1 varchar(6)
- FireExtinguisherStatusHotChargingRoom1 varchar(6)
- HouseKeepingHotChargingRoom1 varchar(6)
- CheckforanyabnormalityinDrivePanelRoom2 varchar(6)
- ACStatusHotChargingRoom2 varchar(6)
- FireExtinguisherStatusHotChargingRoom2 varchar(6)
- HouseKeepingHotChargingRoom2 varchar(6)
- EAFTemperatureLance varchar(6)
- LRFTemperatureLance varchar(6)
- CCMTemperatureLance varchar(6)
- ScarpShearMachineMotorandPanelsStatus varchar(6)
- ScarpShearMachineSensorsandHMIStatus varchar(6)
- CopexMachineMotorandPanelsStatus varchar(6)
- CopexMachineSensorsandHMIStatus varchar(6)
- CopexMachineCoolingWaterTemperature decimal
- ShedLightingIlluminationatScarpYard varchar(6)
- ShedLightingIlluminationatTeemingBay varchar(6)
- ShedLightingIlluminationatCastingBay varchar(6)
- ShedLightingIlluminationatBilletBay varchar(6)
- SampleConveyorSystemStatus varchar(6)
- EAFCarbonInjectionMachineStatus varchar(6)
- EAFFieldLimitSwitchesandSensorStatus varchar(6)
- EAFWaterFlowMetersStatus varchar(6)
- EAFBottomRTDsStatus varchar(6)
- EAFShellRTDsStatus varchar(6)
- LRFFieldLimitSwitchesandSensorStatus varchar(6)
- LRFWaterFlowMetersStatus varchar(6)
- LRFRTDsStatus varchar(6)
- MaterialHandlingSystemFieldSensorsStatus varchar(6)
- MaterialHandlingSystemFieldLSWsStatus varchar(6)
- MHSWeighingSystemStatus varchar(6)
- LadleTransferCarWeighingSystemStatus varchar(6)
- CCMTurretWeighingSystemStatus varchar(6)
- CCMTundishCar1and2WeighingSystemStatus varchar(6)
- EAFLFandSpectroUPSStatus varchar(6)
- MHSandHCCCMUPSStatus varchar(6)
- SubStationandECR2AUPSStatus varchar(6)
- HBIDRIandECR3AUPSStatus varchar(6)
- O2PlantandSVCPUPSStatus varchar(6)
- CapacitorStatusECR4A1000kvarRoom4 varchar(6)
- CapacitorStatusECR4A1000kVArRoom2 varchar(6)
- CapacitorBankStatus1000kVArRoom4 decimal
- BatteryChargingOPCurrentRoom4 int
- BatteryChargingOPCurrentRoom1 int
- CapacitorBankStatusThreeA800kvarBool varchar(6)
- CapacitorStatusECR41000kvarRoom4 varchar(6)
- CapacitorStatusECR21000Kvar varchar(6)
- CapacitorBankStatus400KvarECR1 varchar(6)
- CapacitorBankStatus800KvarECR1 varchar(6)
- CapacitorBankStatusThreeA800kvar decimal
- NOofHeatTapped int
- NameofEngineers varchar(8000)
- NameofElectrician varchar(8000)
- ContractManpower varchar(8000)
- Date datetime
