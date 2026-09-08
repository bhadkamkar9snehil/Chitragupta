---
type: Reference
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: H

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## Heat_Chemistry_Quality_Data.Grade -> Grade_Master.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: Grade-Grade_Master
Provenance: xstudio_configuration_relationship (1 source row(s))

## Heat_Chemistry_Quality_Data.HeatNo -> EAF_PER_HEAT.ID
Databases: XStudio_XBatch -> XStudio_XBatch
Cardinality: Many -> One
Relation: HeatNo-EAF_PER_HEAT
Provenance: xstudio_configuration_relationship (1 source row(s))

## Heat_Chemistry_Quality_Data.ModifiedBy -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration
Cardinality: Many -> One
Relation: ModifiedBy-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Heat_End_Selection_Trn_Tbl.ModifiedBy -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: ModifiedBy-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

