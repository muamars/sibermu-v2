<script setup lang="ts">
import { ArrowRight } from '@lucide/vue'
import { computed, onMounted, onUnmounted, ref } from 'vue'

import filmSrc from '@/assets/film-hero-final.mp4'
import { Button } from '@/components/ui/button'
import { filmScenes } from '@/data/filmScenes'

const sectionRef = ref<HTMLElement | null>(null)
const videoRef = ref<HTMLVideoElement | null>(null)

const activeScene = ref(0)
const isVideoReady = ref(false)

/**
 * Semua scene berdurasi 4 detik.
 * 6 scene × 4 detik = 24 detik.
 */
const SCENE_DURATION = 4
const SCENE_COUNT = 7

/**
 * 1 scene = 100vh scroll.
 * Total 6 scene = 600vh.
 */
const SCROLL_VH_PER_SCENE = 100

const scenes = computed(() => filmScenes.slice(0, SCENE_COUNT))
const sceneCount = computed(() => scenes.value.length)

const totalDuration = computed(() => {
  return sceneCount.value * SCENE_DURATION
})

const stageHeight = computed(() => {
  return `${sceneCount.value * SCROLL_VH_PER_SCENE}vh`
})

const currentScene = computed(() => {
  return scenes.value[activeScene.value] ?? scenes.value[0]
})

const activePosition = computed(() => {
  return currentScene.value?.position ?? 'center'
})

function clamp(value: number, min: number, max: number) {
  return Math.min(max, Math.max(min, value))
}

let ticking = false

function updateScrub() {
  const section = sectionRef.value
  const video = videoRef.value

  if (!section || !video || !isVideoReady.value) return

  const scrollableDistance = section.offsetHeight - window.innerHeight

  if (scrollableDistance <= 0) return

  const rect = section.getBoundingClientRect()

  const scrolled = clamp(
    -rect.top,
    0,
    scrollableDistance,
  )

  const scrollProgress = scrolled / scrollableDistance

  /**
   * Timeline video yang dipakai hanya 24 detik.
   * Kalau file punya sedikit frame ekstra, tetap dibatasi 24 detik.
   */
  const usableDuration = Math.min(
    totalDuration.value,
    video.duration,
  )

  const targetTime = clamp(
    scrollProgress * usableDuration,
    0,
    Math.max(usableDuration - 0.001, 0),
  )

  /**
   * Karena semua scene 4 detik:
   *
   * 0–4   = scene 1
   * 4–8   = scene 2
   * 8–12  = scene 3
   * 12–16 = scene 4
   * 16–20 = scene 5
   * 20–24 = scene 6
   */
  const sceneIndex = clamp(
    Math.floor(targetTime / SCENE_DURATION),
    0,
    sceneCount.value - 1,
  )

  activeScene.value = sceneIndex

  /**
   * Jangan seek untuk selisih terlalu kecil.
   * Ini membantu mengurangi jitter saat scroll pelan.
   */
  if (Math.abs(video.currentTime - targetTime) > 0.025) {
    video.currentTime = targetTime
  }
}

function handleScroll() {
  if (ticking) return

  ticking = true

  requestAnimationFrame(() => {
    updateScrub()
    ticking = false
  })
}

function handleResize() {
  updateScrub()
}

function handleLoadedMetadata() {
  const video = videoRef.value

  if (!video) return

  video.pause()
  isVideoReady.value = true

  requestAnimationFrame(() => {
    updateScrub()
  })
}

/**
 * Klik indicator langsung menuju scene terkait.
 * Sedikit offset dipakai supaya tidak berhenti persis
 * pada frame transisi antar scene.
 */
function goToScene(index: number) {
  const section = sectionRef.value

  if (!section) return

  const scrollableDistance = section.offsetHeight - window.innerHeight

  if (scrollableDistance <= 0) return

  const sceneStartTime = index * SCENE_DURATION
  const safeOffset = 0.15
  const targetTime = sceneStartTime + safeOffset

  const targetProgress = clamp(
    targetTime / totalDuration.value,
    0,
    1,
  )

  const sectionTop =
    section.getBoundingClientRect().top +
    window.scrollY

  window.scrollTo({
    top:
      sectionTop +
      targetProgress * scrollableDistance,
    behavior: 'smooth',
  })
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll, {
    passive: true,
  })

  window.addEventListener('resize', handleResize)

  requestAnimationFrame(() => {
    updateScrub()
  })
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
  window.removeEventListener('resize', handleResize)
})
</script>

