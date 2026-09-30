from pathlib import Path
import textwrap

PAGE_W, PAGE_H = 595, 842
NAVY = (0.035, 0.145, 0.235)
BLUE = (0.03, 0.48, 0.62)
CYAN = (0.03, 0.62, 0.76)
INK = (0.08, 0.16, 0.22)
MUTED = (0.34, 0.41, 0.46)
PALE = (0.95, 0.97, 0.98)
LINE = (0.84, 0.89, 0.92)
WHITE = (1, 1, 1)


def color(c):
    return ' '.join(f'{v:.3f}' for v in c)


def safe(s):
    replacements = {
        '\u2018': "'", '\u2019': "'", '\u201c': '"', '\u201d': '"',
        '\u2013': '-', '\u2014': '-', '\u2022': '-', '\u00a0': ' ',
        '\u00e2': 'a', '\u00e9': 'e', '\u00ed': 'i', '\u00f3': 'o',
        '\u00fa': 'u', '\u00c2': 'A', '\u00c9': 'E', '\u00d3': 'O',
    }
    for old, new in replacements.items():
        s = s.replace(old, new)
    return s.encode('cp1252', errors='replace').decode('cp1252')


class Page:
    def __init__(self, dark=False):
        self.ops = []
        self.dark = dark
        if dark:
            self.rect(0, 0, PAGE_W, PAGE_H, NAVY)

    def rect(self, x, y, w, h, fill, stroke=None, radius=0):
        self.ops.append('q')
        self.ops.append(f'{color(fill)} rg')
        if stroke:
            self.ops.append(f'{color(stroke)} RG 0.8 w')
        yy = PAGE_H - y - h
        if radius:
            r = radius
            k = 0.55228475 * r
            path = [
                f'{x+r:.2f} {yy:.2f} m', f'{x+w-r:.2f} {yy:.2f} l',
                f'{x+w-r+k:.2f} {yy:.2f} {x+w:.2f} {yy+r-k:.2f} {x+w:.2f} {yy+r:.2f} c',
                f'{x+w:.2f} {yy+h-r:.2f} l',
                f'{x+w:.2f} {yy+h-r+k:.2f} {x+w-r+k:.2f} {yy+h:.2f} {x+w-r:.2f} {yy+h:.2f} c',
                f'{x+r:.2f} {yy+h:.2f} l',
                f'{x+r-k:.2f} {yy+h:.2f} {x:.2f} {yy+h-r+k:.2f} {x:.2f} {yy+h-r:.2f} c',
                f'{x:.2f} {yy+r:.2f} l',
                f'{x:.2f} {yy+r-k:.2f} {x+r-k:.2f} {yy:.2f} {x+r:.2f} {yy:.2f} c',
                'h', 'B' if stroke else 'f',
            ]
            self.ops.extend(path)
        else:
            self.ops.append(f'{x:.2f} {yy:.2f} {w:.2f} {h:.2f} re')
            self.ops.append('B' if stroke else 'f')
        self.ops.append('Q')

    def line(self, x1, y1, x2, y2, stroke=LINE, width=0.8):
        self.ops.extend(['q', f'{color(stroke)} RG {width:.2f} w', f'{x1:.2f} {PAGE_H-y1:.2f} m {x2:.2f} {PAGE_H-y2:.2f} l S', 'Q'])

    def text(self, x, y, value, size=11, fill=INK, bold=False, oblique=False):
        value = safe(value).replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')
        font = 'F2' if bold else ('F3' if oblique else 'F1')
        self.ops.extend(['q', f'{color(fill)} rg', f'BT /{font} {size:.2f} Tf 1 0 0 1 {x:.2f} {PAGE_H-y:.2f} Tm ({value}) Tj ET', 'Q'])

    def para(self, x, y, value, width, size=10.2, fill=MUTED, leading=None, bold=False):
        leading = leading or size * 1.43
        max_chars = max(12, int(width / (size * (0.54 if bold else 0.50))))
        lines = []
        for paragraph in value.split('\n'):
            if not paragraph:
                lines.append('')
            else:
                lines.extend(textwrap.wrap(safe(paragraph), width=max_chars, break_long_words=False, break_on_hyphens=False) or [''])
        for i, row in enumerate(lines):
            self.text(x, y + i * leading, row, size, fill, bold)
        return y + len(lines) * leading

    def bullet(self, x, y, value, width, size=9.4, fill=INK, marker=BLUE, leading=None):
        leading = leading or size * 1.38
        self.rect(x, y - 7, 4, 4, marker, radius=2)
        end = self.para(x + 11, y, value, width - 11, size, fill, leading)
        return max(y + leading, end) + 4


