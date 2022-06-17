#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas


# In[5]:


df = pandas.read_csv("sfo.csv")
print(df)


# In[6]:


df.columns


# In[7]:


df.shape


# In[8]:


df.head(5)


# In[9]:


df.tail(2)


# In[10]:


print(df['temperature'].max())


# In[11]:


print(df[df['temperature'] == df['temperature'].max()])


# In[12]:


print(df.describe())


# In[13]:


print(df.set_index('day', inplace=True)) #to replace original data frame with new index
print(df)


# In[14]:


df


# In[15]:


df.loc['01-06-2018']


# In[16]:


df.iloc[:,2]


# In[17]:


df.iloc[1:5,2] # n+1


# In[20]:


print(df.reset_index(inplace = True)) #reset index


# In[21]:


df


# In[22]:


print(df[['event','day','temperature']])


# In[23]:


#df using Dictionry
import pandas
weather_data = {
    'day':['1/2/2018','1/2/2018','1/3/2018'],
    'temperature':[32,34,36],
    'windspeed': [6,7,8],
    'event': [ 'rain','sunny','snow']
}
df = pandas.DataFrame(weather_data)
print(df)


# In[24]:


#df using tuple

import pandas
weather_data = [
    ('1/1/2018',32,6,'rain'),
    ('1/2/2018',34,7,'snow'),
    ('1/3/2018',36,5,'sunny1')    
]
df = pandas.DataFrame(weather_data, columns=['day','temperature','windspeed','event'])


# In[25]:


df


# In[28]:


Sales=pandas.read_csv('fortune.csv.csv')


# In[30]:


Sales


# In[31]:


Sales.describe() # summary of all variable


# In[35]:


Sales['Rank'].describe() # summary of a variable


# In[39]:


sum(Sales.Rank.isnull()) # missing value count in a variable


# In[41]:


Sales.sample(n=10) #Take a random sample of size 10


# In[43]:


df2 = Sales.drop(["Revenue (in millions)"], axis =1) # axis 0 = rows and 1 = column
df2


# In[ ]:




