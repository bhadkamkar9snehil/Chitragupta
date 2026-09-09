---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: Q part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## Quality_Deviation_Master.Product -> Product_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Product-Product_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## Quality_Deviation_Master.Size -> Size_Nominal_Wt_Value_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Size-Size_Nominal_Wt_Value_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## Quality_Spectro_Result.SampleID -> Quality_Spectro_Sample.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: SampleID-Quality_Spectro_Sample
Provenance: xstudio_configuration_relationship (1 source row(s))
