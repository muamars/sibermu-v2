export interface FilmScene {
  eyebrow: string
  title: string
  body: string
  position: 'center' | 'left' | 'right'
  variant?: 'hero' | 'cta'
}

export const filmScenes: FilmScene[] = [
  {
    eyebrow: 'Kampus Digital Islam Berkemajuan',
    title: 'Tumbuh bersama Sibermu.',
    body: 'SiberMu bukan hanya ruang untuk kuliah. Di sini, mahasiswa belajar, membangun relasi, dan tumbuh bersama nilai Islam Berkemajuan.',
    position: 'center',
    variant: 'hero',
  },
  {
    eyebrow: 'Est. 2021',
    title: 'Masuki Ruang Belajar',
    body: 'Tanpa ruang kelas fisik, tanpa jarak yang membatasi. Kampus virtual SiberMu hadir lewat teknologi digital yang terbimbing dan fleksibel.',
    position: 'left',
  },
  {
    eyebrow: 'Kemahasiswaan',
    title: 'Ruang untuk Bertumbuh',
    body: 'Organisasi otonom, unit kegiatan mahasiswa, dan komunitas lintas wilayah — semua terbuka untuk siapa saja yang ingin mencoba hal baru.',
    position: 'right',
  },
  {
    eyebrow: 'Al-Islam & Kemuhammadiyahan',
    title: 'Ilmu yang Tumbuh Bersama Nilai',
    body: 'Kajian rutin, Baitul Arqam daring, dan syiar digital menjadi bagian dari perjalanan membentuk karakter dan wawasan keislaman.',
    position: 'left',
  },
  {
    eyebrow: 'Prestasi Mahasiswa',
    title: 'Dari Ruang Digital, Lahir Karya Nyata',
    body: 'Medali internasional, publikasi jurnal terakreditasi, hingga wisuda cumlaude. Jarak bukan penghalang untuk terus berprestasi.',
    position: 'right',
  },
  {
    eyebrow: 'Komunitas',
    title: 'Lebih dari Sekadar Kuliah',
    body: 'Mahasiswa datang dengan latar dan tujuan yang berbeda, namun semuanya memiliki ruang yang sama untuk terhubung dan bertumbuh.',
    position: 'left',
  },
  {
    eyebrow: 'Perjalananmu Menunggu',
    title: 'Mulai Langkahmu di SiberMu',
    body: 'Belajar. Bertumbuh. Berkarya. Bersama SiberMu.',
    position: 'center',
    variant: 'cta',
  },
]
