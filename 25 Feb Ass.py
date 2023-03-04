#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[2]:


course_name = ['Data Science', 'Machine Learning', 'Big Data', 'Data Engineer']
duration = [2,3,6,4]
df = pd.DataFrame(data = {'course_name' : course_name, 'duration ': duration})


# In[3]:


df


# Q1. Write a code to print the data present in the second row of the dataframe, df.

# In[4]:


df.iloc[1]


# Q2. What is the difference between the functions loc and iloc in pandas.DataFrame?

# ANS : loc is a label-based function that uses row and column labels to access data, while iloc is an integer-based function that uses the integer indices of rows and columns to access data.

# Q3. Reindex the given dataframe using a variable, reindex = [3,0,1,2] and store it in the variable, new_df
# then find the output for both new_df.loc[2] and new_df.iloc[2].

# In[5]:


df


# In[21]:



new_df = df.reindex([3,0,1,2])


# In[22]:


new_df.loc[2]


# In[23]:


new_df.iloc[2]


# ANS : The loc() function is label based data selecting method  & the iloc() function is an indexed-based selecting method

# In[24]:


import numpy as np
columns = ['column_1', 'column_2', 'column_3', 'column_4', 'column_5', 'column_6']
indices = [1,2,3,4,5,6]
#Creating a dataframe:
df1 = pd.DataFrame(np.random.rand(6,6), columns = columns, index = indices)


# In[25]:


df1 


# In[48]:


df1[df1.dtypes[(df1.dtypes=='int64')|(df1.dtypes=='float64')].index].mean() 


# In[54]:


df1[df1.dtypes[(df1.dtypes=='int64')|(df1.dtypes=='float64')].index].std()


# Q7. Write a code to print only the current month and year at the time of answering this question.
# 

# Q8. Write a Python program that takes in two dates as input (in the format YYYY-MM-DD) and
# calculates the difference between them in days, hours, and minutes using Pandas time delta. The
# program should prompt the user to enter the dates and display the result.

# In[56]:


print("PLZ enter date in the format YYYY-MM-DD")
date_1_str = input("Enter First Date :")
date_2_str = input("Enter Second Date :")
date_1 = pd.to_datetime(date_1_str)
date_2 = pd.to_datetime(date_2_str)
diff = date_1 - date_2 
diff_days = diff.days
diff_hours = diff.seconds //3600 
diff_minutes = (diff.seconds // 60 )%60 

print("Time difference :{} days, {} hours, {} minutes".format(diff_days,diff_hours,diff_minutes))


# Q9. Write a Python program that reads a CSV file containing categorical data and converts a specified
# column to a categorical data type. The program should prompt the user to enter the file path, column
# name, and category order, and then display the sorted data.

# In[1]:


import pandas as pd 


# In[3]:


path = input("Enter file Path or Name:")
data = pd.read_csv(path)
column_name = input("Enter Which column to convert inot categorical data type :")
pd.Categorical(data[column_name])


# Q10. Write a Python program that reads a CSV file containing sales data for different products and
# visualizes the data using a stacked bar chart to show the sales of each product category over time. The
# program should prompt the user to enter the file path and display the chart.

# In[ ]:



file_path = input("Enter CSV file path: ")
sales_data = pd.read_csv(file_path)


sales_pivot = pd.pivot_table(sales_data, values='Sales', index=['Year'], columns=['Category'], aggfunc=sum)


sales_pivot.plot(kind='bar', stacked=True)


plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Sales by Product Category Over Time')

plt.show()


# Q11. You are given a CSV file containing student data that includes the student ID and their test score. Write
# a Python program that reads the CSV file, calculates the mean, median, and mode of the test scores, and
# displays the results in a table.

# In[ ]:


file_path = input("Enter filepath :")
data = pd.read_csv(file_path)

mean_score = data['test_score'].mean()
median_score = data['test_score'].median()
mode_score = data['test_score'].mode()[0]

d = {'Statistic':['Mean','Median','Mode'],
    'Score':[mean_score,median_score,mode_score]}

d_df = pd.DataFrame(d)
print(d_df)


# In[ ]:




