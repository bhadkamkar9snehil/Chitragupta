---
type: procedure
title: "XBatch_RM_BilletWiseNGConsumption"
built: "2026-09-24T11:36:36"
---

# XBatch_RM_BilletWiseNGConsumption


## Writes

- Billet_NGConsumption_InFurnace: NGConsumption, Price
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- Billet_NGConsumption_InFurnace: OutTime
- Billets_InFurnace_Tracking_Trn: BilletNo, BilletPosition, CreatedOn, EntryDateTime
- NM3_To_MMBTU_Factor: CreatedOn, IsDeleted, ModifiedOn, Nm3toMMBTUFactor
- Price_Mst_Tbl: ID, UnitPriceUSD

## What its own log shows

1,389,517 log rows, 2026-05-30 10:23 to 2026-09-24 11:30.
Error steps: 13 Error

Steps:
- 1 Entered
- 2 Get Latest Billet no, Enddate of position2 from billet in furnace tracking Start
- 3 Get Latest Billet no, Enddate of position 2 from billet in furnace tracking End
- 4 Get Latesat Startdate of position 1 from billet in furnace tracking Start
- 5 Get Latesat Startdate of position 1 from billet in furnace tracking End
- 6 Create Temp table of tag condition Start
- 7 Create Temp table of tag condition End
- 8 insert into temp table tagid and condition from tag master for NG ACTUAL DAY Consumption Tag Start
- 9 insert into temp table tagid and condition from tag master for NG ACTUAL DAY Consumption Tag End
- 10 Create temp table CCM SMS Block  Start
- 11 Create temp table CCM SMS Block  End
- 12 insert start date, enddate in temp table CCM SMS Block by executing historian procedure of XHS_Tag_Max_Sub_Max_Value_Usp Start
- 13 Error
- 13 insert start date, enddate in temp table CCM SMS Block by executing historian procedure of XHS_Tag_Max_Sub_Max_Value_Usp End
- 14 Truncate temp table tag condition Start
- 15 Truncate temp table tag condition End
- 16 Get count of billet no from billets in furnace tracking Start
- 17 Get count of billet no from billets in furnace tracking End
- 18 Update get val formula from temp table CCM SMS Block Start
- 19 Update get val formula from temp table CCM SMS Block End
- 20 Update Ngconsumption Billet Ng Consumption infurnace when out time is null Start
- 21 Update Ngconsumption Billet Ng Consumption infurnace when out time is null End
- 22 Update Price Billet Ng Consumption infurnace when out time is null Start
- 23 Update Price Billet Ng Consumption infurnace when out time is null End
- 24 Completed

Example call: `EXEC XStudio_Xbatch.dbo.XBatch_RM_BilletWiseNGConsumption`
