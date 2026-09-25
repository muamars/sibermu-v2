# DESIGN.md — Landing Page SiberMu 2026

## 1. Ringkasan

Dokumen ini menjadi acuan visual dan implementasi untuk **Landing Page SiberMu 2026** menggunakan:

- **Vue 3**
- **Vite**
- **Tailwind CSS**
- JavaScript / TypeScript sesuai kebutuhan proyek
- Pendekatan **responsive-first**
- Komponen modular dan reusable

Arah desain mengambil inspirasi dari referensi yang diberikan: layout universitas modern, whitespace luas, tipografi besar, card-based layout, warna biru cerah sebagai aksen utama, dan penggunaan foto mahasiswa sebagai elemen visual utama.

Desain **tidak menyalin referensi secara identik**. Bahasa visual akan disesuaikan dengan identitas **Universitas Siber Muhammadiyah**, nuansa **Islami, akademik, modern, muda, dan digital**.

---

# 2. Design Direction

## 2.1 Konsep Utama

Tema visual:

> **Belajar, Berkarya, Berdampak.**

Landing page harus terasa:

- modern
- akademik
- human-centered
- Islami namun tidak kaku
- youthful
- clean
- digital-first
- premium tetapi tetap approachable

Nuansa utama bukan seperti website institusi pemerintahan, melainkan seperti **modern digital university landing page**.

---

## 2.2 Kata Kunci Visual

- Clean
- Spacious
- Editorial
- Modern University
- Digital Campus
- Muhammadiyah
- Gen Z
- Human
- Friendly
- Bold Typography
- Modular Cards
- Soft Rounded Corners
- Blue Accent
- Subtle Islamic Geometry

---

# 3. Brand & Color System

## 3.1 Primary Colors

Gunakan biru SiberMu / Muhammadiyah sebagai warna utama.

```css
--color-primary: #1268F3;
--color-primary-600: #0F5CDA;
--color-primary-700: #0D4FC0;
--color-primary-soft: #EAF2FF;
```

Rekomendasi Tailwind:

```js
primary: {
  50: '#F3F7FF',
  100: '#EAF2FF',
  200: '#D6E6FF',
  300: '#AFCFFF',
  400: '#74AFFF',
  500: '#3B8CFF',
  600: '#1268F3',
  700: '#0F5CDA',
  800: '#104DB2',
  900: '#123F8C',
}
```

---

## 3.2 Secondary / Cyan

Untuk aksen modern seperti pada referensi.

```css
--color-cyan: #35E6ED;
--color-cyan-soft: #DDFBFC;
```

Digunakan untuk:

- decorative line
- badge
- icon background
- hover state
- CTA secondary
- ornament abstrak

---

## 3.3 Neutral

```css
--color-dark: #050816;
--color-text: #111827;
--color-muted: #64748B;
--color-border: #E5E7EB;
--color-surface: #F7F8FA;
--color-white: #FFFFFF;
```

---

## 3.4 Islamic Accent

Untuk elemen AIK gunakan hijau sebagai aksen sekunder, **bukan sebagai warna dominan halaman**.

```css
--color-aik: #0F9D72;
--color-aik-soft: #E8F8F2;
```

Penggunaan:

- tag AIK
- icon kegiatan keislaman
- badge kajian
- elemen dekoratif pada section AIK

---

# 4. Typography

Gunakan sans-serif modern yang bersih.

Rekomendasi:

1. **Plus Jakarta Sans**
2. **Manrope**
3. **Inter**
4. **Satoshi** jika memiliki lisensi

Pilihan utama:

```txt
Plus Jakarta Sans
```

Import melalui Google Fonts jika diperlukan.

---

## 4.1 Type Scale

### Hero Display

Desktop:

```txt
64–84px
font-weight: 700 / 800
line-height: 0.95–1.05
letter-spacing: -0.04em
```

Mobile:

```txt
42–52px
```

### Section Heading

Desktop:

```txt
42–56px
font-weight: 700
line-height: 1.05
letter-spacing: -0.03em
```

Mobile:

```txt
32–40px
```

### Card Heading

```txt
22–28px
font-weight: 600–700
```

