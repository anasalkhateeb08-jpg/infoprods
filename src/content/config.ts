import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    author: z.string().default('InfoProds Team'),
    date: z.date(),
    image: z.string().optional(),
    category: z.string(),
    tags: z.array(z.string()).optional(),
  }),
});

const devices = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    brand: z.string(),
    deviceType: z.string(),
    releaseDate: z.date().optional(),
    price: z.string().optional(),
    image: z.string().optional(),
  }),
});

export const collections = { blog, devices };