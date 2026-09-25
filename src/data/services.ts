export interface ServiceItem {
  title: string
  description: string
  icon: 'GraduationCap' | 'Wallet' | 'MessageCircle' | 'ClipboardList' | 'Briefcase' | 'LifeBuoy'
}

export const services: ServiceItem[] = [
  {
    title: 'Layanan Akademik',
    description: 'LMS, SIM Akademik, dan kampus virtual untuk mendukung proses perkuliahanmu setiap hari.',
    icon: 'GraduationCap',
  },
  {
    title: 'Beasiswa',
    description: 'Temukan informasi peluang bantuan dan dukungan pendidikan dari kampus maupun mitra.',
    icon: 'Wallet',
  },
  {
    title: 'Konseling Mahasiswa',
    description: 'Ruang aman untuk berdiskusi dan mendapatkan dukungan melalui hotline tatap maya SiberMu Solusi.',
    icon: 'MessageCircle',
  },
  {
    title: 'Administrasi',
    description: 'Akses KRS, KHS, hingga status pembayaran kuliah dengan lebih mudah lewat SIM Akademik.',
    icon: 'ClipboardList',
  },
  {
    title: 'Pengembangan Karier',
    description: 'Persiapkan diri untuk langkah berikutnya lewat SiberMu Career dan program MBKM.',
    icon: 'Briefcase',
  },
  {
    title: 'Bantuan Teknis',
    description: 'Dukungan ketika kamu membutuhkan bantuan dalam layanan digital kampus, kapan pun dibutuhkan.',
    icon: 'LifeBuoy',
  },
]
