---
type: event
title: "CCM_SMS/Delays"
built: "2026-09-24T11:36:36"
---

# CCM_SMS/Delays

Area CCM_SMS. Inactive.
Creates and updates rows in Delay_Trn_Tbl.

## State 1: Arcing Delay

Condition: `{EAFPowerOn} > 48`
Workflow status on: Entered, off: Completed.
Captures: EAFHeatID -> HeatNo

## State 1: Power OFF Delay

Condition: `{EAFPowerOff} > 7`
Workflow status on: Entered, off: Completed.
Captures: EAFHeatID -> HeatNo
