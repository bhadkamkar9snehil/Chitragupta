# Install Chitragupta on Windows

Use `Chitragupta-Setup.exe` for a new machine. It includes Microsoft ODBC Driver 18, the self-contained console/API, embedded Python, the engine service host, GBrain and the prebuilt knowledge index. Node, Python, Bun and the .NET SDK are build prerequisites only; they are not needed on the target.

## Requirements and installation

- Windows x64 and an administrator account. Windows Server 2025 was tested.
- An available TCP port (default **3417**) and access from console clients. The MSI creates its firewall rule.
- Network access to SQL Server and the configured LM Studio endpoint. Jev needs outbound HTTPS to TypeSafe. Knowledge search uses the local shipped index.
- Exactly one engine connected to a given Helpdesk database. Stop any development engine before installing. Keep additional test installations disconnected from SQL.

Run Setup as administrator, select the installation folder and console port, then open `http://127.0.0.1:3417/admin` (substitute the selected port). For unattended installation:

```powershell
& 'C:\Install\Chitragupta-Setup.exe' /install /quiet /norestart /log 'C:\Install\setup.log'
```

For a non-default port, install the included ODBC driver through Setup first, or use an existing Driver 18 installation and the MSI:

```powershell
Start-Process msiexec.exe -Wait -ArgumentList '/i','C:\Install\Chitragupta.msi','/qn','/norestart','PORT=3418','/l*v','C:\Install\install.log'
```

The current release is unsigned. A trusted code-signing certificate is still needed for signed distribution.

## Services and settings

| Item | Location or behavior |
|---|---|
| Console service | `ChitraguptaConsole`, automatic start; chosen HTTP port |
| Engine service | `ChitraguptaEngine`, automatic start; supervises GBrain |
| Installed payload | `C:\Program Files\Chitragupta` by default |
| Settings | `C:\ProgramData\Chitragupta\chitragupta.json` |
| Logs / index | `C:\ProgramData\Chitragupta\logs` / `gbrain` |
| GBrain | `http://127.0.0.1:3131`, generated credentials for this installation |

The installer restricts the settings/data directory to SYSTEM and Administrators. Connection secrets remain in that protected JSON file; they are not DPAPI-encrypted. The first-run template contains no connection secrets. GBrain credentials are generated locally before its single-process database is served.

In **Settings → Connections**, verify GBrain first, then configure and test LM Studio and Jev. Configure SQL last, once this machine is the sole intended engine owner. Save applies settings to the API and causes the engine service to restart. An unconfigured installation serves the console and knowledge without claiming tickets. Do not paste credentials into logs or source files.

If moving production execution to another machine, stop the old engine service before saving SQL credentials on the new one. A server installation with SQL unconfigured verifies packaging; it does not prove ticket processing.

## Upgrade, uninstall and checks

Run the newer Setup to upgrade. Settings and logs survive upgrades and uninstall; the console port is remembered. Setup removes services and its firewall rule when uninstalled. Retained ProgramData must be handled separately if you deliberately want to erase settings or knowledge.

```powershell
Get-Service ChitraguptaConsole,ChitraguptaEngine
Invoke-WebRequest 'http://127.0.0.1:3417/admin' -UseBasicParsing
Invoke-RestMethod 'http://127.0.0.1:3417/api/admin/connections/test/gbrain' -Method Post -ContentType application/json -Body '{}'
```

Use `127.0.0.1` for local checks: the GBrain listener uses IPv4, and `localhost` health probes timed out on the tested machines. Saving Connections and watching the engine PID change verifies restart-on-settings behavior. Both services have Windows recovery actions to restart after a failure.

The old `build\dev-start.ps1` launcher refuses to start development loops when the installed engine service exists. The disabled development logon task is not changed by this installation.

## Build a release

Run `build\build-brain.ps1` only when the generated knowledge world changes. Verify the index with `Model_Bench/e2e/run_world.py`; staging reuses the cached index. Stage separately from a running development copy:

```powershell
& 'C:\Users\Admin\Documents\Office\AIHelpdesk\build\build.ps1' -Version 0.1.1 -StageDir 'C:\Users\Admin\Documents\Office\AIHelpdesk\build\stage-release'
dotnet build 'C:\Users\Admin\Documents\Office\AIHelpdesk\installer\Package\Chitragupta.wixproj' -c Release -p:Version=0.1.1 -p:StageDir='C:\Users\Admin\Documents\Office\AIHelpdesk\build\stage-release'
dotnet build 'C:\Users\Admin\Documents\Office\AIHelpdesk\installer\Bundle\Setup.wixproj' -c Release -p:Version=0.1.1
```

Outputs are `installer\Bundle\bin\Release\Chitragupta-Setup.exe` and `installer\Package\bin\Release\Chitragupta.msi`. Keep hashes with the release artifacts. A successful build is followed by an elevated install, service/HTTP/knowledge checks, settings restart, upgrade retention and isolated uninstall/custom-port tests.
