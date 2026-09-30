<script setup lang="ts">
import { ArrowRight } from '@lucide/vue'
import { ref } from 'vue'
import campusImage from '@/assets/kampus-virtual.webp'
import { usePrefersReducedMotion } from '@/composables/usePrefersReducedMotion'

const imageFrame = ref<HTMLElement | null>(null)
const tilt = ref({ x: 0, y: 0 })
const prefersReducedMotion = usePrefersReducedMotion()

function handleImagePointerMove(event: PointerEvent) {
  const frame = imageFrame.value
  if (!frame || prefersReducedMotion.value || event.pointerType === 'touch') return

  const bounds = frame.getBoundingClientRect()
  const x = (event.clientX - bounds.left) / bounds.width - 0.5
  const y = (event.clientY - bounds.top) / bounds.height - 0.5
  tilt.value = { x: y * -5, y: x * 5 }
}

function resetImageTilt() {
  tilt.value = { x: 0, y: 0 }
}
</script>

<template>
  <section class="bg-navy-950 px-4 py-12 text-white sm:px-6 sm:py-16 lg:px-10">
    <div class="mx-auto max-w-[1440px]">
      <div class="grid gap-8 lg:grid-cols-2 lg:items-center lg:gap-12">
        <div>
          <p class="mb-3 flex items-center gap-2 text-[10px] font-bold tracking-[0.18em] text-white/80 uppercase">
            <span class="h-px w-3 bg-cyan-400" aria-hidden="true" />
            Teknologi Kampus Virtual
          </p>
          <h2 class="text-balance text-[32px] leading-[1.08] font-semibold tracking-tight sm:text-[40px]">
            Satu Kampus,<br />
            <span class="text-[#11BAEE]">Tanpa Batas Ruang.</span>
          </h2>
        </div>

        <div class="lg:pt-8">
          <p class="max-w-xl text-sm leading-relaxed text-white/75 sm:text-base">
            <strong class="font-semibold text-white/90">Kampus Virtual SiberMu</strong>
            menghadirkan ruang belajar digital yang membantu mahasiswa tetap terhubung dengan aktivitas akademik dari mana pun mereka berada.
          </p>
          <a
            href="https://sibermu.ac.id"
            target="_blank"
            rel="noopener noreferrer"
            class="mt-6 inline-flex items-center gap-2 text-xs font-semibold text-white transition-colors hover:text-[#078db6]"
          >
            Jelajahi Kampus Virtual
            <ArrowRight class="size-4" />
          </a>
        </div>
      </div>

      <div
        ref="imageFrame"
        class="mt-8 aspect-[16/10] overflow-hidden rounded-b-2xl [perspective:1000px] sm:mt-10 sm:aspect-[16/8] sm:rounded-b-[18px]"
        @pointermove="handleImagePointerMove"
        @pointerleave="resetImageTilt"
      >
        <img
          :src="campusImage"
          alt="Visual kampus virtual SiberMu"
          class="block h-full w-full scale-[1.04] object-cover transition-transform duration-300 ease-out will-change-transform"
          :style="{ transform: `rotateX(${tilt.x}deg) rotateY(${tilt.y}deg) scale(1.04)` }"
        />
      </div>
    </div>
  </section>
</template>
