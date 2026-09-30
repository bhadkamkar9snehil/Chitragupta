---
type: procedure
title: "MES_U_WRM_Bundle"
built: "2026-09-24T11:36:36"
---

# MES_U_WRM_Bundle

Parameters: @UserId varchar, @SystemId varchar, @RecordIds varchar, @Status varchar, @DataCollection varchar.

## Writes

- MES_Current_Batch: WRMBundle
- MES_WRM: BundleNo, Status

## Reads

- MES_WRM: ID