def header(page, section, page_no):
    page.rect(0, 0, PAGE_W, 98, NAVY)
    page.rect(44, 21, 4, 42, CYAN, radius=2)
    page.text(58, 34, 'SIBERMU', 10, WHITE, True)
    page.text(58, 48, 'KEMAHASISWAAN  +  AIK', 6.5, (0.65, 0.82, 0.88), True)
    page.text(412, 34, 'DOKUMENTASI KARYA', 7, (0.76, 0.87, 0.91), True)
    page.text(58, 79, section, 21, WHITE, True)
    page.rect(518, 62, 33, 22, (0.10, 0.30, 0.40), radius=11)
    page.text(526, 77, f'{page_no:02d} / 04', 7, WHITE, True)
    page.line(44, 800, 551, 800)
    page.text(44, 819, 'TIM DINAS LINGKUNGAN HIDUP PROVINSI DKI JAKARTA', 7.5, MUTED, True)
    page.text(531, 819, f'{page_no:02d}', 8, BLUE, True)


def card(page, x, y, w, h, title, kicker=None):
    page.rect(x, y, w, h, WHITE, LINE, 12)
    start = y + 25
    if kicker:
        page.text(x + 18, start, kicker.upper(), 7.3, BLUE, True)
        start += 17
    page.text(x + 18, start, title, 13, NAVY, True)
    return start + 17


pages = []

# 1. Cover and executive summary
p = Page(dark=True)
p.rect(405, 34, 152, 4, CYAN, radius=2)
p.text(44, 58, 'DOKUMENTASI SINGKAT  /  LOMBA 2026', 8.5, (0.55, 0.83, 0.90), True)
p.text(44, 153, 'Ruang Bertumbuh,', 34, WHITE, True)
p.text(44, 198, 'Berkemajuan.', 34, (0.35, 0.82, 0.92), True)
p.para(46, 240, 'Landing page kemahasiswaan dan Al-Islam Kemuhammadiyahan Universitas Siber Muhammadiyah.', 420, 13, (0.88, 0.93, 0.96), 19)
p.rect(44, 330, 507, 1, (0.18, 0.34, 0.43))
p.text(44, 372, 'KARYA OLEH', 8, (0.55, 0.83, 0.90), True)
p.text(44, 400, 'Muammar  /  Falih Ananta  /  Nur Arifin', 14, WHITE, True)
p.para(44, 438, 'Dinas Lingkungan Hidup Provinsi DKI Jakarta', 430, 10.5, (0.79, 0.87, 0.91), 15)
p.rect(44, 510, 507, 186, (0.07, 0.21, 0.30), (0.19, 0.37, 0.47), 14)
p.text(66, 543, 'GAGASAN UTAMA', 8, (0.55, 0.83, 0.90), True)
p.para(66, 571, 'Satu halaman yang memperlihatkan bagaimana mahasiswa SiberMu dapat belajar, berorganisasi, berprestasi, dan bertumbuh dengan nilai Islam Berkemajuan.', 460, 13, WHITE, 19)
p.para(66, 647, 'Dirancang sebagai pengalaman digital yang informatif, responsif, dan dekat dengan calon mahasiswa.', 452, 9.5, (0.77, 0.86, 0.90), 14)
p.text(44, 772, 'UNIVERSITAS SIBER MUHAMMADIYAH  |  SEPTEMBER 2026', 8, (0.60, 0.76, 0.83), True)
pages.append(p)

