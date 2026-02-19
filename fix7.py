with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    content = f.read()

old = '''        <div class="grid grid-cols-3 md:grid-cols-2 lg:grid-cols-4 gap-2">
         <!-- Car Accessories & Care -->'''

new = '''        <div class="grid grid-cols-3 md:grid-cols-2 lg:grid-cols-4 gap-2">
          {catList.map((cat) => (
            <a href={cat.href} class="category-card group relative h-28 md:h-64 rounded-lg md:rounded-2xl overflow-hidden hover:scale-105 transition-transform duration-300">
              <div class="slideshow-container absolute inset-0">
                {categoryImages[cat.name].map((imgSrc, index) => (
                  <img src={imgSrc} alt={cat.label} class={index === 0 ? "slide active" : "slide"} loading={index === 0 ? "eager" : "lazy"} />
                ))}
              </div>
              <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent flex flex-col justify-end p-2 md:p-6 z-10">
                <h3 class="text-xs md:text-xl font-bold mb-0 md:mb-1 leading-tight">{cat.label}</h3>
                <p class="text-[10px] md:text-sm text-gray-300 hidden md:block">{cat.count}</p>
              </div>
            </a>
          ))}
        </div>
         <!-- REMOVED_OLD_CARDS'''

if old in content:
    content = content.replace(old, new)
    print("Step 1 OK")
else:
    print("Step 1 NOT FOUND")

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(content)
