<script setup lang="ts">
import { ArrowRight, Menu, X } from '@lucide/vue'
import { ref } from 'vue'
import logo from '@/assets/sibermu-logo.png'
import { Button } from '@/components/ui/button'
import { navigation } from '@/data/navigation'

const isOpen = ref(false)

function closeMenu() {
  isOpen.value = false
}
</script>

<template>
  <header class="sticky top-0 z-50 border-b border-black/5 bg-white/80 backdrop-blur-xl">
    <div class="mx-auto flex h-20 max-w-[1440px] items-center justify-between px-4 sm:px-6 lg:px-10">
      <a href="#beranda" class="flex items-center gap-2" @click="closeMenu">
        <img :src="logo" alt="Universitas Siber Muhammadiyah" class="h-8 w-auto sm:h-9" />
      </a>

      <nav class="hidden items-center gap-7 lg:flex">
        <a
          v-for="item in navigation"
          :key="item.href"
          :href="item.href"
          class="text-sm font-medium text-foreground/70 transition-colors hover:text-primary-600"
        >
          {{ item.label }}
        </a>
      </nav>

      <div class="hidden lg:block">
        <Button as-child class="h-11 gap-2 rounded-full bg-primary-600 px-6 text-sm font-semibold hover:bg-primary-700">
          <a href="https://sibermu.ac.id" target="_blank" rel="noopener">
            Kenali SiberMu
            <ArrowRight class="size-4" />
          </a>
        </Button>
      </div>

      <button
        type="button"
        class="inline-flex size-10 items-center justify-center rounded-full text-foreground lg:hidden"
        :aria-expanded="isOpen"
        aria-label="Buka menu navigasi"
        @click="isOpen = !isOpen"
      >
        <Menu v-if="!isOpen" class="size-6" />
        <X v-else class="size-6" />
      </button>
    </div>

    <transition
      enter-active-class="transition ease-out duration-200"
      enter-from-class="opacity-0 -translate-y-2"
      enter-to-class="opacity-100 translate-y-0"
      leave-active-class="transition ease-in duration-150"
      leave-from-class="opacity-100 translate-y-0"
      leave-to-class="opacity-0 -translate-y-2"
    >
      <div v-if="isOpen" class="border-t border-black/5 bg-white px-4 pb-6 pt-2 lg:hidden">
        <nav class="flex flex-col gap-1">
          <a
            v-for="item in navigation"
            :key="item.href"
            :href="item.href"
            class="rounded-xl px-3 py-3 text-base font-medium text-foreground/80 hover:bg-surface"
            @click="closeMenu"
          >
            {{ item.label }}
          </a>
        </nav>
        <Button as-child class="mt-3 h-11 w-full gap-2 rounded-full bg-primary-600 text-sm font-semibold hover:bg-primary-700">
          <a href="https://sibermu.ac.id" target="_blank" rel="noopener" @click="closeMenu">
            Kenali SiberMu
            <ArrowRight class="size-4" />
          </a>
        </Button>
      </div>
    </transition>
  </header>
</template>
