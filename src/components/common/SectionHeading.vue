<script setup lang="ts">
import SectionBadge from './SectionBadge.vue'

withDefaults(
  defineProps<{
    eyebrow?: string
    title: string
    accent?: string
    description?: string
    align?: 'left' | 'center'
    tone?: 'primary' | 'cyan' | 'aik' | 'light' | 'dark'
    size?: 'md' | 'lg'
  }>(),
  {
    align: 'left',
    tone: 'primary',
    size: 'lg',
  },
)
</script>

<template>
  <div
    class="flex flex-col gap-4"
    :class="align === 'center' ? 'items-center text-center' : 'items-start text-left'"
  >
    <SectionBadge v-if="eyebrow" :tone="tone">{{ eyebrow }}</SectionBadge>
    <h2
      class="text-balance font-extrabold tracking-tight text-foreground"
      :class="size === 'lg'
        ? 'text-[32px] leading-[1.08] sm:text-[40px] lg:text-[48px]'
        : 'text-[26px] leading-[1.1] sm:text-[30px] lg:text-[34px]'"
    >
      <slot name="title">
        {{ accent ? title.replace(accent, '') : title }}<span v-if="accent" class="text-[#078db6]">{{ accent }}</span>
      </slot>
    </h2>
    <p
      v-if="description"
      class="max-w-xl text-base leading-relaxed text-muted-foreground sm:text-lg"
    >
      {{ description }}
    </p>
  </div>
</template>
