<script setup lang="ts">
import { Quote, UserRound } from '@lucide/vue'
import SectionHeading from '@/components/common/SectionHeading.vue'
import { testimonials } from '@/data/testimonials'
</script>

<template>
  <section id="cerita" class="px-4 py-16 sm:px-6 sm:py-20 lg:px-10 lg:py-28">
    <div class="mx-auto max-w-[1280px]">
      <SectionHeading
        align="center"
        eyebrow="Cerita Mahasiswa"
        title="Setiap perjalanan punya cerita."
        description="Mahasiswa datang dengan latar, tujuan, dan perjalanan yang berbeda. Namun semuanya memiliki ruang yang sama untuk tumbuh."
      />

      <div class="mx-auto mt-10 grid max-w-full gap-5 lg:grid-cols-3">
        <div
          v-for="testimonial in testimonials"
          :key="testimonial.name"
          class="flex min-h-[320px] flex-col justify-between rounded-3xl p-7"
          :class="testimonial.tone === 'primary' ? 'bg-primary-600 text-white' : 'bg-surface text-foreground'"
        >
          <div class="flex items-center justify-between">
            <span
              class="flex size-11 items-center justify-center rounded-full"
              :class="testimonial.tone === 'primary' ? 'bg-white/15' : 'bg-white'"
            >
              <UserRound class="size-5" :stroke-width="1.75" />
            </span>
            <Quote class="size-6 opacity-40" />
          </div>

          <p class="mt-6 text-balance text-lg leading-relaxed font-medium">
            "{{ testimonial.quote }}"
          </p>

          <div class="mt-6 flex flex-col">
            <span class="text-sm font-semibold">{{ testimonial.name }}</span>
            <span class="text-xs opacity-70">{{ testimonial.program }}</span>
          </div>
        </div>
      </div>

      <p class="mx-auto mt-6 max-w-2xl text-center text-xs leading-relaxed text-muted-foreground">
        Testimoni di atas merupakan gambaran umum pengalaman mahasiswa dan menunggu
        pengisian cerita nyata dari mahasiswa SiberMu beserta izin publikasinya.
      </p>
    </div>
  </section>
</template>
