import winner2Photo from '@/assets/winner/winner2.webp'
import winner1Photo from '@/assets/winner/winner1.webp'

export interface Achievement {
  title: string
  description: string
  category: string
  recipients?: string[]
  photo?: string
  year?: string
  featured?: boolean
}

export const achievements: Achievement[] = [
  {
    title: 'Bronze Medal & Best Presenter Award',
    description:
      'Meraih medali perunggu sekaligus penghargaan presentasi terbaik pada ajang internasional Global Leadership for Sustainable Economy and Well-Being: Idea Presentation.',
    category: 'Kompetisi Internasional',
    recipients: ['Hilmawan Arief Mufatichien', 'Nur Khanifah Rahmawati'],
    photo: winner1Photo,
    year: '2025',
    featured: true,
  },
  {
    title: 'Medali Emas (Juara 1) KOSPRESIA 2025',
    description:
      'Olimpiade Sains bidang Biologi tingkat Nasional pada ajang Kompetisi Sains Prestasi Siswa Indonesia (KOSPRESIA)',
    category: 'Akademik · Nasional',
    recipients: ['Nabila Syafira'],
    year: '2025',
    photo: winner2Photo,
  },
  {
    title: 'Juara 2 Lomba Esai Ilmiah Nasional',
    description:
      'Tim mahasiswa meraih Juara 2 pada Medical Scientific Competition and Award of UIN Malang (MIDBRAIN) melalui gagasan ilmiah mereka.',
    category: 'Akademik · Nasional',
    recipients: ['NADA PRATIWI'],
    year: '2023',
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
    recipients: ['Nurseni Yulianti'],
    year: '2024',
  },
  {
    title: 'Pelopor Gerakan Digital Imersif',
    description:
      'Keterlibatan aktif mahasiswa dalam ekosistem kampus berbasis metaverse dan AI menjadikan mereka agen Islam Berkemajuan di era digital.',
    category: 'Kontribusi Digital',
    recipients: ['Dr. Bambang Riyanta, S.T., M.T.', 'Prof. Dr. K.H. Haedar Nashir, M.Si.'],
  },
]
