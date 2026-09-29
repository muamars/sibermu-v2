# SiberMu

## Chatbot API

Widget chatbot memanggil endpoint same-origin `POST /api/chat`. `server/controllers/chatController.mjs` meneruskan payload `{ message, sessionId }` ke webhook n8n. Tujuan webhook dapat diatur melalui `CHAT_WEBHOOK_URL` (lihat `.env.example`).

Untuk production, build lalu jalankan server Node yang menyajikan `dist` sekaligus endpoint API:

```sh
npm run build
npm start
```

Untuk development, jalankan `npm start` dan `npm run dev` di terminal terpisah. Vite meneruskan `/api` ke server Node di port 3000.

Server membutuhkan Node.js 18 atau lebih baru.

This template should help get you started developing with Vue 3 and TypeScript in Vite. The template uses Vue 3 `<script setup>` SFCs, check out the [script setup docs](https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup) to learn more.

Learn more about the recommended Project Setup and IDE Support in the [Vue Docs TypeScript Guide](https://vuejs.org/guide/typescript/overview.html#project-setup).
