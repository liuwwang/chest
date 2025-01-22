$filePath = "文件地址"
$splitSize = 1MB
$fileName = [System.IO.Path]::GetFileNameWithoutExtension($filePath)
$fileExt = [System.IO.Path]::GetExtension($filePath)

$inputStream = [System.IO.File]::OpenRead($filePath)
$buffer = New-Object Byte[] ($splitSize)
$index = 0
$partNumber = 1

while (($bytesRead = $inputStream.Read($buffer, 0, $buffer.Length)) -gt 0) {
    $outputPath = "文件所在地址的文件夹\$fileName" + "_part$partNumber$fileExt"
    $outputStream = [System.IO.File]::OpenWrite($outputPath)
    $outputStream.Write($buffer, 0, $bytesRead)
    $outputStream.Close()
    $partNumber++
}

$inputStream.Close()