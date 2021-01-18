#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[22]:


df = pd.read_csv('C:\\Users\\lx_fe\\Desktop\\DATA SCIENCE CLASS MATERIALS\\day.csv')


# In[23]:


df


# In[ ]:


df.head()
df.describe()


# In[31]:


df['cnt'].mean()


# In[33]:


df['cnt'].std()


# In[40]:


df.plot(kind='hist', x='instant', y='cnt', color='blue')
plt.show()


# In[ ]:




