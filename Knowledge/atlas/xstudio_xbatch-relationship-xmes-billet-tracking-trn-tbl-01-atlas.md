---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: xmes-billet-tracking-trn-tbl part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## XMES_Billet_Tracking_Trn_Tbl.Materialid -> XBatch_Material_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Materialid-XBatch_Material_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_Tracking_Trn_Tbl.ProcessStage -> XMES_Process_Stage_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: ProcessStage-XMES_Process_Stage_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_Tracking_Trn_Tbl.Qualitygradeid -> XBatch_Material_Grade_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Qualitygradeid-XBatch_Material_Grade_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_Tracking_Trn_Tbl.StatePosition -> XMES_State_Position_State_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: StatePosition-XMES_State_Position_State_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## XMES_Billet_Tracking_Trn_Tbl.UOMID -> XBatch_Measurement_Unit_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: UOMID-XBatch_Measurement_Unit_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
