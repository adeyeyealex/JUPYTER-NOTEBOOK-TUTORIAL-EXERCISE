#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random 

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 


# In[2]:


a = 4


# In[3]:


2 == 2


# In[4]:


2 == 4


# In[5]:


a == 2


# In[6]:


a == 4


# In[7]:


b = 2


# In[8]:


c = a + b
print(c)


# In[9]:


d = a * b
print(d)


# In[10]:


a == d/b


# In[11]:


a**2


# In[12]:


item1 = 'python' 
item2 = 'is'
item3 = 'fun'
item4 = '!'
print (item1, item2, item3, item4)


# In[13]:


np.random.randint(0, 100, (5, 2))


# In[15]:


e = pd.Series([1, 3, 5, np.nan, 6, 8])
e


# In[16]:


e[0]


# In[17]:


e[3]


# In[18]:


e.dropna()


# In[19]:


def add_two_numbers(a, b):
    """
    Adds two numbers together and returns the result.
    
    params:
      a: int or float
      b: int or float
    returns:
      int or float of the sum of a and b
    """
    return a + b
add_two_numbers(2, 4)


# In[21]:


def fibonacci(x):                                
    if x > 1:                                           
        x = fibonacci(x - 1) + fibonacci(x - 2)  
    return(x)
fibonacci(12)


# In[22]:


fib = []                       
iteration = 20                 
for i in range(0, iteration):   
    fib.append(fibonacci(i))   
print(fib)


# In[23]:


x = list(range(iteration))  # create a list of x values same length as the fibonacci sequence
x


# In[24]:


plt.plot(x, fib)                  
plt.xlabel('Iteration Length')    
plt.ylabel("Fibonacci's Values")  
plt.title('Fibonacci Squence')   
plt.show()


# In[27]:


def fibo(num):               
    a, b = 0, 1              
    for i in range(0, num):  
        yield a              
        a, b = b, a + b      
        
l = list(fibo(20))           
l  
plt.plot(l)                      
plt.xlabel('Iteration Length')   
plt.ylabel("Fibonacci's Values") 
plt.title('Fibonacci Squence')   
plt.show()


# In[28]:


def fibo(num):               
    a, b = 0, 1              
    for i in range(0, num):  
        yield a              
        a, b = b, a + b      
        
l = list(fibo(20))           
l


# In[ ]:




