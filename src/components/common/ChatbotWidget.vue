<script setup lang="ts">
import { LoaderCircle, Send, X } from '@lucide/vue'
import { nextTick, ref, watch } from 'vue'
import sahabatMu from '@/assets/SahabatMu.webp'

type ChatMessage = {
  id: number
  role: 'assistant' | 'user'
  text: string
}

const webhookUrl = 'http://10.50.50.61:5678/webhook/sibermu'
const sessionStorageKey = 'sibermu-chat-session-id'
const panelOpen = ref(false)
const draft = ref('')
const sending = ref(false)
const messages = ref<ChatMessage[]>([
  { id: 0, role: 'assistant', text: 'Halo! Saya asisten SiberMu. Ada yang bisa saya bantu?' },
])
const conversation = ref<HTMLElement | null>(null)
let nextMessageId = 1

function getSessionId() {
  let sessionId = window.localStorage.getItem(sessionStorageKey)
  if (!sessionId) {
    sessionId = `session_${Date.now()}_${Math.random().toString(36).slice(2, 12)}`
    window.localStorage.setItem(sessionStorageKey, sessionId)
  }
  return sessionId
}

function extractReply(data: unknown): string {
  if (typeof data === 'string') return data
  if (Array.isArray(data)) return data.length ? extractReply(data[0]) : ''
  if (data && typeof data === 'object') {
    const result = data as Record<string, unknown>
    for (const key of ['reply', 'response', 'message', 'output', 'text']) {
      if (typeof result[key] === 'string') return result[key] as string
    }
  }
  return ''
}

async function scrollToLatest() {
  await nextTick()
  conversation.value?.scrollTo({ top: conversation.value.scrollHeight, behavior: 'smooth' })
}

async function sendMessage() {
  const message = draft.value.trim()
  if (!message || sending.value) return

  messages.value.push({ id: nextMessageId++, role: 'user', text: message })
  draft.value = ''
  sending.value = true
  await scrollToLatest()

  try {
    const response = await fetch(webhookUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message, sessionId: getSessionId() }),
    })
    const contentType = response.headers.get('content-type') ?? ''
    const data: unknown = contentType.includes('application/json')
      ? await response.json()
      : await response.text()
    if (!response.ok) {
      const detail = extractReply(data) || (typeof data === 'string' ? data : '')
      throw new Error(detail ? `Server ${response.status}: ${detail}` : `Server ${response.status}`)
    }
    const reply = extractReply(data)
    messages.value.push({
      id: nextMessageId++,
      role: 'assistant',
      text: reply || 'Pesan diterima. Silakan tanyakan hal lain jika masih membutuhkan bantuan.',
    })
  } catch (error) {
    messages.value.push({
      id: nextMessageId++,
      role: 'assistant',
      text: error instanceof Error && error.message.startsWith('Server ')
        ? `Chatbot gagal memproses pesan. ${error.message}`
        : 'Maaf, chatbot belum dapat terhubung. Silakan coba beberapa saat lagi.',
    })
  } finally {
    sending.value = false
    await scrollToLatest()
  }
}

watch(panelOpen, (open) => {
  if (open) scrollToLatest()
})
</script>

<template>
  <div class="fixed right-4 bottom-4 z-[60] flex flex-col items-end gap-3 sm:right-6 sm:bottom-6">
    <Transition
      enter-active-class="transition duration-200 ease-out"
      enter-from-class="translate-y-3 scale-95 opacity-0"
      enter-to-class="translate-y-0 scale-100 opacity-100"
      leave-active-class="transition duration-150 ease-in"
      leave-from-class="translate-y-0 scale-100 opacity-100"
      leave-to-class="translate-y-3 scale-95 opacity-0"
    >
      <section
        v-if="panelOpen"
        class="flex h-[min(620px,calc(100dvh-112px))] w-[min(380px,calc(100vw-32px))] flex-col overflow-hidden rounded-[28px] border border-black/10 bg-white shadow-2xl shadow-slate-900/20"
        aria-label="Chatbot SiberMu"
      >
        <header class="flex items-center gap-3 bg-primary-700 px-5 py-4 text-white">
          <div class="flex size-10 items-center justify-center rounded-2xl bg-white/15">
            <img :src="sahabatMu" alt="SahabatMu" class="size-9 rounded-xl object-cover" />
          </div>
          <div class="min-w-0 flex-1">
            <h2 class="font-semibold">SahabatMu</h2>
            <p class="text-xs text-white/75">Siap membantu pertanyaan Anda</p>
          </div>
          <button type="button" class="rounded-full p-2 transition hover:bg-white/15" aria-label="Tutup chatbot" @click="panelOpen = false">
            <X class="size-5" />
          </button>
        </header>

        <div ref="conversation" class="flex-1 space-y-4 overflow-y-auto bg-slate-50/80 px-4 py-5" aria-live="polite">
          <div v-for="item in messages" :key="item.id" class="flex" :class="item.role === 'user' ? 'justify-end' : 'justify-start'">
            <p
              class="max-w-[85%] whitespace-pre-wrap rounded-2xl px-4 py-3 text-sm leading-relaxed"
              :class="item.role === 'user' ? 'rounded-br-md bg-primary-600 text-white' : 'rounded-bl-md border border-slate-200 bg-white text-slate-700 shadow-sm'"
            >{{ item.text }}</p>
          </div>
          <div v-if="sending" class="flex justify-start">
            <div class="flex items-center gap-2 rounded-2xl rounded-bl-md border border-slate-200 bg-white px-4 py-3 text-sm text-slate-500 shadow-sm">
              <LoaderCircle class="size-4 animate-spin" />
              Mengetik…
            </div>
          </div>
        </div>

        <form class="flex items-center gap-2 border-t border-slate-200 bg-white p-3" @submit.prevent="sendMessage">
          <input
            v-model="draft"
            type="text"
            autocomplete="off"
            placeholder="Tulis pesan…"
            aria-label="Tulis pesan untuk chatbot"
            class="h-11 min-w-0 flex-1 rounded-full bg-slate-100 px-4 text-sm outline-none transition placeholder:text-slate-400 focus:ring-2 focus:ring-primary-500/30"
          />
          <button
            type="submit"
            class="flex size-11 shrink-0 items-center justify-center rounded-full bg-primary-600 text-white transition hover:bg-primary-700 disabled:cursor-not-allowed disabled:opacity-50"
            aria-label="Kirim pesan"
            :disabled="sending || !draft.trim()"
          >
            <Send class="size-4" />
          </button>
        </form>
      </section>
    </Transition>

    <button
      type="button"
      class="flex h-14 items-center gap-2 rounded-full bg-primary-600 px-5 text-white shadow-xl shadow-primary-700/25 transition hover:-translate-y-0.5 hover:bg-primary-700"
      :aria-expanded="panelOpen"
      :aria-label="panelOpen ? 'Tutup chatbot' : 'Buka chatbot'"
      @click="panelOpen = !panelOpen"
    >
      <X v-if="panelOpen" class="size-5" />
      <img v-else :src="sahabatMu" alt="" class="size-9 rounded-full object-cover" />
      <span class="text-sm font-semibold">{{ panelOpen ? 'Tutup' : 'Tanya SahabatMu' }}</span>
    </button>
  </div>
</template>
