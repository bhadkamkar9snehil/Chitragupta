---
type: screen
title: "Recipe Phases"
built: "2026-09-24T11:36:36"
---

# Recipe Phases

XStudio screen 'Recipe Phases' (Recipe Phase; page List_Page_XBatch_Recipe_Phase_Mst_Tbl, list view List_XBatch_Recipe_Phase_Mst_Tbl).
Shows rows of XStudio_List_XBatch_Recipe_Phase_Mst_Tbl_Vw.
Filter: only rows where ('<request.PhaseTargetType>' = 0 and ParentID IN (SELECT ID From XStudio_XBatch.dbo.XBatch_Recipe_Phase_Group_Mst_Tbl)) or
('<request.PhaseTargetType>' = 1 and ParentID in('<request.PhaseGroupID>'))
