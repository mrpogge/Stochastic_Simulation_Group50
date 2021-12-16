import numpy as np
import random as rd
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import ttest_ind

#travelling salesman with simulated annealing

def distance(A, B):
  '''
  Function to calculate the distance between two points in a finite dimensional space

  Params:
    A: numpy array, numeric
      Coordinates for object A
    B: numpy array, numeric
      Coordinates for object B
  
  Return:
    dist_a_b: numeric
      distance between the two points

  '''
  diff_coordinate = A - B
  dist_a_b = np.sqrt(diff_coordinate @ diff_coordinate)

  return dist_a_b

def travel_f(route):
  '''
  Function to calculate the total distance of a route

  Params:
    route: numpy array shape(number of cities, number of dimensions)
      list of coordinates in order of the travel
  Return:
    travel_distance: numeric
      total distance travelled

  '''

  travel_distance = 0
  for i in range(1, route.shape[0]):
    travel_distance = travel_distance + distance(route[i-1, :], route[i, :])
  
  return travel_distance


def city_selector(city_list):
  '''
  Choose a random route
  '''
  index = np.random.permutation(city_list.shape[0])
  route = city_list[index]

  return route
  
def elementary_edit(route):

  '''
  A step from a route to a neighbouring one
  '''

  index = np.linspace(0, route.shape[0] - 1, route.shape[0])
  choice_to_swap, new_place = np.random.choice(index,2)

  city_to_swap = route[int(choice_to_swap), :] 

  route = np.delete(route, int(choice_to_swap), 0)
  route = np.insert(route, int(new_place), city_to_swap, 0)

  return route
  

def simulated_annealing_TSP(city_list, cooling_schedule, iter):
  
  route = city_selector(city_list)
  markov_chain = [route]
  func_value = [travel_f(route)]
  current_route = route
  for i in range(iter):
    T = cooling_schedule[0] / np.log(i + 1 + cooling_schedule[1])
    prop_route = elementary_edit(current_route)

    #Boltzman function
    func_eval = np.exp(-1 * (travel_f(prop_route) - travel_f(current_route)) / T)
    alpha = min(1, func_eval)
    u = np.random.uniform(0,1)

    if alpha > u:
      current_route = prop_route
      markov_chain.append(current_route)
    else:
      markov_chain.append(current_route)

    func_value.append(travel_f(current_route))
    # if i % 1000 == 0:
    #   plt.hist(func_value)
    #   plt.show()
    #   plt.pause(0.01)

  return np.array(func_value[1:])


def simulated_annealing_MSE(func_value, n_batches):

  if len(func_value) % n_batches !=0:
    raise ValueError("Choose the number of batches that the length of the function value vector is mod 0")

  r = len(func_value) / n_batches 

  Y_b = []
  for b in range(n_batches):
    aux = func_value[int(b * r) : int((b+1) * r)]
    aux = sum(aux) / r
    Y_b.append(aux)
  
  #estimate and sample variance
  estimate = sum(Y_b)/n_batches
  s_variance = 1 / (n_batches - 1) * sum((Y_b - estimate)**2)

  return estimate, np.sqrt(s_variance)

def convergence_diag(func_value, n_batches):

  if len(func_value) % n_batches !=0:
    raise ValueError("Choose the number of batches that the length of the function value vector is mod 0")

  r = len(func_value) / n_batches 

  Y_geweke = []
  for b in range(n_batches):
    aux = func_value[int(b * r) : int((b+1) * r)]
    Y_geweke.append(aux)

  #convergence diag 
  converged_batch = Y_geweke[-1]
  Y_geweke.pop()
  ttest_res = []
  for b_g in range(len(Y_geweke)):
    ttest_res.append(ttest_ind(Y_geweke[b_g], converged_batch)[1])

  ttest_res = np.array(ttest_res)
  ttest_res_min = np.where(ttest_res > 0.05)

  try:
    ttest_res_min = np.min(ttest_res_min) * r
  except ValueError:  #raised if array is empty.
    ttest_res_min = len(func_value)

  

  return ttest_res_min
