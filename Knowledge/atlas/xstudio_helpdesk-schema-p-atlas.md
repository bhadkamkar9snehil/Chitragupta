---
type: note
subtype: schema-reference
database: XStudio_Helpdesk
authority: static-advisory
---
# XStudio_Helpdesk schema atlas: P

Static routing knowledge generated from the authoritative export. Current ticket facts require live SQL.

## dbo.Pipeline_Mst_Tbl
ID:varchar, Name:varchar, RegionID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar

## dbo.Pipeline_Mst_Tbl_Audit
ID:varchar, Name:varchar, RegionID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar

## dbo.PowerGenerationOutput
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, TotalForTheYear:decimal, TotalForTheDay:decimal, SolarForTheYear:decimal, SolarForTheMonth:decimal, WindForTheMonth:decimal, WindForTheDay:decimal, Region:varchar, TotalForTheMonth:decimal, WindForTheYear:decimal, SolarForTheDay:decimal, ReportDate:date, Station:varchar

## dbo.PowerGenerationOutput_Audit
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, TotalForTheYear:decimal, TotalForTheDay:decimal, SolarForTheYear:decimal, SolarForTheMonth:decimal, WindForTheMonth:decimal, WindForTheDay:decimal, Region:varchar, TotalForTheMonth:decimal, WindForTheYear:decimal, SolarForTheDay:decimal, ReportDate:date, Station:varchar

## dbo.Procedure_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, AreaID:varchar, DurationUnit:varchar, FrequencyID:varchar, GenerationTimeLimit:int

## dbo.Procedure_Steps_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ProcedureID:varchar, StepDtlID:varchar, Srno:int, Type:varchar

## dbo.Procedure_Task_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntityID:varchar, EquipmentID:varchar, PageID:varchar, ViewPageID:varchar, Isscanable:bit

## dbo.priority_mst
ID:varchar, priority:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Icon:varchar

