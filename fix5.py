with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    content = f.read()

old = '''          {catList.map((cat) => {
            const imgs = categoryImages[cat.name] || [cat.fallback];
            return (
              <a href={cat.href} class="group relative h-28 md:h-64 rounded-lg md:rounded-2xl overflow-hidden hover:scale-105 transition-transform duration-300">
                  <img src={src} alt={cat.label} class={"cat-slide w-full h-full object-cover absolute top-0 left-0" + (i === 0 ? " active" : "")} />
                  <img src={src} alt={cat.label} class={"cat-slide w-full h-full object-cover absolute top-0 left-0" + (i === 0 ? " active" : "")} />
                ))}
                <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent flex flex-col justify-end p-2 md:p-6" style="z-index:2">
                  <h3 class="text-xs md:text-xl font-bold mb-0 md:mb-1 leading-tight">{cat.label}</h3>
                  <p class="text-[10px] md:text-sm text-gray-300 hidden md:block">{cat.count}</p>
                </div>
              </a>
            );
          })}'''

new = '''          {catList.map((cat) => (
            <a href={cat.href} class="group relative h-28 md:h-64 rounded-lg md:rounded-2xl overflow-hidden hover:scale-105 transition-transform duration-300">
              {(categoryImages[cat.name] || [cat.fallback]).map((src, i) => (
                <img src={src} alt={cat.label} class={"cat-slide w-full h-full object-cover absolute top-0 left-0" + (i === 0 ? " active" : "")} />
              ))}
              <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent flex flex-col justify-end p-2 md:p-6" style="z-index:2">
                <h3 class="text-xs md:text-xl font-bold mb-0 md:mb-1 leading-tight">{cat.label}</h3>
                <p class="text-[10px] md:text-sm text-gray-300 hidden md:block">{cat.count}</p>
              </div>
            </a>
          ))}'''

if old in content:
    content = content.replace(old, new)
    print("OK")
else:
    print("NOT FOUND")

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(content)
