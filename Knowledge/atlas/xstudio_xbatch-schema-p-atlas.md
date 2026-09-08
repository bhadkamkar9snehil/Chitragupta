---
type: Reference
database: XStudio_Xbatch
authority: static-advisory
---
# XStudio_Xbatch schema atlas: P

Static routing knowledge generated from the authoritative export. Current ticket facts require live SQL.

## dbo.PTW_Details
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EngineerName:varchar, PTWNO:decimal, Shift:varchar, Name:varchar, EntryDateTime:datetime, NOofPTWIssued:decimal, ReportDate:date, TechnicianName:varchar, ParentID:varchar, IsProcessed:bit

## dbo.Particulars_Masters
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ParentID:varchar, UOM:varchar, Type:varchar, SrNo:int, Name:varchar, ReportDate:datetime, Particulars:varchar

## dbo.Particulars_Masters_Audit
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ParentID:varchar, UOM:varchar, Type:varchar, SrNo:int, Name:varchar, ReportDate:datetime, Particulars:varchar

## dbo.Particulars_Masters_Trn
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, SrNo:int, Name:varchar, Particulars:varchar, Type:varchar, UOM:varchar, ReportDate:datetime, ParentID:varchar, EntryDateTime:datetime, IsProcessed:bit, Target:decimal

## dbo.Per_Heat_LadleNo
ID:varchar, HeatNo:int, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, LadleNo:varchar, LadleNoAtEAF:bit, LadleNoAtLRF:bit, LadleNoAtCCM:bit, EntryTime:datetime, LadleNoAtEAFDatetime:datetime, LadleNoAtLRFDatetime:datetime, LadleNoAtCCMDatetime:datetime, EAFShellNo:varchar, TundishNo:varchar

## dbo.Plant_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Location:varchar, Latitude:decimal, Longitude:decimal

## dbo.Plant_Name_MST
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Plant:varchar, AliasName:varchar, ColourCode:varchar

## dbo.Powe_Consumption_Report
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, Transformer132kv1:decimal, Transformer132kv2:decimal, Transformer33kv1:decimal, Transformer33kv2:decimal, EAF:decimal, LRF:decimal, Transformer24MVA:decimal, Transformer15MVA:decimal, RollingMill:decimal, WRM:decimal, OxygenPlant4A:decimal, NGConsumption:decimal, PlantTotal:decimal, SMSTotal:decimal, SMSAuxWithO2:decimal, SMSAuxWithoutO2:decimal, TotalRollingMill:decimal, Transformer125MVALosses:decimal, Transformer63MVALosses:decimal

## dbo.Powe_Consumption_Report_Audit
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, Transformer132kv1:decimal, Transformer132kv2:decimal, Transformer33kv1:decimal, Transformer33kv2:decimal, EAF:decimal, LRF:decimal, Transformer24MVA:decimal, Transformer15MVA:decimal, RollingMill:decimal, WRM:decimal, OxygenPlant4A:decimal, NGConsumption:decimal, PlantTotal:decimal, SMSTotal:decimal, SMSAuxWithO2:decimal, SMSAuxWithoutO2:decimal, TotalRollingMill:decimal, Transformer125MVALosses:decimal, Transformer63MVALosses:decimal

## dbo.Power_Consumption_LogSheet
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, Transformer132kv1:decimal, Transformer132kv2:decimal, Transformer33kv1:decimal, Transformer33kv2:decimal, EAF:decimal, LRF:decimal, Transformer24MVA:decimal, Transformer15MVA:decimal, RollingMill:decimal, WRM:decimal, OxygenPlant4A:decimal, NGConsumptionSm3:decimal, Transformer63MVALosseskWH:decimal, Transformer125MVALosseskWH:decimal, NGActualReading:decimal, Shift:varchar, RMNGConsumption:decimal

## dbo.Power_Consumption_LogSheet_Audit
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, Transformer132kv1:decimal, Transformer132kv2:decimal, Transformer33kv1:decimal, Transformer33kv2:decimal, EAF:decimal, LRF:decimal, Transformer24MVA:decimal, Transformer15MVA:decimal, RollingMill:decimal, WRM:decimal, OxygenPlant4A:decimal, NGConsumptionSm3:decimal, Transformer63MVALosseskWH:decimal, Transformer125MVALosseskWH:decimal, NGActualReading:decimal, Shift:varchar

