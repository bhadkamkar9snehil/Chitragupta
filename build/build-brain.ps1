<#
Builds the knowledge index once: the generated XBatch world (Knowledge/world, committed) imported into a GBrain
PGLite brain with LM Studio embeddings, plus a read-only access token. Output: build/cache/brain.zip and
build/cache/brain.token. About half an hour; needs LM Studio serving the embedding model. Run when the world changes.
  build-brain.ps1 -LmStudio http://<host>:1234/v1
#>
param([Parameter(Mandatory)][string]$LmStudio, [string]$Gbrain = "$PSScriptRoot\cache\gbrain.exe")
$ErrorActionPreference = 'Stop'
$root = Split-Path $PSScriptRoot -Parent
$work = "$PSScriptRoot\cache\brain-work"
if (-not (Test-Path $Gbrain)) { throw "Build gbrain first (build.ps1 compiles it into build\cache\gbrain.exe)." }
Remove-Item $work -Recurse -Force -ErrorAction SilentlyContinue
New-Item -ItemType Directory -Force $work | Out-Null
$env:GBRAIN_HOME = $work
$env:LMSTUDIO_BASE_URL = $LmStudio
function G { & $Gbrain @args 2>&1 | Where-Object { $_ -notmatch 'UPGRADE_AVAILABLE|self-upgrade' } }

G init --pglite --embedding-model lmstudio:text-embedding-nomic-embed-text-v1.5 --embedding-dimensions 768 | Out-Null
$pack = "$work\.gbrain\schema-packs\xbatch-world"
New-Item -ItemType Directory -Force $pack | Out-Null
Copy-Item "$root\deploy\gbrain\xbatch-world\pack.yaml" "$pack\pack.yaml"
G schema validate xbatch-world
G schema use xbatch-world | Out-Null
G sources add xstudio-knowledge --path $root --name "XBatch world" --federated | Out-Null
G sync --source xstudio-knowledge --repo $root --src-subpath Knowledge/world --no-pull --no-extract --yes --json
G embed --stale --include-null-signature
# The typed links between pages (writes, reads, calls, ...): a second step after the import, through the same binary.
$env:CHITRAGUPTA_GBRAIN_BIN = $Gbrain; $env:CHITRAGUPTA_GBRAIN_HOME = $work; Remove-Item env:CHITRAGUPTA_GBRAIN_URL -ErrorAction SilentlyContinue
python "$root\Model_Bench\world_links.py"
if ($LASTEXITCODE -ne 0) { throw "world_links.py reported missing link endpoints." }
$token = [regex]::Match((G auth create chitragupta --scopes read | Out-String), 'gbrain_[A-Za-z0-9_\-]+').Value
if (-not $token) { throw "Could not create the access token." }
Set-Content "$PSScriptRoot\cache\brain.token" $token -NoNewline

# Ship the data, not the machine-specific bits (config.json holds an absolute path; the engine rewrites it).
$pkg = "$PSScriptRoot\cacherain-pkg"
Remove-Item $pkg -Recurse -Force -ErrorAction SilentlyContinue
robocopy "$work\.gbrain" "$pkg\.gbrain" /E /XF config.json .gbrain-resolve.sock /XD .gbrain-lock /NFL /NDL /NJH /NJS | Out-Null
$zip = "$PSScriptRoot\cacherain.zip"
Remove-Item $zip -ErrorAction SilentlyContinue
tar.exe -a -c -f $zip -C $pkg .gbrain  # Compress-Archive (5.1) rejects the pre-1980 timestamps inside PGLite
Write-Host "brain.zip $([int]((Get-Item $zip).Length / 1MB)) MB, token saved."
