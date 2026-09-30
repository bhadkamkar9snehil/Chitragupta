---
type: event
title: "CCM/Cast Billets Count"
built: "2026-09-24T11:36:36"
---

# CCM/Cast Billets Count

Area CCM. Active.
Creates and updates rows in BilletsCastCount.

## State 1: Billets Produces Start

Condition: `{CCMTotalBilletsCount}>0`
Workflow status on: Entered, off: Completed.
Captures: CCMHeatNO -> HeatID, ActualBilletCountByOperator -> ActualBilletsCountbyOperator
