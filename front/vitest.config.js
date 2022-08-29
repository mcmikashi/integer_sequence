import {defineConfig} from 'vite'
import {svelte} from '@sveltejs/vite-plugin-svelte'

export default defineConfig({
  plugins: [svelte({hot: !process.env.VITEST})],
  test: {
    globals: true,
    deps: {
      inline: [
        "msw"
      ]
    },
    include: ['src/**/*.{test,spec}.{js,mjs,cjs,ts,mts,cts,jsx,tsx}'],
    environment: 'jsdom',
    setupFiles: ['./tests/setup.js'],
    coverage:{
      exclude : ['tests/*','src/**/*.spec.js'],
    }
  },
})