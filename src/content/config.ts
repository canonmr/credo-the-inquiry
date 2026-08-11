import { defineCollection, z } from 'astro:content';

// ============================================================================
// Argument nodes (POE-001 through POE-NNN)
// ============================================================================
const argumentNodes = defineCollection({
  type: 'content',
  schema: z.object({
    id: z.string().regex(/^POE-\d{3}$/),
    layer: z.union([z.literal(1), z.literal(2), z.literal(3)]),
    title: z.string(),
    language: z.enum(['id', 'en']).optional().default('en'),
    speaker: z.string().nullable(),
    claim_type: z.string(),
    domain: z.string(),
    claim: z.string().min(1),
    definitions: z.record(z.string()),
    premises: z.array(z.string()).min(1),
    inference: z.string(),
    conclusion: z.string(),
    inference_status: z.enum(['VALID', 'INVALID', 'CONTESTED', 'REQUIRES_ADDITIONAL_PREMISE', 'UNDERDETERMINED']),
    hidden_assumptions: z.array(z.string()),
    strongest_objection: z.string(),
    strongest_response: z.string(),
    counter_response: z.string(),
    caveat: z.string(),
    what_this_argument_does_not_establish: z.array(z.string()),
    evidential_challenge: z.string(),
    defeat_condition: z.string(),
    related_nodes: z.array(z.string()),
    sources: z.array(z.string()),
    chapter_placement: z.string(),
    visual_treatment: z.string(),
    confidence: z.enum(['low', 'medium', 'high'])
  })
});

// ============================================================================
// Sources (data collection — pure structured records, no body content)
// ============================================================================
const sources = defineCollection({
  type: 'data',
  schema: z.object({
    source_id: z.string(),
    author: z.string(),
    title: z.string(),
    date: z.string(),
    source_type: z.enum([
      'primary-philosophical',
      'primary-theological',
      'church-document',
      'biblical-text',
      'patristic',
      'historical',
      'scholarly-secondary',
      'reference'
    ]),
    language: z.string(),
    edition: z.string(),
    location: z.string(),
    original_quote: z.string(),
    translation: z.string().optional(),
    paraphrase: z.string().optional(),
    verification_status: z.enum(['VERIFIED', 'PARTIALLY VERIFIED', 'UNVERIFIED', 'DISPUTED']),
    notes: z.string().optional(),
    supports_nodes: z.array(z.string()).optional(),
    changes: z.array(z.string()).optional()
  })
});

// ============================================================================
// Chapters (bilingual)
// ============================================================================
const chapters = defineCollection({
  type: 'content',
  schema: z.object({
    id: z.string(),
    title: z.string(),
    title_id: z.string().optional(),
    chapter_slug: z.string(),
    order: z.number(),
    language: z.enum(['id', 'en']),
    is_primary: z.boolean().optional(),
    nodes_used: z.array(z.string()),
    sources_used: z.array(z.string()),
    epistemic_ledger: z.object({
      established: z.array(z.string()),
      contested: z.array(z.string()),
      not_established: z.array(z.string())
    }),
    next_chapter: z.string().nullable()
  })
});

export const collections = {
  'argument-nodes': argumentNodes,
  sources: sources,
  chapters: chapters
};
