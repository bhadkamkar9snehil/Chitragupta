---
type: Reference
database: XStudio_Helpdesk
authority: static-advisory
---
# XStudio_Helpdesk schema atlas: C

Static routing knowledge generated from the authoritative export. Current ticket facts require live SQL.

## dbo.CentralDispatch_Mst_Tbl
ID:varchar, Name:varchar, PipelineID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar

## dbo.CentralDispatch_Mst_Tbl_Audit
ID:varchar, Name:varchar, PipelineID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar

## dbo.CommonErrors
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, subarea:varchar

## dbo.CommonErrors_Audit
ID:varchar, Name:varchar, ParentID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, subarea:varchar

## dbo.ComplaintType_Mst_Tbl
ID:varchar, Name:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, subarea:varchar

## dbo.ComplaintType_Mst_Tbl_Audit
ID:varchar, Name:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, subarea:varchar

## dbo.Complaint_Mst_Tbl
ID:varchar, AreaID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ComplaintTypeID:varchar, Description:varchar, BriefDetails:varchar, Solution:varchar, Status:varchar, TicketNo:varchar, Attachment:varchar, Priority:varchar, RepeatTicketNo:varchar, commonerror:varchar, subareadetails:varchar, repeat:bit, FirstLastName:varchar, ContactNo:varchar, EmailID:varchar, ssmmessage:varchar, Soharmessage:varchar, messages:varchar, SupportExecutiveRemarks:varchar, ServerName:varchar, AskRemarks:varchar, ReplyRemarks:varchar, AskStatus:varchar, ProblemCategory:varchar, SourceSystem:varchar, ConversationSummary:nvarchar, SuspectedCause:nvarchar, ExtractedEntitiesJson:nvarchar, ConversationLogJson:nvarchar

## dbo.Complaint_Mst_Tbl_Audit
ID:varchar, AreaID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, ComplaintTypeID:varchar, Description:varchar, BriefDetails:varchar, Solution:varchar, Status:varchar, TicketNo:varchar, Attachment:varchar, Priority:varchar, RepeatTicketNo:varchar, commonerror:varchar, subareadetails:varchar, repeat:bit, FirstLastName:varchar, ContactNo:varchar, EmailID:varchar, ssmmessage:varchar, Soharmessage:varchar, messages:varchar, SupportExecutiveRemarks:varchar, ServerName:varchar, AskRemarks:varchar, ReplyRemarks:varchar, AskStatus:varchar

## dbo.ControlRoom_Mst_Tbl
ID:varchar, Name:varchar, SystemID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar

## dbo.ControlRoom_Mst_Tbl_Audit
ID:varchar, Name:varchar, SystemID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar

