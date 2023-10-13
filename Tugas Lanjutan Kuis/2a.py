# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 18:34:38 2023

@author: ADMIN
"""

from cmath import exp, pi
from scipy.fft import fft


def FFT(x):
    Panjang = len(x)
    jawaban = []
    if Panjang <= 2:
        return x
    else:
        for k in range(Panjang):
            temp = []
            for i in range (Panjang):
                temp.append(x[i] * exp(-2j * pi * k * i / Panjang))
            jawaban.append(sum(temp))
        return jawaban
    
 
x = [3, 5, 7, 9, 11]
    
myans = FFT(x)
jawaban = fft(x)

print(myans)
print(jawaban)



