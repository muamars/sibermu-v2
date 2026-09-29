<script setup lang="ts">
import { ArrowUpRight } from '@lucide/vue'
import { computed, ref } from 'vue'
import SectionHeading from '@/components/common/SectionHeading.vue'

import administrasiKesehatanLogo from '@/assets/prodi/S1 PJJ Administrasi Kesehatan.png'
import akuntansiLogo from '@/assets/prodi/S1 PJJ Akuntansi.png'
import hukumLogo from '@/assets/prodi/S1 PJJ Hukum.png'
import informatikaLogo from '@/assets/prodi/S1 PJJ Informatika.png'
import manajemenLogo from '@/assets/prodi/S1 PJJ Manajemen.png'
import sistemInformasiLogo from '@/assets/prodi/S1 PJJ Sistem Informasi.png'

type Faculty = 'all' | 'teknologi' | 'bisnis'

const filters: { label: string; value: Faculty }[] = [
  { label: 'Semua prodi', value: 'all' },
  { label: 'Teknologi & Kesehatan', value: 'teknologi' },
  { label: 'Bisnis & Humaniora', value: 'bisnis' },
]

const programs = [
  {
    name: 'Informatika',
    faculty: 'teknologi',
    facultyLabel: 'Teknologi & Ilmu Kesehatan',
    description: 'Bangun solusi digital melalui pemrograman, data, dan teknologi komputasi.',
    logo: informatikaLogo,
    href: 'https://sibermu.ac.id/sarjana-informatika/',
  },
  {
    name: 'Sistem Informasi',
    faculty: 'teknologi',
    facultyLabel: 'Teknologi & Ilmu Kesehatan',
    description: 'Hubungkan kebutuhan organisasi dengan sistem dan teknologi yang tepat.',
    logo: sistemInformasiLogo,
    href: 'https://sibermu.ac.id/sarjana-sistem-informasi/',
  },
  {
    name: 'Administrasi Kesehatan',
    faculty: 'teknologi',
    facultyLabel: 'Teknologi & Ilmu Kesehatan',
    description: 'Pelajari pengelolaan layanan kesehatan yang efektif dan adaptif.',
    logo: administrasiKesehatanLogo,
    href: 'https://sibermu.ac.id/sarjana-administrasi-kesehatan/',
  },
  {
    name: 'Hukum',
    faculty: 'bisnis',
    facultyLabel: 'Bisnis & Humaniora',
    description: 'Asah cara berpikir kritis untuk memahami hukum dan masyarakat digital.',
    logo: hukumLogo,
    href: 'https://sibermu.ac.id/sarjana-hukum/',
  },
  {
    name: 'Manajemen',
    faculty: 'bisnis',
    facultyLabel: 'Bisnis & Humaniora',
    description: 'Kembangkan kemampuan mengelola bisnis, tim, dan peluang baru.',
    logo: manajemenLogo,
    href: 'https://sibermu.ac.id/sarjana-manajemen/',
  },
  {
    name: 'Akuntansi',
    faculty: 'bisnis',
    facultyLabel: 'Bisnis & Humaniora',
    description: 'Dalami keuangan dan pelaporan untuk keputusan yang lebih cermat.',
    logo: akuntansiLogo,
    href: 'https://sibermu.ac.id/sarjana-akuntansi/',
  },
] as const

const activeFaculty = ref<Faculty>('all')
const visiblePrograms = computed(() =>
  activeFaculty.value === 'all'
    ? programs
    : programs.filter((program) => program.faculty === activeFaculty.value),
)
</script>

