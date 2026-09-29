<script setup lang="ts">
import { ArrowRight } from '@lucide/vue'
import { computed, onMounted, onUnmounted, ref } from 'vue'
import scene1 from '@/assets/scene1.webp'
import scene2 from '@/assets/scene2.webp'
import scene3 from '@/assets/scene3.webp'
import scene4 from '@/assets/scene4.webp'
import scene5 from '@/assets/scene5.webp'
import scene6 from '@/assets/scene6.webp'
import scene7 from '@/assets/scene7.webp'
import { Button } from '@/components/ui/button'
import { filmScenes } from '@/data/filmScenes'

const images = [scene1, scene2, scene3, scene4, scene5, scene6, scene7]
const scenes = filmScenes.slice(0, images.length).map((copy, index) => ({
  ...copy,
  image: images[index],
}))

const sectionRef = ref<HTMLElement | null>(null)
const activeScene = ref(0)
const sceneCount = scenes.length
const stageHeight = computed(() => `${sceneCount * 100}vh`)
const currentScene = computed(() => scenes[activeScene.value] ?? scenes[0])

function clamp(value: number, min: number, max: number) {
  return Math.min(max, Math.max(min, value))
}

let ticking = false
let wheelLocked = false

function updateScene() {
  const section = sectionRef.value
  if (!section) return

  const scrollableDistance = section.offsetHeight - window.innerHeight
  if (scrollableDistance <= 0) return

  const progress = clamp(-section.getBoundingClientRect().top / scrollableDistance, 0, 1)
  activeScene.value = Math.min(Math.floor(progress * sceneCount), sceneCount - 1)
}

function handleScroll() {
  if (ticking) return
  ticking = true
  requestAnimationFrame(() => {
    updateScene()
    ticking = false
  })
}

function goToScene(index: number) {
  const section = sectionRef.value
  if (!section) return

  const scrollableDistance = section.offsetHeight - window.innerHeight
  const sectionTop = section.getBoundingClientRect().top + window.scrollY
  const progress = index / sceneCount
  window.scrollTo({ top: sectionTop + progress * scrollableDistance, behavior: 'smooth' })
}

function handleWheel(event: WheelEvent) {
  const section = sectionRef.value
  if (!section || wheelLocked || event.deltaY === 0) return

  const rect = section.getBoundingClientRect()
  const isInsideHero = rect.top < window.innerHeight && rect.bottom > 0
  if (!isInsideHero) return

  const nextScene = activeScene.value + (event.deltaY > 0 ? 1 : -1)
  if (nextScene < 0 || nextScene >= sceneCount) return

  event.preventDefault()
  wheelLocked = true
  goToScene(nextScene)
  window.setTimeout(() => {
    wheelLocked = false
  }, 650)
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll, { passive: true })
  window.addEventListener('resize', updateScene)
  window.addEventListener('wheel', handleWheel, { passive: false })
  updateScene()
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
  window.removeEventListener('resize', updateScene)
  window.removeEventListener('wheel', handleWheel)
})
</script>

<template>
  <section id="beranda" ref="sectionRef" class="relative" :style="{ height: stageHeight }">
    <div class="sticky top-0 h-dvh min-h-[560px] w-full overflow-hidden bg-[#092845]">
      <Transition mode="out-in" name="hero-image">
        <img
          :key="currentScene.image"
          :src="currentScene.image"
          alt=""
          class="absolute inset-0 size-full object-cover"
        />
      </Transition>

      <div class="pointer-events-none absolute inset-0 bg-gradient-to-b from-black/10 via-black/15 to-black/45" />
      <div
        class="pointer-events-none absolute inset-0 transition-all duration-700"
        :class="{
          'bg-gradient-to-r from-black/65 via-black/25 to-transparent': currentScene.position === 'left',
          'bg-gradient-to-l from-black/65 via-black/25 to-transparent': currentScene.position === 'right',
          'bg-gradient-to-t from-black/55 via-black/15 to-black/10': currentScene.position === 'center',
        }"
      />

      <div class="absolute inset-0 z-10 flex items-center px-6 sm:px-10 lg:px-16 xl:px-24">
        <Transition mode="out-in" name="hero-copy">
          <div :key="activeScene" class="w-full">
            <div
              class="max-w-[620px]"
              :class="{
                'mx-auto text-center': currentScene.position === 'center',
                'mr-auto text-left': currentScene.position === 'left',
                'ml-auto text-left lg:text-right': currentScene.position === 'right',
              }"
            >
              <p class="text-[11px] font-semibold tracking-[0.18em] text-white/75 uppercase sm:text-xs">
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
                class="mt-5 max-w-[540px] text-sm leading-[1.75] text-white/85 sm:text-base lg:text-[17px]"
                :class="{
                  'mx-auto': currentScene.position === 'center',
                  'lg:ml-auto': currentScene.position === 'right',
                }"
              >
                {{ currentScene.body }}
              </p>

              <div
                v-if="currentScene.variant === 'hero'"
                class="mt-7 flex flex-col gap-3 sm:flex-row"
                :class="currentScene.position === 'center' ? 'sm:justify-center' : ''"
              >
                <Button as-child class="h-12 gap-2 rounded-full bg-white px-6 text-sm font-semibold text-[#092845] hover:bg-white/90">
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

      <div class="absolute bottom-8 left-1/2 z-20 flex -translate-x-1/2 items-center gap-2">
        <button
          v-for="(scene, index) in scenes"
          :key="scene.title"
          type="button"
          class="group relative flex h-5 items-center justify-center"
          :aria-label="`Scene ${index + 1}: ${scene.title}`"
          :aria-current="activeScene === index ? 'true' : undefined"
          @click="goToScene(index)"
        >
          <span
            class="block rounded-full transition-all duration-300"
            :class="activeScene === index ? 'h-1.5 w-8 bg-white' : 'size-1.5 bg-white/45 group-hover:bg-white/80'"
          />
        </button>
      </div>

      <div class="pointer-events-none absolute right-6 bottom-8 z-20 hidden items-baseline gap-1 text-white sm:flex lg:right-10">
        <span class="text-sm font-semibold">{{ String(activeScene + 1).padStart(2, '0') }}</span>
        <span class="text-[10px] text-white/60">/ {{ String(sceneCount).padStart(2, '0') }}</span>
      </div>
    </div>
  </section>
</template>

<style scoped>
.hero-image-enter-active,
.hero-image-leave-active,
.hero-copy-enter-active,
.hero-copy-leave-active {
  transition: opacity 350ms ease, transform 350ms ease;
}

.hero-image-enter-from,
.hero-image-leave-to {
  opacity: 0;
}

.hero-copy-enter-from {
  opacity: 0;
  transform: translateY(1rem);
}

.hero-copy-leave-to {
  opacity: 0;
  transform: translateY(-0.75rem);
}
</style>
