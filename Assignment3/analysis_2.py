import numpy as np
import random as rd
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import ttest_ind

import simulated_annealing as sa

cooling_schedule = [40, 30]
iter = 10000

test_data = pd.read_csv('TSP280.csv', delimiter=',')
test_data = test_data.iloc[:, 1:]

city_route_test = test_data.to_numpy()

sample_sqrt = 10

len1 = 99
len2 = 99
b_x_lower = 1 #lower boundary of x axis
b_y_lower = 1 # lower boundary of y axis

c_cooling = []
c_res = []
counter = 0
for i in range(sample_sqrt):
  for j in range(sample_sqrt):
    counter = counter+1
    a_ran = np.random.uniform(b_x_lower + i * len1 / sample_sqrt, b_x_lower + (i + 1) * len1 / sample_sqrt )
    b_ran = rd.uniform(b_y_lower + j * len2 / sample_sqrt, b_y_lower + (j + 1) * len2 / sample_sqrt )

    cooling_schedule = [a_ran, b_ran]
    iter = 20000
    res_cooling = sa.simulated_annealing_TSP(city_route_test, cooling_schedule, iter)
    c_res.append(res_cooling)
    c_cooling.append(cooling_schedule.append(sa.convergence_diag(res_cooling, 200)))
    print(cooling_schedule)

c_res_array = np.array(c_res)

c_res_df = pd.DataFrame(c_res_array)
c_res_df.to_csv("c_res_df.csv")

MSE_res = []
for i in range(100):
  MSE_res.append(sa.simulated_annealing_MSE(c_res_array[i,:], n_batches = 200))

MSE_res = np.array(MSE_res)
MSE_res_df = pd.DataFrame(MSE_res)
MSE_res_df.to_csv("MSE_res_df.csv")

c_cooling = np.array(c_cooling)
c_cooling_df = pd.DataFrame(c_cooling)
c_cooling_df.to_csv("c_cooling_df.csv")



