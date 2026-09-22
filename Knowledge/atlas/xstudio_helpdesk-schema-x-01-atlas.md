---
type: note
subtype: schema-reference
database: XStudio_Helpdesk
authority: static-advisory
---
# XStudio_Helpdesk schema atlas: X part 1

Static routing knowledge generated from the authoritative export. Current ticket facts require live SQL.

## dbo.XStudio_Alarm_Viewer_Filter_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, AreaName:varchar, TagName:varchar, TagValue:decimal, AlarmState:varchar, AlarmType:varchar, MessageType:varchar, ReceivedTime:datetime, EventTime:datetime, AcknowledgeTime:datetime, RetrunTime:datetime, Remark:varchar, Description:varchar

## dbo.XStudio_Shift_Dtl_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, SrNo:int, StartTime:time, EndTime:time

## dbo.XStudio_Shift_Mst_Tbl
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, NoOfShift:int, SrNo:int
