---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: per-heat-ladleno part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## Per_Heat_LadleNo.EAFShellNo -> XMES_Life_Element_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: EAFShellNo-XMES_Life_Element_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Per_Heat_LadleNo.LadleNo -> XMES_Life_Element_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: LadleNo-XMES_Life_Element_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Per_Heat_LadleNo.TundishNo -> XMES_Life_Element_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: TundishNo-XMES_Life_Element_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
