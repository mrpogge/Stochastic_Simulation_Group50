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
    c_container = np.zeros(shape = (sample+1, 3))
    stats_container = np.zeros(sample+1)

    for s in range(1, sample+1):
        real = np.random.uniform(-2,1) #sampling for the real axis
        imag = np.random.uniform(-3/2, 3/2) #sampling for the imaginary axis

        #filling the container
        c_container[s,0] = real
        c_container[s,1] = imag

        is_mandelbrot = mandelbrot(real, imag, max_iter) #checking whether the given sample is in the mandelbrot set
        hit = hit +  is_mandelbrot

        c_container[s,2] = is_mandelbrot

        stats_container[s] = hit/s * 9

    
    return stats_container, c_container

def mandelbrotLHC(sample, max_iter):
  dim1 = np.array(range(0,sample))
  dim2 = np.array(range(0, sample))

  ##setting up the parameters of the rectangle bound
  len1 = len2 = 3 #length of each axis segment
  b_x_lower = -2 #lower boundary of x axis
  b_y_lower = -3/2 # lower boundary of y axis

  hit = 0
  
  #creating containers 
  c_container = np.zeros(shape = (sample + 1, 3))
  stats_container = np.zeros(sample+1)

  for s in range(1, sample+1):
    #choose a subspace
    x_strata = np.random.choice(dim1, 1)
    y_strata = np.random.choice(dim2, 1)

    #update the remaining subspaces
    dim1 = np.delete(dim1, np.where(dim1 == x_strata))
    dim2 = np.delete(dim2, np.where(dim2 == y_strata))

    #sample random values with given boundaries
    real = rd.uniform(b_x_lower + x_strata * len1 / sample, b_x_lower + (x_strata + 1) * len1 / sample )
    imag = rd.uniform(b_y_lower + y_strata * len2 / sample, b_y_lower + (y_strata + 1) * len2 / sample )

    #filling the container
    c_container[s,0] = real
    c_container[s,1] = imag

    #checking whether the given sample is in the mandelbrot set
    is_mandelbrot = mandelbrot(real, imag, max_iter)
    hit = hit +  is_mandelbrot

    c_container[s,2] = is_mandelbrot

    stats_container[s] = hit/s * 9


  return stats_container, c_container


def mandelbrotOS(sample_sqrt, max_iter):
  ##setting up the parameters of the rectangle bound
  len1 = len2 = 3 #length of each axis segment
  b_x_lower = -2 #lower boundary of x axis
  b_y_lower = -3/2 # lower boundary of y axis

  hit = 0
  #creating containers 
  c_container = np.zeros(shape = (sample_sqrt**2 + 1, 3))
  stats_container = np.zeros(sample_sqrt**2 + 1)

  counter = 0
  for i in range(sample_sqrt):
    for j in range(sample_sqrt):
      counter = counter+1
      real = rd.uniform(b_x_lower + i * len1 / sample_sqrt, b_x_lower + (i + 1) * len1 / sample_sqrt )
      imag = rd.uniform(b_y_lower + j * len2 / sample_sqrt, b_y_lower + (j + 1) * len2 / sample_sqrt )

      #filling the container
      c_container[counter,0] = real
      c_container[counter,1] = imag  

      is_mandelbrot = mandelbrot(real, imag, max_iter)
      hit = hit +  is_mandelbrot

      c_container[counter,2] = is_mandelbrot

      stats_container[counter] = hit/counter * 9

  
  return stats_container, c_container

