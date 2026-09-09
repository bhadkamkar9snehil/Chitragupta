---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: mes-raw-material-consumptions-trn-tbl part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## MES_Raw_Material_Consumptions_Trn_Tbl.ParentID -> MES_Raw_Material_Consumptions_Mapping_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ParentID-MES_Raw_Material_Consumptions_Mapping_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## MES_Raw_Material_Consumptions_Trn_Tbl.SalesOrder -> XBatch_Sales_Order_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: SalesOrder-XBatch_Sales_Order_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## MES_Raw_Material_Consumptions_Trn_Tbl.Unit -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Unit-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
