# Run locally on the publisher's Windows computer AFTER GitHub Pages is enabled.
# This never publishes releases. Keep the private signing key OUTSIDE both GitHub repositories.
param([Parameter(Mandatory=$true)][string]$GameSourceRoot)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path $GameSourceRoot).Path
$script = Join-Path $root 'scripts\configure-publisher.js'
if (-not (Test-Path $script)) { throw 'Expected v13.4.4 updater source: configure-publisher.js missing' }
if (-not (Get-Command node -ErrorAction SilentlyContinue)) { throw 'Install Node.js 22 first' }
$privateDir = Join-Path $HOME 'NFF-private-publisher-keys'
$desktopFeed = 'https://tre2k3.github.io/martin-no-filter-fighters-updates/updates/stable/'
$mediaManifest = 'https://tre2k3.github.io/martin-no-filter-fighters-updates/content/manifest.json'
Write-Host "Publisher feed: $desktopFeed"
Write-Host "Signing key storage (private): $privateDir"
& node $script $desktopFeed $mediaManifest $privateDir
if ($LASTEXITCODE -ne 0) { throw 'Publisher configuration failed' }
Write-Host 'Local source configured. DO NOT ship until signed installer and real installed-upgrade testing succeed.'