### Body

```txt
16–18px
line-height: 1.65
```

### Small Text

```txt
12–14px
```

---

# 5. Layout System

## 5.1 Container

Desktop:

```html
max-w-[1440px] mx-auto px-6 lg:px-10
```

Main content area:

```html
max-w-[1280px] mx-auto
```

Mobile:

```html
px-4
```

---

## 5.2 Section Spacing

Desktop:

```txt
py-24 hingga py-32
```

Mobile:

```txt
py-16 hingga py-20
```

Gunakan whitespace luas.

Jangan menjejalkan banyak informasi dalam satu viewport.

---

## 5.3 Border Radius

Global radius:

```txt
small   : 12px
medium  : 20px
large   : 28px
hero    : 32px
pill    : 999px
```

Tailwind:

```txt
rounded-xl
rounded-2xl
rounded-3xl
```

---

# 6. Page Structure

Urutan halaman yang direkomendasikan:

```txt
Navbar
Hero
Quick Highlights / Stats
Tentang SiberMu
Kemahasiswaan
Program & Organisasi Mahasiswa
Prestasi Mahasiswa
AIK
Kegiatan / Kajian
Student Stories
Layanan Mahasiswa
FAQ
Final CTA
Footer
```

Kedua tema lomba — **Kemahasiswaan** dan **AIK** — harus terasa saling terhubung, bukan menjadi dua website berbeda.

---

# 7. Navbar

## Tujuan

Navigasi harus ringan, modern, dan tidak terlalu banyak item.

### Struktur

```txt
Logo SiberMu

Tentang
Kemahasiswaan
AIK
Prestasi
Layanan
FAQ

[ Jelajahi SiberMu ]
```

Desktop:

```txt
h-20
```

Navbar dapat menggunakan:

```txt
bg-white/80
backdrop-blur-xl
sticky top-0
z-50
border-b border-black/5
```

CTA kanan menggunakan button pill.

---

# 8. Hero Section

Hero menjadi area visual terkuat.

## 8.1 Layout

Gunakan hero image besar dengan rasio landscape.

```txt
min-height desktop: 620–720px
border-radius: 28–32px
```

Di atas image:

- logo kecil / eyebrow
- headline
- deskripsi singkat
- CTA
- small metadata

Contoh copy:

```txt
SIBERMU · KAMPUS DIGITAL MUHAMMADIYAH

Belajar tanpa batas.
Bertumbuh bersama.
Berdampak untuk umat.
```

Deskripsi:

```txt
Ruang belajar digital untuk mahasiswa yang ingin berkembang,
berkarya, dan membawa nilai Islam berkemajuan ke masa depan.
```

CTA:

```txt
Jelajahi Kehidupan Mahasiswa →
```

Secondary CTA:

```txt
Kenali SiberMu
```

---

## 8.2 Hero Image Treatment

Image menggunakan foto mahasiswa / suasana pembelajaran.

Tambahkan:

```css
linear-gradient(
  180deg,
  rgba(0,0,0,0.05),
  rgba(0,0,0,0.60)
)
```

Tujuan:

- teks tetap readable
- foto tetap terlihat
- hero terasa premium

---

## 8.3 Decorative Typography

Terinspirasi dari referensi:

```txt
SIBERMU
```

dapat ditempatkan sebagai large background typography.

Contoh:

```txt
text-[160px]
font-extrabold
tracking-[-0.06em]
text-white/20
```

Jangan terlalu dominan pada mobile.

---

# 9. Highlight Banner

Setelah hero, gunakan banner horizontal.

Contoh isi:

```txt
Kuliah fleksibel.
Komunitas aktif.
Nilai yang berdampak.
```

Layout:

```txt
grid-cols-12
```

Kiri:

```txt
col-span-5
```

Kanan:

```txt
col-span-7
```

Background:

```txt
bg-primary-600
```

Tambahkan abstract cyan curve atau Islamic geometric ornament.

---

# 10. About SiberMu

Section berupa editorial layout.

Kiri:

```txt
small badge:
TENTANG SIBERMU
```

Kanan:

headline besar:

