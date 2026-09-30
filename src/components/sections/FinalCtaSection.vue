<script setup lang="ts">
import { ArrowRight } from '@lucide/vue'
import studentImage from '@/assets/mulai.webp'
import sibermuLogo from '@/assets/sibermu-white.png'
</script>

<template>
  <section class="px-4 py-16 sm:px-6 sm:py-20 lg:px-10 lg:pt-32">
    <div
      class="relative mx-auto max-w-[1440px] rounded-[28px] bg-primary-600 px-4 pt-4 pb-0 sm:px-8 sm:pt-8 lg:min-h-[320px] lg:py-12"
    >
      <div class="pointer-events-none absolute -top-24 right-10 size-64 rounded-full bg-cyan-400/25 blur-3xl" aria-hidden="true" />
      <img
        :src="sibermuLogo"
        alt=""
        aria-hidden="true"
        class="pointer-events-none absolute top-1/2 right-[18%] z-0 w-[min(48vw,560px)] -translate-y-1/2 opacity-[0.08]"
      />

      <div class="relative grid gap-8 lg:grid-cols-[1fr_0.65fr] lg:items-center">
        <div class="relative z-10 flex flex-col gap-5 lg:max-w-xl">
          <h2 class="text-balance text-[34px] leading-[1.05] font-extrabold text-white sm:text-[44px]">
            Perjalananmu dimulai <span class="text-[#078db6]">dari sini.</span>
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
              Daftar Sekarang
              <ArrowRight class="size-4" />
            </a>
            <!-- <a
              href="https://sibermu.ac.id"
              target="_blank"
              rel="noopener"
              class="inline-flex h-12 items-center justify-center gap-2 rounded-full border border-white/30 bg-white/5 px-6 text-sm font-semibold text-white transition-colors hover:bg-white/15"
            >
              Kunjungi Website Resmi
            </a> -->
          </div>
        </div>
      </div>

      <div
        class="pointer-events-none relative z-10 mt-6 flex h-56 items-end justify-center sm:h-64 lg:absolute lg:right-10 lg:bottom-0 lg:mt-0 lg:h-[135%] lg:justify-end"
      >
        <img
          :src="studentImage"
          alt="Mahasiswa SiberMu siap memulai perjalanan kuliah"
          class="block h-full w-auto max-w-full object-contain object-bottom lg:max-w-none"
          loading="lazy"
        />
      </div>
    </div>
  </section>
</template>
