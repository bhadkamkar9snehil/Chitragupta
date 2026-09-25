# RepoPad

RepoPad is a small native Windows WPF control surface for applying checked-in repository update scripts.

The application reads:

`%LOCALAPPDATA%\RepoPad\repos.json`

Each repository entry contains an id, label, local path, checked-in PowerShell apply script, accent and optional URL. Chitragupta's `apply-helpdesk-update.ps1` publishes RepoPad into a versioned LocalAppData directory and creates `RepoPad.lnk` on the Desktop.

## Interaction model

RepoPad is intentionally closer to a physical macropad than a generic launcher:

- each repository is a tactile APPLY key with visible press travel;
- repository colors come from the JSON configuration;
- the selected repository is shown on the monitor before execution;
- the command monitor streams the actual PowerShell output;
- the status LED distinguishes ready/running/failure;
- Open app, Open folder and Clear log are secondary hardware-style keys;
- repository slots are assigned A01, A02, and so on as more repositories are added.

The executable requests Administrator elevation through its application manifest. Child PowerShell apply scripts inherit the elevated token.

The UI is configuration-driven so additional repositories become additional keys without changing execution logic.
