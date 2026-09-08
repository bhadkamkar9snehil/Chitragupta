# XBatch World Knowledge Design

## Purpose

Give the Hermes L2 harness a deterministic, provenance-bearing map of the
XStudio XBatch world and machine-readable investigation recipes. The local
model interprets a bounded evidence package; it does not discover schemas,
relationships, or investigation order from scratch.

This extends the existing semantic atlas, manifest, typed tools, dispatch
bundle, frozen proposal, and reviewer lifecycle. It does not create another
registry or lifecycle authority.

## Boundaries

- `Knowledge/xstudio_semantic_atlas.json` remains the generated canonical
  machine-readable atlas.
- `Knowledge/manifest.json` remains the route/catalog authority.
- Git-tracked source snapshots and curated recipe definitions are authority;
  GBrain is a derived retrieval index.
- Ticket facts still require current audited SQL evidence.
- No agent receives SQL credentials or database transport details.
- No new ticket mutation path, queue, reviewer lifecycle, or publisher is
  introduced.
- LM Studio and Ollama are interchangeable embedding compute providers, not
  knowledge authorities and not availability fallbacks for one another.
- One GBrain instance uses one pinned primary embedding signature. Changing
  provider or model requires a complete provider-aware re-embedding.

## Authoritative inputs

| Input | Authority | Contribution |
|---|---|---|
| XBatch schema export | Mechanically observed | Objects, columns and types |
| XBatch procedure export | Mechanically observed | Parameters, safety and object dependencies |
| XStudio configuration relationship snapshot | Mechanically observed | Source/target attributes, database and cardinality |
| View catalog and definitions | Mechanically observed/curated | UI/reporting projections and dependencies |
| Verified domain documents | Curated with provenance | Meaning, aliases, invariants and pitfalls |
| `Knowledge/manifest.json` | Canonical configuration | Ticket routes and preferred evidence leads |

The configuration snapshot contains active rows from
`XStudio_Configuration_Xbatch.dbo.XStudio_EntityRelations_Mst_Tbl`, resolved
through `XStudio_Entities_Mst_Tbl` and `XStudio_Attribute_Mst_Tbl`. Deleted
rows are excluded. Secrets and operational ticket data are never exported.

## Canonical atlas

Atlas schema version 2 adds these top-level collections without removing the
existing `databases` contract:

- `relationships`: normalized source object/attribute to target
  database/object/attribute edges with cardinality and source provenance;
- `domains`: route-derived concepts, keywords, identifiers, knowledge
  documents and preferred live objects;
- `recipes`: validated machine-readable investigation and review contracts.

Every edge has a stable deterministic ID. Duplicate configuration rows that
describe the same semantic edge collapse to one edge while retaining source
row counts. Dangling objects or attributes remain visible as validation
errors; the builder never invents replacements.

Generated Markdown pages are derived from the atlas and grouped into bounded
object and domain pages. They are searchable in GBrain, but the JSON atlas and
its Git inputs remain authoritative.

## Recipe contract

Each recipe contains:

- `recipe_id`, `route`, `description` and `ticket_signals`;
- recognized `identifiers` with aliases and validation patterns;
- ordered `probes` naming existing typed tools and required inputs;
- `required_evidence` groups with acceptable object/operation alternatives;
- `interpretation_rules` that distinguish observations from causal claims;
- `stop_conditions` and `escalation_conditions`;
- `review_checks` mapping proposal claims to required evidence categories.

Recipes may select existing high-level tools such as
`xstudio_heat_context`, `xstudio_sap_api_context`, and
`xstudio_work_order_context`. A recipe cannot contain arbitrary SQL or a
write operation.

## Runtime flow

1. The dispatcher routes only from requester/ticket-owned fields.
2. It selects one primary recipe plus bounded secondary recipe IDs.
3. It injects a compact world context: route, identifiers, relevant objects,
   direct atlas neighbours and required evidence.
4. Existing deterministic high-level tools collect current audited evidence.
5. The investigator receives the compact context and evidence, then produces
   the existing frozen proposal.
6. Before reviewer creation, the harness creates an evidence matrix from the
   proposal claims and recorded action references.
7. The reviewer receives the frozen proposal, recipe checks, evidence matrix,
   and current reviewer-owned live context where already supported.
8. Existing deterministic approve/rework/escalate/publish behavior remains
   unchanged.

The evidence matrix is advisory for semantic adequacy in the first slice. It
must not reject a proposal merely because a recipe does not yet cover a valid
unusual investigation. Structural claim-reference validation remains the
hard deterministic gate.

## Failure behavior

- Missing or invalid recipe data fails validation and deployment.
- Unknown routes use a minimal `discover` recipe and expose no invented
  domain semantics.
- Dangling relationship edges fail the atlas build unless explicitly marked
  as an external configuration target.
- Missing GBrain embeddings prevent production claims under the existing
  readiness contract, but do not prevent atlas generation or validation.
- Embedding-provider changes are maintenance operations and never occur while
  L2 work owns the global WIP slot.

## Acceptance criteria

1. All existing 563 XBatch objects and 388 procedures remain represented.
2. The committed relationship snapshot contains all active configuration
   relationships and regenerates deterministically.
3. Every normalized relationship has provenance, endpoints and cardinality.
4. Every manifest route resolves to exactly one validated recipe.
5. Recipes expose only registered typed read-only tools.
6. Dispatch context includes bounded recipe/world context without increasing
   model context or iteration limits.
7. Reviewer cards contain a deterministic evidence matrix tied to the frozen
   proposal and recorded action references.
8. Existing lifecycle, SQL safety, audit, WIP, budget, rework and publisher
   tests remain green.
9. Generated artifacts pass check-mode reproducibility.
10. GBrain sync and retrieval evaluation pass after the generated pages are
    indexed with one pinned embedding signature.

