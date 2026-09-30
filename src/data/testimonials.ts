export interface Testimonial {
  name: string
  program: string
  quote: string
  tone: 'primary' | 'light'
}

export const testimonials: Testimonial[] = [
  {
    name: 'Muammar',
    program: 'Mahasiswa Prodi Sistem Informasi',
    quote:
      'Saya datang untuk belajar. Ternyata saya juga menemukan komunitas yang membuat perjalanan kuliah terasa lebih berarti.',
    tone: 'primary',
  },
  {
    name: 'Falih Ananta',
    program: 'Mahasiswa Prodi Sistem Informasi',
    quote:
      'Belajar secara daring tidak membuat saya merasa sendirian. Ada banyak ruang untuk bertemu, berdiskusi, dan berkembang bersama.',
    tone: 'light',
  },
  {
    name: 'Nur Arifin',
    program: 'Mahasiswa Prodi Hukum',
    quote:
      'Bagi saya, kuliah bukan hanya tentang nilai akademik. Saya belajar untuk lebih percaya diri, aktif, dan berani mencoba hal baru.',
    tone: 'light',
  },
]
