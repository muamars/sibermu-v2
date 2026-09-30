<script setup lang="ts">
import { computed, nextTick, onMounted, onUnmounted, ref, watch } from 'vue'

type Item = { name: string; desc: string; slug: string }

const item = (name: string, desc: string, slug: string): Item => ({ name, desc, slug })

const categories = [
  {
    id: 'organisasi',
    title: 'Organisasi Mahasiswa',
    summary: 'Belajar memimpin, bekerja dalam tim, dan mengubah ide menjadi gerakan nyata.',
    items: [
      item('Ikatan Mahasiswa Muhammadiyah (IMM)', 'Organisasi kader mahasiswa yang menekankan pengembangan intelektual, keimanan, dan kepemimpinan.', 'imm'),
      item('Hizbul Wathan', 'Gerakan kepanduan yang melatih kedisiplinan, kemandirian, dan karakter lewat kegiatan lapangan.', 'hizbul-wathan'),
      item('Tapak Suci', 'Perguruan pencak silat yang melatih kemampuan fisik, mental, dan akhlak.', 'tapak-suci'),
    ],
  },
  {
    id: 'ukm',
    title: 'Unit Kegiatan Mahasiswa',
    summary: 'Asah minat, bangun keterampilan, dan wujudkan ide bersama.',
    items: [
      item('English Club', 'Wadah berlatih bahasa Inggris lewat diskusi, permainan, dan kegiatan kebahasaan.', 'english-club'),
      item('Business Digital', 'Ruang belajar bisnis dan pemasaran digital, dari ide usaha sampai praktik langsung.', 'business-digital'),
      item('Digital Creator', 'Belajar membuat konten kreatif seperti foto, video, dan desain untuk media digital.', 'digital-creator'),
    ],
  },
  {
    id: 'komunitas',
    title: 'Komunitas Mahasiswa',
    summary: 'Temukan teman belajar dan ruang kolaborasi lintas program studi.',
    items: [
      item('Health Science Research Club', 'Komunitas untuk mahasiswa yang tertarik riset dan penulisan ilmiah di bidang kesehatan.', 'health-science-research-club'),
      item('Discord Information System SiberMu', 'Komunitas daring mahasiswa sistem informasi untuk diskusi, berbagi ilmu, dan kolaborasi.', 'discord-sibermu'),
    ],
  },
  {
    id: 'ilmiah',
    title: 'Kegiatan Ilmiah Mahasiswa',
    summary: 'Perluas wawasan, uji gagasan, dan raih pengalaman kompetisi di tingkat nasional.',
    items: [
      item('Pekan Ilmiah Mahasiswa Nasional (PIMNAS)', 'Forum ilmiah tingkat nasional untuk mempresentasikan dan memamerkan hasil karya PKM.', 'pimnas'),
      item('Program Kreativitas Mahasiswa (PKM)', 'Program pembinaan dan pendanaan gagasan kreatif mahasiswa dalam bentuk proposal karya.', 'pkm'),
      item('Kompetisi Bisnis Mahasiswa Indonesia (KBMI)', 'Kompetisi pengembangan usaha rintisan yang dijalankan mahasiswa.', 'kbmi'),
      item('Pemilihan Mahasiswa Berprestasi (MAWAPRES)', 'Seleksi mahasiswa berprestasi berdasarkan capaian akademik, organisasi, dan gagasan.', 'mawapres'),
      item('Pagelaran Mahasiswa Nasional Bidang Teknologi Informasi dan Komunikasi (GEMASTIK)', 'Ajang kompetisi nasional di bidang teknologi informasi dan komunikasi.', 'gemastik'),
      item('Kompetisi Debat Mahasiswa Indonesia (KDMI)', 'Kompetisi debat untuk mengasah argumentasi dan berpikir kritis.', 'kdmi'),
      item('Statistika Ria dan Festival Sains Data (SATRIA DATA)', 'Kompetisi dan festival di bidang statistika dan sains data.', 'satria-data'),
      item('Lomba Inovasi Digital Mahasiswa (LIDM)', 'Lomba untuk menghadirkan solusi inovatif berbasis teknologi digital.', 'lidm'),
      item('Kompetisi Nasional Mahasiswa bidang ilmu Bisnis, Manajemen, dan Keuangan (KBMK)', 'Kompetisi nasional untuk mahasiswa bidang bisnis, manajemen, dan keuangan.', 'kbmk'),
      item('Berbagai kompetisi yang diselenggarakan Pusat Prestasi Perguruan Tinggi Muhammadiyah dan Aisyiyah (PUSPRESMA PTMA)', 'Beragam kompetisi dari Pusat Prestasi PTMA yang terbuka untuk mahasiswa.', 'puspresma-ptma'),
    ],
  },
  {
    id: 'minat-bakat',
    title: 'Kegiatan Minat Bakat',
    summary: 'Salurkan potensi seni dan keagamaan melalui panggung kompetisi mahasiswa.',
    items: [
      item('Musabaqah Tilawatil Qur’an Mahasiswa Nasional', 'Kompetisi tilawah dan seni Al-Qur’an untuk mahasiswa tingkat nasional.', 'mtqmn'),
      item('Pekan Seni Mahasiswa Perguruan Tinggi Muhammadiyah/Aisyiyah (PTMA)', 'Ajang apresiasi dan kompetisi seni antar-PTMA.', 'peksimida-ptma'),
    ],
  },
  {
    id: 'internasional',
    title: 'Kegiatan Internasional',
    summary: 'Bangun perspektif global melalui pengalaman dan kolaborasi lintas negara.',
    items: [
      item('Global Youth Action', 'Program aksi pemuda lintas negara untuk isu sosial dan pembangunan berkelanjutan.', 'global-youth-action'),
      item('Youth Innovation Forum', 'Forum pemuda internasional untuk berbagi dan mengembangkan gagasan inovatif.', 'youth-innovation-forum'),
      item('Student Exchange', 'Pertukaran mahasiswa untuk belajar di kampus mitra luar negeri.', 'student-exchange'),
      item('Student Mobility', 'Program mobilitas belajar jangka pendek di kampus mitra.', 'student-mobility'),
    ],
  },
]

