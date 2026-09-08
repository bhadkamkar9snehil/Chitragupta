---
type: Reference
database: XStudio_Helpdesk
authority: static-advisory
---
# XStudio_Helpdesk stored-procedure atlas: S

Safety is fail-closed. Only READ_ONLY_REVIEWED procedures may be exposed as diagnostics.

## dbo.sp_assignhod
Safety: MUTATING
Parameters: @RECORDID:varchar(36)
Referenced objects: none detected

## dbo.sp_assignsupportexecutive
Safety: MUTATING
Parameters: @id:varchar(36), @userid:varchar(36)
Referenced objects: none detected

## dbo.SP_Create_TicketNo
Safety: MUTATING
Parameters: @Id:varchar(36), @Entity:varchar(100), @ticketcolumn:varchar(100)
Referenced objects: none detected

## dbo.sp_handoverDetails
Safety: MUTATING
Parameters: @SYSTEMID:varchar(36), @USERID:varchar(36), @RECORDID:varchar(36), @STATUS:varchar(50)
Referenced objects: none detected

## dbo.Sp_Logsheet_Calculation_Adhoc
Safety: MUTATING
Parameters: @ID:varchar(36), @Entity:varchar(2000), @SystemID:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_System_Mst_Tbl

## dbo.Sp_Logsheet_Calculation_Adhoc_By_Date
Safety: MUTATING
Parameters: @Date:date
Referenced objects: XStudio_Helpdesk.dbo.FN_GET_ReportDate

