---
type: event
title: "EAF_SMS/LadleAddition"
built: "2026-09-24T11:36:36"
---

# EAF_SMS/LadleAddition

Area EAF_SMS. Active.
Creates and updates rows in LadleAddition.

## State 1: Silo

Condition: `IIF({Silo3} > 0 OR {Silo4} > 0 OR {Silo5} > 0 OR {Silo6} > 0 OR {Silo7} > 0 OR {Silo8} > 0, True, IIF({Silo3} = 0 AND {Silo4} = 0 AND {Silo5} = 0 AND {Silo6} = 0 AND {Silo7} = 0 AND {Silo8} = 0, False, Null))`
Captures: Silo6 -> Silo6KG, Silo4 -> Silo4KG, HeatNoSilo -> HeatNo, Silo5 -> Silo5KG, Silo3 -> Silo3KG, Silo7 -> Silo7KG, Silo8 -> Silo8KG
