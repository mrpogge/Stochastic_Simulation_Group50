import numpy as np
from numpy.core.fromnumeric import shape
import pandas as pd
import random as rd
import matplotlib.pyplot as plt
import math

import mandelbrot_functions as ms
import utilities as util

s = 100489
proc = 100

stats_MC = np.zeros(shape = (s+1, proc))
stats_LHC = np.zeros(shape = (s+1, proc))
stats_OS = np.zeros(shape = (s+1, proc))

for reps in range(proc):
    stats_MC[:, reps] = ms.mandelbrotMC(s, 2000)[0]
    stats_LHC[:, reps] = ms.mandelbrotLHC(s, 2000)[0]
    stats_OS[:, reps] = ms.mandelbrotOS(round(np.sqrt(s)), 2000)[0]

df_stats_MC = pd.DataFrame(stats_MC)
df_stats_LHC = pd.DataFrame(stats_LHC)
df_stats_OS = pd.DataFrame(stats_OS)

df_stats_MC.to_csv("df_stats_MC.csv")
df_stats_LHC.to_csv("df_stats_LHC.csv")
df_stats_OS.to_csv("df_stats_OS.csv")
