<script setup lang="ts">
import { ImageIcon } from '@lucide/vue'

withDefaults(
  defineProps<{
    label?: string
    tone?: 'primary' | 'cyan' | 'aik' | 'navy' | 'neutral'
    rounded?: string
  }>(),
  {
    tone: 'neutral',
    rounded: 'rounded-3xl',
  },
)

const toneClasses: Record<string, string> = {
  primary: 'from-primary-600 via-primary-700 to-primary-900 text-white',
  cyan: 'from-cyan-300 via-cyan-400 to-primary-600 text-white',
  aik: 'from-aik-400 via-aik-500 to-aik-600 text-white',
  navy: 'from-navy-900 via-navy-950 to-black text-white',
  neutral: 'from-slate-200 via-slate-300 to-slate-400 text-slate-600',
}
</script>

<template>
  <div
    class="relative flex h-full w-full items-center justify-center overflow-hidden bg-gradient-to-br"
    :class="[toneClasses[tone], rounded]"
  >
    <div class="bg-noise-grid absolute inset-0 opacity-40" />
    <div class="relative flex flex-col items-center gap-2 px-6 text-center">
      <ImageIcon class="size-7 opacity-70" :stroke-width="1.5" />
      <span v-if="label" class="text-xs font-medium opacity-80">{{ label }}</span>
    </div>
  </div>
</template>
