---
type: note
subtype: procedure-reference
database: XStudio_Xbatch
authority: static-advisory
---
# XStudio_Xbatch stored-procedure atlas: B part 1

Safety is fail-closed. Only READ_ONLY_REVIEWED procedures may be exposed as diagnostics.

## dbo.BilletsCapacityDetails_VIEW_USP
Safety: MUTATING
Parameters: none
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.VW_Xbatch_YMS_BilletsCapacityDetails

## dbo.BilletsPosition_InFurnace_Usp
Safety: MUTATING
Parameters: @StartTime:datetime
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.Billet_NGConsumption_InFurnace, XStudio_Xbatch.dbo.BilletsPosition_InFurnace
