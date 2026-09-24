---
type: view
title: "XStudio_List_XMES_Billet_Movement_Dtl_Tbl_Vw"
built: "2026-09-24T11:36:36"
---

# XStudio_List_XMES_Billet_Movement_Dtl_Tbl_Vw

View in XStudio_Xbatch. Rows: unknown.

## Identifiers it holds

- BilletNo: same values as key `BilletNo`
- ChargingBedBilletNo: same values as key `BilletNo`
- Section1BilletNo: same values as key `BilletNo`
- Section2BilletNo: same values as key `BilletNo`
- ZonewiseBilletNo: same values as key `BilletNo`

## Reads

- RM_Operator_HeatSelection
- XMES_Billet_Movement_Dtl_Tbl
- XMES_Live_Billet_Charging_Bed
- XMES_Live_Charging_SECT1
- XMES_Live_Charging_SECT2
- XMES_RM_Furnace_Billet_Trn_Tbl

## Columns

- Edit varchar(246)
- ID varchar(36)
- BilletNo varchar(36)
- Section1BilletNo varchar(36)
- Section2BilletNo varchar(36)
- Delete varchar(100)
- Details varchar(-1)
- BilletGrade varchar(20)
- ChargingBedBilletNo_BilletNo varchar(100)
- BilletLength decimal
- ChargingBedBilletNo varchar(36)
- Weight decimal
- ChargingBedInTime datetime
- Section1InTIme datetime
- Section2InTIme datetime
- FuranceInTime datetime
- FurnaceOutTime datetime
- TotalResidenceTime varchar(8)
- TotalResidenceTimeinSecond int
- Zone1ResidenceTimeMMSS varchar(100)
- ZonewiseBilletNo varchar(36)
- Zone2ResidenceTimeMMSS varchar(100)
- Zone3ResidenceTimeMMSS varchar(100)
- Zone4ResidenceTimeMMSS varchar(100)
- Zone5ResidenceTimeMMSS varchar(100)
- Zone6ResidenceTimeMMSS varchar(100)
- Zone7ResidenceTimeMMSS varchar(100)
- Zone8ResidenceTimeMMSS varchar(100)
