#!/usr/bin/env python
# coding: utf-8

# # Random Forest Model

# In[37]:


import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error


# In[6]:


user = pd.read_csv('users.csv')
user


# In[7]:


rating = pd.read_csv('ratings.csv')
rating


# In[8]:


p = pd.merge(user, rating.rename(columns={'User-ID':'User-ID'}), on='User-ID',  how='left')


# In[9]:


book = pd.read_csv('books.csv')
df = pd.merge(p, book.rename(columns={'ISBN':'ISBN'}), on='ISBN',  how='left')
df = df.drop(columns=['Image-URL-S', 'Image-URL-M', 'Image-URL-L'])
df


# In[17]:


df1 = df[['Location','Book-Title','Book-Author','Publisher']]
str_cols = df1.columns[df1.dtypes.eq('object')]

clfs = {c:LabelEncoder() for c in str_cols}
for col, clf in clfs.items():
    df1[col] = clfs[col].fit_transform(df1[col])
df1
        


# In[32]:


df2 = df[['Age','Book-Rating']]
df3 = df1.join(df2)

df3 = df3[~df.isin([np.nan, np.inf, -np.inf]).any(1)]
#r = [x for x in df3['ISBN'] if str(x).endswith(('x','X'))]
#df4 = df3[~df3.ISBN.isin(r)]
#df4.info()
df3


# In[39]:


X = df3.iloc[:, :5]
y = df3['Book-Rating']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[40]:


rf = RandomForestRegressor(n_estimators = 50,  max_depth = 5).fit(X_train, y_train)


# In[41]:


prediction = rf.predict(X_test)
mse = mean_squared_error(y_test, prediction)
rmse = mse**.5
print(mse)
print(rmse)


# In[ ]:





# In[ ]:





# In[ ]:




