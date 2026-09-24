---
type: screen
title: "List_XBatch_Batch_Unit_Procedure_Mst_Tbl"
built: "2026-09-24T11:36:36"
---

# List_XBatch_Batch_Unit_Procedure_Mst_Tbl

XStudio screen 'List_XBatch_Batch_Unit_Procedure_Mst_Tbl' (Batch Unit Procedure; page List_Page_XBatch_Batch_Unit_Procedure_Mst_Tbl, list view List_XBatch_Batch_Unit_Procedure_Mst_Tbl).
Shows rows of XStudio_List_XBatch_Batch_Unit_Procedure_Mst_Tbl_Vw.
Filter: only rows where ('<request.BatchUpTargetType>' = 0 and ParentID IN (SELECT ID From XStudio_XBatch.dbo.XBatch_Batch_Mst_Tbl)) or
('<request.BatchUpTargetType>' = 1 and ParentID in('<request.BatchID>'))
