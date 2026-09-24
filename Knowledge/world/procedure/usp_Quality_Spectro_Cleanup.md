---
type: procedure
title: "usp_Quality_Spectro_Cleanup"
built: "2026-09-24T11:36:36"
---

# usp_Quality_Spectro_Cleanup

Parameters: @BufferDays int, @Source varchar.

## Writes

- Quality_Spectro_File: IsDeleted, Source
- Quality_Spectro_Result: IsDeleted, Source
- Quality_Spectro_Sample: IsDeleted, Source

## Reads

- Quality_Spectro_File: Importedon
- Quality_Spectro_Result: SampleID
- Quality_Spectro_Sample: ID, XMLCreatedAt
