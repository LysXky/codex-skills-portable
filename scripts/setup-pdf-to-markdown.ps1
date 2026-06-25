[CmdletBinding()]
param(
    [string]$CodexHome = $(if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" }),
    [string]$Python = "python"
)

$ErrorActionPreference = "Stop"
$skill = Join-Path $CodexHome "skills\pdf-to-markdown"
$runtime = Join-Path $skill ".runtime"
$requirements = Join-Path $skill "requirements.txt"

if (-not (Test-Path -LiteralPath $requirements)) {
    throw "pdf-to-markdown is not installed at $skill"
}

& $Python -m venv $runtime
$runtimePython = Join-Path $runtime "Scripts\python.exe"
& $runtimePython -m pip install --upgrade pip
& $runtimePython -m pip install -r $requirements
& $runtimePython -m pip check
& $runtimePython -m markitdown --version

Write-Host "PDF conversion runtime installed at: $runtime"
