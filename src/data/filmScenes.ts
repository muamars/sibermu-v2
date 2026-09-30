export interface FilmScene {
  eyebrow: string
  title: string
  titleAccent?: string
  body: string
  position: 'center' | 'left' | 'right'
  variant?: 'hero' | 'cta'
}

export const filmScenes: FilmScene[] = [
  {
    eyebrow: 'Kemahasiswaan',
    title: 'Ruang untuk Bertumbuh',
    titleAccent: 'Bertumbuh',
    body: 'Organisasi otonom, unit kegiatan mahasiswa, dan komunitas lintas wilayah — semua terbuka untuk siapa saja yang ingin mencoba hal baru.',
    position: 'right',
  },
  {
    eyebrow: 'Al-Islam & Kemuhammadiyahan',
    title: 'Ilmu yang Tumbuh Bersama Nilai',
    titleAccent: 'Bersama Nilai',
    body: 'Kajian rutin, Baitul Arqam daring, dan syiar digital menjadi bagian dari perjalanan membentuk karakter dan wawasan keislaman.',
    position: 'left',
  },
  {
    eyebrow: 'Prestasi Mahasiswa',
    title: 'Dari Ruang Digital, Lahir Karya Nyata',
    titleAccent: 'Lahir Karya Nyata',
    body: 'Medali internasional, publikasi jurnal terakreditasi, hingga wisuda cumlaude. Jarak bukan penghalang untuk terus berprestasi.',
    position: 'right',
  },
  {
    eyebrow: 'Komunitas',
    title: 'Lebih dari Sekadar Kuliah',
    titleAccent: 'Sekadar Kuliah',
    body: 'Mahasiswa datang dengan latar dan tujuan yang berbeda, namun semuanya memiliki ruang yang sama untuk terhubung dan bertumbuh.',
    position: 'left',
  },
]
