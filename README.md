# Belajar POM dengan Playwright dan Pytest

Proyek ini berisi automated UI tests untuk [SauceDemo](https://www.saucedemo.com/), menggunakan Python, Playwright, pytest, dan pola Page Object Model (POM).

## Prasyarat

- Python 3
- Koneksi internet untuk membuka SauceDemo dan mengunduh browser Playwright

## Instalasi

Buka PowerShell di folder proyek, lalu jalankan:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m playwright install chromium
```

Jika PowerShell memblokir aktivasi virtual environment, Anda tetap dapat menjalankan perintah Python melalui `.venv\Scripts\python.exe`.

## Menjalankan test

Jalankan semua test:

```powershell
python -m pytest
```

Jalankan satu file test:

```powershell
python -m pytest tests\test_login.py -v
```

Lihat daftar test tanpa menjalankannya:

```powershell
python -m pytest --collect-only -q
```

## Cakupan test

Test mencakup login, inventory, keranjang, checkout, validasi input, akses halaman, dan isolasi sesi pengguna. Test UI memerlukan browser Chromium yang dipasang melalui Playwright serta akses ke SauceDemo.

## Struktur proyek

```text
conftest.py   # Fixture pytest dan konfigurasi laporan
pages/        # Page Object untuk halaman aplikasi
tests/        # Skenario automated test
```

Laporan HTML dibuat di folder `reports/`. Jika test gagal, konfigurasi proyek juga mencoba menyimpan screenshot di folder tersebut.
