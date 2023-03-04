#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 


# Q1. Is there any difference in the data type of variables list_ and array_list? If there is then write a code
# to print the data types of both the variables.

# In[2]:


list_ = ['1','2','3','4','5']


# In[3]:


array_list = np.array(object=list_)


# In[4]:


array_list


# In[5]:


type(list_)


# In[6]:


type(array_list)


# Q2. Write a code to print the data type of each and every element of both the variables list_ and
# arra_list.

# In[11]:


for i in list_:
    print(type(i))


# In[8]:


for i in array_list:
    print(type(i))


# In[12]:


array_list = np.array(object = list_, dtype = int)


# In[13]:


for i in list_:
    print(type(i))


# In[14]:


for i in array_list:
    print(type(i))


# In[15]:


num_list = [ [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] ]
num_array = np.array(object = num_list)


# Q4. Write a code to find the following characteristics of variable, num_array:
# 
# (i) shape
# 
# 
# (ii) size

# In[16]:


num_array.shape


# In[19]:


num_array.size 


# Q5. Write a code to create numpy array of 3*3 matrix containing zeros only, using a numpy array
# creation function.

# In[21]:


array = np.zeros((3,3))


# In[22]:


array


# Q6. Create an identity matrix of shape (5,5) using numpy functions?

# In[23]:


identity = np.eye(5,5)


# In[24]:


identity

