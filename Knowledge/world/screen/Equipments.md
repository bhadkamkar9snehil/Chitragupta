---
type: screen
title: "Equipments"
built: "2026-09-24T11:36:36"
---

# Equipments

XStudio screen (menu 'Equipments', page List_Page_XBatch_Unit_Equipment_Mst_Tbl, list view List_XBatch_Unit_Equipment_Mst_Tbl).
Shows rows of XStudio_List_XBatch_Unit_Equipment_Mst_Tbl_Vw.
Filter: only rows where ('<request.UETargetType>' = 0 and ParentID IN (SELECT ID From XStudio_XBatch.dbo.XBatch_Unit_Mst_Tbl)) or
('<request.UETargetType>' = 1 and ParentID in('<request.unitID>'))