const activeId = ref(categories[0].id)
const activeCategory = computed(() => categories.find((c) => c.id === activeId.value) ?? categories[0])

/* Tabs */
function activateTabFromHash() {
  const id = window.location.hash.replace('#km-', '')
  if (categories.some((c) => c.id === id)) activeId.value = id
}

function onTabKeydown(event: KeyboardEvent) {
  const keys = ['ArrowRight', 'ArrowDown', 'ArrowLeft', 'ArrowUp']
  if (!keys.includes(event.key)) return
  event.preventDefault()
  const step = event.key === 'ArrowRight' || event.key === 'ArrowDown' ? 1 : -1
  const current = categories.findIndex((c) => c.id === activeId.value)
  const next = categories[(current + step + categories.length) % categories.length]
  activeId.value = next.id
  document.getElementById(`km-${next.id}`)?.focus()
}

/* Modal */
const selected = ref<Item | null>(null)
const copied = ref(false)
const dialogRef = ref<HTMLElement | null>(null)
let trigger: HTMLElement | null = null
let copyTimer: ReturnType<typeof setTimeout> | undefined

function openModal(entry: Item, event: MouseEvent) {
  trigger = event.currentTarget as HTMLElement
  copied.value = false
  selected.value = entry
}

function closeModal() {
  selected.value = null
}

function registerLink(entry: Item) {
  // Ganti dengan URL pendaftaran asli jika sudah ada
  return new URL(`/daftar/${entry.slug}`, window.location.origin).href
}

