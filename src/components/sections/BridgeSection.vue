<script setup lang="ts">
import { HandHeart, Sparkles, Users } from '@lucide/vue'
</script>

<template>
  <section class="px-4 py-14 sm:px-6 lg:px-10">
    <div class="mx-auto max-w-[1440px] rounded-3xl border border-border bg-surface px-6 py-10 sm:px-10 sm:py-14">
      <div class="flex flex-col items-center gap-4 text-center">
        <h2 class="text-balance text-[26px] leading-[1.15] font-extrabold text-foreground sm:text-[32px]">
          Aktif dalam kegiatan. Kuat dalam nilai.
        </h2>
        <p class="max-w-xl text-base leading-relaxed text-muted-foreground">
          Kemahasiswaan memberi ruang untuk bergerak. Al-Islam dan Kemuhammadiyahan
          memberi arah dalam setiap langkah. Di SiberMu, keduanya tumbuh bersama.
        </p>
      </div>

      <div class="mt-8 flex flex-col items-center gap-4 sm:flex-row sm:justify-center">
        <div class="flex w-full max-w-xs items-center gap-3 rounded-2xl border border-primary-100 bg-white px-5 py-4 sm:w-auto">
          <span class="flex size-10 shrink-0 items-center justify-center rounded-full bg-primary-50 text-primary-600">
            <Users class="size-5" :stroke-width="1.75" />
          </span>
          <span class="text-sm font-semibold text-foreground">Kemahasiswaan</span>
        </div>
        <span class="flex size-8 items-center justify-center rounded-full bg-navy-950 text-white">
          <Sparkles class="size-4" />
        </span>
        <div class="flex w-full max-w-xs items-center gap-3 rounded-2xl border border-aik-100 bg-white px-5 py-4 sm:w-auto">
          <span class="flex size-10 shrink-0 items-center justify-center rounded-full bg-aik-50 text-aik-600">
            <HandHeart class="size-5" :stroke-width="1.75" />
          </span>
          <span class="text-sm font-semibold text-foreground">AIK</span>
        </div>
      </div>
    </div>
  </section>
</template>