```txt
Kampus digital yang
mendekatkan ilmu,
komunitas, dan nilai.
```

Tambahkan 3–4 statistik.

Contoh:

```txt
100%
Pembelajaran Digital

25+
Komunitas & Kegiatan

Indonesia
Belajar dari mana saja

AIK
Nilai Islam Berkemajuan
```

Stats menggunakan card asimetris.

---

# 11. Kemahasiswaan Section

Bagian ini menjadi salah satu section utama.

Eyebrow:

```txt
KEMAHASISWAAN
```

Heading:

```txt
Ruang untuk tumbuh
di luar kelas.
```

Deskripsi:

```txt
Temukan organisasi, komunitas, kegiatan, serta layanan
yang membantu mahasiswa berkembang secara akademik dan personal.
```

---

# 12. Student Activity Cards

Gunakan tiga kategori besar.

### Card 1

```txt
Organisasi Mahasiswa
```

### Card 2

```txt
Unit Kegiatan Mahasiswa
```

### Card 3

```txt
Komunitas & Kolaborasi
```

Layout desktop:

```txt
grid-cols-3
```

Card:

```txt
min-h-[360px]
rounded-3xl
overflow-hidden
relative
```

Gunakan foto pada bagian bawah card seperti referensi.

Card pertama bisa menggunakan primary blue agar ada visual anchor.

---

# 13. Program / Student Path Section

Terinspirasi dari layout "Find your path forward".

Section diletakkan di atas background foto kampus / aktivitas.

Di tengah:

```txt
white floating container
rounded-[28px]
shadow-xl
```

Isi berupa daftar.

Contoh:

```txt
Organisasi Mahasiswa
Bangun kepemimpinan dan pengalaman berorganisasi.

Unit Kegiatan Mahasiswa
Kembangkan minat dan bakat bersama komunitas.

Prestasi Mahasiswa
Kenali karya dan capaian mahasiswa SiberMu.
```

Setiap row:

```txt
grid grid-cols-[1.4fr_1fr_120px]
```

Mobile:

```txt
grid-cols-1
```

---

# 14. Prestasi Mahasiswa

Gunakan asymmetric card layout.

Headline:

```txt
Dari ruang digital,
lahir karya yang nyata.
```

Card dapat menampilkan:

- kompetisi
- akademik
- inovasi
- pengabdian
- karya kreatif

Layout:

```txt
grid-cols-12
```

Contoh:

```txt
featured card: col-span-7
small card: col-span-5
```

Tambahkan metadata:

```txt
Nama mahasiswa
Kategori
Tahun
```

---

# 15. AIK Section

AIK harus tampil modern, tidak seperti layout artikel biasa.

Eyebrow:

```txt
AL-ISLAM & KEMUHAMMADIYAHAN
```

Headline:

```txt
Ilmu yang tumbuh
bersama nilai.
```

Copy:

```txt
SiberMu menghadirkan ruang belajar yang menghubungkan
pengetahuan, spiritualitas, dan semangat Islam berkemajuan.
```

---

## 15.1 AIK Visual Style

Gunakan kombinasi:

```txt
white
dark navy
soft green
primary blue
```

Tambahkan pattern geometris Islami sangat subtle.

Opacity:

```txt
3–8%
```

Jangan menggunakan pattern terlalu ramai.

---

# 16. AIK Cards

Tiga card:

```txt
Kajian & Diskusi
Ruang refleksi dan pembelajaran keislaman.

Syiar Digital
Menyebarkan nilai Islam melalui media dan teknologi.

Islam Berkemajuan
Nilai yang mendorong ilmu, kemajuan, dan kebermanfaatan.
```

Card gunakan icon line sederhana.

Icon container:

```txt
size-12
rounded-full
bg-aik-soft
text-aik
```

---

# 17. Student Stories

Mengikuti inspirasi referensi testimonial cards.

Heading center:

```txt
Cerita mereka,
bagian dari perjalanan kita.
```

Gunakan 3 card.

Card pertama:

```txt
bg-primary-600
text-white
```

Card lainnya:

```txt
bg-[#F7F8FA]
```

Setiap card:

