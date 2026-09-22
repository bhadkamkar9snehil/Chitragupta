# XStudio_Xbatch.dbo.Billet_Cross_Section

**table_kind:** production_data

### What this table is for

- **Curated domain match (billet_inventory):** Billet missing, wrong location/furnace/yard/transfer, genealogy, count, or weight issue.
  (source: `Knowledge/xstudio_semantic_atlas.json` domains, human-curated, not inferred)
- **Indexed under investigation keywords:** billets, cast, catalog, core, count, data, entities, entity, flow, from, highlights, insert, routing, sohar, xlsx (source: `Knowledge/table_keyword_index.json`, human-curated)
- **Inferred from its own column names** (not human-verified): columns repeatedly reference cross, section, weight, billet, material, specific.

**Primary Key:** ID  
**Row Count:** 10  
**Date Range (ModifiedOn):** 2025-08-28T17:15:22.0000000 to 2026-06-20T19:32:44.0000000  

### Schema

| Column | Data Type | Nullable | Length/Precision | Default |
| --- | --- | --- | --- | --- |
| ID | varchar | NO | 36 | (newid()) |
| MaterialSpecificWeight | decimal | YES | 18,4 | — |
| CreatedBy | varchar | YES | 36 | — |
| ModifiedBy | varchar | YES | 36 | — |
| CreatedOn | datetime | YES | — | (getdate()) |
| ModifiedOn | datetime | YES | — | — |
| IsDeleted | bit | YES | — | ((0)) |
| IsSystem | bit | YES | — | ((0)) |
| AssignedUserID | varchar | YES | 36 | — |
| HostAddress | varchar | YES | 100 | — |
| DbSyncStatus | varchar | YES | 500 | — |
| MobileSyncStatus | varchar | YES | 100 | — |
| Source | varchar | YES | 20 | — |
| CrossSection | varchar | YES | 100 | — |
| CrossSection1 | int | YES | 10,0 | — |
| BilletWeight | decimal | YES | 18,4 | — |

### Top 10 Records

| ID | MaterialSpecificWeight | CreatedBy | ModifiedBy | CreatedOn | ModifiedOn | IsDeleted | IsSystem | AssignedUserID | HostAddress |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9F378E14-AAD8-4ABC-A4F4-77B42A2082B4 | 0.0780 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | 2025-08-28T17:15:22.2170000 | 2025-08-28T17:15:22.0000000 | False | False | NULL | 172.16.100.58 |
| A40B49BE-C8E3-47E6-A6A5-824C8B0E1352 | 0.1530 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-08-28T17:15:07.3900000 | 2025-09-18T15:36:52.0000000 | False | False | NULL |  |
| 80BC2EA6-69BC-48A0-9055-FA31DC36AC38 | 0.1750 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-08-28T17:14:41.7230000 | 2025-09-18T15:37:06.0000000 | False | False | NULL |  |
| CF14038D-8D47-4DCB-A192-724B79C0223D | 0.1320 | 49796991-BC00-4368-8182-B39E4E6BD4A6 | E85231EB-0A04-42D6-A407-328F17EADEFE | 2025-08-28T17:14:54.3800000 | 2025-09-18T15:40:25.0000000 | False | False | NULL |  |
| 2692FC9A-D648-4C30-9F06-D2E365EE10FF | 0.1770 | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 2026-04-11T00:43:08.9800000 | 2026-04-11T00:43:08.0000000 | False | False | NULL | 10.76.111.2 |
| 6B517A8B-4EC4-40DC-A1FA-0F78AA53C924 | 0.1770 | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 2026-04-11T07:41:40.7300000 | 2026-04-11T07:41:40.0000000 | False | False | NULL |  |
| D6F7928D-DFFE-4F2D-BD40-44BF2919A760 | 0.1760 | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 2026-04-17T08:07:44.0800000 | 2026-04-17T08:07:44.0000000 | False | False | NULL |  |
| BF53DB56-6A39-46FA-9C50-3CFAA702DA41 | 0.1770 | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 2026-04-21T18:35:58.6200000 | 2026-04-21T18:35:58.0000000 | False | False | NULL |  |
| 784FA6AF-2CA4-45EA-9D3E-7CD34A3B51B8 | 0.1760 | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 2026-05-06T18:08:53.0970000 | 2026-05-06T18:08:53.0000000 | False | False | NULL | 10.76.20.74 |
| 90513267-BC1F-4D23-B865-EDAA1F522812 | 0.1770 | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 4EA2C448-9996-458A-8181-AE5DB2C71CEB | 2026-06-20T19:32:44.0100000 | 2026-06-20T19:32:44.0000000 | False | False | NULL | 10.76.111.2 |

---

### Known relationships (from Knowledge/xstudio_semantic_atlas.json)

- `XStudio_XBatch.Billet_Cross_Section.CreatedBy` -> `XStudio_Configuration.XStudio_User_Mst_Tbl.ID` (Many to One)
