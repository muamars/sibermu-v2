# Landing Page SiberMu 2026

Dokumentasi karya Tim Dinas Lingkungan Hidup Provinsi DKI Jakarta untuk **Lomba Pembuatan Landing Page SiberMu 2026** yang diselenggarakan oleh Universitas Siber Muhammadiyah.

## Tim

- Muammar
- Falih Ananta
- Nur Arifin

## Tentang Karya

Karya ini berupa landing page satu halaman yang memperkenalkan kehidupan kemahasiswaan dan Al-Islam dan Kemuhammadiyahan (AIK) SiberMu dalam satu pengalaman yang utuh. Halaman dirancang agar calon mahasiswa dapat melihat ruang untuk belajar, berorganisasi, berprestasi, mengembangkan diri, dan bertumbuh dengan nilai Islam Berkemajuan.

Konsep visualnya menggabungkan suasana universitas digital yang modern dengan pendekatan yang hangat dan berpusat pada mahasiswa. Warna biru mengambil inspirasi dari identitas SiberMu, sementara aksen visual AIK diintegrasikan ke dalam bahasa desain yang sama.

## Isi dan Fitur

- **Hero dan pengenalan SiberMu** untuk memperkenalkan pengalaman belajar digital.
- **Kemahasiswaan** yang mencakup organisasi, UKM, prestasi, dan layanan mahasiswa.
- **Detail Kemahasiswaan** yang merangkum komunitas, kegiatan ilmiah, minat bakat, serta program internasional mahasiswa.
- **AIK** yang menampilkan kegiatan keagamaan, kajian, syiar, serta nilai Kemuhammadiyahan.
- **Delapan nilai utama Kemuhammadiyahan** sebagai dasar pembentukan karakter dan kontribusi sosial.
- **Hall of Fame** untuk menampilkan prestasi dan penerimanya dalam urutan tahun.
- **Layanan mahasiswa**, **cerita mahasiswa**, FAQ, dan ajakan mengenal SiberMu lebih lanjut.
- **Chatbot Aisa** yang mengirim pesan langsung ke webhook informasi SiberMu.
- Tata letak responsif untuk ponsel dan desktop, dengan dukungan pengurangan animasi.

## Referensi Konten dan Desain

- Cakupan tema dan ketentuan lomba mengacu pada [Panduan Lomba Landing Page SiberMu 2026](docs/Panduan_Lomba_Landing_Page_SiberMu_2026.md).
- Fakta institusi dan informasi akademik merujuk pada situs resmi [sibermu.ac.id](https://sibermu.ac.id/) dan salinan materi yang dihimpun di folder [`sibermu-data`](sibermu-data/README.md). Salinan tersebut merupakan snapshot bertanggal 11 September 2026; situs resmi tetap menjadi rujukan terbaru.
- Arah desain dan struktur halaman dijelaskan lebih lanjut di [`docs/DESIGN.md`](docs/DESIGN.md) dan [`docs/LANDING-PAGE-STRUCTURE.md`](docs/LANDING-PAGE-STRUCTURE.md).
- Screenshot referensi layout yang dibagikan selama proses desain digunakan sebagai inspirasi tata letak. Implementasi halaman disusun ulang untuk identitas SiberMu dan bukan file gambar yang ditampilkan sebagai konten situs.

## Kredit Media dan Aset

Ketentuan lomba meminta sumber gambar, ikon, huruf, dan media lain dicantumkan. Berikut sumber yang dapat diidentifikasi dari proyek:

| Media | Lokasi/penggunaan | Sumber yang tercatat |
|---|---|---|
| Logo SiberMu dan logo program studi | `src/assets/sibermu-logo.png`, `src/assets/sibermu-white.png`, `src/assets/prodi/` | Berkas identitas yang tersedia di proyek. URL asal dan keterangan lisensi belum tercatat; konfirmasikan kepada pemilik identitas SiberMu. |
| Foto mahasiswa belajar | `src/assets/student.png` | Instagram [SiberMu](https://www.instagram.com/sibermu/). Tautan posting spesifik belum dicatat. |
| Foto dan visual mahasiswa/kampus lainnya | `src/assets/scene*.webp`, `src/assets/kajian.webp`, `src/assets/mulai.webp`, `src/assets/kampus-virtual.webp`, `src/assets/winner/` | Aset lokal yang digunakan pada halaman. Informasi fotografer, URL publikasi, dan lisensi sumber aslinya belum tercatat di repositori; lengkapi kredit setelah diverifikasi. |
| Ikon antarmuka | Komponen Vue | Lucide — [lucide.dev](https://lucide.dev/), paket `@lucide/vue`. |
| Font | `src/style.css` | Google Fonts: [Geist](https://fonts.google.com/specimen/Geist), [Inter Tight](https://fonts.google.com/specimen/Inter+Tight), dan [TASA Explorer](https://fonts.google.com/specimen/TASA+Explorer). |

Screenshot referensi yang dibagikan untuk arahan visual berasal dari materi referensi desain selama pengerjaan. Screenshot tersebut tidak menjadi aset gambar halaman. **Asal dan izin penggunaan aset foto lokal belum dapat diverifikasi dari metadata proyek**, sehingga sumber/pemilik dan izin publikasinya perlu dipastikan sebelum pengumpulan lomba. Jangan mencantumkan Unsplash atau sumber lain tanpa verifikasi.

> Catatan editorial: nama pada testimoni saat ini adalah nama contoh, bukan konfirmasi identitas mahasiswa. Ganti dengan testimoni nyata beserta izin publikasi, atau gunakan label anonim sebelum karya dipublikasikan.

## Teknologi

- Vue 3 dan TypeScript
- Vite
- Tailwind CSS 4
- Lucide Vue untuk ikon

## Menjalankan Proyek

Pasang dependensi:

```sh
npm install
```

Jalankan server pengembangan:

```sh
npm run dev
```

Buat build production:

```sh
npm run build
```
