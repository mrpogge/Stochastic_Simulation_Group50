import numpy as np
import random as rd
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import ttest_ind

import simulated_annealing as sa

convergence_res = pd.read_csv("convergence_res_df.csv")
convergence_res_array = convergence_res.to_numpy()

#calculating Geweke's convergence diagnostics
Geweke_res = []
for i in range(1,100):
  Geweke_res.append(sa.convergence_diag(convergence_res_array[i,1:], n_batches = 1000))

Geweke_res_array = np.array(Geweke_res)

#calculating the mean and the standard deviation of the runs
MSE_res = []
for i in range(1,100):
  MSE_res.append(sa.simulated_annealing_MSE(convergence_res_array[i,1:], n_batches = 100))

MSE_res_array = np.array(MSE_res)
print(MSE_res_array)

#print(MSE_res_array)
print(np.where(MSE_res_array[:,1].min() == MSE_res_array[:,1]))
MSE_arranged = MSE_res_array[MSE_res_array[:, 0].argsort()[::-1]]

est = np.mean(convergence_res_array[1:,1:], axis = 0)
error = np.std(convergence_res_array[1:,1:], axis = 0)

#plot convergence diagnostic results
plt.figure(figsize=(6, 2))
plt.title("Estimates based on repeated simulation and estimates for every iteration length.")
plt.subplot(121)
x = range(50000)
plt.plot(x, error, label = "Standard deviation")
plt.legend(prop = {"size": 15})
plt.ylabel("Travel distance", size = 20)
plt.xlabel("Number of iterations", size = 15)
plt.subplot(122)
x = range(50000)
plt.errorbar(x, est, error, label = "Estimate and Standard deviation")
plt.legend(prop = {"size": 15})
plt.xlabel("Number of iterations", size = 15)
#plt.show()

#mean and standard deviation of the smallest estimate
print(est.min())
print(error[np.where(est == est.min())])

#Printing Geweke's modified convergence diagnostics result
print(sum(Geweke_res_array < 50000)/len(Geweke_res_array))