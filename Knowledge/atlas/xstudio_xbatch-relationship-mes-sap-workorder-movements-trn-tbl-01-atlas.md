---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: mes-sap-workorder-movements-trn-tbl part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## MES_SAP_WorkOrder_Movements_Trn_Tbl.ParentID -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
