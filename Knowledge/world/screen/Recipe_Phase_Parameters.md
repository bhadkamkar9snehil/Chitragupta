---
type: screen
title: "Recipe Phase Parameters"
built: "2026-09-24T11:36:36"
---

# Recipe Phase Parameters

XStudio screen (menu 'Recipe Phase Parameters', page List_Page_XBatch_Recipe_Phase_Parameter_Mst_Tbl, list view List_XBatch_Recipe_Phase_Parameter_Mst_Tbl).
Shows rows of XStudio_List_XBatch_Recipe_Phase_Parameter_Mst_Tbl_Vw.
Filter: only rows where ('<request.PhaseParameterTargetType>' = 0 and ParentID IN (SELECT ID From XStudio_XBatch.dbo.XBatch_Recipe_Phase_Mst_Tbl)) or
('<request.PhaseParameterTargetType>' = 1 and ParentID in('<request.PhaseID>'))
