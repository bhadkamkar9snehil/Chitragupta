---
type: procedure
title: "MES_M_Sect1_to_Sect2_Billet_Tracking"
built: "2026-09-24T11:36:36"
---

# MES_M_Sect1_to_Sect2_Billet_Tracking

Parameters: @systemid varchar, @userid varchar, @RecordId varchar, @status varchar.

## Writes

- XMES_Live_Billet_Charging_Bed: BilletTrackingStatus, ModifiedOn
- XMES_Live_Charging_SECT1: ModifiedOn, OutTime, ReverseWorkFlow, Status
- XMES_Live_Charging_SECT2: BilletNo, InTIme, ModifiedOn, ParentID, Status

## Reads

- XMES_Live_Billet_Charging_Bed: BilletNo, ID, IsDeleted
- XMES_Live_Charging_SECT1: BilletNo, ID, IsDeleted
- XMES_Live_Charging_SECT2: IsDeleted
