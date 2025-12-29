import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import rehypeSlug from 'rehype-slug';
import rehypeAutolinkHeadings from 'rehype-autolink-headings';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://infoprods.com',
  vite: {
    plugins: [tailwindcss()],
  },
  markdown: {
    rehypePlugins: [
      rehypeSlug,
      [rehypeAutolinkHeadings, { behavior: 'append' }],
    ],
  },
  integrations: [sitemap()],
});