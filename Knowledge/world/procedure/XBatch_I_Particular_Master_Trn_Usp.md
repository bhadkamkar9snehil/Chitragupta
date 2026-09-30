---
type: procedure
title: "XBatch_I_Particular_Master_Trn_Usp"
built: "2026-09-24T11:36:36"
---

# XBatch_I_Particular_Master_Trn_Usp

Parameters: @Reportdate datetime.

## Writes

- Particulars_Masters_Trn: Particulars, ReportDate, SrNo, Type, UOM

## Reads

- Particulars_Masters: IsDeleted, Particulars, SrNo, Type, UOM
- Particulars_Masters_Trn: IsDeleted
