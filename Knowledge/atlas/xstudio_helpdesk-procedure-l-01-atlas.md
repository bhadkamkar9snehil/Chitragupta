---
type: note
subtype: procedure-reference
database: XStudio_Helpdesk
authority: static-advisory
---
# XStudio_Helpdesk stored-procedure atlas: L part 1

Safety is fail-closed. Only READ_ONLY_REVIEWED procedures may be exposed as diagnostics.

## dbo.L3_Module_Import
Safety: MUTATING
Parameters: @CS:nvarchar(500), @CR:nvarchar(500), @CT:nvarchar(500), @FP:nvarchar(500)
Referenced objects: none detected

## dbo.L3_Module_Import_2
Safety: MUTATING
Parameters: @CS:nvarchar(500), @CR:nvarchar(500), @CT:nvarchar(500), @FP:nvarchar(500), @FM:datetime, @TE:datetime
Referenced objects: none detected

## dbo.Logsheet_Generation_Check
Safety: MUTATING
Parameters: none
Referenced objects: XStudio_Configuration.dbo.XStudio_System_Mst_Tbl, XStudio_Helpdesk.dbo.FN_Get_Current_Rota, XStudio_Helpdesk.dbo.Logsheet_Master, XStudio_Helpdesk.dbo.Logsheets
