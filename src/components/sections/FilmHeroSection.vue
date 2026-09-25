<script setup lang="ts">
import { ArrowRight, Phone } from '@lucide/vue'
import { computed, onMounted, onUnmounted, ref } from 'vue'
import filmSrc from '@/assets/film.mp4'
import { Button } from '@/components/ui/button'
import { filmScenes } from '@/data/filmScenes'

const sectionRef = ref<HTMLElement | null>(null)
const videoRef = ref<HTMLVideoElement | null>(null)
const activeScene = ref(0)
const isVideoReady = ref(false)

const sceneCount = filmScenes.length
const stageHeight = `${sceneCount * 100}vh`

function clamp(value: number, min: number, max: number) {
  return Math.min(max, Math.max(min, value))
}

let ticking = false

function updateScrub() {
  const section = sectionRef.value
  const video = videoRef.value
  if (!section) return

  const scrollableDistance = section.offsetHeight - window.innerHeight
  if (scrollableDistance <= 0) return

  const rect = section.getBoundingClientRect()
  const scrolled = clamp(-rect.top, 0, scrollableDistance)
  const progress = scrolled / scrollableDistance

  activeScene.value = clamp(Math.floor(progress * sceneCount), 0, sceneCount - 1)

  if (video && Number.isFinite(video.duration) && video.duration > 0) {
    const targetTime = progress * video.duration
    if (Math.abs(video.currentTime - targetTime) > 0.04) {
      video.currentTime = targetTime
    }
  }
}

function onScroll() {
  if (ticking) return
  ticking = true
  requestAnimationFrame(() => {
    updateScrub()
    ticking = false
  })
}

function handleLoadedMetadata() {
  isVideoReady.value = true
  updateScrub()
}

function goToScene(index: number) {
  const section = sectionRef.value
  if (!section) return
  const scrollableDistance = section.offsetHeight - window.innerHeight
  const targetProgress = (index + 0.1) / sceneCount
  const sectionTop = section.getBoundingClientRect().top + window.scrollY
  window.scrollTo({ top: sectionTop + targetProgress * scrollableDistance, behavior: 'smooth' })
}

onMounted(() => {
  window.addEventListener('scroll', onScroll, { passive: true })
  window.addEventListener('resize', onScroll)
  updateScrub()
})

onUnmounted(() => {
  window.removeEventListener('scroll', onScroll)
  window.removeEventListener('resize', onScroll)
})

const activePosition = computed(() => filmScenes[activeScene.value].position)
</script>

