---
type: note
subtype: procedure-reference
database: XStudio_Xbatch
authority: static-advisory
---
# XStudio_Xbatch stored-procedure atlas: D part 1

Safety is fail-closed. Only READ_ONLY_REVIEWED procedures may be exposed as diagnostics.

## dbo.DelayEntry_EBTFilling_USP
Safety: MUTATING
Parameters: @HeatNo:int
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP
