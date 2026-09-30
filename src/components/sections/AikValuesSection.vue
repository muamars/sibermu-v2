<script setup lang="ts">
const values = [
  {
    number: '01',
    title: 'Al-Qiyam Al-Fadhilah',
    description: 'Menjunjung nilai keutamaan dan orientasi pada kemajuan serta modernitas—hadir dan memberi arti pada masa kini.',
    keyword: 'Keutamaan & kemajuan',
  },
  {
    number: '02',
    title: 'Pemuliaan Manusia',
    description: 'Menjaga harkat dan martabat setiap manusia, dengan menjunjung kesetaraan serta emansipasi perempuan.',
    keyword: 'Martabat & kesetaraan',
  },
  {
    number: '03',
    title: 'Persaudaraan',
    description: 'Menguatkan ukhuwah Islamiyah dan merawat titik temu dalam menyikapi perbedaan.',
    keyword: 'Ukhuwah & kebersamaan',
  },
  {
    number: '04',
    title: 'Welas Asih',
    description: 'Mewujudkan kepedulian sosial yang nyata melalui pengamalan Teologi Al-Ma’un.',
    keyword: 'Kepedulian nyata',
  },
  {
    number: '05',
    title: 'Etos Kerja Tinggi',
    description: 'Menumbuhkan produktivitas, profesionalisme, dan semangat kerja keras dalam setiap amal usaha.',
    keyword: 'Produktif & profesional',
  },
  {
    number: '06',
    title: 'Tauhid Pro Kemanusiaan',
    description: 'Menghidupkan keimanan dan tauhid yang mendorong pembebasan serta pemberdayaan sesama.',
    keyword: 'Iman yang memberdayakan',
  },
  {
    number: '07',
    title: 'Nilai Ilmiah/Keilmuan',
    description: 'Membiasakan cara berpikir yang rasional, objektif, dan berpijak pada ilmu pengetahuan.',
    keyword: 'Rasional & berbasis ilmu',
  },
  {
    number: '08',
    title: 'Nilai Peradaban',
    description: 'Mengikhtiarkan khairu ummah—umat terbaik yang menjadi pelopor kemajuan peradaban.',
    keyword: 'Khairu ummah',
  },
]
</script>

<template>
  <section class="relative overflow-hidden bg-[#F3F7FA] px-4 py-16 sm:px-6 sm:py-20 lg:px-10 lg:py-24">
    <div class="pointer-events-none absolute -top-40 -right-24 size-[32rem] rounded-full bg-primary-100/65 blur-3xl" aria-hidden="true" />
    <div class="relative mx-auto max-w-[1440px]">
      <div class="mb-9 flex flex-col gap-5 md:flex-row md:items-end md:justify-between">
        <div class="max-w-2xl">
          <p class="mb-3 flex items-center gap-2 text-[10px] font-bold tracking-[0.2em] text-primary-600 uppercase">
            <span class="h-px w-3 bg-primary-500" aria-hidden="true" />
            Nilai Kemuhammadiyahan
          </p>
          <h2 class="text-balance text-[30px] leading-[1.08] font-extrabold tracking-tight text-navy-950 sm:text-[38px] lg:text-[44px]">
            Delapan nilai untuk <span class="text-[#078db6]">melangkah maju.</span>
          </h2>
        </div>
        <p class="max-w-md text-sm leading-relaxed text-slate-600">
          Nilai-nilai ini menjadi arah dalam menuntut ilmu, membangun hubungan, dan menghadirkan manfaat bagi sesama.
        </p>
      </div>

      <div class="grid gap-3 sm:grid-cols-2 xl:grid-cols-4">
        <article
          v-for="value in values"
          :key="value.number"
          class="group relative flex min-h-[220px] flex-col overflow-hidden rounded-[22px] border border-primary-100 bg-white p-5 transition duration-300 hover:-translate-y-1 hover:border-primary-300 hover:shadow-[0_16px_38px_rgba(12,35,52,0.09)] sm:p-6"
        >
          <div class="flex items-center justify-between">
            <span class="font-mono text-[11px] font-bold tracking-[0.14em] text-primary-500">{{ value.number }}</span>
            <span class="h-px w-10 bg-primary-200 transition-all duration-300 group-hover:w-16 group-hover:bg-[#078db6]" aria-hidden="true" />
          </div>
          <h3 class="mt-8 text-lg leading-tight font-bold tracking-tight text-navy-950">{{ value.title }}</h3>
          <p class="mt-2 text-xs leading-relaxed text-slate-600 sm:text-[13px]">{{ value.description }}</p>
          <span class="mt-auto w-fit rounded-full bg-primary-50 px-3 py-1.5 text-[9px] font-bold tracking-[0.12em] text-primary-700 uppercase">
            {{ value.keyword }}
          </span>
          <span class="pointer-events-none absolute -right-4 -bottom-8 font-mono text-[100px] leading-none font-black text-primary-600/[0.035] transition-transform duration-500 group-hover:-translate-y-2" aria-hidden="true">
            {{ value.number.slice(-1) }}
          </span>
        </article>
      </div>
    </div>
  </section>
</template>