# 2. Competition framing and design
p = Page()
header(p, 'Konteks dan Gagasan', 2)
p.para(44, 111, 'Lomba Pembuatan Landing Page SiberMu 2026 meminta satu halaman yang memuat Kemahasiswaan dan AIK secara terpadu. Karya ini menyatukan kedua tema dalam alur yang berangkat dari pengenalan kampus, pengalaman mahasiswa, kegiatan, nilai, hingga ajakan untuk mengenal SiberMu.', 500, 10.2, MUTED, 15)

y = card(p, 44, 196, 242, 158, 'Tujuan Karya', 'Arah komunikasi')
y = p.bullet(62, y + 9, 'Membantu calon mahasiswa memahami ruang belajar dan kegiatan di SiberMu.', 207, 9.2)
y = p.bullet(62, y, 'Menunjukkan hubungan antara pengalaman kemahasiswaan dan nilai AIK.', 207, 9.2)
y = p.bullet(62, y, 'Mengajak pengunjung menelusuri informasi melalui satu halaman.', 207, 9.2)

y = card(p, 303, 196, 248, 158, 'Audiens dan Pesan', 'Untuk calon mahasiswa')
y = p.para(321, y + 9, 'Audiens utama adalah calon mahasiswa dan pengunjung yang ingin mengenal kegiatan, layanan, serta karakter pembelajaran SiberMu.', 208, 9.2, MUTED, 13)
p.text(321, 323, 'Belajar. Bertumbuh. Memberi manfaat.', 8.3, BLUE, True)

