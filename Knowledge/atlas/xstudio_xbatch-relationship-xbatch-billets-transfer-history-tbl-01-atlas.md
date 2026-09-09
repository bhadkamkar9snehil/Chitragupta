---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: xbatch-billets-transfer-history-tbl part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## XBatch_Billets_Transfer_History_Tbl.ActionBy -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: LocationAssignBy-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Billets_Transfer_History_Tbl.InventoryID -> XBatch_Material_Inventory_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: InventoryID-XBatch_Material_Inventory_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Billets_Transfer_History_Tbl.OutwardBy -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: OutwardBy-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
