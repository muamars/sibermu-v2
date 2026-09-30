<script setup lang="ts">
import { BookOpen, HandHeart, Radio, Sparkles } from '@lucide/vue'
import aikImage from '@/assets/kajian.webp'
import { aikActivities } from '@/data/aikActivities'

const icons = { BookOpen, Radio, Sparkles, HandHeart }
</script>

<template>
  <section id="aik" class="relative overflow-hidden px-4 pt-8 pb-16 sm:px-6 sm:pt-10 sm:pb-20 lg:px-10 lg:pb-24">
    <div class="pointer-events-none absolute top-16 right-[-9rem] size-[28rem] rounded-full bg-primary-100/70 blur-3xl" aria-hidden="true" />
    <div class="relative mx-auto grid max-w-[1440px] items-center gap-10 lg:grid-cols-[0.95fr_1fr] lg:gap-16">
      <figure class="group relative min-h-[280px] overflow-hidden rounded-[8px_28px_28px_28px] bg-navy-950 sm:min-h-[360px] lg:min-h-[390px]">
        <img
          :src="aikImage"
          alt="Mahasiswa mengikuti kegiatan belajar Al-Qur'an"
          class="absolute inset-0 size-full object-cover object-center transition-transform duration-700 group-hover:scale-[1.04]"
          loading="lazy"
        />
      </figure>

      <div>
        <p class="mb-3 flex items-center gap-2 text-[10px] font-bold tracking-[0.2em] text-primary-600 uppercase">
          <span class="h-px w-3 bg-primary-500" aria-hidden="true" />
          Al-Islam & Kemuhammadiyahan
        </p>
        <h2 class="max-w-xl text-balance text-[30px] leading-[1.08] font-extrabold tracking-tight text-navy-950 sm:text-[38px] lg:text-[42px]">
          Menjadikan Nilai Sebagai<br /><span class="text-[#078db6]">Bagian dari Perjalanan.</span>
        </h2>
        <p class="mt-3 max-w-xl text-sm leading-relaxed text-slate-600">
          Tumbuh dalam ilmu, iman, dan kepedulian melalui pengalaman belajar yang dekat dengan keseharian.
        </p>

        <div class="mt-6 grid gap-2 sm:grid-cols-2">
          <article
            v-for="(activity, index) in aikActivities"
            :key="activity.title"
            class="group relative overflow-hidden rounded-2xl border border-primary-100/80 bg-white/85 p-4 transition duration-300 hover:-translate-y-1 hover:border-primary-300 hover:shadow-[0_12px_30px_rgba(12,35,52,0.09)]"
          >
            <div class="flex items-start gap-3">
              <span class="flex size-9 shrink-0 items-center justify-center rounded-xl bg-primary-50 text-primary-700 transition-colors group-hover:bg-primary-600 group-hover:text-white">
                <component :is="icons[activity.icon]" class="size-4" :stroke-width="1.8" />
              </span>
              <div class="min-w-0">
                <div class="flex items-center gap-2">
                  <span class="font-mono text-[9px] font-semibold text-primary-500">0{{ index + 1 }}</span>
                  <h3 class="text-sm font-bold leading-snug text-navy-950">{{ activity.title }}</h3>
                </div>
                <p class="mt-1.5 text-xs leading-relaxed text-slate-600">{{ activity.description }}</p>
              </div>
            </div>
          </article>
        </div>
      </div>
    </div>
  </section>
</template>
