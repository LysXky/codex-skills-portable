[CmdletBinding()]
param(
    [string]$CodexHome = $(if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" }),
    [string]$Python = "python"
)

$ErrorActionPreference = "Stop"
$projectRoot = $PSScriptRoot
$destination = Join-Path $CodexHome "skills\pdf-to-markdown"

New-Item -ItemType Directory -Force -Path (Split-Path $destination) | Out-Null
if (Test-Path -LiteralPath $destination) {
    Remove-Item -Recurse -Force -LiteralPath $destination
}
Copy-Item -Recurse -Force -LiteralPath (Join-Path $projectRoot "skill") -Destination $destination

& $Python -m venv (Join-Path $destination ".runtime")
$runtimePython = Join-Path $destination ".runtime\Scripts\python.exe"
& $runtimePython -m pip install --upgrade pip
& $runtimePython -m pip install -r (Join-Path $destination "requirements.txt")
& $runtimePython -m pip check

Write-Host "Installed pdf-to-markdown at: $destination"
