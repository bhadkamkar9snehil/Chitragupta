---
type: event
title: "LRF_SMS/LRF_ProcessTime"
built: "2026-09-24T11:36:36"
---

# LRF_SMS/LRF_ProcessTime

Area LRF_SMS. Active.
Creates and updates rows in LRF_ProcessTime.

## State 1: Ladle Car at LRF

Condition: `iif({LRFLadleCar} = 1 AND {LiquidMetal} > 10, True, IIF({LRFLadleCar} = 0 AND {LiquidMetal} < 10, False, Null))`
Captures: PTLRFHeatID -> HeatID

## State 1: Treatment Start

Condition: `IIF({LRFTreatmentTime} > 0 AND {RoofUpE2} = 0 AND {RoofUpE1} = 0, True, IIF({LRFTreatmentTime} > 0 AND {RoofUpE2} = 1 AND {RoofUpE1} = 1, False, Null))`
Captures: PTLRFHeatID -> HeatID

## State 2: LRF Roof Close

Condition: `IIF({RoofUpE1} = 0 AND {RoofUpE2} = 0, True, IIF({RoofUpE1} = 1 AND {RoofUpE2} = 1, False, Null))`
Captures: PTLRFHeatID -> HeatID

## State 3: Arcing Start

Condition: `IIF({RoofUpE1} = 0 AND {RoofUpE2} = 0 AND {LRFArcTime} > 0, True, IIF({RoofUpE1} = 1 AND {RoofUpE2} = 1 AND {LRFArcTime} > 0, False, Null))`
Captures: PTLRFHeatID -> HeatID

## State 4: LRF Roof Open

Condition: `IIF({RoofUpE1} = 1 AND {RoofUpE2} = 1, True, IIF({RoofUpE1} = 0 AND {RoofUpE2} = 0, False, Null))`
Captures: PTLRFHeatID -> HeatID

## State 5: Ladle Move From LRF To CCM

Condition: `IIF({RoofUpE1} = 1 AND {RoofUpE2} = 1 AND {CCMArm1InstantWieght} < 10 AND {LRFArcTime} > 0, True, IIF({RoofUpE1} = 1 AND {RoofUpE2} = 1 AND {CCMArm1InstantWieght} > 70 AND {LRFArcTime} = 0, False, Null))`
Captures: PTLRFHeatID -> HeatID

## State 5: Ladle Move From LRF To CCM

Condition: `IIF({RoofUpE1} = 1 AND {RoofUpE2} = 1 AND {CCMArm2InstantWieght} < 10 AND {LRFArcTime} > 0, True, IIF({RoofUpE1} = 1 AND {RoofUpE2} = 1 AND {CCMArm2InstantWieght} > 70 AND {LRFArcTime} = 0, False, Null))`
Captures: PTLRFHeatID -> HeatID
