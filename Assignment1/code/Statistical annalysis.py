#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import numpy as np
import statistics as st
from scipy import stats
import math


# In[2]:


df_stats_MC = pd.read_csv('df_stats_MC.csv')
df_stats_OS = pd.read_csv('df_stats_OS.csv')
df_stats_LHC = pd.read_csv('df_stats_LHC.csv')


# In[33]:


end_MC = df_stats_MC.iloc[-1].tolist()
end_MC.pop(0)
means_MC = end_MC
M_MC = sum(means_MC)/len(means_MC)
std_MC = st.stdev(means_MC)
CI_MC = 0.95*(std_MC/math.sqrt(100))


# In[34]:


end_LHC = df_stats_LHC.iloc[-1].tolist()
end_LHC.pop(0)
means_LHC = end_LHC
M_LHC = sum(means_LHC)/len(means_LHC)
std_LHC = st.stdev(means_LHC)
CI_LHC= 0.95*(std_LHC/math.sqrt(100))


# In[35]:


end_OS = df_stats_OS.iloc[-1].tolist()
end_OS.pop(0)
means_OS = end_OS
M_OS = sum(means_OS)/len(means_OS)
std_OS = st.stdev(means_OS)
CI_OS = 0.95*(std_OS / math.sqrt(100))


# In[38]:


print("Monte Carlo: Mean = ",round(M_MC, 4),", CI =",round(CI_MC,6), ", S = ", std_MC)
print("Latin Hypercube : Mean = ",round(M_LHC,4),", CI =",round(CI_LHC,6),", S = ", std_LHC)
print("Ortgonal Sampling: Mean = ",round(M_OS,4),", CI =",round(CI_OS,6),", S = ", std_OS)
    

