# XBatch Helpdesk (L1)

The human front door to Chitragupta: plant users describe a problem, Jev decides whether to answer,
ask for details, or raise a ticket; L2's replies and questions come back here. See `AGENTS.md`.

Run both (or use the `l1-api` and `l1-ui` entries in `.claude/launch.json`):

```bash
dotnet run --project L1/api --launch-profile http
npm --prefix l1-ui run dev -- -p 3417
```

The API reads `MSSQL_MCP_SERVER/USER/PASSWORD`, `TYPESAFE_API_KEY`, and optionally `L1_LMSTUDIO_URL`,
`L1_QWEN_MODEL` from the environment. The UI reads `L1_API_URL` (default `http://127.0.0.1:5116`).

Check before committing: `npm run check && npm run build`.
