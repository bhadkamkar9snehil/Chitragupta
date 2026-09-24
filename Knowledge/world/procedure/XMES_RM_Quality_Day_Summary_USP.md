---
type: procedure
title: "XMES_RM_Quality_Day_Summary_USP"
built: "2026-09-24T11:36:36"
---

# XMES_RM_Quality_Day_Summary_USP

Parameters: @ReportDate date, @Product varchar, @Campaign varchar.

## Reads

- RM_Quality_Data_Summary: ActualCrossSectionalArea, Agt, BilletGrade, Campaign, IsDeleted, Line, Nom, NominalCrossSectionArea, Product, ReportDate, SampleID, Tolerance, UTSMPa, UTSorYSRatio, WtMtr, YSMPa

## Writes (named in its SQL text)

- RM_Quality_Data_Day_Summary
