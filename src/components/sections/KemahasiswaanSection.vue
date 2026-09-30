<script setup lang="ts">
import { BadgeCheck, BookOpenCheck, GraduationCap, UsersRound } from '@lucide/vue'
import studentCommunity from '@/assets/bem.webp'

const highlights = [
  {
    number: '01',
    title: 'Organisasi Mahasiswa',
    description: 'Temukan ruang untuk berkolaborasi, mengambil peran, dan membangun pengalaman bersama.',
    icon: UsersRound,
    href: '#km-organisasi',
  },
  {
    number: '02',
    title: 'Unit Kegiatan Mahasiswa',
    description: 'Kembangkan minat dan bakat melalui komunitas dan aktivitas yang sesuai dengan passion.',
    icon: BookOpenCheck,
    href: '#km-ukm',
  },
  {
    number: '03',
    title: 'Prestasi Mahasiswa',
    description: 'Apresiasi berbagai pencapaian mahasiswa di bidang akademik maupun non-akademik.',
    icon: GraduationCap,
    href: '#prestasi',
  },
  {
    number: '04',
    title: 'Layanan Mahasiswa',
    description: 'Berbagai layanan yang mendukung perjalanan akademik dan kehidupan mahasiswa.',
    icon: BadgeCheck,
    href: '#layanan',
  },
]
</script>

<template>
  <section id="kemahasiswaan" class="px-4 pt-16 pb-8 sm:px-6 sm:pt-20 lg:px-10 lg:pt-24">
    <div class="mx-auto grid max-w-[1440px] items-center gap-10 lg:grid-cols-[1fr_0.95fr] lg:gap-16">
      <div>
        <p class="mb-3 flex items-center gap-2 text-[10px] font-bold tracking-[0.2em] text-primary-600 uppercase">
          <span class="h-px w-3 bg-primary-500" aria-hidden="true" />
          Kemahasiswaan
        </p>
        <h2 class="max-w-xl text-balance text-[30px] leading-[1.08] font-extrabold tracking-tight text-foreground sm:text-[38px] lg:text-[42px]">
          Ruang Untuk Tumbuh,<br /><span class="text-[#078db6]">Berkarya, dan Berprestasi.</span>
        </h2>

        <div class="mt-7 grid gap-2 sm:grid-cols-2">
          <a
            v-for="item in highlights"
            :key="item.number"
            :href="item.href"
            class="group relative overflow-hidden rounded-2xl border border-primary-100/80 bg-white/85 p-4 transition duration-300 hover:-translate-y-1 hover:border-primary-300 hover:shadow-[0_12px_30px_rgba(12,35,52,0.09)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600"
          >
            <div class="flex items-start gap-3">
              <span class="flex size-9 shrink-0 items-center justify-center rounded-xl bg-primary-50 text-primary-700 transition-colors group-hover:bg-primary-600 group-hover:text-white">
                <component :is="item.icon" class="size-4" :stroke-width="1.8" />
              </span>
              <div class="min-w-0">
                <div class="flex items-center gap-2">
                  <span class="font-mono text-[9px] font-semibold text-primary-500">{{ item.number }}</span>
                  <h3 class="text-sm leading-snug font-bold text-navy-950">{{ item.title }}</h3>
                </div>
                <p class="mt-1.5 text-xs leading-relaxed text-slate-600">{{ item.description }}</p>
              </div>
            </div>
          </a>
        </div>
      </div>

      <figure class="group relative min-h-[280px] overflow-hidden rounded-[28px_28px_28px_8px] bg-navy-950 sm:min-h-[360px] lg:min-h-[390px]">
        <img
          :src="studentCommunity"
          alt="Mahasiswa berdiskusi dan berkolaborasi dalam kegiatan bersama"
          class="absolute inset-0 size-full object-cover object-center transition-transform duration-700 group-hover:scale-[1.04]"
          loading="lazy"
        />
        <div class="absolute inset-0 bg-gradient-to-t from-navy-950/80 via-navy-950/10 to-transparent" />
        <figcaption class="absolute bottom-3 left-3 rounded-full bg-navy-950/65 px-3 py-1.5 text-[10px] font-medium text-white backdrop-blur-sm">
          Sumber: AI Generated Content
        </figcaption>
      </figure>
    </div>

    <div class="mx-auto mt-12 flex max-w-[1440px] items-center gap-4 sm:mt-16" aria-hidden="true">
      <span class="h-px flex-1 bg-border" />
      <span class="text-center text-[9px] font-bold tracking-[0.18em] text-primary-600 uppercase">Karena bertumbuh bukan hanya tentang pencapaian</span>
      <span class="h-px flex-1 bg-border" />
    </div>
  </section>
</template>
