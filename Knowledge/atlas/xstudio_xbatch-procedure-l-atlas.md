---
type: Reference
database: XStudio_Xbatch
authority: static-advisory
---
# XStudio_Xbatch stored-procedure atlas: L

Safety is fail-closed. Only READ_ONLY_REVIEWED procedures may be exposed as diagnostics.

## dbo.Ladle_Life_Count_Each_Heat
Safety: MUTATING
Parameters: @RecordId:varchar(36)
Referenced objects: XStudio_Configuration.dbo.XStudio_Add_ErrorLog_USP, XStudio_Xbatch.dbo.LRF_Ladle_No_Per_Heat

