---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: xmes-billet-vs-gls-grade-mapping part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## XMES_Billet_VS_GLS_Grade_Mapping.BilletGrade -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: BilletGrade-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_VS_GLS_Grade_Mapping.EndproductGrade -> Grade_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EndproductGrade-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_VS_GLS_Grade_Mapping.GLSGrade -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: GLSGrade-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
