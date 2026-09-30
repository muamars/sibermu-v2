<script setup lang="ts">
import { Globe } from '@lucide/vue'
import logoWhite from '@/assets/sibermu-white.png'

const footerNav = [
  {
    title: 'Kemahasiswaan',
    links: [
      { label: 'Organisasi Mahasiswa', href: '#kemahasiswaan' },
      { label: 'Unit Kegiatan Mahasiswa', href: '#kemahasiswaan' },
      { label: 'Prestasi', href: '#prestasi' },
      { label: 'Layanan Mahasiswa', href: '#layanan' },
    ],
  },
  {
    title: 'AIK',
    links: [
      { label: 'Kajian', href: '#aik' },
      { label: 'Syiar', href: '#aik' },
      { label: 'Kegiatan AIK', href: '#aik' },
      { label: 'Islam Berkemajuan', href: '#aik' },
    ],
  },
  {
    title: 'Tentang',
    links: [
      { label: 'Tentang SiberMu', href: 'https://sibermu.ac.id/profil/' },
      { label: 'Website Resmi', href: 'https://sibermu.ac.id' },
      { label: 'Kontak', href: 'https://wa.me/6285179946901' },
    ],
  },
]

const socials = [
  { label: 'Instagram', href: 'https://instagram.com/sibermu', icon: 'instagram' },
  { label: 'YouTube', href: 'https://www.youtube.com/channel/UCeyzSDwnAzK3Hfza5hMcICw', icon: 'youtube' },
  { label: 'Website', href: 'https://sibermu.ac.id', icon: 'globe' },
]

const mediaCredits = [
  {
    title: 'Konten AI',
    detail: 'Hero scene3–scene6, bem.webp (Kemahasiswaan), kajian.webp (AIK), dan mulai.webp (Final CTA).',
  },
  {
    title: 'Instagram SiberMu',
    detail: 'student.png serta winner1.webp dan winner2.webp pada section Prestasi. Tautan posting spesifik belum dicatat.',
  },
  {
    title: 'Website SiberMu dan aset lokal',
    detail: 'kampus-virtual.webp, logo-only.png, sibermu-logo.png, sibermu-white.png, dan enam logo program studi di src/assets/prodi/ bersumber dari website SiberMu. aisa.webp dibuat oleh tim.',
  },
  {
    title: 'Ikon dan font',
    detail: 'Ikon Lucide (@lucide/vue, lucide.dev); font Geist, Inter Tight, dan TASA Explorer dari Google Fonts.',
  },
  {
    title: 'UI',
    detail: 'Primitif komponen interaktif dari Reka UI; gaya dan utility CSS menggunakan Tailwind CSS.',
  },
]
</script>

<template>
  <footer id="kontak" class="bg-navy-950 text-white">
    <div class="mx-auto max-w-[1440px] px-4 pt-16 pb-8 sm:px-6 lg:px-10">
      <div class="grid gap-12 lg:grid-cols-[1.3fr_2fr]">
        <div class="flex flex-col gap-4">
          <img :src="logoWhite" alt="Universitas Siber Muhammadiyah" class="h-auto w-6/12" />
          <p class="max-w-sm text-sm leading-relaxed text-white/60">
            Kampus digital yang menghadirkan pembelajaran fleksibel, komunitas yang dekat,
            dan nilai Islam Berkemajuan.
          </p>
          <div class="flex items-center gap-3 pt-2">
            <a
              v-for="social in socials"
              :key="social.label"
              :href="social.href"
              target="_blank"
              rel="noopener"
              :aria-label="social.label"
              class="inline-flex size-10 items-center justify-center rounded-full border border-white/15 text-white/70 transition-colors hover:border-white/40 hover:text-white"
            >
              <svg v-if="social.icon === 'instagram'" viewBox="0 0 24 24" fill="none" class="size-4.5" stroke="currentColor" stroke-width="1.6">
                <rect x="3" y="3" width="18" height="18" rx="5" />
                <circle cx="12" cy="12" r="4" />
                <circle cx="17.2" cy="6.8" r="0.6" fill="currentColor" stroke="none" />
              </svg>
              <svg v-else-if="social.icon === 'youtube'" viewBox="0 0 24 24" fill="none" class="size-4.5" stroke="currentColor" stroke-width="1.6">
                <rect x="2.5" y="5.5" width="19" height="13" rx="4" />
                <path d="M10.5 9.3v5.4l4.8-2.7-4.8-2.7Z" fill="currentColor" stroke="none" />
              </svg>
              <Globe v-else class="size-4.5" />
            </a>
          </div>
        </div>

        <div class="grid grid-cols-2 gap-8 sm:grid-cols-3">
          <div v-for="col in footerNav" :key="col.title" class="flex flex-col gap-3">
            <h3 class="text-sm font-semibold text-white">{{ col.title }}</h3>
            <a
              v-for="link in col.links"
              :key="link.label"
              :href="link.href"
              class="text-sm text-white/60 transition-colors hover:text-white"
              target="_blank"
              rel="noopener"
            >
              {{ link.label }}
            </a>
          </div>
        </div>
      </div>

      <div class="mt-12 flex flex-col gap-2 border-t border-white/10 pt-6">
        <p class="text-xs font-semibold tracking-wide text-white/50 uppercase">Kredit Media</p>
        <ul class="grid gap-x-8 gap-y-3 text-[11px] leading-relaxed text-white/45 sm:grid-cols-2">
          <li v-for="credit in mediaCredits" :key="credit.title">
            <strong class="font-semibold text-white/65">{{ credit.title }}:</strong>
            {{ credit.detail }}
          </li>
        </ul>
      </div>

      <div class="mt-6 flex flex-col gap-2 border-t border-white/10 pt-6 text-xs text-white/40 sm:flex-row sm:items-center sm:justify-between">
        <p>© 2026 Universitas Siber Muhammadiyah.</p>
        <p>Dibuat untuk Lomba Landing Page SiberMu 2026.</p>
      </div>
    </div>
  </footer>
</template>
