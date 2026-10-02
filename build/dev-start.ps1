<#
TEMPORARY, until the installer is used on this machine: starts the console and the engine from build\stage (each in a
small restart loop, because the engine exits on purpose to apply new Connections settings), then optionally opens the console.
Run at logon by the "Chitragupta" scheduled task; also behind the desktop icon.   dev-start.ps1 [-Open]
#>
param([switch]$Open)
$root = Split-Path $PSScriptRoot -Parent
$stage = "$root\build\stage"
$port = if ($env:CHITRAGUPTA_PORT) { $env:CHITRAGUPTA_PORT } else { "3417" }
if (Get-Service ChitraguptaEngine -ErrorAction SilentlyContinue) {
    $saved = Get-ItemProperty 'HKLM:\Software\Chitragupta' -Name ConsolePort -ErrorAction SilentlyContinue
    if ($saved.ConsolePort) { $port = $saved.ConsolePort }
    if ($Open) { Start-Process "http://localhost:$port/admin" }
    Write-Host 'Chitragupta is installed. Use its Windows services.'
    return
}

function Start-Loop([string]$Name, [string]$Exe, [string]$Arguments, [string]$WorkDir, [hashtable]$Env = @{}) {
    if (Get-CimInstance Win32_Process -Filter "Name='powershell.exe'" | Where-Object { $_.CommandLine -like "*Chitragupta-loop-$Name*" }) { return }
    $envLines = ($Env.GetEnumerator() | ForEach-Object { "`$env:$($_.Key) = '$($_.Value)'" }) -join '; '
    $loop = "# Chitragupta-loop-$Name`n$envLines`nSet-Location '$WorkDir'`nwhile (`$true) { & '$Exe' $Arguments; Start-Sleep 5 }"
    Start-Process powershell -WindowStyle Hidden -ArgumentList '-NoProfile', '-ExecutionPolicy', 'Bypass', '-Command', $loop
}

Start-Loop "api" "$stage\api\L1Api.exe" "" "$stage\api" @{ CHITRAGUPTA_PORT = $port }
Start-Loop "engine" "$stage\engine\python\python.exe" "'$stage\engine\app\Model_Bench\engine.py'" "$stage\engine\app\Model_Bench" @{
    PYTHONUNBUFFERED = "1"; CHITRAGUPTA_GBRAIN_BIN = "$stage\gbrain\gbrain.exe" }

if ($Open) {
    for ($i = 0; $i -lt 60; $i++) {
        try { Invoke-WebRequest "http://localhost:$port/" -UseBasicParsing -TimeoutSec 2 | Out-Null; break } catch { Start-Sleep 1 }
    }
    Start-Process "http://localhost:$port/admin"
}
