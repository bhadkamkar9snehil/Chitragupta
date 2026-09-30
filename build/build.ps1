<#
Stages everything the installer ships into build\stage:
  api\      the .NET API (self-contained) with the console UI in wwwroot
  engine\   embedded Python + pyodbc, the application code, and the WinSW service host
  gbrain\   gbrain.exe (Bun-compiled, pinned) and the prebuilt knowledge index (brain.zip)
Downloads are cached in build\cache (Python embeddable, WinSW, ODBC driver, the GBrain source).
Run build-brain.ps1 first when the knowledge index has not been built yet.
#>
param([string]$Version = "0.1.0")
$ErrorActionPreference = 'Stop'
$root = Split-Path $PSScriptRoot -Parent
$cache = "$PSScriptRoot\cache"; $stage = "$PSScriptRoot\stage"
$pyVersion = "3.14.4"; $gbrainTag = "v0.50.5.0"
New-Item -ItemType Directory -Force $cache | Out-Null

function Get-Cached([string]$Url, [string]$Name) {
    $path = "$cache\$Name"
    if (-not (Test-Path $path)) { Write-Host "downloading $Name"; Invoke-WebRequest $Url -OutFile $path -UseBasicParsing }
    $path
}

Remove-Item $stage -Recurse -Force -ErrorAction SilentlyContinue
New-Item -ItemType Directory -Force "$stage\api", "$stage\engine", "$stage\gbrain" | Out-Null

Write-Host "== console"
npm --prefix "$root\l1-ui" ci --silent
npm --prefix "$root\l1-ui" run build
Write-Host "== api"
dotnet publish "$root\L1\api" -c Release -r win-x64 --self-contained true -o "$stage\api" --nologo -v q
Copy-Item "$root\l1-ui\out" "$stage\api\wwwroot" -Recurse

Write-Host "== python"
$embed = Get-Cached "https://www.python.org/ftp/python/$pyVersion/python-$pyVersion-embed-amd64.zip" "python-embed.zip"
Expand-Archive $embed "$stage\engine\python"
$pth = Get-ChildItem "$stage\engine\python\python*._pth"
# The embeddable Python ignores PYTHONPATH and the script directory: list the application folders in its ._pth.
((Get-Content $pth) -replace '^#import site', 'import site') + '..\app' + '..\app\Model_Bench' | Set-Content $pth
python -m pip install --quiet --target "$stage\engine\python\Lib\site-packages" --only-binary=:all: --platform win_amd64 --python-version ($pyVersion -replace '\.\d+$') --implementation cp -r "$root\build\requirements.txt"

Write-Host "== application"
$app = "$stage\engine\app"
robocopy "$root\Model_Bench" "$app\Model_Bench" /E /XD __pycache__ results e2e /XF "test_*.py" *.pyc /NFL /NDL /NJH /NJS | Out-Null
robocopy "$root\deploy" "$app\deploy" /E /NFL /NDL /NJH /NJS | Out-Null
robocopy "$root\Knowledge" "$app\Knowledge" /E /XD vendor_docs_extracted world view_docs /NFL /NDL /NJH /NJS | Out-Null
Copy-Item "$root\Hermes_Orchestrator.py" $app

Write-Host "== service host"
Copy-Item (Get-Cached "https://github.com/winsw/winsw/releases/download/v2.12.0/WinSW-x64.exe" "WinSW-x64.exe") "$stage\engine\ChitraguptaEngine.exe"
Copy-Item "$PSScriptRoot\ChitraguptaEngine.xml" "$stage\engine\ChitraguptaEngine.xml"

Write-Host "== gbrain"
$src = "$cache\gbrain-src"
if (-not (Test-Path $src)) { git clone --quiet --depth 1 --branch $gbrainTag https://github.com/garrytan/gbrain $src }
Push-Location $src
bun install --silent
bun build --compile --outfile "$stage\gbrain\gbrain.exe" src/cli.ts
Pop-Location
Copy-Item "$stage\gbrain\gbrain.exe" "$cache\gbrain.exe" -Force  # build-brain.ps1 uses the same binary
if (-not (Test-Path "$cache\brain.zip")) { throw "No knowledge index yet: run build\build-brain.ps1 -LmStudio <url>." }
Copy-Item "$cache\brain.zip" "$stage\gbrain\brain.zip"

Write-Host "== first-run configuration template"
[ordered]@{
    gbrain = [ordered]@{ url = "http://127.0.0.1:3131"; client_id = (Get-Content "$cache\brain.client")[0].Trim(); client_secret = (Get-Content "$cache\brain.client")[1].Trim() }
} | ConvertTo-Json | Set-Content "$stage\chitragupta.json" -Encoding utf8
Set-Content "$stage\version.txt" $Version
Write-Host "staged: $([int]((Get-ChildItem $stage -Recurse -File | Measure-Object Length -Sum).Sum / 1MB)) MB"
