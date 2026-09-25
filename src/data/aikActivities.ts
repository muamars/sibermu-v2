export interface AikActivity {
  title: string
  description: string
  icon: 'BookOpen' | 'Radio' | 'Sparkles' | 'HandHeart'
}

export const aikActivities: AikActivity[] = [
  {
    title: 'Kajian & Diskusi',
    description:
      'Ruang untuk belajar, bertanya, dan memahami nilai Islam secara lebih dekat lewat kajian rutin virtual dan Baitul Arqam daring.',
    icon: 'BookOpen',
  },
  {
    title: 'Syiar Digital',
    description:
      'Membawa pesan kebaikan melalui MOOCs, konten dakwah kreatif, hingga kajian imersif berbasis Virtual Reality.',
    icon: 'Radio',
  },
  {
    title: 'Islam Berkemajuan',
    description:
      'Menjadikan ilmu, teknologi, dan kepedulian sosial sebagai ikhtiar membangun masa depan yang lebih baik, sesuai manhaj tarjih Muhammadiyah.',
    icon: 'Sparkles',
  },
  {
    title: 'Dari Nilai Menjadi Aksi',
    description:
      'Karena nilai tidak berhenti pada kata-kata. Ia tumbuh lewat KKN Jarak Jauh, aksi solidaritas kemanusiaan, dan dakwah Al-Ma\'un.',
    icon: 'HandHeart',
  },
]
