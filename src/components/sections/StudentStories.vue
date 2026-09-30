<script setup lang="ts">
import { computed, ref } from 'vue'
import { ArrowLeft, ArrowRight, Quote } from '@lucide/vue'
import { testimonials } from '@/data/testimonials'
import { usePrefersReducedMotion } from '@/composables/usePrefersReducedMotion'

const currentIndex = ref(0)
const currentTestimonial = computed(() => testimonials[currentIndex.value])
const prefersReducedMotion = usePrefersReducedMotion()

function showPrevious() {
  currentIndex.value = (currentIndex.value - 1 + testimonials.length) % testimonials.length
}

function showNext() {
  currentIndex.value = (currentIndex.value + 1) % testimonials.length
}
</script>

<template>
  <section id="cerita" class="bg-[#F3F7FA] px-4 py-12 sm:px-6 sm:py-16 lg:px-10 lg:py-20">
    <div class="mx-auto grid max-w-[1440px] gap-8 lg:grid-cols-[0.82fr_1fr] lg:items-center lg:gap-16">
      <div class="py-2 lg:py-6">
        <p class="mb-5 flex items-center gap-2 text-[9px] font-bold tracking-[0.2em] text-[#078db6] uppercase">
          <span class="h-px w-3 bg-[#078db6]" aria-hidden="true" />
          Cerita Mahasiswa
        </p>
        <h2 class="max-w-md text-balance text-[28px] leading-[1.12] font-bold tracking-tight text-[#102E43] sm:text-[36px]">
          Setiap mahasiswa<br /><span class="text-[#078db6]">punya cerita.</span>
        </h2>
        <p class="mt-5 max-w-sm text-xs leading-[1.8] text-slate-600 sm:text-sm">
          Mahasiswa datang dengan latar, tujuan, dan perjalanan yang berbeda. Namun semuanya memiliki ruang yang sama untuk tumbuh.
        </p>

        <div class="mt-6 flex items-center gap-3">
          <button
            type="button"
            class="flex size-9 items-center justify-center rounded-full border border-primary-200 text-navy-900 transition-colors hover:border-primary-500 hover:bg-white"
            aria-label="Testimoni sebelumnya"
            @click="showPrevious"
          >
            <ArrowLeft class="size-4" />
          </button>
          <span class="min-w-[38px] text-center font-mono text-[9px] font-semibold tracking-wide text-navy-900">
            {{ String(currentIndex + 1).padStart(2, '0') }} / {{ String(testimonials.length).padStart(2, '0') }}
          </span>
          <button
            type="button"
            class="flex size-9 items-center justify-center rounded-full border border-primary-200 text-navy-900 transition-colors hover:border-primary-500 hover:bg-white"
            aria-label="Testimoni berikutnya"
            @click="showNext"
          >
            <ArrowRight class="size-4" />
          </button>
        </div>
      </div>

      <div class="relative min-h-[290px] overflow-hidden rounded-[18px] border border-primary-100 bg-white p-6 shadow-[0_12px_40px_rgba(12,35,52,0.045)] sm:min-h-[310px] sm:p-8 lg:p-9">
        <Transition :name="prefersReducedMotion ? '' : 'story-switch'" mode="out-in">
          <article :key="currentIndex" class="flex min-h-[238px] flex-col">
            <Quote class="size-7 fill-[#078db6] text-[#078db6]" :stroke-width="0" aria-hidden="true" />
            <p class="mt-7 text-[7px] font-bold tracking-[0.2em] text-[#078db6] uppercase">Cerita Mahasiswa</p>
            <p class="mt-3 text-balance text-base leading-[1.65] font-medium text-[#102E43] sm:text-lg">
              {{ currentTestimonial.quote }}
            </p>

            <div class="mt-auto flex items-end justify-between gap-5 border-t border-primary-100 pt-4">
              <div>
                <p class="text-[9px] font-semibold tracking-wide text-navy-900">{{ currentTestimonial.name }}</p>
                <p class="mt-1 text-[7px] font-medium tracking-[0.16em] text-slate-500 uppercase">{{ currentTestimonial.program }}</p>
              </div>
              <span class="font-mono text-base font-bold text-primary-600">{{ String(currentIndex + 1).padStart(2, '0') }}</span>
            </div>
          </article>
        </Transition>
      </div>
    </div>
  </section>
</template>

<style scoped>
.story-switch-enter-active,
.story-switch-leave-active {
  transition: opacity 180ms ease, transform 180ms ease;
}

.story-switch-enter-from {
  opacity: 0;
  transform: translateY(8px);
}

.story-switch-leave-to {
  opacity: 0;
  transform: translateY(-8px);
}

@media (prefers-reduced-motion: reduce) {
  .story-switch-enter-active,
  .story-switch-leave-active {
    transition: none;
  }
}
</style>
