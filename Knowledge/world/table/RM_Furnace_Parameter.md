---
type: table
title: "RM_Furnace_Parameter"
built: "2026-09-24T11:36:36"
---

# RM_Furnace_Parameter

Table in XStudio_Xbatch. Rows: 8,185.

## Written by

- SP_ReCalculate_RM_Furnace_Block_USP (text)
- Xstudio_Historian_RM_Furnace_Logbook_Block_usp (text)
- Xstudio_RM_Furnace_Parameter_USP

## Read by

- Xstudio_RM_Furnace_Parameter_USP

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
- Shift varchar(100)
- OperatorName varchar(36)
- ProductDia varchar(100)
- BilletLength int
- PreheatingTopZone1TempSet decimal
- PreheatingTopZone1TempActual decimal
- PreheatingBottomZone2TempActual decimal
- PreheatingBottomZone2TempSet decimal
- HeatingTopBottomZone3TempSet decimal
- HeatingTopBottomZone3TempActual decimal
- HeatingBottomZone4TempActual decimal
- HeatingBottomZone4TempSet decimal
- SoakingTopLeftZone5TempSet decimal
- SoakingTopLeftZone5TempActual decimal
- SoakingTopRightZone6TempActual decimal
- SoakingTopRightZone6TempSet decimal
- SoakingBottomLeftZone7TempSet decimal
- SoakingBottomLeftZone7TempActual decimal
- SoakingBottomRightZone8TempActual decimal
- SoakingBottomRightZone8TempSet decimal
- RecuperatorAirOutletTemp decimal
- RecuperatorFlueGasInletTemp decimal
- RecuperatorFlueGasOutletTemp decimal
- RecuperatorDamperPosition decimal
- PressuremmWCCombustionAirSet decimal
- PressuremmWCCombustionAirActual decimal
- PressuremmWCNaturalGasBeforePRV decimal
- PressuremmWCNaturalGasAfterPRV decimal
- PressureFurnaceSet decimal
- PressureFurnaceActual decimal
- Remarks varchar(-1)
