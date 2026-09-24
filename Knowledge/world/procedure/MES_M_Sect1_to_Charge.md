---
type: procedure
title: "MES_M_Sect1_to_Charge"
built: "2026-09-24T11:36:36"
---

# MES_M_Sect1_to_Charge

Parameters: @billetno varchar, @count int.

## Writes

- XMES_Live_Billet_Charging_Bed: BilletTrackingStatus, ModifiedOn, Status
- XMES_Live_Charging_SECT1: Status

## Reads

- XMES_Live_Billet_Charging_Bed: ID, IsDeleted
- XMES_Live_Charging_SECT1: BilletNo, CreatedOn, ID, IsDeleted, ParentID
