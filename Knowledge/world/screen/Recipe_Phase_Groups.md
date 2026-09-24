---
type: screen
title: "Recipe Phase Groups"
built: "2026-09-24T11:36:36"
---

# Recipe Phase Groups

XStudio screen (menu 'Recipe Phase Groups', page List_Page_XBatch_Recipe_Phase_Group_Mst_Tbl, list view List_XBatch_Recipe_Phase_Group_Mst_Tbl).
Shows rows of XStudio_List_XBatch_Recipe_Phase_Group_Mst_Tbl_Vw.
Filter: only rows where ('<request.PGTargetType>' = 0 and ParentID IN (SELECT ID From XStudio_XBatch.dbo.XBatch_Recipe_Operation_Mst_Tbl)) or
('<request.PGTargetType>' = 1 and ParentID in('<request.OperationID>'))
