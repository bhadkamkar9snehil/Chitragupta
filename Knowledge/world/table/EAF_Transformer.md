---
type: table
title: "EAF_Transformer"
built: "2026-09-24T11:36:36"
---

# EAF_Transformer

Table in XStudio_Xbatch. Rows: 483.

## Identifiers it holds

- Attendant: same values as key `TechnicianName`
- HeatNo: same values as key `HeatNo`
- TapChangerCounter: same values as key `EAFTransformerTapChangerReading`

## Written by

- Xstudio_EAF_Transformer_USP

## Read by

- Xstudio_EAF_Transformer_USP

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
- TransformerCurver int
- PowerMW decimal
- TapChangerCounter int
- VCBCounter int
- OilTemperature int
- MainTank int
- TapChanger int
- Phase1B7A int
- Phase2B7B int
- Phase3B7C int
- HVBushingTemperature1U decimal
- HVBushingTemperature1V decimal
- HVBushingTemperature1W decimal
- HVBushingReactorU1 decimal
- HVBushingReactorU2 decimal
- HVBushingReactorV1 decimal
- HVBushingReactorV2 decimal
- HVBushingReactorW1 decimal
- HVBushingReactorW2 decimal
- LVTubeTemperature2UE1 decimal
- LVTubeTemperature2VE2 decimal
- LVTubeTemperature2WE3 decimal
- SecFlexibleTemperature2UE1 decimal
- SecFlexibleTemperature2VE2 decimal
- SecFlexibleTemperature2WE3 decimal
- OilFlowRunningCooler1 decimal
- OilFlowRunningCooler2 decimal
- WaterFlowm3perhrCooler1 decimal
- WaterFlowm3perhrCooler2 decimal
- BreatherStatusTransformer bit
- BreatherStatusTapChanger bit
- Remarks varchar(100)
- Attendant varchar(36)
- Shift varchar(100)
