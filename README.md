# ðŸ'¥ WlsBruteforce â€” Generator Kata Sandi Edukatif ðŸ”'
*Ringan â€¢ Berbasis Generator â€¢ Lintas Platform*

Modul Python yang sederhana dan portabel yang dirancang **untuk penelitian keamanan siber pendidikan**, menunjukkan cara kerja mekanika bruteforce menggunakan `itertools` Python dan **generator hemat memori**.

<p align="kiri">
  <img src="https://img.shields.io/badge/Python-3.6%2B-biru?style=untuk-lencana&logo=python&logoColor=putih" />
  <img src="https://img.shields.io/badge/Lisensi-MIT-kuning?style=untuk-lencana" />
  <img src="https://img.shields.io/github/stars/NamaPenggunaAnda/wlsbruteforce?style=untuk-lencana&warna=biru" />
</p>

---

## âœ¨ Fitur

- **Bruteforce Berbasis Generator**  
  Menggunakan `yield` Python untuk pembangkitan sesuai permintaan â€” tidak ada kehabisan memori.

- **Set Karakter Lengkap**  
  Termasuk huruf kecil (`aâ€“z`), huruf besar (`Aâ€“Z`), dan angka (`0â€“9`).

- **Sangat Ringan**  
  Python murni. Tanpa dependensi eksternal.

**Kompatibel Lintas Platform**  
  Berfungsi pada Linux, macOS, Windows, dan Android Termux.

> âš ï¸ **Penafian:** Modul ini semata-mata ditujukan untuk **penelitian keamanan pendidikan & etika**.  
> Jangan menggunakannya untuk kegiatan ilegal.

---

## ðŸ“¥ Instalasi

Instal langsung dari GitHub:

```pesta
pip install "git+https://github.com/NamaPenggunaAnda/wlsbruteforce.git"
```

---

## ðŸš€ Mulai Cepat

### 1. Jalankan Interpreter Python
```pesta
$ python3
```

### 2. Impor kelas
```ular piton
dari wlsbruteforce impor WlsBruteforce
```

### 3. Inisialisasi generator
```ular piton
generator = WlsBruteforce()
```

### 4. Hasilkan percobaan (panjang 1-2)
```ular piton
percobaan = generator.brute(panjang_min=1, panjang_maks=2)
```

### 5. Cetak 10 percobaan pertama
```ular piton
untuk i dalam rentang (10):
    cetak(berikutnya(percobaan), akhir=' ')
```

### 6. Tampilkan total perkiraan percobaan
```ular piton
cetak(generator.perkiraan_kombinasi_total)
```

**Perhitungan:**  
`62^1 + 62^2 = 62 + 3844 = 3906`

---

## ðŸ“š Contoh Kode

```ular piton
dari wlsbruteforce impor WlsBruteforce

generator = WlsBruteforce()

percobaan = generator.brute(panjang_min=1, panjang_maks=3)

untuk i, mencoba menghitung(percobaan):
    cetak(percobaan)

    jika i == 50: # Berhenti setelah 50 percobaan
        merusak

cetak("Perkiraan total:", generator.total_combinations_estimate)
```

---

## ðŸ“¦ Struktur Proyek

```
wlsbruteforce/
â”‚â”€â”€ wlsbruteforce.py
â”‚â”€â”€ __init__.py
â”‚â”€â”€ README.md
â”‚â”€â”€ LISENSI
```

---

## ðŸ› ï¸ Cara Kerjanya

- Menggunakan `itertools.product()` untuk membuat kombinasi
- Dibungkus dengan `yield` untuk membuat generator streaming
- Berjalan sangat cepat dan tanpa menghabiskan memori besar

---

## ðŸ“„ Lisensi

Proyek ini dilisensikan di bawah **Lisensi MIT** â€” silakan gunakan, modifikasi, dan distribusikan secara bertanggung jawab.

---

## â Dukungan

Jika Anda merasa ini berguna, beri proyek ini **bintang** di GitHub!  
