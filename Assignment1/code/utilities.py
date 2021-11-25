import numpy as np
import pandas as pd
import random as rd
import matplotlib.pyplot as plt
import math 

def bootstrapMandelbrot(c_container, resamples):
  """Bootstrap method to resample the previously sampled complex numbers and calculate the mean area according to that

  Parameters
  ----------
  c_containers : numpy array
     Numpy array containing the complex numbers we sampled from the differt methods
  resamples : int
      Number of resamples

  Returns
  -------
  float: 
    Estimate of the area of the Mandelbrot based on the resamples. 
     
  """
  nrows, ncols = c_container.shape
  indexes = np.random.random_integers(0, nrows, size = resamples)
  resampled_c = c_container[indexes, :]
  hit = len(resampled_c[:,2] == 1)
  
  return hit / resamples

def convergenceDiag(mean_vec):
  """Monte Carlo simulation function for the Mandelbrot set

  Parameters
  ----------
  mean_vec : numpy array 
    Numpy array containing the means we calculated from the differt methods
  
  Returns
  -------
  res: 
    numpy array: Difference between the last estimate and all other estimates in the array.
     
  """
  est = mean_vec[-1]
  res = abs(est - mean_vec) 

  return res

#proba

  