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
  primary: 'border-primary-200 bg-primary-50 text-primary-700',
  cyan: 'border-cyan-200 bg-cyan-50 text-cyan-600',
  aik: 'border-aik-100 bg-aik-50 text-aik-600',
  light: 'border-white/30 bg-white/10 text-white',
  dark: 'border-border bg-surface text-foreground',
}
</script>

<template>
  <span
    class="inline-flex items-center gap-2 rounded-full border px-3 py-1 text-[11px] font-semibold tracking-[0.14em] uppercase"
    :class="toneClasses[tone]"
  >
    <slot />
  </span>
</template>
