---
type: note
subtype: schema-reference
database: XStudio_Helpdesk
authority: static-advisory
---
# XStudio_Helpdesk schema atlas: E part 1

Static routing knowledge generated from the authoritative export. Current ticket facts require live SQL.

## dbo.Equipment_Type_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, GeneratePagesButton:varchar, Frequency:varchar, Icon:varchar, IsBatchingEntity:bit, BatchingEquipmentClass:varchar, Hierarchy:varchar, IsEventCheck:bit, BlockType:varchar, DataSourceID:varchar, IsHandoverEnabled:bit

## dbo.Events_Monitoring
ID:varchar, EntryDateTime:datetime, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ErrorLastHoursMessageCount:int, ErrorLastHoursMessageImage:varchar, ErrorLast24HoursMessageCount:int, WarningLastHoursMessageCount:int, WarningLastHoursMessageImage:varchar, WarningLast24HoursMessageCount:int, CriticalLastHoursMessageCount:int, CriticalLastHoursMessageImage:varchar, CriticalLast24HoursMessageCount:int, ErrorLastHoursMessageRemarks:varchar, WarningLastHoursMessageRemarks:varchar, CriticalLastHoursMessageRemarks:varchar

## dbo.Events_Monitoring_Audit
ID:varchar, EntryDateTime:datetime, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ErrorLastHoursMessageCount:int, ErrorLastHoursMessageImage:varchar, ErrorLast24HoursMessageCount:int, WarningLastHoursMessageCount:int, WarningLastHoursMessageImage:varchar, WarningLast24HoursMessageCount:int, CriticalLastHoursMessageCount:int, CriticalLastHoursMessageImage:varchar, CriticalLast24HoursMessageCount:int, ErrorLastHoursMessageRemarks:varchar, WarningLastHoursMessageRemarks:varchar, CriticalLastHoursMessageRemarks:varchar