p.text(44, 398, 'PRINSIP DESAIN', 8, BLUE, True)
p.text(44, 423, 'Modern, jelas, dan berpusat pada mahasiswa.', 16, NAVY, True)
principles = [
    ('01', 'Satu alur terpadu', 'Kemahasiswaan dan AIK hadir dalam narasi satu landing page.'),
    ('02', 'Hierarki yang mudah dipindai', 'Judul, kategori, dan kartu membantu pengunjung menemukan informasi.'),
    ('03', 'Visual SiberMu', 'Palet navy dan biru dipadukan dengan aksen yang menjaga keterbacaan.'),
    ('04', 'Lintas perangkat', 'Tata letak menyesuaikan layar ponsel dan desktop.'),
]
for i, (n, title, desc) in enumerate(principles):
    x = 44 + (i % 2) * 259
    y = 458 + (i // 2) * 126
    p.rect(x, y, 242, 106, PALE, LINE, 10)
    p.text(x + 15, y + 25, n, 8, BLUE, True)
    p.text(x + 44, y + 25, title, 10.5, NAVY, True)
    p.para(x + 15, y + 51, desc, 212, 8.6, MUTED, 12)
pages.append(p)

# 3. Information architecture and content
p = Page()
header(p, 'Isi dan Pengalaman Pengunjung', 3)
p.para(44, 111, 'Landing page disusun bertahap: pengenalan SiberMu, gambaran kehidupan mahasiswa, ruang kegiatan, prestasi, AIK, layanan, cerita mahasiswa, FAQ, dan ajakan bertindak.', 500, 10.2, MUTED, 15)

y = card(p, 44, 171, 247, 564, 'Kemahasiswaan', 'Ruang untuk tumbuh dan berkarya')
content_groups = [
    ('Organisasi dan UKM', 'IMM, Hizbul Wathan, Tapak Suci; English Club, Business Digital, Digital Creator.'),
    ('Komunitas', 'Health Science Research Club dan Discord Information System SiberMu.'),
    ('Ilmiah dan kompetisi', 'PIMNAS, PKM, KBMI, MAWAPRES, GEMASTIK, KDMI, SATRIA DATA, LIDM, KBMK, dan PUSPRESMA PTMA.'),
    ('Minat bakat', 'Musabaqah Tilawatil Quran Mahasiswa Nasional dan Pekan Seni Mahasiswa PTMA.'),
    ('Internasional', 'Global Youth Action, Youth Innovation Forum, Student Exchange, dan Student Mobility.'),
    ('Prestasi dan layanan', 'Hall of Fame mengelompokkan prestasi per tahun. Kartu sinopsis mengarah ke bagian prestasi, UKM, organisasi, dan layanan terkait.'),
]
for title, desc in content_groups:
    p.text(62, y + 6, title, 9.1, NAVY, True)
    y = p.para(62, y + 22, desc, 210, 8.5, MUTED, 12) + 10

y = card(p, 307, 171, 244, 564, 'Al-Islam dan Kemuhammadiyahan', 'Nilai dalam keseharian')
aik_groups = [
    ('Kegiatan', 'Kegiatan keagamaan, kajian, syiar digital, dan penguatan nilai Kemuhammadiyahan.'),
    ('Delapan nilai utama', 'Al-Qiyam Al-Fadhilah; pemuliaan manusia; persaudaraan; welas asih; etos kerja tinggi; tauhid pro kemanusiaan; nilai ilmiah/keilmuan; dan nilai peradaban.'),
    ('Penyajian', 'Foto kegiatan, aksen warna biru, dan daftar kegiatan berbentuk kartu menjaga konsistensi dengan bagian kemahasiswaan.'),
]
for title, desc in aik_groups:
    p.text(325, y + 6, title, 9.1, NAVY, True)
    y = p.para(325, y + 22, desc, 208, 8.6, MUTED, 12) + 16
p.rect(325, 581, 208, 108, (0.93, 0.96, 0.98), None, 10)
p.text(341, 608, 'FITUR INTERAKTIF', 7.5, BLUE, True)
p.para(341, 630, 'Tab kategori Kemahasiswaan, tab Visi/Misi, carousel cerita mahasiswa, navigasi section, dan chatbot Aisa.', 176, 8.5, MUTED, 12)
pages.append(p)

# 4. Implementation, assets, and references
p = Page()
header(p, 'Teknologi dan Kredit Media', 4)
p.text(44, 112, 'IMPLEMENTASI', 8, BLUE, True)
p.text(44, 136, 'Dibangun sebagai antarmuka web satu halaman.', 15, NAVY, True)

stack = [
    ('Vue 3 + TypeScript', 'Komponen section modular dan data konten terpisah.'),
    ('Vite', 'Server pengembangan dan proses build production.'),
    ('Tailwind CSS 4', 'Sistem utility untuk tata letak responsif dan token visual.'),
    ('Lucide Vue', 'Ikon antarmuka.'),
]
for i, (title, desc) in enumerate(stack):
    x = 44 + (i % 2) * 259
    y = 158 + (i // 2) * 66
    p.rect(x, y, 242, 54, PALE, LINE, 9)
    p.text(x + 13, y + 21, title, 9, NAVY, True)
    p.text(x + 13, y + 38, desc, 7.5, MUTED)

p.text(44, 318, 'SUMBER INFORMASI DAN VISUAL', 8, BLUE, True)
p.para(44, 344, 'Informasi institusi merujuk pada situs resmi sibermu.ac.id dan snapshot materi proyek bertanggal 11 September 2026. Panduan lomba menjadi acuan cakupan tema Kemahasiswaan dan AIK. Referensi screenshot desain dipakai sebagai inspirasi tata letak; halaman dirancang ulang untuk identitas SiberMu.', 500, 9.1, MUTED, 13)

media = [
    ('Konten AI', 'Hero scene3-scene6, bem.webp (Kemahasiswaan), kajian.webp (AIK), dan mulai.webp (Final CTA).'),
    ('Instagram SiberMu', 'student.png serta winner/winner1.webp dan winner/winner2.webp (Prestasi). Posting spesifik belum dicatat.'),
    ('Website SiberMu + aset lokal', 'kampus-virtual.webp bersumber dari website SiberMu. Asal/lisensi aisa.webp, logo-only.png, sibermu-logo.png, sibermu-white.png, dan enam logo src/assets/prodi/ belum tercatat.'),
    ('Ikon, font, UI', 'Lucide Icons (@lucide/vue); Geist, Inter Tight, TASA Explorer (Google Fonts); Reka UI; Tailwind CSS.'),
    ('Referensi konten/desain', 'Informasi sibermu.ac.id, panduan lomba, dan screenshot referensi yang dibagikan selama proses desain.'),
]
for i, (label, desc) in enumerate(media):
    y = 414 + i * 47
    p.line(44, y - 10, 551, y - 10)
    p.text(44, y + 4, label, 7.8, NAVY, True)
    p.para(174, y + 4, desc, 377, 7.5, MUTED, 10)

p.rect(44, 677, 507, 84, (1.0, 0.96, 0.89), (0.91, 0.78, 0.55), 10)
p.text(60, 702, 'CATATAN SEBELUM PENGUMPULAN', 7.5, (0.55, 0.34, 0.08), True)
p.para(60, 723, 'Konfirmasikan asal dan izin publikasi aset lokal yang belum memiliki sumber. Nama testimoni yang tampil merupakan nama contoh, bukan identitas mahasiswa terverifikasi.', 472, 8.1, (0.35, 0.31, 0.25), 11)
pages.append(p)


def make_pdf(page_list, output):
    objects = []
    def add(obj):
        objects.append(obj if isinstance(obj, bytes) else obj.encode('latin1'))
        return len(objects)

    catalog_id = add(b'')
    pages_id = add(b'')
    font_regular = add(b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>')
    font_bold = add(b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>')
    font_oblique = add(b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique /Encoding /WinAnsiEncoding >>')
    page_ids = []
    for page in page_list:
        stream = ('\n'.join(page.ops)).encode('cp1252', errors='replace')
        content_id = add(f'<< /Length {len(stream)} >>\nstream\n'.encode('ascii') + stream + b'\nendstream')
        page_id = add(f'<< /Type /Page /Parent {pages_id} 0 R /MediaBox [0 0 {PAGE_W} {PAGE_H}] /Resources << /Font << /F1 {font_regular} 0 R /F2 {font_bold} 0 R /F3 {font_oblique} 0 R >> >> /Contents {content_id} 0 R >>')
        page_ids.append(page_id)
    kids = ' '.join(f'{pid} 0 R' for pid in page_ids)
    objects[pages_id - 1] = f'<< /Type /Pages /Kids [{kids}] /Count {len(page_ids)} >>'.encode('ascii')
    objects[catalog_id - 1] = f'<< /Type /Catalog /Pages {pages_id} 0 R >>'.encode('ascii')

    pdf = bytearray(b'%PDF-1.4\n%\xe2\xe3\xcf\xd3\n')
    offsets = [0]
    for i, obj in enumerate(objects, start=1):
        offsets.append(len(pdf))
        pdf.extend(f'{i} 0 obj\n'.encode('ascii'))
        pdf.extend(obj)
        pdf.extend(b'\nendobj\n')
    xref = len(pdf)
    pdf.extend(f'xref\n0 {len(objects)+1}\n'.encode('ascii'))
    pdf.extend(b'0000000000 65535 f \n')
    for offset in offsets[1:]:
        pdf.extend(f'{offset:010d} 00000 n \n'.encode('ascii'))
    pdf.extend(f'trailer\n<< /Size {len(objects)+1} /Root {catalog_id} 0 R >>\nstartxref\n{xref}\n%%EOF\n'.encode('ascii'))
    Path(output).write_bytes(pdf)


make_pdf(pages, Path(__file__).with_name('Dokumentasi_Lomba_SiberMu_2026.pdf'))
