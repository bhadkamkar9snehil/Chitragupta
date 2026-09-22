---
type: note
subtype: configured-relationship
database: XStudio_Configuration_Xbatch
authority: configuration-observed
---
# XBatch configured relationships: electrical-shift-b-check-list part 1

Configured joins and cardinality. They are routing knowledge; verify current ticket rows live.

## Electrical_Shift_B_Check_List.ContractManpower -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: ContractManpower-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Electrical_Shift_B_Check_List.NameofElectrician -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: NameofElectrician-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))

## Electrical_Shift_B_Check_List.NameofEngineers -> XStudio_User_Mst_Tbl.ID
Databases: XStudio_XBatch -> XStudio_Configuration_XBatch
Cardinality: Many -> One
Relation: NameofEngineers-XStudio_User_Mst_Tbl
Provenance: xstudio_configuration_relationship (1 source row(s))
