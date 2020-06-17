#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd;
import sqlalchemy as sqla;
engine = sqla.create_engine('mysql+pymysql://root:root@localhost:3306/world')


# In[3]:


country = pd.read_sql_table('country', engine)


# In[4]:


country


# In[12]:


query = '''
select A.Code,A.LifeExpectancy, B.Population from world.country A join world.city B on A.Code = B.CountryCode;
'''


# In[14]:


population = pd.read_sql_query(query,engine)


# In[15]:


population.rename(columns={'Code' : 'Codes','LifeExpectancy':'LifeExpectancy','Population':'Population'} ,inplace=True)


# In[17]:


population.to_sql(
name='population', con= engine, if_exists='append', index =False)


# In[18]:


population


# In[28]:


population[ (population['LifeExpectancy'] > 81) & (population['Population'] > 20000)]


# In[31]:


len(population)


# In[ ]:




