# World build: ways it can fail (written before the code)

Checked by `Model_Bench/e2e/run_world.py` against the built world in GBrain and live XBatch.

1. **False key links from common values.** Small integers, status codes, "0", "1", dates and
   GUID-less flags appear everywhere; linking on them joins unrelated tables. Only values of 5+
   characters count, and a link needs many shared values, not one.
2. **Missed key links from sampling different time windows.** Two tables holding heats but sampled
   from different months share nothing. Samples come from each table's most recent rows so windows
   line up; the plant snapshot ends 2026-07-08.
3. **Framework columns** (ID, ParentID, CreatedBy, ModifiedBy, AssignedUserID ...) link every table
   to every other. Excluded by how many tables carry the column, not by a name list.
4. **One key swallowing another.** Heat 1604014 and billet 1604014_S1_29 share a prefix; exact
   values only, never prefixes, when grouping.
5. **Known joins missing.** Must contain, without hand-typing: CCM_Per_Heat.HeatID,
   EAF_PER_HEAT.HeatID, XMES_CCM_Billet_Genealogy_Trn_Tbl.HeatNo in one key;
   XMES_SAP_API_UsageDecision_Error.HeatNo in it too.
6. **Writers missing.** Every acceptance chain of `build_process_world.py` must exist as a GBrain
   `writes`/`reads` link.
7. **Stale world.** Pages carry the build time; a build older than the procedure definitions'
   last change is reported.
8. **Duplicate or orphan pages.** Re-running the build must not duplicate links; every link endpoint
   must be a page.
9. **Slow build or slow lookups.** Build bounded (per-query timeout, skips reported); `get_links` on
   a node within ~1 s.
10. **Brain pollution.** World pages live under `world/` only; the build never touches other pages.
