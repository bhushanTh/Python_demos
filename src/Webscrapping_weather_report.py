# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 21:35:33 2020

@author: Priyanka
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=39.118430000000046&lon=-75.55326499999995#.Xuo1BUUzZPY')
soup = BeautifulSoup(page.content,'html.parser')
week = soup.find(id='seven-day-forecast-body')

items = week.find_all(class_='forecast-tombstone')
#print(items[0])

items[0].find(class_='period-name').get_text()
items[0].find(class_='short-desc').get_text()
#items[0].find(class_='temp').get_text()

period_names = [i.find(class_='period-name').get_text() for i in items ]
short_desc = [i.find(class_='short-desc').get_text() for i in items ]
#tempr = [i.find(class_='temp').get_text() for i in items ]

#print(period_names)
#print(short_desc)
#print(tempr)
#####################
####Creating Data Frame
#####################
weather_stuff = pd.DataFrame(
    {'period' : period_names,
     'short_Description': short_desc,
     #'Temperatures': tempr
     })
weather_stuff.to_csv("C:\\Users\\HP\\Desktop\\weather_report.csv")
