param(
    [switch]$Online
)

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[Console]::OutputEncoding = $utf8NoBom
$OutputEncoding = $utf8NoBom
$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"

$pythonCommand = $null
$pythonPrefix = @()
if (Get-Command python -ErrorAction SilentlyContinue) {
    $pythonCommand = (Get-Command python).Source
}
elseIf (Get-Command py -ErrorAction SilentlyContinue) {
    $pythonCommand = (Get-Command py).Source
    $pythonPrefix = @("-3")
}
elseIf (Get-Command python3 -ErrorAction SilentlyContinue) {
    $pythonCommand = (Get-Command python3).Source
}
else {
    Write-Error "找不到 Python 3.9+。請勿自動安裝；改由 Codex 執行 README.md 所述的唯讀人工檢查。"
    exit 1
}

function Invoke-PythonCheck {
    param(
        [Parameter(Mandatory = $true)][string]$Script,
        [string[]]$Arguments = @()
    )
    & $pythonCommand @pythonPrefix $Script @Arguments
    if ($LASTEXITCODE -ne 0) {
        exit $LASTEXITCODE
    }
}

Write-Output "Platform: Windows"
Invoke-PythonCheck -Script (Join-Path $repoRoot "doctor.py")
Invoke-PythonCheck -Script (Join-Path $repoRoot "security_scan.py")
$linkArguments = @()
if ($Online) { $linkArguments += "--online" }
Invoke-PythonCheck -Script (Join-Path $repoRoot "link_check.py") -Arguments $linkArguments
Write-Output "Windows checks passed."
