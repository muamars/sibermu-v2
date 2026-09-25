<script setup lang="ts">
import { ArrowRight, Compass } from '@lucide/vue'
import ImagePlaceholder from '@/components/common/ImagePlaceholder.vue'
import { Button } from '@/components/ui/button'
</script>

<template>
  <section id="beranda" class="px-4 py-16 sm:px-6 sm:py-20 lg:px-10 lg:py-28">
    <div class="relative mx-auto max-w-[1440px] overflow-hidden rounded-3xl sm:rounded-[32px]">
      <div class="absolute inset-0">
        <ImagePlaceholder tone="navy" label="Foto suasana belajar digital mahasiswa SiberMu" rounded="rounded-none" />
        <div class="absolute inset-0 bg-gradient-to-b from-black/10 via-black/30 to-black/75" />
      </div>

      <div
        class="pointer-events-none absolute right-0 bottom-0 left-0 overflow-hidden select-none"
        aria-hidden="true"
      >
        <span
          class="block translate-y-6 text-center text-[22vw] font-extrabold tracking-tighter text-white/10 sm:text-[160px]"
        >
          SIBERMU
        </span>
      </div>

      <div class="relative flex min-h-[560px] flex-col justify-between px-6 py-10 sm:min-h-[680px] sm:px-10 sm:py-12 lg:min-h-[720px]">
        <div class="flex items-center justify-between">
          <span class="inline-flex items-center gap-2 rounded-full border border-white/25 bg-white/10 px-3 py-1 text-[11px] font-semibold tracking-[0.14em] text-white uppercase backdrop-blur-sm">
            Kampus Digital · Islam Berkemajuan
          </span>
        </div>

        <div class="flex flex-col gap-6">
          <h1 class="max-w-2xl text-balance text-[42px] leading-[1.02] font-extrabold tracking-tight text-white sm:text-[64px] lg:text-[76px]">
              Tumbuh bersama Sibermu.
          </h1>

          <p class="max-w-md text-base leading-relaxed text-white/80 sm:text-lg">
            SiberMu bukan hanya ruang untuk kuliah. Di sini, mahasiswa belajar,
            membangun relasi, dan tumbuh bersama nilai Islam Berkemajuan.
          </p>

          <div class="flex flex-col gap-3 sm:flex-row sm:items-center">
            <Button as-child class="h-12 gap-2 rounded-full bg-white px-6 text-sm font-semibold text-navy-950 hover:bg-white/90">
              <a href="#kemahasiswaan">
                Jelajahi Kehidupan Mahasiswa
                <ArrowRight class="size-4" />
              </a>
            </Button>
            <Button
              as-child
              variant="outline"
              class="h-12 gap-2 rounded-full border-white/30 bg-white/5 px-6 text-sm font-semibold text-white hover:bg-white/15 hover:text-white"
            >
              <a href="https://sibermu.ac.id" target="_blank" rel="noopener">
                Kenali SiberMu
              </a>
            </Button>
          </div>

          <div class="flex items-center gap-2 text-xs font-medium text-white/60">
            <Compass class="size-4" />
            Belajar fleksibel. Komunitas aktif. Nilai yang berdampak.
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
