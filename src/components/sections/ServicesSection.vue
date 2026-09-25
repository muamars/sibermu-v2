<script setup lang="ts">
import { Briefcase, ClipboardList, GraduationCap, LifeBuoy, MessageCircle, Wallet } from '@lucide/vue'
import SectionHeading from '@/components/common/SectionHeading.vue'
import { services } from '@/data/services'

const icons = { GraduationCap, Wallet, MessageCircle, ClipboardList, Briefcase, LifeBuoy }
</script>

<template>
  <section id="layanan" class="px-4 py-16 sm:px-6 sm:py-20 lg:px-10 lg:py-28">
    <div class="mx-auto max-w-[1280px]">
      <SectionHeading
        eyebrow="Layanan Mahasiswa"
        title="Ada yang mendukungmu di setiap perjalanan."
        description="Dari kebutuhan akademik hingga pengembangan diri, SiberMu menghadirkan layanan untuk membantu mahasiswa menjalani perkuliahan dengan lebih nyaman."
      />

      <div class="mt-10 grid gap-4 grid-cols-2 md:grid-cols-3">
        <div
          v-for="service in services"
          :key="service.title"
          class="flex flex-col gap-4 rounded-2xl border border-border bg-white p-6 transition-all duration-300 hover:-translate-y-1 hover:shadow-md"
        >
          <span class="flex size-11 items-center justify-center rounded-full bg-primary-50 text-primary-600">
            <component :is="icons[service.icon]" class="size-5" :stroke-width="1.75" />
          </span>
          <h3 class="text-base font-bold text-foreground">{{ service.title }}</h3>
          <p class="text-sm leading-relaxed text-muted-foreground">{{ service.description }}</p>
        </div>
      </div>
    </div>
  </section>
</template>
