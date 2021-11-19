import numpy as np
import pandas as pd
import random as rd
import matplotlib.pyplot as plt
import math 

import mandelbrot_sim as ms
import utilities as util

#setting s to 5041
#iterating max_iter in 1 to 10000
#doing this procedure 100 times

s = 4000
proc = 100
max_iter_i = range(1, 10000)

mean_resultsMC = np.zeros(shape = (s+1, len(max_iter_i), proc))
mean_resultsLHC = np.zeros(shape = (s+1, len(max_iter_i), proc))
mean_resultsOS = np.zeros(shape = (s, len(max_iter_i), proc))

for i in range(proc):
  for max_i in max_iter_i:
    mean_resultsMC[:, max_i-1, i] = ms.mandelbrotMC(s, max_i)[0]
    mean_resultsLHC[:,max_i-1, i] = ms.mandelbrotLHC(s, max_i)[0]
    mean_resultsOS[:,max_i-1, i] = ms.mandelbrotOS(round(np.sqrt(s)), max_i)[0]


#bootstrap alternative knowing the right max iteration
bootstrap_samples = 500
s_new = 50000
max_iter_calib = 500
mean_resultsMC_boot = np.zeros(shape = (bootstrap_samples, s_new+1))
mean_resultsLHC_boot = np.zeros(shape = (bootstrap_samples, s_new+1))
mean_resultsOS_boot = np.zeros(shape = (bootstrap_samples, s_new+1))

mean_resultsMC_boot[0, :], c_vals_MC_boot =  ms.mandelbrotMC(s_new, max_iter_calib)
mean_resultsLHC_boot[0, :], c_vals_LHC_boot =  ms.mandelbrotMC(s_new, max_iter_calib)
mean_resultsOS_boot[0, :], c_vals_OS_boot =  ms.mandelbrotMC(s_new, max_iter_calib)

for samps in range(1, s_new+1):
    for boots in range(1, bootstrap_samples):
        mean_resultsMC_boot[boots, samps] = util.bootstrapMandelbrot(c_vals_MC_boot, samps)
        mean_resultsLHC_boot[boots, samps] = util.bootstrapMandelbrot(c_vals_LHC_boot, samps)
        mean_resultsOS_boot[boots, samps] = util.bootstrapMandelbrot(c_vals_OS_boot, samps)


