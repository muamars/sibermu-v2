export interface StudentActivity {
  title: string
  description: string
  cta: string
  tone: 'primary' | 'light' | 'dark'
  imageHint: string
}

export const studentActivities: StudentActivity[] = [
  {
    title: 'Organisasi Mahasiswa',
    description:
      'Belajar memimpin, bekerja dalam tim, dan mengubah ide menjadi gerakan yang nyata bersama IMM, Hizbul Wathan, dan Tapak Suci.',
    cta: 'Jelajahi Organisasi',
    tone: 'primary',
    imageHint: 'Diskusi organisasi mahasiswa',
  },
  {
    title: 'Unit Kegiatan Mahasiswa',
    description:
      'Temukan ruang untuk mengembangkan minat, bakat, dan kreativitas lewat UKM Bisnis Digital, English Club, hingga Konten Kreatif.',
    cta: 'Lihat Kegiatan',
    tone: 'light',
    imageHint: 'Aktivitas unit kegiatan mahasiswa',
  },
  {
    title: 'Komunitas & Kolaborasi',
    description:
      'Karena belajar tidak harus selalu sendirian. Bangun koneksi dan tumbuh bersama mahasiswa dari berbagai daerah lewat kelompok belajar wilayah.',
    cta: 'Temukan Komunitas',
    tone: 'dark',
    imageHint: 'Kolaborasi mahasiswa lintas wilayah',
  },
]
