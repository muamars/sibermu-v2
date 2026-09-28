<script setup lang="ts">
import darimanaBackground from '@/assets/Darimana.webp'

const highlights = ['Belajar Digital', 'Komunitas Mahasiswa', 'Prestasi', 'AIK']
</script>

<template>
  <section class="px-4 py-3 md:py-20 sm:px-6 lg:px-10">
    <div
      class="relative mx-auto max-w-[1440px] overflow-hidden rounded-3xl bg-primary-600 bg-contain bg-right bg-no-repeat px-6 py-10 sm:px-10 sm:py-12"
      :style="{ backgroundImage: `url(${darimanaBackground})` }"
    >
      <div class="relative grid gap-8 lg:grid-cols-12 lg:items-center">
        <div class="lg:col-span-5">
          <h2 class="text-balance text-[28px] leading-[1.1] font-extrabold text-white sm:text-[34px]">
            Kuliah boleh dari mana saja. Perjalananmu tetap penuh cerita.
          </h2>
        </div>
        <div class="flex flex-col gap-5 lg:col-span-7">
          <p class="max-w-xl text-base leading-relaxed text-white/80 sm:text-lg">
            Temukan ruang untuk belajar, berorganisasi, berprestasi,
            dan bertumbuh bersama komunitas SiberMu.
          </p>
          <div class="flex flex-wrap gap-2">
            <span
              v-for="item in highlights"
              :key="item"
              class="rounded-full border border-white/25 bg-white/10 px-4 py-1.5 text-sm font-medium text-white backdrop-blur-sm"
            >
              {{ item }}
            </span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
