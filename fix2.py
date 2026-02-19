import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add categoryImages to frontmatter
old_fm = "const rightPosts = [...shuffled].sort(() => 0.5 - Math.random());"
new_fm = """const rightPosts = [...shuffled].sort(() => 0.5 - Math.random());
const catList = [
  { name: 'Car Accessories & Care', href: '/categories/car-accessories-and-care', label: 'Car Accessories & Care', count: '2,000+ Products', fallback: '/images/car-car-accessories.jpg' },
  { name: 'Technology & Devices', href: '/categories/technology-and-devices', label: 'Technology & Devices', count: '1,500+ Products', fallback: 'https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=600&q=80' },
  { name: 'Fitness & Health', href: '/categories/fitness-and-health', label: 'Fitness & Health', count: '2,000+ Products', fallback: 'https://images.unsplash.com/photo-1461896836934-ffe607ba8211?w=600&q=80' },
  { name: 'Outdoor & Survival', href: '/categories/outdoor-and-survival', label: 'Outdoor & Survival', count: 'Various Products', fallback: '/images/Outdoor & Survival.jpg' },
  { name: 'Sports & Sport Info', href: '/categories/sports-and-sport-info', label: 'Sports & Sport Info', count: '2,000+ Products', fallback: '/images/uploads/sportsinfo.webp' },
  { name: 'Jewelry', href: '/categories/jewelry', label: 'Jewelry & Accessories', count: '3,000+ Products', fallback: 'https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=600&q=80' },
  { name: 'Home', href: '/categories/home', label: 'Home & Decor', count: '4,000+ Products', fallback: 'https://images.unsplash.com/photo-1513694203232-719a280e022f?w=600&q=80' },
  { name: 'Kitchen', href: '/categories/kitchen', label: 'Kitchen & Gadgets', count: '2,500+ Products', fallback: 'https://images.unsplash.com/photo-1556911220-bff31c812dba?w=600&q=80' },
  { name: 'Beauty', href: '/categories/beauty', label: 'Beauty & Skincare', count: '1,800+ Products', fallback: 'https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=600&q=80' },
];
const categoryImages: Record<string, string[]> = {};
for (const cat of catList) {
  const imgs = allPosts.filter((p:any) => p.data.category === cat.name && p.data.image).map((p:any) => p.data.image).slice(0, 8);
  categoryImages[cat.name] = imgs.length > 0 ? imgs : [cat.fallback];
}"""

if old_fm in content:
    content = content.replace(old_fm, new_fm)
    print("Step 1: OK")
else:
    print("Step 1: NOT FOUND")

# 2. Replace grid content
old_grid = '''        <div class="grid grid-cols-3 md:grid-cols-2 lg:grid-cols-4 gap-2">'''
new_grid = '''        <div class="grid grid-cols-3 md:grid-cols-2 lg:grid-cols-4 gap-2">
          {catList.map((cat) => {
            const imgs = categoryImages[cat.name] || [cat.fallback];
            return (
              <a href={cat.href} class="group relative h-28 md:h-64 rounded-lg md:rounded-2xl overflow-hidden hover:scale-105 transition-transform duration-300">
                {imgs.map((src, i) => (
                  <img src={src} alt={cat.label} class={`cat-slide w-full h-full object-cover absolute top-0 left-0${i === 0 ? ' active' : ''}`} />
                ))}
                <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent flex flex-col justify-end p-2 md:p-6" style="z-index:2">
                  <h3 class="text-xs md:text-xl font-bold mb-0 md:mb-1 leading-tight">{cat.label}</h3>
                  <p class="text-[10px] md:text-sm text-gray-300 hidden md:block">{cat.count}</p>
                </div>
              </a>
            );
          })}'''

if old_grid in content:
    content = content.replace(old_grid, new_grid)
    print("Step 2: OK")
else:
    print("Step 2: NOT FOUND")

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(content)
print("Done")
