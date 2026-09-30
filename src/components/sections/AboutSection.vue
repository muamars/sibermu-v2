<script setup lang="ts">
const pillars = [
  {
    number: '1',
    title: 'Pembelajaran Jarak Jauh (PJJ)',
    description: 'Akses pembelajaran yang memungkinkan mahasiswa belajar lebih fleksibel, kapan pun dan di mana pun.',
  },
  {
    number: '2',
    title: 'Pendidikan Berbasis Teknologi',
    description: 'Pembelajaran berbasis teknologi dirancang untuk menjawab kebutuhan pendidikan di era digital.',
  },
  {
    number: '3',
    title: 'Ilmu yang Berpijak pada Nilai AIK',
    description: 'Al-Islam dan Kemuhammadiyahan menjadi sumber nilai dalam proses pendidikan dan kehidupan akademik.',
  },
  {
    number: '4',
    title: 'Ruang Untuk Bertumbuh',
    description: 'Membangun kemampuan profesional sekaligus karakter Islami untuk menghadapi dunia yang terus berkembang.',
  },
]
</script>

<template>
  <section class="relative isolate overflow-hidden bg-[#0c2b43] px-4 py-16 text-white sm:px-6 sm:py-20 lg:px-10 lg:py-24">
    <div class="pointer-events-none absolute -left-32 bottom-[-18rem] z-0 size-[34rem] rounded-full border border-white/[0.035] bg-white/[0.025]" aria-hidden="true" />
    <div class="pointer-events-none absolute -left-20 bottom-[-15rem] z-0 size-[25rem] rounded-full border border-white/[0.04]" aria-hidden="true" />

    <div class="relative z-10 mx-auto grid max-w-[1440px] gap-12 lg:grid-cols-[1.05fr_1fr] lg:items-center lg:gap-16">
      <div class="max-w-[680px]">
        <p class="mb-5 flex items-center gap-2 text-[9px] font-bold tracking-[0.2em] text-[#078db6] uppercase">
          <span class="h-px w-3 bg-cyan-400" aria-hidden="true" />
          Sebuah Perjalanan
        </p>
        <h2 class="text-balance text-[28px] leading-tight font-medium tracking-tight text-white sm:text-[36px] lg:text-[40px]">
          Mengapa Memilih <span class="font-bold">SiberMu?</span>
        </h2>
        <p class="mt-5 max-w-[660px] text-sm leading-[1.8] text-white/80">
          <span class="font-semibold text-[#078db6]">SiberMu</span> hadir untuk menjawab perubahan tersebut melalui pendidikan tinggi berbasis teknologi yang fleksibel, modern, dan tetap berpijak pada nilai Islam berkemajuan. Ilmu tidak berhenti pada penguasaan pengetahuan. Ia menjadi bekal untuk berkarya, memberi manfaat, dan menjawab kebutuhan pendidikan. SiberMu menempatkan AIK sebagai sumber nilai dalam aktivitasnya dan menargetkan lulusan yang kompeten dalam ilmu/teknologi sekaligus berkarakter Islami.
        </p>
      </div>

      <div class="grid gap-x-8 gap-y-10 sm:grid-cols-2 sm:gap-x-10 sm:gap-y-14">
        <article v-for="pillar in pillars" :key="pillar.number" class="relative min-h-[120px]">
          <span class="pointer-events-none absolute -top-14 -left-1 z-0 font-mono text-[88px] leading-none font-black text-white/[0.045] sm:text-[104px]" aria-hidden="true">
            {{ pillar.number }}
          </span>
          <div class="relative z-10 pt-1">
            <h3 class="text-sm font-semibold tracking-tight text-white sm:text-base">{{ pillar.title }}</h3>
            <p class="mt-2 max-w-[290px] text-xs leading-relaxed text-white/75 sm:text-[13px]">{{ pillar.description }}</p>
          </div>
        </article>
      </div>
    </div>
  </section>
</template>
