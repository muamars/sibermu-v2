<script setup lang="ts">
import { BookOpen, HandHeart, Radio, Sparkles } from '@lucide/vue'
import SectionHeading from '@/components/common/SectionHeading.vue'
import { aikActivities } from '@/data/aikActivities'

const icons = { BookOpen, Radio, Sparkles, HandHeart }
</script>

<template>
  <section id="aik" class="relative overflow-hidden bg-aik-50/60 px-4 py-16 sm:px-6 sm:py-20 lg:px-10 lg:py-28">
    <div
      class="pointer-events-none absolute inset-0 opacity-[0.06]"
      aria-hidden="true"
      style="background-image: radial-gradient(circle, currentColor 1.5px, transparent 1.5px); background-size: 28px 28px; color: #0f9d72;"
    />
    <div class="pointer-events-none absolute top-10 right-[-80px] size-72 rounded-full border border-aik-400/20" aria-hidden="true" />
    <div class="pointer-events-none absolute top-24 right-[-40px] size-56 rounded-full border border-aik-400/20" aria-hidden="true" />

    <div class="relative mx-auto max-w-[1280px]">
      <div class="grid gap-10 lg:grid-cols-2 lg:items-center">
        <SectionHeading
          eyebrow="Al-Islam & Kemuhammadiyahan"
          title="Ilmu yang tumbuh bersama nilai."
          description="Di SiberMu, pendidikan tidak berhenti pada pengetahuan. Al-Islam dan Kemuhammadiyahan menjadi bagian dari perjalanan untuk membentuk karakter, memperluas cara pandang, dan menghadirkan manfaat bagi sesama."
          tone="aik"
        />

        <div class="rounded-3xl border border-aik-100 bg-white p-8">
          <p class="text-balance text-xl leading-relaxed font-semibold text-aik-600 sm:text-2xl">
            "Berilmu untuk memahami. Beriman untuk menguatkan. Beramal untuk memberi manfaat."
          </p>
        </div>
      </div>

      <div class="mt-12 grid gap-5 sm:grid-cols-2 lg:grid-cols-4">
        <div
          v-for="activity in aikActivities"
          :key="activity.title"
          class="flex flex-col gap-4 rounded-2xl border border-aik-100 bg-white p-6 transition-transform duration-300 hover:-translate-y-1"
        >
          <div class="flex size-12 items-center justify-center rounded-full bg-aik-50 text-aik-600">
            <component :is="icons[activity.icon]" class="size-5" :stroke-width="1.75" />
          </div>
          <h3 class="text-base font-bold text-foreground">{{ activity.title }}</h3>
          <p class="text-sm leading-relaxed text-muted-foreground">{{ activity.description }}</p>
        </div>
      </div>
    </div>
  </section>
</template>
