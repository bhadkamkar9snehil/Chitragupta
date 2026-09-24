---
type: screen
title: "Storage Subareas"
built: "2026-09-24T11:36:36"
---

# Storage Subareas

XStudio screen (menu 'Storage Subareas', page List_Page_XBatch_Storage_Rack_Mst_Tbl, list view List_XBatch_Storage_Rack_Mst_Tbl).
Shows rows of XStudio_List_XBatch_Storage_Rack_Mst_Tbl_Vw.
Filter: only rows where ('<request.SRTargetType>' = 0 and ParentID IN (SELECT ID From XStudio_XBatch.dbo.XBatch_Storage_Area_Mst_Tbl)) or
('<request.SRTargetType>' = 1 and ParentID in('<request.StorageAreaID>'))
