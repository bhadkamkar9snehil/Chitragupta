---
type: screen
title: "List_XBatch_Batch_Phase_Mst_Tbl"
built: "2026-09-24T11:36:36"
---

# List_XBatch_Batch_Phase_Mst_Tbl

XStudio screen 'List_XBatch_Batch_Phase_Mst_Tbl' (Batch Phase; page List_Page_XBatch_Batch_Phase_Mst_Tbl, list view List_XBatch_Batch_Phase_Mst_Tbl).
Shows rows of XStudio_List_XBatch_Batch_Phase_Mst_Tbl_Vw.
Filter: only rows where ('<request.BatchPhaseTargetType>' = 0 and ParentID IN (SELECT ID From XStudio_XBatch.dbo.XBatch_Batch_Phase_Group_Mst_Tbl)) or
('<request.BatchPhaseTargetType>' = 1 and ParentID in('<request.BatchPhaseGroupID>'))
