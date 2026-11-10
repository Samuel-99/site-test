import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://samuel-oliveira.ch',
  output: 'static',
  trailingSlash: 'always',
  server: { port: 4321 },
});
