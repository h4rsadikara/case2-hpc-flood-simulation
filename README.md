# Studi Kasus 2: Bridging Global Infrastructure to Address Local Challenge with HPC

## Deskripsi
Simulasi Monte Carlo risiko banjir pada 400 sel grid. Tiap sel independen (embarrassingly parallel), sehingga mudah dibagi ke banyak core atau node. Kode memeriksa bahwa hasil paralel identik dengan serial, lalu mengukur speedup dan efisiensi. Speedup bergantung jumlah core mesinmu; jalankan ulang di laptopmu dan pakai angkamu sendiri. Di cluster, pola yang sama dijalankan lewat SLURM array job.

## Cara menjalankan
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py
```
Grafik tersimpan di folder `outputs/`.

## Catatan
Data pada proyek ini sintetis atau bawaan library agar bisa dijalankan tanpa dataset eksternal. Kesimpulan substantif perlu divalidasi dengan data nyata.

## Afsha Dwi Saputra G1A025101
