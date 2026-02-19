with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    content = f.read()
old = '<img src={src} alt={cat.label} class={`cat-slide w-full h-full object-cover absolute top-0 left-0${i === 0 ? \' active\' : \'\'}`} />'
new = '<img src={src} alt={cat.label} class={"cat-slide w-full h-full object-cover absolute top-0 left-0" + (i === 0 ? " active" : "")} />'
if old in content:
    content = content.replace(old, new)
    print("OK")
else:
    print("NOT FOUND - trying alternative")
    import re
    content = re.sub(r'<img src=\{src\}[^\n]+cat-slide[^\n]+/>', '<img src={src} alt={cat.label} class={"cat-slide w-full h-full object-cover absolute top-0 left-0" + (i === 0 ? " active" : "")} />', content)
    print("REGEX DONE")
with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(content)
