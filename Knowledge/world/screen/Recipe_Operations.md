---
type: screen
title: "Recipe Operations"
built: "2026-09-24T11:36:36"
---

# Recipe Operations

XStudio screen (menu 'Recipe Operations', page List_Page_XBatch_Recipe_Operation_Mst_Tbl, list view List_XBatch_Recipe_Operation_Mst_Tbl).
Shows rows of XStudio_List_XBatch_Recipe_Operation_Mst_Tbl_Vw.
Filter: only rows where ('<request.OperationTargetType>' = 0 and ParentID IN (SELECT ID From XStudio_XBatch.dbo.XBatch_Recipe_Unit_Procedure_Mst_Tbl)) or
('<request.OperationTargetType>' = 1 and ParentID in('<request.ProcedureID>'))
