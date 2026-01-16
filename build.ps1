Write-Host "Cleaning previous build..."
Remove-Item -Recurse -Force dist, build -ErrorAction SilentlyContinue

Write-Host "Building EXE using main.spec..."
pyinstaller main.spec

Write-Host "Build complete!"