<template>
  <section id="prodi" class="px-4 py-16 sm:px-6 sm:py-20 lg:px-10 lg:py-28">
    <div class="mx-auto max-w-[1440px]">
      <div class="flex flex-col justify-between gap-8 lg:flex-row lg:items-end">
        <SectionHeading
          eyebrow="Program Studi"
          title="Temukan bidang yang ingin kamu dalami."
          description="Enam program sarjana jarak jauh memberi ruang untuk belajar sesuai minat dan arah masa depanmu."
        />
        <div class="flex shrink-0 items-end gap-3 border-l-2 border-primary-200 pl-5 lg:mb-1">
          <span class="text-6xl leading-none font-extrabold tracking-tight text-primary-600">06</span>
          <span class="pb-1 text-sm leading-tight font-medium text-muted-foreground">program studi<br />sarjana PJJ</span>
        </div>
      </div>

      <div class="mt-10 rounded-[28px] bg-[#f3f7fa] p-3 sm:p-5 lg:p-7">
        <div class="flex flex-wrap gap-2 px-1 pb-5 sm:pb-6" role="group" aria-label="Filter program studi">
          <button
            v-for="filter in filters"
            :key="filter.value"
            type="button"
            class="rounded-full border px-4 py-2 text-xs font-semibold transition-colors sm:text-sm"
            :class="activeFaculty === filter.value
              ? 'border-primary-600 bg-primary-600 text-white shadow-sm'
              : 'border-primary-200 bg-white text-primary-700 hover:border-primary-500 hover:bg-primary-50'"
            :aria-pressed="activeFaculty === filter.value"
            @click="activeFaculty = filter.value"
          >
            {{ filter.label }}
          </button>
        </div>

        <TransitionGroup name="program" tag="div" class="grid gap-3 sm:grid-cols-2 lg:grid-cols-3 sm:gap-4">
          <article
            v-for="(program, index) in visiblePrograms"
            :key="program.name"
            class="group relative flex min-h-[340px] flex-col overflow-hidden rounded-[22px] border border-primary-100 bg-white p-6 transition-[border-color,box-shadow,transform] duration-300 hover:border-primary-300 hover:shadow-xl hover:shadow-primary-900/10 motion-safe:hover:-translate-y-1 sm:p-7"
          >
            <div
              class="absolute inset-x-0 top-0 h-1 origin-left scale-x-0 bg-primary-600 transition-transform duration-300 group-hover:scale-x-100"
              aria-hidden="true"
            />
            <div class="flex items-start justify-between gap-4">
              <span class="text-[10px] font-bold tracking-[0.16em] text-primary-500 uppercase">S1 · PJJ</span>
              <span class="text-[11px] font-semibold text-primary-400">{{ String(index + 1).padStart(2, '0') }}</span>
            </div>

            <div class="mt-5 flex h-24 items-center">
              <img :src="program.logo" :alt="`Logo Prodi ${program.name}`" class="h-full w-[260px] max-w-full object-contain object-left" loading="lazy" />
            </div>

            <div class="mt-auto pt-6">
              <p class="text-[10px] font-bold tracking-[0.13em] text-primary-500 uppercase">{{ program.facultyLabel }}</p>
              <h3 class="mt-2 text-xl leading-tight font-extrabold text-primary-700 sm:text-[22px]">{{ program.name }}</h3>
              <p class="mt-3 max-w-sm text-sm leading-relaxed text-muted-foreground">{{ program.description }}</p>
              <a
                :href="program.href"
                target="_blank"
                rel="noopener noreferrer"
                class="mt-6 inline-flex items-center gap-1.5 text-sm font-bold text-primary-600 transition-colors hover:text-primary-800"
                :aria-label="`Lihat Program Studi ${program.name}`"
              >
                Lihat program
                <ArrowUpRight class="size-4 transition-transform duration-300 group-hover:translate-x-0.5 group-hover:-translate-y-0.5" />
              </a>
            </div>
          </article>
        </TransitionGroup>
      </div>
    </div>
  </section>
</template>

<style scoped>
.program-enter-active,
.program-leave-active {
  transition: opacity 220ms ease, transform 220ms ease;
}

.program-enter-from,
.program-leave-to {
  opacity: 0;
  transform: translateY(12px);
}

@media (prefers-reduced-motion: reduce) {
  .program-enter-active,
  .program-leave-active {
    transition: none;
  }
}
</style>
