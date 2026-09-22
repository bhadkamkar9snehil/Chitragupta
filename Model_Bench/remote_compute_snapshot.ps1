$ErrorActionPreference = 'Stop'

$credentialPath = Join-Path $env:USERPROFILE '.hermes_infra_creds\desktop_pc.xml'
$credential = Import-Clixml -LiteralPath $credentialPath

Invoke-Command -ComputerName 100.111.69.102 -Credential $credential -ScriptBlock {
    $gpuLine = (& nvidia-smi --query-gpu=name,utilization.gpu,memory.used,memory.total,temperature.gpu,power.draw --format=csv,noheader,nounits | Select-Object -First 1)
    $gpu = @($gpuLine -split ',') | ForEach-Object { $_.Trim() }
    $processors = @(Get-CimInstance Win32_Processor)
    $operatingSystem = Get-CimInstance Win32_OperatingSystem
    $modelProcesses = @(Get-Process -ErrorAction SilentlyContinue | Where-Object {
        $_.ProcessName -match '^(LM Studio|lmstudio|lms|llama-server)$'
    })

    $totalMemoryMb = [math]::Round([double]$operatingSystem.TotalVisibleMemorySize / 1024, 0)
    $freeMemoryMb = [math]::Round([double]$operatingSystem.FreePhysicalMemory / 1024, 0)
    [pscustomobject]@{
        gpu_name = $gpu[0]
        gpu_util_pct = [int]$gpu[1]
        gpu_mem_used_mb = [int]$gpu[2]
        gpu_mem_total_mb = [int]$gpu[3]
        gpu_temperature_c = [int]$gpu[4]
        gpu_power_w = if ($gpu[5] -match '^[0-9.]+$') { [math]::Round([double]$gpu[5], 2) } else { $null }
        cpu_util_pct = [math]::Round(($processors | Measure-Object -Property LoadPercentage -Average).Average, 0)
        system_mem_used_mb = $totalMemoryMb - $freeMemoryMb
        system_mem_total_mb = $totalMemoryMb
        lmstudio_working_set_mb = [math]::Round(($modelProcesses | Measure-Object -Property WorkingSet64 -Sum).Sum / 1MB, 0)
    } | ConvertTo-Json -Compress
}
