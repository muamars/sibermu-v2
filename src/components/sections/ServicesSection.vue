<script setup lang="ts">
import { ArrowUpRight, Briefcase, ClipboardList, GraduationCap, LifeBuoy, MessageCircle, Wallet } from '@lucide/vue'
import { computed } from 'vue'
import { services } from '@/data/services'

const icons = { GraduationCap, Wallet, MessageCircle, ClipboardList, Briefcase, LifeBuoy }
const scholarship = computed(() => services.find((service) => service.title === 'Beasiswa')!)
const leftServices = computed(() => [
  services.find((service) => service.title === 'Layanan Akademik')!,
  services.find((service) => service.title === 'Administrasi')!,
])
const rightServices = computed(() => [
  services.find((service) => service.title === 'Pengembangan Karier')!,
  services.find((service) => service.title === 'Bantuan Teknis')!,
])
const additionalServices = computed(() => services.filter((service) => service.title === 'Konseling Mahasiswa'))
</script>

<template>
  <section id="layanan" class="px-4 py-16 sm:px-6 sm:py-20 lg:px-10 lg:py-24">
    <div class="mx-auto max-w-[1440px]">
      <div class="mb-10 flex flex-col gap-6 sm:mb-12 md:flex-row md:items-end md:justify-between">
        <div>
          <p class="mb-3 flex items-center gap-2 text-[10px] font-bold tracking-[0.2em] text-primary-600 uppercase">
            <span class="h-px w-3 bg-primary-500" aria-hidden="true" />
            Layanan Mahasiswa
          </p>
          <h2 class="text-balance text-[32px] leading-[1.08] font-extrabold tracking-tight text-foreground sm:text-[40px] lg:text-[48px]">
            Ada yang mendukungmu di <span class="text-[#078db6]">setiap perjalanan.</span>
          </h2>
        </div>
        <p class="max-w-sm text-sm leading-relaxed text-muted-foreground md:pb-1 md:text-right">
          Dari kebutuhan akademik hingga pengembangan diri, SiberMu menghadirkan layanan untuk membantu mahasiswa menjalani perkuliahan dengan lebih nyaman.
        </p>
      </div>

      <div class="grid gap-3 lg:grid-cols-[1fr_1fr_1fr]">
        <div class="grid gap-3 sm:grid-cols-2 lg:grid-cols-1">
          <article
            v-for="service in leftServices"
            :key="service.title"
            class="group flex min-h-[180px] flex-col justify-between rounded-[22px] bg-[#FCFDFE] p-5 border border-grey-200 transition duration-300 hover:-translate-y-1 hover:shadow-[0_14px_32px_rgba(12,35,52,0.1)] sm:p-6"
          >
            <div class="flex items-center justify-between">
              <span class="flex size-9 items-center justify-center rounded-full bg-slate-100 text-navy-900">
                <component :is="icons[service.icon]" class="size-4" :stroke-width="1.8" />
              </span>
              <span class="flex size-8 items-center justify-center rounded-full border border-slate-200 text-navy-800 transition duration-300 group-hover:-translate-y-0.5 group-hover:translate-x-0.5 group-hover:border-primary-300 group-hover:text-primary-700">
                <ArrowUpRight class="size-4" />
              </span>
            </div>
            <div class="mt-8">
              <h3 class="text-base font-bold tracking-tight text-navy-950">{{ service.title }}</h3>
              <p class="mt-1.5 text-xs leading-relaxed text-slate-600">{{ service.description }}</p>
            </div>
          </article>
        </div>

        <article class="group relative flex min-h-[260px] flex-col justify-between overflow-hidden rounded-[22px] bg-[#0c2b43] p-6 text-white sm:p-7 lg:min-h-[370px]">
          <div class="pointer-events-none absolute -right-16 bottom-[-7rem] size-72 rounded-full border-[1px] border-white/[0.05] bg-white/[0.025]" aria-hidden="true" />
          <div class="pointer-events-none absolute -right-24 bottom-[-11rem] size-96 rounded-full border-[1px] border-white/[0.05]" aria-hidden="true" />
          <div class="relative flex items-start justify-between">
            <span class="flex size-9 items-center justify-center rounded-full bg-white/10 text-white">
              <Wallet class="size-4" :stroke-width="1.8" />
            </span>
            <ArrowUpRight class="size-5 text-white/75 transition-transform duration-300 group-hover:-translate-y-1 group-hover:translate-x-1" />
          </div>
          <div class="relative mt-12">
            <h3 class="text-lg font-bold tracking-tight">{{ scholarship.title }}</h3>
            <p class="mt-1.5 max-w-sm text-xs leading-relaxed text-white/75">{{ scholarship.description }}</p>
            <a
              href="https://sibermu.ac.id"
              target="_blank"
              rel="noopener noreferrer"
              class="mt-4 inline-flex h-9 items-center justify-center rounded-full border border-white/70 px-5 text-[11px] font-medium text-white transition-colors hover:bg-white hover:text-navy-950"
            >
              Lihat Beasiswa
            </a>
          </div>
        </article>

        <div class="grid gap-3 sm:grid-cols-2 lg:grid-cols-1">
          <article
            v-for="service in rightServices"
            :key="service.title"
            class="group flex min-h-[180px] flex-col justify-between rounded-[22px] bg-[#FCFDFE] p-5 border border-grey-200 transition duration-300 hover:-translate-y-1 hover:shadow-[0_14px_32px_rgba(12,35,52,0.1)] sm:p-6"
          >
            <div class="flex items-center justify-between">
              <span class="flex size-9 items-center justify-center rounded-full bg-slate-100 text-navy-900">
                <component :is="icons[service.icon]" class="size-4" :stroke-width="1.8" />
              </span>
              <span class="flex size-8 items-center justify-center rounded-full border border-slate-200 text-navy-800 transition duration-300 group-hover:-translate-y-0.5 group-hover:translate-x-0.5 group-hover:border-primary-300 group-hover:text-primary-700">
                <ArrowUpRight class="size-4" />
              </span>
            </div>
            <div class="mt-8">
              <h3 class="text-base font-bold tracking-tight text-navy-950">{{ service.title }}</h3>
              <p class="mt-1.5 text-xs leading-relaxed text-slate-600">{{ service.description }}</p>
            </div>
          </article>
        </div>
      </div>

      <article
        v-for="service in additionalServices"
        :key="service.title"
        class="group mt-3 flex flex-col gap-5 rounded-[22px] bg-[#FCFDFE] p-5 border border-grey-200 transition duration-300 hover:shadow-[0_14px_32px_rgba(12,35,52,0.1)] sm:flex-row sm:items-center sm:p-6"
      >
        <span class="flex size-9 shrink-0 items-center justify-center rounded-full bg-slate-100 text-navy-900">
          <MessageCircle class="size-4" :stroke-width="1.8" />
        </span>
        <div class="flex-1">
          <h3 class="text-base font-bold tracking-tight text-navy-950">{{ service.title }}</h3>
          <p class="mt-1.5 text-xs leading-relaxed text-slate-600">{{ service.description }}</p>
        </div>
        <ArrowUpRight class="size-5 text-navy-700 transition-transform duration-300 group-hover:-translate-y-1 group-hover:translate-x-1" />
      </article>
    </div>
  </section>
</template>
