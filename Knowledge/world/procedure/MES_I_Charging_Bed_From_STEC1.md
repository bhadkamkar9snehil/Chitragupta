---
type: procedure
title: "MES_I_Charging_Bed_From_STEC1"
built: "2026-09-24T11:36:36"
---

# MES_I_Charging_Bed_From_STEC1

Parameters: @RecordID varchar, @EnteredBillets int, @Heatno varchar, @Grade varchar, @BilletLength int, @CampaignId varchar, @workorder varchar, @length decimal, @BedNo varchar, @BilletNo varchar.

## Writes

- RM_Operator_HeatSelection: BedNo, BilletLength, BilletQty, CampaignId, Grade, Heatno, ID, length, workorder
- XMES_Live_Billet_Charging_Bed: BilletNo, InTIme, ParentID
- XMES_Live_Charging_SECT1: Status

## Reads

- XMES_Live_Charging_SECT1: ID
