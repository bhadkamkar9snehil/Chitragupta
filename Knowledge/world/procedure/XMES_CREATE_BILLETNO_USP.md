---
type: procedure
title: "XMES_CREATE_BILLETNO_USP"
built: "2026-09-24T11:36:36"
---

# XMES_CREATE_BILLETNO_USP

Parameters: @EventID varchar, @Status varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Writes

- XMES_Billet_Tracking_Per_Strand: BilletNo, BilletSequence, CreatedOn, EventID, HeatNo, ID, IsDeleted, IsSystem, Status, StrandNo, StrandSequence
- XMES_Billet_Tracking_Trn_Tbl: Batch, BilletNo, BilletQuantity, BilletWeight, CreatedOn, CutLength, EntryDateTime, HeatNo, ManufacturingOrder, Materialid, Plant, PostingMaterialType, ProcessStage, Qualitygradeid, ReportDate, Source, StatePosition, StorageLocation, UOMID
- XMES_CCM_Billet_Sequence: CreatedOn, CurrentSequence, HeatNo, ID, IsDeleted, IsSystem, StrandNo, StrandSequence
- XMES_Log_Trn_Tbl: EntryDateTime, ExecutionQuery, Name, ReportDate, Source, SrNo, Status, SubSeqNo, Type

## Reads

- Billet_Track_Per_Strand: CreatedOn, HeatNo, ID, StartTime, Status, StrandwiseCount
- BilletsCastCount: HeatID, IsDeleted, StartTime, WorkFlowStatus

## What its own log shows

768,276 log rows, 2026-06-01 10:56 to 2026-08-10 14:56.

Steps:
- 1 Entered
- 2 Get status and starttime from Billet Track Per Strand using Event ID Start
- 3 Get status Heat Change and starttime 09-Jun-2026 10:09:07.150 from Billet Track Per Strand using Event ID End
- 3 Get status Heat Change and starttime 09-Jun-2026 11:00:42.127 from Billet Track Per Strand using Event ID End
- 3 Get status Heat Change and starttime 09-Jun-2026 11:54:34.817 from Billet Track Per Strand using Event ID End
- 3 Get status Heat Change and starttime 09-Jun-2026 12:51:52.120 from Billet Track Per Strand using Event ID End
- 3 Get status Heat Change and starttime 09-Jun-2026 13:49:41.170 from Billet Track Per Strand using Event ID End
- 3 Get status Heat Change and starttime 09-Jun-2026 14:48:55.213 from Billet Track Per Strand using Event ID End
- 3 Get status Heat Change and starttime 09-Jun-2026 16:03:25.987 from Billet Track Per Strand using Event ID End
- 3 Get status Heat Change and starttime 09-Jun-2026 17:34:49.067 from Billet Track Per Strand using Event ID End
- 3 Get status Heat Change and starttime 09-Jun-2026 18:46:07.923 from Billet Track Per Strand using Event ID End
- 3 Get status Heat Change and starttime 09-Jun-2026 19:41:14.853 from Billet Track Per Strand using Event ID End
- 3 Get status Heat Change and starttime 09-Jun-2026 20:41:17.217 from Billet Track Per Strand using Event ID End
- 3 Get status Heat Change and starttime 09-Jun-2026 21:25:47.743 from Billet Track Per Strand using Event ID End
- 3 Get status Heat Change and starttime 09-Jun-2026 22:10:11.077 from Billet Track Per Strand using Event ID End
- 3 Get status Heat Change and starttime 09-Jun-2026 22:55:56.047 from Billet Track Per Strand using Event ID End
- 3 Get status Heat Change and starttime 09-Jun-2026 23:59:21.797 from Billet Track Per Strand using Event ID End
- 3 Get status Heat Change and starttime 10-Jun-2026 06:35:36.820 from Billet Track Per Strand using Event ID End
- 3 Get status Heat Change and starttime 10-Jun-2026 07:31:44.713 from Billet Track Per Strand using Event ID End
- 3 Get status Heat Change and starttime 10-Jun-2026 08:27:55.107 from Billet Track Per Strand using Event ID End
- 3 Get status Heat Change and starttime 10-Jun-2026 09:22:47.143 from Billet Track Per Strand using Event ID End
- 3 Get status Heat Change and starttime 10-Jun-2026 10:15:46.103 from Billet Track Per Strand using Event ID End
- 3 Get status Heat Change and starttime 10-Jun-2026 11:08:23.763 from Billet Track Per Strand using Event ID End
- 3 Get status Heat Change and starttime 10-Jun-2026 12:01:03.180 from Billet Track Per Strand using Event ID End
- 3 Get status Heat Change and starttime 10-Jun-2026 12:53:25.720 from Billet Track Per Strand using Event ID End
- 3 Get status Heat Change and starttime 10-Jun-2026 13:47:29.727 from Billet Track Per Strand using Event ID End
- 3 Get status Heat Change and starttime 10-Jun-2026 14:43:58.810 from Billet Track Per Strand using Event ID End
- 3 Get status Heat Change and starttime 10-Jun-2026 15:39:37.213 from Billet Track Per Strand using Event ID End
- 3 Get status Heat Change, starttime 01-Jul-2026 00:00:06.437 AND Total Billet Count NULL from Billet Track Per Strand using Event ID End
- 3 Get status Heat Change, starttime 01-Jul-2026 00:07:15.397 AND Total Billet Count NULL from Billet Track Per Strand using Event ID End

Example call: `EXEC XStudio_Xbatch.dbo.XMES_CREATE_BILLETNO_USP @EventID='FFFF04BC-9EAC-4625-93F2-AEC7E4AFB8A7', @Status='Strand 5 Billet Generate'`