<template>
  <section
    id="beranda"
    ref="sectionRef"
    class="relative"
    :style="{ height: stageHeight }"
  >
    <div
      class="sticky top-0 h-screen w-full overflow-hidden bg-[#092845]"
    >
      <!-- VIDEO -->
      <video
        ref="videoRef"
        :src="filmSrc"
        muted
        playsinline
        preload="auto"
        class="absolute inset-0 h-full w-full object-cover transition-opacity duration-500"
        :class="
          isVideoReady
            ? 'opacity-100'
            : 'opacity-0'
        "
        @loadedmetadata="handleLoadedMetadata"
      />

      <!-- FALLBACK -->
      <div
        class="absolute inset-0 bg-[#092845] transition-opacity duration-500"
        :class="
          isVideoReady
            ? 'pointer-events-none opacity-0'
            : 'opacity-100'
        "
      />

      <!-- SOFT GLOBAL OVERLAY -->
      <div
        class="pointer-events-none absolute inset-0 bg-gradient-to-b from-black/5 via-transparent to-black/30"
      />

      <!-- DYNAMIC OVERLAY SESUAI POSISI TEKS -->
      <div
        class="pointer-events-none absolute inset-0 transition-all duration-700"
        :class="{
          'bg-gradient-to-r from-black/55 via-black/15 to-transparent':
            activePosition === 'left',

          'bg-gradient-to-l from-black/55 via-black/15 to-transparent':
            activePosition === 'right',

          'bg-gradient-to-t from-black/55 via-black/10 to-black/5':
            activePosition === 'center',
        }"
      />

      <!-- CONTENT -->
      <div
        class="absolute inset-0 z-10 flex items-center px-6 sm:px-10 lg:px-16 xl:px-24"
      >
        <Transition
          mode="out-in"
          enter-active-class="transition-all duration-500 ease-out"
          enter-from-class="translate-y-4 opacity-0"
          enter-to-class="translate-y-0 opacity-100"
          leave-active-class="transition-all duration-300 ease-in"
          leave-from-class="translate-y-0 opacity-100"
          leave-to-class="-translate-y-3 opacity-0"
        >
          <div
            :key="activeScene"
            class="w-full"
          >
            <div
              class="max-w-[620px]"
              :class="{
                'mx-auto text-center':
                  currentScene.position === 'center',

                'mr-auto text-left':
                  currentScene.position === 'left',

                'ml-auto text-left lg:text-right':
                  currentScene.position === 'right',
              }"
            >
              <p
                class="text-[11px] font-semibold tracking-[0.18em] text-white/70 uppercase sm:text-xs"
              >
                {{ currentScene.eyebrow }}
              </p>

              <h1
                v-if="currentScene.variant === 'hero'"
                class="mt-4 text-balance text-[42px] leading-[0.98] font-bold tracking-[-0.04em] text-white sm:text-[58px] lg:text-[72px]"
              >
                {{ currentScene.title }}
              </h1>

              <h2
                v-else
                class="mt-4 text-balance text-[34px] leading-[1.03] font-bold tracking-[-0.035em] text-white sm:text-[44px] lg:text-[54px]"
              >
                {{ currentScene.title }}
              </h2>

              <p
                class="mt-5 max-w-[540px] text-sm leading-[1.75] text-white/75 sm:text-base lg:text-[17px]"
                :class="{
                  'mx-auto':
                    currentScene.position === 'center',

                  'lg:ml-auto':
                    currentScene.position === 'right',
                }"
              >
                {{ currentScene.body }}
              </p>

              <!-- HERO CTA -->
              <div
                v-if="currentScene.variant === 'hero'"
                class="mt-7 flex flex-col gap-3 sm:flex-row"
                :class="
                  currentScene.position === 'center'
                    ? 'sm:justify-center'
                    : ''
                "
              >
                <Button
                  as-child
                  class="h-12 gap-2 rounded-full bg-white px-6 text-sm font-semibold text-[#092845] hover:bg-white/90"
                >
                  <a href="#kemahasiswaan">
                    Jelajahi Kehidupan Mahasiswa
                    <ArrowRight class="size-4" />
                  </a>
                </Button>
              </div>
            </div>
          </div>
        </Transition>
      </div>

      <!-- SCENE INDICATOR -->
      <div
        class="absolute bottom-8 left-1/2 z-20 flex -translate-x-1/2 items-center gap-2"
      >
        <button
          v-for="(scene, index) in scenes"
          :key="scene.title"
          type="button"
          class="group relative flex h-5 items-center justify-center"
          :aria-label="`Scene ${index + 1}: ${scene.title}`"
          :aria-current="
            activeScene === index
              ? 'true'
              : undefined
          "
          @click="goToScene(index)"
        >
          <span
            class="block rounded-full transition-all duration-300"
            :class="
              activeScene === index
                ? 'h-1.5 w-8 bg-white'
                : 'size-1.5 bg-white/35 group-hover:bg-white/70'
            "
          />
        </button>
      </div>

      <!-- SCROLL HINT -->
      <div
        class="pointer-events-none absolute bottom-8 left-6 z-20 hidden items-center gap-3 text-white/50 sm:flex lg:left-10"
      >
        <span
          class="text-[9px] font-semibold tracking-[0.2em] uppercase"
        >
          Scroll
        </span>

        <span class="h-px w-10 bg-white/30" />
      </div>

      <!-- SCENE NUMBER -->
      <div
        class="pointer-events-none absolute right-6 bottom-8 z-20 hidden items-baseline gap-1 text-white sm:flex lg:right-10"
      >
        <span class="text-sm font-semibold">
          {{
            String(activeScene + 1).padStart(
              2,
              '0',
            )
          }}
        </span>

        <span class="text-[10px] text-white/40">
          /
          {{
            String(sceneCount).padStart(
              2,
              '0',
            )
          }}
        </span>
      </div>
    </div>
  </section>
</template>
