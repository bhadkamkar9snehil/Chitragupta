---
type: procedure
title: "MES_I_Charging_Bed"
built: "2026-09-24T11:36:36"
---

# MES_I_Charging_Bed

Parameters: @RecordID varchar, @EnteredBillets int, @Heatno varchar, @From varchar.

## Writes

- XMES_Live_Billet_Charging_Bed: BilletNo, InTIme, ParentID

## Reads

- XMES_Billet_Tracking_Trn_Tbl: BilletNo, HeatNo
