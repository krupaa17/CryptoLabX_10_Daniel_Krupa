param(
    [ValidateRange(1048576, 2147483647)]
    [int]$Bytes = 1048576,
    [string]$OutputDirectory = (Join-Path $PSScriptRoot "generated")
)

$ErrorActionPreference = "Stop"
New-Item -ItemType Directory -Force -Path $OutputDirectory | Out-Null

$buffer = New-Object byte[] $Bytes
$randomNumberGenerator = [System.Security.Cryptography.RandomNumberGenerator]::Create()
try {
    $randomNumberGenerator.GetBytes($buffer)
}
finally {
    $randomNumberGenerator.Dispose()
}

$outputPath = Join-Path $OutputDirectory "windows_dotnet_rng.bin"
[System.IO.File]::WriteAllBytes($outputPath, $buffer)

$actualSize = (Get-Item $outputPath).Length
if ($actualSize -ne $Bytes) {
    throw "Expected $Bytes bytes in $outputPath, got $actualSize."
}
Write-Output "${outputPath}: ${actualSize} bytes"
