---
type: screen
title: "Units"
built: "2026-09-24T11:36:36"
---

# Units

XStudio screen 'Units' (Unit; page List_Page_XBatch_Unit_Mst_Tbl, list view List_XBatch_Unit_Mst_Tbl).
Shows rows of XStudio_List_XBatch_Unit_Mst_Tbl_Vw.
Filter: only rows where ('<request.UnitTargetType>' = 0 and ParentID IN (SELECT ID From XStudio_XBatch.dbo.XBatch_Process_Cell_Mst_Tbl)) or
('<request.UnitTargetType>' = 1 and ParentID in('<request.CellID>'))
