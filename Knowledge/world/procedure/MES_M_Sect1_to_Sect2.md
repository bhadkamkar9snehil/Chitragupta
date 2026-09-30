---
type: procedure
title: "MES_M_Sect1_to_Sect2"
built: "2026-09-24T11:36:36"
---

# MES_M_Sect1_to_Sect2

Parameters: @id varchar, @BilletNO varchar, @Mode varchar, @Refid varchar.

## Writes

- XMES_Live_Billet_Charging_Bed: BilletTrackingStatus, ModifiedOn
- XMES_Live_Charging_SECT1: ModifiedOn, ReverseWorkFlow, Status
- XMES_Live_Charging_SECT2: BilletNo, InTIme, ModifiedOn, ParentID, Status

## Reads

- XMES_Live_Billet_Charging_Bed: BilletNo, IsDeleted
- XMES_Live_Charging_SECT1: ID, IsDeleted
- XMES_Live_Charging_SECT2: ID, IsDeleted
