content = open('src/pages/index.astro', 'r', encoding='utf-8').read()
old = open('src/pages/index.astro', 'r', encoding='utf-8').read()

old_script = """  <script>
    document.addEventListener('DOMContentLoaded', async () => {
      const categories = document.querySelectorAll('[data-category]');

      for (const card of categories) {
        const category = card.dataset.category;
        const img = card.querySelector('img');

        try {
          const response = await fetch(/api/category-images?category=);
          const images = await response.json();

          if (images.length > 1) {
            let currentIndex = 0;
            setInterval(() => {
              currentIndex = (currentIndex + 1) % images.length;
              img.src = images[currentIndex];
            }, 2000);
          }
        } catch (error) {
          console.error(Error loading images for :, error);
        }
      }
    });
  </script>"""

new_script = """  <script>
    document.addEventListener("DOMContentLoaded", () => {
      const grid = document.getElementById("categories-grid");
      if (!grid) return;
      const allCatImages = JSON.parse(grid.dataset.images || "{}");
      grid.querySelectorAll("[data-category]").forEach(card => {
        const images = allCatImages[card.dataset.category] || [];
        if (images.length < 2) return;
        const firstImg = card.querySelector("img");
        firstImg.style.cssText += ";position:absolute;top:0;left:0;width:100%;height:100%;object-fit:cover;opacity:1;transition:opacity 1s ease;z-index:1;";
        images.slice(1).forEach(src => {
          const img = document.createElement("img");
          img.src = src;
          img.style.cssText = "position:absolute;top:0;left:0;width:100%;height:100%;object-fit:cover;opacity:0;transition:opacity 1s ease;z-index:1;";
          card.appendChild(img);
        });
        let idx = 0;
        const slides = card.querySelectorAll("img");
        setInterval(() => {
          slides[idx].style.opacity = "0";
          idx = (idx + 1) % slides.length;
          slides[idx].style.opacity = "1";
        }, 5000);
      });
    });
  </script>"""

if old_script in content:
    content = content.replace(old_script, new_script)
    open('src/pages/index.astro', 'w', encoding='utf-8').write(content)
    print('SUCCESS')
else:
    print('NOT FOUND')
