# Hermes L2 Bundle Validation

- OKF validator: **PASS**
- Stored procedures in full install: **20**
- Unique stored procedures: **20**
- Routing regression cases: **9/9 PASS**

## Routing regression cases

| Ticket | Expected | Got | Pass |
|---|---|---|---|
| Heat 12345 production is not posting to SAP | `sap_posting` | `sap_posting` | Yes |
| Transaction 3F8... failed and has an API response error | `api_transaction` | `api_transaction` | Yes |
| Work order 50001234 is missing or not released | `work_order` | `work_order` | Yes |
| Heat 12345 is visible in EAF but missing in CCM | `heat_execution` | `heat_execution` | Yes |
| Billet 123456 is not available in billet yard / rolling | `billet_inventory` | `billet_inventory` | Yes |
| Chemistry result or usage decision is not reflected | `quality` | `quality` | Yes |
| OEE/delay value is wrong for yesterday | `performance` | `performance` | Yes |
| Ticket workflow reply/close status is wrong | `helpdesk_ticket` | `helpdesk_ticket` | Yes |
| Unclassified cross-domain MES fault | `discover` | `discover` | Yes |

## SQL static checks

- All expected Hermes procedure definitions are present once in the full-install script.
- The package was not executed against the LMEL SQL Server in this session; live deployment must run `sql/99_postflight.sql`.
- Helpdesk `Status` / `AskStatus` semantics are intentionally not invented from the truncated snapshot. Run `Hermes_L2_Discover_Helpdesk_Workflow_Usp` after deployment.
