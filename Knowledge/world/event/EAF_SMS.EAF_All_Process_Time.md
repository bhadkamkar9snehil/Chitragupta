---
type: event
title: "EAF_SMS/EAF_All_Process_Time"
built: "2026-09-24T11:36:36"
---

# EAF_SMS/EAF_All_Process_Time

Area EAF_SMS. Active.
Creates and updates rows in EAF_ProcessTime.

## State 1: EAF Bucket Charging

Condition: `IIF({RoofClose} = 0 AND {EAFPowerOnTimeMinute} = 0, True, IIF({RoofClose} = 1 AND {EAFPowerOnTimeMinute} = 0, False, Null))`
Captures: EAFHeatID -> HeatID

## State 1: Heat Start

Condition: `({EAFHeatTimeMinute}+ {EAFHeatTimeSec}) > 0`
Captures: EAFHeatID -> HeatID

## State 2: PowerOn

Condition: `IIF({RoofClose} = 1 AND {EAFPowerOnTimeMinute} > 0 AND {EAFTapping1} = 0, True, IIF({RoofClose} = 1 AND {EAFPowerOnTimeMinute} > 0 AND {EAFTapping1} = 1, False, Null))`
Captures: EAFHeatID -> HeatID

## State 3: Ladle Car At EAF

Condition: `IIF({EAFPowerOnTimeMinute} > 0 AND {EAFLadleCarPosition} = 1, True, IIF({EAFPowerOnTimeMinute} > 0 AND {EAFLadleCarPosition} = 0, False, Null))`
Captures: EAFHeatID -> HeatID

## State 4: Tapping

Condition: `IIF({EAFTapping1} = 1 AND {EAFHeatTimeMinute} > 0, True, IIF({EAFTapping1} = 0 AND {EAFPowerOnTimeMinute} > 0, False, Null))`
Captures: EAFHeatID -> HeatID

## State 5: Ladle Car Move From EAF To LRF

Condition: `IIF({EAFTapping1} = 1 AND {EAFLadleCarPosition} = 0 AND {LRFLadleCarPosition} = 0, True, IIF({EAFLadleCarPosition} = 0 AND {LRFLadleCarPosition} = 1, False, Null))`
Captures: EAFHeatID -> HeatID
