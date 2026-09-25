<script setup lang="ts">
import SectionHeading from '@/components/common/SectionHeading.vue'

const stats = [
  {
    value: '100%',
    label: 'Pembelajaran Digital',
    description: 'Belajar dengan fleksibel dari berbagai tempat.',
    tone: 'accent',
  },
  {
    value: 'Komunitas',
    label: 'Ruang untuk Bertumbuh',
    description: 'Bertemu, berkolaborasi, dan berkembang bersama.',
    tone: 'plain',
  },
  {
    value: 'Prestasi',
    label: 'Dari Ide Menjadi Karya',
    description: 'Mendorong mahasiswa untuk berani mencoba dan berkarya.',
    tone: 'plain',
  },
  {
    value: 'AIK',
    label: 'Nilai dalam Setiap Langkah',
    description: 'Menumbuhkan karakter melalui Islam Berkemajuan.',
    tone: 'aik',
  },
]
</script>

<template>
  <section class="px-4 py-16 sm:px-6 sm:py-20 lg:px-10 lg:py-28">
    <div class="mx-auto max-w-[1440px]">
      <SectionHeading
        eyebrow="Kehidupan Mahasiswa"
        title="Kampus digital, tetap terasa dekat."
        description="Jarak tidak membatasi mahasiswa SiberMu untuk saling terhubung. Melalui organisasi, komunitas, kegiatan, dan layanan mahasiswa, setiap orang memiliki ruang untuk mengenal potensi diri, membangun relasi, dan menciptakan pengalaman baru."
      />

      <div class="mt-10 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
        <div
          v-for="stat in stats"
          :key="stat.label"
          class="flex flex-col gap-2 rounded-2xl border p-6"
          :class="{
            'border-cyan-200 bg-cyan-50': stat.tone === 'accent',
            'border-border bg-white': stat.tone === 'plain',
            'border-aik-100 bg-aik-50': stat.tone === 'aik',
          }"
        >
          <span
            class="text-2xl font-extrabold"
            :class="stat.tone === 'aik' ? 'text-aik-600' : 'text-primary-700'"
          >
            {{ stat.value }}
          </span>
          <span class="text-sm font-semibold text-foreground">{{ stat.label }}</span>
          <p class="text-sm leading-relaxed text-muted-foreground">{{ stat.description }}</p>
        </div>
      </div>
    </div>
  </section>
</template>