```txt
min-height: 400px
```

Isi:

```txt
avatar/icon
nama
program studi
quote
foto mahasiswa
```

Foto mahasiswa dapat overlapping ke bawah.

---

# 18. Layanan Mahasiswa

Section layanan menggunakan card modular.

Contoh:

```txt
Akademik
Beasiswa
Konseling
Administrasi
Karier
Bantuan Teknis
```

Layout:

```txt
grid-cols-2 md:grid-cols-3
```

Card:

```txt
p-6
rounded-2xl
border
hover:-translate-y-1
transition-all
```

---

# 19. FAQ

Section sederhana.

Heading:

```txt
Masih penasaran?
Kami punya jawabannya.
```

Gunakan accordion.

Pertanyaan contoh:

```txt
Bagaimana sistem perkuliahan di SiberMu?
Apa saja kegiatan mahasiswa yang tersedia?
Bagaimana cara bergabung dengan organisasi mahasiswa?
Apakah mahasiswa dapat mengikuti kegiatan AIK secara daring?
Apa saja layanan pendukung mahasiswa?
```

Accordion menggunakan Vue state lokal.

---

# 20. Final CTA

Gunakan full-width card sebelum footer.

Background:

```txt
primary blue
```

Heading:

```txt
Perjalananmu
dimulai dari sini.
```

Subheading:

```txt
Belajar. Bertumbuh. Berkarya.
Bersama SiberMu.
```

CTA:

```txt
Kenali SiberMu →
```

Tambahkan dua visual mahasiswa di sisi kanan.

---

# 21. Footer

Footer menggunakan dark navy.

```txt
bg-[#030617]
text-white
```

Layout:

```txt
logo + intro
social
menu columns
copyright
```

Menu:

```txt
Kemahasiswaan
AIK
Kegiatan
Prestasi
Layanan
Tentang
Kontak
```

Tambahkan baris kredit sumber media karena diwajibkan dalam ketentuan lomba.

Contoh:

```txt
Kredit Media
Foto dan ikon yang digunakan pada halaman ini berasal dari ...
```

---

# 22. Component Architecture

Struktur Vue:

```txt
src/
├── assets/
│   ├── images/
│   ├── icons/
│   └── patterns/
│
├── components/
│   ├── layout/
│   │   ├── AppNavbar.vue
│   │   ├── AppFooter.vue
│   │   └── SectionContainer.vue
│   │
│   ├── common/
│   │   ├── AppButton.vue
│   │   ├── SectionBadge.vue
│   │   ├── SectionHeading.vue
│   │   ├── StatCard.vue
│   │   └── MediaCredit.vue
│   │
│   ├── home/
│   │   ├── HeroSection.vue
│   │   ├── HighlightBanner.vue
│   │   ├── AboutSection.vue
│   │   ├── StudentLifeSection.vue
│   │   ├── StudentPathSection.vue
│   │   ├── AchievementSection.vue
│   │   ├── AikSection.vue
│   │   ├── StudentStories.vue
│   │   ├── StudentServices.vue
│   │   ├── FaqSection.vue
│   │   └── FinalCtaSection.vue
│
├── data/
│   ├── studentActivities.js
│   ├── achievements.js
│   ├── aikActivities.js
│   ├── testimonials.js
│   └── faq.js
│
├── views/
│   └── HomeView.vue
│
├── App.vue
└── main.js
```

---

# 23. Reusable Components

## AppButton

Variants:

```txt
primary
secondary
dark
ghost
```

Ukuran:

```txt
sm
md
lg
```

---

## SectionBadge

Style:

```txt
rounded-full
border
px-3
py-1
text-[11px]
font-semibold
uppercase
tracking-wide
```

---

## SectionHeading

Props:

```txt
eyebrow
title
description
alignment
```

---

# 24. Tailwind Utility Guidelines

Gunakan utility langsung untuk layout dasar.

Contoh:

```html
<section class="py-20 lg:py-28">
  <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
  </div>
</section>
```

Hindari custom CSS jika utility Tailwind sudah cukup.

Gunakan custom CSS hanya untuk:

