---
type: procedure
title: "MES_I_Small_Cut"
built: "2026-09-24T11:36:36"
---

# MES_I_Small_Cut

Parameters: @UserId varchar, @SystemId varchar, @RecordIds varchar, @Status varchar, @DataCollection varchar.

## Writes

- MES_Current_Batch: TMT_Small_Cut
- MES_TMT: RemainLength, Status
- MES_TMT_Small_Cut: BatchNo, Length, ParentID

## Reads

- MES_TMT: ID
