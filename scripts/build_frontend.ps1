param(
    [switch]$SkipTests
)

$ErrorActionPreference = "Stop"
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

$ProjectRoot = Split-Path -Parent $PSScriptRoot
$FrontendRoot = Join-Path $ProjectRoot "frontend"
$TempRoot = Join-Path $ProjectRoot ".tmp"

if (-not (Test-Path $FrontendRoot)) {
    throw "Frontend directory not found: $FrontendRoot"
}
if (-not (Test-Path $TempRoot)) {
    New-Item -ItemType Directory -Path $TempRoot | Out-Null
}

$NodeCommand = Get-Command node.exe -ErrorAction SilentlyContinue
$NpmCommand = Get-Command npm.cmd -ErrorAction SilentlyContinue
$NodePath = if ($NodeCommand) { $NodeCommand.Source } else { "" }
$NpmPath = if ($NpmCommand) { $NpmCommand.Source } else { "" }

if (-not $NodeCommand -or -not $NpmCommand) {
    Write-Host "Node.js is not on PATH. Preparing a project-local LTS runtime..."
    $Releases = Invoke-RestMethod -Uri "https://nodejs.org/dist/index.json"
    $Release = $Releases |
        Where-Object { $_.lts -and ($_.files -contains "win-x64-zip") } |
        Select-Object -First 1
    if (-not $Release) {
        throw "No Windows x64 Node.js LTS release was found."
    }

    $Version = $Release.version
    $ArchiveName = "node-$Version-win-x64.zip"
    $RuntimeName = "node-$Version-win-x64"
    $ArchivePath = Join-Path $TempRoot $ArchiveName
    $RuntimePath = Join-Path $TempRoot $RuntimeName

    if (-not (Test-Path $ArchivePath)) {
        Write-Host "Downloading Node.js $Version from nodejs.org..."
        Invoke-WebRequest -UseBasicParsing -Uri "https://nodejs.org/dist/$Version/$ArchiveName" -OutFile $ArchivePath
    }
    if (-not (Test-Path $RuntimePath)) {
        Write-Host "Expanding Node.js $Version..."
        Expand-Archive -LiteralPath $ArchivePath -DestinationPath $TempRoot
    }

    $NodePath = Join-Path $RuntimePath "node.exe"
    $NpmPath = Join-Path $RuntimePath "npm.cmd"
}

$NodeRoot = Split-Path -Parent $NodePath
$env:Path = "$NodeRoot;$env:Path"
Write-Host "Using Node.js $(& $NodePath --version)"
Write-Host "Using npm $(& $NpmPath --version)"

Push-Location $FrontendRoot
try {
    Write-Host "Installing frontend dependencies..."
    & $NpmPath install --registry=https://registry.npmmirror.com
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Mirror install failed. Retrying with the official npm registry..."
        & $NpmPath install --registry=https://registry.npmjs.org
        if ($LASTEXITCODE -ne 0) {
            throw "Frontend dependency installation failed."
        }
    }

    if (-not $SkipTests) {
        Write-Host "Running frontend tests..."
        & $NpmPath test -- --run
        if ($LASTEXITCODE -ne 0) {
            throw "Frontend tests failed."
        }
    }

    Write-Host "Checking TypeScript..."
    & $NpmPath run typecheck
    if ($LASTEXITCODE -ne 0) {
        throw "Frontend type checking failed."
    }

    Write-Host "Building production frontend..."
    & $NpmPath run build
    if ($LASTEXITCODE -ne 0) {
        throw "Frontend production build failed."
    }
}
finally {
    Pop-Location
}

$Output = Join-Path $FrontendRoot "dist\index.html"
if (-not (Test-Path $Output)) {
    throw "Frontend build did not create $Output"
}
Write-Host "Frontend build complete: $Output"
