---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: rm-sales-order part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## RM_Sales_Order.Customer -> XBatch_Customer_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Customer-XBatch_Customer_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Sales_Order.MaterialGrade -> Steel_Grade_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: MaterialGrade-Steel_Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## RM_Sales_Order.MaterialID -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: MaterialID-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
