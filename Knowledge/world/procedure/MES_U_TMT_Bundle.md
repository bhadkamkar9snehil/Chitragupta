---
type: procedure
title: "MES_U_TMT_Bundle"
built: "2026-09-24T11:36:36"
---

# MES_U_TMT_Bundle

Parameters: @UserId varchar, @SystemId varchar, @RecordIds varchar, @Status varchar, @DataCollection varchar.

## Writes

- MES_Current_Batch: TMTBundle
- MES_TMT_Small_Cut: BundleNo, Status

## Reads

- MES_TMT_Small_Cut: ID
