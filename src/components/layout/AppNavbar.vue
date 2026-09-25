<script setup lang="ts">
import { ArrowRight, Menu, X } from '@lucide/vue'
import { onMounted, onUnmounted, ref } from 'vue'
import logoFull from '@/assets/sibermu-logo.png'
import logoIcon from '@/assets/logo-only.png'
import { Button } from '@/components/ui/button'
import { navigation } from '@/data/navigation'

const isOpen = ref(false)
const isScrolled = ref(false)

function closeMenu() {
  isOpen.value = false
}

function onScroll() {
  isScrolled.value = window.scrollY > 24
}

onMounted(() => {
  window.addEventListener('scroll', onScroll, { passive: true })
  onScroll()
})

onUnmounted(() => {
  window.removeEventListener('scroll', onScroll)
})
</script>

<template>
  <header class="pointer-events-none fixed inset-x-0 top-3 z-50 flex justify-center px-3 sm:top-4 sm:px-4">
    <div
      class="pointer-events-auto flex w-full flex-col items-center transition-all duration-300"
      :class="isScrolled ? 'max-w-[820px]' : 'max-w-[1120px]'"
    >
      <div
        class="flex w-full items-center justify-between gap-2 rounded-full border backdrop-blur-xl transition-all duration-300"
        :class="isScrolled
          ? 'border-black/10 bg-white/85 px-2.5 py-2 shadow-lg shadow-black/10 sm:px-3'
          : 'border-white/40 bg-white/60 px-3 py-2.5 shadow-md shadow-black/5 sm:px-4'"
      >
        <a href="#beranda" class="relative flex items-center justify-start pl-1" @click="closeMenu">
          <img
            :src="logoFull"
            alt="Universitas Siber Muhammadiyah"
            class="h-7 w-auto transition-all duration-300 sm:h-8"
            :class="isScrolled ? 'pointer-events-none scale-90 opacity-0' : 'scale-100 opacity-100'"
          />
          <img
            :src="logoIcon"
            alt="Universitas Siber Muhammadiyah"
            class="absolute top-1/2 left-1 h-12 w-12 -translate-y-1/2 object-contain transition-all duration-300 sm:h-12 sm:w-12"
            :class="isScrolled ? 'scale-100 opacity-100' : 'pointer-events-none scale-90 opacity-0'"
          />
        </a>

        <nav class="hidden items-center gap-0.5 lg:flex">
          <a
            v-for="item in navigation"
            :key="item.href"
            :href="item.href"
            class="rounded-full px-3.5 py-2 text-sm font-medium text-foreground/70 transition-colors hover:bg-black/5 hover:text-primary-700"
          >
            {{ item.label }}
          </a>
        </nav>

        <div class="hidden lg:block">
          <Button as-child class="h-10 gap-2 rounded-full bg-primary-600 px-5 text-sm font-semibold hover:bg-primary-700">
            <a href="https://sibermu.ac.id" target="_blank" rel="noopener">
              Kenali SiberMu
              <ArrowRight class="size-4" />
            </a>
          </Button>
        </div>

        <button
          type="button"
          class="inline-flex size-9 items-center justify-center rounded-full text-foreground transition-colors hover:bg-black/5 lg:hidden"
          :aria-expanded="isOpen"
          aria-label="Buka menu navigasi"
          @click="isOpen = !isOpen"
        >
          <Menu v-if="!isOpen" class="size-5" />
          <X v-else class="size-5" />
        </button>
      </div>

      <transition
        enter-active-class="transition ease-out duration-200"
        enter-from-class="opacity-0 -translate-y-2 scale-95"
        enter-to-class="opacity-100 translate-y-0 scale-100"
        leave-active-class="transition ease-in duration-150"
        leave-from-class="opacity-100 translate-y-0 scale-100"
        leave-to-class="opacity-0 -translate-y-2 scale-95"
      >
        <div
          v-if="isOpen"
          class="mt-2 w-full rounded-[28px] border border-black/10 bg-white/90 p-3 shadow-lg shadow-black/10 backdrop-blur-xl lg:hidden"
        >
          <nav class="flex flex-col gap-1">
            <a
              v-for="item in navigation"
              :key="item.href"
              :href="item.href"
              class="rounded-2xl px-4 py-3 text-base font-medium text-foreground/80 hover:bg-black/5"
              @click="closeMenu"
            >
              {{ item.label }}
            </a>
          </nav>
          <Button as-child class="mt-2 h-11 w-full gap-2 rounded-full bg-primary-600 text-sm font-semibold hover:bg-primary-700">
            <a href="https://sibermu.ac.id" target="_blank" rel="noopener" @click="closeMenu">
              Kenali SiberMu
              <ArrowRight class="size-4" />
            </a>
          </Button>
        </div>
      </transition>
    </div>
  </header>
</template>
