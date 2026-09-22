---
type: note
subtype: schema-reference
database: XStudio_Xbatch
authority: static-advisory
---
# XStudio_Xbatch schema atlas: E part 3

Static routing knowledge generated from the authoritative export. Current ticket facts require live SQL.

## dbo.Electricity_Meter_Electricity_Rate_Tbl_Mst
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, OffPeak:int, Months:varchar, NightPeak:int, WeekdayDayPeak:int, WeekendDayPeak:int, Year:varchar, EntryDatetime:datetime

## dbo.Electricity_Meter_Reading
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EndDateTime:datetime, ReportDate:date, IsProcessed:bit, Position:int, Value:decimal, Quality:int, Price:varchar, FeederName:varchar, Consumption:decimal, Status:varchar, MonthNumber:int

## dbo.Electricity_Meter_Reading_Test
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, IsProcessed:bit, Price:varchar, EndDateTime:datetime, Consumption:decimal, Quality:int, ReportDate:date, MonthNumber:int, Status:varchar, Value:decimal, FeederName:varchar, Position:int

## dbo.Electricity_Meter_Reading_Upload
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, IsProcessed:bit, FIleUpload132KVIC1:varchar, FIleUpload132KVIC2:varchar, FIleUpload33KVIC1:varchar, FIleUpload33KVIC2:varchar, FIleUploadEAF:varchar, FIleUploadLRF:varchar, FIleUpload24MVA:varchar, FIleUpload15MVA:varchar, FIleUploadROLLINGMILL:varchar, Status:varchar, Reportdate:date, AllFIleUpload:varchar

## dbo.Electricity_Meter_Timing
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, RateBand:varchar, FromTime:time, ToTime:time, DayOfWeek:varchar, SrNo:int, Year:varchar, EntryDatetime:datetime, Weekdays:varchar, ColorCode:varchar

## dbo.Equipment
ID:varchar, Name:varchar, Areaid:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar

## dbo.Equipment_Instance_Documents_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentTypeID:varchar, TemplateID:varchar, InstanceID:varchar, File:varchar, Description:varchar, AIGeneratedSummary:varchar

## dbo.Equipment_Template_Documents_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentTypeID:varchar, TemplateID:varchar, File:varchar, Description:varchar, AIGeneratedSummary:varchar

## dbo.Equipment_Type_Documents_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EquipmentTypeID:varchar, File:varchar, Description:varchar, AIGeneratedSummary:varchar

## dbo.Equipment_Type_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, GeneratePagesButton:varchar, Frequency:varchar, Icon:varchar, IsBatchingEntity:bit, BatchingEquipmentClass:varchar, Hierarchy:varchar, IsEventCheck:bit, BlockType:varchar, DataSourceID:varchar, IsHandoverEnabled:bit, ModuleID:varchar, ModuleType:varchar

## dbo.Equipment_Wise_Delay
ID:varchar, EquipmentName:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, EntryDateTime:datetime, ReportDate:date, IsProcessed:bit, DelayAgency:varchar, Duration:decimal, Remark:varchar, SubEquipmentName:varchar, Durationmmss:varchar, DurationInSecond:int

## dbo.eaf1_Life_Tracking_Transaction_tbl_Pivot
HeatID:varchar, Ladle Life:decimal, EAF Porous Plug Life:decimal, EAF Slide Gate Plate Life:decimal, EAF Porous Plug Checked:decimal

## dbo.eaf_Life_Tracking_Transaction_tbl_Pivot
Ladle Life:decimal, EAF Porous Plug Life:decimal, EAF Slide Gate Plate Life:decimal, EAF Porous Plug Checked:decimal
