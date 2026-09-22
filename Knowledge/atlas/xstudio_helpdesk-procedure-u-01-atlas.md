---
type: note
subtype: procedure-reference
database: XStudio_Helpdesk
authority: static-advisory
---
# XStudio_Helpdesk stored-procedure atlas: U part 1

Safety is fail-closed. Only READ_ONLY_REVIEWED procedures may be exposed as diagnostics.

## dbo.UAT_Test_Report_USP
Safety: MUTATING
Parameters: @EntityName:nvarchar(128)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Helpdesk.dbo.UAT_Test_Report_Data

## dbo.UAT_Tracking_Transaction_DataInsert_USP
Safety: MUTATING
Parameters: none
Referenced objects: none detected

## dbo.UAT_U_Enddatetime_Ticket_Generate_USP
Safety: MUTATING
Parameters: @ID:varchar(36), @Entity:varchar(100)
Referenced objects: XStudio_Helpdesk.dbo.Complaint_Mst_Tbl, XStudio_Helpdesk.dbo.sp_assignhod, XStudio_Helpdesk.dbo.UAT_Test_Mst_Tbl, XStudio_Helpdesk.dbo.UAT_Test_Report_USP, XStudio_Helpdesk.dbo.UAT_Tracking_Transaction_DataInsert_USP
