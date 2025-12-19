# سكريبت لإضافة FAQ Schema لجميع المقالات
# المسار: F:\site\files\infoprods-new

Write-Host "=== بدء معالجة المقالات ===" -ForegroundColor Green

# الحصول على جميع ملفات المقالات
$blogFiles = Get-ChildItem -Path "src/content/blog" -Filter "*.md" -File

Write-Host "تم العثور على $($blogFiles.Count) مقال" -ForegroundColor Cyan

$processedCount = 0
$skippedCount = 0
$errorCount = 0

foreach ($file in $blogFiles) {
    try {
        Write-Host "`nمعالجة: $($file.Name)" -ForegroundColor Yellow
        
        # قراءة محتوى الملف
        $content = Get-Content $file.FullName -Raw -Encoding UTF8
        
        # التحقق من وجود FAQ بالفعل في frontmatter
        if ($content -match '(?s)---.*?faqs:.*?---') {
            Write-Host "   يحتوي بالفعل على FAQs - تم التخطي" -ForegroundColor Gray
            $skippedCount++
            continue
        }
        
        # البحث عن قسم FAQ في المحتوى
        if ($content -match '(?s)##\s*(?:Frequently Asked Questions|FAQ)\s*\n(.*?)(?=\n##|\z)') {
            $faqSection = $matches[1]
            
            # استخراج الأسئلة والأجوبة
            $questions = @()
            
            # نمط البحث: Q: سؤال؟ متبوعاً بـ A: جواب
            $pattern = '(?s)(?:\*\*)?Q:\s*(.+?)\?(?:\*\*)?\s*\n\s*(?:\*\*)?A:\s*(.+?)(?=\n\s*(?:\*\*)?Q:|$)'
            
            $matches = [regex]::Matches($faqSection, $pattern)
            
            foreach ($match in $matches) {
                $question = $match.Groups[1].Value.Trim()
                $answer = $match.Groups[2].Value.Trim()
                
                # تنظيف النص
                $question = $question -replace '\s+', ' '
                $answer = $answer -replace '\s+', ' '
                $answer = $answer -replace '\n', ' '
                
                if ($question -and $answer) {
                    $questions += @{
                        question = $question + "?"
                        answer = $answer
                    }
                }
            }
            
            if ($questions.Count -gt 0) {
                Write-Host "   تم العثور على $($questions.Count) سؤال" -ForegroundColor Green
                
                # إنشاء YAML للـ FAQs
                $faqYaml = "faqs:`n"
                foreach ($q in $questions) {
                    $faqYaml += "  - question: `"$($q.question -replace '"', '\"')`"`n"
                    $faqYaml += "    answer: `"$($q.answer -replace '"', '\"')`"`n"
                }
                
                # إضافة FAQs إلى frontmatter
                $content = $content -replace '(---\s*\n(?:.*?\n)*?)(---)', "`$1$faqYaml`$2"
                
                # حفظ الملف المعدل
                $content | Set-Content -Path $file.FullName -Encoding UTF8 -NoNewline
                
                Write-Host "   تم إضافة FAQs بنجاح!" -ForegroundColor Green
                $processedCount++
            } else {
                Write-Host "   لم يتم العثور على أسئلة صالحة" -ForegroundColor Yellow
                $skippedCount++
            }
        } else {
            Write-Host "  - لا يحتوي على قسم FAQ" -ForegroundColor Gray
            $skippedCount++
        }
        
    } catch {
        Write-Host "   خطأ: $($_.Exception.Message)" -ForegroundColor Red
        $errorCount++
    }
}

Write-Host "`n=== انتهت المعالجة ===" -ForegroundColor Green
Write-Host "تمت المعالجة: $processedCount مقال" -ForegroundColor Green
Write-Host "تم التخطي: $skippedCount مقال" -ForegroundColor Yellow
Write-Host "أخطاء: $errorCount مقال" -ForegroundColor Red
