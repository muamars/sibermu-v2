<script setup lang="ts">
import { ArrowRight } from '@lucide/vue'
import ImagePlaceholder from '@/components/common/ImagePlaceholder.vue'
import SectionHeading from '@/components/common/SectionHeading.vue'
import { studentActivities } from '@/data/studentActivities'

const toneCardClasses: Record<string, string> = {
  primary: 'bg-primary-600 text-white',
  light: 'bg-white text-foreground border border-border',
  dark: 'bg-navy-950 text-white',
}
</script>

<template>
  <section id="kemahasiswaan" class="px-4 py-16 sm:px-6 sm:py-20 lg:px-10 lg:py-28">
    <div class="mx-auto max-w-[1280px]">
      <div class="flex flex-col gap-10 lg:flex-row lg:items-end lg:justify-between">
        <SectionHeading
          eyebrow="Kemahasiswaan"
          title="Lebih dari sekadar kuliah."
          description="Masa kuliah bukan hanya tentang menyelesaikan mata kuliah. Ini adalah waktu untuk mencoba hal baru, menemukan lingkungan yang tepat, dan membangun pengalaman yang dibawa jauh setelah lulus."
        />
        <p class="max-w-xs text-lg font-semibold text-foreground/70 lg:text-right">
          Temukan ruangmu. Tumbuh dengan caramu.
        </p>
      </div>

      <div class="mt-10 grid gap-5 lg:grid-cols-3">
        <div
          v-for="activity in studentActivities"
          :key="activity.title"
          class="group relative flex min-h-[380px] flex-col justify-between overflow-hidden rounded-3xl p-6 transition-transform duration-300 hover:-translate-y-1"
          :class="toneCardClasses[activity.tone]"
        >
          <div class="relative z-10 flex flex-col gap-2">
            <h3 class="text-xl font-bold">{{ activity.title }}</h3>
            <p class="text-sm leading-relaxed opacity-80">{{ activity.description }}</p>
          </div>

          <div class="relative z-10 mt-6 h-40 overflow-hidden rounded-2xl">
            <ImagePlaceholder
              :tone="activity.tone === 'primary' ? 'cyan' : activity.tone === 'dark' ? 'navy' : 'neutral'"
              :label="activity.imageHint"
              rounded="rounded-2xl"
            />
          </div>

          <a href="#prestasi" class="relative z-10 mt-6 inline-flex items-center gap-1.5 text-sm font-semibold transition-transform group-hover:translate-x-1">
            {{ activity.cta }}
            <ArrowRight class="size-4" />
          </a>
        </div>
      </div>
    </div>
  </section>
</template>
