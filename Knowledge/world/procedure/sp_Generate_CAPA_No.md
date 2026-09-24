---
type: procedure
title: "sp_Generate_CAPA_No"
built: "2026-09-24T11:36:36"
---

# sp_Generate_CAPA_No

Parameters: @ID varchar, @TransactionID varchar, @AgencyID varchar.

## Writes

- RMShiftDelayEntry_CAPA: CAPANO

## Reads

- RMShiftDelayEntry_CAPA: Agency, AgencyTransactionid, ID
- ShiftDelayEntry: AreaName, ID
