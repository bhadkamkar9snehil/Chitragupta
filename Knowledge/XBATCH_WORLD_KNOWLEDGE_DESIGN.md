# XBatch World: a graph Jev walks one step at a time

Supersedes the 2026-09-09 atlas + recipe design. The live pipeline keeps using the atlas until the
walker replaces it; nothing here is wired into the lifecycle yet.

## Rule: no hand-written facts

Every node, link and key in the world is generated from XBatch itself: its catalog, its procedure
code, its own logs, its event configuration and its data. People and models write none of it.
Hand-written material is limited to *rules* (the link types, the roles Jev assigns) and *tests*.
If the generator cannot see something, the world says "unknown", it does not guess.

## Where it lives

GBrain (`~/.hermes/xstudio-gbrain`), source `world`, one page per node, typed links between them.

| Node page | Generated from |
|---|---|
| `world/table/<name>` | catalog: columns, types, row count; key columns (below) |
| `world/procedure/<name>` | definition: parameters, columns read/written, dynamic SQL; runtime log: runs, error steps |
| `world/event/<area>/<event>` | `<Area>_Event_Configuration/State/Action/Tag_Mapping` |
| `world/api/<name>` | config-DB API log (what each API inserts) |
| `world/job/<name>` | SQL Agent jobs and steps |
| `world/key/<name>` | a group of columns that hold the same identifier (below) |

| Link type (`add_link`, `context` = columns) | Meaning |
|---|---|
| `writes` / `reads` | procedure -> table, with the columns |
| `calls` | procedure -> procedure |
| `feeds` | api -> table |
| `records_to` | event -> table it writes |
| `runs` | job -> procedure |
| `holds` | table -> key, with the column (`CCM_Per_Heat.HeatID`) |

Pages give Jev plain words; links give Jev the next possible steps; `get_links` / `get_backlinks`
over one `gbrain serve` session keep each step fast. `process_world.json` stays as the build's
intermediate output, not a second source of truth.

## Keys: which columns hold the same identifier

Not typed in. Derived from values: for every identifier-like column (text <= 60 chars or integer,
values of 5+ characters) take the distinct values of the most recent rows (by the vendor's
`ModifiedOn`/`CreatedOn`), invert them into value -> columns, and link columns that share enough
values. Vendor relationships (`XStudio_EntityRelations_Mst_Tbl`) add the joins they declare.
Columns present on almost every table (framework audit columns) are excluded by frequency, not by
name. A key is a connected group of columns; its name is its most common column name.
This replaces the hand-typed lists in `entity_resolver.ENTITY_KINDS`, `evidence_walk.HEAT_COLUMNS`
and the bridge's fixed heat queries.

## The walk

1. **Start.** Code finds the identifier in the ticket and confirms which keys hold it (data check).
   The first options are the tables holding that value, plus GBrain search hits for the ticket text.
2. **Step.** The options are every link out of every node visited so far that is not yet visited,
   each written as one short line ("procedure XMES_CCM_BILLET_CUT_USP writes
   XMES_CCM_Billet_Genealogy_Trn_Tbl (HeatNo, BilletNo)"), plus `stop: explained` and
   `stop: not a data problem`. Jev picks exactly one.
3. **Look.** Code reads live data for the chosen node and this identifier:
   table -> its rows (Jev marks which columns matter); procedure -> its runtime-log runs mentioning
   the identifier (parameters, steps, error steps) and what it writes; event -> its condition and
   whether the row reached its state.
4. **Judge.** Jev assigns the observation a role: what the requester sees / stuck record / cause /
   unrelated. Then back to 2, up to a fixed number of steps.
5. **Result.** The trail (each step, what was seen, its role) is the evidence handed to the answer
   stage. Numbers are compared by code; Jev never does arithmetic.

## Tests (E2E only)

Failure modes are written before the code in `Model_Bench/e2e/WORLD_FAILURE_MODES.md` and
`WALK_FAILURE_MODES.md`. The thermometer runs real tickets through the real walk on live XBatch
with real Jev and scores the trail. Cases must include every failure class, not only SAP errors.
