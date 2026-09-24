---
type: event
title: "LRF_SMS/LRF_Per_HeatData"
built: "2026-09-24T11:36:36"
---

# LRF_SMS/LRF_Per_HeatData

Area LRF_SMS. Active.
Creates and updates rows in LRF_Per_Heat.

## State 1: LRF Start

Condition: `{ActualPowerOnTime} > 0`
Workflow status on: Entered, off: Completed.
Captures: LRFLiquidMetalWeight -> LiquidMetalWeight, PowerOFFTime -> PowerOFFTime, LRFTemperature -> LRFTemperature, ArcingTime -> ArcingTime, ArgonConsumption -> ArgonConsumption, Energy -> PowerMWH, PowerOnTime -> PowerONTime
