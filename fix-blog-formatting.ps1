# Fix blog post formatting
$blogFolder = "src\content\blog"
$files = Get-ChildItem -Path $blogFolder -Filter "*.md"

Write-Host "Found $($files.Count) articles" -ForegroundColor Cyan

foreach ($file in $files) {
    Write-Host "Processing: $($file.Name)" -ForegroundColor Yellow
    
    $content = Get-Content $file.FullName -Raw -Encoding UTF8
    $originalContent = $content
    
    # Remove ** from around headings at start and end of lines
    $content = $content -replace '(?m)^\*\*\s*(.+?)\s*\*\*\s*$', '$1'
    
    # Add ## to headings that start with numbers or "Introduction"
    $content = $content -replace '(?m)^(Introduction:.+)$', '## $1'
    $content = $content -replace '(?m)^(\d+\..+)$', '## $1'
    
    if ($content -ne $originalContent) {
        Set-Content -Path $file.FullName -Value $content -Encoding UTF8 -NoNewline
        Write-Host "Fixed!" -ForegroundColor Green
    } else {
        Write-Host "No changes" -ForegroundColor Gray
    }
}

Write-Host "Done!" -ForegroundColor Green