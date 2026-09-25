export interface Testimonial {
  name: string
  program: string
  quote: string
  tone: 'primary' | 'light'
}

export const testimonials: Testimonial[] = [
  {
    name: 'Mahasiswa Prodi Informatika',
    program: 'Angkatan 2024',
    quote:
      'Saya datang untuk belajar. Ternyata saya juga menemukan komunitas yang membuat perjalanan kuliah terasa lebih berarti.',
    tone: 'primary',
  },
  {
    name: 'Mahasiswa Prodi Sistem Informasi',
    program: 'Angkatan 2023',
    quote:
      'Belajar secara daring tidak membuat saya merasa sendirian. Ada banyak ruang untuk bertemu, berdiskusi, dan berkembang bersama.',
    tone: 'light',
  },
  {
    name: 'Mahasiswa Prodi Hukum',
    program: 'Angkatan 2023',
    quote:
      'Bagi saya, kuliah bukan hanya tentang nilai akademik. Saya belajar untuk lebih percaya diri, aktif, dan berani mencoba hal baru.',
    tone: 'light',
  },
]
