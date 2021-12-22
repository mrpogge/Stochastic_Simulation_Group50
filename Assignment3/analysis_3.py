import numpy as np
import random as rd
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import ttest_ind

import simulated_annealing as sa

#reading in the dataframe
test_data = pd.read_csv('TSP280.csv', delimiter=',')
test_data = test_data.iloc[:, 1:]

#saving it to numpy array
city_route_test = test_data.to_numpy()

#setting the cooling according to the results of analysis_2 and post_analysis_2
optimal_cooling = [14,13]
samplesize = 100
iter = 50000

#Running a chain with fixed properties 100 times
func_container = np.zeros(shape = (samplesize, iter))
for i in range(samplesize):
  res_conv = sa.simulated_annealing_TSP(city_route_test, optimal_cooling, iter)
  func_container[i,:] = res_conv

#saving the results
convergence_res = np.array(func_container)
convergence_res_df = pd.DataFrame(convergence_res)
convergence_res_df.to_csv("convergence_res_df.csv")

