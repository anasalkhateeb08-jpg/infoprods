import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

export const GET: APIRoute = async ({ url }) => {
  const category = url.searchParams.get('category');
  
  if (!category) {
    return new Response(JSON.stringify([]), {
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    });
  }

  const posts = await getCollection('blog', ({ data }) => {
    return data.category === category;
  });

  const images = posts
    .filter(post => post.data.image)
    .map(post => post.data.image);

  return new Response(JSON.stringify(images), {
    status: 200,
    headers: { 'Content-Type': 'application/json' }
  });
};
