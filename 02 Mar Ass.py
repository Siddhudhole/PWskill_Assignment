#!/usr/bin/env python
# coding: utf-8

# Q1: What is Matplotlib? Why is it used? Name five plots that can be plotted using the Pyplot module of
# Matplotlib.

# ANS :- 
#     
# Matplotlib is a Python data visualization library that provides a wide range of tools for creating high-quality static, animated, and interactive visualizations in Python. It is widely used in scientific computing, data analysis, and machine learning applications. Matplotlib provides a wide range of customizable 2D and 3D plots, including line plots, scatter plots, bar plots, histograms, pie charts, heatmaps, and many more.
# 
# Matplotlib is used for:
# 
# Exploratory data analysis (EDA): Matplotlib is commonly used to create various types of plots to visualize and explore data, such as scatter plots, histograms, and box plots.
# 
# Presentation and publication-quality graphics: Matplotlib provides a wide range of customization options, allowing users to create highly polished graphics for presentations and publications.
# 
# Machine learning: Matplotlib is commonly used in machine learning workflows to visualize training data, model performance, and validation metrics.
# 
# Five plots that can be plotted using the Pyplot module of Matplotlib are:
# 
# Line plot: A line plot is a graph that displays data as points connected by straight lines. Line plots are useful for visualizing trends and patterns in data over time.
# 
# Scatter plot: A scatter plot is a graph that displays data as a collection of points. Scatter plots are useful for visualizing the relationship between two variables.
# 
# Bar plot: A bar plot is a graph that displays data as a series of bars. Bar plots are useful for comparing data across categories.
# 
# Histogram: A histogram is a graph that displays the distribution of a continuous variable. Histograms are useful for visualizing the shape and spread of data.
# 
# Pie chart: A pie chart is a graph that displays data as a series of slices of a circle. Pie charts are useful for visualizing the proportion of data in different categories.

# Q2: What is a scatter plot? Use the following code to generate data for x and y. Using this generated data
# plot a scatter plot.

# ANS :-  scatter plot is a graph that displays data as a collection of points. Scatter plots are useful for visualizing the relationship between two variables.

# In[6]:


import numpy as np 
import matplotlib.pyplot as plt 


# In[2]:


np.random.seed(3)


# In[3]:


x = 3 + np.random.normal(0,2,50)
y = 3 + np.random.normal(0,2,len(x))


# In[4]:


x 


# In[5]:


y 


# In[7]:


plt.plot(x,y)
plt.xlabel("X - AXIS")
plt.ylabel("Y - AXIS")
plt.title("THIS IS MY SCATTER PLOT ")
plt.show()


# Q3: Why is the subplot() function used? Draw four line plots using the subplot() function.

# In[8]:


x1 = np.array([0, 1, 2, 3, 4, 5])
y1 = np.array([0, 100, 200, 300, 400, 500])


# In[9]:


x2 = np.array([0, 1, 2, 3, 4, 5])
y2 = np.array([50, 20, 40, 20, 60, 70])


# In[10]:


x3 = np.array([0, 1, 2, 3, 4, 5])
y3 = np.array([10, 20, 30, 40, 50, 60])


# In[11]:


x4 = np.array([0, 1, 2, 3, 4, 5])
y4 = np.array([200, 350, 250, 550, 450, 150])


# In[14]:


fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x1, y1)
axs[0, 1].plot(x2, y2)
axs[1, 0].plot(x3, y3)
axs[1, 1].plot(x4, y4)

axs[0, 0].set_title('Line 1')
axs[0, 1].set_title('Line 2')
axs[1, 0].set_title('Line 3')
axs[1, 1].set_title('Line 4')

plt.show()


# Q4: What is a bar plot? Why is it used? Using the following data plot a bar plot and a horizontal bar plot.

# ANS :- A bar plot is a graphical representation of data that uses bars to show the relationship between different categories or groups. The bars are typically arranged vertically, with the height of each bar indicating the frequency or magnitude of the data in each category.
# 
# Bar plots are commonly used to display and compare data across different groups or categories. They can be useful in identifying trends, patterns, and outliers in data, and can be used to make comparisons between different subsets of the data.

# In[15]:


company = np.array(["Apple", "Microsoft", "Google", "AMD"])
profit = np.array([3000, 8000, 1000, 10000])


# In[16]:


plt.bar(company,profit)
plt.show()


# In[17]:


plt.barh(company,profit)
plt.show()


# Q5: What is a box plot? Why is it used? Using the following data plot a box plot.
# 
# box1 = np.random.normal(100, 10, 200)
# 
# box2 = np.random.normal(90, 20, 200)

# ANS :-  A box plot, also known as a box-and-whisker plot, is a graphical representation of data that summarizes the distribution of a dataset by displaying the median, quartiles, and outliers. The box plot consists of a box that extends from the first quartile (Q1) to the third quartile (Q3), with a line indicating the median. Whiskers extend from the box to indicate the range of the data, with any points outside the whiskers considered outliers.
# 
# Box plots are commonly used to display and compare the distribution of data across different groups or categories. They can be useful in identifying differences in the median, range, and variability of data between groups.

# In[18]:


box1 = np.random.normal(100,10,200)


# In[19]:


box2 = np.random.normal(90,20,200)


# In[21]:


data = [box1,box2]


# In[ ]:


plt.boxplot(data)

