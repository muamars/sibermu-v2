export interface Achievement {
  title: string
  description: string
  category: string
  year?: string
  featured?: boolean
}

export const achievements: Achievement[] = [
  {
    title: 'Bronze Medal & Best Presenter Award',
    description:
      'Meraih medali perunggu sekaligus penghargaan presentasi terbaik pada ajang internasional Global Leadership for Sustainable Economy and Well-Being: Idea Presentation.',
    category: 'Kompetisi Internasional',
    year: '2025',
    featured: true,
  },
  {
    title: 'Juara 2 Lomba Esai Ilmiah Nasional',
    description:
      'Tim mahasiswa meraih Juara 2 pada Medical Scientific Competition and Award of UIN Malang (MIDBRAIN) melalui gagasan ilmiah mereka.',
    category: 'Akademik · Nasional',
  },
  {
    title: 'Publikasi Jurnal Terakreditasi SINTA',
    description:
      'Tugas akhir mahasiswa S1 PJJ Hukum berhasil dikonversi menjadi artikel ilmiah yang terbit di jurnal nasional terakreditasi SINTA 3.',
    category: 'Riset & Publikasi',
  },
  {
    title: 'Wisuda Perdana dengan Predikat Cumlaude',
    description:
      'Angkatan pertama lulusan SiberMu mempertahankan tradisi keunggulan akademik dengan IPK yang memuaskan dan predikat pujian.',
    category: 'Akademik',
  },
  {
    title: 'Juara 2 Ajang Literasi Nasional',
    description:
      'Melewati seleksi ketat mulai dari pembuatan video profil hingga wawancara, mahasiswa SiberMu meraih posisi ke-2 tingkat nasional.',
    category: 'Non-Akademik · Literasi',
  },
  {
    title: 'Pelopor Gerakan Digital Imersif',
    description:
      'Keterlibatan aktif mahasiswa dalam ekosistem kampus berbasis metaverse dan AI menjadikan mereka agen Islam Berkemajuan di era digital.',
    category: 'Kontribusi Digital',
  },
]
