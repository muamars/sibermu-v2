<script setup lang="ts">
import { ArrowRight } from '@lucide/vue'
import ImagePlaceholder from '@/components/common/ImagePlaceholder.vue'
</script>

<template>
  <section class="px-4 py-16 sm:px-6 sm:py-20 lg:px-10">
    <div class="relative mx-auto max-w-[1440px] overflow-hidden rounded-[28px] bg-primary-600 px-6 py-12 sm:px-10 sm:py-16">
      <div class="pointer-events-none absolute -top-24 right-10 size-64 rounded-full bg-cyan-400/25 blur-3xl" aria-hidden="true" />

      <div class="relative flex flex-col gap-8 lg:flex-row lg:items-center lg:justify-between">
        <div class="flex flex-col gap-5 lg:max-w-md">
          <h2 class="text-balance text-[34px] leading-[1.05] font-extrabold text-white sm:text-[44px]">
            Perjalananmu dimulai dari sini.
          </h2>
          <p class="text-base leading-relaxed text-white/80 sm:text-lg">
            Belajar. Bertumbuh. Berkarya. Bersama SiberMu.
          </p>
          <div class="flex flex-col gap-3 sm:flex-row">
            <a
              href="https://sibermu.ac.id"
              target="_blank"
              rel="noopener"
              class="inline-flex h-12 items-center justify-center gap-2 rounded-full bg-white px-6 text-sm font-semibold text-navy-950 transition-colors hover:bg-white/90"
            >
              Kenali SiberMu
              <ArrowRight class="size-4" />
            </a>
            <a
              href="https://sibermu.ac.id"
              target="_blank"
              rel="noopener"
              class="inline-flex h-12 items-center justify-center gap-2 rounded-full border border-white/30 bg-white/5 px-6 text-sm font-semibold text-white transition-colors hover:bg-white/15"
            >
              Kunjungi Website Resmi
            </a>
          </div>
        </div>

        <div class="hidden gap-4 sm:flex">
          <div class="h-56 w-36 overflow-hidden rounded-2xl">
            <ImagePlaceholder tone="cyan" rounded="rounded-2xl" />
          </div>
          <div class="mt-8 h-56 w-36 overflow-hidden rounded-2xl">
            <ImagePlaceholder tone="navy" rounded="rounded-2xl" />
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
