# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 15:11:47 2020

@author: Bhushan

"""

import pandas as pd;
import sqlalchemy as sqla;
engine = sqla.create_engine('mysql+pymysql://root:root@localhost:3306/world')
country = pd.read_sql_table('country', engine)
country
query = '''
select A.Code,A.LifeExpectancy, B.Population from world.country A join world.city B on A.Code = B.CountryCode;
'''
population = pd.read_sql_query(query,engine)
population.rename(columns={'Code' : 'Codes','LifeExpectancy':'LifeExpectancy','Population':'Population'} ,inplace=True)
population.to_sql(name='population', con= engine, if_exists='append', index =False)