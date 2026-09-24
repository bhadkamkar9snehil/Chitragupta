---
type: procedure
title: "XBatch_Get_Tag_Mapping_Entries_By_Page_Type_Usp"
built: "2026-09-24T11:36:36"
---

# XBatch_Get_Tag_Mapping_Entries_By_Page_Type_Usp

Parameters: @PageType varchar, @ID varchar.
Builds SQL at runtime; some of what it touches is only visible in its text.

## Reads

- Equipment_Type_Mst_Tbl: ID, IsDeleted, Name
- XBatch_Connection_Capability_Mst_Tbl: ID, IsDeleted, ParentID
- XBatch_Connection_Interlock_Error_Mst_Tbl: DataSourceID, ID, IsDeleted, Name, ParentID, TagName, Type
- XBatch_Connection_Parameter_Mst_Tbl: DataSourceID, ID, IsDeleted, Name, ParentID, TagName, Type
