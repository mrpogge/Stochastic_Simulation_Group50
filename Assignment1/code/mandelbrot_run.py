import numpy as np
import pandas as pd
import random as rd
import matplotlib.pyplot as plt
import math

import mandelbrot_sim as ms
import utilities as util

statsMC, valuesMC = ms.mandelbrotMC(10000, 100)