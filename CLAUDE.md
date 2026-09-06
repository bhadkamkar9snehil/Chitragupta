# Claude Entry Point — Chitragupta

Read `AGENTS.md` first.

Hermes owns the agent harness. GBrain owns the shared XStudio knowledge/retrieval platform. Chitragupta owns deterministic Helpdesk lifecycle rules and the typed XStudio evidence boundary.

Current key invariants:

- `l2_pipeline_runtime.py` is the only lifecycle mutation authority.
- L1 and L2 share `~/.hermes/xstudio-gbrain`; do not create duplicate brains.
- L2 workers use native read-only GBrain MCP tools, not a custom recall plugin.
- `xstudio-l2-tools` exposes only `xstudio_l2`.
- Current-ticket claims require live `xstudio_l2` evidence.
- Full schema/SP reference documents are authoritative and preserved.
- GBrain owns embeddings, graph, source sync and maintenance/autopilot.
- Chitragupta materializes reviewed outcomes and governed Solutions; it does not build another memory framework.
- The Windows SQL bridge remains until WSL-native SQL access is proven equivalent.
- Delete benchmark, migration, wrapper and compatibility code when its real caller disappears.

Validate with:

```bash
bash Model_Bench/validate_l2_pipeline_local.sh
```
