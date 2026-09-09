---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: ccm-section-strands part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## CCM_Section_Strands.Grade -> Grade_Master.GradeName
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Grade-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## CCM_Section_Strands.MouldOperatorStrand1 -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: MouldOperatorStrand1-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## CCM_Section_Strands.MouldOperatorStrand2 -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: MouldOperatorStrand2-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## CCM_Section_Strands.MouldOperatorStrand3 -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: MouldOperatorStrand3-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## CCM_Section_Strands.MouldOperatorStrand4 -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: MouldOperatorStrand4-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## CCM_Section_Strands.MouldOperatorStrand5 -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: MouldOperatorStrand5-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## CCM_Section_Strands.MouldOperatorStrand6 -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: MouldOperatorStrand6-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
