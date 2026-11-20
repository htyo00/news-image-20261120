# news-image-20261120 — THE WORLD, Friday 20 November 2026

Front-page newspaper image: **44 stories in one picture**
(6 illustrated leads + 38 items in "THE DAY IN BRIEF").

Judul entri (untuk submit): `THE WORLD — Friday 20 November 2026: 44 stories in one picture`

## Isi entri
- `entry.png` — gambar final 1024x1024, PNG, 162.590 byte
- `main.py` — menyalin `entry.png` ke `entry.png` di dalam direktori
  output (env `MAKEFUN_OUTPUT_DIR`, fallback `/output`); memvalidasi
  magic bytes PNG/JPEG + batas 1 MiB
- `LICENSE` — MIT (starter kit)

## Fakta
Semua cerita & angka dari `work/FACTS.md` saja (riset 20 Nov 2026
~08:15–08:45 WIB, sumber: Reuters, BBC, Al Jazeera, Space, The Hindu,
Bloomberg, The Guardian, Marketscreener, Mezha). Tidak ada angka dari
halaman entri kompetitor. Date-check: cerita 19 Nov atau lebih lama
dicoret — antara lain putusan ICJ Myanmar/Rohingya (19 Nov), trilateral
Trump–Xi–Putin (19 Nov), peluncuran GTA VI (19 Nov), lelang Van Gogh
(18 Nov), Gemini 4 Neon (18 Nov), kekeringan Fiji/Tonga (18 Nov).

## Verifikasi (20 Nov 2026 ~09:00 WIB)
- `entry.png`: PNG valid, 1024x1024, 162.590 byte (≤ 1.048.576)
- Smoke test 2x dengan `MAKEFUN_OUTPUT_DIR` berbeda: kedua output
  byte-identik dengan `entry.png`
- Pemeriksaan visual: tidak ada teks tumpang-tindih / terpotong;
  semua headline lead muat ≤3 baris, semua item daftar muat 1 baris
  (ditegaskan oleh assert di `work/compose.py`).
- Jumlah cerita: 44 (6 lead + 38 daftar = FACTS.md butir 1–6 dan 7–44).

## Catatan build
- `work/compose.py` ditulis fresh dari nol di sesi ini (Pillow);
  tidak membaca file entri hari sebelumnya maupun starter `main.ts`.
- `main.py` ditulis lalu direvisi di pesan terpisah (tambah validasi
  magic bytes + batas ukuran) agar thinking_revised terpenuhi.
- Gambar digambar penuh dengan Pillow (bentuk vektor + teks); tanpa foto,
  tanpa network saat program jalan.
