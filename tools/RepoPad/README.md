# RepoPad

RepoPad is a small native Windows WPF control surface for applying checked-in repository update scripts.

The application reads:

`%LOCALAPPDATA%\RepoPad\repos.json`

Each repository entry contains an id, label, local path, checked-in PowerShell apply script, accent and optional URL. Chitragupta's `apply-helpdesk-update.ps1` publishes RepoPad into a versioned LocalAppData directory and creates `RepoPad.lnk` on the Desktop.

## Interaction model

The surface is intentionally narrow:

1. choose a repository key;
2. press **APPLY**;
3. watch the actual PowerShell output;
4. finish on **READY** or **FAILED**.

The design keeps the useful physical cues—key travel, status LED, inset enclosure and hardware-style secondary keys—without duplicating the same operation in decorative labels or stage indicators.

- Repository colors come from the JSON configuration.
- The selected repository and local path are always visible before execution.
- The command monitor is unwrapped so terminal output remains readable.
- Open app, Folder and Clear are secondary actions and are disabled while an apply is running.
- Repository slots are assigned A01, A02 and so on as more repositories are added.

The executable requests Administrator elevation through its application manifest. Child PowerShell apply scripts inherit the elevated token.

The UI is configuration-driven so additional repositories become additional keys without adding another execution path.
