import numpy as np
import random as rd
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import ttest_ind

import simulated_annealing as sa

test_data = pd.read_csv('TSP280.csv', delimiter=',')
test_data = test_data.iloc[:, 1:]

city_route_test = test_data.to_numpy()

optimal_cooling = [53,78]
samplesize = 100
iter = 20000

func_container = np.zeros(shape = (samplesize, iter))
for i in range(samplesize):
  res_conv = sa.simulated_annealing_TSP(city_route_test, optimal_cooling, iter)
  func_container[i,:] = res_conv

convergence_res = np.array(func_container)
convergence_res_df = pd.DataFrame(convergence_res)
convergence_res_df.to_csv("convergence_res_df.csv")

