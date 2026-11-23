import { defineConfig } from 'astro/config';
import svelte from '@astrojs/svelte';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  site: 'https://iconstash.io',
  output: 'static',
  trailingSlash: 'always',
  build: {
    format: 'directory',
  },
  prefetch: {
    prefetchAll: false,
    defaultStrategy: 'hover',
  },
  integrations: [svelte()],
  vite: {
    plugins: [tailwindcss()],
    worker: {
      format: 'es',
    },
    build: {
      target: 'es2022',
    },
  },
});
