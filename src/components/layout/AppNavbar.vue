<script setup lang="ts">
import { ArrowRight, Menu, X } from '@lucide/vue'
import { nextTick, onMounted, onUnmounted, ref, watch } from 'vue'
import logoFull from '@/assets/sibermu-logo.png'
import logoIcon from '@/assets/logo-only.png'
import { Button } from '@/components/ui/button'
import { navigation } from '@/data/navigation'

const isOpen = ref(false)
const isScrolled = ref(false)

const navRef = ref<HTMLElement | null>(null)
const linkEls: (HTMLElement | null)[] = []
const hoveredIndex = ref<number | null>(null)
const indicator = ref({ x: 0, w: 0, visible: false })

function setLink(el: unknown, index: number) {
  linkEls[index] = (el as HTMLElement | null) ?? null
}

function measure() {
  const el = hoveredIndex.value === null ? null : linkEls[hoveredIndex.value]
  if (!el || el.offsetWidth === 0) {
    indicator.value = { ...indicator.value, visible: false }
    return
  }
  indicator.value = { x: el.offsetLeft, w: el.offsetWidth, visible: true }
}

function closeMenu() {
  isOpen.value = false
}

function onScroll() {
  isScrolled.value = window.scrollY > 24
}

function onKeydown(event: KeyboardEvent) {
  if (event.key === 'Escape') closeMenu()
}

let resizeObserver: ResizeObserver | null = null

onMounted(() => {
  window.addEventListener('scroll', onScroll, { passive: true })
  window.addEventListener('keydown', onKeydown)
  onScroll()

  if (navRef.value) {
    resizeObserver = new ResizeObserver(measure)
    resizeObserver.observe(navRef.value)
  }
})

onUnmounted(() => {
  window.removeEventListener('scroll', onScroll)
  window.removeEventListener('keydown', onKeydown)
  resizeObserver?.disconnect()
})

watch(hoveredIndex, () => nextTick(measure))
</script>

<template>
  <header class="pointer-events-none fixed inset-x-0 top-3 z-50 flex justify-center px-3 sm:top-4 sm:px-4">
    <div
      class="pointer-events-auto flex w-full flex-col items-center transition-all duration-500 ease-out motion-reduce:transition-none"
      :class="isScrolled ? 'max-w-[820px]' : 'max-w-[1120px]'"
    >
      <div
        class="relative flex w-full items-center justify-between gap-2 rounded-full border backdrop-blur-xl transition-all duration-500 ease-out motion-reduce:transition-none"
        :class="isScrolled
          ? 'border-black/10 bg-white/85 px-2.5 py-2 shadow-xl shadow-primary-900/15 sm:px-3'
          : 'border-white/40 bg-white/60 px-3 py-2.5 shadow-md shadow-black/5 sm:px-4'"
      >
        <a href="#beranda" class="relative flex items-center justify-start pl-1" @click="closeMenu">
          <img
            :src="logoFull"
            alt="Universitas Siber Muhammadiyah"
            class="h-7 w-auto transition-all duration-500 motion-reduce:transition-none sm:h-8"
            :class="isScrolled ? 'pointer-events-none scale-90 opacity-0' : 'scale-100 opacity-100'"
          />
          <img
            :src="logoIcon"
            alt="Universitas Siber Muhammadiyah"
            class="absolute top-1/2 left-1 h-12 w-12 -translate-y-1/2 object-contain transition-all duration-500 motion-reduce:transition-none"
            :class="isScrolled ? 'scale-100 opacity-100' : 'pointer-events-none scale-90 opacity-0'"
          />
        </a>

        <nav
          ref="navRef"
          class="relative hidden items-center gap-0.5 lg:flex"
          aria-label="Navigasi utama"
          @mouseleave="hoveredIndex = null"
        >
          <!-- Satu indikator yang berpindah antar menu saat di-hover -->
          <span
            class="pointer-events-none absolute top-0 bottom-0 left-0 rounded-full bg-primary-600/10 ring-1 ring-primary-600/15 transition-[transform,width,opacity] duration-300 ease-[cubic-bezier(0.22,1,0.36,1)] motion-reduce:transition-none"
            :class="indicator.visible ? 'opacity-100' : 'opacity-0'"
            :style="{ width: `${indicator.w}px`, transform: `translateX(${indicator.x}px)` }"
            aria-hidden="true"
          />
          <a
            v-for="(item, index) in navigation"
            :key="item.href"
            :ref="(el) => setLink(el, index)"
            :href="item.href"
            class="relative z-10 rounded-full px-3.5 py-2 text-sm font-medium transition-colors duration-200 outline-none focus-visible:ring-2 focus-visible:ring-primary-600"
            :class="hoveredIndex === index ? 'text-primary-700' : 'text-foreground/70'"
            @mouseenter="hoveredIndex = index"
            @focus="hoveredIndex = index"
            @blur="hoveredIndex = null"
          >
            {{ item.label }}
          </a>
        </nav>

        <div class="hidden lg:block">
          <Button
            as-child
            class="group h-10 gap-2 rounded-full bg-primary-600 px-5 text-sm font-semibold transition-all duration-300 hover:bg-primary-700 hover:shadow-lg hover:shadow-primary-600/30"
          >
            <a href="https://sibermu.ac.id" target="_blank" rel="noopener">
              Kenali SiberMu
              <ArrowRight class="size-4 transition-transform duration-300 group-hover:translate-x-1 motion-reduce:transition-none" />
            </a>
          </Button>
        </div>

        <button
          type="button"
          class="inline-flex size-9 items-center justify-center rounded-full text-foreground transition-colors hover:bg-black/5 lg:hidden"
          :aria-expanded="isOpen"
          aria-controls="mobile-menu"
          :aria-label="isOpen ? 'Tutup menu navigasi' : 'Buka menu navigasi'"
          @click="isOpen = !isOpen"
        >
          <Menu v-if="!isOpen" class="size-5" />
          <X v-else class="size-5" />
        </button>
      </div>

      <transition
        enter-active-class="transition ease-out duration-300"
        enter-from-class="opacity-0 -translate-y-3 scale-95"
        enter-to-class="opacity-100 translate-y-0 scale-100"
        leave-active-class="transition ease-in duration-150"
        leave-from-class="opacity-100 translate-y-0 scale-100"
        leave-to-class="opacity-0 -translate-y-3 scale-95"
      >
        <div
          v-if="isOpen"
          id="mobile-menu"
          class="mt-2 w-full origin-top rounded-[28px] border border-black/10 bg-white/90 p-3 shadow-xl shadow-primary-900/15 backdrop-blur-xl lg:hidden"
        >
          <nav class="flex flex-col gap-1" aria-label="Navigasi seluler">
            <a
              v-for="item in navigation"
              :key="item.href"
              :href="item.href"
              class="rounded-2xl px-4 py-3 text-base font-medium text-foreground/80 transition-colors hover:bg-black/5"
              @click="closeMenu"
            >
              {{ item.label }}
            </a>
          </nav>
          <Button as-child class="group mt-2 h-11 w-full gap-2 rounded-full bg-primary-600 text-sm font-semibold hover:bg-primary-700">
            <a href="https://sibermu.ac.id" target="_blank" rel="noopener" @click="closeMenu">
              Kenali SiberMu
              <ArrowRight class="size-4 transition-transform duration-300 group-hover:translate-x-1" />
            </a>
          </Button>
        </div>
      </transition>
    </div>
  </header>
</template>