## dbo.Power_Consumption_Report
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, OxygenPlant4A:decimal, SMSTotal:decimal, Transformer132kv2:decimal, Transformer132kv1:decimal, Transformer63MVALosses:decimal, Transformer33kv1:decimal, EntryDateTime:datetime, WRM:decimal, ReportDate:date, RollingMill:decimal, Transformer15MVA:decimal, SMSAuxWithO2:decimal, ParentID:varchar, Transformer33kv2:decimal, TotalRollingMill:decimal, LRF:decimal, Transformer125MVALosses:decimal, PlantTotal:decimal, Name:varchar, SMSAuxWithoutO2:decimal, NGConsumption:decimal, IsProcessed:bit, EAF:decimal, Transformer24MVA:decimal, SMSConsumption:decimal, TotalProduction:decimal, RMNGConsumption:decimal

## dbo.Power_Consumption_Report_Audit
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, OxygenPlant4A:decimal, SMSTotal:decimal, Transformer132kv2:decimal, Transformer132kv1:decimal, Transformer63MVALosses:decimal, Transformer33kv1:decimal, EntryDateTime:datetime, WRM:decimal, ReportDate:date, RollingMill:decimal, Transformer15MVA:decimal, SMSAuxWithO2:decimal, ParentID:varchar, Transformer33kv2:decimal, TotalRollingMill:decimal, LRF:decimal, Transformer125MVALosses:decimal, PlantTotal:decimal, Name:varchar, SMSAuxWithoutO2:decimal, NGConsumption:decimal, IsProcessed:bit, EAF:decimal, Transformer24MVA:decimal

## dbo.Power_Meter_Reading_Time
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, TX1TX5MVAH:decimal, TX1TX5MWH:decimal, NOofHeatTapped:decimal, Feeder33KVF2MWH:decimal, TX2TX2AMVAH:decimal, Feeder15MVAMWH:decimal, IC1MWH66:decimal, Feeder132KVF2MWH:decimal, IsProcessed:bit, Feeder33KVF1MVAH:decimal, Feeder33KVF1MWH:decimal, ParentID:varchar, ReportDate:date, Feeder132KVF1MWH:decimal, Feeder33KVF2MVAH:decimal, TX4TX4AMWH:decimal, Shift:varchar, RollingMillFDRMWH:decimal, Feeder132KVF2MVAH:decimal, Feeder132KVF1MVAH:decimal, IC2MWH66:decimal, ECR5MWH:decimal, TX2TX2AMWH:decimal, TX4TX4AMVAH:decimal, Name:varchar, TX3TX3AMWH:decimal, TechnicianName:varchar, TX3TX3AMVAH:decimal, LRFFeederMWH:decimal, EngineerName:varchar, Feeder24MVAMWH:decimal, EntryDateTime:datetime, EAFFeederMWH:decimal, WRMMWH:decimal

## dbo.Price_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, ItemType:varchar, UnitOfMeasurement:varchar, UnitPriceUSD:decimal, EffectiveDate:datetime, Remarks:varchar

## dbo.Procedure_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, AreaID:varchar, DurationUnit:varchar, FrequencyID:varchar, GenerationTimeLimit:int

## dbo.Procedure_Steps_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ProcedureID:varchar, StepDtlID:varchar, Srno:int, Type:varchar

## dbo.Procedure_Task_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntityID:varchar, EquipmentID:varchar, PageID:varchar, ViewPageID:varchar, Isscanable:bit

## dbo.Product_Master
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar

## dbo.ProductionMonthlyTargets
ID:varchar, Month:datetime, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, TargetMT:decimal, FiscalYear:varchar, Monthnumber:int, MonthStarttime:datetime, MonthEndTime:datetime

## dbo.ProductionWeeklyTargets
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, WeekStartTime:date, Month:varchar, Week:varchar, WeekEndTime:date, TargetMT:decimal

