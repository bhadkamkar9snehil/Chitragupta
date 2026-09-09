---
type: note
subtype: procedure-reference
database: XStudio_Xbatch
authority: static-advisory
---
# XStudio_Xbatch stored-procedure atlas: M part 1

Safety is fail-closed. Only READ_ONLY_REVIEWED procedures may be exposed as diagnostics.

## dbo.MES_U_Delay_Merge
Safety: MUTATING
Parameters: @UserId:varchar(36), @SystemId:varchar(36), @RecordIds:varchar(max), @Status:varchar(36), @DataCollection:nvarchar(max)
Referenced objects: none detected
