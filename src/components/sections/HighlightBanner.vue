<script setup lang="ts">
import { ref } from 'vue'
import student from '@/assets/student.png'

const activeTab = ref<'visi' | 'misi'>('visi')
const missions = [
  'Menyelenggarakan Tri Dharma Perguruan Tinggi berbasis Teknologi Informasi.',
  'Menjadikan Al-Islam dan Kemuhammadiyahan sebagai sumber nilai setiap aktivitas.',
  'Menyelenggarakan layanan pendidikan modular berbasis Teknologi Informasi.',
  'Mendukung penyelenggaraan pembelajaran online di Indonesia.',
]
</script>

<template>
  <section class="px-4 py-10 sm:px-6 sm:py-14 lg:px-10 lg:py-20">
    <div class="mx-auto grid max-w-[1440px] items-center gap-8 md:grid-cols-[1.1fr_0.9fr] md:gap-10 lg:gap-14">
      <div class="relative h-[250px] overflow-hidden rounded-[28px_28px_0_28px] sm:h-[300px] lg:h-[340px]">
        <img
          :src="student"
          alt="Mahasiswa SiberMu belajar menggunakan laptop"
          class="absolute inset-0 size-full object-cover object-top"
          loading="lazy"
        />
        <a
          href="https://www.instagram.com/sibermu/"
          target="_blank"
          rel="noopener noreferrer"
          class="absolute bottom-3 left-3 rounded-full bg-navy-950/65 px-3 py-1.5 text-[10px] font-medium text-white backdrop-blur-sm transition-colors hover:bg-navy-950/85"
        >
          Sumber: Instagram SiberMu
        </a>
      </div>

      <div class="flex flex-col items-start gap-4 text-left">
        <p class="flex items-center gap-2 text-[10px] font-bold tracking-[0.2em] text-primary-600 uppercase">
          <span class="h-px w-3 bg-primary-500" />
          Profil Kampus
        </p>

        <h2 class="max-w-[620px] text-balance text-[32px] leading-[1.08] font-extrabold tracking-tight text-foreground sm:text-[40px] lg:text-[48px]">
          Tentang <span class="text-[#078db6]">SiberMu</span>
        </h2>

        <p class="max-w-xl text-base flex flex-col gap-4 leading-relaxed text-muted-foreground sm:text-lg text-balance">
          <span>SiberMu adalah  adalah perguruan tinggi swasta resmi milik Muhammadiyah yang menyelenggarakan pendidikan tinggi dengan modus tunggal Pendidikan Jarak Jauh (PJJ) atau 100% full online.
          </span>
          <span>SiberMu berpusat di Yogyakarta, dikenal sebagai pelopor kampus PJJ berbasis metaverse pertama di Indonesia, memungkinkan mahasiswa belajar secara fleksibel dari mana saja dan kapan saja.
          </span>
        </p>

        <div class="mt-2 w-full max-w-xl">
          <div class="flex gap-2 border-b border-border" role="tablist" aria-label="Informasi SiberMu">
            <button
              id="tab-visi"
              type="button"
              role="tab"
              :aria-selected="activeTab === 'visi'"
              aria-controls="panel-visi"
              class="border-b-2 px-4 py-3 text-sm font-semibold transition-colors"
              :class="activeTab === 'visi' ? 'border-primary-600 text-primary-700' : 'border-transparent text-muted-foreground hover:text-foreground'"
              @click="activeTab = 'visi'"
            >
              Visi
            </button>
            <button
              id="tab-misi"
              type="button"
              role="tab"
              :aria-selected="activeTab === 'misi'"
              aria-controls="panel-misi"
              class="border-b-2 px-4 py-3 text-sm font-semibold transition-colors"
              :class="activeTab === 'misi' ? 'border-primary-600 text-primary-700' : 'border-transparent text-muted-foreground hover:text-foreground'"
              @click="activeTab = 'misi'"
            >
              Misi
            </button>
          </div>

          <div v-if="activeTab === 'visi'" id="panel-visi" role="tabpanel" aria-labelledby="tab-visi" class="min-h-32 py-5 text-sm leading-relaxed text-foreground/80">
            Menjadi Perguruan Tinggi Siber terpercaya, terdepan dan terkemuka yang menyediakan akses Pendidikan berkualitas secara luas berdasarkan nilai-nilai Islam berkemajuan.
          </div>
          <ol v-else id="panel-misi" role="tabpanel" aria-labelledby="tab-misi" class="min-h-32 list-decimal space-y-2 py-5 pl-5 text-sm leading-relaxed text-foreground/80 marker:font-semibold marker:text-primary-600">
            <li v-for="mission in missions" :key="mission">{{ mission }}</li>
          </ol>
        </div>
      </div>
    </div>
  </section>
</template>
