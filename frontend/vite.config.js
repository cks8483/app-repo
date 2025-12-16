import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  build: {
    rollupOptions: {
      input: {
        // index.html의 위치를 절대 경로로 강제 지정합니다.
        main: path.resolve(__dirname, 'index.html'),
      },
    },
  },
})