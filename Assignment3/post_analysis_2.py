import numpy as np
import random as rd
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import ttest_ind

import simulated_annealing as sa


c_res = pd.read_csv('c_res_df.csv')
c_res = c_res.iloc[1:, 1:]

c_res_array = c_res.to_numpy()

#calculate the the estimate and the standard deviation of each cooling
MSE_res = pd.read_csv("MSE_res_df.csv")
MSE_res_array = MSE_res.to_numpy()
x = range(100)

#ordering the results
print(np.where(MSE_res_array[:,1].min() == MSE_res_array[:,1]))
MSE_arranged = MSE_res_array[MSE_res_array[:, 1].argsort()[::-1]]

#plotting the ordered results in terms of estimate and standard deviation
plt.errorbar(x, MSE_arranged[:,1], np.sqrt(MSE_arranged[:,2]), label = "Mean and Standard deviation of the estimator")
plt.legend()
plt.xlabel("Rank of the cooling schedule")
plt.ylabel("Travel distance")
#plt.show()

#print some of the results
print(MSE_arranged[0,1])
print(MSE_arranged[-1,1])
print(MSE_arranged[0,2])
print(MSE_arranged[-1,2])