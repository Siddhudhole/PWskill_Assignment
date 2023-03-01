#!/usr/bin/env python
# coding: utf-8

# Q1. List any five functions of the pandas library with execution.

# ANS :  
#     
# 1) head()
# 
# 2) tail()
# 
# 3) dtypes
# 
# 4) columns
# 
# 5) describe()
# 
# 6) drop()
# 
# 7) fillna()

# In[2]:


import pandas as pd 


# In[7]:


data = {'key1':[1,2,3,4,5,6,7,8,9,10],
       'key2':[1,2,3,4,5,6,7,8,9,10]} 


# In[8]:


df = pd.DataFrame(data)


# In[9]:


df.head()


# In[10]:


df.tail()


# In[11]:


df.dtypes


# In[12]:


df.columns


# In[13]:


df.describe()


# Q2. Given a Pandas DataFrame df with columns 'A', 'B', and 'C', write a Python function to re-index the
# DataFrame with a new index that starts from 1 and increments by 2 for each row.

# In[36]:



def reindex_dataframe(df):
    df = df.reset_index(drop=True)
    df.index = df.index * 2 + 1
    return df 


# In[37]:


df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})


# In[38]:


df = reindex_dataframe(df)


# In[39]:


df


# In[40]:


df.index


# Q3. You have a Pandas DataFrame df with a column named 'Values'. Write a Python function that
# iterates over the DataFrame and calculates the sum of the first three values in the 'Values' column. The
# function should print the sum to the console.

# In[55]:


def fun(x):
    add = 0 
    for i in :
        add= add + i 
        
    return add
    


# In[51]:


Q3. You have a Pandas DataFrame df with a column named 'Values'. Write a Python function that
iterates over the DataFrame and calculates the sum of the first three values in the 'Values' column. The
function should print the sum to the console.


# In[52]:


df3 = pd.DataFrame(data3)


# Q4. Given a Pandas DataFrame df with a column 'Text', write a Python function to create a new column
# 'Word_Count' that contains the number of words in each row of the 'Text' column.

# In[63]:


def count_word(df):
    df['word_cout']=df['Text'].apply(lambda x :len(x))
    return df 


# In[64]:


df = pd.DataFrame({'Text':['siddhu','dhole','kapil','kamble']})


# In[65]:


df = count_word(df)


# In[66]:


df


# How are DataFrame.size() and DataFrame.shape() different?

# ANS : 
#     
# DataFrame.size :- returns the total number of elements in the DataFrame, which is equal to the number of rows multiplied by the number of columns. The returned value is an integer.
# 
# 
# DataFrame.shape:- returns a tuple that contains the number of rows and columns in the DataFrame, respectively. The returned value is a tuple of integers.

# Q6. Which function of pandas do we use to read an excel file?

# Ans : pd.read_excel()

# Q7. You have a Pandas DataFrame df that contains a column named 'Email' that contains email
# addresses in the format 'username@domain.com'. Write a Python function that creates a new column
# 'Username' in df that contains only the username part of each email address.

# In[3]:


df =pd.DataFrame( {'Email':['siddhu@domain.com','suma@domain.com','kaipl@domain.com']})


# In[4]:


df


# In[21]:


def username():
    
    df['Username'] = df['Email'].apply(lambda x: x.split('@')[0])


# In[22]:


df['Username']


# In[23]:


df


# Q8. You have a Pandas DataFrame df with columns 'A', 'B', and 'C'. Write a Python function that selects
# all rows where the value in column 'A' is greater than 5 and the value in column 'B' is less than 10. The
# function should return a new DataFrame that contains only the selected rows.

# In[15]:


import numpy as np 

data = {"A":list(np.random.randint(0,20,10)),
       "B":list(np.random.randint(0,30,10)),
       "C":list(np.random.randint(0,40,10))}


# In[16]:


data


# In[17]:


df = pd.DataFrame(data)


# In[18]:


def fun(df):
    
    return df[(df["A"]>5 )&(df["B"]<10)]


# In[19]:


fun(df)


# Q9. Given a Pandas DataFrame df with a column 'Values', write a Python function to calculate the mean,
# median, and standard deviation of the values in the 'Values' column.

# In[20]:


df =pd.DataFrame({'Values':list(np.random.randint(1,50,10))})


# In[48]:


df['Values'].mean()


# In[71]:


def stat(df):
    mean = df["Values"].mean()
    median = df['Values'].median()
    return ("Mean =",mean,"Median =", median)
    
    
    


# In[72]:


stat(df)


# Q10. Given a Pandas DataFrame df with a column 'Sales' and a column 'Date', write a Python function to
# create a new column 'MovingAverage' that contains the moving average of the sales for the past 7 days
# for each row in the DataFrame. The moving average should be calculated using a window of size 7 and
# should include the current day.

# In[6]:


import numpy as np 
def add_moving_average(df):
    df['MovingAverage'] = df['Sales'].rolling(window=7, min_periods=1).mean()
    return df


# In[7]:


df = pd.DataFrame({"Sales":list(np.random.randint(1,100,10)),
                  "Date":list(pd.date_range(start=19-2-2023,periods=10))})


# In[8]:


add_moving_average(df)


# Q11. You have a Pandas DataFrame df with a column 'Date'. Write a Python function that creates a new
# column 'Weekday' in the DataFrame. The 'Weekday' column should contain the weekday name (e.g.
# Monday, Tuesday) corresponding to each date in the 'Date' column.

# In[15]:


df = pd.DataFrame({'Date':list(pd.date_range(1/1/2023,periods=10))})


# In[16]:


df


# In[17]:


def weekDays(df):
    df['WeekDay'] = df['Date'].dt.day_name()
    return df 


# In[18]:


weekDays(df)


# Q12. Given a Pandas DataFrame df with a column 'Date' that contains timestamps, write a Python
# function to select all rows where the date is between '2023-01-01' and '2023-01-31'.

# In[30]:


df = pd.DataFrame({'Date':pd.date_range(start='1-10-2022',end='1-2-2023')})


# In[31]:


df


# In[32]:


def select_jan(df):
    start_date = pd.Timestamp('2023-01-01')
    end_date = pd.Timestamp('2023-01-31')
    jan = (df['Date']>=start_date) & (df['Date'] <=end_date)
    return df[jan]


# In[33]:


select_jan(df)


# Q13. To use the basic functions of pandas, what is the first and foremost necessary library that needs to
# be imported?

# ANS : To use the basic functions of Pandas, the first and foremost necessary library that needs to be imported is pandas itsel

# In[ ]:




