---
type: procedure
title: "XMES_CCM_BILLET_CUT_USP"
built: "2026-09-24T11:36:36"
---

# XMES_CCM_BILLET_CUT_USP

Parameters: @EventID varchar, @Status varchar.

## Writes

- XMES_CCM_Billet_Genealogy_Trn_Tbl: BilletNo, BilletSequence, CutEndTime, CutEventID, CutStartTime, HeatNo, Source, Status, StrandNo, StrandSequence
- XMES_CCM_Billet_Sequence_New: CurrentSequence, HeatNo, Source, StrandNo, StrandSequence

## Reads

- Billet_Track_Per_Strand: EndTime, HeatNo, ID, StartTime, Status
- BilletsCastCount: HeatID, IsDeleted, StartTime, WorkFlowStatus
- XMES_CCM_Billet_Sequence_New: IsDeleted
