<script setup lang="ts">
import student from '@/assets/student.png'
</script>

<template>
  <section class="px-4 py-10 sm:px-6 sm:py-14 lg:px-10 lg:py-20">
    <div class="mx-auto grid max-w-[1440px] items-center gap-8 md:grid-cols-[1.1fr_0.9fr] md:gap-10 lg:gap-14">
      <div class="relative h-[250px] overflow-hidden rounded-[28px_28px_0_28px] sm:h-[300px] lg:h-[340px]">
        <img
          :src="student"
          alt="Mahasiswa SiberMu belajar menggunakan laptop"
          class="absolute inset-0 size-full object-cover object-top"
          loading="lazy"
        />
      </div>

      <div class="flex flex-col gap-4 items-start text-left">
        <p class="flex items-center gap-2 text-[10px] font-bold tracking-[0.2em] text-primary-600 uppercase">
          <span class="h-px w-3 bg-primary-500" />
          Sebuah Perjalanan
        </p>

        <h2 class="max-w-[620px] text-balance text-[32px] leading-[1.08] font-extrabold tracking-tight text-foreground sm:text-[40px] lg:text-[48px]">
          Kuliah boleh dari mana saja,
          <span class="block text-[#078db6]">Perjalananmu tetap penuh cerita.</span>
        </h2>

        <p class="max-w-xl text-base leading-relaxed text-muted-foreground sm:text-lg">
          Temukan ruang untuk belajar, berorganisasi, berprestasi,
          dan bertumbuh bersama komunitas SiberMu.
        </p>
      </div>
    </div>
  </section>
</template>
