$ErrorActionPreference = 'Stop'
$src = $args[0]
$out = $args[1]
$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false
try {
    $wb = $excel.Workbooks.Open($src, $false, $true)
    $wb.ExportAsFixedFormat(0, $out)
    $wb.Close($false)
    Write-Output "PDF -> $out"
} finally {
    $excel.Quit()
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($excel) | Out-Null
}