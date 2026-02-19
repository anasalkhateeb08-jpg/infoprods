with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace('style="z-index:2"', 'class="z-10"')
with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(content)
print("OK")
