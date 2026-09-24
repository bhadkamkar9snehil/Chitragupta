---
type: event
title: "EAF_SMS/SMS Delay Data"
built: "2026-09-24T11:36:36"
---

# EAF_SMS/SMS Delay Data

Area EAF_SMS. Active.
Creates and updates rows in SMS_Delay_Trn_Tbl.

## State 1: Power On Delay

Condition: `IIF({RoofClose} = 1 AND {EAFPowerOnTimeMinute} > 0 AND {EAFTapping1} = 0, True, IIF({RoofClose} = 1 AND {EAFPowerOnTimeMinute} > 0 AND {EAFTapping1} = 1, False, Null))`
Workflow status on: Entered, off: Completed.
Captures: EAF_Heat_ID -> HeatNo

## State 2: Tapping Delay

Condition: `{Liquid_Tapping}=1`
Workflow status on: Entered, off: Completed.
Captures: EAF_Heat_ID -> HeatNo

## State 3: Bucket Charging

Condition: `{EAF_Roof_Status}=0`
Workflow status on: Entered, off: Completed.
Captures: EAF_Heat_ID -> HeatNo

## State 4: Setup Delay

Condition: `{Liquid_Tapping} = 0 AND {EAF_Roof_Status}=0`
Workflow status on: Entered, off: Completed.
Captures: EAF_Heat_ID -> HeatNo
