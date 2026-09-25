<script setup lang="ts">
import { onMounted, onUnmounted, ref } from 'vue'

const progress = ref(0)
let ticking = false

function update() {
  const doc = document.documentElement
  const scrollable = doc.scrollHeight - doc.clientHeight
  progress.value = scrollable > 0 ? (doc.scrollTop / scrollable) * 100 : 0
}

function onScroll() {
  if (ticking) return
  ticking = true
  requestAnimationFrame(() => {
    update()
    ticking = false
  })
}

onMounted(() => {
  window.addEventListener('scroll', onScroll, { passive: true })
  window.addEventListener('resize', onScroll)
  update()
})

onUnmounted(() => {
  window.removeEventListener('scroll', onScroll)
  window.removeEventListener('resize', onScroll)
})
</script>

<template>
  <div class="pointer-events-none fixed top-0 right-0 left-0 z-[60] h-[3px] bg-transparent" aria-hidden="true">
    <div class="h-full bg-primary-600 transition-[width] duration-150 ease-out" :style="{ width: `${progress}%` }" />
  </div>
</template>
