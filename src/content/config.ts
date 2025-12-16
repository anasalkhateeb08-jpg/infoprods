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

    // --- Schema Fields (FAQ, HowTo, Product) ---
    faqs: z.array(z.object({
      question: z.string(),
      answer: z.string(),
    })).optional(),

    howToName: z.string().optional(),
    howToDescription: z.string().optional(),
    howToTime: z.string().optional(),
    howToSteps: z.array(z.object({
      name: z.string(),
      text: z.string(),
      image: z.string().optional(),
    })).optional(),
    
    productName: z.string().optional(),
    productDescription: z.string().optional(),
    productImage: z.string().optional(),
    productBrand: z.string().optional(),
    productRating: z.object({
      ratingValue: z.number(),
      reviewCount: z.number(),
      bestRating: z.number().optional(),
    }).optional(),
    productOffers: z.object({
      url: z.string(),
      priceCurrency: z.string(),
      price: z.string(),
      availability: z.string().optional(),
    }).optional(),
    // ---------------------------------------------

  }),
});

export const collections = { blog };