# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 10:44:57 2023

@author: 62813
"""
print ("Implementation a Convolution of two 1-dimensional array signals")
print ("Muhammad Rifan Ikhlasul Ammal")
print ("500921138")

def convolution(signal, kernel):
    signal_length = len(signal)
    kernel_length = len(kernel)
    output_length = signal_length + kernel_length - 1
    result = [0] * output_length

    for i in range(output_length):
        for j in range(kernel_length):
            if i - j >= 0 and i - j < signal_length:
                result[i] += signal[i - j] * kernel[j]

    return result

signal = [1, 2, 3, 4, 5]
kernel = [0.5, 1, 0.5]

result = convolution(signal, kernel)
print("Convolution result (without NumPy):", result)

# Using only NumPy to validate the result:
import numpy as np

numpy_result = np.convolve(signal, kernel, mode='full')
print("NumPy Convolve result (for validation):", numpy_result.tolist())
