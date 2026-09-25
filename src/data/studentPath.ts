export interface StudentPathItem {
  title: string
  description: string
  imageHint: string
}

export const studentPath: StudentPathItem[] = [
  {
    title: 'Berorganisasi',
    description: 'Bangun kepemimpinan, pengalaman, dan relasi lewat organisasi otonom serta unit kegiatan mahasiswa.',
    imageHint: 'Mahasiswa rapat organisasi',
  },
  {
    title: 'Berkarya',
    description: 'Kembangkan ide menjadi sesuatu yang bisa dibanggakan, dari riset ilmiah hingga konten digital.',
    imageHint: 'Mahasiswa mengerjakan proyek',
  },
  {
    title: 'Berkolaborasi',
    description: 'Temukan teman belajar dan komunitas yang sejalan meski terpisah jarak dan waktu.',
    imageHint: 'Diskusi kelompok belajar wilayah',
  },
  {
    title: 'Memberi Dampak',
    description: 'Gunakan ilmu dan pengalaman untuk memberi manfaat bagi sekitar melalui pengabdian masyarakat.',
    imageHint: 'Kegiatan pengabdian masyarakat',
  },
]
