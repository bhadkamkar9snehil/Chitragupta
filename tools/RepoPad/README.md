# RepoPad

RepoPad is a tiny Windows WPF utility that turns local repository maintenance into tactile "macropad" keys.

The application reads:

`%LOCALAPPDATA%\RepoPad\repos.json`

Each repository entry contains an id, label, local path, checked-in PowerShell apply script and optional URL. Chitragupta's `apply-helpdesk-update.ps1` publishes RepoPad into a versioned LocalAppData directory and creates `RepoPad.lnk` on the Desktop.

The executable requests Administrator elevation through its application manifest. Child PowerShell apply scripts therefore inherit the elevated token.

The UI is deliberately configuration-driven so additional repositories can become additional keys without redesigning the executable.
