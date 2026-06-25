[CmdletBinding()]
param(
    [string]$CodexHome = $(if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" })
)

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent $PSScriptRoot
$source = Join-Path $repoRoot "skills"
$destination = Join-Path $CodexHome "skills"

New-Item -ItemType Directory -Force -Path $destination | Out-Null
Get-ChildItem -Directory -LiteralPath $source | ForEach-Object {
    $target = Join-Path $destination $_.Name
    if (Test-Path -LiteralPath $target) {
        Remove-Item -Recurse -Force -LiteralPath $target
    }
    Copy-Item -Recurse -Force -LiteralPath $_.FullName -Destination $target
}

Get-ChildItem -Directory -Recurse -Filter "__pycache__" -LiteralPath $destination |
    Remove-Item -Recurse -Force
Get-ChildItem -Directory -Recurse -Filter ".runtime" -LiteralPath $destination |
    Remove-Item -Recurse -Force

Write-Host "Installed skills into: $destination"
Write-Host "Run scripts/setup-pdf-to-markdown.ps1 to enable local PDF conversion."
Write-Host "Restart Codex or VSCodium after installation."
