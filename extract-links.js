import { readdirSync, readFileSync, writeFileSync } from 'fs';
import { join } from 'path';

const affiliateLinks = [];
const blogPath = './src/content/blog';

try {
  const files = readdirSync(blogPath);
  
  for (const file of files) {
    if (file.endsWith('.md')) {
      const filePath = join(blogPath, file);
      const content = readFileSync(filePath, 'utf-8');
      
      // نبحث عن كل روابط AliExpress
      const regex = /<a[^>]*href="(https:\/\/s\.click\.aliexpress\.com\/e\/[^"]+)"[^>]*>([\s\S]*?)<\/a>/gi;
      let match;
      
      while ((match = regex.exec(content)) !== null) {
        const url = match[1];
        const innerHtml = match[2];
        
        // استخراج اسم المنتج
        let productName = 'AliExpress Product';
        
        const nameMatch = innerHtml.match(/<\/span>\s*([^<]+)/i);
        if (nameMatch && nameMatch[1].trim()) {
          productName = nameMatch[1].trim();
        } else {
          const cleanText = innerHtml.replace(/<[^>]+>/g, ' ').trim();
          if (cleanText) {
            productName = cleanText.slice(0, 100);
          }
        }
        
        // تحقق من عدم التكرار
        if (!affiliateLinks.some(link => link.url === url)) {
          affiliateLinks.push({
            url: url,
            title: productName,
            category: "General"
          });
        }
      }
    }
  }
  
  // حفظ في JSON
  writeFileSync(
    './src/data/affiliateLinks.json',
    JSON.stringify(affiliateLinks, null, 2),
    'utf-8'
  );
  
  console.log('✅ تم استخراج', affiliateLinks.length, 'رابط وحفظهم في affiliateLinks.json');
  
} catch (e) {
  console.error('❌ خطأ:', e.message);
}