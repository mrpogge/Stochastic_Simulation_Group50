import numpy as np
import pandas as pd
import random as rd
import matplotlib.pyplot as plt
import math 

def bootstrapMandelbrot(c_container, resamples):
  nrows, ncols = c_container.shape
  indexes = np.random.random_integers(0, nrows, size = resamples)
  resampled_c = c_container[indexes, :]
  hit = len(resampled_c[:,2] == 1)
  
  return hit / resamples

def convergenceDiag(mean_vec):
  est = mean_vec[-1]
  res = abs(est - mean_vec) 

  return res

#proba

  