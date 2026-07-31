$ErrorActionPreference = "Stop"

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = Split-Path -Parent $scriptRoot
$example = Join-Path $projectRoot "preferences.example.yaml"
$preferences = Join-Path $projectRoot "preferences.yaml"
$plans = Join-Path $projectRoot "plans"
$marker = Join-Path $projectRoot ".schedule-init.json"

if (Test-Path -LiteralPath $preferences) {
    Write-Output "KEEP: preferences.yaml"
}
else {
    Copy-Item -LiteralPath $example -Destination $preferences
    Write-Output "CREATE: preferences.yaml"
}

New-Item -ItemType Directory -Path $plans -Force | Out-Null

if (Test-Path -LiteralPath $marker) {
    Write-Output "KEEP: .schedule-init.json"
}
else {
    $payload = [ordered]@{
        schema_version = 1
        initialized = $true
        initialized_at = [DateTime]::UtcNow.ToString("o")
    }
    $payload | ConvertTo-Json | Set-Content -LiteralPath $marker -Encoding UTF8
    Write-Output "CREATE: .schedule-init.json"
}

Write-Output "Schedule project initialized. Ask for timezone before date planning."
