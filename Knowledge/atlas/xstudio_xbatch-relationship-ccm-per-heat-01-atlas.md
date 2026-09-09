---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: ccm-per-heat part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## CCM_Per_Heat.Grade -> Grade_Master.GradeName
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Grade-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## CCM_Per_Heat.SalesOrder -> XBatch_Sales_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: SalesOrder-XBatch_Sales_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## CCM_Per_Heat.SuperHeat -> CCM_Section_Strands.SuperHeat
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: SuperHeat-CCM_Section_Strands
Provenance: xstudio_configuration_relationship (1 source row(s))

## CCM_Per_Heat.WorkOrder -> XBatch_Work_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: WorkOrder-XBatch_Work_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
