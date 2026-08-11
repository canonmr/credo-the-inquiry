// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';

// https://astro.build/config
export default defineConfig({
  site: 'https://canonmr.github.io',
  base: '/credo-the-inquiry/',
  output: 'static',
  trailingSlash: 'ignore',
  integrations: [mdx()],
  build: {
    inlineStylesheets: 'auto',
  },
  vite: {
    server: {
      fs: {
        // Allow Astro to read content from sibling project folders if needed.
        strict: true,
      },
    },
  },
  i18n: {
    defaultLocale: 'id',
    locales: ['id', 'en'],
    routing: {
      prefixDefaultLocale: true,
      redirectToDefaultLocale: false,
    },
  },
});
