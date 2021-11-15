import numpy as np
import pandas as pd
import random as rd
import matplotlib.pyplot as plt
import math 

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

def mandelbrotMC(sample, max_iter):
    
    hit = 0
    
    #creating containers for values
    c_container = np.zeros(shape = (sample+1, 2))
    stats_container = np.zeros(shape = (sample+1, 2))

    for s in range(1, sample+1):
        real = np.random.uniform(-2,1) #sampling for the real axis
        imag = np.random.uniform(-3/2, 3/2) #sampling for the imaginary axis

        #filling the container
        c_container[s,0] = real
        c_container[s,1] = imag

        is_mandelbrot = mandelbrot(real, imag, max_iter) #checking whether the given sample is in the mandelbrot set
        hit = hit +  is_mandelbrot

        stats_container[s,0] = hit/s * 9
        stats_container[s,1] = np.mean(stats_container[:s,0])

    return hit / sample * 9 

def mandelbrotLHC(sample, max_iter):
  dim1 = np.array(range(0,sample))
  dim2 = np.array(range(0, sample))

  ##setting up the parameters of the rectangle bound
  len1 = len2 = 3 #length of each axis segment
  b_x_lower = -2 #lower boundary of x axis
  b_y_lower = -3/2 # lower boundary of y axis

  hit = 0
  
  #creating containers 
  c_container = np.zeros(shape = (sample + 1, 2))
  stats_container = np.zeros(shape = (sample+1, 2))

  for s in range(1, sample+1):
    #choose a subspace
    x_strata = np.random.choice(dim1, 1)
    y_strata = np.random.choice(dim2, 1)

    #update the remaining subspaces
    dim1 = np.delete(dim1, np.where(dim1 == x_strata))
    dim1 = np.delete(dim1, np.where(dim1 == x_strata))

    #sample random values with given boundaries
    real = rd.uniform(b_x_lower + x_strata * len1 / sample, b_x_lower + (x_strata + 1) * len1 / sample )
    imag = rd.uniform(b_y_lower + y_strata * len2 / sample, b_y_lower + (y_strata + 1) * len2 / sample )

    #filling the container
    c_container[s,0] = real
    c_container[s,1] = imag

    #checking whether the given sample is in the mandelbrot set
    stats_container[s,0] = hit/s * 9
    stats_container[s,1] = np.mean(stats_container[:s,0])

  return hit / sample * 9


def mandelbrotOS(sample_sqrt, max_iter):
  ##setting up the parameters of the rectangle bound
  len1 = len2 = 3 #length of each axis segment
  b_x_lower = -2 #lower boundary of x axis
  b_y_lower = -3/2 # lower boundary of y axis

  hit = 0

  for i in range(sample_sqrt):
    for j in range(sample_sqrt):
      real = rd.uniform(b_x_lower + i * len1 / sample_sqrt, b_x_lower + (i + 1) * len1 / sample_sqrt )
      imag = rd.uniform(b_y_lower + j * len2 / sample_sqrt, b_y_lower + (j + 1) * len2 / sample_sqrt )
      
      is_mandelbrot = mandelbrot(real, imag, max_iter)
      hit = hit +  is_mandelbrot
  
  return hit / (sample_sqrt ** 2) * 9

#questionable but it seem to work
def mandelbrotAntiVar(sample, max_iter):
  hit = 0

  for s in range(sample):
    r1 = rd.random()
    r1_anti = 1 - r1
    r2 = rd.random()
    r2_anti = 1 - r2 #creating every antitetic point
    r1_samps = [r1, r1_anti]
    r2_samps = [r2, r2_anti]
    
    for i in r1_samps: #iterating over these points
      for j in r2_samps:
        real = (i*3) - 2
        imag = (j * 3) - 3/2
        
        is_mandelbrot = mandelbrot(real, imag, max_iter)
        hit = hit +  is_mandelbrot


  return hit / (4 * sample) * 9