import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

export const GET: APIRoute = async () => {
  const allPosts = await getCollection('blog');
  
  const searchData = allPosts.map(post => ({
    slug: post.slug,
    title: post.data.title,
    description: post.data.description,
    category: post.data.category,
    image: post.data.image,
  }));
  
  return new Response(JSON.stringify(searchData), {
    headers: { 'Content-Type': 'application/json' }
  });
};