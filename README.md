# Tbo Engine V2: Simulator Deterministic Finite Automata (DFA) Berbasis Web

Proyek ini merupakan implementasi perangkat lunak simulator otomata berhingga deterministik yang dibangun untuk memenuhi tugas akhir (*Capstone Project*) pada mata kuliah Teori Bahasa dan Otomata. Aplikasi ini mengonversi konsep matematika abstrak DFA menjadi sistem aplikasi web interaktif yang mampu mengevaluasi untai karakter secara *real-time*.

---

## Identitas Pengembang
* **Nama:** Syifa Kanita Putri Gunawan
* **NIM:** 301240016
* **Program Studi:** Teknik Informatika
* **Keterangan Tugas:** Capstone Project - Mata Kuliah Teori Bahasa dan Otomata (TBO)

---

## Tautan Akses Aplikasi (Deployment)
Aplikasi ini telah dideploy secara online dan dapat diakses publik melalui tautan domain berikut:
* **Custom Domain:** syifakanitaputri.my.id

---

## Fitur Utama Aplikasi
1. **Mesin Evaluasi DFA Linar:** Memproses inputan string alfabet `{a, b}` secara sekuensial dengan transisi status yang deterministik dan presisi.
2. **Ekspresi Reguler (Regex) Matcher:** Validasi pola bahasa reguler di sisi backend untuk memastikan akurasi kebenaran untai.
3. **Antarmuka Responsif (Bootstrap Grid):** Tata letak halaman yang adaptif, tetap rapi saat diakses melalui perangkat komputer maupun layar ponsel (*smartphone*).
4. **Visualisasi Dinamis & Animasi CSS:** Komponen penanda hasil yang interaktif dengan perubahan warna responsif (*emerald green* untuk diterima dan *crimson red* untuk ditolak) disertai efek transisi gerak halus (*smooth fade-in*).
5. **Sistem Pengaman Input (Data Cleansing):** Backend dilengkapi dengan penanganan eror (*error handling*) yang otomatis menolak karakter ilegal di luar alfabet ruang lingkup sistem.

---

## Arsitektur Teknologi (Tech Stack)
* **Backend:** Python, Flask Framework
* **Frontend:** HTML5, CSS3 (Custom Animation), Bootstrap v5
* **Infrastruktur & Hosting:** Hugging Face Spaces, Cloudflare DNS Management, SSL/TLS HTTPS

---

## Struktur Berkas Proyek
```text
├── static/
│   └── css/
│       └── style.css      # Kustomisasi animasi dan gaya visual antarmuka
├── templates/
│   └── index.html         # Struktur halaman utama dan logika Jinja2 template
├── .gitignore             # Daftar berkas terabaikan dari pelacakan git
├── app.py                 # Logika utama server Flask dan tabel transisi DFA
├── README.md              # Dokumentasi proyek (berkas ini)
└── requirements.txt       # Daftar pustaka dependensi Python untuk deployment
