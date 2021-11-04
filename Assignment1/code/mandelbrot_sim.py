import numpy as np
import pandas as pd
import random as rd
import matplotlib.pyplot as plt

def mandelbrot(real, imag, max_iter):
    c = complex(real, imag)
    z = 0 + c
    n = 1
    while abs(z) <= 2 and n < max_iter:
        z = z * z + c
        n = n + 1
    if n != max_iter:
        return 0
    else: 
        return 1


print(mandelbrot(0, -0.5, 100))

def mandelbrotMC(sample, max_iter):
    hit = 0
    for s in range(sample):
        r1 = rd.random()
        r2 = rd.random()
        real = (r1*3) - 2
        imag = (r2 * 3) - (3/2)

        hit = hit + mandelbrot(real, imag, max_iter)
    return (hit / sample) * 9
        
res = mandelbrotMC(10000, 1000)
print(res)
    
