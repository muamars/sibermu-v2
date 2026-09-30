<script setup lang="ts">
withDefaults(
  defineProps<{
    tone?: 'primary' | 'cyan' | 'aik' | 'light' | 'dark'
  }>(),
  {
    tone: 'primary',
  },
)

const toneClasses: Record<string, string> = {
  primary: 'text-primary-600',
  cyan: 'border-cyan-200 bg-cyan-50 text-[#078db6]',
  aik: 'border-aik-100 bg-aik-50 text-aik-600',
  light: 'border-white/30 bg-white/10 text-white',
  dark: 'border-border bg-surface text-foreground',
}
</script>

<template>
  <span
    :class="[
      toneClasses[tone],
      tone === 'primary'
        ? 'flex items-center gap-2 text-[10px] font-bold tracking-[0.2em] uppercase'
        : 'inline-flex items-center gap-2 rounded-full border px-3 py-1 text-[11px] font-semibold tracking-[0.14em] uppercase',
    ]"
  >
    <span v-if="tone === 'primary'" class="h-px w-3 bg-primary-500" aria-hidden="true" />
    <slot />
  </span>
</template>