<template>
  <section id="beranda" ref="sectionRef" class="relative" :style="{ height: stageHeight }">
    <div class="sticky top-0 h-screen w-full overflow-hidden">
      <div class="absolute inset-0 bg-navy-950 transition-opacity duration-500" :class="isVideoReady ? 'opacity-0' : 'opacity-100'" />

      <video
        ref="videoRef"
        class="absolute inset-0 h-full w-full object-cover transition-opacity duration-500"
        :class="isVideoReady ? 'opacity-100' : 'opacity-0'"
        muted
        playsinline
        preload="auto"
        :src="filmSrc"
        @loadedmetadata="handleLoadedMetadata"
      />

      <div class="absolute inset-0 bg-gradient-to-b from-black/20 via-black/35 to-black/80" />
      <div class="absolute inset-0 bg-gradient-to-r from-black/50 via-transparent to-black/50" />

      <div class="absolute inset-0 flex items-center px-6 sm:px-10 lg:px-16">
        <div
          v-for="(scene, index) in filmScenes"
          :key="scene.title"
          class="absolute inset-x-6 top-1/2 max-w-xl -translate-y-1/2 transition-all duration-700 ease-out sm:inset-x-10 lg:inset-x-16"
          :class="[
            activeScene === index ? 'pointer-events-auto opacity-100' : 'pointer-events-none opacity-0',
            scene.position === 'center' && 'mx-auto text-center',
            scene.position === 'left' && (activeScene === index ? 'translate-x-0' : '-translate-x-4') + ' text-left',
            scene.position === 'right' && (activeScene === index ? 'translate-x-0 lg:ml-auto' : 'translate-x-4 lg:ml-auto') + ' text-left lg:text-right',
          ]"
        >
          <p class="text-xs font-semibold tracking-[0.18em] text-cyan-300 uppercase sm:text-sm">
            {{ scene.eyebrow }}
          </p>

          <h1
            v-if="scene.variant === 'hero'"
            class="mt-3 text-balance text-[40px] leading-[1.05] font-extrabold whitespace-pre-line text-white sm:text-[56px] lg:text-[68px]"
          >
            {{ scene.title }}
          </h1>
          <h2
            v-else
            class="mt-3 text-balance text-[28px] leading-[1.1] font-extrabold text-white sm:text-[38px] lg:text-[44px]"
            :class="scene.variant === 'cta' && 'text-[34px] sm:text-[48px] lg:text-[56px]'"
          >
            {{ scene.title }}
          </h2>

          <p class="mt-4 text-sm leading-relaxed text-white/75 sm:text-base lg:text-lg">
            {{ scene.body }}
          </p>

          <div
            v-if="scene.variant === 'hero'"
            class="mt-6 flex flex-col gap-3 sm:flex-row"
            :class="scene.position === 'center' && 'sm:justify-center'"
          >
            <Button as-child class="h-12 gap-2 rounded-full bg-white px-6 text-sm font-semibold text-navy-950 hover:bg-white/90">
              <a href="#kemahasiswaan">
                Jelajahi Kehidupan Mahasiswa
                <ArrowRight class="size-4" />
              </a>
            </Button>
          </div>

          <div v-if="scene.variant === 'cta'" class="mt-7 flex flex-col gap-3 sm:flex-row sm:justify-center">
            <Button as-child class="h-12 gap-2 rounded-full bg-primary-600 px-6 text-sm font-semibold hover:bg-primary-700">
              <a href="https://sibermu.ac.id" target="_blank" rel="noopener">
                Kenali SiberMu
                <ArrowRight class="size-4" />
              </a>
            </Button>
            <Button
              as-child
              variant="outline"
              class="h-12 gap-2 rounded-full border-white/30 bg-white/5 px-6 text-sm font-semibold text-white hover:bg-white/15 hover:text-white"
            >
              <a href="https://wa.me/6285179946901" target="_blank" rel="noopener">
                <Phone class="size-4" />
                Hubungi Kami
              </a>
            </Button>
          </div>
        </div>
      </div>

      <nav
        class="absolute top-1/2 right-4 z-10 hidden -translate-y-1/2 flex-col gap-3 sm:right-6 lg:flex"
        aria-label="Navigasi cerita SiberMu"
      >
        <button
          v-for="(scene, index) in filmScenes"
          :key="scene.title"
          type="button"
          class="size-2.5 rounded-full border border-white/50 transition-all"
          :class="activeScene === index ? 'scale-125 bg-white' : 'bg-white/0 hover:bg-white/40'"
          :aria-label="`Ke bagian ${index + 1}: ${scene.eyebrow}`"
          :aria-current="activeScene === index"
          @click="goToScene(index)"
        />
      </nav>

      <a
        href="#kemahasiswaan"
        class="absolute bottom-8 left-1/2 z-10 flex -translate-x-1/2 flex-col items-center gap-2 text-white/70 transition-colors hover:text-white"
        :class="activePosition === 'center' && activeScene === sceneCount - 1 ? 'opacity-0' : 'opacity-100'"
        aria-label="Gulir ke bawah"
      >
        <span class="text-[10px] font-semibold tracking-[0.2em] uppercase">Scroll</span>
        <span class="h-8 w-px bg-white/40" />
      </a>
    </div>
  </section>
</template>