- complex decorative shape
- mask
- gradient
- animation tertentu
- special typography effect

---

# 25. Responsive Design

Breakpoints utama:

```txt
sm  : 640px
md  : 768px
lg  : 1024px
xl  : 1280px
2xl : 1536px
```

Prioritas:

```txt
Mobile
Tablet
Desktop
Large Desktop
```

Pada mobile:

- navbar collapse
- headline lebih pendek
- CTA stack vertical
- card grid menjadi single column
- dekorasi besar disembunyikan
- foto tetap menjadi visual anchor

---

# 26. Motion & Interaction

Animasi harus subtle.

Gunakan:

```txt
duration-300
ease-out
```

Hover card:

```txt
translate-y-[-4px]
```

Image:

```txt
group-hover:scale-[1.03]
```

Button:

```txt
hover:translate-x-1
```

Scroll animation opsional:

```txt
fade-up
fade-in
```

Durasi maksimal:

```txt
400–700ms
```

Jangan menggunakan animasi berlebihan.

---

# 27. Accessibility

Target minimum:

```txt
WCAG AA
```

Pastikan:

- contrast cukup
- semua gambar memiliki `alt`
- tombol memiliki label jelas
- focus state tidak dihilangkan
- navigasi dapat digunakan keyboard
- accordion menggunakan `aria-expanded`
- heading memiliki hierarchy yang benar

---

# 28. Image Direction

Foto yang dipilih sebaiknya:

- mahasiswa Indonesia
- suasana belajar digital
- diskusi
- organisasi
- kegiatan sosial
- kegiatan keagamaan
- ekspresi natural
- pencahayaan hangat
- tidak terasa seperti stock photo generik

Crop:

```txt
object-cover
object-center
```

Untuk card portrait:

```txt
aspect-[4/5]
```

Hero:

```txt
aspect-[16/8]
```

---

# 29. Icon Style

Gunakan satu library konsisten.

Rekomendasi:

```txt
Lucide
```

Style:

```txt
stroke
1.5–2px
rounded
minimal
```

Hindari mencampur icon outline dan filled secara acak.

---

# 30. Content Style

Tone:

- ringkas
- human
- optimis
- akademik
- tidak terlalu formal
- bernuansa Islami tanpa berlebihan

Hindari:

```txt
"Website resmi kemahasiswaan..."
```

Lebih baik:

```txt
"Ruang untuk belajar, bertumbuh, dan memberi dampak."
```

---

# 31. Design Tokens

Contoh implementasi Tailwind / CSS:

```css
:root {
  --primary: #1268F3;
  --primary-dark: #0D4FC0;
  --cyan: #35E6ED;
  --aik: #0F9D72;

  --background: #FFFFFF;
  --surface: #F7F8FA;
  --text: #111827;
  --muted: #64748B;
  --border: #E5E7EB;

  --radius-sm: 12px;
  --radius-md: 20px;
  --radius-lg: 28px;
}
```

---

# 32. Recommended Vue Page Composition

```vue
<template>
  <AppNavbar />

  <main>
    <HeroSection />
    <HighlightBanner />
    <AboutSection />
    <StudentLifeSection />
    <StudentPathSection />
    <AchievementSection />
    <AikSection />
    <StudentStories />
    <StudentServices />
    <FaqSection />
    <FinalCtaSection />
  </main>

  <AppFooter />
</template>
```

---

# 33. Visual Hierarchy

Urutan prioritas visual:

```txt
1. Hero
2. Kemahasiswaan
3. AIK
4. Prestasi
5. Student Stories
6. Layanan
7. FAQ
8. CTA
```

Tidak semua section perlu memiliki visual weight yang sama.

Gunakan ritme:

```txt
BIG → calm → cards → BIG → calm → cards → CTA
```

agar scrolling terasa dinamis.

---

# 34. Originality Direction

Supaya karya tidak terasa seperti template kampus biasa, gunakan elemen khas SiberMu:

### Digital Grid

Grid kecil abstrak yang merepresentasikan:

```txt
network
digital learning
connectivity
```

### Islamic Geometry

Pattern geometris sederhana yang hanya muncul di bagian AIK.

