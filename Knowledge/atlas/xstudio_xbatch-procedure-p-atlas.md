---
type: note
subtype: procedure-reference
database: XStudio_Xbatch
authority: static-advisory
---
# XStudio_Xbatch stored-procedure atlas: P

Safety is fail-closed. Only READ_ONLY_REVIEWED procedures may be exposed as diagnostics.

## dbo.Per_Heat_LadleNo_Conformation_usp
Safety: MUTATING
Parameters: @HeatNo:int, @LadleNo:varchar(500), @LRFConformed:bit, @CCMConformed:varchar(10), @TundishNo:varchar(500)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.Per_Heat_LadleNo

