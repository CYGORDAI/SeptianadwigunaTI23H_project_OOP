# Project UAS OOP: MLBB Scrim Tracker

Aplikasi ini adalah sebuah sistem pelacak jadwal dan hasil latihan tanding (scrim) untuk tim Mobile Legends, yang dibangun dengan Python dan konsep Object-Oriented Programming (OOP) berbasis Command-Line Interface (CLI).

## Inspirasi

Aplikasi ini terinspirasi dari kegiatan rutin tim e-sports amatir, yaitu melakukan scrim untuk melatih kekompakan dan strategi. Seringkali, jadwal dan hasil scrim hanya dicatat di grup chat sehingga sulit dilacak dan dianalisis. Aplikasi ini bertujuan untuk menjadi pusat data scrim yang terorganisir bagi sebuah tim.

## Fitur

-   **Penjadwalan Scrim**: Membuat jadwal scrim baru melawan tim lain dengan format pertandingan yang bisa ditentukan.
-   **Pencatatan Hasil**: Mengupdate hasil scrim yang telah selesai, termasuk hasil per-game dan skor akhir.
-   **Analisis Sederhana**: Pengguna dapat menambahkan catatan analisis untuk setiap game dan keseluruhan scrim sebagai bahan evaluasi.
-   **Riwayat Pertandingan**: Menampilkan semua jadwal scrim yang akan datang dan riwayat scrim yang telah selesai.
-   **Penyimpanan Database**: Semua data disimpan secara terstruktur di database MySQL lokal (via XAMPP).

## Instalasi dan Konfigurasi

Ikuti langkah-langkah berikut untuk menyiapkan project agar bisa berjalan:

**1. Prasyarat**
   - Pastikan **Python 3.x** dan **XAMPP** sudah terinstal.
   - Instal library yang dibutuhkan dengan membuka terminal di folder project dan jalankan:
     ```bash
     pip install mysql-connector-python
     ```

**2. Setup Database**
   - Jalankan modul **Apache** dan **MySQL** dari XAMPP Control Panel.
   - Buka `phpMyAdmin` di browser (`http://localhost/phpmyadmin`).
   - Gunakan fitur **"Import"** untuk membuat database dan tabel secara otomatis:
     1. Klik "New" di panel kiri, buat database kosong bernama `mlbb_scrim_db`.
     2. Klik database `mlbb_scrim_db` tersebut.
     3. Buka tab **"Import"**.
     4. Klik "Choose File" dan pilih file `database_setup.sql` dari dalam folder `data/` project ini.
     5. Klik **"Go"** untuk memulai proses import.

**3. Jalankan Aplikasi**
   - Setelah setup database selesai, jalankan aplikasi dari terminal:
     ```bash
     python main.py
     ```
   - Ikuti menu interaktif yang muncul.

---

**Link Video Demo:** [Tulis link video YouTube atau repo Anda di sini]