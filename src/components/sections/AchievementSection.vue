<script setup lang="ts">
import { ArrowRight, Award } from '@lucide/vue'
import ImagePlaceholder from '@/components/common/ImagePlaceholder.vue'
import SectionHeading from '@/components/common/SectionHeading.vue'
import { achievements } from '@/data/achievements'

const featured = achievements.find((item) => item.featured)!
const rest = achievements.filter((item) => !item.featured)
const secondary = rest[0]
const others = rest.slice(1)
</script>

<template>
  <section id="prestasi" class="px-4 py-16 sm:px-6 sm:py-20 lg:px-10 lg:py-28">
    <div class="mx-auto max-w-[1280px]">
      <div class="flex flex-col gap-6 lg:flex-row lg:items-end lg:justify-between">
        <SectionHeading
          eyebrow="Prestasi Mahasiswa"
          title="Dari ruang digital, lahir karya yang nyata."
          description="Prestasi bukan hanya tentang menjadi juara. Ia dimulai dari keberanian mencoba, konsistensi belajar, dan kemauan untuk terus berkembang."
        />
        <a
          href="#cerita"
          class="inline-flex items-center gap-1.5 text-sm font-semibold text-primary-700 transition-transform hover:translate-x-1"
        >
          Lihat Cerita Prestasi
          <ArrowRight class="size-4" />
        </a>
      </div>

      <div class="mt-10 grid gap-5 lg:grid-cols-12">
        <div class="relative flex flex-col justify-between overflow-hidden rounded-3xl bg-navy-950 p-7 text-white lg:col-span-7">
          <div class="absolute inset-0 opacity-30">
            <ImagePlaceholder tone="primary" rounded="rounded-none" />
          </div>
          <div class="relative z-10 flex items-center justify-between">
            <span class="inline-flex items-center gap-2 rounded-full bg-white/10 px-3 py-1 text-[11px] font-semibold tracking-wide text-white uppercase">
              {{ featured.category }}
            </span>
            <Award class="size-6 text-cyan-300" />
          </div>
          <div class="relative z-10 mt-24 flex flex-col gap-2">
            <h3 class="text-2xl font-bold sm:text-3xl">{{ featured.title }}</h3>
            <p class="max-w-md text-sm leading-relaxed text-white/75">{{ featured.description }}</p>
          </div>
        </div>

        <div class="flex flex-col justify-between rounded-3xl border border-border bg-white p-7 lg:col-span-5">
          <span class="inline-flex w-fit items-center gap-2 rounded-full bg-primary-50 px-3 py-1 text-[11px] font-semibold tracking-wide text-primary-700 uppercase">
            {{ secondary.category }}
          </span>
          <div class="mt-6 flex flex-col gap-2">
            <h3 class="text-xl font-bold text-foreground">{{ secondary.title }}</h3>
            <p class="text-sm leading-relaxed text-muted-foreground">{{ secondary.description }}</p>
          </div>
        </div>
      </div>

      <div class="mt-5 grid gap-5 sm:grid-cols-2 lg:grid-cols-4">
        <div
          v-for="item in others"
          :key="item.title"
          class="flex flex-col gap-2 rounded-2xl border border-border bg-white p-6 transition-transform duration-300 hover:-translate-y-1"
        >
          <span class="text-[11px] font-semibold tracking-wide text-muted-foreground uppercase">{{ item.category }}</span>
          <h3 class="text-base font-bold text-foreground">{{ item.title }}</h3>
          <p class="text-sm leading-relaxed text-muted-foreground">{{ item.description }}</p>
        </div>
      </div>
    </div>
  </section>
</template>
