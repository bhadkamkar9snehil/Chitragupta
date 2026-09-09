---
type: note
subtype: schema-reference
database: XStudio_Helpdesk
authority: static-advisory
---
# XStudio_Helpdesk schema atlas: H

Static routing knowledge generated from the authoritative export. Current ticket facts require live SQL.

## dbo.HOD_Mst_Tbl
ID:varchar, Name:varchar, AreaID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, UserID:varchar

## dbo.HOD_Mst_Tbl_Audit
ID:varchar, Name:varchar, AreaID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, UserID:varchar

## dbo.Hardware_Monitoring
ID:varchar, RBCSCDLBP1Summary:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, RBCSCDLBP1ErrorFound:bit, RBCSCDLBP1ErrorImages:varchar, RBCSCDLBP2Summary:varchar, RBCSCDLBP2ErrorFound:bit, RBCSCDLBP2ErrorImages:varchar, PLHODLBP1Summary:varchar, PLHODLBP1ErrorFound:bit, PLHODLBP1ErrorImages:varchar, PLHODLBP2Summary:varchar, PLHODLBP2ErrorFound:bit, PLHODLBP2ErrorImages:varchar, NoidaSANSummary:varchar, NoidaSANErrorFound:bit, NoidaSANErrorImages:varchar, BangaloreSANSummary:varchar, BangaloreSANErrorFound:bit, BangaloreSANErrorImages:varchar, RBCSCDLBP1FailurePrediction:varchar, RBCSCDLBP2FailurePrediction:varchar, PLHODLBP1FailurePrediction:varchar, PLHODLBP2FailurePrediction:varchar, Entrydatetime:datetime, Parentid:varchar, RBCSCDLBP1SummaryRemarks:varchar, RBCSCDLBP2SummaryRemarks:varchar, PLHODLBP1SummaryRemarks:varchar, PLHODLBP2SummaryRemarks:varchar, NoidaSANSummaryRemarks:varchar, BangaloreSANSummaryRemarks:varchar, RBCSCDLBP1FailurePredictionRemarks:varchar, RBCSCDLBP2FailurePredictionRemarks:varchar, PLHODLBP1FailurePredictionRemarks:varchar, PLHODLBP2FailurePredictionRemarks:varchar

## dbo.Hardware_Monitoring_Audit
ID:varchar, RBCSCDLBP1Summary:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, RBCSCDLBP1ErrorFound:bit, RBCSCDLBP1ErrorImages:varchar, RBCSCDLBP2Summary:varchar, RBCSCDLBP2ErrorFound:bit, RBCSCDLBP2ErrorImages:varchar, PLHODLBP1Summary:varchar, PLHODLBP1ErrorFound:bit, PLHODLBP1ErrorImages:varchar, PLHODLBP2Summary:varchar, PLHODLBP2ErrorFound:bit, PLHODLBP2ErrorImages:varchar, NoidaSANSummary:varchar, NoidaSANErrorFound:bit, NoidaSANErrorImages:varchar, BangaloreSANSummary:varchar, BangaloreSANErrorFound:bit, BangaloreSANErrorImages:varchar, RBCSCDLBP1FailurePrediction:varchar, RBCSCDLBP2FailurePrediction:varchar, PLHODLBP1FailurePrediction:varchar, PLHODLBP2FailurePrediction:varchar, Entrydatetime:datetime, Parentid:varchar, RBCSCDLBP1SummaryRemarks:varchar, RBCSCDLBP2SummaryRemarks:varchar, PLHODLBP1SummaryRemarks:varchar, PLHODLBP2SummaryRemarks:varchar, NoidaSANSummaryRemarks:varchar, BangaloreSANSummaryRemarks:varchar, RBCSCDLBP1FailurePredictionRemarks:varchar, RBCSCDLBP2FailurePredictionRemarks:varchar, PLHODLBP1FailurePredictionRemarks:varchar, PLHODLBP2FailurePredictionRemarks:varchar

## dbo.Hermes_L2_Response_Trn_Tbl
ID:varchar, TicketID:varchar, AttemptNo:int, WorkerID:varchar, ProcessStatus:varchar, IsActive:bit, Route:varchar, ResponseType:varchar, ProblemSummary:nvarchar, Findings:nvarchar, RootCause:nvarchar, Resolution:nvarchar, ReplyText:nvarchar, InvestigationJson:nvarchar, ActionsTakenJson:nvarchar, RequiresUserInput:bit, EscalateToL3:bit, IsResolved:bit, TicketModifiedOnSeen:datetime, ClaimedOn:datetime, HeartbeatOn:datetime, NextEligibleOn:datetime, CompletedOn:datetime, ErrorMessage:nvarchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, HostAddress:varchar, Source:varchar

## dbo.Hermes_L2_SQL_Action_Trn_Tbl
ID:varchar, RunID:varchar, TicketID:varchar, ActionNo:int, ActionType:varchar, DatabaseName:varchar, SchemaName:varchar, ObjectName:varchar, OperationName:varchar, Purpose:nvarchar, SqlText:nvarchar, ParametersJson:nvarchar, BeforeJson:nvarchar, AfterJson:nvarchar, Status:varchar, RowsAffected:int, StartedOn:datetime, CompletedOn:datetime, ErrorNumber:int, ErrorMessage:nvarchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, Source:varchar

## dbo.HyperV_Monitoring
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Entrydatetime:datetime, Name:varchar, State:varchar, MemoryAssigned:int, CPUUsage:int, PSComputerName:varchar, RunspaceId:varchar, PSShowComputerName:varchar

## dbo.HyperV_Monitoring_Audit
ID:varchar, CreatedBy:varchar, ModifiedBy:varchar, CreatedOn:datetime, ModifiedOn:datetime, IsDeleted:bit, IsSystem:bit, AssignedUserID:varchar, HostAddress:varchar, DbSyncStatus:varchar, MobileSyncStatus:varchar, Source:varchar, Entrydatetime:datetime, Name:varchar, State:varchar, MemoryAssigned:int, CPUUsage:int, PSComputerName:varchar, RunspaceId:varchar, PSShowComputerName:varchar

