# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 18:10:03 2023

@author: 62813
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import ifft2, fft2, fftshift

# Mgambar uji
x, y = np.meshgrid(np.linspace(-5, 5, 256), np.linspace(-5, 5, 256))
image = np.sin(np.sqrt(x**2 + y**2))

#  FFT dua dimensi
hasilfft = fft2(image)
hasilfft = fftshift(hasilfft)  # Menggeser frekuensi nol ke tengah

# magnitude spektrum frekuensi
magnitudespectrum = np.abs(hasilfft)

# invers FFT untuk mendapatkan gambar kembali
reconstructed_image = ifft2(hasilfft)

# gambar asli, spektrum frekuensi, dan gambar rekonstruksi
plt.figure(figsize=(12, 6))

plt.subplot(131)
plt.imshow(image, cmap='gray')
plt.title('Gambar Asli')
plt.xticks([]), plt.yticks([])

plt.subplot(132)
plt.imshow(np.log(magnitudespectrum + 1), cmap='gray')
plt.title('Spektrum Frekuensi')
plt.xticks([]), plt.yticks([])

plt.subplot(133)
plt.imshow(np.real(reconstructed_image), cmap='gray')
plt.title('Gambar Rekonstruksi')
plt.xticks([]), plt.yticks([])

plt.show()

