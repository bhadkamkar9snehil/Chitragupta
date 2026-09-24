---
type: procedure
title: "XSTUDIO_WORKFLOW_3BFFE5C9-33C9-4C50-A0F0-3665571F92D4_SP"
built: "2026-09-24T11:36:36"
---

# XSTUDIO_WORKFLOW_3BFFE5C9-33C9-4C50-A0F0-3665571F92D4_SP

Parameters: @p_SystemId varchar, @p_UserId varchar, @p_RecordId varchar, @p_StatusAttributeName varchar, @p_Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Reads

- XMES_SAP_Batch_Characteristic_Trn_Tbl: ActualGrade, BatchNo, ClassNumber, ClassType, ColourCode, EntryDateTime, ExternalGrade, HeatNo, HeatSequenceNumber, ID, InspectionAgency, IsProcessed, Length, Material, NoOfPieces, Pieces, Plant, ProcessRoute, Product, ProductionSectionalWeight, ReportDate, Saptransactionid, SectionalWeight, TDCRefNo, Thickness, TonsPerPiece, Width

## Writes (named in its SQL text)

- XMES_SAP_Batch_Characteristic_Trn_Tbl
