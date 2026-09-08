---
type: Reference
database: XStudio_Xbatch
authority: static-advisory
---
# XStudio_Xbatch stored-procedure atlas: C

Safety is fail-closed. Only READ_ONLY_REVIEWED procedures may be exposed as diagnostics.

## dbo.campaignplan_released_workflow_usp
Safety: MUTATING
Parameters: none
Referenced objects: none detected

## dbo.Charging_Stack_Usp
Safety: MUTATING
Parameters: @stack:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP

