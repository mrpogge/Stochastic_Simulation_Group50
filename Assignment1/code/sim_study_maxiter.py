import numpy as np
import pandas as pd
import random as rd
import matplotlib.pyplot as plt
import math 

import mandelbrot_functions as ms
import utilities as util

#setting s to 5041
#iterating max_iter in 1 to 10000 by 10 
#doing this procedure 100 times

s = 4096
proc = 100
max_iter_i = range(1, 10000, 10)

mean_resultsMC = np.zeros(shape = (s+1, len(max_iter_i)))
mean_resultsLHC = np.zeros(shape = (s+1, len(max_iter_i)))
mean_resultsOS = np.zeros(shape = (s+1, len(max_iter_i)))


for max_i in range(len(max_iter_i)):
  mean_resultsMC[:, max_i-1] = ms.mandelbrotMC(s, max_iter_i[max_i])[0]
  mean_resultsLHC[:,max_i-1] = ms.mandelbrotLHC(s, max_iter_i[max_i])[0]
  mean_resultsOS[:,max_i-1] = ms.mandelbrotOS(round(np.sqrt(s)), max_iter_i[max_i])[0]

df_MC = pd.DataFrame(mean_resultsMC)
df_LHC = pd.DataFrame(mean_resultsLHC)
df_OS = pd.DataFrame(mean_resultsOS)

df_MC.to_csv("df_MC_maxiter.csv")
df_LHC.to_csv("df_LHC_maxiter.csv")
df_OS.to_csv("df_OS_maxiter.csv")




