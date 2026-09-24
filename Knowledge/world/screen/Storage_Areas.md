---
type: screen
title: "Storage Areas"
built: "2026-09-24T11:36:36"
---

# Storage Areas

XStudio screen 'Storage Areas' (Storage Area; page List_Page_XBatch_Storage_Area_Mst_Tbl, list view List_XBatch_Storage_Area_Mst_Tbl).
Shows rows of XStudio_List_XBatch_Storage_Area_Mst_Tbl_Vw.
Filter: only rows where ('<request.SATargetType>' = 0 and ParentID IN (SELECT ID From XStudio_XBatch.dbo.XBatch_Store_Mst_Tbl)) or
('<request.SATargetType>' = 1 and ParentID in('<request.StoreID>'))
