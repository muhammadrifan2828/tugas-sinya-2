# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 23:43:57 2023

@author: 62813
"""
print ('Muhammad Rifan Ikhlasul Ammal')
print ('5009211138')

import numpy as np
import cmath
import matplotlib.pyplot as plt

# Parameter
SetengahPanjangSinyal = 3  
PanjangSinyal = 4 * SetengahPanjangSinyal  
JumlahSampel = 1024  
t = np.linspace(-PanjangSinyal / 2, PanjangSinyal / 2, JumlahSampel, endpoint=False)  # Sampel waktu


def f(t):
    if abs(t) <= SetengahPanjangSinyal:
        return 1.0
    else:
        return 0.0


F_manual = [0] * JumlahSampel

# Menghitung FFT Manual
for k in range(JumlahSampel):
    Fk = 0
    for j in range(JumlahSampel):
        Fk += f(t[j]) * cmath.exp(-2j * cmath.pi * k * j / JumlahSampel)
    F_manual[k] = Fk

# Menghitung FFT Menggunakan Numpy
F_numpy = np.fft.fft([f(tj) for tj in t])

# Validasi hasil
hasilvalidasi = np.allclose(F_manual, F_numpy, rtol=1e-10, atol=1e-10)
if hasilvalidasi:
    print("Hasil sesuai")
else:
    print("Hasil tidak sesuai")

# Hitung frekuensi
freqs = [k / PanjangSinyal for k in range(JumlahSampel)]

# Plot sinyal asli, manual, melalalui validasi numpy

plt.figure(figsize=(10, 6))
plt.subplot(311)
plt.plot(t, [f(tj) for tj in t])
plt.title('Sinyal Asli')
plt.grid()


plt.subplot(312)
plt.plot(freqs, [abs(Fk) for Fk in F_manual])
plt.title('Manual')
plt.grid()


plt.subplot(313)
plt.plot(freqs, np.abs(F_numpy))
plt.title('Validasi Numpy')
plt.grid()

plt.tight_layout()
plt.show()
