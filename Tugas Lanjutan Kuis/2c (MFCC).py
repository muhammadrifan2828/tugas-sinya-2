# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 18:23:40 2023

@author: 62813
"""
print ('Muhammad Rifan Ikhlasul Ammal')
print ('5009211138')

import numpy as np
import matplotlib.pyplot as plt

def fft(x):
    N = len(x)
    if N <= 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    twiddle_factors = [np.exp(-2j * np.pi * k / N) * odd_k for k, odd_k in enumerate(odd)]
    return [even_k + twiddle_k for even_k, twiddle_k in zip(even, twiddle_factors)] + \
           [even_k - twiddle_k for even_k, twiddle_k in zip(even, twiddle_factors)]

def ifft(x):
    N = len(x)
    if N <= 1:
        return x
    even = ifft(x[0::2])
    odd = ifft(x[1::2])
    twiddle_factors = [np.exp(2j * np.pi * k / N) * odd_k for k, odd_k in enumerate(odd)]
    return [even_k + twiddle_k for even_k, twiddle_k in zip(even, twiddle_factors)] + \
           [even_k - twiddle_k for even_k, twiddle_k in zip(even, twiddle_factors)]

def fft2d(matrix):
    rows, cols = len(matrix), len(matrix[0])

    for i in range(rows):
        matrix[i] = fft(matrix[i])

    for j in range(cols):
        col = [matrix[i][j] for i in range(rows)]
        col = fft(col)
        for i in range(rows):
            matrix[i][j] = col[i]

    return matrix

def fmcc(matrix):
    
    matrixfft = fft2d(matrix)

 
    log_spectrum = np.log(np.abs(matrixfft) ** 2 + 1e-10)

    # Inverse FFT
    cepstrum = ifft2d(log_spectrum)

    return cepstrum

def ifft2d(matrix):
    rows, cols = len(matrix), len(matrix[0])

    for i in range(rows):
        matrix[i] = ifft(matrix[i])

    for j in range(cols):
        col = [matrix[i][j] for i in range(rows)]
        col = ifft(col)
        for i in range(rows):
            matrix[i][j] = col[i]

    return matrix

def display_matrix(matrix, judul):
    plt.imshow(np.abs(matrix), cmap='viridis')
    plt.colorbar()
    plt.title(judul)
    plt.show()

# Oontoh dengan input matrix yang lain
input_matrix = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
    [12, 13, 14, 15]
]

# modifikasi input matrix
for i in range(len(input_matrix)):
    for j in range(len(input_matrix[0])):
        input_matrix[i][j] += i + j  

fmcc_result = fmcc(input_matrix)

# Display Input FMCC dan Input yang termodifikasi
display_matrix(input_matrix, 'Input Modifikasi Matrix')


display_matrix(fmcc_result, 'Implementasi FFC')