---
type: procedure
title: "MES_M_Billet_to_Sect1"
built: "2026-09-24T11:36:36"
---

# MES_M_Billet_to_Sect1

Parameters: @id varchar, @BilletNo varchar.

## Writes

- XMES_Live_Billet_Charging_Bed: BilletTrackingStatus, ModifiedOn, OutTime, Status
- XMES_Live_Charging_SECT1: BilletNo, InTIme, ModifiedOn, ParentID, ReverseWorkFlow, Status

## Reads

- XMES_Live_Billet_Charging_Bed: ID, IsDeleted
- XMES_Live_Charging_SECT1: IsDeleted