### Muhammadiyah Blue

Blue tetap menjadi warna dominan identitas.

### Human Cutout

Foto mahasiswa dapat dibuat cutout pada beberapa section untuk memberi visual depth.

### Editorial Copy

Gunakan headline pendek dan kuat.

Contoh:

```txt
Belajar dari mana saja.
Berdampak di mana saja.
```

---

# 35. Performance Guidelines

Target:

```txt
Lighthouse Performance >= 90
Accessibility >= 90
Best Practices >= 90
SEO >= 90
```

Optimasi:

- gunakan WebP / AVIF
- lazy load image non-hero
- ukuran hero image maksimal sekitar 300–500 KB
- hindari library animasi besar jika tidak perlu
- gunakan SVG untuk icon
- preload font utama
- maksimal 2 font family
- hindari layout shift

---

# 36. SEO

Landing page harus memiliki:

```html
<title>Mahasiswa SiberMu — Belajar, Berkarya, Berdampak</title>

<meta
  name="description"
  content="Kenali kehidupan mahasiswa, organisasi, prestasi, layanan, serta Al-Islam dan Kemuhammadiyahan di Universitas Siber Muhammadiyah."
/>
```

Tambahkan:

```txt
Open Graph
Twitter Card
canonical
favicon
```

---

# 37. Suggested Home Copy

## Hero

```txt
Belajar tanpa batas.
Bertumbuh bersama.
Berdampak untuk umat.
```

## Kemahasiswaan

```txt
Lebih dari sekadar kuliah.

Temukan komunitas, organisasi, kegiatan,
dan ruang tumbuh yang membuat perjalanan
kuliah lebih bermakna.
```

## AIK

```txt
Ilmu yang tumbuh bersama nilai.

Al-Islam dan Kemuhammadiyahan menjadi bagian
dari perjalanan mahasiswa untuk membangun
karakter, wawasan, dan kebermanfaatan.
```

## Prestasi

```txt
Dari ruang digital,
lahir karya yang nyata.
```

## Student Story

```txt
Cerita mereka,
bagian dari perjalanan kita.
```

## Final CTA

```txt
Perjalananmu
dimulai dari sini.

Belajar. Bertumbuh. Berkarya.
Bersama SiberMu.
```

---

# 38. Do & Don't

## Do

- gunakan whitespace
- gunakan typography besar
- gunakan foto manusia sebagai visual utama
- gunakan card modular
- jaga konsistensi radius
- tampilkan AIK dan kemahasiswaan sebagai satu cerita
- prioritaskan mobile
- gunakan copy singkat
- cantumkan kredit media

## Don't

- terlalu banyak gradient
- terlalu banyak warna
- terlalu banyak icon
- memakai carousel untuk semua section
- memakai ilustrasi berbeda style
- membuat layout terlalu padat
- membuat AIK terasa sebagai halaman terpisah
- memakai animasi berlebihan
- menyalin referensi 1:1

---

# 39. Final Design Principle

Landing page harus memberikan impresi:

> **SiberMu adalah kampus digital yang modern, aktif, dekat dengan mahasiswa, dan tetap berakar pada nilai Islam Berkemajuan.**

Secara visual, halaman harus terasa seperti kombinasi antara:

```txt
Modern University
+
Digital Product
+
Student Community
+
Islamic Values
```

Bukan sekadar company profile universitas.

---

# 40. Reference Implementation Notes

Untuk Vue + Vite + Tailwind CSS:

```txt
Vue
├── component-based
├── data-driven sections
├── semantic HTML
└── minimal JS

Tailwind
├── responsive layout
├── spacing system
├── typography
├── colors
└── interaction states
```

Gunakan data statis pada `/src/data` supaya konten mudah diganti tanpa menyentuh struktur komponen.

Contoh:

```js
export const studentActivities = [
  {
    title: 'Organisasi Mahasiswa',
    description: 'Belajar memimpin, berkolaborasi, dan membangun jejaring.',
    image: '/images/student-organization.webp',
  },
]
```

Dengan pola tersebut, desain tetap clean dan implementasi mudah dikembangkan.
