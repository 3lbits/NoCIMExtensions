$ErrorActionPreference = "Stop"
Push-Location $PSScriptRoot

if (-not (Test-Path "venv")) {
    Write-Host "Creating virtual environment..."
    python -m venv venv
}

Write-Host "Activating virtual environment..."
. .\venv\Scripts\Activate.ps1

Write-Host "Installing dependencies..."
pip install -r requirements.txt

Write-Host "Installing cim4 CLI tool in editable mode..."
pip install -e .

Write-Host ""
Write-Host "Ready. Usage:"
Write-Host "  cim4 --help"

Pop-Location
