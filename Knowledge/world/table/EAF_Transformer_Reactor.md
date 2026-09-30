---
type: table
title: "EAF_Transformer_Reactor"
built: "2026-09-24T11:36:36"
---

# EAF_Transformer_Reactor

Table in XStudio_Xbatch. Rows: 477.

## Identifiers it holds

- Attendant: same values as key `TechnicianName`
- HeatNo: same values as key `HeatNo`
- TapChangerCounter: same values as key `EAFSeriesReactorTapChangerReading`

## Written by

- Xstudio_EAF_Transformer_Reactor_USP

## Read by

- Xstudio_EAF_Transformer_Reactor_USP

## Columns

- ID varchar(36)
- Name varchar(100)
- ParentID varchar(36)
- CreatedBy varchar(36)
- ModifiedBy varchar(36)
- CreatedOn datetime
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
- IsProcessed bit
- HeatNo varchar(100)
- TapNo int
- TapChangerCounter int
- OilTremperature int
- OilLevelReactor int
- OilLevelTapChanger int
- DivertorTankTemperaturePhase1B7A int
- DivertorTankTemperaturePhase2B7B int
- DivertorTankTemperaturePhase3B7C int
- HVBushingTemperatureU1 decimal
- HVBushingTemperatureU2 decimal
- HVBushingTemperatureV1 decimal
- HVBushingTemperatureV2 decimal
- HVBushingTemperatureW1 decimal
- HVBushingTemperatureW2 decimal
- OilFlowRunningCooler1 decimal
- OilFlowRunningCooler2 decimal
- WaterFlowm3perhrCooler1 decimal
- WaterFlowm3perhrCooler2 decimal
- BreatherStatusTransformer bit
- BreatherStatusTapChanger bit
- Remarks varchar(100)
- Attendant varchar(36)
- Shift varchar(100)
