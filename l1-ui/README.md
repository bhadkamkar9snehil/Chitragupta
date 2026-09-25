# XBatch Helpdesk (L1)

Plant users describe a problem; Jev decides whether to answer (with XBatch world knowledge from GBrain), ask for
details, or raise a ticket for L2. L2's replies and questions come back here. Support staff use `/admin`.
See `AGENTS.md` for boundaries and surfaces.

Run both (or use the `l1-api` and `l1-ui` entries in `.claude/launch.json`):

```bash
dotnet run --project L1/api --launch-profile http
npm --prefix l1-ui run dev -- -p 3417
```

The API reads `MSSQL_MCP_SERVER/USER/PASSWORD` and `TYPESAFE_API_KEY` from the environment and needs WSL GBrain
(`~/.hermes/xstudio-gbrain`). The writer model is chosen in `/admin` → Settings → AI provider.
The UI reads `L1_API_URL` (default `http://127.0.0.1:5116`).

Embed in XStudio as a page control with Load URL as iFrame: `http://<host>:3417/?user={XStudioUserID}`.

Check before committing: `npm run check && npm run build`.