async function copyLink() {
  if (!selected.value) return
  const url = registerLink(selected.value)
  try {
    await navigator.clipboard.writeText(url)
  } catch {
    const input = document.createElement('input')
    input.value = url
    document.body.appendChild(input)
    input.select()
    document.execCommand('copy')
    input.remove()
  }
  copied.value = true
  clearTimeout(copyTimer)
  copyTimer = setTimeout(() => (copied.value = false), 2000)
}

function onWindowKeydown(event: KeyboardEvent) {
  if (event.key === 'Escape' && selected.value) closeModal()
}

watch(selected, async (value) => {
  document.body.style.overflow = value ? 'hidden' : ''
  if (value) {
    await nextTick()
    dialogRef.value?.focus()
  } else {
    trigger?.focus()
  }
})

onMounted(() => {
  activateTabFromHash()
  window.addEventListener('hashchange', activateTabFromHash)
  window.addEventListener('keydown', onWindowKeydown)
})

onUnmounted(() => {
  window.removeEventListener('hashchange', activateTabFromHash)
  window.removeEventListener('keydown', onWindowKeydown)
  document.body.style.overflow = ''
  clearTimeout(copyTimer)
})
</script>

<template>
  <section id="kemahasiswaan-detail" class="bg-[#F3F7FA] px-4 py-16 sm:px-6 sm:py-20 lg:px-10 lg:py-24">
    <div class="mx-auto max-w-[1440px]">
      <div class="mb-10 max-w-2xl sm:mb-12">
        <p class="mb-3 text-xs font-semibold tracking-wide text-primary-600">Eksplorasi Kemahasiswaan</p>
        <h2 class="text-balance text-[30px] leading-[1.1] font-extrabold tracking-tight text-navy-950 sm:text-[38px] lg:text-[44px]">
          Banyak ruang untuk <span class="text-[#078db6]">jadi lebih.</span>
        </h2>
        <p class="mt-4 max-w-xl text-sm leading-relaxed text-muted-foreground sm:text-base">
          Dari komunitas hingga kompetisi nasional dan internasional, temukan ruang yang mendukung minat, gagasan, dan langkahmu.
        </p>
      </div>

      <div class="grid gap-8 lg:grid-cols-[260px_minmax(0,1fr)] lg:gap-14">
        <!-- Tabs -->
        <div
          class="-mx-4 flex overflow-x-auto border-b border-slate-200 px-4 sm:-mx-6 sm:px-6 lg:mx-0 lg:flex-col lg:overflow-visible lg:border-b-0 lg:border-l lg:px-0"
          role="tablist"
          aria-label="Kategori kemahasiswaan"
          aria-orientation="vertical"
          @keydown="onTabKeydown"
        >
          <button
            v-for="category in categories"
            :id="`km-${category.id}`"
            :key="category.id"
            type="button"
            role="tab"
            :aria-selected="activeId === category.id"
            :aria-controls="`panel-${category.id}`"
            :tabindex="activeId === category.id ? 0 : -1"
            class="-mb-px shrink-0 border-b-2 px-4 py-3 text-left text-sm font-medium whitespace-nowrap transition-colors lg:mb-0 lg:-ml-px lg:border-b-0 lg:border-l-2 lg:py-2.5 lg:whitespace-normal"
            :class="
              activeId === category.id
                ? 'border-primary-600 text-navy-950'
                : 'border-transparent text-slate-500 hover:text-navy-950'
            "
            @click="activeId = category.id"
          >
            {{ category.title }}
          </button>
        </div>

        <!-- Panel -->
        <Transition
          mode="out-in"
          enter-active-class="transition duration-200 ease-out"
          enter-from-class="opacity-0 translate-y-1"
          leave-active-class="transition duration-100 ease-in"
          leave-to-class="opacity-0"
        >
          <section
            :id="`panel-${activeCategory.id}`"
            :key="activeCategory.id"
            role="tabpanel"
            :aria-labelledby="`km-${activeCategory.id}`"
            class="min-h-[320px]"
          >
            <div class="flex flex-wrap items-baseline justify-between gap-x-6 gap-y-1">
              <h3 class="text-2xl font-bold tracking-tight text-navy-950 sm:text-[28px]">{{ activeCategory.title }}</h3>
              <span class="text-sm text-slate-500">{{ activeCategory.items.length }} kegiatan</span>
            </div>
            <p class="mt-3 max-w-2xl text-sm leading-relaxed text-slate-600 sm:text-base">{{ activeCategory.summary }}</p>

            <ul class="mt-8 grid border-b border-slate-200 sm:grid-cols-2 sm:gap-x-10">
              <li
                v-for="entry in activeCategory.items"
                :key="entry.slug"
                class="border-t border-slate-200 sm:[&:nth-last-child(2):nth-child(odd)]:border-b-0"
              >
                <button
                  type="button"
                  class="group flex w-full items-start justify-between gap-4 py-4 text-left text-sm leading-relaxed text-navy-950 transition-colors hover:text-primary-600 sm:text-[15px]"
                  @click="openModal(entry, $event)"
                >
                  <span>{{ entry.name }}</span>
                  <span class="mt-0.5 shrink-0 text-slate-400 transition group-hover:translate-x-0.5 group-hover:text-primary-600" aria-hidden="true">→</span>
                </button>
              </li>
            </ul>
          </section>
        </Transition>
      </div>
    </div>

    <!-- Modal -->
    <Teleport to="body">
      <Transition
        enter-active-class="transition duration-200 ease-out"
        enter-from-class="opacity-0"
        leave-active-class="transition duration-150 ease-in"
        leave-to-class="opacity-0"
      >
        <div
          v-if="selected"
          class="fixed inset-0 z-50 flex items-end justify-center bg-navy-950/50 p-0 sm:items-center sm:p-6"
          @click.self="closeModal"
        >
          <div
            ref="dialogRef"
            role="dialog"
            aria-modal="true"
            aria-labelledby="km-modal-title"
            tabindex="-1"
            class="w-full max-w-md rounded-t-2xl bg-white p-6 shadow-xl outline-none sm:rounded-2xl sm:p-7"
          >
            <div class="flex items-start justify-between gap-4">
              <h4 id="km-modal-title" class="text-lg leading-snug font-bold tracking-tight text-navy-950">
                {{ selected.name }}
              </h4>
              <button
                type="button"
                class="-mr-2 -mt-1 rounded-lg p-2 text-slate-400 transition-colors hover:bg-slate-100 hover:text-navy-950"
                aria-label="Tutup"
                @click="closeModal"
              >
                <svg viewBox="0 0 20 20" class="size-4" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round">
                  <path d="M5 5l10 10M15 5L5 15" />
                </svg>
              </button>
            </div>

            <p class="mt-3 text-sm leading-relaxed text-slate-600">{{ selected.desc }}</p>

            <div class="mt-6 flex flex-col-reverse gap-2 sm:flex-row sm:justify-end">
              <button
                type="button"
                class="rounded-xl px-4 py-2.5 text-sm font-medium text-slate-600 transition-colors hover:bg-slate-100"
                @click="closeModal"
              >
                Tutup
              </button>
              <button
                type="button"
                class="rounded-xl bg-primary-600 px-5 py-2.5 text-sm font-semibold text-white transition-colors hover:bg-primary-700"
                :class="copied && 'bg-emerald-600 hover:bg-emerald-600'"
                @click="copyLink"
              >
                {{ copied ? 'Tautan tersalin' : 'Daftar' }}
              </button>
            </div>
            <p class="sr-only" role="status">{{ copied ? 'Tautan pendaftaran tersalin ke clipboard' : '' }}</p>
          </div>
        </div>
      </Transition>
    </Teleport>
  </section>
</template>