<script setup lang="ts">
import { ArrowUpRight } from '@lucide/vue'
import ImagePlaceholder from '@/components/common/ImagePlaceholder.vue'
import SectionBadge from '@/components/common/SectionBadge.vue'
import { studentPath } from '@/data/studentPath'
</script>

<template>
  <section class="px-4 py-16 sm:px-6 sm:py-20 lg:px-10 lg:py-28">
    <div class="relative mx-auto max-w-[1280px] overflow-hidden rounded-[28px]">
      <div class="absolute inset-0">
        <ImagePlaceholder tone="neutral" label="Foto suasana kampus digital SiberMu" rounded="rounded-none" />
        <div class="absolute inset-0 bg-navy-950/50" />
      </div>

      <div class="relative flex flex-col gap-8 p-4 sm:p-8 lg:p-10">
        <div class="rounded-[24px] bg-white p-6 shadow-xl sm:p-8">
          <div class="flex flex-col gap-3 sm:max-w-md">
            <SectionBadge tone="primary">Jalanmu di SiberMu</SectionBadge>
            <h2 class="text-balance text-[28px] leading-[1.1] font-extrabold text-foreground sm:text-[34px]">
              Banyak cara untuk bertumbuh.
            </h2>
            <p class="text-sm leading-relaxed text-muted-foreground sm:text-base">
              Setiap mahasiswa punya perjalanan yang berbeda. Pilih ruang yang paling
              sesuai dengan minat dan tujuanmu.
            </p>
          </div>

          <div class="mt-6 divide-y divide-border border-t border-border">
            <div
              v-for="item in studentPath"
              :key="item.title"
              class="grid grid-cols-1 items-center gap-4 py-5 sm:grid-cols-[1.4fr_1fr_96px]"
            >
              <h3 class="text-lg font-bold text-foreground">{{ item.title }}</h3>
              <p class="text-sm leading-relaxed text-muted-foreground">{{ item.description }}</p>
              <div class="hidden h-16 w-24 overflow-hidden rounded-xl sm:block">
                <ImagePlaceholder tone="primary" rounded="rounded-xl" />
              </div>
            </div>
          </div>
        </div>

        <div class="flex flex-col items-start justify-between gap-4 rounded-[24px] bg-primary-600 p-6 text-white sm:flex-row sm:items-center sm:p-8">
          <h3 class="text-balance text-2xl font-extrabold sm:max-w-sm">
            Siap menemukan jalanmu sendiri di SiberMu?
          </h3>
          <a
            href="#layanan"
            class="inline-flex h-11 items-center gap-2 rounded-full bg-white px-6 text-sm font-semibold text-navy-950 transition-colors hover:bg-white/90"
          >
            Lihat Layanan Mahasiswa
            <ArrowUpRight class="size-4" />
          </a>
        </div>
      </div>
    </div>
  </section>
</template>
