"""Studi Kasus 2 - Bridging global infrastructure to address local challenge with HPC.
Kasus: simulasi risiko banjir lokal. Ratusan sel grid dihitung runoff-nya dengan
Monte Carlo curah hujan. Pekerjaan dipecah ke banyak core (pola yang sama dengan
cluster HPC / SLURM array job), lalu diukur speedup & efisiensi.
"""
import time, os
import numpy as np
from multiprocessing import Pool

N_CELLS, N_SIM = 400, 20000

def simulate_cell(seed):
    rng = np.random.default_rng(seed)
    rain = rng.gamma(shape=2.0, scale=40.0, size=N_SIM)          # mm/hari
    cn = rng.uniform(60, 95)                                      # curve number tanah
    s = 25400 / cn - 254
    runoff = np.where(rain > 0.2 * s, (rain - 0.2 * s) ** 2 / (rain + 0.8 * s), 0)
    return float((runoff > 80).mean())                            # peluang banjir

def run(workers):
    t = time.perf_counter()
    if workers == 1:
        res = [simulate_cell(i) for i in range(N_CELLS)]
    else:
        with Pool(workers) as p:
            res = p.map(simulate_cell, range(N_CELLS), chunksize=10)
    return time.perf_counter() - t, np.array(res)

if __name__ == "__main__":
    cores = os.cpu_count()
    t1, r1 = run(1)
    print(f"Core tersedia: {cores}")
    print(f"Serial   : {t1:.2f} s")
    for w in sorted({2, 4, cores}):
        if w < 2: continue
        tw, rw = run(w)
        assert np.allclose(r1, rw)                                # hasil harus identik
        print(f"{w} proses : {tw:.2f} s | speedup {t1/tw:.2f}x | efisiensi {t1/tw/w:.0%}")
    print(f"Rata-rata peluang banjir antar sel: {r1.mean():.1%}")
    print("Catatan: di cluster HPC, kode yang sama dipecah per node via SLURM array job.")
