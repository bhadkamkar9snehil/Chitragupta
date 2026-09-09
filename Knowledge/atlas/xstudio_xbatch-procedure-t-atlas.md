---
type: note
subtype: procedure-reference
database: XStudio_Xbatch
authority: static-advisory
---
# XStudio_Xbatch stored-procedure atlas: T

Safety is fail-closed. Only READ_ONLY_REVIEWED procedures may be exposed as diagnostics.

## dbo.Tag_Trend
Safety: MUTATING
Parameters: @TagName:varchar(200)
Referenced objects: XStudio_Xbatch.dbo.Tag_Configuration

## dbo.test_usp
Safety: MUTATING
Parameters: @id:varchar(36), @name:varchar(300)
Referenced objects: none detected

