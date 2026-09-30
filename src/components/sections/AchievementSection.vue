<script setup lang="ts">
import { computed } from 'vue'
import { ArrowDownRight } from '@lucide/vue'
import SectionHeading from '@/components/common/SectionHeading.vue'
import { achievements } from '@/data/achievements'

const yearGroups = computed(() => {
  const groups = new Map<string, typeof achievements>()

  achievements.forEach((achievement) => {
    const year = achievement.year ?? 'Tahun lainnya'
    groups.set(year, [...(groups.get(year) ?? []), achievement])
  })

  return [...groups.entries()].sort(([yearA], [yearB]) => {
    if (yearA === 'Tahun lainnya') return 1
    if (yearB === 'Tahun lainnya') return -1
    return Number(yearB) - Number(yearA)
  })
})
</script>

<template>
  <section id="prestasi" class="relative overflow-hidden bg-[#F4F8FB] px-4 py-16 sm:px-6 sm:py-20 lg:px-10 lg:py-28">
    <div class="pointer-events-none absolute -top-40 right-[-8rem] size-[28rem] rounded-full bg-cyan-300/15 blur-3xl" aria-hidden="true" />
    <div class="relative mx-auto max-w-[1200px]">
      <div class="flex flex-col gap-7 border-b border-navy-950/10 pb-10 md:flex-row md:items-end md:justify-between">
        <SectionHeading
          eyebrow="Hall of Fame · SiberMu"
          title="Jejak juara, dari tahun ke tahun."
          accent="dari tahun ke tahun."
          description="Setiap pencapaian menjadi bagian dari perjalanan mahasiswa SiberMu. Telusuri kisah dan prestasi mereka berdasarkan tahun."
        />
        <a href="#cerita" class="inline-flex shrink-0 items-center gap-2 pb-1 text-sm font-semibold text-primary-700 transition-transform hover:translate-x-1">
          Cerita mahasiswa <ArrowDownRight class="size-4" />
        </a>
      </div>

      <div class="mt-10 space-y-12 sm:mt-14 sm:space-y-16">
        <section v-for="[year, items] in yearGroups" :key="year" class="grid gap-5 md:grid-cols-[150px_minmax(0,1fr)] md:gap-10">
          <div class="relative flex items-start gap-4 md:justify-end">
            <div class="md:sticky md:top-24 md:flex md:flex-col md:items-end">
              <span class="font-mono text-3xl font-bold tracking-tight text-navy-950 sm:text-4xl">{{ year }}</span>
              <span class="mt-1 text-xs font-semibold tracking-[0.16em] text-primary-700 uppercase">{{ items.length }} prestasi</span>
            </div>
            <div class="absolute top-1 -right-[21px] hidden h-full w-px bg-gradient-to-b from-cyan-400 via-primary-200 to-transparent md:block" aria-hidden="true" />
          </div>

          <div class="relative space-y-4 md:before:absolute md:before:-left-10 md:before:top-7 md:before:size-3 md:before:rounded-full md:before:border-4 md:before:border-[#F4F8FB] md:before:bg-cyan-500 md:before:shadow-[0_0_0_1px_rgba(17,186,238,0.35)]">
            <article
              v-for="(item, index) in items"
              :key="item.title"
              class="group relative isolate min-h-[220px] overflow-hidden rounded-[26px] border border-navy-950/[0.07] bg-white p-6 shadow-[0_8px_30px_rgba(12,35,52,0.04)] transition duration-300 hover:-translate-y-1 hover:shadow-[0_18px_45px_rgba(12,35,52,0.11)] sm:p-8"
            >
              <div v-if="item.photo" class="pointer-events-none absolute inset-y-0 right-0 z-0 w-[45%] sm:w-[38%]">
                <img :src="item.photo" :alt="`Foto ${item.title}`" class="h-full w-full object-contain object-right-bottom transition-transform duration-500 group-hover:scale-[1.04]" />
                <div class="absolute inset-0 bg-gradient-to-r from-white via-white/70 to-transparent" aria-hidden="true" />
              </div>

              <div class="relative z-10 flex h-full max-w-[720px] flex-col">
                <div class="flex flex-wrap items-center gap-2">
                  <span class="inline-flex items-center gap-1.5 rounded-full bg-cyan-50 px-3 py-1 text-[10px] font-bold tracking-[0.12em] text-primary-800 uppercase">
                    <!-- <Medal v-if="item.title.toLowerCase().includes('medal') || item.title.toLowerCase().includes('emas')" class="size-3.5" />
                    <Trophy v-else class="size-3.5" /> -->
                    {{ item.category }}
                  </span>
                </div>

                <h3 class="mt-5 max-w-[560px] text-xl leading-tight font-bold tracking-tight text-navy-950 sm:text-2xl">{{ item.title }}</h3>
                <p class="mt-2 max-w-[560px] text-sm leading-relaxed text-slate-600">{{ item.description }}</p>

                <div v-if="item.recipients?.length" class="mt-auto flex flex-wrap gap-x-5 gap-y-1 pt-5 text-sm font-semibold text-primary-800">
                  <span v-for="recipient in item.recipients" :key="recipient" class="flex items-center gap-2">
                    <span class="size-1.5 rounded-full bg-cyan-500" aria-hidden="true" />{{ recipient }}
                  </span>
                </div>
              </div>
              <span class="pointer-events-none absolute right-5 top-5 font-mono text-xs text-navy-950/20">{{ String(index + 1).padStart(2, '0') }}</span>
            </article>
          </div>
        </section>
      </div>
    </div>
  </section>
</template>
