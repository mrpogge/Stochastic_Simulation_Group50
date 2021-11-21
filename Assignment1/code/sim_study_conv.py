import numpy as np
from numpy.core.fromnumeric import shape
import pandas as pd
import random as rd
import matplotlib.pyplot as plt
import math 

import mandelbrot_functions as ms
import utilities as util

df_MC_maxiter = pd.read_csv("df_MC_maxiter.csv")
df_LHC_maxiter = pd.read_csv("df_LHC_maxiter.csv")
df_OS_maxiter = pd.read_csv("df_OS_maxiter.csv")

MC_maxiter = np.array(df_MC_maxiter)
LHC_maxiter = np.array(df_LHC_maxiter)
OS_maxiter = np.array(df_OS_maxiter)


conv_MC = np.zeros(shape = shape(MC_maxiter))
conv_LHC = np.zeros(shape = shape(LHC_maxiter))
conv_OS = np.zeros(shape = shape(OS_maxiter))

threshold_MC = []
threshold_LHC = []
threshold_OS = []

for cl in range(shape(MC_maxiter)[1]):
    conv_MC[:,cl] = util.convergenceDiag(MC_maxiter[:,cl])
    conv_LHC[:,cl] = util.convergenceDiag(LHC_maxiter[:,cl])
    conv_OS[:,cl] = util.convergenceDiag(OS_maxiter[:,cl])
    
    threshold_MC.append(np.where(conv_MC[:, cl] < 0.001)[0][0])
    threshold_LHC.append(np.where(conv_LHC[:, cl] < 0.001)[0][0])
    threshold_OS.append(np.where(conv_OS[:, cl] < 0.001)[0][0])



plt.show()

#threshold_MC = np.array(threshold_MC)
#threshold_LHC = np.array(threshold_LHC)
#threshold_OS = np.array(threshold_OS)

#print(np.where(threshold_MC == min(threshold_MC)))
#print(np.where(threshold_LHC == min(threshold_LHC)))
#print(np.where(threshold_OS == min(threshold_OS)))

df_conv_MC = pd.DataFrame(conv_MC)
df_conv_LHC = pd.DataFrame(conv_LHC)
df_conv_OS = pd.DataFrame(conv_OS)

df_conv_MC.to_csv("df_conv_MC.csv")
df_conv_LHC.to_csv("df_conv_LHC.csv")
df_conv_OS.to_csv("df__conv_OS.csv")



