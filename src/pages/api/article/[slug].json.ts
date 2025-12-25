import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

export async function getStaticPaths() {
  const posts = await getCollection('blog');
  return posts.map(post => ({
    params: { slug: post.slug }
  }));
}

export const GET: APIRoute = async ({ params }) => {
  const { slug } = params;
  
  const posts = await getCollection('blog');
  const post = posts.find(p => p.slug === slug);

  if (!post) {
    return new Response(JSON.stringify({ error: 'Post not found' }), {
      status: 404,
      headers: { 'Content-Type': 'application/json' }
    });
  }

  return new Response(JSON.stringify({
    slug: post.slug,
    title: post.data.title,
    description: post.data.description,
    image: post.data.image,
    category: post.data.category
  }), {
    headers: { 'Content-Type': 'application/json' }
  });
};