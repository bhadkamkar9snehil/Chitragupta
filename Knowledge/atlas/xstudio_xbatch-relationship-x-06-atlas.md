---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: X part 6

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## XMES_Work_Order_Trn_Tbl.WorkOrder -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: WorkOrder-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Xstudio_Xbatch_ChargingPlan_Mst_Tbl.Stackid -> XBatch_Storage_Area_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Stackid-XBatch_Storage_Area_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
