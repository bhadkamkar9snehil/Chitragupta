---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: xbatch-sales-order-mst-tbl part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## XBatch_Sales_Order_Mst_Tbl.ApprovedBy -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: ApprovedBy-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Sales_Order_Mst_Tbl.Grade -> Grade_Master.GradeName
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Grade-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Sales_Order_Mst_Tbl.ItemID -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ItemID-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Sales_Order_Mst_Tbl.ParentID -> XBatch_Customer_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-XBatch_Customer_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Sales_Order_Mst_Tbl.Status -> XBatch_Status_Mst_Tbl.Name
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Status-XBatch_Status_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XBatch_Sales_Order_Mst_Tbl.UnitID -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: UnitID-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
