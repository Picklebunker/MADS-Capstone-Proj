#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import string
import re


# # Import Data

# In[2]:


user = pd.read_csv('users.csv')
user


# In[3]:


rating = pd.read_csv('ratings.csv')
rating


# In[4]:


book = pd.read_csv('books.csv')
book


# # 1. Data Preparation and EDA for dataset user

# In[40]:


# check data duplication
user.duplicated().sum()


# In[6]:


user.Age.value_counts()


# In[7]:


user.Age.describe()


# In[8]:


# age distribution before setting the age range 0-150.
user.hist(column="Age")


# In[ ]:





# In[9]:


print(f"Skewness: {user['Age'].skew()}")
print(f"Kurtosis: {user['Age'].kurt()}")


# In[10]:


#  make a new df users by selecting the users whose age are between 0 and 150.
users = user[ (user['Age']>= 0) & (user['Age'] <= 150.) ]
users


# In[11]:


# add a new column, age group, to label users' age

bins= [0,2,4,13,20,110]
labels = ['Infant','Toddler','Kid','Teen','Adult']
users['AgeGroup'] = pd.cut(users['Age'], bins=bins, labels=labels, right=False)

# add a columns: Country,State,and City, to label users' country, state, and city.

users['Country'] = users['Location'].str.split(',').str[-1]
users['State'] = users['Location'].str.split(',').str[-2]
users['City'] = users['Location'].str.split(',').str[-3]

# Process the country column to only retain alphabetic letters+space+period as no country name contain numbers, special characters
users['Country'] = users['Country'].str.replace('[^a-zA-Z\.\ ]', '')
users['State'] = users['State'].str.replace('[^a-zA-Z\.\ ]', '')
users['City'] = users['City'].str.replace('[^a-zA-Z\.\ ]', '')

# strip off the leading and trailing white spaces
users['Country'] = users['Country'] .str.strip()
users['State'] = users['State'] .str.strip()
users['City'] = users['City'] .str.strip()


# ## get df users (aga range is 0-150), after data preparation for dataset user

# In[12]:


users 


# ## users' age distribution

# In[13]:


users.hist(column="Age")


# In[14]:


users['AgeGroup'].value_counts().plot(kind='bar', title="users distribution per age group ")


# ## top 30 users countries

# In[15]:


(users['Country'].value_counts()[:30]).plot(kind='bar', title="top 30 user countries")


# In[16]:


#users.pivot_table(index='AgeGroup', columns='Country', aggfunc='size').plot.barh()


# # 2. Data Preparation and EDA for rating

# In[17]:


# check data duplication
rating.duplicated().sum()


# In[18]:


# count of book rating group by User-ID and ISBN
rating_counts = rating.groupby(['User-ID','ISBN']).size()


# In[19]:


# mean of book rating group by User-ID
rating_mean_user = rating.groupby('User-ID')['Book-Rating'].mean()
rating_mean_user


# In[20]:


# count of book rating group by ISBN
rating_count_user = rating.groupby('User-ID')['Book-Rating'].count()
rating_count_user


# In[21]:


# merge rating_mean and rating_count
user_rating = pd.concat([rating_count_user, rating_mean_user], axis=1)
user_rating.columns = ['book_rating_counts', 'book_rating']


# ## get df book rating per users after data preparation for dataset rating

# In[22]:


user_rating


# In[23]:


# check the outliers and correlation between book_rating_counts and book_rating per users
user_rating.plot.scatter(x='book_rating_counts', y='book_rating',c='Green')


# In[ ]:





# In[24]:


# mean of book rating group by ISBN
rating_mean_isbn = rating.groupby('ISBN')['Book-Rating'].mean()
rating_mean_isbn 


# In[25]:


# count of book rating group by ISBN
rating_count_isbn = rating.groupby('ISBN')['Book-Rating'].count()
rating_count_isbn 


# In[26]:


# merge rating_mean and rating_count
isbn_rating = pd.concat([rating_count_isbn, rating_mean_isbn], axis=1)
isbn_rating.columns = ['book_rating_counts', 'book_rating']


# ## get df book rating per ISBN after data preparation for dataset rating

# In[27]:


isbn_rating


# In[28]:


isbn_rating[isbn_rating['book_rating_counts']==1]


# In[29]:


# check the outliers and correlation between book_rating_counts and book_rating per users
isbn_rating.plot.scatter(x='book_rating_counts', y='book_rating',c='Red')


# # 3. Data Preparation and EDA for book

# In[30]:


# check data duplication
book.duplicated().sum()


# In[31]:


book.info()


# In[32]:


# Group by Year-Of-Publication and diognose the unnormal rows
book.groupby(['Year-Of-Publication']).count()


# In[33]:


# locate the unnormal data values
book[book['Year-Of-Publication'].isin(['DK Publishing Inc', 'Gallimard'])]
     


# In[38]:


# shift the unnormal data row to right
book.iloc[209538, :] = book.iloc[209538, :].shift()
book.iloc[220731, :] = book.iloc[220731, :].shift()
book.iloc[221678, :] = book.iloc[221678, :].shift()


# In[39]:


# groupby the Year-Of-Publication after correcting the unnormal rows
book.groupby(['Year-Of-Publication']).count()


# In[46]:


# plot the number of books by year
book.groupby(['Year-Of-Publication']).count().plot(legend=False, title = 'number of books by year')


# In[51]:


book.groupby(['Book-Author']).count()


# In[48]:


book.groupby(['Publisher']).count()


# In[ ]:




